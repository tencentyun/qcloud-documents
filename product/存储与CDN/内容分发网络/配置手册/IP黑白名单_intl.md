## Overview
CDN provides IP Blacklist&Whitelist Configuration feature which allows you to set up filtering policies for the source IPs of user requests based on your business needs to prevent various problems such as cheating and attacks from malicious IPs.


## Configuration Instructions
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **IP Blacklist & Whitelist** configuration in "Access control":![](https://mc.qcloudimg.com/static/img/3df7a73facd5c400d3b61ebb660790c3/2.png)


### Default Configuration
By default, IP blacklist & whitelist feature is disabled and no blacklist and whitelist exist.


### Custom Configuration
#### Configuring IP Whitelist
Click **Edit** button and select **Whitelist** to configure whitelist:
![](https://mc.qcloudimg.com/static/img/58958ebb4f01092c74b6a71769f2e994/3.png)

Assume that a user has configured IP whitelist for domain "www.abc.com" with the following content:

> 1.1.1.1
> 2.2.2.2/24

This indicates that the requested content can be returned successfully **only if** the source IP of the request is 1.1.1.1 or matches the network segment 2.2.2.2/24. A 403 error will be returned for any request that does not meet the condition. 


#### Configuring IP Blacklist
Click **Edit** button and select **Blacklist** to configure blacklist:
![](https://mc.qcloudimg.com/static/img/9a73b80493da1519b15e3783fee2952f/4.png)

Assume that a user has configured IP blacklist for domain "www.abc.com" with the following content:

> 3.3.3.3
> 4.4.4.4/16

This indicates a 403 error will be returned **only if** the source IP of the request is 3.3.3.3 or matches the network segment 4.4.4.4/16. For any other requests, the requested content will be returned.


### Note
+ IP blacklist and whitelist are not compatible with each other. You can only enable either of them at the same time;
+ You can add a maximum of 100 entries, separated by line breaks (one entry per line);
+ Currently, only network segments of the following formats are supported: /8, /16, /24, /32. Any other segment formats are not supported;
+ When both lists are empty, it means that IP blacklist & whitelist feature is currently disabled.



