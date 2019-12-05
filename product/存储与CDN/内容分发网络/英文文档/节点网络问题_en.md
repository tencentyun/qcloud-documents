### 1. How long is the default timeout for Tencent Cloud CDN nodes?
10 seconds.

### 2. What will happen to the files on the CDN node if I close accessing domain from CDN management?
If you close the CDN service of a domain which has already accessed CDN, the CDN node will retain the access configurations of the domain, no further CDN traffic will be generated, and requests towards this domain will all go back to the origin server. Before this operation, make sure that:
- You have configured the CNAME of this domain based on A record, otherwise the domain cannot be accessed.
- Your origin server has enough bandwidth processing capabilities, or problems may occur when you access your domain.

### 3. What to do when I can't open my website after accessing CDN?
First, check if the CDN status of accessing domain is "Closed". The website will not function if status is "Closed". Proceed the next step if the status is not "Closed":
+ Check whether the CNAME resolution of the domain has taken effect by using ping or nslookup. If CNAME is not bound, please see [CNAME Configuration](https://cloud.tencent.com/doc/product/228/3121) for how to bind CNAME at your DNS service provider.
+ After CNAME takes effect, check if you can access the origin server as usual.

If the problem is not solved after completion of the above procedure, contact us by [submitting a ticket](https://console.cloud.tencent.com/workorder/category).

### 4. How do I tell which CDN node are the users accessing?
You can acquire basic troubleshooting information such as the IP, latency and lost packet of the CDN node accessed by users by using the commands ping and nslookup.

### 5. Why do I have a low hit rate?
This is generally caused by the following reasons:
+ Cache configuration problem, such as short cache validity period;
+ Http Header prevents caching. Check the origin server's Cache-Control or Expires configurations;
+ Few cacheable content for the origin server type;
+ Website has less visits and low validity period. Low hit rate for files leads to frequent back-to-origin requests.

### 6. When users think it is too slow to access CDN?
We consider download speed for large files and latency for small files. First, acquire the URL that is slow to access for users and determine if the access is slow by using speed test websites such as 17ce http://www.17ce.com (recommended):
+  If the access is slow according to test and the origin server is FTP hosted origin, contact us by [submitting a ticket](https://console.cloud.tencent.com/workorder/category).
+  If the access is slow according to test and the origin server is a self-owned origin, you should assist the user to check if the machine load and bandwidth of the origin server are restricted.

### 7. How do I tell whether a user access has hit the CDN Cache?
Check the X-Cache-Lookup information in the header of the access response packet: ![](https://mc.qcloudimg.com/static/img/64ac912c895b36f0241a927df6da3543/image.png)
+ X-Cache-Lookup:Hit From MemCache: Memory of the CDN node is hit.
+ X-Cache-Lookup:Hit From Disktank: Disk of the CDN node is hit.
+ X-Cache-Lookup:Hit From Upstream: The CDN is not hit.

### 8. Why are the sizes of files returned by the node with the same file name different?
As all file types are cached by default, there may be different versions for a file on the CDN node. To solve this problem:
+ Manually refresh files and update cache immediately;
+ Use a version number, for example ```http://www.xxx.com/xxx.js?version=1```.
+ Change the file name to avoid using files with the same name.

If the problem is not solved after completion of the above procedure, contact us by [submitting a ticket](https://console.cloud.tencent.com/workorder/category).
