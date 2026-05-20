---
title: Why isn't my newsletter in my inbox?
source: https://help.rasa.io/why-isnt-my-newsletter-in-my-inbox
keywords: DMARC,Email,domain authentication,newsletter delivery,SPAM folder,inbox issues,email filtering,trustworthy emails,Send From address,email contacts,email settings,email provider settings
---

_If it looks like your newsletter generated successfully — but you didn’t receive it in your inbox, the issue is almost always on your mailbox or internal security end._

###### 1. It Likely Did Send Successfully

If your newsletter:

- Shows a **current send date** in Analytics or Content > History, and
- You see **fresh or empty content** in the Upcoming page,

then your newsletter was successfully **generated and delivered** to your mail server.  
The system received a “delivered” confirmation, meaning the email left our servers and reached yours.

If you still don’t see it in your inbox, it’s likely being **filtered, quarantined, or redirected** internally.

###### 2. Check Internal Mail Security Settings

When you’re sending from your **own domain**, your organization’s mail security may flag newsletters that appear to come “from you” but are technically sent **through a new vendor (rasa.io)**.

This is one of the **most common reasons** newsletters don’t appear in the sender’s own inbox.  
Your IT system may think:

> “This email looks like it’s from our domain, but it wasn’t sent from our internal mail server — it could be spam.”

Even if your domain is properly **authenticated** (with SPF, DKIM, and DMARC records in place), internal filters can still block or quarantine your newsletters until the system recognizes rasa.io as a safe sender.

> ✅ **Tip:** Ask your IT or security team to whitelist rasa.io’s sending IPs and domains, so mail from your authenticated domain is fully trusted.

###### 3. It’s Not Usually a Deliverability Problem for Subscribers

If your newsletter is generating successfully but only **you** (or internal team members) aren’t receiving it, it doesn’t mean your subscribers are having the same issue.

These internal filtering conflicts are specific to:

- Company networks
- Internal mail security systems
- Organizational spam policies

Your **external subscribers** are almost always still receiving the newsletter normally.

###### 4. Other Quick Things to Check

- **Check your spam or junk folder** — especially for the first few sends from a new or authenticated domain.
- **Mark the newsletter as safe** or move it to your primary inbox if found.
- **Add your “From” address to your contacts or safe senders list.**
- **Ask IT** to review or release any messages quarantined under your company’s spam policy.

---

###### 5. If You’re Still Not Seeing ItIf you’ve checked your inbox, spam, and internal filters but the issue persists:

- Confirm that your contact is **still subscribed** under **Contacts > Unsubscribed**.
- If your contact status looks correct and the newsletter appears delivered,  
  contact **support@rasa.io** with your send date and any delivery details you can provide.
