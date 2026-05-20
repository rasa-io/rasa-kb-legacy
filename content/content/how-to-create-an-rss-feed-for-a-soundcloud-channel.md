---
title: How to create an RSS feed for a SoundCloud channel
source: https://help.rasa.io/how-to-create-an-rss-feed-for-a-soundcloud-channel
keywords: content,article,RSS feed,audio rss feed,soundcloud rss feed,rss feed curation,soundcloud,soundcloud channel,audio content,music rss feed
---

In order to create an RSS feed for a [SoundCloud](https://soundcloud.com/) channel, follow the steps below.

1. Go to the SoundCloud page you want to create an RSS feed for.

2. Look at the page URL. For example:

<https://soundcloud.com/garyvee>

3. Then right-click somewhere on the page and select "view page source". Then search (CTRL+F) for "soundcloud://users:" The user ID is the number in that Soundcloud URL.

4. Place the value for the user ID at the end of the URL:

http://feeds.soundcloud.com/users/soundcloud:users:USERID/sounds.rss

so that the full URL will look like this:

<http://feeds.soundcloud.com/users/soundcloud:users:2366352/sounds.rss>

If you want to brush up on your knowledge of RSS feeds, check out [this page](https://help.rasa.io/finding-an-rss-feed) to learn about more the basics of RSS feeds.
