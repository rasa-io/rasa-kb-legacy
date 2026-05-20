---
title: What do the fields in my Contacts Export represent?
source: https://help.rasa.io/what-do-the-fields-in-my-contacts-export-represent
keywords: contact export,contact management,export fields,subscriber information,subscription data,unsubscribe reasons,email engagement,bounce rate,contact tracking,contact history
---

On your [Contacts page](https://dashboard.rasa.io/contacts), you can export via the Actions button to see an in-depth view of your contacts and their interaction with your newsletter. Here are all the columns you should see in your export and what they mean.

![]()![mceclip0 (27)](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/mceclip0%20(27).png)

**ID:** internal [rasa.io](http://rasa.io/)  ID

**First Name:** contacts first name (if available)

**Last Name:** contacts last name (if available)

**Email:** contacts email address

**Subscribed:** 1 means subscribed; 0 means unsubscribed

**Unsubscribe Reason:**

- *Bounce* - A permanent failure to deliver the email, based on conditions with the recipient mail server. [rasa.io](http://rasa.io/)  will not email this address again.
- *Unsubscribed* - Opted out via the link in the newsletter footer.
- *API* - Unsubscribe was done manually via the dashboard or through a CSV upload or through another integrated platform. Changes have been made to separate API and CSV as unique unsubscribe reasons.
- *Dropped* - Similar to a bounce, if our email service provider has attempted a send to this email before and repeatedly seen bounces, invalid emails, or spam reports returned, it will "drop" it in order to protect the sender's reputation. [rasa.io](http://rasa.io/)  will          continue to send to this address until it hard bounces
- *CSV-* Unsubscribe was done through a CSV upload
- *Blank* - It is an old record or contact that was subscribed again later. An old record means the unsubscribe happened before this column was added to the export.

**Created:**  The date the contact was originally created in the dashboard

**Updated:** The date the contact was last updated. This refers to any change made to the contact.

**Referral Code:** Every subscriber has a referral code that is assigned to them. If they forward your newsletter and a new subscriber signs up, you will see the referral code in the referred by column. You will only see this if we manage your subscribe page.

**Source:** How a contact was subscribed to the newsletter

- UI- The contact was uploaded via a CSV file or manually in the dashboard
- Newsbrief- The contact was subscribed via clicking subscribe within the                    newsletter
- \_integration\_key- the contact was subscribed via an integration you have set up
- signup-page- the contact subscribed via the personalized sign-up page provided for your newsletter
- articles-page- the contact was subscribed via the top articles page provided for your newsletter
- Blank It is an old record. An old record means the subscription happened before this column was added to the export.

**Subscription Change Date:** last action date on subscription status. Either subscribed or unsubscribed.

**external \_id:** id that corresponds with your integration i.e. Mailchimp, HubSpot, etc.

**last\_click:** last date/ time contact clicks in the newsletter

**last\_newbrief:** last newsletter contact received

**last \_open:** last date/time contact opened the newsletter

**Referred by:** Each subscriber has a referral code. If they forward your newsletter and they sign up from there, you can see who it was. You will only see this if we manage your subscribe page.

**Unique clicks:** the total number of unique clicks associated with a contact since they become a subscriber

**Unique opens:** the total number of unique clicks associated with a contact since they became a subscriber

**Full\_name:** contacts full name (if available )
