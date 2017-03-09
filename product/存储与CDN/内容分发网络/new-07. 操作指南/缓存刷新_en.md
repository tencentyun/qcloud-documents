The update mechanism for the resources cached on the nodes in CDN is generally controlled by the cache expiration time. Configuring a reasonable cache expiration time policy can effectively reduce back-to-origin rate. For more details, please refer to [Cache Expiration](https: //www.qcloud.com/doc/product/228/6290) in CDN Configuration Manual. When resources have been updated at your origin server, you can use the cache refresh feature if you want users to directly get new resources, instead of old ones, during access.

When resources have been updated at your origin server, you can use CDN's resource prefetch feature to cache the resources at the origin server to all CDN nodes.

<font color="red">URL prefetch feature is under a gray release. It will be fully available in the future.</font>

## URL Refreshing

Log in to [CDN Console](https://console.qcloud.com/cdn), select "Cache Refresh" menu on the left, and then select "URL Refresh":

![](https://mccdn.qcloud.com/static/img/87acfaeaee3fc0f31e5753ad90b776ba/image.png)

Enter the URLs of objects to be refreshed (must contain http:// or https://), one per line, for example: http://www.abc.com/test.html.

**Note:**

+ A maximum of 10,000 URLs are allowed to be refreshed each day and a maximum of 1,000 URLs are allowed to be submitted for each refresh. It takes about 5 to 10 minutes for the refresh to take effect;
+ Once a URL is refreshed, the resource from the URL will be set to expired if they have been cached on the CDN nodes across the network. When user's request reaches a node, the node will pull the requested resource from the origin server and then cache it while returning it to the user. In this way, it can be guaranteed that users can get the up-to-date resources;
+ It takes 5 minutes for the file refresh to take effect. If the cache validity period set for the file is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the refresh tool.


## Directory Refresh

Log in to [CDN Console](https://console.qcloud.com/cdn), select the "Cache Refresh" menu on the left, and then select the "Directory Refresh":

![](https://mc.qcloudimg.com/static/img/207fbcf44c416b3324e839e47c739c5a/image.png)

Enter the URLs of directories to be refreshed (must contain http:// or https://), one per line, for example: http://www.abc.com/test/.

**Note:**

+ A maximum of 100 directories are allowed to be refreshed each day and a maximum of 20 directories are allowed to be submitted for each refresh. It takes about 5 to 10 minutes for the refresh to take effect;
+ It takes 5 minutes for the file refresh to take effect. If the cache validity period set for the file is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the refresh tool.


## URL Prefetch

Log in to [CDN Console](https://console.qcloud.com/cdn), select "Cache Refresh" menu on the left, and then select "Prefetch URL":
![](https://mc.qcloudimg.com/static/img/9382c4263460e6031b757ddb9dc0b2c5/image.png)

Enter the URLs of objects to be prefetched (must contain http:// or https://), one per line, for example: http://www.abc.com/test.html.

**Note:**
+ If the resource has been cached on the node and has not expired, it will not be updated to the latest one. If you need to update the resources on all CDN nodes to the latest ones, you can refresh them before prefetch.
+ A maximum of 1000 URLs are allowed to be prefetched each day and a maximum of 20 URLs are allowed to be submitted for each prefetch. It takes about 5 to 10 minutes for the prefetch to take effect, depending on the file size;


## Task Query

You can query the status of submitted refresh and prefetch tasks in "History" section.











