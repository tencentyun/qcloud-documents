## Overview

You can configure a bandwidth cap for the domain. When the bandwidth of the domain exceeds this cap within a statistical point (5 minutes), all access requests will be forwarded back to the origin server or the CDN service will be disabled, depending on your configuration (in either of the cases, a 404 error will be returned for all access requests).

When the bandwidth cap is reached, the domain will go into <font color="orange">Disabled</font> status whether it is set to forward the access request back to origin server or to return the 404 status code. It takes about <font color="orange">5 to 15 minutes</font> for the behavior of back-to-origin/returning 404 to take effect.


## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to **Domain Management** page. Then click the **Manage** button to the right of the domain name whose configuration is to be modified:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **Capped Bandwidth Configuration** in **Advanced Configuration**:

![](https://mc.qcloudimg.com/static/img/0a53afbcf5f33dd59c2ec4e9cc7824c4/2.png)


### Default Configuration

By default, capped bandwidth configuration is disabled.

### Configuring the Threshold

When capped bandwidth configuration is enabled, by default, the bandwidth cap is 10Gbps and when the cap is reached, "access request is forwarded to origin server":

![](https://mc.qcloudimg.com/static/img/d534483a485993d979cbab4bec715d54/3.png)

You can modify the cap as well as how to process user requests when it is reached:

![](https://mc.qcloudimg.com/static/img/771ee9889b358b9b3cfe0a22f5db0f36/4.png)


### Note

+ If the domain is disabled because the bandwidth cap is reached and you wish to continue using CDN service, you can manually activate the domain in the **Domain Management** page of the CDN console;
+ If your purpose is to prevent strong DDoS attacks, it is recommended to set to "return 404 for access request" to protect your origin server;
+ If your purpose is to control CDN service cost, it is recommended to set to "forward access request to origin server" to prevent your service from being affected.
