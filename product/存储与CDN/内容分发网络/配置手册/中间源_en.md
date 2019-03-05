## Overview

An intermediate node can be considered as a secondary cache node. When a user sends a request, it will first reach the edge node. If this node doesn't have the requested resource, it will send request to the intermediate node, which will then send the request to the origin server if it still does not have the requested resource.

Once intermediate node is enabled, access requests to origin from users will be converged at this node. The node will then acquire the requested data from the origin in a centralized manner, reducing the pressure on the origin server.

<font color="red">It is recommended to enable intermediate node in order to improve your CDN acceleration and reduce back-to-origin bandwidth.</font>

## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

Go to **Intermediate Node Configuration** under "Origin Configuration" to enable intermediate node:

![](https://mc.qcloudimg.com/static/img/fc5a1ad63147a184d38ea072484ce0ed/2.png)

The intermediate node configuration is disabled by default.





