You need to modify the mechanism for domain name resolution of mobile App in the process of connecting to HttpDNS. New process is shown as follows:

![Best Practice for HttpDNS](//mccdn.qcloud.com/static/img/21b1ec2b1656ead133d18ad136320dda/image.png)

Follow the two design policies below during modification:

### 1. Failover Policy
HttpDNS has been connected to BGP Anycast, and implemented multi-region disaster recovery across data centers. However, to ensure that domain name resolution at the client end is not affected even in the worst case, the following failover policy is recommended:
- First, send domain name query request to HttpDNS
- If the query result returned from HttpDNS is not an IP address (but a null value, non-IP or connection timeout, etc.), you can resolve domain name through LocalDNS. It is recommended to set the timeout to 5 seconds

### 2 Cache Policy
The network environment for mobile Internet users is more complex. In order to minimize the delay caused by domain name resolution, it is recommended to cache locally. Caching rules are as follows:
- Cache Expiration Time
It is recommended to set the cache expiration time to 120-600 seconds, and no less than 60 seconds.

- Cache Update
You should update cache in the following two scenarios:
**When user's network status changes:**
When user's network status of mobile Internet switches between 3G and Wi-Fi, the network of the access point may change. So if user's network status changes, you need to send request for domain name resolution to HttpDNS again to acquire the best IP address under user's current network.
**When cache expires:**
When the time during which the result of domain name resolution is cached expires, the client should resend a domain name resolution request to HttpDNS to acquire the IP corresponding to the latest domain name. To reduce user's waiting time for a new domain name resolution after cache expires, it is recommended to resolve domain name when TTL is 75%. If TTL for local cache is 600 seconds, the client should resolve domain name at the moment of 600*0.75=450 sec.

In addition to the above suggestions, decreasing the number of domain name resolutions can also effectively reduce network interactions and improve user's access experience. Try to minimize the number of domain names without affecting the business. It is recommended to distinguish among different resources by url.

### 3. Notes

Tips on modification of App:

1. Please try to distinguish among resources with the same domain name but with different features by url, to reduce the number of domain name resolutions (This is to improve user experience and make it easy for disaster recovery. Even if an additional domain name is hit in the cache, at least 100 ms of access delay occurs). Batch resolution of domain name will be available for new edition.
2. TTL value for cache should not be set too low (no less than 60 seconds) to prevent frequent HttpDNS requests.
3. The business that is connected to HttpDNS should be used with LocalDNS as a channel for disaster recovery. When HttpDNS is unable to provide services normally (mobile network is unstable or HttpDNS service fails), you can use LocalDNS for resolution.
4. 404 error may occur in Android App, but no error occurs in browser. It may be caused by permission issues or other problems. For more information, please see http://stackoverflow.com/questions/10835845/android-http-request-wierd-404-not-found-issue.
5. For bytetohex & hextobyte, you need to implement the API independently to convert between hexadecimal strings and bytes.
6. For HTTPS problems, client should check whether domain and extension domain in certificate contain the host of this request through client hook, and replace IP with original domain name. Then, certificate verification can be performed. Or just ignore the certificate verification, similar to the parameter "curl -k".
7. It is recommended to set the timeout of HttpDNS request to 2-5 seconds.
8. When network type changes, for example, from 4G to WiFi or between different WiFi, you should resend HttpDNS request to refresh local cache.

