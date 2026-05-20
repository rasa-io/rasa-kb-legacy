---
title: Connecting Informz and rasa.io
source: https://help.rasa.io/connecting-informz-and-rasa.io
keywords: Informz
---

_This page provides step-by-step instructions for integrating your Informz account with rasa.io to synchronize your contact list effectively._

###### Important First Step: Whitelist Our IP Addresses

Before you begin integrating **rasa with Informz**, please ensure that you whitelist our IP addresses. This is required so the integration can function properly without being blocked by your firewall or security settings.

**You can find the list of IP addresses by clicking on [this article link](https://help.rasa.io/ip-addresses) and using the IP addresses listed under the "Integrations" section.**

###### Required Information for Integration

To successfully connect Informz with rasa.io, you will need to provide the following details from your Informz account:

- **Brand ID** (also known as Tenant ID)
- **Username**
- **Password**
- **Encryption Key**
- **Interests**

---

###### Locating the Brand ID (Tenant ID) and Encryption Key

- The **Brand ID** is also known as the **Tenant ID** and can be found in your Informz dashboard.
  - It is located above the **Account Number** under the user icon in the top right corner of the screen.
- The Encryption Key can be found in Settings > System Settings > Informz API Configuration ![image-1](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/image-1.png)

###### Finding the Interests

- **Interests** correspond to the Target Group Name in Informz and represent the list of contacts you want to sync.
- To locate the **Interests**:
  1. Go to **Target Groups** in the Informz dashboard.
  2. Find the **Target Group Name** that has a **Type of Interests** and note the count of contacts associated with it.

---

###### Enabling the Rest API in Informz

To use the integration, you may need to enable the Rest API on your Informz account. Follow these steps if the API is not already enabled:

1. **Submit a Support Case to Higher Logic**:

   - Go to [Higher Logic Support](https://support.higherlogic.com/).
   - Create a support case with the following details:
     - **Informz Account Number**
     - **Brand ID** (Tenant ID)
2. **Request API Enablement**:

   - Ask Higher Logic Support to enable the Rest API for your account.
   - Mention that you are **not changing AMSs** but simply adding rasa.io, which may expedite the request.
3. **Provide rasa.io IP Addresses**:

   - Ensure the necessary rasa.io IP addresses are whitelisted as part of your API request.

###### Creating an API User Account

Once the Rest API is enabled:

1. Create a new user account in Informz specifically for the integration.
2. Assign **Administrator level permissions** to this user to ensure all required API calls can be made.
   - Note: While Administrator permissions are highly recommended for ease of integration, check with your team to confirm if this is a strict requirement or a helpful suggestion.

---

###### Authentication in rasa.io

After setting up your Informz account and user permissions, enter the following information into the rasa.io integration settings:

- **Brand ID (Tenant ID)**
- **Username**
- **Password**
- **Encryption Key**
- **Interests (Target Group Name)**
