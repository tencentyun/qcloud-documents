## Security Group and Network
- Security group is a virtual firewall that allows state-based packet filtering. You can restrict access by using a firewall (security group) to allow the trusted addresses to access instances. Different security group rules for instance groups of different security levels are created to ensure that the instances running important business cannot be accessed easily from the outside. For more information, please see [Security Group](/doc/product/213/5221).
- You need to regularly repair, update and protect the operating system and applications on the instance.
- EIPs allow you to remap your IPs to your CVM instances (or NAT gateway instances) quickly to block any failure of any CVM instance. For more information, please see [EIP Address](https://cloud.tencent.com/doc/product/213/5733).
- Log in to your Linux instances using [SSH key](https://cloud.tencent.com/doc/product/213/6092) whenever possible. For the instances that you [Log in with Password](https://cloud.tencent.com/doc/product/213/6093), the password needs to be changed from time to time.
- Choose to use [VPC](https://cloud.tencent.com/doc/product/213/5227) for the division of logical zones.

## Storage
- For data that is required to have extremely high reliability, use [Cloud Block Storage](https://cloud.tencent.com/doc/product/362) to ensure the persistent and reliable data storage.
- For databases that are frequently accessed and variable in size, use [Tencent Cloud Database](https://cloud.tencent.com/product/cdb-overview.html).
- You can use [COS](https://cloud.tencent.com/product/cos) to store important data, such as static web pages, massive images and videos.

## Backup and Recovery
- One of the recovery methods is to rollback a [Custom Image](https://cloud.tencent.com/doc/product/213/4942) you backed up via [CVM Console](https://console.cloud.tencent.com/cvm/index).
- Deploy key components of an application across multiple availability zones, and copy the data as appropriate.
- Regularly review the monitoring data and set corresponding alarm. For more information, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).

