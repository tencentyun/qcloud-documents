## Overview

Origin Host Header refers to the site domain accessed by the CDN node at the origin server.

**Note:**

+ Origin server and origin host header: The IP/domain configured at the origin server allows the CDN node to find the origin server when it attempts to access the origin. There can be multiple WEB sites on the server, and the hosting source indicates on which site the resource resides.


## Configuration Instructions

Log in to [CDN Console](https://console.qcloud.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

Go to **Origin Configuration** in "Basic Configuration" to configure hosting source:

![](https://mc.qcloudimg.com/static/img/5440c6887c5120a103601f52167113dd/image.png)



### Default Configuration

By default, the origin host header of a sub-domain is the configured accelerated domain; The origin host header of a wildcard domain is the access domain:

![](https://mc.qcloudimg.com/static/img/df14797663acbdf2924702a4f49c0142/image.png)

+ If the accelerated domain connected is www.test.com, when the node sends an access request to origin server for the resource under this domain, the host field in the Request HTTP Header will be "www.test.com";
+ If the accelerated domain connected is a wildcard domain such as \*.test.com, and the access domain is abc.test.com, then the origin host header will be abc.test.com.


### Custom Configuration

You can set custom origin host header according to your business needs.

![](https://mc.qcloudimg.com/static/img/e6e934df080a16422d56f35bab8b312e/image.png)


### Note

- Currently, the configuration of origin host header is only available for domains with a connection method of **Own Origin**;
- Please make sure the origin host header domain you set is available for access, otherwise it will cause the failure of back-to-origin request, making your business affected.
