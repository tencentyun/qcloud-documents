This document is designed to help users maximize the security and reliability during the use of CVM.

## Security and network

- Restrict access by using a firewall (Security Group) to only allow the trusted addresses to access instances, and set the most stringent rules in the Security Group. For example, by restricting the TCP inbound traffic of port 80 to IP `111.111.111.111`, you can make your CVM perform TCP access only from your local host ` 111.111.111.111`. For more information, see [Security Group] (/doc/product/213/5221).
- Create different Security Group rules for instance groups of different security levels to ensure that the instances running important business cannot be accessed easily from the outside.
- Regularly update and protect applications on the instances.
- Choose to use [Virtual Private Cloud] (/doc/product/213/5227) to divide logical areas.
- When it is necessary to use multiple different accounts to control the same set of cloud resources, users can use the [policy mechanisms](https://www.qcloud.com/doc/product/378/4513) to control their access to cloud resources.
- Log in to user's Linux instances by use of [SSH Key] (/doc/product/213/6092) whenever possible. For the instances that you [log in with password](/doc/product/213/6093), the password needs to be changed from time to time.

## Storage

- For the data that is required to have very high reliability, please use Tencent Cloud's Cloud Block Storage to ensure the persistent storage and reliability of data. Try not to choose [local disk] (/doc/product/213/5798) for storage. For more information, see [Cloud Block Storage product documentation](https://www.qcloud.com/doc/product/362).
- For the frequently-assessed databases with unstable capacity, you can use [Tencent Cloud's Cloud Database](https://www.qcloud.com/product/cdb-overview.html).

## Backup and recovery

- Back up instances by use of "CBS Snapshot"(/doc/ product/362/5754) function on a regular basis.
- Deploy key components of application across multiple availability zones and copy the data as appropriate.
- Use [Elastic IP] (/doc/product/213/5733) for domain name mapping and ensure that the server can quickly redirect the service IP to another CVM instance when it is unavailable.
- Regularly review the monitoring data and set alarm as appropriate . For more information, see [Cloud Monitoring Product Documentation](https://www.qcloud.com/doc/product/248).
- Process emergent requests with Auto Scaling. For more information, see [Auto Scaling product documentation](https://www.qcloud.com/doc/product/377).
