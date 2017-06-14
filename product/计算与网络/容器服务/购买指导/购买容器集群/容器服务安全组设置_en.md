## CCS Security Group Configuration
Security has always been our major concern. By listing security as the top priority of the product design, Tencent Cloud requires its products fully isolated and provides multiple security protections with its basic network. CCS is a typical example. It adopts VPC as the underlying network of CCS in Phase I. This document mainly introduces the best practices of the security group under the CCS to help you select the security group policy.

### What Is the Security Group?
Security group is a virtual firewall with a stateful packet filtering feature and critical network security isolation means to set network access control for one or more CVM(s). For more information on security groups, please see [Security Details](https://www.qcloud.com/document/product/213/5221).

### Principles on Security Group Selection with CCS

- 1. It is recommended that CVMs in the same cluster are bound to the same security group. The cluster's security group does not add other CVMs.
- 2. Security groups grant the minimum permission externally.
- 3. The following CCS rules need to be open to the Internet:
 - a. Container network and node network
 - b. Container network and node network of the cluster if different clusters in the same VPC cannot be connected
 - c. Port 22 in SSH login node
 - d. Port 30000-32767 for CCS access

### Suggestions
It is recommended that you configure the security groups for the cluster through the security group template provided by the CCS.
