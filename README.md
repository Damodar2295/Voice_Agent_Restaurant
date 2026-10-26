# Voice_Agent_Restaurant


Is look at data in some of the tables.
Uh, this tables.So this is one of the base tables. The monthly table. So here the common pattern that you will find is the CRM ID type.
Uh, the CRM ID type number. Okay. And the CRM ID. So basically CRM ID is your Salesforce ID, CRM.
ID type is the type of the ID, whether it's an asset ID, account ID, SBGPMPRP, whatever.And this type number is simply being used for partitioning. Then we have the build currency code, concurrency code and said, see 11.
Uh, the customer ID, right? That is CDS. Null because it is uh, it is .
Yeah. And. Uh, when crm id type 600, uh, how that value is being defined. 600 yeah, it's this is, this is going to be a standard value across the.
The data layer and data layer. And it is kept in one of the lookup tables. Okay. And we only have five. I mean, as a data team.
It is in one of the tables lookup tables. You mean from the standard central data warehouse. No, no no there is no only in SDF. There is this concept of CRM type number. Okay. And we as a. Internally we have defined like 600 will be mapped as a asset ID like that or 250 is mapped as a. Yes. Okay. Okay. Yes. And this was done just in case we want to partition the tables. And 
Even when consuming the data through Salesforce or wherever, if you want to keep the merge tables partitioned. We can do that. so this is CM11. Then we have the customer ID. We have the bill amounts the bill amount in USD and.The bill amount, the t the non T&E bill. So every. So in these tables we have the bill amounts and we have the corresponding bill USD forms.And every type of amount, whether it's t any non t e. That's. So this is this state code. 

Let's look at.Let's look at the fact charge volume summary. Charge volume. Monthly one having a monthly spend level. Aggregated information.
Yes. And it has aggregations at different levels.
Okay. For each month. Period of time? I mean, uh. Okay. So now if we look at.
Charge volume summary. Here we have same thing. So this is simply as of date for data. And this is the CRM ID type. This is the CRM ID, CRM ID type number for GP.
Uh, rest of the.Then we have said. customer ID.And current year month number. Last. So current year month number is basically every. Every card has a different or sorry, every account has a different cycle date. Right? So, uh.This is the current year month number as, which tells us.
What is the currentUh. This thing. So this is what the date. Cycle content or, uh. It is close to cycle date. Actually. We can get into the discussion. That will require some explanation then. So for that, basically.
Cards. Cards have a fixed cycle date, right. But that is not the case with six. MM. Right. So what we are doing is that if for a particular set.We, we are keeping a cut off date.
Okay. Or which is also called a date. For example. If there.
Is an account. Right. Uh, say a set and it has multiple cards and it has, it has had transactions. It has one transaction in the month of September. MM. Okay. But there is no fixed cycle date for that for a set.
So we wait till the 7th of October. So that.
After that we consider that cycle to be closed. So basically that is a date.
Okay. But each card it will be different right. Let's say uh for other is October. But the date is November. Then in that case, uh, which one we will take the, the latest one. The last one.
The maximum one which have a flip date. Yeah. So for card, see if card there is a transaction record in the table. That means the cycle cut has closed automatically. Okay.
But you cannot say that for certain with certainty.
That means even if you find one record in cursed, that does not mean.
That the build cycle for that set has closed in a way for all the cards under that set up closed.
Okay, so we wait till seventh of the month before we.
Consider. This cycle cut for the set to be closed.What is.Not a problem for.
So. Earlier. In earlier code base. What were we doing? We were checking the last build date.And we were considering that two year cycle.But that cycle cut date can change every every month. Correct. Month. MM. Right. And the other problem with that was that what happens if the cycle is there.
Are two cards. For one card we have one transaction record in the month of September. But for the other card we. The last transaction happened in February. MM.
Right. And then we started calculating. So we. Then we started calculating the article for one card from February and the other card from September. Correct. MM. Right. Which is incorrect. So.

How do we. Know that if there is no transaction. There is no transaction coming in for card E for the month of March. April. May. June. July.
September. MM. Okay. So we simply consider for such cards also the flip date as the.
If the transaction happened in February. So what will be the date for that card? And let's say this is September date for every account by default becomes seven.
To keep it straightforward. Seven okay. Seven.
Seven because of it's a.
So we usually keep it. Seven because for certain systems like GDR, their date is also seven. That means they don't consider any more transactions coming in. They don't expect any transactions to come in after seven of a month for the old month. Okay, okay.
And we calculate the, uh, the spend from the flip date.
For DD accounts, for which there is no transaction. There is no means 7 to 7. Will it be like, suppose I'm, uh, suppose for the month of September, right. September 7th to October 7th will be calculating.
Y for. For dormant accounts or for accounts for which there are no transactions. So that becomes a global cut off date.
Okay. Now one scenario, let's say for a set, there are two cards. Okay. Um, one having spend on August and, uh, on September is the, uh, the last date where he can pay the amount, right? One month later and the other card, which got spend in September. Uh, but the cards, uh, can be paid by the October. Now, in these two scenario. Cid will be the single one. So what will be the current date? We will take it now.

So one is August to September. Other is September to October.So I think for this we are considering something because we already have uh.
So no, no I'm getting a question. But for that we have there is something that's been done that we are considering.
Is. How are we going to take a uniform date now? Uh, because there is a overlap. There is a, uh, 2 to 2 months continuously different, uh, dates and different times. And for that's it, which will be the, uh, date we will calculate for all the cards for that, for that, we will consider, uh.
This thing.
It, it is such that the, for that seventh will not be considered.
Huh. Not considered. But what that which date we will start looking now. I mean, the latest one. 
For continuously two months there has been no transaction.
MM. Right. That means we are in October. Progress. There was no transaction. August. He did. August he did for one card. Other card transaction in September. Right. And then for other the transaction was in September. Huh. Right. But now.
If it's a uh, since we.
Found a transaction in September. It's a it's a CM 11.That means because it has a transaction, in September and.That that means it's September. Cycle was closed.
Right. Because in September. Because it's September transaction was closed. Cycle was closed. That's why there is a record in. There. Otherwise.
Build unbuilt record will not show Calculate. We will do. From the October. Is it. So two.
Other. If the cycle closed on 15th of September, then we consider that to be the cycle. 
And do other card which got closed in August cycle. Did. We will start in mid August. Is it. Or let's say after August. Uh.
So we consider that seventh date is also considered okay. I mean, it's been a while. There was logic applied to this. I will look at it again. That's why I was saying because, uh.
We. But that the whole idea of doing this was because dormant accounts and accounts, which have not had transactions even in the recent month, were getting picked up incorrectly. So.
We have to have a cut off date, after which we should not be considering transactions because.
So CM 11, it's pretty straightforward. But for. Since it becomes a problem because for sets, the. The cycle cut can change every. Every.
In. Okay. So that working. But but I'll revise this and and let you know the logic on that.One that this the above effect charge volume monthly one. Right. So here we are bringing monthly data. And with all the hierarchy. So the data volume will be very high right in this table. Because in each month and for each level of hierarchy cm 11RPGP.
N for last 36 month it will be view. If we. If for monthly, we have turned on all the levels or. Just let me check one.
It's a. It's a huge table that means. Right. But it's partitioned.64 million MCA.
170. Why. What assets to.
One. Month, 36 months. And there will be. So many assets are.
Okay, okay. 174 million Million. Okay. Um. Okay. So we can do part when we have to. Uh, look at the data. Uh. We can.
Use partition partition key. Right. Or.
And if you have the, if you want to look at it using a particular CRM ID.
Was a clustered or partitioned.
Clustered by CRM ID And CRM ID type. Okay, but this one is partitioned on. Uh. So it is partitioned on your month number.
Year month number. Okay. Along with along with CRM id id. So if you want. So see if you have clustering on CRM, ID.
Then it anyways becomes very fast along with the partition for the particular month. MM. Okay. If the CRM id is unique, then clustering alone will help.
But you have multiple CRM ID for every month month. Right. Then partitioning with CRM. I'm asking so many questions because even I'm.
Hearing it out first time. So I'm going through these tables and all. Yeah.
, can you go in left one column? Normalization tag. R normalization. What is the normal. Okay. So this is another complete.
Uh, an MCA can have transactions in different currency. MM. Right. So.
If in a particular month there is a said.
Uh, for which you have current transaction and USD and euros for.
Okay. We cannot simply add Up the amount.\
Sorry, we cannot simply add. We cannot simply add up those amounts. Correct. We have to change in a USD or some. Uh, yeah, common. If you have to have a single record, we'll have to normalize the currency. MM. Right. So how we are normalizing it is by using the account currency code. Okay. So the CRM IDs, the Salesforce account currency code for that MCA. MM. This is only this logic is only for MC for assets. We don't have any technical.

So for. So what we do is we take that MC CRM IDs account currency code and we do that normalization using the yearly exchange rate.
Okay. And then sum up then sum. Okay. So if it.
Is null means we haven't done any any normalization. It was basically in the same way all GP, SGP normalization will only happen for uh MC. Okay. Can we see any record which is MC. And this term.

 Normalization. Tag.


Uh. Currency. What is that? There is.
Uh. Single currency code. And that means. So for.


Cases where you have multiple currencies. Let's.


Look at it. There is another one called multi.


Normal time.


Can simply get all the distinct normal tag right from that.


What are there. You get. No there are just two only. Okay.


Okay. So here we have.


If we look at if we look at the.


Multiple currency code.That means.I go to the transactions. We will see different account currency. Uh.We will see different currency codes, transactions. So.

We can select any CRM ID. It will be a table.It should be a table where we are normalizing this.

Called. Mesures.And currency code zero. Okay. But it's not necessary.But there has to be multiple.The same. You have that table name handy or resource table for this?

Uh, searchable. For.Okay. The charge. Volume. Charge volume. Right. Uh.
So is it for commercial? Okay. Let.
So I have few.Let me just check.You got it right.No, no. Yeah, I got it. Okay.Can I ask one question?
 Apparently. Apparently these tables. Actually, all this transformation is done from the Informatica, right? Earlier it was in Informatica, right? And then earlier it was per spark in.
Cornerstone. And before that it was Informatica. I was I guess.So from cornerstone is simply migrated to GCP. Lumi with.The same logic.
Not with the same. But.Because we had to change the logic or. Not with the same logic, but some changes had to be done.Because earlier we were used. We used to calculate.There were certain changes that had to happen, uh, to.
Avoid incorrect roll. Okay. And also in earlier code, we didn't roll up to our PGP with. Now that you did it for PGP. Also on all hierarchies.
Yeah. Even we used to calculate. We never supplied that data. Right. We did not have RPM right. Or did we know.
Look at this. This set right. It has records in multiple currencies.
Right. We are changing it. We are changing it. And wherever we are changing it, we are applying that normalization tag. MM. As Currency.
. So if the normalization tag is multicurrency means that that that set is having or any cm 11 is having multiple transaction in a different currencies. Yeah. And then we calculated the amount. Right. What about the single currency means that all the transactions currency we are normal. Everything is in that single currency. And then we don't really care about the account currency code. But here will we will be doing the code right. Uh, changing. Yeah. We have to normalize. So here what we do is if we find multiple records for now, we find a R, s, and USD. And we will see what is the account currency. Okay, so for this one, what.

What was the account currency.This was.Account currency was USD. So we converted a r to USD and then some of. Okay. And then we added a tag over here. Then this is a multi-currency account.
Okay. Then there was some change that that had happened. Okay. And if I want to know what all currencies were there, then I have to go and check in this norm table and. Yeah, I think initially I added an aggregated an array over here.
I thought I added but I removed it. This conversion logic is like real time or we are taking some, uh, standard value because every day it changes, right? For month, maybe no annual.
Every day it changes as, uh, USD.
To any other currency conversion you are doing, right? Yes. Some other currency.
So we used the exchange rate for that. Whatever is the
Exchange rate. Okay. And this will be annual exchange rate. Annual exchange rate. 
So it doesn't keep changing every time.
Now where we find single currency code.
If I have to know what all currency, currency code word there, which table I can see.
I think I tried it here somewhere.
He will currency.Code list.Let. Items there below. Word list was there.
Are array. Aggregated list. I saw that.But I think it should be a temporary table. Temporary table. I think it's not enough.
Internal counted.It's in the. But we can add it. It's named.As a currency coming CORR.It's only temporary. Mhm.Distinguished currency code. Can you run this?I think that is.
What will this give it?  currency code. As.No. But that is given a GCB commercial. Table. But anyways, I think that can be added in the. This main final table just.
To be.Aware of that, how many currencies are there for that account? So it. Yeah. That column we can add to the normalized table. That's not a problem right.
Tables.But you got the idea right. I mean this is not like a Super important. But yeah, this can lead to incorrect calculation. So at least to minimize the the.
Incorrect reporting of. The We will have to do this. The normalization. So let's look at an example of.It. So where we just have one currency.
We are keeping it as single currency.Charging off.
So basically this is the.Concept that single currency versus multiple multi-currency.Can you go. Yes. Yes.So can I assume that same asset can have multiple or only it's in the commercial only will have that. It's only in uh for its assets don't have multiple. Yes. Yes.Just give me one moment.
So, uh. So we look at rest of the Charge volume summary.
So where are we doing this wire saving thing? 
This is encryption. So this is all. Wire. See, these are all.
Okay. I mean, I don't know whether we.I don't know if it's really called biases. If people just call it I don't.I just call it encryption. Encryption. What the underlying.
Algorithm is, is not okay. Okay, okay. This is m11 ID. But when we see encrypted. If I want to see it here can't see like write some algorithm. I have to write.
You can you will have to run a function. Okay. Uh, they given a UDF for this function. BigQuery function. Got it. Yeah. You define. Yeah.
 So yeah, we have the last, the last value or month number. That means when was the last transaction? When when was the last transaction?Made. For that account.
Okay. So if it was February.
2024. And it said what was the last value based on.Bill amount. Then the different roll in bill. Bill currency and the USD currency, right. So basically here we just have different role role of windows.
Here we have. Rollup windows.Current month USD. Current month. Bill amount. Previous year, etc.. I mean there are a lot of amounts over here and.
But basically these are the rollups at different windows and also roll ups for, uh, TNE non TNE.Then. Okay.Highest amount in the last 12 months. Lowest amount in last 12 months. Average trend. All of that.
Any questions for this table?Okay. Then we will look at the.Top of chain.Summary. Yeah.Right. Volume.And volume.Issue. Summary.Same set of columns. Except here we have the top of chain AC number top of chain AC name, AC number and SD. Write. That same concept remains the same.
And the different rollups. And thenOn top of. Okay, we are giving rank based on the amounts for aggregate at aggregated level.No, I'm just checking. Why is this current month rank and.current rank. Null. You don't have current one. It will be.Just look at on.Total count.But we're ranking at every at every level. Six month. 12 months.Um, we have, yeah, we have different ranks. We have it at uh.
You know, the, the top of chain rank is at 12.And current rank six month rank.And 12 month ranking and top of chain rank is based on current month. Now top of top of chain rank is.
Uh, that the that will be on 12 month. That within that top of chain.
Uh. What is the rank within that top of chain.o, no. Let's look at the data because there is one charge volume summary. Then there should be one charge volume top of chain also. I'll explain one. Let me just pull some good data first.So this. Is there.Serum.And equals this.s an asset. Now.
It is not 12 month here also.We will stay.Current month.
So here we have the rank.This particular SE is rank.
Is rank or this particular asset.
Is rank for this. So this is the 12 month rank.That means the top.
This particular asset has uh. Sorry. This particular said.
A maximum amount with this particular uh AC number.
Last 12 months. Okay. In the last 12 months.
It is coming against it. Are you bringing. Will be. So this is because.
11 sets also have same elements, right? Mhm. So this is just the first CM 11 that's been captured.
For CM 13. There is a separate table. This can be ignored. This is not needed. Nothing can be uh. There's nothing. Okay. Okay. So. That is 12 month. Now. To see. MM. No. TLC rank. What if you if we. I think if we open it and.
Sorry. Decrypted. This will be 11 zeros.
Okay. Instead of null. Because initially we had kept it as zero. There was some problem that was having that we were getting in decryption in the views. So we hard coded the value to 110 so that at least the decryption. If this is of no relevance.
To sit.In this table. Mhm.
Got it. Now. Can we discuss on.
The rank part. Huh. So that is now number. See. So we have three types of ranks here. We have 126 month and current month. Okay.
So this same as SC was was also the top ranking SC in the last six months.
Okay. But not in the last in the.
Current month. In current month, the top ranking was this one.
Okay. Okay. Now let's look at the same account in the top of chain SC. But one question. What is TOC SC rank in this table? Okay. So this is for the individual SC the child. SC huh. Okay. Now let's look at the top of chain.
Top of chain.
In the top of chain.
S this table lists the individual SC along with the top of the list. Right. So here we see the individual SC name and the parent SC name.
And global is a parent SC name.
Here. And here we are simply indicating what is the rank of the top of chain.


Where top of this is in this table. Top of SC summary table.


Rank of top of chain. So anything which is rolling. Previous rolling. All these are based on the top of chain chain rank. Correct. No.


No. C one table holds only top of chain.This one. This is your holds only top of chain.

The other one holds the SC level. The the child rank also. So one top chain can have ten AC. Or five.
AC. The other one is more granular. It is showing me five child SC level ranks.


Okay. Okay. So my first. Along with that, along with that, it is also showing the top of chains.


Ranking. From the other table.


Okay. That is not getting.


It. Huh. It.I know, I know. I'll explain what the today's problem is and how we are addressing it today. So see one table.
Every every supplier has a has a hierarchy. Okay. In this case, a degree of global is the top of chain. The parent is.
One SC, top of chain SC or the parent SC or parent merchant can have multiple child merchant right. The top of chain SC is showing how much and account.


Uh NCA spend against the top of chain SC and where do different top of chain C right.


MM.


The other.So this table. Okay. Okay. Huh. Hold on please. So this table top of chain SC summary.

Is showing all this summary. This spend amount based on the top of chain SC. Is this correct. This previous year all those things. Okay. Can you scroll in right once. MM. For this in this, uh table only just want to see.
Okay. So it doesn't have anything. And this is a top of chain rank. Yeah. And that rank is based on the 12 month spend. 12.
Is spend, which is your, uh, current. Uh, okay. Top rolling 12. Okay. Rolling 12 spend for that particular, uh.


Top of. Chain SC only. Right. That this SC has spent this much, but on which.But on which account. So let me give you that example that Google examples. Alphabet is the parent company of Google.
Right. So basically you can have multiple. Child merchants under Google. Uh, under alphabet, it could be Google AdWords. It could be GCP cloud. It could be some.
Uh. Could be anything. Right. Babble or whatever. Those are individual license. Your alphabet is a top of chain. MM. This table is giving you. Where does alphabet rank with a merchant with a buyer. Whether.
It it it it ranks one.Two. Three. Whatever.
There is a buyer information here. 11 is.


A buyer? No. See. Same 11.11 MC. This is MC MC. There is MC it is. It.


So.


It.So it is then the corresponding MC right. So that is. Why. Now we want to know.
Give me all of the. How does a particular asset rank or sorry a particular MC rank within the child merchants of alphabet.Then you go to the other table.
Split. Break for each. Um.Under that top TOC. Right. Now, when you have to display this information on the UI. MM.
How we display it is that. First we display alphabet.


Then there is a tree which expands and it shows the child merchants of alphabet. MM.

Then there is another top of chain. Say it could be Hilton hotels. And it shows the individual hotels of Hilton. Got it. Merchandising right. If we use the second table. MM.
If we. Use the second table we can easily draw that tree.Where is that second table one is this fact charge volume ptosis sec. Summary. Other table is.
SEC summary one is top of chains SC. Summary. The other is SC summary SC summary. Okay okay. Yeah.
SC summary is the most useful because with that we can get.
Both ranking.


MM. Now in SC summary. What is a TOC rank.
SC. Is in S.


It tells you whether Google was above Hilton or Hilton was above Google.
Okay. So let's see this example here. Top of rank one is for which SC name.Can you please uh, left scroll it to left.
So I want to see the SC name. What was the SC name for this top one.And this is uh, this one is this one.
Okay. These are all parentheses. Parent SC now if we check in the SC now in each parent SC can can have multiple child. Mhm.


Where do those child S's rank.If they've spent with this particular NC. If this MC has spent with child. SC so Adagio global has a child. SC.
Called. New city Appart hotel.Okay. And uh, this is the child. SC now this top of the Adagio could also have.No, for Adagio it will be the top SC rank will be one in this SC summary table. Right.
Okay.You see, SC rank will be equal to one for Adagio. In SC summary table in this table. Correct. No. It can also repeat uh repeat all.


So wherever it is. Wherever the parent is it argue it will repeat. It will repeat. And this is based here in this table TOCS rank. And this is the green that I got it TOC SC rank will be on again rolling 12 only in SC. SC is rolling 12 in.


Both the tables. Yeah.So when we use this table SC rolling 12 monthly rank will be used with TOC rank not these two.
Okay. So the client view but SC once again SC rolling 12 month rank can be different with TOC rank right. Because SC rolling 12 month will be your normal SC but TOC will be on your top of.
You said TOC.
And SC rolling 12 month rank will be same. No right. It cannot be same. No.


Not necessarily.Because SC rolling month is on your child. SC right but TOC will be your top of chain rank which is.Top of chain 12 month summary.
MM. So these can be different.


Okay. So basically the idea is one is holding the individual. One is holding the top of chain rank. You don't have to read both of them together. You can leave out the TOC rank in the SC summary table. That is only for easy consumption of. In the listing. Okay. In if. If in client. We have to directly pull this data and display that graph that tree. We can do it easily.

This table is only meant for individual license. One is meant for top of chain. One is. One is meant for this.
