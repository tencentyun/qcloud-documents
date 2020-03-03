This document is designed to help users maximize the security and reliability during the use of CVM.

## Security and Network

- **Limited access:** Restrict access by using a firewall ([Security Group](/doc/product/213/5221)) to only allow the trusted addresses to access instances, and set the most stringent rules in the Security Group. For example, to limit access via port/IP address.
- **Security level:** Different security group rules can be created for instance groups of different security levels to ensure that instances running important business cannot be accessed easily from the outside.
- **Network logical isolation:** Choose to use [VPC](/doc/product/213/5227) to divide logical zones.
- **Account permission management:** When it is necessary to use multiple different accounts to control the same set of cloud resources, you can control their access to cloud resources using the [policy mechanism](/doc/product/378/4513).
- **Secure login:** Log in to user's Linux instances by use of [SSH Key] (/doc/product/213/6092) whenever possible. For the instances that you [log in with password](/doc/product/213/6093), the password needs to be changed from time to time.

## Storage

- **Hardware storage:** For the data that requires high reliability, use Tencent Cloud's cloud disks to ensure the persistent storage and reliability of data. Try not to choose [Local Disk](/doc/product/213/5798) for storage. For more information, please see [Cloud Block Storage Product Documentation](/doc/product/362).
- **Database:** For databases that are frequently accessed and variable in size, use [Tencent Cloud Database](https://cloud.tencent.com/product/cdb-overview).

## Backup and Recovery

- **Intra-region instance backup:** You can back up your instances and business data using **custom image** and **CBS snapshot**. For more information, please see [CBS Snapshot](/doc/product/362/5754) and [Create Custom Image](/doc/product/213/4942).
- **Cross-region instance backup:** You can copy and back up instances across regions using [Copy Image](/doc/product/213/4943).
- **Blocking instance failures:** You can use [EIP](/doc/product/213/5733) for domain name mapping to ensure that the server can quickly redirect the service IP to another CVM instance when it is unavailable, thereby blocking instance failures.

## Monitoring and Alarm
- **Monitoring and responding events:** Periodically check monitoring data and set proper alarms. For more information, please see [Cloud Monitor Product Documentation](/doc/product/248).
- **Handling emergent requests:** With [Auto Scaling](/doc/product/377), the stability of CVMs during peak hours can be guaranteed and unhealthy instances can be replaced automatically.

