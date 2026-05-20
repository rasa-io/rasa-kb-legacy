---
title: iMIS Integration Documentation
source: https://help.rasa.io/imis-integration-documentation
keywords: contacts,integrations,imis,imis integration,API endpoint,IQA QueryName,one-way integration,integration dashboard,contact management,iMIS EMS
---

_Our step-by-step guide to integrating your contacts with iMIS. Note: This is a one way integration._

###### Required Information

Before proceeding, ensure you have the following information from your iMIS system:

1. **API Endpoint**: This is the URL for accessing the iMIS API.
2. **IQA QueryName**: The specific IQA query you wish to run, such as `$/Common/Queries/Search/Contact`.
   1. **Note**: Include member ID in the IQA
3. **Username**: Your iMIS username.
4. **Password**: Your iMIS password.

###### Integration Steps

1. **Accessing the Integration Dashboard**

   - Navigate to the rasa.io integration dashboard.
   - Locate the iMIS integration section.
2. **Entering Required Information**

   - **API Endpoint**: Enter your iMIS API endpoint URL.
     - Example: `https://yourimiswebsite.org/api/endpoint`
   - **IQA QueryName**: Enter the IQA QueryName.
     - Example: `$/Common/Queries/Search/Contact`
   - **Username**: Enter your iMIS username.
   - **Password**: Enter your iMIS password.
3. **Authenticate**

###### Special Instructions for iMIS EMS and Earlier Versions

For users on earlier versions of iMIS and not on iMIS EMS, the endpoint format includes the instance name. The format is as follows:

- **Endpoint Format**: `URL/instance name/api/endpoint`

**Example**:

- If your public iMIS website URL is `https://abc.org` and the website instance name is `abcmembers`, to call the party endpoint, the full API URL would be:
  - `https://abc.org/abcmembers/api/party`

###### Troubleshooting

- Ensure that all fields are filled out correctly.
- Double-check the endpoint URL format for your specific version of iMIS.
- Verify that your IQA QueryName is accurate and correctly formatted.

If you encounter any issues, please contact rasa.io support for further assistance.
