## Overview

CDN's parameter filtering switch allows you to control whether to filter out parameters following the question mark in the user request URLs based on your business needs. You can use this feature to achieve versioning with flexibility, or to perform Token-based authentication against resources.



## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **Ignore Parameter** in "Access Control" to set parameter filtering:

![](https://mc.qcloudimg.com/static/img/6d5d13d6de3a11221fb89ad15f545b13/2.png)



### Default Configuration

The switch is disabled by default. In this case, parameters following the "?" in user request URLs  will not be ignored.

1. For example, if the URL of resource requested by a user is ```http://www.test.com/1.jpg?version=1.1```, and the requested content is not cached on the node which receives this request, the resource will be acquired from the origin server and then cached to the node;
2. If the user requests for resource with URL: ```http://www.test.com/1.jpg?version=1.1```again, and the resource has been already cached on the node, the resource will be hit and directly returned to the user;
3. If the user then requests for resource with ```http://www.test.com/1.jpg?version=1.2 ```, which does not match the full path of resource because parameter filtering is disabled, thus the resource will be pulled from the origin server again.

### Enabling Parameter Filtering

When the parameter filtering configuration is enabled, parameters following the "?" in user request URLs will be ignored.

1. For example, if the URL of resource requested by a user is ```http://www.test.com/1.jpg?version=1.1 ``` and the content is not cached on the node which receives this request, the resource will be acquired from the origin server and then cached to the node. With parameter filtering enabled, the resource URL stored by the node will be ```http://www.test.com/1.jpg```;
2. If the user requests for resource with URL: ```http://www.test.com/1.jpg?version=1.1```again, the actual resource that be looked up on the node will be ```http://www.test.com/1.jpg```, which has already been cached, thus the resource is hit and directly returned to the user;
3. If the user then requests for resource with URL: ```http://www.test.com/1.jpg?version=1.2```, the actual resource that be looked up on the node will be ```http://www.test.com/1.jpg```, which has already been cached, thus the resource is hit and directly returned to the user.


