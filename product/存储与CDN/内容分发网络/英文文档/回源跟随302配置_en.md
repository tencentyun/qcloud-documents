## Overview
CDN provides "Follow 302 Configuration" feature.

## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **Follow 302 Configuration** in "Origin Configuration":

![](https://mc.qcloudimg.com/static/img/f1105290fdd59da3c9c68c915a18462b/2.png)

### Default Configuration
By default, Follow 302 Configuration is **disabled**.

### Result of Configuration

For example, if a user requests for resource ```http://www.test1.com/1.jpg``` and the resource isn't cached on the node, the node will request to acquire the resource from the origin server. If the HTTP Response status code sent from the origin server is 302, the request will be redirected to ```http://www.test2.com/2.jpg```. 

**When Follow 302 Configuration is disabled**:

+ Since the resource is not cached in cased of status code 302, the node will directly transmit the HTTP Response to the user.
+ When a user sends request to ```http://www.test2.com/2.jpg```, there will be no acceleration if this domain is not connected to CDN.
+ If another user sends a request to ```http://www.test1.com/1.jpg``` at this point, the above process will be repeated.

**When Follow 302 Configuration is enabled**:

+ When Follow 302 Configuration is enabled, the node will directly request for the resource if it receives the status code 302 as HTTP Response.
+ The resource will be acquired, cached to the node and then returned to the user.
+ If another user also sends a request for ```http://www.test2.com/1.jpg```, the resource will be hit on this node. 

**Note**:
+ When Follow 302 Configuration is enabled, a maximum of **3 redirections** are allowed. If the limit is exceeded, status code 302 will be returned directly to the user.

