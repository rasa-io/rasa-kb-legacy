---
title: Troubleshooting Images Not Displaying in Emails
source: https://help.rasa.io/troubleshooting-images-not-displaying-in-emails
keywords: image size,Email,image,display,image display issues,email troubleshooting,blocked images,firewall restrictions,image loading solutions,background images
---

When sending out emails, it's important to ensure that all recipients can view the content as intended. However, there are several reasons why images may not display in your email. Here's a comprehensive guide to troubleshoot and resolve this issue.

###### Reasons Why Images May Not Load

1. **Blocked Images:** Recipients' email clients may block externally hosted images for various reasons. These blocks can be set based on personal preferences or controlled by system administrators.
2. **Background Images Not Supported:** Certain email clients, such as some versions of Microsoft Outlook on Windows, do not support background images. In such cases, it's essential to have fallback options in place.
3. **Firewall Restrictions:** Strict firewall rules, especially in government organizations, may block access to external image servers, preventing images from loading in emails.

###### Recommended Solutions

To address the possibility of images not loading in emails, we recommend implementing the following strategies:

1. **Include a Web Version Link:** Always include a link to the web version of your email. This ensures that recipients can access the content even if images do not load in their email client.
2. **Use Text and Images Together:** Strike a balance between text and images in your email content. By incorporating meaningful text alongside images, you can convey your message effectively even if images fail to load.

###### Enabling Image Display in Email Clients

Recipients experiencing issues with image display can try adjusting their email client settings. Here are instructions for enabling image display in various email clients:

**AOL Mail**

1. Click **Settings** ![Settings icon](https://o.aolcdn.com/membership/help/000000_New_Salesforce_Org/000011839/mail-n_settings-icon_en_02.png) | **More Settings** ![SMore settings icon](https://o.aolcdn.com/membership/help/000000_New_Salesforce_Org/000011851/mail-n_more-icon_en_01.png).
2. Click **Viewing email** tab.
3. Scroll down, until you see **Show images in messages**.

• Choose **Always, except spam folder** to enable images.  
• Choose **Ask before showing external images** to block images.

For additional assistance with AOL Mail, please see [AOL Support](https://help.aol.com/products/aol-mail/articles).

**Apple Mail on Mac**

1. Click **Mail** > **Preferences**.
2. Click the**Viewing** button.
3. Make sure a check mark is next to "Load remote content in messages."
4. Close the window.

For additional assistance with viewing settings in Apple Mail, please see [Apple Support](https://support.apple.com/guide/mail/change-viewing-preferences-cpmlprefview/mac).

**Apple Mail on iPhone/iPad**

1. Tap **Settings.**
2. Tap **Mail**.
3. Find the **Load Remote Images**option and toggle it on.

For additional assistance with iOS devices, please see [Apple Support](https://support.apple.com/)

**Gmail**

Head to the [Gmail site](https://mail.google.com/) and sign in if you aren’t already.

Once you’re logged in, click the **Settings** icon (gear) in the top right.

Click the **See all settings**button.

Under the **General** tab, scroll down to the **Images** section and check the **Always display external images**option.

After making your selection, scroll to the bottom of the page and click the **Save Changes**button.

**Outlook 365**

Open Outlook application - Go to File > Options > Trust Center > Trust Center Settings > Automatic Download. - Make sure the "Don't download pictures automatically in HTML email messages or RSS items" checkbox is not selected. - Click OK to apply.

If it's already applied, but still having the same issue, please proceed with the further steps below: Try to clear the Temp files:

1. Press Windows key + R to open Run dialog box
2. Type %temp% and press Enter on the keyboard.
3. Delete the files in the folder that opens.

Now, if the same issue continues, try to check if there's an available update for Outlook:

1. Open Outlook application
2. Go to File > Office Account
3. Click on Update Options > Update Now

For additional support, please see [Microsoft Office support](https://support.office.com/en-us/article/block-or-unblock-automatic-picture-downloads-in-email-messages-15e08854-6808-49b1-9a0a-50b81f2d617a).

**Mozilla Thunderbird:** By default, Thunderbird blocks remote images in email messages to help protect your privacy. When you receive a message with remote images, Thunderbird will display an alert stating that remote images have been blocked.

Allow images from all senders:

1. Click **Tools**.
2. Click **Options**.
3. Click **Privacy**.
4. Check the "Allow remote content in messages" checkbox to have all remote content loaded by default.

For additional assistance with images in Thunderbird, please see [Mozilla Support](https://support.mozilla.org/en-US/kb/remote-content-in-messages).

****Samsung Mail:****Display images in all emails:

1. Tap the menu icon in the top left of the screen.
2. Tap the settings gear icon.
3. Tap the account you want to to edit the settings for.
4. Find the "Show images" option and toggle it on.

For additional assistance with Samsung Mail, please see [Samsung support](https://www.samsung.com/ie/support/mobile-devices/how-do-i-use-the-samsung-email-app/).

**Yahoo Mail**: Disable image blocking for all messages:

1. Click Settings gear icon and then click **More Settings**.
2. Click "Viewing email."
3. Under the Show images in messages section, select "Always, except in spam folder."

For additional assistance with Yahoo Mail, please see [Yahoo Support](https://help.yahoo.com/kb/new-mail-for-desktop?).

  

###### Specific Situations and Solutions

- **Blocked Images:** Unfortunately, it's not possible to override recipients' email client settings. The best approach is to keep your subscriber list engaged with valuable content, include alternative text for images, and provide a web version link in your emails.
- **Background Images Not Supported:** To address this issue, choose a background color similar to your image as a fallback option.

###### Additional Troubleshooting Tips

If images still do not display after adjusting settings, consider the following troubleshooting steps:

- **Try Different Browser:** Encourage recipients to open emails in a different web browser to rule out browser-specific issues. Images may display correctly in an alternate browser if the original browser has compatibility issues.
- **Firewall and Security Programs:** Verify that firewall or intrusion prevention security programs do not block URLs or IP addresses associated with image hosting. Whitelisting the necessary domains can resolve image loading issues caused by strict firewall restrictions.

Ensuring that images load correctly in emails is essential for effective communication with your audience. By implementing the recommended solutions and providing support for recipients, you can enhance the overall email experience and maximize engagement with your content. If you encounter any further issues or need assistance, please don't hesitate to reach out to our support team for help at support@rasa.io.
