---
title: What does the "Unsubscribe Reason" mean in my Contacts export?
source: https://help.rasa.io/what-does-the-unsubscribe-reason-mean-in-my-contacts-export
keywords: delivery,Email,deliverability,contacts,subscribe,unsubscribe
---

Once you have exported your contact list, you can access insights regarding the reasons behind someone's decision to unsubscribe from your newsletter. You will encounter several options when reviewing this information under the column titled " Unsubscribe Reason".

**Bounce**: This indicates a permanent failure to deliver the email due to specific conditions within the recipient's mail server.

**Unsubscribed**: This denotes individuals who have opted out by using the unsubscribe link found in the footer of your newsletter

**API**: Unsubscribes that were initiated manually either through the dashboard or by utilizing an integrated platform.

**Dropped**: This scenario is similar to a bounce, occurring when our email service provider has previously attempted to send emails to a particular address and has repeatedly encountered bounces, invalid email addresses, or spam reports. In this case, the email will be "dropped" to safeguard the sender's reputation.

**SoftBounce**: If an email has bounced consecutively for 5 newsletters sends or more, the contact will be automatically unsubscribed.

**Admin UI / UI**: If an email address was manually unsubscribed from your rasa.io dashboard Contacts tab.   
  
**One Click Unsubscribe**: Per new [Google and Yahoo bulk sender requirements](https://learn.microsoft.com/en-us/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/stay-compliant-one-click-unsubscribe-emails), subscribers must have an option to unsubscribe with one click via code in the header of the email. All rasa.io templates are equipped with this code and you are able to view those who used that specific unsubscribe method on your export.   
  
**CSV**: If an email was unsubscribed via CSV file import using the [Bulk Unsubscribe feature](https://help.rasa.io/bulk-unsubscribe-contacts).   
  
**Spam Report**: If an subscriber marked your newsletter as spam, they will be automatically unsubscribed.   
  
**Other or blank**: If a contact has unsubscribed prior to 2020, we may not have the Unsubscribe Reason data available as we were not tracking that detail at the time.   
  
Please see below for an example of what you would see when looking for the Unsubscribe Reason in a Contact Export.

|  |  |  |
| --- | --- | --- |
| Active | Subscribed | Unsubscribed Reason |
| TRUE | FALSE | Unsubscribed |
| TRUE | FALSE | API |
| TRUE | FALSE | Bounce |
| TRUE | FALSE | Dropped |
