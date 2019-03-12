The CVM instance described below also refers to dedicated CVM.

The cloud products on the Tencent Cloud can access each other via [Internet Access](/doc/product/213/5224) or via the private network of Tencent Cloud. Private network services are LAN services. Cloud services can access each other via internal linkages. Interconnected with megabyte/gigabyte underlying networks, Tencent Cloud's data centers can enable communication via private network featured by large bandwidth and low latency, which is free of charge in the same region, giving you the flexibility to build a network architecture.

> - Private network services are user-sensitive. Different users are isolated from each other, which means that the cloud services of the other user cannot be accessed via the private network by default.
> - Private network services are also region-sensitive. Different regions are isolated from each other, which means that the cloud services under the same account in a different region cannot be accessed via the private network by default.

## Private IP

Private IPs are IPs that cannot be accessed through Internet. Tencent Cloud's private network services are realized based on them. The communication between instances within the same network (basic network or VPC) can be achieved using a private IP. Each instance has a default network interface (eth0) for the assignment of private IPs. Private IPs can be automatically assigned by Tencent Cloud, or defined by users (only under the [VPC]()). Combined with [Internet Access](/doc/product/213/5224), the network architecture of Tencent Cloud is composed of the following two parts:

- Public network ENI: it is configured on the uniform API layer TGW, with the CVM unaffected. When a [public IP](/doc/product/213/5224) is assigned to an instance, TGW will automatically configure a public network API for it.
- Private network ENI: it is managed by Tencent Cloud, and supports user-defined configuration.

Therefore, when you use such commands as `ifconfig` in the CVM to view the network interface information, only the information of private IP will display. You can log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/), and view the public network information in the CVM List/Details page. Please note that, if you change the private IP by yourself within the operating system, the communication via the private network will be interrupted.

A private IP can be used for CLB load balancing, or used for CVMs to access each other through a private network, and also used for CVM instances and other cloud services to access each other via a private network, such as CDN and CDB.

## How to obtain a private IP
Each CVM instance will be given a default private IP when activated. The private IP varies with [Network Environment](/doc/product/213/5227):
- Basic network: the private IP is assigned by Tencent Cloud automatically and cannot be changed.
- VPC: the initial private IP is assigned by Tencent Cloud randomly in VPC IP address range, and users can define the private IP for the CVM instance within the `10.[0 - 255].0.0/8`, `172.[0 - 31].0.0/16` and `192.168.0.0/16` IP address ranges. The specific value range is determined by the VPC where the instance locates. For more information, please see [VPC and Subnet](https://cloud.tencent.com/doc/product/215/4927).

## Private network DNS 
Private network DNS service is used for domain name resolution. If DNS configuration is incorrect, the domain name will become inaccessible. Therefore, Tencent Cloud provides reliable private network DNS servers in different regions. Specific configurations are shown below:
<table><tbody>
<tr><th>Network Environment</th><th>Region</th><th>Private Network DNS Server</th></tr>
<tr><td rowspan="7">Basic network</td><td>Guangzhou</td><td>10.225.30.181<br>10.225.30.223</td></tr>
<tr><td>Shanghai</td><td>10.236.158.114<br>10.236.158.106</td></tr>
<tr><td>Beijing</td><td>10.53.216.182<br>10.53.216.198</td></tr>
<tr><td>Shanghai Finance</td><td>10.48.18.9<br>10.48.18.82</td></tr>
<tr><td>North America</td><td>10.116.19.188<br>10.116.19.185</td></tr>
<tr><td>Hong Kong</td><td>10.243.28.52<br>10.225.30.178</td></tr>
<tr><td>Singapore</td><td>100.78.90.19<br>100.78.90.8</td></tr>
<tr><td>VPC</td><td>All regions</td><td>183.60.83.19<br>183.60.82.98</td></tr>
</tbody>
</table>

When a network resolution error occurs, users can set the private network DNS manually. The private network DNS can be set as follows:

- For Linux systems, the CVM DNS can be modified by editing the `/etc/resolv.conf` file.
  Run the command `vi /etc/resolv.conf`, and edit the DNS IP of the region according to the above table.
  ![](https://mc.qcloudimg.com/static/img/fa8ecdf52b7f51361c369dbc96eea4ec/image.png)

- For Windows systems, users can open "Control Panel" - "Network and Sharing Center" - "Change Adapter Settings", right-click the "Property" of the ENI, and double-click the "Internet Protocol Version 4" to modify the DNS server.
  ![](https://mc.qcloudimg.com/static/img/beb44bdaad8d90c9534891b725a1d3a6/image.png)
  ![](https://mc.qcloudimg.com/static/img/7f6590044c32188faa7f8e749aade9fe/image.png)

## Obtain the private IP of an instance
You can use Tencent Cloud Console and API to obtain the private IP of an instance. You can also use instance metadata to obtain the private IP of an instance from the instance. For more information, please see [Instance Metadata](/doc/product/213/4934).

### Obtain the private IP of an instance in console

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) The CVM list displays the instances under your account. Move the mouse over the private IP of the CVM, and the "Copy" button will appear; click the button to copy this IP.

3) (Optional) Click the ID of the CVM instance you want to check to enter the details page of the CVM, and then view the specific information, including **Parameter**, **Monitor**, **Health check**, **Security group** and **Operation log**.

> The public IP is mapped to the private IP through NAT. Therefore, if you check the attributes of the network interface in the instance (for example, through ifconfig (Linux) or ipconfig (Windows)), the public IP is not displayed.

### Obtain the private IP of an instance using API
Please see [DescribeInstances API](https://cloud.tencent.com/doc/api/229/831).

### Obtain the private IP of an instance using instance metadata

First, you need to log in to the CVM instance. For more information, please see [Log in to CVM Instance on Linux](https://cloud.tencent.com/document/product/416/5436) and [Log in to CVM Instance on Windows](https://cloud.tencent.com/document/product/416/5435).

Use the following command to obtain the private IP:

```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1eeb9557a8.png)

