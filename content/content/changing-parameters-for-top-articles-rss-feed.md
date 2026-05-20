---
title: Changing Parameters for Top Articles RSS Feed
source: https://help.rasa.io/changing-date-parameters-for-top-articles-rss-feed
keywords: RSS feed,top articles,data parameters,content filtering,content verification,article retrieval
---

rasa.io provides a Top Articles RSS feed that pulls from the top clicked articles from the most recent send. The default is a two-week look back but the data parameters can be changed and the default for the number of articles in the feed is 10 and can be changed.

This knowledge base page provides guidance on changing date parameters for the Top Articles RSS feed using the start\_date and end\_date parameters, changing the number of articles parameter using the num\_records parameter, and filtering the feed to show only original articles using the source=original parameter.

###### Understanding Date Parameters

rasa.io supports both absolute and relative date parameters for filtering RSS feed content:

###### Absolute Dates

bash

CopyEdit

`https://api-public.rasa.io/v1/top-articles/2061bfcd-f5eb-4e50-8a71-3a2513564174?format=rss&start_date=2021-05-01&end_date=2021-05-30`

This example fetches articles published between May 1, 2021, and May 30, 2021.

###### Relative Dates

bash

CopyEdit

`https://api-public.rasa.io/v1/top-articles/2061bfcd-f5eb-4e50-8a71-3a2513564174?format=rss&start_date=now-7d&end_date=now-1d`

Here, the API fetches articles published in the last 7 days (from now-7d) up to yesterday (now-1d).

###### Using Relative Dates

rasa.io allows users to use convenient relative date expressions for flexibility with the RSS feed. See examples below:

- now-1d: Retrieve articles published within the last 1 day.
- now-7d: Retrieve articles from the last 7 days.
- now-3d: Retrieve articles from exactly 3 days before the current time.
- now-72h: Equivalent to -3d, representing a 72-hour time frame before the current time.

/d: Cap the end date at the start of the current day.

/h: Cap the end date at the start of the current hour.

/m: Cap the end date at the start of the current month.

Examples:

- now-4d/m: Retrieve content from 4 days before the current time, with the end date set at the beginning of the current month.
- now-1w/m: Retrieve content from 1 week before the current time, with the end date set at the beginning of the current month.

###### Step-by-Step Guide for Changing Date Parameters

1. Find your Top Articles RSS feed on the Widgets & Tools page:  
   <https://dashboard.rasa.io/widgets/toparticles>
2. Choose Date Parameters:

The default parameters are a two-week look back. If you want to change that, decide whether you want to use absolute or relative dates for content retrieval.

1. Modify the URL:

Adjust the start\_date and end\_date parameters in the URL accordingly. See example below:

1. Test the Modified Feed URL:

Paste the modified URL in a web browser or a feed reader to verify that the API returns the desired content.

###### Step-by-Step Guide for Changing Number of Articles Parameters

1. Find your Top Articles RSS feed on the Widgets & Tools page:  
   <https://dashboard.rasa.io/widgets/toparticles>
2. Choose Number of Articles Parameter:

The default parameter is 10 articles. If you want to change that, decide the number of articles you will want to retrieve.

1. Modify the URL:

Adjust the num\_records parameter in the URL accordingly. See example below:

bash

CopyEdit

`https://api-public.rasa.io/v1/top-articles/2061bfcd-f5eb-4e50-8a71-3a2513564174?format=rss&num_records=25`

1. Test the Modified Feed URL:

Paste the modified URL in a web browser or a feed reader to verify that the API returns the desired content.

###### Step-by-Step Guide for Filtering Only Original Articles

1. Find your Top Articles RSS feed on the Widgets & Tools page:  
   <https://dashboard.rasa.io/widgets/toparticles>
2. Choose Source Parameter:

If you want the feed to include only articles that are original content created through rasa.io, you can add the source parameter.

1. Modify the URL:

Adjust the source parameter in the URL by adding `source=original`. See example below:

bash

CopyEdit

`https://public-api.rasa.io/top-articles/b95c857c-e040-4662-a45f-a5b6bfe7a887?format=rss&num_records=50&source=original`

1. Test the Modified Feed URL:

Paste the modified URL in a web browser or a feed reader to verify that the API returns only original articles.
