The backend CVM is a [CVM instance](https://cloud.tencent.com/doc/product/213) that processes the corresponding forwarding request after a cloud load balancer instance is created and bounded to it.  [Cloud Load Balancer Listener](/doc/product/214/6151) sends requests to the backend CVM via different [Round-robin Methods](/doc/product/214/6153) to ensure smooth and reliable performance of the application.  You can select to bind CVM instance in a single or multiple availability zones within the region where the cloud load balancer instance resides to increase the robustness of the application and block single point of failure. 

## Best Practices for Backend Instances 

When adding a backend server, we recommend that you: 

- Install a Web server (such as Apache or IIS) on all CVM instances that you want to add to cloud load balancer and keep running of the application consistent. 
- It is recommended that you enable the [Session Persistence](/doc/product/214/6154) feature, which will make cloud load balancer to maintain a longer TCP connection and make multiple requests to reuse it to reduce the load on the Web server and increase cloud load balancer throughput. 
- Ensure that the security group for the backend instance has inbound rules for the cloud load balancer listener port and the health check port. For more information, refer to [Backend Server Access Control](/doc/product/214/6157). 


