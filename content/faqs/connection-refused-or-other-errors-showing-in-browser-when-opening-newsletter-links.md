---
title: 'Connection Refused' or Other Errors Showing in Browser When Opening Newsletter Links
source: https://help.rasa.io/connection-refused-error
keywords: security,browser,links,error,browser issues,clear cache,VPN issues,connection refused,DNS error
---

Like most email services, our system uses link tracking to gather insights about email engagement and effectiveness. This is achieved by temporarily redirecting links through our tracking domain, 'links.rasa.io'. When you click on a link in our emails, you may notice the URL 'links.rasa.io' appear briefly in your browser's address bar before it resolves to the intended webpage. This process is essential to tracking interactions within email and is typically very quick and seamless.

**While this tracking process is designed to be seamless, there are occasions where you might encounter browser errors such as 'Connection Refused' (ERR\_CONNECTION\_REFUSED) or DNS errors (DNS\_PROBE\_FINISHED\_NXDOMAIN). Let’s explore why these errors occur and how to resolve them.**

The connection issues you encounter, such as 'Connection Refused', are typically caused by one of two factors: network security settings or computer security software. Both of these are designed to protect your digital environment but can occasionally interfere with the normal operation of link tracking even when the links are completely safe.

###### First, you will want to identify whether it is your network or computer security software.

If you have security software enabled such a Bitdefender, Microsoft Essentials or McAfee, try disabling it temporarily. Do the links work while disabled? **If yes, this is a security software issue. In this case, you will need to access the admin settings in the software and add "links.rasa.io" as a trusted site.**

Are you on a VPN? When you disconnect from your VPN, do the links work? **If yes, this is likely a network issue.**

If you are not using a VPN and simply using a personal or company Wi-Fi network, try connecting to a different network (ex. use your mobile phone - be sure to disconnect Wi-Fi to use cellular data), do the links work? **If yes, this is likely a network issue.**

###### Here are some steps you can take to troubleshoot these network issues:

**1. Check Your Network Connection**

Many browser issues, including 'Connection Refused' errors, can stem from network problems. Try these quick fixes:

- **Restart your router**: This simple step often resolves connection issues.
- **Evaluate your WiFi**: Ensure you're not on a slow or unstable connection.

**2**. **Clear Your Browser’s Cache**

Browsers like Chrome store data in your cache to load pages faster on subsequent visits. However, an outdated cache can lead to issues such as connection errors. Clearing your cache can often resolve these discrepancies between stored and live versions of a page.

**3**. **Disable Outdated Chrome Extensions**

Incorrectly coded or outdated extensions can easily cause connection issues.

**4**. **Clear Your DNS Cache**

Your operating system, like your browser, stores a DNS cache that contains temporary entries of visited web pages. This speeds up page loading by avoiding repeated DNS server requests. However, if these entries are outdated, they can cause errors such as 'ERR\_CONNECTION\_REFUSED'. Clearing your DNS cache can resolve these issues. The method for doing so varies by operating system.

If you have taken the above steps to troubleshoot and still are unable to access the links in your rasa.io newsletter, please reach out to support@rasa.io so that we can further investigate.
