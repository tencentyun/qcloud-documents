## Product Overview
Content Delivery Network (CDN) is a new network architecture added on the existing Internet and is made up of high-performance acceleration nodes distributed around the world. These high-performance service nodes will store your business content based on a certain cache policy. When your user makes a request for your business content, the request will be allocated to the service node that is closest to the user. The service node will give a direct response to the request quickly, greatly reducing the user's access latency and improving availability.

CDN can effectively solve the following netowrk problems of Internet business:
1. The long physical distance between the user and the business server makes the request need to be forwarded via network many times, leading to a high transmission latency and instability.
2. The ISP used by the user is different from the one where the business server resides in, so the request need to be forwarded between the ISPs after they are interconnected with each other.
3. The limited network bandwidth and processing capacity of business server result in a slower response and lower availability in case of massive user requests. 

**Featuring a simple connection, CDN allows you to enjoy the global CDN acceleration services without the need to change your business structure or perform complicated operations and configuration. **For more information about connection, refer to [Getting Started](https://cloud.tencent.com/doc/product/228/3149).

## How does it work?
For example, if your business origin server's domain name is www.test.com and the domain name has been connected to CDN and starts to use acceleration service, when your user makes an HTTP request, the request will be processed as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/1bead74703061b71eeaf6bf4db27fcdb/image.png)
**The procedure is as follows:**
1. A user wants to make a request to access a picture resource on www.test.com, e.g. 1.jpg. The user needs to send a domain name resolution request to Local DNS first.
2. The Local DNS resolves www.test.com and find that CNAME www.test.com.cdn.dnsv1.com has been configured. It forwards the resolution request to Tencent DNS (GSLB). GSLB is a scheduling system independently developed by Tencent Cloud and will allocate the best node IP to the request;
3. Local DNS receives the resolved IP returned by Tencent DNS;
4. The user receives the resolved IP;
5. The user sends a request to access 1.jpg to the received IP;
6. If 1.jpg is cached on the node corresponding to the IP, the data will be returned directly to the user (10), then the request ends. If 1.jpg does not exist on the node, the node will send a request for 1.jpg to the origin server (6,7,8). After obtaining the resource, the node will use the user-defined cache policy (refer to the section about cache duration setting in the User Guide) to store the resource (9) and return it to the user (10). The request ends now.


