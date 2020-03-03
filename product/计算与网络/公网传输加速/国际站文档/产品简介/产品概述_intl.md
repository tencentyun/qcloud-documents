## **What Is Tencent Cloud Anycast Internet Acceleration?**
Anycast Internet Acceleration (AIA) is a dynamic acceleration network with global coverage that can greatly improve the Internet access experience of your business. Unlike other application-layer acceleration services, AIA can optimize IP transfer quality, enable access from the nearest entry node and reduce jitter and packet loss of network transfer, thereby improving service quality of in-cloud applications, expanding service scope and simplifying backend deployment.

## **Why Choose AIA?**
### **Low Latency**
AIA uses the Anycast method to simultaneously publish the IP to multiple regions. The request packet will reach the optimal IP publishing region according to the transfer protocol. The packet will prioritize entering Tencent Cloud before reaching the server through Tencent Cloud's backbone Direct Connect line, helping avoid Internet congestion and reduce latency.

### **High Reliability**
Internet transfers can be unreliable; if a line interruption of the ISP leads to inability to access the Internet, users will have no choice but to wait for recovery to complete the transfers. With the aid of AIA, multiple paths and entries are made possible by Tencent Cloud's backbone networks, the ISP's backbone networks and Tencent Cloud's POPs, thus eliminating the potential for connection failures caused by single-region or single-line network outages and enhancing network stability.

### **Reduced Jitter**
The performance of the Internet link is unstable, leading to an unstable service experience, such as the network jitter caused by cross-ISP or cross-border connection issues. In contrast, AIA allows the request to access the nearest Tencent Cloud node and get transferred through Tencent Cloud's private Direct Connect line across regions, which perfectly resolves any issues with Internet jitter and ensures stable transfer performance.

### **Simplified Deployment**
Implementing services that are accessed by end users in many different regions can be cumbersome as servers have to be deployed in each region, DNS has to be properly configured to enable load balancing and IPs vary in different regions. AIA eliminates the need to configure IPs for each region, clearing up the trouble caused by geographic dispersion at the IP level. In addition, only one set of logics need to be maintained on the backend where the requests from different regions are accelerated to reach the backend servers through the Direct Connect line.

### **Global Load Balancing**
AIA uses the Anycast addressing method to simultaneously publish the IP to multiple regions. The request packet will reach the optimal IP publishing region (usually the nearest region) according to the transfer protocol, which achieves global load balancing. Additionally, in the case of a traffic-based attack, the cross-region publishing of IPs helps distribute the attacking traffic.
### **Ease of Use**
AIA is compatible with common IP operations, allowing you to purchase just one accelerating elastic public IP and lowering the threshold for use. It supports self-service Internet bandwidth limiting, making it easy to configure upper limits for bandwidth based on cost or server processing speed. In addition, it supports traffic monitoring for backtracking and analysis as well as binding and unbinding for easier backend resource changes.

## **Version History**

| Updated on | Release notes |
|---------|---------|
| November 23, 2017 | AIA EIP starts internal trial; multi-region anycasting is supported |
| January 20, 2016 | Cross-region traffic scheduling capability is added to the backend |

