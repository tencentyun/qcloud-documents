When an application deployed by a user on a CVM instance needs to provide public services, the data must be transferred over the Internet. Tencent Cloud Internet access is provided by Tencent Cloud data centers' high-speed Internet. Domestic multi-line BGP network covers more than 20 ISPs; BGP public network external ports can switch cross-domains instantly, guaranteeing that users can enjoy a high-speed and secure network quality on all kinds of networks.

If your CVM instance is to provide service over the Internet, it must have an IP address (also known as a public IP) on the Internet in order to communicate with other services on the Internet. You can also configure a CVM instance with a public IP on the Internet. For more information about logging into a CVM instance, please see [Log in to CVM Instance on Linux](/doc/product/213/5436) and [Log in to CVM Instance on Windows](/doc/product/213/5435).

## Public IP
A public IP is an IP address that can be accessed from the Internet and be used for communication between instances and the Internet. The public IP is mapped to the instance's [Private IP](/doc/product/213/5225) through Network Address Translation (NAT). All the public network APIs of Tencent Cloud are processed by Tencent Gateway (TGW). TGW provides more efficient and secure network access, it features high reliability, high extensibility, high performance and strong anti-attack abilities. Therefore, Tencent Cloud CVM instance public network ENIs are configured on the uniform TGW API layer with the CVM unaffected.

When the user uses commands such as 'ifconfig' to view network API information on the CVM, this feature caused users to only see information about the [Private Network](/doc/product/213/5225). Users have to log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and view Public network information on CVM list/details page.

Instances providing services through public network IPs need to pay the corresponding fees; for specifics, please see [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509#2.1.-.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9).

## How to Obtain a Public IP
Tencent Cloud network (public network) billing has three methods: pay-by-bandwidth, pay-by-traffic and bandwidth packages (for more information on network billing methods, please see [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509#2.1.-.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9)). At the [Purchase and Start CVM Instance](/doc/product/213/4855), users in the Network Settings can:

- Select pay-by-bandwidth, and set the bandwidth to a value greater than 0 Mbps.
- Select pay-by-traffic, and set the bandwidth upper limit to a value greater than 0 Mbps (including unlimited).
- Select bandwidth package, and set the bandwidth to a value greater than 0 Mbps.

Tencent Cloud system will automatically assign a public IP for the instance from the Tencent public IP pool. This address cannot be changed, and is not associated with your Tencent Cloud account.

## Release of Public IP
A user cannot actively associate or disassociate a public IP from an instance. In some cases, Tencent Cloud system will automatically release the public IP, or assign a new address to the instance. The released public IP will be returned to the public IP pool, and is not reusable.

- When an instance has been terminated (active termination of pay-per-use instances; or termination of expired monthly or yearly packages), Tencent Cloud will release its public IP.
- If a user associates an [Elastic Public IP(EIP)](/doc/product/213/5733) with an instance, Tencent Cloud will release the original public IP of the instance. When disassociating an instance with the EIP, a new public IP is automatically assigned to the instance.

Since the public IP is closely related to the instance, it might be released in the above situation; therefore, if you need a fixed permanent public IP, you can use the EIP instead. For example, if you need to remap a custom domain name to the public IP of a new instance, it might take hours to dozens of hours for the mapping to propagate over the Internet; during which time, the new instance cannot receive requests and the requests are all parsed to the original instance. EIPs can solve this issue, which is to maintain the domain name mapping relationship and quickly bind it to a new instance. For more information, please see [Elastic Public IP (EIP)](/doc/product/213/5733).

## Obtain Public IP of the Instance
You can use the Tencent Cloud console and API to determine the public IP of the instance. You can also use the instance metadata to determine the public IP of an instance from within. For more information, please see [Instance Metadata](/doc/product/213/4934).

### Use console to obtain public IP of the instance

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).

2) CVM list shows your instances, move the mouse over the CVM public IP, and click on the appeared copy button to copy the IP.

3)(Optional) Click on the CVM instance ID to enter the CVM info page and view detailed information, including **Parameters**, **Monitoring**, **Health Check**, **Security Group**, **Operation Log** and so on.

> The public IP is mapped to the private IP through NAT. Therefore, if you check the attributes of the network interface within the instance (for example, through ifconfig (Linux) or ipconfig (Windows)), the public IP is not displayed. To determine the public IP of an instance from within, you can use the instance's metadata.

### Use API to obtain public IP of the instance
Please see [DescribeInstances API](https://cloud.tencent.com/doc/api/229/831).

### Use instance's metadata to obtain public IP of the instance

First, you need to log into the CVM instance. For details, please see [Log in to CVM Instance on Linux](/doc/product/213/5436) and [Log in to CVM Instance on Windows](/doc/product/213/5435).

Use the following command to obtain the public IP:

```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
The returned value has a structure similar to the following:
![](//mccdn.qcloud.com/img56a1f015c48e5.png)

