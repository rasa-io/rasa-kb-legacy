---
title: How to Use UTM Codes in Scheduled Content to Add Multiple Articles with the Same URL
source: https://help.rasa.io/how-to-use-utm-codes-in-scheduled-content-multiple-articles
keywords: content scheduling,UTM codes
---

_If you plan to feature the same URL more than once in future newsletters using Scheduled Content, it's important to understand how the rasa.io platform identifies and handles repeated links._

###### Why only one article per URL can be scheduled

When you add content to Scheduled Content in rasa.io, our system uses the **URL as the unique identifier** for that article. This helps us track engagement, avoid duplicates, and maintain consistency in how content is handled.

Because of this:

> If you try to schedule multiple articles with the **exact same URL** for different future dates, the system will treat them as the **same article** — even if you’ve changed the headline or description.

The result? Your new scheduled entries may **overwrite or merge** with your original entry.

###### The solution: Use UTM codes to make URLs unique

To schedule the same article multiple times on different dates, we recommend **modifying the URL slightly** using **UTM parameters**. These parameters make each version of the link unique while still pointing to the same destination.

###### Example:

Let’s say your base URL is: https://example.com/awesome-report  
To schedule this article for three different send dates, you could use:

1. https://example.com/awesome-report?utm\_source=rasa&utm\_campaign=april1
2. https://example.com/awesome-report?utm\_source=rasa&utm\_campaign=april8
3. https://example.com/awesome-report?utm\_source=rasa&utm\_campaign=april15

  

Each of these links will be treated as a separate article in Scheduled Content, allowing you to:

- Customize the title or description for each instance
- Set different rank levels if desired
- Feature the same report multiple times without merging issues

###### Recap:

- rasa.io uses the **URL as the unique identifier** for scheduled articles.
- To schedule the same content more than once, **change the URL** slightly using UTM codes.
- This allows you to **reuse content across multiple newsletters** without overwrite issues.
