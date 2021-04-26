## Overview
SEO optimization configuration is designed to deal with the problem that the domain authority on search engines will be affected by the frequent changes of IP address made by CDN following the connection of domain to CDN. By identifying whether the accessing IP belongs to a search engine and allowing users to choose to access resources directly from origin server, the feature can ensure a consistent domain authority on search engines.
Once SEO optimization configuration feature is enabled, requests from search engines will be directed to the origin server while other requests will access the CDN node normally.


## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **SEO Optimization** in "Advanced Configuration":

![](https://mc.qcloudimg.com/static/img/18bc9019b47152b2e214e1ca6a4296e8/2.png)

+ SEO optimization is only available when connection method is **"Own origin"**. Once SEO optimization is enabled, **if the domain has multiple origin server addresses, the default origin address for back-to-origin requests will be the first one added**;
+ If the CNAME of the current domain is an old CNAME (as shown below), you need to update it to a new CNAME to use SEO optimization configuration feature.

![](https://mc.qcloudimg.com/static/img/4e2b1880d2da85c39930f713996dd93b/1.png)

How to update CNAME:
+ Submit a ticket to request to change the CNAME of the domain to a new one;
+ Go to your domain resolution service provider and switch the CNAME resolution of the domain to a new CNAME;

Note: Due to the frequent updating of IP addresses for search engines, Tencent Cloud CDN can only ensure to identify the majority of search engine IP addresses.
