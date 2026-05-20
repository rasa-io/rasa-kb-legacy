---
title: What can I tell my subscribers who aren't receiving my newsletter?
source: https://help.rasa.io/what-can-i-tell-my-subscribers-who-arent-receiving-my-newsletter
keywords: delivery,deliverability,spam,newsletter delivery,whitelist email,safe senders
---

_Here is some helpful copy you can use when subscribers are having issues receiving your newsletter to their primary inbox._

Some of your subscribers may have higher email security settings in place, which can occasionally prevent your newsletters from being delivered. Below, you'll find helpful copy and specific instructions that can be used to ensure these emails are properly received. Taking these additional steps will help guarantee that your communications reach every intended inbox.

**Example Copy:**

To ensure you continue receiving our [NAME] communications, please follow the steps below. This will help your IT department or firewall administrator whitelist our email domain and IP addresses, ensuring our messages are not blocked or filtered out.

1. **Whitelist the Email Domain:**

   - Add our domain "[example.org]" to your organization’s email whitelist. This can typically be done through your email provider's settings or your organization's email gateway.
2. **Whitelist IP Addresses:**

   - Add the following IP addresses to the whitelist of your email server or firewall:
     - **[\*contact your Customer Success representative for your account's dedicated IP addresses, these can vary by customer]**
   - For most email systems, this can be done by accessing the email security or spam filter settings and entering these IP addresses under "Allowed IP Addresses" or "Safe Senders."
3. **Release Blocked Messages:**

   - If any previous communications from us have been blocked, please request that your IT department release those emails from the quarantine or blocked list.

**Instructions for Common Email Systems:**

- **Microsoft 365 (Exchange Online):**

  - Go to the **Exchange Admin Center**.
  - Navigate to **Protection** > **Connection Filter**.
  - Under **IP Allow List**, click **+** and add the above IP addresses.
  - Also, ensure that the domain "[YOUR DOMAIN]" is added under **Safe Senders** in **Mail Flow Rules**.
- **Gmail (Google Workspace):**

  - Go to **Google Admin Console**.
  - Navigate to **Apps** > **Google Workspace** > **Gmail** > **Spam, Phishing, and Malware**.
  - Under **Inbound Gateway**, add the IP addresses to the list of allowed IPs.
  - Also, add "aiaa.org" under **Spam** > **Approved Senders**.
- **Firewalls (e.g., Cisco, SonicWall):**

  - Access the firewall management interface.
  - Navigate to the **Email Security** or **Content Filtering** section.
  - Add the IP addresses to the whitelist or **Allow** list.
  - Ensure that the domain "[YOUR DOMAIN]" is also whitelisted in the **Domain** section.

If your IT team needs any additional details or has any issues implementing these steps, please don’t hesitate to reach out to us. We're here to help.
