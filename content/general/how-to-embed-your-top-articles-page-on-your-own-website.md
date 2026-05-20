---
title: How to embed your top articles page on your own website
source: https://help.rasa.io/how-to-embed-your-top-articles-page-on-your-own-website
keywords: content,article,RSS feed,top articles,user experience,top articles page,customizable forms,dynamic feature,newsletter engagement,subscriber interaction,HTML embedding,iframe code,website integration
---

You can embed your [top articles page](https://dashboard.rasa.io/widgets) on your website site with the code below!

The [top articles page](https://dashboard.rasa.io/widgets) provides a succinct view of the most clicked articles by your audience for each newsletter. This page is continually updated as you send your newsletter and your subscribers engage with the content.

Embedding this dynamic feature on your website could entice non-subscribers to subscribe to your newsletter and encourage them to stay up-to-date with the latest news and insights. And for current subscribers, the [top articles page](https://dashboard.rasa.io/widgets) provides them with the opportunity to view articles that they may have missed otherwise.

To learn more about the Top Articles page and other customizable forms, visit this [page](https://help.rasa.io/customizable-forms)!

A few things to keep in mind though when embedding your top articles page...

- This iframe is going to have a scroll bar so we suggest putting it on a page without a scroll or you will see double scroll bars.

- If you'd like to hide the header image and sign-up link, simply adjust it in the settings [on this page where you can customize it fully](https://dashboard.rasa.io/widgets/toparticles#headerAndLogo).

Here is an example of the code you will need to embed but do note that each newsletter has its unique code to embed: <html>   
<body style="height:95%;width:95%">   
<div>   
<iframe height="100%" width="100%" style="height:100%;width:100%;overflow:hidden" frameborder=0 src= [**your top articles page link here**](https://dashboard.rasa.io/widgets) ?iframe=true frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>   
</div>   
</body>   
</html>

**Changes you can make to this code to adjust how it displays (remember, these settings are going to be custom depending on the setup of your site):**

**1. Adjusting the Display Dimensions:**

To control how much content is displayed within the iframe, you can modify the height and width properties of both the `body` and `iframe` elements. Here's how you can do it:

html<html><body style="height:100%;width:100%;margin:0;"><div style="height:100vh; width:100vw;"><iframe height="100%" width="100%" style="height:100%;width:100%;overflow:auto;" frameborder="0" src="your\_top\_articles\_page\_link\_here" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></body></html>

- The `height` and `width` properties are set to 100% for both `body` and `iframe` to utilize the entire viewport.
- A `margin: 0;` style is added to the `body` element to eliminate any default spacing.

**2. Controlling Scrolling Behavior:**

By changing the `overflow` property in the iframe style, you can control whether or not scrollbars appear when the embedded content exceeds the dimensions of the iframe.

- `overflow: hidden;`: No scrollbars will be visible. Content that exceeds the dimensions of the iframe will be cropped.
- `overflow: auto;`: Scrollbars will appear when the content exceeds the dimensions of the iframe. Users can scroll to see more content.

Remember to replace `"your_top_articles_page_link_here"` it with the actual URL of the page you want to embed.

These code modifications enable you to customize the display of embedded content according to your preferences, making it easier to showcase more or less content as needed.
