---
title: Does rasa.io support merge fields?
source: https://help.rasa.io/does-rasa.io-support-merge-fields
keywords: merge fields,dynamic content,custom subject lines,preview text,contact first name,newsletter name,dynamic autofill,customization options,personalization examples,empty merge fields,email personalization
---

We have several different merge fields that will dynamically autofill values in certain elements of your email. Merge fields are supported in [custom subject lines, custom preview text](https://dashboard.rasa.io/design#sendfrom) as well as in the [text/html boxes](https://dashboard.rasa.io/design#layout) available in the templates.

Below are the inputs for the available merge fields within each supported section:

**\*Please note that "TESTfirstname" will show as the first name in your TEST emails only**

**Custom Subject Line**

Contact First Name: \_\_FIRST\_NAME\_\_

Date: \_\_DATE\_\_

Newsletter Name: \_\_COMMUNITY\_\_

Personalized Article Title: \_\_RECOMMENDED\_TITLE\_\_

Boosted Article Title: \_\_TITLE\_\_

**Custom Preview Text**

Contact First Name: \_\_FIRST\_NAME\_\_

Date: \_\_DATE\_\_

Newsletter Name: \_\_COMMUNITY\_\_

Personalized Article Title: \_\_RECOMMENDED\_TITLE\_\_

**Text/Html Boxes**

First Name: \_\_FIRST\_NAME\_\_

Email: \_\_EMAIL\_\_

If the value of the merge field is empty (i.e. you do not have first name data for a contact), it will not show any text in that field.

*Example:*

Custom Subject Line input: "Hi \_\_FIRST\_NAME\_\_, here's your weekly newsletter."

For a contact with no first name in our system, it will show as: "Hi, here's your weekly newsletter."
