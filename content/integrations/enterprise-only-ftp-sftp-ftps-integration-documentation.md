---
title: [ENTERPRISE ONLY] FTP / SFTP / FTPS Integration Documentation
source: https://help.rasa.io/enterprise-only-ftp-/-sftp-/-ftps-integration-documentation
keywords: contact management,FTP,SFTP,FTPS,subscriber list management,data synchronization,connection setup
---

Follow the steps below to set up and configure the integration using the FTP, SFTP, or FTPS methods.

**Step 1: Obtain Your Credentials**

To begin the integration process, you will need your FTP/SFTP/FTPS credentials from rasa.io. These credentials include the following information:

- **Hostname/Server Address:** ftp.rasa.io
- **Username:** [YourUsername]
- **Password:** [YourPassword]

**Note for SFTP users:** If you choose to use the SFTP method, please provide your Customer Success contact with your IP(s) to whitelist. You will not be able to connect using SFTP until this step is complete. **Please keep this in mind if you switch or add new IP addresses, it could cause a disruption to your transfers.**

**Step 2: Connect to ftp.rasa.io**

Using your preferred FTP client, connect to rasa.io's server (ftp.rasa.io) using the provided credentials. Ensure that your connection is secure by choosing the appropriate protocol (FTP, SFTP, or FTPS) based on your preference and security requirements.

**Step 3: Configure File Export**

After successfully connecting to the rasa.io server, configure your file export settings within your CRM or AMS. Set up your subscriber list file to land in the designated folder created for you on the server. This folder is where rasa.io will retrieve the data for processing.

**Step 4: Prepare Your Subscriber List**

Your subscriber list should, at a minimum, include a column for email addresses. Additionally, you can include other fields such as first name, last name, and segment code (if utilizing rasa.io's segments feature). Ensure that your data is formatted correctly, and each column is labeled appropriately.

**Step 5: Choose List Update Method**

rasa.io offers two methods for updating your subscriber list:

- **Full List Replacement:** Replace the entire list with the most recent version during each sync. **Note:** It is recommended to perform a full list replacement only if subscribes or unsubscribes are managed through a form hosted on your site.
- **Incremental Add/Update:** Add new subscribers and update existing ones without replacing the entire list. This is a good option if rasa.io is housing your unsubscribe form / list.

**Step 6: Schedule List Sync**

Decide on the frequency of list synchronization. You can choose to sync the list every night or at a frequency that suits your needs, we will process the files overnight. Ensure that your sync schedule aligns with your data update frequency and list management practices.

**Step 7 (OPTIONAL but highly recommended):** **Include Record Count File for Verification**

To enhance the integrity of your synchronization process, it is recommended to include a record count file along with your subscriber list. This file provides a count of the records being transferred and serves as a verification mechanism. **Including a record count file adds an extra layer of assurance, helping to maintain the accuracy and completeness of your subscriber list during each synchronization.**

- **Generate Record Count File:** Before initiating the file transfer, generate a record count file that includes the total number of records in your subscriber list. This file should be a simple text document containing a single number, representing the count of records.
- **File Naming Convention:** Name the record count file in a way that clearly associates it with the corresponding subscriber list file. For example, if your subscriber list file is named "subscriber\_list.csv," name the record count file "subscriber\_list\_count.txt."
- **Placement in the Same Folder:** Ensure that the record count file is placed in the same folder as your subscriber list file on the Rasa.io server. This facilitates easy retrieval and verification.

**Verification Process:**

During the synchronization process, rasa.io will check the received record count against the actual number of records in the subscriber list file. If, for any reason (e.g., connection drop, incomplete upload), the record count and the received file become mismatched, the system will void the sync. In such cases, rasa.io will default to the last successful import to prevent the potential issue of under-sending your newsletter to an incomplete list.

**Pushing Data Back to Your System**

Exciting news! We've recently enhanced our integration capabilities to allow for the seamless transfer of data back to your system. Now, not only can you effortlessly sync your subscriber lists to rasa.io, but you can also push data back to your CRM or AMS. This two-way data flow ensures that your systems stay updated with the latest subscriber information, providing a comprehensive solution for managing your audience.

In the file we return to you, we can include any and all of the following data points for all subscribers:

- opt-outs
- open and click counts
- date of last open and click
- topical data

If you encounter any issues or have further questions, please refer to the rasa.io support team at support@rasa.io or reach out to your dedicated Customer Success representative for assistance.
