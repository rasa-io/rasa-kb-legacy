---
title: Email Validation Process for CSV Uploads
source: https://help.rasa.io/email-validation-process-for-csv-uploads
keywords: deliverability,email validation,csv upload
---

_Our enhanced email validation process for CSV uploads ensures high deliverability, compliance, and data hygiene by classifying email addresses into specific categories and providing actionable insights._

###### **Process Overview**

1. **Upload CSV File**

   - User uploads email list in CSV format.
2. **Validation and Analysis**

   - The system evaluates addresses based on metrics and statuses described above.
3. **Detailed Reporting**

   - A comprehensive report is provided, breaking down deliverability status, sub-statuses, and recommended actions.
   - This information is not readily available to the rasa.io team. Please contact to discuss obtaining this reporting.

###### **Classifications:**

###### **Valid Emails**

These addresses are safe to email and have a bounce rate below 2%.

- **Alias\_address:** Valid but act as forwarders (e.g., "info@example.com" forwards to "user@example.com"). An alias is a valid email address, and your email will not bounce.
- **Leading\_period\_removed:** Gmail addresses starting with `.` are adjusted for compatibility.
- **Alternate:** These emails are valid but likely to be secondary addresses for the users. Alternate emails are often used to sign up for accounts but do not see much engagement.

###### **Invalid Emails**

Addresses that cannot receive emails and should be removed. Emails that are undeliverable due to syntax issues, inactive domains, or other permanent errors.

- **Sub-Statuses:**
  - **Does\_not\_accept\_mail:** Domain only sends but does not receive emails.
  - **Failed\_syntax\_check:** Emails that fail RFC syntax protocols.
  - **Mailbox\_not\_found:** These emails addresses are valid in syntax, but do not exist.
  - **No\_dns\_entries:** These emails are valid in syntax, but the domain doesn't have any DNS records or incomplete DNS Records. Therefore, mail programs will have difficulty delivering emails to them or be entirely unsuccessful.
  - **Mailbox\_quota\_exceeded** - These addresses exceeded their space quota and no longer accept emails (temporarily).

- - **Unroutable\_ip\_address:** These email domains point to an unroutable IP address.

###### **Catch-All Emails**

Impossible to fully validate without sending an email. While deliverable in some cases, they carry a higher bounce risk.

- Indicates domains configured to accept all emails, making validation uncertain.

###### **Spamtrap Emails**

Addresses likely set as spam traps. Avoid emailing these to prevent blacklisting.

###### **Abuse Emails**

These emails are of people known to click the abuse links in emails, hence abusers or complainers. We recommend not emailing these addresses.

###### **Do Not Mail**

These are company emails, role-based, or simply addresses you should avoid emailing. They are broken down into 6 sub-categories

- **Sub-Statuses:**
  - **Disposable:** These email addresses are temporary and become invalid after a set period. Avoid adding disposable emails to your list to avoid future bounces.
  - **Role\_based:** These emails belong to a position or a group of people, like sales@ info@ and contact@. Role-based emails strongly correlate to people reporting emails sent to them as spam and abuse.
  - **Toxic:** These email addresses are known for abuse and spam. They may also be bot-created emails. If any of your emails possess this flag, you shouldn't email them. We also provide additional fields that you should consider before emailing.
  - **Global\_suppression:** These emails are found in many popular global suppression lists (GSL). They consist of known ISP complainers, direct complainers, purchased addresses, domains that don't send mail, and known litigators.Found in widely known suppression lists.
  - **Possible\_trap:** These emails contain keywords that might correlate to possible spam traps like spam@ or @spamtrap.com. Examine these before deciding whether to send emails to them or not.

###### **Why Do Not Mail?**

The **Do Not Mail** category is crucial for protecting your IP/domain reputation. It flags addresses likely to harm email campaigns, ensuring your emails land in inboxes, not spam folders.

###### **Unknown Emails**

Validation could not determine a result due to issues like offline servers or anti-spam measures.

- **Sub-Statuses:**
  - **Antispam\_system** - These emails have anti-spam systems deployed that are preventing us from validating these emails. You can submit these to us through the contact us screen.
  - **Exception\_occurred** - These emails caused an exception when validating. If this happens repeatedly, please let us know.
  - **Failed\_smtp\_connection** - These emails belong to a mail server that won't allow an SMTP connection. Most of the time, these emails will end up being invalid.
  - **Forcible\_disconnect** - These emails belong to a mail server that disconnects immediately upon connecting. Most of the time, these emails will end up being invalid.
  - **Greylisted** - Greylisting technology is temporarily preventing the validation attempt. If you resubmit these emails, they will often validate on a second pass.
  - **Mail\_server\_did\_not\_respond** - These emails belong to a mail server that is not responding to mail commands. Most of the time, these emails will end up being invalid.
  - **Mail\_server\_temporary\_error** - These emails belong to a mail server returning a temporary error. Most of the time, these emails will end up being invalid.
  - **Timeout\_exceeded** - These emails belong to a mail server that responds slowly. Most of the time, these emails will end up being invalid.

###### **Best Practices**

- Regularly validate and clean email lists.
- Avoid risky addresses flagged by the system.
- Monitor and address SMTP bounce codes for insights on deliverability issues.

This process ensures that your newsletters are effective, compliant, and capable of maintaining a strong sender reputation.
