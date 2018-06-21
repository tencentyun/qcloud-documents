Instance metadata refers to the data of the instance that you operate on, and can be used to configure and manage running instances.

>Note: While instance metadata can only be accessed internally from the instance, the data has not been protected through encryption. Anyone who accesses the instance can view its metadata. Therefore, you should take proper precautions to safeguard sensitive data (e.g. using permanent encryption key).


## Instance Metadata Classification
Now Tencent Cloud provides the following metadata information:

| Data | Description | Latest Version |
|---------|---------|---------|
| instance-id | Instance ID | 1.0 |
| uuid | Instance ID | 1.0 |
| local-ipv4 | Private IP of instance | 1.0 |
| public-ipv4 | Public IP of instance | 1.0 |
| mac | MAC address of instance's eth0 device | 1.0 |
| placement/region | Information of the region in which the instance resides | 2017-09-19 |
| placement/zone | Information of the availability zone in which the instance resides | 2017-09-19 |
| network/interfaces/macs/<font style="color:red">mac</font>/mac | The device address for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/primary-local-ipv4 | The primary private IP for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/public-ipv4s | The public IP for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/gateway | The gateway address for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/local-ipv4 | The private IP for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/public-ipv4 | The public IP for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/public-ipv4-mode | The public network mode for the network interface of the instance | 1.0 |
| network/interfaces/macs/<font style="color:red">mac</font>/local-ipv4s/<font style="color:red">local-ipv4</font>/subnet-mask | The subnet mask for the network interface of the instance | 1.0 |

> Fields <font style="color:red">mac</font> and <font style="color:red">local-ipv4</font> in red in the above table refer to the device address and private IP of the network interface specified for the instance, respectively.
> 
> The destination URL address of the request is case sensitive. You must construct the destination URL address of a new request according to the returned result of the request.
>
> The data returned by `placement` is changed in the current version (2017-09-19). If you need to use the data of the version 1.0, you can specify the path of the previous version or do not specify the version path so as to access the data of version 1.0. For more information on the data returned by `placement`, please see [Region and Availability Zone](/document/product/213/6091).

## Querying Instance Metadata
Within the instance, you can access data, such as local IP and public IP of instance, via instance metadata to manage the connection with external applications.
To view all types of instance metadata within the running instance, use the following URI:
```
http://metadata.tencentyun.com/latest/meta-data/
```
You can access metadata via the cURL tool or HTTP GET request. For example:
```
curl http://metadata.tencentyun.com/latest/meta-data/
```
* For resources that do not exist, HTTP error code 404 - Not Found is returned.
* The operations on the instance metadata can only be performed **within the instance**. Log in to the instance first. For more information on instance login, please see [Log in to Windows Instance](/doc/product/213/5435) and [Log in to Linux Instance](/doc/product/213/5436).

### Examples of Metadata Querying

The following example shows how to get metadata version. For now, the metadata versions include "1.0", "2017-09-19" and "latest". Tencent Cloud may release new metadata versions time by time. You can specify the version that your application or scripts depending on. Data of Version 1.0 is returned if not specified.
```
[qcloud-user]# curl http://metadata.tencentyun.com/
1.0
2017-09-19
latest
meta-data
```

The following example shows how to view the metadata root directory. The words ending with `/` represent directories, and words that do not end with `/` represent access data. For the meaning of the specific access data, please see the **Instance Metadata Classification** above.
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

The following example shows how to get the physical location of the instance. For the relationship between returned data and the physical location, please see [Region and Availability Zone](/document/product/213/6091).
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/placement/region
ap-guangzhou

[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/placement/zone
ap-guangzhou-3
```

The following example shows how to get the private IP of the instance. If there is more than one ENI in the instance, the network address of the eth0 device is returned.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/local-ipv4
10.104.13.59
```

The following example shows how to get the public IP of the instance.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/public-ipv4
139.199.11.29
```

The following example shows how to get the instance ID. Instance ID is the unique identifier of the instance.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/instance-id
ins-3g445roi
```

The following example shows how to get the instance uuid. The uuid is also a unique identifier of the instance. However it is recommended to use instance ID above.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/uuid
cfac763a-7094-446b-a8a9-b995e638471a
```

The following example shows how to get MAC address of eth0 device of the instance.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/mac
52:54:00:BF:B3:51
```

The following example shows how to get ENI information of the instance. Multiple lines of data will be returned for multiple ENIs. Each line contains the data directory of an ENI.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/
52:54:00:BF:B3:51/
```

The following example shows how to get the information of a specified ENI.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/
local-ipv4s/
mac
primary-local-ipv4
public-ipv4s
```

The following example shows how to get a list of private IP addresses bound to a specified ENI. If the ENI is bound to multiple private IPs, multiple lines of data are returned.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/
10.104.13.59/
```

The following example shows how to get the information of private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59
gateway
local-ipv4
public-ipv4
public-ipv4-mode
subnet-mask
```

The following example shows how to get the private IP gateway. This data is only available to instance using VPC. For more information on VPC, please see [Private Network](/document/product/215).
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/gateway
10.15.1.1
```

The following example shows how to get the access mode of private IP to public network. This data is only available to instance using VPC. Instance using basic network can access Internet via public network gateway.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/public-ipv4-mode
NAT
```

The following example shows how to get the public network IP bound to the private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/public-ipv4
139.199.11.29
```

The following example shows how to get the subnet mask of the private IP.
```
[qcloud-user]# curl http://metadata.tencentyun.com/latest/meta-data/network/interfaces/macs/52:54:00:BF:B3:51/local-ipv4s/10.104.13.59/subnet-mask
255.255.192.0
```

