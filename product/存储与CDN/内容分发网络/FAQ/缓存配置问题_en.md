### 1. What is cache expiration configuration?
Cache expiration configuration refers to a set of expiration policies the CDN acceleration nodes should follow when caching your business contents.
User resources cached on CDN nodes may be "Expired". If a resource cached on a node is not expired, when a user request for the resource reaches the node, the node will directly return the cached resource to the user to speed up the resource acquisition. If a resource is beyond the set validity period and thus becomes expired, the node will forward the user request for the resource to the origin server, reacquire and cache the resource, and then return it to the user. A reasonable cache validity period can effectively improve the resource hit rate and reduce origin-pull rate so as to save bandwidth.

### 2. What is advanced cache configuration?
Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select "Domain Management" in the left navigation bar, and click "Manage" in the right of the domain name to be edited.
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
In the Cache Expiration Configuration module, click on the **Advanced Cache Expiration Configuration** switch to enable it.
![](https://mc.qcloudimg.com/static/img/253949748892d15c5340f341b99af32f/advanced_cache.png)
After that, the following results are achieved.
When a user requests for a certain resource from the origin server and the Response HTTP Header includes the Cache-Control field with a value of max-age=xxxx, the cache validity period for the resource on the node will be subject to the smaller one between the set validity period and max-age:
- For example, if the max-age set for the /index.html of the origin server is 200 seconds and the cache validity period set for CDN is 600 seconds, the actual cache validity period for the file is 200 seconds.
- If the max-age set for the /index.html of the origin server is 800 seconds and the cache validity period set for CDN is 600 seconds, the actual cache validity period for the file is 600 seconds.

> **Note:** If the Cache-Control field does not exist in the Response Header of your origin server, CDN adds the "Cache-Control:max-age=600" header by default.

### 3. How to control the file cache time in a browser?
Tencent Cloud CDN supports the Cache-Control configuration on the origin server by default, but configuration of the Cache-Control header is not supported. max-age cannot be configured on CDN nodes, but CDN nodes can inherit the origin server's max-age. To configure max-age on CDN nodes, you only need to configure the max-age on the origin server.

### 4. How to adjust the priority of cache configuration?
For more information, please see [Priority Adjustment](https://cloud.tencent.com/document/product/228/6290#.E4.BC.98.E5.85.88.E7.BA.A7).

### 5. Can CDN self-owned origin be configured to not cache a certain file? Does it mean "do not cache" if the cache validity period is 0?
You can configure different cache validity periods for different types of directories and files. If the cache validity period is configured to 0, the CDN node will not cache the resource, in which case the CDN node needs to pull related resources from the origin server every time the users send access request to the node. For more information on cache configurations, please see [Cache Expiration Configuration](https://cloud.tencent.com/document/product/228/6290).

### 6. Which cache expiration configuration does Tencent Cloud support?
Tencent Cloud CDN supports cache validity period configuration at various dimensions, custom priority adjustment, and cache inheritance policies (advanced cache configuration). A reasonable cache validity period can effectively improve the resource hit rate and reduce origin-pull rate, so as to save bandwidth.

### 7. What is the default cache configuration of CDN?
Default configuration is as follows when a domain accesses:
Self-own origin domain connection: By default, the cache validity period for all files is 30 days while that of the general dynamic files (such as .php, .jsp, .asp, .aspx) is 0 by default, which means any request for such files will be directly forwarded to the origin server.
COS origin domain access: By default, the cache validity period for all files is 30 days.
Advanced cache expiration configuration is disabled by default.

### 8. What are cache inheritance policies?
When a user makes a request for a certain business resource, the origin server's Response HTTP Header includes the Cache-Control field. The default policy is as follows:
If the Cache-Control field is max-age, the cache validity period for this resource is subject to the one set for the resource, instead of inheriting the value specified by max-age.
If the Cache-Control field is no-cache or no-store, the CDN node does not cache the resource.

### 9. What are cache matching rules?
When multiple caching policies are set, the priorities of the entries are determined on a bottom-to-top basis, with the entry at the bottom of list having the highest priority and the one at the top having the lowest priority. For example, if the following caching policies are set for a domain:
> All files (30 days)
> .php .jsp .aspx (0 second)
> .jpg .png .gif (300 seconds)
> /test/*.jpg (400 seconds)
> /test/abc.jpg (200 seconds)

If a domain name is ```www.test.com```, and the resource is ```www.test.com/test/abc.jpg```, the matching rule is as follows:
1. Match with the first entry. It is hit, so the cache validity period is 30 days.
2. Match with the second entry. It is not hit.
3. Match with the third entry. It is hit, so the cache validity period is 300 seconds.
4. Match with the fourth entry. It is hit, so the cache validity period is 400 seconds.
5. Match with the fourth entry. It is hit, so the cache validity period is 200 seconds.

The final cache validity period is subject to the last matching result, that is 200 seconds.
