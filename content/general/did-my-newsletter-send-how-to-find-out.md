---
title: Did My Newsletter Send? How to Find Out
source: https://help.rasa.io/checking-newsletter-delivery-status
keywords: deliverability,sending schedule,newsletter sent
---

_Covers overall delivery confirmation using Analytics, Content, and sending logs._

Sometimes it can look like your newsletter didn’t go out — but in most cases, it actually **did generate and deliver** successfully. The issue is often related to timing, email filtering, or subscriber status.  
Here’s how to confirm what really happened and where to look next.

---

###### Step 1: Confirm the Newsletter Was Generated and Sent

Start by confirming that the system successfully created and sent your newsletter.

###### ✅ Check the **Analytics > Daily Stats** Page

- Go to the **Analytics** tab and select **Daily Stats**.
- If you see the **date of your most recent newsletter** in the dropdown, that means the newsletter **was generated and sent**.
- Data might still be syncing for a few minutes right after send time — so if metrics look incomplete, give it a short while.

###### ✅ Check the **Content > History** Tab

- Open the **Content** tab.
- In the **Upcoming** section, you should see **few or no articles** — this indicates the system just used them to create your latest send.
- Switch to the **History** tab. If the date of the newsletter appears in the dropdown, it confirms that the send **was completed successfully**.

If both of these checks confirm a send, you can be confident the newsletter **went out**.  
If you or a subscriber still didn’t receive it, move on to the next step.

---

###### Step 2: Determine Whether It’s a Delivery or Subscription Issue

###### 🔍 Check Your (or the Subscriber’s) Contact Details

- Go to the **Contacts** tab and search for the email address in question.
- Click on the record to open **Contact Details**.
- Look for the **“Last Newsletter”** date field.

**If the Last Newsletter date is current:**  
That means the system delivered the newsletter to your mail server.

- If it didn’t show up in your inbox, check your **spam**, **junk**, or **company quarantine folders**.
- If it’s still missing, reach out to your **IT team** to have them release or whitelist the message — we’ve already received a successful delivery confirmation, so the issue is internal to your email system.

**If the Last Newsletter date is not current:**  
That means the contact likely didn’t receive it — continue to Step 3.

---

###### Step 3: Check if the Contact Was Unsubscribed or Dropped

If the subscriber didn’t receive the newsletter and their “Last Newsletter” date is outdated:

- Still in the **Contact Details** page, look for the **Unsubscribe Reason** field.  
  This will help you understand why they stopped receiving newsletters.

###### **Unsubscribe Reason: Dropped**

- The subscriber was subscribed, but their email previously returned a **hard bounce** (invalid or permanently undeliverable).
- When the system detects a repeated hard bounce, it automatically marks the address as **Dropped** to protect your sending reputation.
- To restore them, click **Resubscribe**, but only if:

  - You’ve confirmed the email address is now valid, and
  - The subscriber wants to receive newsletters again.

###### **Unsubscribe Reason: Soft Bounce**

- A soft bounce is a temporary delivery failure (like a full inbox or temporary server block).
- If a contact soft bounces **five consecutive newsletters**, the system automatically unsubscribes them.
- You can resubscribe them after confirming they’ve **whitelisted your sending address** or cleared any internal filters.

> 💡 **Tip:** Before resubscribing anyone, make sure the root cause of the bounce has been fixed so future sends aren’t blocked again.

---

###### Step 4: Troubleshoot Missing Emails

If your newsletter shows as sent and your contact is still subscribed, but no one’s receiving it:

- Verify that your **sending domain** and IP are whitelisted by your organization’s email filters.
- Encourage subscribers using corporate or government email domains to do the same.
- Refer to our [[Whitelisting](https://help.rasa.io/what-can-i-tell-my-subscribers-who-arent-receiving-my-newsletter) & [IP Knowledge Base Page](https://help.rasa.io/ip-addresses)] for step-by-step instructions.

---

###### Summary

| Situation | What It Means | What to Do |
| --- | --- | --- |
| Newsletter date appears in Analytics & History | It generated and sent successfully | Check delivery at the contact level |
| “Last Newsletter” date is current | Delivered, but possibly filtered | Check spam/junk or contact IT |
| Contact is unsubscribed (Dropped or Soft Bounce) | System removed them due to bounces | Resubscribe only if valid and fixed |
| No recent send or date showing | Newsletter didn’t generate | Contact Support for investigation |

---

This step-by-step approach helps bridge the gap between thinking your newsletter “didn’t go out” and diagnosing whether the issue is a **system delivery**, **subscriber status**, or **email filtering problem**.
