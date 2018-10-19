Welcome to Tencent Cloud Load Balancer. Cloud Load Balancer sends the requests from client to multiple associated backend [CVMs](https://cloud.tencent.com/document/product/439/6328) in the same region with the specified method by setting a virtual IP (VIP).

Cloud Load Balancer virtualizes multiple CVMs as an available Cloud Pool. It can check the health of CVMs in the Could Pool, and automatically isolate abnormal CVMs, thus dealing with the single point of failure (SPOF) of a single CVM and improving the overall service capability of applications. If the service suffers a DDOS attack, Cloud Load Balancer can defend against a peak traffic above 300 Gb.

Cloud Load Balancer is a solution that serves multiple machines simultaneously, and it needs to be used in combination with CVM. **The APIs discussed in this document are used to execute Cloud Load Balancer instances. Before using these APIs, please make sure that you have a thorough understanding of [Product Overview](https://cloud.tencent.com/document/product/214/524) and [Tips on Usage](https://cloud.tencent.com/doc/product/214/%E9%80%89%E6%8B%A9%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%9C%B0%E5%9F%9F) of Cloud Load Balancer**.


## Glossary

| Term | Full Name | English | Description |
|---------|---------|---------|
| CLB | Cloud LoadBalancer | Cloud Load Balancer | Cloud Load Balancer sends the requests from client to the associated CVMs in the same region with specified method by setting a virtual IP (VIP). It can automatically isolate abnormal CVMs, thus dealing with the single point of failure (SPOF) of a single CVM and massive concurrent access requests to the service. |
| Listener | LoadBalancer Listener | Load Balancer Listener | Load Balancer Listener provides users with customized listener port, request forwarding policy, health check configuration, etc. |
| backend | backend server | Backend CVM | Load Balancer instance sends requests to backend CVMs, which will provide service in a real sense. |
| VIP | Virtual IP | Virtual IP of service | Load Balancer instance provides the virtual IP of service. |

## How to Use
Before using Cloud Load Balancer through APIs, please make sure that a port is open on one or more of your CVMs, e.g. TCP port 80. Next, you need to perform the following steps:
1. Purchase a load balancer instance.
You can use API [Purchase Load Balancer Instance](https://cloud.tencent.com/document/api/214/1254) to create a load balancer instance, and obtain the unique ID of this instance.
2. Create a load balancer listener.
After purchasing a load balancer instance, you need to use API [Create Load Balancer Listener](https://cloud.tencent.com/document/api/214/1255) to create a listener that listens for a protocol and port. For example, you can create a TCP-based listener that listens for TCP port 80 and backend port 80.
3. Bind the backend CVM to the load balancer instance.
Finally, you need to bind the CVM on which the service is deployed to the purchased load balancer instance through API [Bind Backend CVM to Load Balancer Instance](https://cloud.tencent.com/document/api/214/1265).

After performing the three steps described above, you can access the service deployed on your CVM by accessing the VIP and port of the load balancer instance.

In case of any conflict between the value or optional range of any parameter provided in "API Description" of this document and that provided on the Tencent Cloud official website, **the latter shall prevail**.

