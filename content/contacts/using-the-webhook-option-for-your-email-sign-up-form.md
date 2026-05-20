---
title: Using the Webhook Option for Your Email Sign-Up Form
source: https://help.rasa.io/using-the-webhook-option-for-your-email-sign-up-form
keywords: contacts,integrations,webhook,API
---

_To seamlessly add new contacts to your newsletter via our webhook option, follow these steps. This guide will walk you through the process of using our API to sign up users._

###### Step 1: Locate Your `<guid>`

1. **Login to your account.**
2. **Navigate to the 'Tools' page.**
3. **Find the 'Sign Up' form link.** The `<guid>` will be part of this URL. It will look like this:

![](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/image-png-Jul-19-2024-03-23-56-9097-PM.png)

###### Step 2: Prepare Your API Call

Use the following API call format to add a contact to your newsletter. You will need to send a POST request to our API with the payload containing the contact's information.

###### API Call Information

**Endpoint URL: https://public-api.rasa.io/signup/**<guid>

**Payload:  
`{`  
`"email": "john.doe@example.com",`  
`"first_name": "John",`  
`"last_name": "Doe"`  
`}`**

###### Example

Here is an example of how your POST request might look in Python using the `requests` library:

![](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/image-png-Jul-19-2024-03-26-23-0030-PM.png)

###### Step 3: Implement the Webhook in Your Form

Integrate this API call into your email sign-up form's backend logic. Ensure your form captures the user's `email`, `first_name`, and `last_name`, and then sends this data to the API endpoint in the correct format.

###### Troubleshooting

- **Invalid `<guid>`**: Make sure you copied the `<guid>` correctly from your 'Tools' page.
- **Incorrect Payload**: Ensure the payload format matches the required structure.
- **Network Issues**: Check your internet connection if the API call fails.

For further assistance, please contact our support team.
