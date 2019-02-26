Instance metadata is the data of the instances you are running and can be used to configure or manage the running instances.

>Note: Although the instance metadata can only be accessed from within the instance itself, the data is not encrypted and protected. Anyone who has the access to an instance also has the access to its metadata. Therefore, it is recommended to take appropriate measures to protect sensitive data (e.g. using a permanent encryption key).


## Overview of Instance Metadata 
Tencent Cloud provides the following meta-data:

| Data | Description | Version Where It Was Introduced |
|---------|---------|---------|
| instance-id | Instance ID | 1.0 |
| uuid | Instance ID | 1.0 |
| local-ipv4 | Instance's private IP | 1.0 |
| public-ipv4 | Instance's public IP | 1.0 |
| mac | MAC address of instance's eth0 device | 1.0 |
| placement/region | Information of the region where the instance resides | Updated on Sept 19, 2017 |
| placement/zone | Information of the availability zone where the instance resides | Updated on Sept 19, 2017 |
| network/interfaces/macs/<font style="color:red">mac</font>/mac | Device address of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/primary-local-ipv4 | Primary private IP of instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/public-ipv4s | Public IP of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/gateway | Gateway address of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/local-ipv4 | Private IP of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/public-ipv4 | Public IP of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/public-ipv4-mode | Public network mode of the instance's network interface | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/subnet-mask | Subnet mask of the instance's network interface | 1.0 |

> Fields <font style="color:red">mac</font> and <font style="color:red">local-ipv4</font> in red in the above table indicate the device address and private IP of the network interface specified for the instance, respectively.
> 
> The requested target URL is case sensitive. > Construct the target URL address of new request in strict accordance with the format of the returned result of request.
>
> In the current version, the returned data of placement has been changed. To use the data in the previous version, specify the previous version path or leave the version path empty to access the data of version 1.0. For more information about the returned data of placement, please see [Region and Availability Zone](/document/product/213/6091).

## Querying Instance Metadata
You can access the instance metadata such as instance's local IP and public IP from within an instance to manage connections with external applications.
To view all the instance metadata from within a running instance, use the following URI:
```
http://metadata.tencentyun.com/latest/meta-data/
```
You can access metadata through the cURL tool or HTTP GET request, for example:
```
curl http://metadata.tencentyun.com/latest/meta-data/
```
* For resources that do not exist, HTTP error code "404 - Not Found" is returned.
* Any operation on instance metadata can only be performed **from within the instance**. Log in to the instance first. For more information on how to log in to an instance, please see [Logging in to Windows Instances](/doc/product/213/5435) and [Logging in to Linux Instances](/doc/product/213/5436).

### Example of querying metadata

The following example shows how to obtain the metadata version information. Note: When the Tencent Cloud modifies the metadata access path or returned data, a new metadata version is released. If your application or script depends on the structure or returned data of previous version, you can access metadata using the specified previous version. If no version is specified, version 1.0 is accessed by default.
```
[qcloud-user]# curl http://metadata.tencentyun.com/
1.0
2017-09-19
latest
meta-data
```

The following example shows how to view the metadata root directory. The line ending with `/` represents a directory and the one not ending with `/` represents the accessed data. For the description of accessed data, please see **Overview of Instance Metadata** described above.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/
instance-id
local-ipv4
mac
network/
placement/
public-ipv4
uuid
```

The following example shows how to obtain the physical location information of an instance. For the relationship between the returned data and the physical location, please see [Region and Availability Zone](/document/product/213/6091).
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/placement/region
ap-guangzhou

[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/placement/zone
ap-guangzhou-3
```

The following example shows how to obtain the private IP of an instance. If an instance has multiple ENIs, the network address of the eth0 device is returned.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/local-ipv4
10.104.13.59
```

The following example shows how to obtain the public IP of an instance.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/public-ipv4
139.199.11.29
```

The following example shows how to obtain an instance ID. Instance ID is used to uniquely identify an instance.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/instance-id
ins-3g445roi
```

The following example shows how to get the instance uuid. Instance uuid can also be used as the unique identifier of an instance, but it is recommended to use instance ID to distinguish between instances.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/uuid
cfac763a-7094-446b-a8a9-b995e638471a
```

The following example shows how to obtain the MAC address of an instance's eth0 device.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/mac
52:54:00:BF:B3:51
```

The following example shows how to obtain the ENI information of an instance. In case of multiple ENIs, multiple lines of data are returned, with each line indicating the data directory of an ENI.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/
52:54:00:BF:B3:51/
```

The following example shows how to obtain the information of specified ENI.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/
local-ipv4s/
mac
primary-local-ipv4
public-ipv4s
```

The following example shows how to obtain the list of private IPs bound to the specified ENI. If the ENI is bound with multiple private IPs, multiple lines of data are returned.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/
10.104.13.59/
```

The following example shows how to obtain the information of private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59
gateway
local-ipv4
public-ipv4
public-ipv4-mode
subnet-mask
```

The following example shows how to obtain the gateway of private IP (only for VPC-based CVMs). For more information about VPC-based CVMs, please see [Virtual Private Cloud (VPC)](/document/product/215).
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/gateway
10.15.1.1
```

The following example shows how to obtain the access mode used by a private IP to access the public network (only for VPC-based CVMs). A basic network-based CVM accesses the public network through the public gateway.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/public-ipv4-mode
NAT
```

The following example shows how to obtain the public IP bound to a private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/public-ipv4
139.199.11.29
```

The following example shows how to obtain the subnet mask of a private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/subnet-mask
255.255.192.0
```

