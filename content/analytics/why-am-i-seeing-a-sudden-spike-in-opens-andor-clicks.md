---
title: Why am I seeing a sudden spike in opens and/or clicks?
source: https://help.rasa.io/why-am-i-seeing-a-sudden-spike-in-clicks
keywords: suspect cliks,suspect,inflated
---

If you’re seeing a sudden spike in **opens or clicks** that looks a bit too good to be true... it’s probably a bot. Email security bots often scan links, images, and content to check for safety, which can lead to inflated **open rates** or an unexpected burst of clicks. These automated systems can trigger false positives, making your engagement numbers look better than they actually are. But don’t worry—there are ways to dig deeper and figure out exactly who (or what) might be behind the surge.

###### What Are Suspect Opens and Clicks?

Suspect opens or clicks are inflated engagement metrics typically caused by automated systems rather than actual users interacting with your content. These can be triggered by security software, such as spam filters or firewalls, scanning the content of your emails for any potentially harmful links or attachments.

###### Why Am I Seeing This Spike?

The influx of **opens or clicks** is usually traced back to one or a few specific domains. These domains belong to email servers or corporate security systems that scan emails before delivering them to the inboxes of their recipients. While this scanning process is intended to protect users, it can result in inflated engagement metrics that do not reflect actual user interactions.

How to Identify a Possible Source of Suspect Clicks

To pinpoint the culprit, follow these steps:

1. **Go to the [Segmentation Report](https://dashboard.rasa.io/analytics/segmentation)** **within your newsletter analytics.**  
   This report allows you to identify which domains are responsible for the spike in **opens or clicks**. Look for unusual patterns, such as a high number of opens or clicks from the same domain or a small group of domains.
2. **Analyze the Click and Open Patterns within the [Opens/Clicks](https://dashboard.rasa.io/analytics) analytics page**.  
   Abnormalities like a large number of opens or clicks in a short period can indicate that email security bots, rather than actual users, are behind the surge.

###### Next Steps: Contact the Domain(s)

Once you’ve identified the domain(s) responsible for the suspect clicks, the next step is to reach out to them. Explain the situation and ask if they can adjust their settings or whitelist your newsletter. This will help reduce automated clicks, providing a more accurate reflection of genuine subscriber engagement.

**What to Send to the Domain to Request Whitelisting**

If you’ve identified the domain causing suspect clicks, you can reach out to their IT department to request whitelisting of your email server. Below is a template you can use:

**Subject: Request for Whitelisting [Your Organization's Name] Emails**

Dear [IT Department],

We have observed an unusually high volume of email traffic originating from your domain, which may be impacting the delivery of our communications. To help alleviate this, we kindly ask that our email server be whitelisted in your system to ensure seamless delivery of [insert your association/company name] communications.

Please release any past messages and whitelist future emails from our servers at “[insert current newsletter domain],” which use the dedicated IP addresses [ask rasa.io Support for your specific IP addresses]. This should improve the delivery of emails to your members/our subscribers and reduce the traffic issues we're encountering.

If you've already completed the whitelisting process and emails are still being filtered out, we suggest adding us to your safe sender list as an additional precaution.

Thank you for your attention to this matter.

Best regards,  
[Your Name]  
[Your Position]  
[Your Contact Information]

---

Using this template will help reduce the impact of automated clicks and improve email delivery to your audience. Be sure to reach out to **rasa.io Support** for assistance with obtaining your specific IP addresses before sending the request.

###### Preventive Measures

- **Regularly Monitor Opens and Clicks.** Make it a habit to review your analytics after each newsletter send, especially for unusual patterns.
- **Engage with Your Audience.** Keep your subscribers informed and encourage them to report any issues with receiving or interacting with your newsletters.

By following these steps, you can ensure your newsletter analytics reflect real user engagement and minimize disruptions caused by suspect clicks.
