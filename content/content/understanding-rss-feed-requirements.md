---
title: Understanding RSS Feed Requirements
source: https://help.rasa.io/understanding-rss-feed-requirements
keywords: RSS feed
---

_RSS (Really Simple Syndication) feeds allow rasa.io to access updated content automatically for newsletters. Each RSS feed uses a specific XML-based format to ensure that content can be properly interpreted and displayed._

rasa.io uses RSS feeds to automatically pull in content for upcoming newsletters. To pull content in as expected, RSS feeds need to be formatted so that rasa.io can access the content link, source, title, description, image, tags, and publication date.

###### Required Elements of an RSS Feed

###### 1. **Root Element: `<rss>`**

- The root of the RSS document is an `<rss>` tag with an attribute specifying the version. For example:

  xml

  Copy code

  `<rss version="2.0">  
   ...  
  </rss>`

###### 2. **Channel Information: `<channel>`**

- The `<channel>` element is a container for all information about the feed. This element must include the following child elements:
  - **Title** (`<title>`): The name of the feed.

    xml

    Copy code

    `<title>Example News Feed</title>`
  - **Link** (`<link>`): A URL linking to the site or the feed’s main page.

    xml

    Copy code

    `<link>https://www.example.com</link>`
  - **Description** (`<description>`): A short description of the feed's purpose or content.

    xml

    Copy code

    `<description>Latest updates and news from Example.</description>`
  - **Language** (`<language>`): The language of the feed, typically in ISO-639 format.

    xml

    Copy code

    `<language>en-us</language>`

###### 3. **Items within the Channel: `<item>`**

- Each `<channel>` must contain one or more `<item>` elements, representing individual articles, blog posts, or updates. Each `<item>` element can contain the following sub-elements:

  - **Title** (`<title>`): The title of the article or update.

    xml

    `<title>New Blog Post: Understanding RSS Feeds</title>`
  - **Link** (`<link>`): A URL linking directly to the full version of the content.

    xml

    `<link>https://www.example.com/blog/rss-guide</link>`
  - **Description** (`<description>`): A brief summary or excerpt of the content.

    xml

    `<description>This article explains the basics of creating and using RSS feeds.</description>`
  - **Publication Date** (`<pubDate>`): The publication date of the content, in RFC 822 format.

    xml

    `<pubDate>Mon, 29 Oct 2024 12:00:00 GMT</pubDate>`
  - **Unique Identifier** (`<guid>`): A globally unique identifier for each item, which helps avoid duplication in feed readers.

    XML

    `<guid isPermaLink="false">urn:uuid:1234-5678-91011-121314</guid>`

    ### Images within an Item

    To include images in an RSS feed, you can use the following methods:

    1. **`<enclosure>` Element**: Allows you to link media files (like images, audio, or video).

       xml

       `<enclosure url="https://www.example.com/images/post-image.jpg" length="12345" type="image/jpeg" />`
    2. **Using `<media:content>`**: If following the Media RSS specification, you can specify detailed metadata about media.

       xml

       `<media:content url="https://www.example.com/images/post-image.jpg" type="image/jpeg" />`
  - **Optional Elements**: Additional elements like `<author>`, `<category>`, and `<enclosure>` can be included to provide more information about each item. For example:

    xmlCopy code

    `<author>author@example.com (John Doe)</author>  
    <category>Technology</category>  
    <enclosure url="https://www.example.com/podcast.mp3" length="12345" type="audio/mpeg" />`

###### The items within the channel are what need to be included in a feed for rasa.io to properly pull in content and the appropriate metadata.

The title gives us the title of the article.

The description gives us the description of the article.

The link gives us where the article should link out to.

The publication date provides a date on the upcoming page and also validates whether the content has been published since the last send and should be pulled in.

We do not need the unique identifier but it is preferred. The same goes for the category as that allows us to assign topical tags based on the category in the feed.

###### Best Practices for a Properly Functioning RSS Feed

1. **Ensure Valid XML Structure**: All tags must open and close properly. Use an XML validator to check your feed.
2. **Adhere to RSS Specification**: Follow the standard elements and attributes as defined in the [RSS 2.0 Specification](https://www.rssboard.org/rss-specification#hrelementsOfLtitemgt) to avoid compatibility issues.
3. **Use Proper Date Formats**: Ensure that dates are formatted correctly (e.g., RFC 822 for `<pubDate>`).
4. **Provide Unique Identifiers**: Use unique `<guid>` values to prevent duplicate content in readers.
5. **Test with RSS Validators and Aggregators**: Verify your feed using online RSS validators and test it in popular feed readers to ensure correct parsing.

###### Common Issues to Avoid

- **Missing or Incorrect Required Elements**: Missing a `<title>`, `<link>`, or `<description>` element can cause the feed to fail or display improperly.
- **Improper Tag Nesting**: Make sure all tags are nested correctly within `<rss>` → `<channel>` → `<item>`.
- **Non-standard or Unsupported Tags**: Custom tags like `<mainimage>` may not be recognized by rasa.io.

By following these guidelines and adhering to the RSS 2.0 specification, you can ensure your RSS feed can be pulled in properly by rasa.io
