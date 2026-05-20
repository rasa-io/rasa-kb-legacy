---
title: How do rasa.io integrations work?
source: https://help.rasa.io/how-do-rasa.io-integrations-work
keywords: integrations,Mailchimp,hubspot integration,one-way integration,salesforce integration,native integrations,content integrations,two-way sync,ActiveCampaign,CRM integration,integration key,zapier
---

rasa.io supports a variety of native [integrations](https://dashboard.rasa.io/settings/integrations). Most of our integrations are related to newsletter subscriber management but we also have several content integrations.

Here is our current list of available integrations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ActiveCampaign** | **Constant Contact** | **Deskera** | **HubSpot - Rich** | **Keap** |
| **Integrately** | **Klaviyo** | **Mailchimp** | **Pabbly** | **Pipedream** |
| **Replug** | **Salesflare** | **SendFox** | **Stripe** | **SyncSpider** |
| **Zoom** | **Zapier** | **Fonteva** | **Magnet Mail** | **iMIS** |
| **LinkedIn** | **Nimble** | **Salesforce - Rich** | **YourMembership** | **Impexium** |
| **Informz** |  |  |  |  |

Below are some additional details regarding each integration.  All integration syncs run daily.

1-way sync transfers data in a single direction, while 2-way sync allows bidirectional data transfer. In contacts management, 1-way sync means changes in one system don't affect the other, whereas 2-way sync ensures updates are reflected in both systems.

![]()

![](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/Knowledge%20Base%20Import/upload.wikimedia.orgwikipediacommonsthumb33fHubSpot_Logo.svg220px-HubSpot_Logo.svg.png)

The HubSpot integration is a two-way sync. You can only sync 1 set of contacts from HubSpot to your rasa.io account. To do so, those contacts need to be part of the same List or Subscription Type. To sync all contacts, create an all-contact List in HubSpot.  
The sync can be one-way if desired.

We also have a rich HubSpot integration available for those on Pro and Enterprise plans. To learn more about it, please visit [this page](https://help.rasa.io/hubspot-integration-documentation).

![](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/Knowledge%20Base%20Import/upload.wikimedia.orgwikipediaenthumb772Mailchimp_logo.svg220px-Mailchimp_logo.svg.png)

The Mailchimp integration is a two-way sync. Please know that you can only sync 1 Audience from Mailchimp. If you would like to combine Audiences, create a custom Audience in Mailchimp then sync that Audience to your rasa.io account.  
The sync can be one-way if desired.

![Salesforce.com_logo.svg](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/Salesforce.com_logo.svg.png)

The SalesForce integration is a two-way sync but requires an ‘OptedOutRasa\_\_c’ custom field for the two-way sync. All of your Salesforce contacts will sync UNLESS you create a custom (boolean) field named "RasaNewsletter\_\_c" in Salesforce and check its box on each contact you want to sync with your rasa.io account.

The sync can be one-way if desired.

We also have a rich Salesforce integration available for those on Pro and Enterprise plans. To learn more about it, please visit [this page](https://help.rasa.io/salesforce-integration-documentation).

\*Creating a custom field in SalesForce:

![salesforce integration custom field](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/salesforce%20integration%20custom%20field.png)

![](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/Knowledge%20Base%20Import/upload.wikimedia.orgwikipediacommonsthumbffdZapier_logo.svg250px-Zapier_logo.svg.png)

[You can access the rasa.io Zap via the Zapier app library](https://zapier.com/apps/rasaio/integrations). You can generate the integration key you will need to begin Zapping between rasa.io and your other applications via the integrations page and clicking Zapier, to generate a key. Using Zapier, you can add new subscribers that come into your CRM to rasa.io. You can also bring open, click, and topic data from rasa.io into your CRM.

![]() ![](https://getvoip.com/uploads/keap-logo-700x340.png)

The integration between Keap and rasa.io is one-way. When you integrate your Infusionsoft account, you will import all customers from Infusionsoft with an email address that is opted in for marketing emails into rasa.io.

![download (2)](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/download%20(2).png)

The integration between SendFox and rasa.io is one-way. You can only sync 1 list from SendFox to your rasa.io account. To sync all contacts, create an all-contact List in SendFox.

![](https://financesonline.com/uploads/2019/12/Salesflare-Logo-3.png)

The integration between Salesflare and rasa.io is one-way. When you integrate your Salesflare account, you will import all customers from Salesflare with an email address that is opted in for marketing emails into rasa.io.

![download (4)](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/download%20(4).png)![]()

The Integration between Deskera and rasa.io is one-way. When you integrate your Deskera account, you will import all of your customers from Deskera that are opted in for marketing emails, unless you create a custom "*RasaNewsletter\_\_c"*field with a value of 0 to exclude and 1 to include. This will create a custom list of customers to import to rasa.io.

![]()![Stripe_logo,_revised_2016](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/Stripe_logo%2c_revised_2016.png)

The integration between rasa.io and Stripe is one-way. When you integrate your Stripe account, you will import all customers from your Stripe site with an email address.

![]()

![]()![replug_logo_black_text](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/replug_logo_black_text.png)

The integration between replug and rasa.io allows for custom short-form URLs. When you integrate your replug account, all articles will be linked in their replug short-form URL rather than the original form.

![activecampaign-1](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/activecampaign-1.svg)

The integration between rasa.io and ActiveCampaign is one-way. When you integrate your ActiveCampaign account, you will import all customers from ActiveCampaign with an email address that is opted in for marketing emails into rasa.io.

![]()

![download](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/download.png)

You can find rasa.io in the SyncSpider app library. You can generate the integration key you will need to integrate between rasa.io and your other applications via the integrations page and by clicking the SyncSpider, then generate a key. Using SyncSpider, you can add new subscribers that come into your CRM to rasa.io. You can also bring open, click, and topic data from rasa.io into your CRM.

![open-uri20210108-68-1ncp24r](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/open-uri20210108-68-1ncp24r.png)

You can generate the integration key you will need to integrate between rasa.io and Pipedream via the integrations page and click Pipedream, then generate a key. Using Pipedream, you can add new subscribers that come into your CRM to rasa.io. You can also bring open, click, and topic data from rasa.io into your CRM.![]()

![pabblyconnect_logo-323b23b7378b865464f570aeb9383488ee36477996233653e0575c0151aa7c54](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/pabblyconnect_logo-323b23b7378b865464f570aeb9383488ee36477996233653e0575c0151aa7c54.png)

You can generate the integration key you will need to integrate between rasa.io and Pabbly via the integrations page and click Pabbly, then generate a key. Using Pabbly, you can add new subscribers that come into your CRM to rasa.io. You can also bring open, click, and topic data from rasa.io into your CRM.

![](https://financesonline.com/uploads/2019/10/YourMembership-logo1.png)

The integration between rasa.io and YourMembership is one-way. For detailed instructions on how to set up your integration, please visit [this page](https://help.rasa.io/yourmembership-integration-documentation).

![](https://logos-world.net/wp-content/uploads/2020/04/Linkedin-Logo-2011-2019.png)

The integration between rasa.io and LinkedIn is available to use as a source to provide content. To use LinkedIn, it must be your organization's account. You can log in to your company's LinkedIn page [here](https://dashboard.rasa.io/settings/integrations/config?systemName=LinkedIn&displayName=LinkedIn) to use the integration. For more information about how sources work, please visit [this page](https://help.rasa.io/how-do-sources-work).

![The History of the Zoom Logo - Hatchwise](https://www.hatchwise.com/wp-content/uploads/2021/12/Screen-Shot-2021-12-03-at-8.16.14-AM.png)

The integration between rasa.io and Zoom is available to use as a source to provide webinars for your newsletter. You can log in to your Zoom account [here](https://dashboard.rasa.io/settings/integrations/config?systemName=Zoom&displayName=Zoom) to use the integration. For more information about how the Zoom integration works, please visit [this page](https://help.rasa.io/zoom-integration-documentation).

![](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_28e0907ae7c6011628a215b97a187ca2/imis.png)

The integration between rasa.io and iMIS is a one-way sync. The information needed to set up the integration is API Endpoint and IQA QueryName.

**For more details on the API endpoint:**  
Accessing the API endpoint

For anyone on iMIS EMS (20.3, 20/20 Advance)  
The API endpoint points to the ASI Scheduler. The endpoint format is: URL/api/endpoint  
For example, your public iMIS website URL is [https://abc.org](https://abc.org/). To call the party endpoint, the full API URL is <https://abc.org/api/party>.  
For anyone on an earlier version and not on iMIS EMS  
The endpoint format is similar to the above but includes the instance name: URL/instance name/api/endpoint  
For example, your public iMIS website URL is [https://abc.org](https://abc.org/) and the website instance name is abcmembers. To call the party endpoint, the full API URL is <https://abc.org/abcmembers/api/party>.

For the IQA QueryName, enter the IQA that returns to you the list of records that should be included in the newsletter distribution. Here is an example of an IQA: $/Rasa.io/Newsletter Integration Sync **or**$/RASA/Current\_Active\_Member

![CC_release_thumb](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/CC_release_thumb.png)

The Constant Contact integration is a two-way sync. When you integrate your Constant Contact account, you can choose a list to sync into the rasa.io dashboard. Please visit [this page](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/31720-Create-and-Manage-Contact-Lists?lang=en_US) for information about how to create and set up a list in Constant Contact.
