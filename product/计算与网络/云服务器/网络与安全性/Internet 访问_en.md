When an application deployed by a user on a CVM instance needs to provide public services, the data must be transferred over the Internet. Tencent Cloud Internet access is provided by Tencent Cloud data centers via high-speed Internet. Domestic multi-line BGP networks cover more than 20 ISPs; BGP public network external ports switches cross-domains instantly, guaranteeing that users can enjoy high-speed, secure network quality, no matter what kind of network they're on.

If your CVM instance is to provide service over the Internet, it must have an IP address (also known as a public IP address) on the Internet in order to communicate with other services on the Internet. You can also configure a CVM instance with a public IP address on the Internet. For more information about logging into a CVM instance, refer to [Logging into a Linux Instance](/doc/product/213/5436) and [Logging into a Windows Instance](/doc/product/213/5435).

## Public IP address
A public IP is an IP address that can be accessed from the Internet and can be used to communicate between instances and the Internet using the public IP. The public IP is mapped to the instance's [private IP](/doc/product/213/5225) through [Network Address Translation (NAT)](/doc/product/213/5225). All the public network interfaces of Tencent Cloud are processed by Tencent Gateway (TGW). TGW features high reliability, high extensibility, high performance and strong anti-attack abilities; and provides more efficient and secure network access. Therefore, Tencent Cloud CVM instance public network cards are unanimously configured on the TGW interface layer, without CVM perception.

This feature allows users to view information about the network interface using commands such as 'ifconfig' on the CVM; but you can only see information that is on the [Private Network](/doc/product/213/5225). Public network information needs to be logged in by the user [Tencent Cloud Console](https://console.qcloud.com/) CVM list/details page to view.

Instances providing services through public network IPs need to pay the corresponding costs; for specifics, refer to [Purchasing Network Bandwidth](https://www.qcloud.com/doc/product/213/509#2.1.-.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9).

## How to obtain a public IP address
Tencent Cloud network (public network) billing has three modes: pay-by-bandwidth, pay-by-traffic and bandwidth packages (for more information on network billing modes, you can refer to [Purchasing Network Bandwidth](https://www.qcloud.com/doc/product/213/509#2.1.-.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9). When users are in the [Purchase and Start CVM Instance](/doc/product/213/4855), in the Network Settings:

- Select pay-by-bandwidth, and set the bandwidth to a value greater than 0 Mbps;
- Select pay-by-traffic, and set the bandwidth upper limit to a value greater than 0 Mbps (including unlimited);
- Select bandwidth package, and set the bandwidth to a value greater than 0 Mbps;

The Tencent Cloud system will automatically assign a public IP address for the instance from the Tencent public IP pool. This address cannot be changed, and is not associated with your Tencent Cloud account.

## Release of public IP address
A user cannot actively associate or unassociate a public IP address from an instance. In some cases, the Tencent Cloud system will automatically release the public network IP address, or assign a new address to the instance. The released public IP address will be returned to the public IP pool, and you will not be able to use it again.

- When an instance has been terminated (actively terminating pay-per-use instances; or teminating the instance after it has expired in monthly or yearly packages), Tencent Cloud will release its public IP address.
- If a user associates an [elastic public IP](/doc/product/213/5733) with an instance, Tencent Cloud will release the public IP address of the instance. When an instance has removed associated with an elastic IP address, the instance is automatically reassigned to a new public IP address.

Because the public IP address is closely related to the instance, it might be released in the above situation; therefore, if you need a fixed permanent public IP, you can use the elastic public IP address instead. For example, if you need to remap a custom domain name to the public IP of a new instance, it might take hours to dozens of hours for the mapping to propagate over the Internet; during which time, the new instance cannot receive requests and the request is all parsed to the original instance. Elastic IPs can solve this issue, maintaining the domain name mapping relationship, and quickly binding to a new instance. For more information, see [Elastic Public IP Addresses](/doc/product/213/5733).

## Obtain public IP of instance
You can use the Tencent Cloud console and API to determine the public IP of the instance. You can also use the instance metadata to determine the public IP of an instance from within. For more information, see [Instance Metadata](/doc/product/213/4934).

### Use console to obtain public IP of instance

1) Open [CVM console](https://console.qcloud.com/cvm/).

2) CVM list shows the names of your instances; move the mouse over the CVM public IP, click on the copy button that appears, and copy the IP.

3) (optional) Click on the CVM Instance ID to view detailed CVM info, including ** Parameters **, ** Monitoring **, ** Health Check **, ** Security Group **, ** Operation log ** and so on.

> The public IP is mapped to the private network IP through NAT. Therefore, if you view the properties of the network interface within the instance (for example, through ifconfig (Linux) or ipconfig (Windows)), the public IP is not displayed. To determine the public IP of an instance from within an instance, you can use the instance's metadata.

### Use API to obtain public IP of instance
Refer to [DescribeInstances interface](https://www.qcloud.com/doc/api/229/831).

### Use instance metadata to obtain public IP of instance

First, you need to login to the CVM instance. For details, refer to [Logging into Linux Instance](/doc/product/213/5436) and [Logging into Windows Instance](/doc/product/213/5435).

Use the following command to obtain the public IP:

```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
The return value has a structure similar to the following:
![](//mccdn.qcloud.com/img56a1f015c48e5.png)
