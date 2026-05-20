---
title: Overview of Domain Authentication
source: https://help.rasa.io/overview-of-domain-authentication
keywords: domain authentication,email deliverability,CNAME records,DNS configuration,verification process,send from authentication,DNS entries,reputation management,spam prevention,hosting provider,email sending permissions,tracking statistics,domain verification,email service providers
---

###### What is domain authentication?

Domain authentication is the process of verifying that you own the email domain you’re sending newsletters from. This allows rasa.io to send on your behalf using your domain, instead of our default address.

When you first create an account, your newsletters will send from the generic address:  
`thiswas@sentwithrasa.io`

By authenticating your domain, you replace this generic sender with your own email domain (for example, `news@yourdomain.com`).

###### Why is this important?

- **Brand consistency:** Your readers see newsletters coming directly from your domain, not rasa.io.
- **Improved trust:** Without authentication, your emails may show “via rasa.io” in the sender line. This signals to inbox providers that the message might not truly come from you.
- **Better deliverability:** Email providers distrust unauthenticated messages. Authenticating your domain proves that you authorized rasa.io to send on your behalf, which strengthens your reputation and helps ensure your newsletters reach the inbox.
- **Lower spam risk:** When your subscribers clearly see your domain in the “from” address, they’re less likely to mark your newsletter as spam.

###### How it works

When you authenticate your domain, rasa.io provides you with multiple sets of DNS records (CNAME records) that must be added to your domain provider (e.g., GoDaddy, Google Domains, Cloudflare). These records verify that rasa.io is authorized to send email on behalf of your domain.

###### What are DNS and CNAME records?

- **DNS (Domain Name System):** Think of DNS as the internet's address book. When someone types your domain name (like animalsthatread.com), DNS makes sure they reach the right place — whether that's your website or your email service.
- **CNAME records**: A CNAME record is like giving a nickname to part of your domain. For example, if you want your newsletters to come from news.animalsthatread.com, a CNAME record tells the internet: "this subdomain is managed by rasa.io." This lets rasa.io send emails that look like they're coming directly from you.

Adding the CNAME records provided by rasa.io does two important things:

1. **Enables newsletter tracking:** Opens and clicks are routed back into your [rasa.io](http://rasa.io/) account.
2. **Builds trust with inboxes:** Your emails are digitally signed, so recipients (and their email providers) know the messages truly come from your domain.

###### Before you begin

- You will need access to your **domain provider** (the company where your domain is hosted, such as GoDaddy, Google Domains, Namecheap, or Cloudflare).
- If you’re not sure who your domain provider is, you can:

  - Reach out to your website developer, or
  - Contact your IT team — they should know who manages your domain.
- If you don’t have direct login access, forward these instructions to your IT team or the person who manages your website so they can complete the update for you.
- Please note: rasa.io cannot authenticate free, public email domains such as **gmail.com, outlook.com, or yahoo.com**. You’ll need to use a domain you own and manage.

###### Important note

- Authenticating a domain will require adding **two sets of DNS records (six CNAME records in total)**.
- If you have multiple domains, you’ll need to complete this process for each domain you want to use.

###### Should I use a subdomain?

We recommend considering a **subdomain** (for example, *news.yourdomain.com* or *updates.yourdomain.com*) for sending your rasa.io newsletters.

Benefits of using a subdomain include:

- **Protecting your main domain reputation:** If a newsletter ever triggers spam filters, your primary domain (like *yourdomain.com*) won’t be affected.
- **Clear separation of traffic:** Marketing and newsletter emails are separated from your everyday business emails.
- **Flexibility:** You can dedicate the subdomain to communications while keeping your main domain focused on regular email use.

###### Next steps

Ready to set up domain authentication? Follow our step-by-step instructions here:  
👉 [How to Authenticate Your Domain](https://help.rasa.io/how-to-authenticate-your-domain)
