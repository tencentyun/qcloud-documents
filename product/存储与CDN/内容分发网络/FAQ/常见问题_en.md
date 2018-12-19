## Common Questions

+ Does Tencent Cloud CDN support any oversea nodes?
  + Currently, Tencent Cloud CDN is able to provide oversea acceleration feature. Tencent Cloud CDN leverages the nodes that have been deployed by Tencent over the past decade. We currently have 50+ acceleration nodes across 30+ overseas countries, allowing oversea acceleration.

+ Does CDN acceleration support ports other than 80?
  + Currently, CDN acceleration supports three ports: 80, 443, 8080.

+ Does CDN support the resolution of wildcard DNS?
  + Currently, CDN supports the connection of wildcard domains.

+ Will the cached content at CDN acceleration nodes be updated in real time?
  + The content will not be updated in real time. CDN nodes will update cache according to the cache expiration time that you have configured in the console. You can update the cache of a certain file in real time by refreshing or prefetching. Please see [Refresh and Prefetch](https://cloud.tencent.com/document/product/228/6299).

+ What is a CDN intermediate node?
  + CDN intermediate node refers to an intermediate node server, it's a middle-tier server located between the business server and CDN node. The intermediate node will converge back-to-origin requests from nodes, reducing pressure caused by such requests on your origin server.

+ Does CDN support HTTPS?
  + Currently, Tencent Cloud CDN fully supports HTTPS.

+ Are there any requirements for domains to be connected to CDN?
  + These domains to be connected to CDN for acceleration are required to be filed with MIIT for the record, and the business content of the origin server must be legal.

+ After being connected to CDN, does the origin server need to be modified to enjoy acceleration service?
  + There is almost no need. However, it is recommended that you separate dynamic files and static files and place them under different domains to achieve better acceleration outcome. Only static files need acceleration.

+ How long does it take to configure CDN?
  + Usually, it will take less than 30 minutes to configure CDN. If it is still not ready after you have completed the setup and waited for 30 minutes, please submit a ticket to us in time for assistance.

+ For CDN self-owned origin, can I configure that a certain file is not cached? Does it mean "do not cache" if I set the cache validity period to 0?
  + You may configure the corresponding cache validity period for directories and file types. If it is configured as 0, the CDN node will not cache the resource, in which case the CDN node will need to pull related resources from the origin server every time the users send access request to the node. For relevant cache configurations, please refer to [Cache Expiration Configuration](https://cloud.tencent.com/document/product/228/6290).

+ What will happen to the files on the CDN node if I close the connected domain from CDN management?
  + If you close the CDN service of a domain which has already been connected to CDN, the CDN node will retain the connection configurations of the domain, no further CDN traffic will be generated, and requests towards this domain will all go back to the origin server. Before this operation, please make sure that you have configured the CNAME of this domain to point to the A record, otherwise the domain will be unavailable for access. You should also make sure that your origin server has enough bandwidth processing capabilities, or problems will occur when accessing your domain.

+ Is the cache-control configuration of the origin server supported?
  + The cache-control configuration of the origin server is supported by Tencent Cloud CDN by default.

+ Why can I only close the CDN but not delete it?
  + Please check if your user is collaborator.

+ How can I increase the capacity of the hosted origin?
  + Some customers may be unable to upload their relevant data in time due to insufficient capacity when using hosted origin, which will prevent their business from going live as planned. In order to prevent such situation, we have implemented the following automatic rules regarding bandwidth usage and capacity. The capacity of the hosted origin will be automatically increased when the corresponding bandwidth usage is reached. When the monitored capacity for a user who has increased his or her capacity to the corresponding level exceeds 80%, the system will calculate the average bandwidth in the past 30 days. When the average bandwidth meets the upgrade requirement, the corresponding policy will be commenced to increase the current capacity by 50%. The limit of the capacity increment will not go above the corresponding capacity volume listed in the table below. If the user's domain has been in the network for less than 30 days, the current average bandwidth will be calculated; When a user has already increased capacity beyond the corresponding volume, the capacity will be kept but not further increased. If you wish to apply for additional capacity for special needs, please submit a ticket and tell us the reason for the application.

+ How do I bind my CNAME after I have connected to CDN?
  + Please refer to the document in this link [CNAME Configuration](https://cloud.tencent.com/document/product/228/3121).

+ Can I configure multiple origin server IPs?
  + Yes, you can. And if you do so, CDN will randomly access one of them upon a back-to-origin request. CDN will skip any unavailable origin server IPs.

+ Is directory refresh supported by CDN?
  + Currently CDN supports directory refresh to refresh URLs. You can perform URL refresh either in Tencent Cloud CDN Console or by calling API. [Click Here](https://cloud.tencent.com/document/product/228/3946).

+ Does Tencent Cloud CDN support cross-region access?
  + Tencent Cloud CDN does not restrict regions when processing cross-region accesses. If a user website requires cross-region access, the user will need to configure Access-Control-Allow-Origin field in his or her own website. You can also choose to configure a cross-region header in CDN for the domain to achieve cross-region access. Please refer to [HTTP Header Configuration](https://cloud.tencent.com/document/product/228/6296) for details.

## Troubleshooting

+ What to do when I can't open my website after connecting to CDN?
  + First, check if the CDN status of the connected domain is "Closed". The website will not function if status is "Closed". Go to the next steps if the status is not "Closed";
  + Check whether the CNAME resolution of the domain has taken effect by using ping or nslookup;
  + Check if you can access the origin server as usual.

+ Why do I have a low hit rate?
  + Cache configuration problem, such as short cache validity period;
  + Http Header prevents caching. Please check origin server's cache-control or expires configurations;
  + Few cacheable content for the origin server type;
  + Website has less visits and low validity period. Low hit rate for files leads to frequent back-to-origin requests.

+ How do I tell which CDN node are the users accessing?
  + You can acquire basic troubleshooting information such as the IP, latency and lost packet of the CDN node accessed by users by using the commands ping and nslookup.

+ Why are the sizes of files with the same name returned by the node different?
  + All file types are cached by default, thus there can be different versions for a file on the CDN node.
  + Solution:
    1. Manually refresh files and update cache immediately;
    2. Use a version number, for example: ```http://www.xxx.com/xxx.js?version=1```
    3. Change file name to avoid using files with the same name.

+ Users are experiencing a slow connection when accessing CDN?
  + We consider download speed for large files and latency for small files:
    1. Acquire the URL that is slow to access for users and determine if the access is slow by using speed test websites. (Recommendation: 17ce http://www.17ce.com, Alibench https://alibench.com.cutestat.com/)
    2. If connection is slow according to test, and origin server is FTP hosted origin or SVN origin, you should report the issue to second-line to solve the problem
    3. If connection is slow according to test, and origin server is self-owned origin, you should assist the user to check if the machine load and bandwidth of the origin server are restricted

+ How do I tell whether a user access has hit the CDN cache?
  + Check the X-Cache-Lookup information in the header of the returned packet for the access![](https://mccdn.qcloud.com/static/img/b28aa4df70343f6bd74290a1f0b85ab7/image.png)
    + X-Cache-Lookup:Hit From MemCache: Memory of the CDN node is hit
    + X-Cache-Lookup:Hit From Disktank: Disk of the CDN node is hit
    + X-Cache-Lookup:Hit From Upstream: The CDN is not hit



