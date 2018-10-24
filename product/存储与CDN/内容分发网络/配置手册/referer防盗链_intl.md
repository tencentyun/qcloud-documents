## Overview

You can use the referer hotlink protection configuration feature provided by CDN to restrict the sources of access requests to your service resources. By setting a filtering policy for referer field value in user's HTTP Request Header, you can restrict the sources of access requests.

## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **referer Hotlink Protection** in "Access Control":

![](https://mc.qcloudimg.com/static/img/3ced38a341766341f11a7c2081cddb25/2.png)


### Default Configuration

By default, hotlink protection is disabled and no blacklist and whitelist exist.

### Custom Configuration

#### Configuring referer whitelist

Click **Edit** near the hotlink protection configuration section and select **referer whitelist** to configure the whitelist:

![](https://mc.qcloudimg.com/static/img/4ee23690f397cf7d079908a0aa9924fe/3.png)


If a user has configured a referer whitelist for domain "www.abc.com" with the following content:

> www.test.com

and **Includes blank referer** is unchecked, only the requests with a referer value of "www.test.com" are allowed to access the resource. For any other requests, a 403 error will be returned. 

##### Must-Know Facts About Whitelist

- If the referer field of a request matches the string set for the whitelist, the CDN node will return the requested information normally;
- If the referer field of a request does not match the string set for the whitelist, the CDN node will reject returning requested information and return the 403 status code;
- Once the whitelist is configured, the CDN node will only return the requested information for the requests that match the string in the whitelist;
- **When "Includes blank referer" is checked, CDN will return requested information normally if the referer field is blank or does not exist for a request (such as browser request).**

#### Configuring the Referer Blacklist

Click **Edit** near the hotlink protection configuration section and select **referer blacklist** to configure the blacklist:

![](https://mc.qcloudimg.com/static/img/61e7384edc25d148b4fa6c2774286102/4.png)

If a user has configured referer blacklist for domain "www.abc.com" with the following content:

> www.test.com

and **Includes blank referer** is unchecked, a 403 error will returned for any request with a referer value of "www.test.com". For any other requests, the requested information will be returned normally.

##### Must-Know Facts About Blacklist

- If the referer field of a request matches the string set for the blacklist, the CDN node will reject returning the requested information and return the 403 status code.
- If the referer field of a request does not match the string set for the blacklist, the CDN node will return the requested information normally;
- **When "Includes blank referer" is checked, the CDN will reject returning the requested information and return the 403 status code if the referer field is blank or does not exist for a request (such as browser request).**

### Note

- Referer blacklist and whitelist are not compatible with each other. You can only enable either of them at the same time;
- You can add a maximum of 400 entries for the hotlink protection feature, separated by line breaks (one entry per line).
- Hotlink protection supports the "domain name/IP" rule (prefix match). For example, if "www.abc.com" is set in the list, "www.abc.com/123" and "www.abc.com.cn" will be considered to match the list; if "127.0.0.1" is set in the list, "127.0.0.1/123" will be considered to match the list;
- Hotlink protection supports the use of wildcard. If "*.qq.com" is set in the list, "www.qq.com" and "a.qq.com" will be considered to match the list..


