import logging
import os
from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    AutoSubscribe,
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
    metrics,
    RoomInputOptions,
)
from livekit.plugins import (
    cartesia,
    openai,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel


load_dotenv(dotenv_path=".env")
logger = logging.getLogger("voice-agent")


class Assistant(Agent):
    def __init__(self) -> None:
        # This project is configured to use Deepgram STT, OpenAI LLM and Cartesia TTS plugins
        # Other great providers exist like Cerebras, ElevenLabs, Groq, Play.ht, Rime, and more
        # Learn more and pick the best one for your app:
        # https://docs.livekit.io/agents/plugins
        super().__init__(
            instructions="You are a friendly and efficient restaurant order-taking assistant. Your goal is to help customers place their orders accurately. "
            "Greet the customer warmly, ask them what they would like to order, and you can suggest popular items if they ask. "
            "Repeat the order back to the customer for confirmation before finalizing. "
            "Keep your responses concise and clear.",
            stt=deepgram.STT(api_key="a8381f8a632058ebfb736a3ad364d968bc6a7690"),
            llm=openai.LLM(model="o3-mini"),
            tts=cartesia.TTS(api_key="sk_car_oaVwZk3QXXz9ium4FDUwjr"),
            # use LiveKit's transformer-based turn detector
            turn_detection=MultilingualModel(),
        )

    async def on_enter(self):
        # The agent should be polite and greet the user when it joins :)
        self.session.generate_reply(
            instructions="Hey, how can I help you today?", allow_interruptions=True
        )


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logger.info(f"starting voice assistant for participant {participant.identity}")

    usage_collector = metrics.UsageCollector()

    # Log metrics and collect usage data
    def on_metrics_collected(agent_metrics: metrics.AgentMetrics):
        metrics.log_metrics(agent_metrics)
        usage_collector.collect(agent_metrics)

    session = AgentSession(
        vad=ctx.proc.userdata["vad"],
        # minimum delay for endpointing, used when turn detector believes the user is done with their turn
        min_endpointing_delay=0.5,
        # maximum delay for endpointing, used when turn detector does not believe the user is done with their turn
        max_endpointing_delay=5.0,
    )

    # Trigger the on_metrics_collected function when metrics are collected
    session.on("metrics_collected", on_metrics_collected)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # enable background voice & noise cancellation, powered by Krisp
            # included at no additional cost with LiveKit Cloud
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
        ),
    )
