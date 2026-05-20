---
title: Understanding Suspect Clicks and the Suspect Clicks Filter
source: https://help.rasa.io/understanding-suspect-clicks-and-the-suspect-clicks-filter
keywords: bot clicks,suspect clicks
---

_rasa.io currently uses an algorithm by which bot and/or security scanner activity can be filtered from email engagement or click reports in your analytics._

###### **What are suspect clicks?**

A suspect click refers to an email click performed by a machine, often to verify the safety of a link or display a link preview. These types of clicks happen within all email service providers

Inbox providers, some 3rd-party security software, and carriers use bots or non-human interactions to click links in emails before any human user. This helps the providers protect users from phishing by ensuring the links are safe and not a malicious URL. Suspect clicks are more common when sending to domains with an increased need for security, such as those belonging to government agencies, financial institutions, and educational institutions. Senders with a history of positive engagement are less inclined to feel the impact of suspect clicks, but no one is immune.

These clicks can impact your analytics because they give a false sense of engagement to a subscriber. It may appear that a subscriber clicked the link in an email because they were interested in the content, but in reality, a machine performed the click and the user did not perform the action.

To improve the accuracy of your data and engagement, rasa.io has built-in filters to identify these clicks. This filter is not based on specific IPs but, rather, suspected behavior. We look at trends and other activity-based data to identify the activity from being logged.

Preventing suspect clicks

Maintaining a strong sender reputation and good overall deliverability shows inbox providers you are a reputable sender and makes them less likely to validate the safety of links in your sends.

**NOTE**

There is no way to prevent bot clicks performed by inbox providers entirely. While these methods can make inbox providers less likely to verify the safety of links in your emails through an automated click, this does not guarantee that all suspect clicks will be prevented.

###### How are analytic reports affected by this filter?

With the suspect click filter enabled, any analytic reports showing click rates or counts of clicks over time will exclude suspect clicks. These analytics include:

- **Opens and Clicks**
- **Daily Stats**
- **Segmentation**
  - NOTE: With segmentation, you can filter to see ONLY suspect clicks and weed out domains that may be inflating your clicks with suspect clicks. If identified, reaching out to the domain can help to combat the inflation and work with the recipients.
- **Topics Reports**
- **Article Reports**
- **Sources Reports**
- **Images Reports**
  - **Should I change how I report my stats to advertisers?**  
    This decision is up to you. Many email platforms still don’t offer this level of transparency. While it can be frustrating to see engagement metrics appear lower when using the suspect clicks filter, the tradeoff is that the data is more authentic.  
    Most advertisers track web traffic driven by their ads, often using tools like Google Analytics. By filtering out bot clicks, your email analytics are more likely to align with what advertisers see on their platforms, providing a more accurate representation of campaign performance. That said, some advertisers prefer seeing everything to gauge total impressions. It’s best to have an open conversation with advertisers about their expectations and the value of transparent data reporting.
- **Other Clicks**

With this filter, we choose to err on the side of caution and do not apply the suspect click label to any activity unless we are certain it did not come from a human. We operate under the idea that we don't want to risk filtering any legitimate activity. Over time, these services will be refined and improved to produce more accurate results, but we cannot guarantee a 100% success rate.

###### How to address and combat suspect clicks

**Determine your newsletter goals.** Are clicksthe desired outcome of your email outreach?  [Measure what counts](https://www.braze.com/resources/articles/email-marketing-the-messaging-metrics-that-matter).

**Follow email best practices.** If your subscribers are opting in because they truly want the email, if your data hygiene is pristine, and if you actively manage your list to remove bounces and unengaged users, then suspect clicks should be minimal.

**Use HTTPS for all links in emails**. This additional layer of security helps demonstrate that your mail has a lower probability of being malicious. rasa.io tracking links will always use HTTPS but be mindful of any links you are manually adding into your newsletter.

**Don’t change your sending schedule.** When suspect clicks are suspected, try your best to send as usual. These automated mechanisms are learning about your behavior, so they need to see it in its purest, unmodified form. If you're constantly changing, they'll need to continue clicking to keep up.

**Clicks happen, and we can't stop them.** Any attempt to evade detection is more likely to have the opposite effect. Remember, security measures are in place to protect subscribers (even you!), not to punish senders.

**Key Insights and Takeaways**

Bot-clicking is now an unavoidable part of the email industry. Regardless of their size or reputation, all bulk senders will experience some level of suspect clicks at some point. These clicks are a natural outcome of increased security measures to protect end users, not a reflection of poor sender performance.

If you’re seeing inflated metrics, stay calm and carry on. These clicks are designed to protect all of us. Focus on becoming a better email sender by executing best practices, and sending truly valuable and relevant content to your audience to build trust and a stronger connection with them.
