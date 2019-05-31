## Overview
Tencent Cloud Anycast Internet Acceleration can help customers perform EIP Anycast in multiple regions, thereby achieving the following features:
### Same Server in Multiple Regions
All of users' requests and responses can come in and out from the nearest Tencent Cloud API, and only one service cluster, one database or one storage node needs to be deployed at the backend. After IP Anycast is performed, the backend service will be available in multiple regions through Tencent Cloud's private network-based Direct Connect. However, in traditional mode, only one cluster or one storage node is deployed in each region to serve nearby customers.
### Multi-regional Acceleration
Slow connection to the Internet can be avoided, and services are not affected by the congestion on the Internet, north-south issue, and ISP's failures.
### Avoiding Congestion
Based on the capabilities of Anycast, the congestion can be avoided during the Internet transmission.

![Congestion](https://mc.qcloudimg.com/static/img/5ad1eb5e3e4f0aac2174bfc45d06c2c0/image.png)

### Blocking Failures
Since the Internet ISP's backbone network fails from time to time, you can use the capabilities of Anycast to block the failures from Internet.

![Failures](https://mc.qcloudimg.com/static/img/34ccc568c4a6cb6c57718952cbb39b47/image.png)

## Relevant Extensions
**The following concepts can help you understand AIA:**
For more information on the concepts, please see [Glossary](https://cloud.tencent.com/document/product/644/12625).
**To provide Anycast service, public cloud vendors must have a powerful global interconnection and interworking node network and a capability of cross-region network scheduling. The basic capabilities of AIA are as follows:**
- Multi-path ISP aggregation: Tencent Cloud has TB-level BGP network egress with 35+ ISP lines.
- Multi-node interconnection and interworking: Tencent Cloud's global TB-level backbone network is used for hosting.
- Multi-dimensional network monitoring model, global network monitoring alarms, and real-time perception of Internet conditions.
- SDN controller that controls the entire network can change IP publishing sites in seconds and enable multidimensional and fine-grained control.
- Optimal path algorithm is generated through self-learning.

