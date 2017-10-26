Instance metadata refers to data of the CVM instance that you operate, and can be used for configuring or managing currently running instances.
>Note: While instance metadata can only be accessed internally from within the instance CVM, the data has not been protected through encryption. Anyone who accesses the instance can view its metadata. Therefore, you should take proper precautions to safeguard sensitive data (e.g. using permanent encryption key).

Tencent Cloud currently provides the following meta-data info:

| Data | Description | Version introduced|
|---------|---------|---------|
| instance-id | Unique ID of CVM | 1.0 |
| uuid | Unique ID of CVM | 1.0 |
| local-ipv4 | Private IP | 1.0 |
| public-ipv4 | Public IP | 1.0 |
| mac | eth0 device mac address | 1.0 |
| placement/region | Region info | 1.1 |
| placement/zone | Availability zone info | 1.1 |
| network/network/macs/**mac**/mac | Network API device address of the machine | 1.2 |
| network/network/macs/**mac**/primary-local-ipv4 | Network API primary Private IP address of the machine | 1.2 |
| network/network/macs/**mac**/public-ipv4s | Network API Public IP address of the machine | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/gateway | Network API Gateway address of the machine | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/local-ipv4 |Network API Private IP address of the machine | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4 | Network API Public IP address of the machine | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4-mode | Network API Public network mode of the machine | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/subnet-mask | Network API subnet mask of the machine | 1.2 |

> Fields **mac** and **local-ipv4** in bold in the above table refer to device address for network API specified by the machine and Private IP address, respectively.
