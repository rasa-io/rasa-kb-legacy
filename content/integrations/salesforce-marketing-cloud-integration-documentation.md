---
title: Salesforce Marketing Cloud Integration Documentation
source: https://help.rasa.io/salesforce-marketing-cloud-integration-documentation
keywords: salesforce integration,syncing contacts,CRM integration
---

_Our Salesforce Marketing Cloud (SFMC) integration allows you to connect your SFMC data to rasa.io for a daily sync that helps identify which contacts should receive newsletters._

###### How the Integration Works

Once connected, rasa.io will perform a one-way sync with Salesforce Marketing Cloud daily. This sync checks the audience information based on your specified criteria and updates the newsletter recipient list accordingly.

###### Required Information to Connect

To connect your Salesforce Marketing Cloud account with rasa.io, you will need the following:

1. **Client ID** (Required):  
   You can find your Client ID in Salesforce Marketing Cloud by navigating to **Setup > Apps > Installed Packages**. Click on the package you want to use, and under **API Integration > Components**, locate your **Client ID**.
2. **Client Secret** (Required):  
   The **Client Secret** is located in the same section as the Client ID. Navigate to **Setup > Apps > Installed Packages**, select your package, and find the **Client Secret** under **API Integration > Components**.
3. **Account ID** (Required):  
   Your Account ID, also known as the **MID (Member ID)**, is visible in the top right corner of the Salesforce Marketing Cloud interface when you log in. You can also find it by navigating to **Admin > Account Settings**.
4. **Subdomain** (Required):  
   The **Subdomain** is part of your SFMC instance URL. For example, if your SFMC URL is `https://mcsubdomain.exacttarget.com`, then `mcsubdomain` is your subdomain. To verify, navigate to **Setup > Administration > Account Settings**, where your instance URL should be displayed.
5. **Data Extension Key / Audience Key** (Required):  
   To find the Data Extension Key, go to **Email Studio > Subscribers > Data Extensions**. Select the Data Extension you wish to use, and the **Data Extension Key** will be displayed in the properties panel. This key uniquely identifies the Data Extension and is essential for the integration.

###### Quick Tip

The Salesforce Marketing Cloud integration is a one-way sync, meaning that rasa.io will only receive data from SFMC and will not push updates back to your Salesforce account.

###### Setting Up the Integration

1. **Navigate to Contacts > Import > Import from third party applications**  in your rasa.io dashboard.
2. **Select Salesforce Marketing Cloud** from the list of available integrations.
3. **Fill in the required fields** listed above. Make sure all information is accurate to ensure a successful connection.
4. **Save** your settings to activate the sync.

###### Troubleshooting

- **Invalid Credentials**: Double-check your Client ID, Client Secret, and Account ID. Ensure there are no extra spaces or incorrect characters.
- **Missing Data**: Ensure the Data Extension Key/Audience Key matches the exact key in SFMC. If the key doesn’t match, the sync may fail.
- **Subdomain Issues**: Ensure the correct subdomain is entered as it appears in your SFMC URL.

For any issues that persist, please reach out to our support team with the details of the error message you encounter.
