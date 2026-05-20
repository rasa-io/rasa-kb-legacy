---
title: Opens/Clicks Report & Other Analytics Definitions
source: https://help.rasa.io/opens-clicks-report
keywords: delivery,analytics,Email,deliverability
---

This [report](https://dashboard.rasa.io/analytics) will show you all of your open, click, delivery, and bounce data for any given date range of your choosing. You also have the option to customize your view by day, week, or month.

![]()![mceclip0 (21)](https://22539073.fs1.hubspotusercontent-na1.net/hubfs/22539073/mceclip0%20(21).png)

Here is what each column on the report means, as well as some other definitions you will see within other Analytics reporting:

- Total Opens or Opens - The total number of times your email was opened. If one person opens the email multiple times, each of those opens will be counted.
- Total Clicks or Real Clicks - The total number of times that someone clicked on a link within your email. If one person clicks on a link multiple times, each of those clicks will be counted.
- Total Non-Suspect Clicks - The total number of times links in your email were clicked, **excluding** any clicks identified as coming from bots or other suspicious activity. If one real person clicks multiple times, each of those valid clicks will be counted, but bot clicks will not.
- Unique Opens - The unique number of times your email was opened. If one person opens the email multiple times, we will only count 1 of their opens.
  - Unique Open Rate=(Unique Opens​÷Emails Delivered​)×100
- Unique Clicks - The unique number of times that someone clicked on a link within your email. If one person clicks on a link multiple times, one 1 of those clicks will be counted.
  - Unique Click Rate=(Unique Clicks​÷Emails Delivered)×100
- Unique Non-Suspect Clicks - The number of **distinct individuals** (non-bots) who clicked on a link in your email. Each individual is only counted once, even if they clicked multiple times. This metric excludes any clicks flagged as suspicious or artificial.
  - Unique Non-Suspect Rate=(Unique Non-Suspect Clicks÷Emails Delivered)×100
- Clicks to Open - The percentage of recipients who clicked on a link within the email after opening it.
  - Clicks to Open Rate=(Unique Clicks÷Unique Opens)×100
- Delivered - How many emails were successfully delivered to your subscribers' inbox.
  - Export your [Contacts](https://dashboard.rasa.io/contacts) list to see the list of emails that have bounced in our system. Bounces - How many email addresses bounced when we attempted delivery.
- Unique Click Rate (should be Unique Click-to-Open Rate): This metric represents the percentage of unique recipients who clicked on a link, relative to the number of times the email was opened.

  - Unique Click-to-Open Rate = (Unique Clicks ÷ Number of Opens) × 100
- Rea/Total Clicks Rate (should be Click-to-Open Rate): Measures the percentage of email openers who clicked on any links or images within the email, offering insights into the relevance of your content.

  - Click-to-Open Rate = (Total Clicks ÷ Number of Opens) × 100

###### Using the Graph

You can display **multiple metrics at once** on the graph to compare performance trends over time.

Each metric has toggle buttons labeled **L** (Left) and **R** (Right), allowing you to assign them to either axis:

1. Click **L** to plot the metric on the left axis.
2. Click **R** to plot the metric on the right axis.

This lets you visualize different types of data — even those on different scales — together in a single view. For example, you can graph **Unique Open** and **Delivered** on the left axis, while showing **Click To Open Rate** on the right.

> Tip: Use a combination of volume-based metrics and percentage-based metrics to gain deeper insights into engagement.

**'Group by' Filter:**

- Group by Day - A granular view of your email opens and clicks on a day-to-day basis. This is particularly useful for identifying specific days that saw higher engagement if you send a daily newsletter. The above rates are based on the number of emails delivered for that day.
- Group by Week - A broader view of the engagement over the entire week. If you only send once per week, the data will be the same as if you grouped by day. If you send more than once per week, the data will be aggregated over multiple days, and the above rates will be calculated based on overall audience penetration for that week. The open and click rates will show the engagement from your *audience as a whole* for that week.
- Group by Month - Similar to grouping by week, this filter will show you a high-level overview of how engaged your audience was over the entire month-long period. The above open and click rates will also be calculated based on your audience as a whole instead of how many total emails were sent that month.

####
