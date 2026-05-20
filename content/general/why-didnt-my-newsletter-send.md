---
title: Why didn't my newsletter send?
source: https://help.rasa.io/why-didnt-my-newsletter-send
keywords: support,content,domain authentication,Email,email troubleshooting,newsletter not sending,content requirements,article settings,minimum article count,schedule settings,SPAM folder,sending schedule
---

_Most “non-sends” aren’t delivery problems—they’re generation problems. This article shows you how to confirm a newsletter did not generate, the most common reasons why, and what to do next._

###### How to Tell Your Newsletter Didn’t Generate

Check these in order:

1. **Analytics › Daily Stats**

   - The **current newsletter date** does **not** appear in the date dropdown.
2. **Content › Upcoming**

   - The articles you expected to be used are **still sitting in Upcoming** (i.e., they were not consumed to build a send).
3. **Content › History**

   - There is **no entry** for that send date in the History dropdown.

If all three are true, the issue is **generation**, not delivery.

> Note: If your newsletter had generated, you would see the send date in Analytics and History, and Upcoming would be largely empty or refreshed.

If it is a delivery issue, [see more on how to troubleshoot here](https://help.rasa.io/checking-newsletter-delivery-status).

---

###### Most Common Reason: Content Requirements Not Met

Your newsletter will only generate if your content settings can be satisfied at the scheduled time.

###### Where to check

- Go to **Preview / Newsletter Settings** and confirm your:

  - **Minimum articles** (the lowest total needed to build a send)
  - **Maximum articles**
  - **Max per source** (the most that can be taken from any single source)

Then compare those settings to what was available **at generation time**:

###### How to compare correctly

1. **Open Content › Upcoming**

   - Review the articles and their **publish dates**.
   - Remember the **cutoff window**: items appearing **after** your scheduled send time would **not** have been eligible when the system attempted to generate.
   - Ask: *“At the scheduled time, were there at least **[****Min #]**eligible articles available?”*
2. **Account for “Max per source”**

   - Even if you had enough total articles, generation can fail if too many came from the same source and your **max-per-source** constraint blocked using them.
   - Ask: *“Could I reach the Minimum using the allowed number from each source?”*
3. **Consider Scheduled Content (if you use it)**

   - If you rely on scheduled items, confirm they were **scheduled for before** the send time and still **eligible**.

If your available, eligible articles couldn’t meet **Minimum** under your **max-per-source** rules, the system will **not** generate a newsletter.

###### Other Rare Causes

In some uncommon cases, a newsletter may fail to generate because:

- A **source unpublished** content or temporarily became **unavailable** around the generation window.
- This can happen if the RSS feed or site structure changed between your last successful generation and your current send.

If you suspect this might be the case, check your **Sources** list to confirm each is still active and returning new content.

  

---

###### Quick Fixes (Right Now)

- If you need to go out **today**:

  1. **Lower your Minimum** temporarily (in **Preview / Newsletter Settings**) to match what’s actually available.
  2. **Loosen max-per-source** just enough to allow the system to reach Minimum.
  3. **Add eligible content** (sources or scheduled items) that fits within the cutoff window.
  4. **Schedule** a manual send. Be sure to switch it back to the automatic schedule after.

> Tip: Make small, reversible changes—note the original settings so you can restore them later.

---

###### Prevent It Next Time

- **Set a realistic Minimum** based on your typical daily content volume.
- **Tune max-per-source** so one prolific source doesn’t block you from reaching Minimums.
- **Broaden sources** or adjust filters so you consistently have enough eligible items by send time.
- **Verify the cutoff window** aligns with when your sources usually publish.

---

###### Still Didn’t Generate But Content Looks Sufficient?

If, after reviewing Upcoming (with correct publish-time context), Min/Max, and max-per-source, it **looks like you had enough** eligible content and it still didn’t generate:

- Contact **support@rasa.io** with:

  - Your **send date/time**
  - A screenshot or list showing **Upcoming** items and publish dates
  - Your **Min/Max and max-per-source** settings from **Preview / Newsletter Settings**

> Rest assured: If there were a **system-wide** generation issue, you would see a **notification in your dashboard**. That’s rarely the case.

---

###### TL;DR Checklist

- ❌ **Date missing** in Analytics & History?
- ❌ **Articles still in Upcoming** for that send?
- ✅ Then it **didn’t generate**.

Next, verify:

- 🔢 **Min/Max** in **Preview / Newsletter Settings**
- 🧱 **Max per source** didn’t block you
- ⏰ Articles were **eligible by send time** (publish dates before cutoff)

If everything checks out but it still didn’t generate → **support@rasa.io**.
