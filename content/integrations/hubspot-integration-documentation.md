---
title: HubSpot Integration Documentation
source: https://help.rasa.io/hubspot-integration-documentation
keywords: integrations,user engagement,hubspot,hubspot integration,contact selection,static list,dynamic list,subscription type,two-way integration,engagement data,real-time updates,custom contact fields,API integration,reporting dashboard,email marketing integration
---

###### Contact Selection

rasa.io supports two methods of acquiring contacts from HubSpot:

- **List**: (static or dynamic): directly defining the contacts to include

- **Subscription Type:** Select the subscription type that describes which contacts have opted in to receive mailings.

We ***highly*** recommend using List AND Subscription Type to sync your contacts from HubSpot. That is best practice.

Think of the list of who is **eligible**to receive the newsletter and the subscription type as a way to identify that contact's **preference**(opted-in or out). The list basically keeps the contact in rasa so you can always look up how or why someone unsubscribed and see that audit trail whereas if you only use one method, as soon as they unsubscribe we'd take them out of rasa because they are no longer going to show as someone who should be included in HubSpot.

Prior to integration, you should select your method of integration and establish the necessary data inside your HubSpot instance.

###### 🧾 Quick Comparison Table

Compare the **unsubscribe scenario** across all three setups so you can see the differences clearly:

| Sync Method | HubSpot Subscription Updated? | Contact stays visible in rasa.io? | Best Use Case |
| --- | --- | --- | --- |
| **Subscription Type only** | ✅ Yes | ❌ No (removed after sync) | Pure preference tracking |
| **List only** | ❌ No | ✅ Yes (marked unsubscribed) | Audit-focused, not recommended alone |
| **List + Subscription Type** | ✅ Yes | ✅ Yes | ✅ Best practice |

###### **List**

When a List is selected for integration, rasa.io does not attempt to remove unsubscribed contacts from the list (as rasa.io has no insight into what attributes were used to build the list).  If 2-way integration is selected, a contact field will be updated to reflect that the user has unsubscribed, but that user will remain in the rasa.io platform as an unsubscribed user.

When a contact is removed from the list (in HubSpot), that user will also be removed from the rasa dashboard.

###### **Subscription Type**

When a Subscription Type is selected for integration, when [rasa.io](https://rasa.io) detects that a user should no longer receive a newsletter, the user will automatically opt out of the indicated subscription type. This will happen if any of the following occur:

- rasa.io receives a signal that the user has opted out of the newsletter
- rasa.io receives a permanent delivery failure report
- rasa.io receives a signal that the user has flagged the email as spam.

When a contact has been opted out, they will subsequently be removed from the rasa.io dashboard, as they are no longer opted in.  This means that normally, you will only see recently unsubscribed contacts inside rasa.io.  When a nightly synchronization runs, those unsubscribed contacts will be removed.

###### Important Note on Subscribed Users

In addition to adding aList and Subscription Type, each contact must also have an assigned **'legal basis'** field in HubSpot. Without set legal basis field, the contact will not be considered a subscribed user and therefore will not be added to your subscribed audience in rasa.io.

###### **Contact Updates**

When selecting a “2-way” integration, rasa.io will update the following parameters inside of HubSpot.

###### **Reporting**

If your HubSpot plan allows you to create custom dashboards with external components, you can embed your engagement data inside HubSpot by using a custom URL.  For this, you will need a GUID, provided by your CS representative.

There are 3 different forms of the URL which present the same data differently:

- [https://hubspot-ui.rasa.io/engagement/chart?c=](https://hubspot-ui.rasa.io/engagement/chart?c=e17e69fe-3b7b-120e-7d7f-9bbffba2ff0e) [guid]: Display a graph of opens and clicks
- [https://hubspot-ui.rasa.io/engagement/table?c=](https://hubspot-ui.rasa.io/engagement/chart?c=e17e69fe-3b7b-120e-7d7f-9bbffba2ff0e) [guid]: Display a opens and clicks data in a table
- [https://hubspot-ui.rasa.io/engagement?c=](https://hubspot-ui.rasa.io/engagement/chart?c=e17e69fe-3b7b-120e-7d7f-9bbffba2ff0e) [guid]: Display *both* the table and the chart

Please check out [HubSpot's article](https://app.hubspot.com/ecosystem/22539073/marketplace/apps/marketing/email/rasa-io-206230) about our integration and watch [this webinar](https://rasa.io/videos/rasa-io-hubspot-webinar/) for more information!

###### **\*Disclaimer:** The information below is only applicable to users integrated with our HubSpot rich integration.

###### **Contact Activity Timeline**

All rasa.io newsletter activities are recorded on the Activity Timeline for the Contact.

- Deliveries: A delivery event is recorded with the date/time of the delivery and the Subject Line.
- Opens: An open event is recorded with the date/time of the open and the Subject Line of the newsletter
- Clicks: A click event is recorded with the date/time of the click and the URL that was clicked on.

###### **Custom Contact Fields**

HubSpot contacts are updated with several attributes to provide insights into how a contact interacts with the rasa.io newsletter.

###### **Real-Time Updates**

These fields are populated in near-real time, as events happen

**Last Article Click**: The date/time of the last click on an article in the newsletter

**Last Click**: The date/time of the last click of any kind

**Last Delivery**: The date/time of the last newsletter delivery attempt

**Last Delivery Status**: The status of the last attempted delivery:

- Delivered: Successful delivery
- Dropped: Failed attempt to redelivery a previously Hard Bounced email address
- Soft Bounce: Temporary delivery failure.  Contact will remain subscribed.
- Hard Bounce: Permanent delivery failure.  Contact will be unsubscribed and future deliveries will not be attempted.

**Last Open**: The date/time of the last newsletter open

###### Daily Updates

These fields are updated on a daily basis

**Click Count:** The count of unique clicks from this contact

**Open Count:** The count of unique newsletter opens from this contact

**Subscription Status:** Describe whether this contact is subscribed (“Subscribed”), or if not - why not:

- API: Unsubscribed via an API integration update
- Unsubscribed: Unsubscribed by user choice/opt-out
- Bounce: Unsubscribed as a result of a delivery problem

**Subscription Status Changed:** The date/time that the Subscription Status field was updated

###### Weekly Updates

These fields are updated on a weekly basis

**Categories**: The top 10 user-specified tags for this contact.  The values are all separated by commas, to allow targeted queries and filtering.

**Engagement Level**: A numeric AI-generated measure of how engaged a user is.  Larger values indicate higher engagement.

**Engagement Update**: The date/time of the last update of the engagement level attribute

**Topics**: The AI-computed top 10 topics of interest for this contact.  The values are all separated by commas, to allow targeted queries and filtering.
