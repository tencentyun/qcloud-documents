Cloud products on the Tencent Cloud can be accessed via [Internet access](/doc/product/213/5224) or accessed mutually via the Tencent Cloud private network. Private network services are Local Area Network (LAN) services, which are accessed mutually via private links. Tencent Cloud server rooms are interconnected by an underlying 10 Gigabit / Gigabit, providing high bandwidth, low latency within network communications services; and regions within the private network enjoy communications completely free of charge, helping you build a flexible network architecture.
> - Private network services contain user attributes; different users are isolated; that is, by default they cannot access another user's network through CVM services.
> - Private network services also have geographical attributes, and different geographical isolation; that is, by default, they cannot access the network through different accounts under cloud services.

## Private IP address

A private IP address is an IP that cannot access via the Internet; this is an implementation of private services by Tencent Cloud. You can use private IP addresses to implement communications between instances on the same network (basic networks or VPC). Each instance has a default network interface (ie, eth0) for assigning private IP addresses. Private IP addresses can be automatically assigned by Tencent and customized by users (only in [Private Network] environments). The combination of [Internet services](/doc/product/213/5224), and the Tencent cloud network architecture consists of the following two parts:

- Public network cards: Unanimously configured on the TGW interface layer, without CVM perception. When an instance is assigned a [Public IP address](/doc/product/213/5224), TGW automatically configures a public network interface for it.
- Private network card: Managed by Tencent Cloud, supports user configurations.

Therefore, when the user uses commands such as 'ifconfig' to view network interface information on the CVM, only the IP information of the private network can be viewed. For public network information, users need to log onto the [Tencent Cloud Console](https://console.qcloud.com/) CVM list/details page to view. Please note that if you change the private network IP within an operating system, it will lead to an interruption of network communications.

Private IPs can be used for CLB load balancing, inter-network visits between CVM instances and between CVM instances and other cloud services, such as CDN and CDB.

## How to obtain a private IP address
Each CVM instance is assigned a default private IP at startup. For different [Network Environments](/doc/product/213/5227), the private IP is also different:
 - Basic network: private IPs within the network are automatically assigned by Tencent Cloud, and cannot be changed.
 - Private network: the initial private IP assigned by Tencent Cloud is done automatically within the VPC network segment of an arbitrary address allocation; the user can be in the '10.[0 - 255].0.0/8', '172.[0 - 31].0.0/16' and '192.168.0.0/16' to define the private IP address for the CVM instance. The specific value range is determined by the private network of the instance. For more information, refer to [Private Network and Subnet](https://www.qcloud.com/doc/product/215/4927).

## Private network DNS 
Private network DNS services are responsible for domain name resolutions; if a DNS configuration is wrong, the domain name cannot be accessed. Therefore, Tencent Cloud provides reliable private DNS servers in different regions. The specific configuration is as follows:
<table><tbody>
<tr><th>Network environment</th><th>Region</th><th>Private DNS server</th></tr>
<tr><td rowspan="7">Basic network</td><td>Guangzhou</td><td>10.225.30.181<br>10.225.30.223</td></tr>
<tr><td>Shanghai</td><td>10.236.158.114<br>10.236.158.106</td></tr>
<tr><td>Beijing</td><td>10.53.216.182<br>10.53.216.198</td></tr>
<tr><td>Shanghai Finance</td><td>10.48.18.9<br>10.48.18.82</td></tr>
<tr><td>North America</td><td>10.116.19.188<br>10.116.19.185</td></tr>
<tr><td>Hong Kong</td><td>10.243.28.52<br>10.225.30.178</td></tr>
<tr><td>Singapore</td><td>100.78.90.19<br>100.78.90.8</td></tr>
<tr><td>Private network</td><td>All regions</td><td>183.60.83.19<br>183.60.82.98</td></tr>
</tbody>
</table>

When a network analysis discovers errors, users can manually set up the private network DNS. Set as follows:

- For Linux systems, you can modify the CVM DNS by editing the '/ etc / resolv.conf' file.
Run the command '/ etc / resolv.conf', according to the corresponding table in different regions to edit the geographical DNS IP.
![](https://mc.qcloudimg.com/static/img/fa8ecdf52b7f51361c369dbc96eea4ec/image.png)

- For Windows, you can modify the DNS server by opening the [Control Panel] - [Network and Sharing Center] - [Change Adapter Devices], then right-clicking on the network card [Properties] and double-clicking [Internet Protocol Version 4].
![](https://mc.qcloudimg.com/static/img/beb44bdaad8d90c9534891b725a1d3a6/image.png)
![](https://mc.qcloudimg.com/static/img/7f6590044c32188faa7f8e749aade9fe/image.png)

## Obtain private IP of instance
You can use the Tencent Cloud console and API to determine the private IP of the instance. You can also use the instance metadata to determine the private IP of an instance from within. For more information, see [Instance Metadata](/doc/product/213/4934).

### Use console to obtain private IP of instance

1) Open [CVM console](https://console.qcloud.com/cvm/).

2) CVM list shows the names of your instances; move the mouse over the CVM private IP, click on the copy button that appears, and copy the IP.

3) (Optional) Click on the CVM Instance ID to view detailed CVM info, including ** Parameters **, ** Monitoring **, ** Health Check **, ** Security Group **, ** Operation log **.

> The public IP is mapped to the private network IP through NAT. Therefore, if you view the properties of the network interface within the instance (for example, through ifconfig (Linux) or ipconfig (Windows)), the public IP is not displayed.

### Use API to obtain private IP of instance
Refer to [DescribeInstances interface](https://www.qcloud.com/doc/api/229/831).

### Use instance metadata to obtain private IP of instance

First, you need to login to the CVM instance. For details, refer to [Logging into Linux Instance](doc/product/213/5436) and [Logging into Windows Instance](/doc/product/213/5435).

Use the following command to obtain the private IP:

```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
The return value is as follows
![](//mccdn.qcloud.com/img56a1eeb9557a8.png)
