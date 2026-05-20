---
title: How To Authenticate Your Domain
source: https://help.rasa.io/how-to-authenticate-your-domain
keywords: CNAME,domain authentication,domain management,CNAME records,DNS host,domain setup,DNS configuration,email sending domain,verification process,common domain hosts,GoDaddy,WordPress,record verification
---

###### Step 1: Open Domain Authentication

1. Log in to your rasa.io account.
2. Go to **Settings → [Domain Authentication](https://dashboard.rasa.io/settings/domain)**.

###### settings

###### Step 2: Generate DNS records

1. On the Domain Authentication page, enter your domain if prompted.
2. You will see a **“Generate Records” button**.

   - You should now see **two sets of DNS records (six CNAME records in total)**.
   - You have the option to copy all records at once or individually copying the name and values one by one.

![all records](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/all%20records.png)

🎥 **Video guide:** This video walks you through the domain authentication process step by step.  
*Please note: the video shows the addition of three records, but you will now need to add six records in total in order to validate your domain.*

![](https://fast.wistia.com/embed/medias/8v4g45cs2s/swatch)

**Important:** If you already have DNS records from a previous setup, **do not remove them**. Just add the new records in addition to the ones already in place.

###### Step 3: Add the records to your domain provider

1. Log in to your domain provider (the company where you purchased or manage your domain, such as GoDaddy, Google Domains, Namecheap, or Cloudflare).
2. Locate the DNS settings or DNS management area.
3. Add all six new CNAME records exactly as they appear in rasa.io.

If you’re not sure who your domain provider is, you can:

- Reach out to your website developer, or
- Contact your IT team — they should know who manages your domain.

If you do know your domain provider but don’t have login access, please forward these instructions to your IT team or the person who manages your website so they can complete the update for you.

###### Step 4: Validate your domain

1. After adding all records, return to rasa.io.
2. On the Domain Authentication page, click **Validate Domain**.

   ![validate domain](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/validate%20domain.png)
3. If validation succeeds, your domain will be marked as authenticated and you will see that both sets of records display as "valid" and the message below pop up in your dashboard.

   ![valid](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/valid.png)

![domain validated](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/domain%20validated.png)

###### Step 5: Repeat for additional domains (if applicable)

If you have more than one domain, repeat these steps for each domain you want to use with rasa.io.

👉 For more background on why domain authentication matters and the benefits of using a subdomain, see our [Overview of Domain Authentication](https://help.rasa.io/overview-of-domain-authentication).

###### Here are instructions for common domain hosts:

- [**Go Daddy**](https://www.godaddy.com/help/add-a-cname-record-19236#smhvid  )
- [**Word Press**](https://en.support.wordpress.com/domains/custom-dns/)
- **[Bluehost](https://my.bluehost.com/hosting/help/dns-management-add-edit-or-delete-dns-entries)**
- **[HostGator](https://www.hostgator.com/help/article/changing-mx-a-cname-records-plesk-10)**
- **[Hostinger](https://www.hostinger.com/how-to/how-can-i-manage-my-dns-records)**
- **[Domain.com](https://www.domain.com/help/article/dns-management-how-to-update-cname-aliases)**
- **[Google Domains](https://support.google.com/domains/answer/9211383?hl=en)**
- [**Yahoo**](https://help.smallbusiness.yahoo.net/s/article/SLN17912)
- [**web.com**](https://knowledge.web.com/subjects/article/KA-01097/en-us)
- [**Network Solutions**](http://www.networksolutions.com/support/cname-records-host-aliases/)
- [**name.com**](https://www.name.com/support/articles/115004895548-Adding-a-CNAME-Record)
- [**A2 Hosting**](https://www.a2hosting.com/kb/cpanel/cpanel-domain-features/using-the-cpanel-zone-editor)
- [**DreamHost**](https://help.dreamhost.com/hc/en-us/articles/215414867-How-do-I-add-custom-DNS-records-)
- **[iPage](https://www.ipage.com/help/article/dns-management-how-to-update-cname-aliases)**
- [**Inmotion Hosting**](https://www.inmotionhosting.com/support/uncategorized/create-cname-record/)
- [**Web Hosting Hub**](https://www.webhostinghub.com/help/learn/domain-names/dns-nameserver/add-cname-record)
- [**Green Geeks**](https://www.greengeeks.com/support/article/how-do-i-change-dns-for-mx-cname-and-a-records/)
- **[1&1](https://www.ionos.com/help/domains/configuring-cname-records-for-subdomains/configuring-a-cname-record-for-a-subdomain/)**
- [**Wix**](https://support.wix.com/en/article/adding-dns-records-in-your-wix-account)
