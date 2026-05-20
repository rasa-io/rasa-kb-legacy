---
title: How to Edit Custom HTML Templates Directly in the Dashboard
source: https://help.rasa.io/how-to-edit-custom-html-templates-directly-in-the-dashboard
keywords: HTMLtemplate
---

_You can now edit your custom HTML newsletter templates directly from the dashboard, without needing to export and reupload them. This makes it faster and easier to make small updates to your design or content._

**Important:** We recommend using this feature only if you have some experience writing or editing HTML. Making incorrect changes may impact how your newsletter renders or processes dynamic content.

We recommend watching the Loom video below to understand how to use the editor and to review some examples of simple edits you can make:

[Using the HTML editor in the rasa.io dashboard - Watch Video](https://www.loom.com/share/48bc36a5288f4e3291e8162b868609fb)
[![](https://cdn.loom.com/sessions/thumbnails/48bc36a5288f4e3291e8162b868609fb-fb01d5685b5bf3ec-full-play.gif#t=0.1)](https://www.loom.com/share/48bc36a5288f4e3291e8162b868609fb)

###### **How to Access Your Custom Templates**

1. Navigate to **Templates** in the dashboard.
2. Under **Saved Templates**, you will see all custom templates that have been used on your account.
3. The currently published template is indicated by a green check mark in the upper-right corner of the template card.
4. You can edit the template that is currently published or edit a different saved template.

###### **How to Edit a Template**

1. Select the **Edit** button located below the template name.
2. A modal will open displaying:

   - An HTML editor on the left
   - A live preview on the right
3. As you make changes in the HTML editor, you will see those updates reflected in the preview on the right.

If the edit you expected (such as a section name change) does **not** appear in the preview, that indicates the change did not occur as expected. In this case, you can undo your changes using:

- Mac: Command + Z
- Windows: Control + Z

When you have finished making your edits, be sure to select **Save**.

###### **Saving Your Changes as a New Template (Optional)**

If you want to make edits without modifying the original template, you can toggle the option labeled **“Save as new template (instead of updating existing)”**.

When this option is selected:

- Your edits will be saved as a completely new template
- You can rename the new template
- The original template will remain unchanged

This is especially helpful if you are testing changes or are unsure how they may affect the final design.

###### **Understanding rasa.io Custom Templates**

rasa custom templates use special HTML attributes to provide processing instructions for inserting dynamic and personalized content. These attributes are required for proper newsletter rendering and personalization.

Because of this, you should avoid removing or altering rasa-specific attributes unless you understand their purpose. That said, many simple updates can be safely made directly in the editor.

###### **Examples of Simple, Safe Edits**

You can use the editor to make updates such as:

- Updating your company address in the footer
- Replacing a social media link with a new URL in the footer
- Moving a section or banner/square to a different location in the template

###### **Using the Find Function to Locate Sections**

We recommend using your browser’s Find function to quickly locate specific sections in the template.

- Mac: Command + F
- Windows: Control + F

###### **Pro Tip:** Use AI to speed up your HTML edits! While rasa.io is in beta with Scout—our AI agent that will soon make live template edits for you—you can use tools like Claude or ChatGPT in the meantime. Just select all the HTML code in the editor, paste it into the chat, and tell it exactly what you want to change. It's a great way to make quick tweaks without deep coding knowledge.

###### Other Best Practices and Tips

- Make small changes at a time and preview often
- Use the preview to confirm your edits worked as expected
- Do not remove `data-rasa-*` attributes unless you know exactly what they do
- Use “Save as new template” when testing or experimenting
- For advanced structural changes, consider reaching out to support@rasa.io
