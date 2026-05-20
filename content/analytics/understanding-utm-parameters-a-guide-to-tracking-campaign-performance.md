---
title: Understanding UTM Parameters: A Guide to Tracking Campaign Performance
source: https://help.rasa.io/understanding-utm-parameters-a-guide-to-tracking-campaign-performance
---

###### What Are UTM Parameters?

UTM parameters (Urchin Tracking Module) are tags added to the end of a URL to track the effectiveness of online marketing campaigns. These parameters help you collect detailed information about where your traffic is coming from, how users interact with your content, and which elements of your campaigns are performing best.

###### Why Use UTM Parameters?

When running multiple campaigns or ads with the same destination URL, UTM parameters allow you to differentiate and track how each element performs. This is particularly useful for clients running multiple ads with identical URLs. If no UTM parameters are used, the performance data for all ads will be combined, making it difficult to assess which ad or content piece is driving the most engagement.

Using UTM parameters provides more dynamic, detailed analytics by allowing you to distinguish between different campaign components. This way, you can easily see how each individual ad performs without the risk of data from multiple campaigns being combined.

###### How to Use UTM Parameters in Your Newsletters

If you have multiple images or ads with the same URL in a newsletter, adding UTM parameters ensures you can track each one individually. For example, if you’re using the same URL across multiple banners or sponsored placements in the same newsletter, without UTM parameters, you’ll only get combined data in your analytics. By adding parameters, you can track the performance of each ad separately, allowing you to see which image or banner drove more clicks or engagement.

Here’s how this works in practice:

**Scenario:**  
You’re running a campaign with the URL `https://rasa.io` for multiple ads in a newsletter. Let’s say you have two placements: a banner ad and a square ad, both leading to the same URL. Without UTM parameters, the clicks from both ads will be lumped together in your analytics, making it impossible to determine which one performed better.

To avoid this, you can add UTM parameters to differentiate the URLs for each ad and track their individual performance.

###### How to Create UTM Parameters

A UTM-tagged URL is made up of the base URL followed by a question mark, and then several key parameters. For your newsletters, the most commonly used UTM parameters will likely be **ad placement** and/or ad **date**. These help you track how each specific ad performs and when it ran, offering more precise analytics.

The key parameters for your use case are:

- **utm\_content**: Differentiates ads or placements within the same campaign (e.g., banner1, square1). This is especially useful for tracking performance based on ad placement.
- **utm\_date** (custom): Tracks the date of when a specific ad was run, helping you compare performance across different dates.

Other UTM parameters you may encounter include:

- **utm\_source**: Identifies the source of the traffic (e.g., newsletter, Google, Facebook).
- **utm\_medium**: Identifies the marketing medium (e.g., email, banner, social).
- **utm\_campaign**: Specifies the campaign name (e.g., SummerSale2024).

Let’s break it down with an example that may be useful for your newsletters.

###### Example Use Case: Tracking Ads in a Newsletter

If you're running two different ads, a banner and a square, and want to track their performance separately, here’s how you could structure the URLs using UTM parameters:

**Base URL**: `https://rasa.io`

1. **For a banner ad running on July 1, 2024:**

   `https://rasa.io?utm_content=banner1&utm_date=jul012024`
2. **For a square ad running on the same date:**

   `https://rasa.io?utm_content=square1&utm_date=jul012024`

By adding UTM parameters to these URLs, you can track how many clicks each ad received, giving you deeper insights into which creative asset is performing better.

###### How rasa.io Handles UTM Parameters

At rasa.io, we automatically handle UTM parameters for articles, banners, and squares unless specific UTMs are provided by the user. Here’s how it works:

- **For all articles**, we automatically append the following UTM parameters to the URLs:

  `utm_medium=email&utm_source=rasa_io&utm_campaign=newsletter`
- **For all banners or square ads**, we also add the following UTM parameters by default:

  `utm_medium=email&utm_source=rasa_io&utm_campaign=newsletter`

  *If a user schedules images with their own UTM parameters, we will use the specified ones instead of the defaults.*

This ensures that all campaigns are trackable and that you receive detailed performance data unless customized UTMs are specified.

###### Key Benefits of Using UTM Parameters

- **Improved Tracking**: UTM parameters provide better visibility into the performance of individual campaign elements.
- **Detailed Analytics**: You can measure not only the overall success of a campaign but also drill down to see which ads, placements, or dates were most effective.
- **Optimized Campaign Performance**: Armed with specific data, you can optimize future campaigns by identifying which strategies are driving the most engagement.

###### Conclusion

UTM parameters are a simple yet powerful tool to enhance your marketing analytics, providing you with the insights needed to make informed decisions and optimize your campaign strategies. Whether you’re running a multi-ad newsletter or tracking campaign effectiveness across different dates, UTM parameters give you the control and granularity needed to get the most out of your marketing efforts.
