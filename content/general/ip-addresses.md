---
title: IP Addresses
source: https://help.rasa.io/ip-addresses
keywords: IP address,whitelist,sendgrid
---

_If you need to whitelist IP addresses for any reason, here are the addresses we use in our infrastructure._

###### Email

We send emails via the following dedicated IP addresses on SendGrid

- 149.72.193.199
- 168.245.114.230
- 168.245.50.210
- 149.72.202.199
- 168.245.124.6

###### Integrations

Integration calls will come from one of these two IP addresses

- 52.11.169.205
- 52.36.170.115

###### Content Pulls

If your content is behind a firewall, we can still pull it into your rasa.io dashboard — you'll just need to whitelist our IP addresses. This lets us securely access your articles or feed so they can appear in your newsletter.

- 52.11.169.205
- 52.36.170.115
- 54.218.186.201
- 54.191.0.82
