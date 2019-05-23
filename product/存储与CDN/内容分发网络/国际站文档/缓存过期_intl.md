## Overview

Cache expiration configuration refers to a set of expiration policies the CDN acceleration nodes should follow when caching your business contents.

User resources cached on CDN nodes all have a "Expiration Time". If a resource cached on a node is not expired, when a user request for the resource reaches the node, the node will directly return the cached resource to the user to speed up the resource acquisition; If a resource is beyond the set validity period and thus becomes expired, the node will forward the user request for the resource to the origin server, reacquire and cache the resource, then return it to the user. 

A reasonable cache validity period can effectively improve the resource hit rate and reduce back-to-origin rate, achieving a saving in bandwidth. Tencent Cloud CDN supports cache validity period settings at various dimensions, custom priority adjustment and cache inheritance policies (advanced cache configuration).



## Configuration Instructions

Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can find **Cache Expiration Configuration** in "Cache Configuration":

![](https://mc.qcloudimg.com/static/img/d325a0b2f444a2887439bfb036b2921a/2.png)

### Default Configuration

Default configuration is as follows when a domain is connected:

- Own origin domain connection: By default, the cache validity period for all files is 30 days, except general dynamic files (such as .php, .jsp, .asp, .aspx), for which the cache validity period is 0 by default, which means any request for such files will be directly forwarded to the origin server;
- COS origin domain connection: By default, the cache validity period for all files is 30 days;
- Advanced cache expiration configuration is disabled by default.

You may modify the default settings mentioned above.

### Custom Configuration

You can make cache validity period settings in addition to the default settings base on your business needs. CDN supports **three settings**:

#### Setting cache validity period by file types

You can set cache validity period by file types by entering the filename extensions, as shown below:

> .jpg .png 300 seconds

In this case, all picture resources matching .jpg and .png under the domain will be cached for 5 minutes on the node.

#### Setting cache validity period by folders

You can set cache validity period by folders by entering the folder path, as shown below:

> /test;/test2 1000 seconds

In this case, if the domain is "www.test.com", all resources under "www.test.com\test\" and "www.test.com\test2\" will be cached for 1000 seconds on the node.

#### Setting cache validity period based on full path of file

You can set cache validity period for a certain file, as shown below:

> /test/1.jpg 2000 seconds

In this case, if the domain is "www.test.com", the resource "www.test.com\test\1.jpg" will be cached for 2000 seconds.

You can also set cache validity period for a certain type of files, as shown below:

> /test/*.jpg 3000 seconds

In this case, if the domain is "www.test.com", all resources with a jpg format under "www.test.com\test\" will be cached for 3000 seconds.

**Note:**

- You can set multiple cache validity periods at a time, with the entries separated by ";". **The entries are case-sensitive**; 
- File types must be specified as extensions starting with ".", such as ".jpg"; Folder types must begin with "/", such as "/12345/test", instead of ending with "/";
- A maximum of **10** custom entries can be added, each of which can only contain 150 characters;
- Cache validity period can be set to any number of seconds in the form of an integer, "0" means resource will not be cached;
- When you are setting caching policies based on full path of file, "*" can only be used to match a certain type of files. Other regular expression matching methods are not supported currently;
- The home page type ending with "/" is not supported in the setting of caching policies based on full path of file.



### Priority

#### Matching Sequence

When multiple caching policies are set, the priorities of the entries are determined on a bottom-to-top basis, with the entry at the bottom of list having the highest priority and the one at the top having the lowest priority. For example, if the following caching policies are set for a domain:

> All files 30 days
> .php .jsp .aspx 0 second
> .jpg .png .gif 300 seconds
> /test/\*.jpg 400 seconds
> /test/abc.jpg 200 seconds

If the domain is "www.test.com", and the resource is "www.test.com/test/abc.jpg", the matching rule will be as follows:

1. Match with the first entry. It is hit, so the cache validity period is 30 days;
2. Match with the second entry. It is not hit;
3. Match with the third entry. It is hit, so the cache validity period is 300 seconds;
4. Match with the fourth entry. It is hit, so the cache validity period is 400 seconds;
5. Match with the fourth entry. It is hit, so the cache validity period is 200 seconds;

The final cache validity period is subject to the last matching result, 200 seconds.

#### Changing Priority

You can customize the order of existing cache validity period entries according to your business needs. Click **Adjust priority** above the cache validity period entries:

![](https://mc.qcloudimg.com/static/img/281be811139a8da61addd6c39875e54b/3.png)

Use the up and down arrows on the right to change the order of cache validity period entries, then click **Save**:

![](https://mc.qcloudimg.com/static/img/f8efc866186f6c27436465b5208f6afb/4.png)



### Cache Inheritance

When a user makes a request for a certain business resource, the origin server's Response HTTP Header will include the cache-control field. The default policy is as follows:

- If the cache-control field is max-age, the cache validity period for this resource is subject to the one set for the resource, instead of inheriting the value specified by max-age;
- If the cache-control field is no-cache or no-store, the CDN node will not cache the resource.



## Advanced Cache Configuration

The **Advanced cache expiration Configuration** switch above the cache expiration configuration list can provide the following features when enabled.

When a user requests for a certain resource from the origin server and the Response HTTP Header includes the cache-control field with a value of max-age=xxxx, the cache validity period for the resource on the node will be subject to the smaller one between the set validity period and max-age:

- For example, If the max-age set for the /index.html of the origin server is 200 seconds  and the cache validity period set for CDN is 600 seconds, the actual cache validity period for the file is 200 seconds;
- If the max-age set for the /index.html of the origin server is 800 seconds and the cache validity period set for CDN is 600 seconds, the actual cache validity period for the file is 600 seconds;

<font color="red">When advanced cache configuration is enabled, if  Cache-Control field does not exist in the Response Header of your origin server, CDN will add the  "Cache-Control:max-age=600" header by default.</font>

## Caching based on status codes

In addition to the cache policies mentioned above, CDN nodes will also use the following default cache policies based on status codes when requesting for resources from the origin server:

+ 2XX: Use normal cache policies;
+ 3XX: Resources are not cached by default;
+ 4XX: Resources are cached for 10 seconds in case of status code 404. In other cases, they're not cached by default;
+ 5XX: Resources are not cached by default.
