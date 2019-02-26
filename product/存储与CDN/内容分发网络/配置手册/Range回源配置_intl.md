## Overview
CDN provides Range GETs Configuration feature which can effectively reduce back-to-origin rate of large files and improve response speed.

<font color="orange">The origin server is required to support Range requests</font>

## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **Range GETs Configuration** in "Origin Configuration":

![](https://mc.qcloudimg.com/static/img/bed21c4d2061d405f30645b160dcd9a8/2.png)

### Default Configuration
By default, Range GETs Configuration is **Enabled**.

### Result of Configuration

If a user makes a request for resource: ```http://www.test.com/test.apk```when the node receives the request and finds out that the cached test.apk has expired, it will send a back-to-origin request.

**When Range GETs Configuration is enabled:**

+ The node will use a Range back-to-origin request to acquire the resource in slices.
+ If the request sent from the user is also a Range request, when the slices stored on the node meet the condition, they will be directly returned to the user, who needs not to wait for all slices.


**When Range GETs Configuration is disabled:**

+ The node will get the entire resource directly from the origin server

**Note**:

+ The origin server is required to support Range requests, otherwise the back-to-origin request will fail;
+ If the resource has never been cached on this node, the resource will not be returned in slices for the initial back-to-origin request;
+ When Range GETs Configuration is enabled, resources will be cached in slices on the node, but all slices have the same cache expiration time and follow the cache expiration rule specified by the user.
