## What is Tencent Cloud Anycast Internet Acceleration?
Anycast Internet Acceleration (AIA) is a global dynamic acceleration network that significantly increases the Internet access experience of your business. Different from other acceleration services in the application layer, AIA can optimize IP transmission quality, access multiple entries from nearby, and reduce jitter, packet loss, and other problems during network transmission. As a result, AIA improves the service quality of cloud applications, expands the service coverage, and simplify the backend deployment.

## Why Tencent Cloud AIA?
### Low Latency
AIA publishes an IP to multiple regions through Anycast at a time. The request packet will reach the optimal IP publishing region according to the transmission protocol. It enters Tencent Cloud first, and then reaches the CVM through the backbone network direct connect of Tencent Cloud, so as to avoid the congestion on the Internet and reduce the latency.

### High Reliability
Internet transmission is unreliable, and for the inaccessibility to the network caused by ISP's line interruption, users can only wait for its restoration. For Tencent Cloud backbone network, ISP's backbone network and Tencent Cloud POP point, AIA can achieve network access through multiple paths and multiple entries, block single-region and single-line failures, and improve the network stability.

### Reducing Jitter
The performance of Internet link is unstable, and network jitter can be caused by north-south or cross-border issue, for example, thereby affecting the service experience. After connecting the request to Tencent Cloud from nearby, AIA can implement cross-region transmission through the private network-based Direct Connect of Tencent Cloud, to solve the problem of Internet jitter and ensure the stability of transmission.

### Simplifying Deployment
For services with customers located in multiple regions that need to be connected to nearby, you must deploy servers and configure the DNS to implement load balance in these regions. Deployment can be quite complex because different regions have different IPs. After AIA is used, the region attributes are converged at the IP level. It is not required to configure the IP for each region, and only one set of logic needs to be maintained at the backend. The requests from different regions are directly accelerated to the backend servers with the Direct Connect.

### Global Load Balance
An IP is published to multiple regions by using Anycast at a time, and the request packet will reach the optimal IP publishing region (usually the nearest region) according to the transmission protocol, thereby achieving the global load balance. When a traffic attack occurs, since the IP has been published to multiple regions, equal allocation of traffic is also achieved.
### Easy of Use
When AIA is used, common IP operations can be compatible if you purchase an accelerated EIP. The requirements for using AIA is relatively low, and you can set a limit on the public network bandwidth by yourself and also configure an appropriate bandwidth limit depending on the cost or the server processing speed. AIA allows traffic monitoring for rewind and analysis, and supports binding and unbinding operations to help you make changes to the backend resources.

## Version History

| Update Time | Description |
|---------|---------|
| Nov. 23, 2017 | Accelerated EIP of Anycast is in internal trial, and multi-region Anycast is supported |
| Jan. 20, 2016 | Cross-region traffic scheduling is supported at the backend |


