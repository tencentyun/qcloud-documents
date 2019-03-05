The update mechanism for the resources cached on the nodes in CDN is generally controlled by the cache expiration time. Configuring a reasonable cache expiration time policy can effectively reduce origin-pull rate. For more details, please refer to [Cache Expiration](https://cloud.tencent.com/doc/product/228/6290) in CDN Configuration Manual. When resources have been updated at your origin server, you can use the cache refresh feature if you want users to directly get new resources, instead of old ones, during access.

When resources have been updated at your origin server, you can use CDN's resource prefetch feature to cache the resources at the origin server to all CDN nodes.

URL prefetch feature is under a Gray-box release. It will be fully available in the future.

## Purge URL

Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select **Purge Cache** menu on the left, and then select **Purge URL**:

![](https://mc.qcloudimg.com/static/img/95184d6e47c917fddc8ec0ef58a94925/1.png)

Enter the URLs of objects to be refreshed (must contain http:// or https://), one per line, for example: `http://www.abc.com/test.html`.

**Note:**

+ A maximum of 10,000 URLs are allowed to be refreshed each day and a maximum of 1,000 URLs are allowed to be submitted for each refresh. It takes about 5 to 10 minutes for the refresh to take effect;
+ Once a URL is refreshed, the resource from the URL will be set to expired if they have been cached on the CDN nodes across the network. When user's request reaches a node, the node will pull the requested resource from the origin server and then cache it while returning it to the user. In this way, it can be guaranteed that users can get the up-to-date resources;
+ It takes 5 minutes for the file refresh to take effect. If the cache validity period set for the file is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the refresh tool.


## Purge Directory

Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select the "Purge Cache" menu on the left, and then select the "Purge Directory":

![](https://mc.qcloudimg.com/static/img/02e28f79c50438007c8a4f70c14f8b82/2.png)

Enter the URLs of directories to be refreshed (must contain http:// or https://), one per line, for example: `http://www.abc.com/test/`.

**Note:**

+ A maximum of 100 directories are allowed to be refreshed each day and a maximum of 20 directories are allowed to be submitted for each refresh. It takes about 5 to 10 minutes for the refresh to take effect;
+ It takes 5 minutes for the file refresh to take effect. If the cache validity period set for the file is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the refresh tool.


## URL Prefetch

Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select "Purge Cache" menu on the left, and then select "Prefetch URL":
![](https://mc.qcloudimg.com/static/img/4d2c6fdb38a739a8f1910d68d7067e8b/3.png)

Enter the URLs of objects to be prefetched (must contain http:// or https://), one per line, for example: `http://www.abc.com/test.html`.

**Note:**
+ If the resource has been cached on the node and has not expired, it will not be updated to the latest one. If you need to update the resources on all CDN nodes to the latest ones, you can refresh them before prefetch.
+ A maximum of 1000 URLs are allowed to be prefetched each day and a maximum of 20 URLs are allowed to be submitted for each prefetch. It takes about 5 to 30 minutes for the prefetch to take effect, depending on the file size;


## Task Query

You can query the status of submitted refresh and prefetch tasks in "History" section.
