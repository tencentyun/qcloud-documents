Instance metadata refers to the data of the instance that you operate on, and can be used to configure and manage running instances.

>Note: Although instance metadata can only be accessed internally from the instance, the data has not been protected through encryption. Anyone who accesses the instance can view its metadata. Therefore, you should take proper precautions to protect sensitive data. For example, using permanent encryption key.

## Instance meta-data
Tencent Cloud provides the following meta-data information:

| Data | Description | Introduced Version |
|---------|---------|---------|
| instance-id | Instance ID | 1.0 |
| uuid | Instance ID | 1.0 |
| local-ipv4 | Instance private IP | 1.0 |
| public-ipv4 | Instance public IP | 1.0 |
| mac | MAC address of instance's eth0 device | 1.0 |
| placement/region | Information of the region in which the instance resides | 1.1 |
| placement/zone | Information of the availability zone in which the instance resides | 1.1 |
| network/network/macs/**mac**/mac | The device address for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/primary-local-ipv4 | The primary private IP for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/public-ipv4s | The public IP for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/gateway | The gateway address for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/local-ipv4 | The private IP for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4 | The public IP for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4-mode | The public network mode for the network interface of the instance | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/subnet-mask | The subnet mask for the network interface of the instance | 1.2 |

> Fields **mac** and **local-ipv4** in bold in the above table refer to the device address and private IP of the network interface specified for the instance, respectively.
> 
> The destination URL address of the request is case sensitive. You must construct the destination URL address of a new request according to the returned result of the request.

## Querying Instance Metadata

Operations on the instance metadata can only be performed **internally within the instance**. You first need to log in to the instance. For more information, please see [Log in to Windows Instance](https://intl.cloud.tencent.com/document/product/213/5435) and [Log in to Linux Instance](https://intl.cloud.tencent.com/document/product/213/5436).


### Querying All Available Meta-data Types
Command:
```
curl http://metadata.tencentyun.com/
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1ebcbd924d.png)

Command:

```
curl http://metadata.tencentyun.com/meta-data
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1ed1128bd4.png)

The placement field includes two types of data: region and zone.

Command:

```
curl http://metadata.tencentyun.com/meta-data/placement
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1edb2b1349.png)



### Querying Instance Private IP
Command:
```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1eeb9557a8.png)

### Querying Instance Public IP
Command:
```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1f015c48e5.png)

### Querying Instance ID
Command:
```
curl http://metadata.tencentyun.com/meta-data/instance-id
```
or
```
curl http://metadata.tencentyun.com/meta-data/uuid
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1f1c703176.png)
![](//mccdn.qcloud.com/img56a1f35d0bb18.png)

### Querying the Device Address of Instance eth0
Command:
```
curl http://metadata.tencentyun.com/meta-data/mac
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1f2800a4e2.png)

### Querying the Region of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/placement/region
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1f3ecd50a2.png)

### Querying the Availability Zone of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/placement/zone
```
The returned value is as follows
![](//mccdn.qcloud.com/img56a1f45687788.png)

### Querying the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/ca12b20583f602d75a541d1a43452c2d/8.1.jpg)

Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/ced32a2fee5e5282cd038d4034fb11a0/8.2.jpg)

### Querying the Details for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/4ee3cd5e1bcba00e846282aab4e352a0/9.jpg)

### Querying the List of Private IPs for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/8a7e0b0e41a65b683f2f530131a45d07/10.jpg)

### Querying the Device Address for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/mac
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/0627af2fbc1aada52f5821f92d200f44/11.jpg)

### Querying the List of Private IPs for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/primary-local-ipv4
```
The returned value is as follows:
![](https://mc.qcloudimg.com/static/img/5458ecf47ec14ba9151e95d7eaa2efd4/12.jpg)

### Querying the List of Public IPs for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/public-ipv4s
```
The returned value is as follows:
![](https://mc.qcloudimg.com/static/img/19fa044afd25b8714b38312c7b3eef6c/13.jpg)

### Querying the Network Information for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/5c0b23aa98661c533b2ee9cfae3a79cd/14.jpg)

### Querying the Gateway Address for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/gateway
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/d297cd00f025c845111a50ee9874612d/15.jpg)

### Querying the Private IP for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/local-ipv4
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/24470fccb042eb877763a03100da8a10/16.jpg)

### Querying the Public IP for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/c0344e7c89ab0643884d8ac2b859711b/17.jpg)

### Querying the Public Network Mode for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4-mode
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/115617733703e99602627bb3ce1f32cc/18.jpg)

> Note:
- NAT: Network Address Translation, the network address translation.
- direct: Connect to the network directly. Access the public network directly through the public IP for the network interface of instance using a router.

### Querying the Subnet Mask for the Network Interface of Instance
Command:
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/subnet-mask
```
The returned value is as follows:
 ![](https://mc.qcloudimg.com/static/img/ca9589a75e2a04859e3004e4b72ee967/19.jpg)

