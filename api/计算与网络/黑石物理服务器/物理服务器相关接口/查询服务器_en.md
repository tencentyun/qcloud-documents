## Description

This API (DescribeDevice) is used to query the server list.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDevice
	&<Common request parameters>
	&offset=<Offset value>
	&limit=<The number of returned CPMs>
	&unVpcId=<VPC ID>
	&deviceClassCode=<Device class>
	&instanceIds.0=<Device ID1>
	&instanceIds.1=<Device ID2>
	&lanIps.0=<Business private IP 1>
	&lanIps.1=<Business private IP 2>
	&alias=<Instance name>
```

### Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For other parameters, please see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeDevice.

| Parameter Name | Required | Type | Description |
| ----------------- | ---- | ------------- | ---------------------------------------- |
| offset | No | Int | Offset value. Default is 0. |
| limit | No | Int | The number of returned CPMs. Default is 20. |
| unVpcId | No | String | VPC ID. You can obtain the VPC information using the API [Query VPC List (DescribeBmVpcEx)](/doc/api/456/6646), and take the value of unVpcId field, such as vpc-8e0ypm3z. |
| unSubnetId | No | String | Subnet ID. You can obtain the VPC subnet information using the API [Query Subnet List (DescribeBmSubnetEx)](/doc/api/456/6648), and take the value of unSubnetId field, such as subnet-34xt45as. |
| deviceClassCode | No | String | Device class. The device class information can be obtained via the API [DescribeDeviceClass](/doc/api/456/6636). |
| lanIps | No | Array (String) | List of business private IPs |
| wanIps | No | Array (String) | List of public IPs |
| instanceIds | No | Array (String) | List of device IDs |
| alias | No | String | Device alias, used for fuzzy search |
| deadlineStartTime | No | String | Filter operation is performed based on device expiration time (start time). Time format: "2016-05-25 12:00:00". |
| deadlineEndTime | No | String | Filter operation is performed based on device expiration time (end time). Time format: "2016-05-25 13:00:00". |
| autoRenewFlag | No | Int | Auto renewal flag. 0: Disable auto renewal. 1: Enable auto renewal. |


## Response

### Response Example
```
{
  "code": 0,
  "message": "OK",
  "data": {
    "totalNum": 2,
    "deviceList": [
      {
        "instanceId": "cpm-d1y5rcex3",
        "subnetId": "3",
        "vpcId": "1025",
        "unVpcId": "vpc-8e0ypm3z",
        "unSubnetId" : "subnet-34xt45as",
        "lanIp": "10.6.10.67",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "Gateway device",
        "appId": "1251000000",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "",
        "deliverTime": "2016-05-10 17:54:48",
        "deadline": "2018-05-10 00:00:00",
        "isVpcGateway": "1",
        "autoRenewFlag": "1",
        "deviceClass" : "M10",
		"deviceClassCode" : "PS100v1"
      },
      {
        "instanceId": "cpm-lad4pu06",
        "subnetId": "4",
        "vpcId": "1025",
		"unVpcId": "vpc-8e0ypm3z",
        "unSubnetId" : "subnet-34xt45as",
        "lanIp": "10.6.10.73",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "Server",
        "appId": "1251001002",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "115.159.240.23",
        "deliverTime": "2016-05-17 18:23:24",
        "deadline": "2017-03-18 22:40:09",
        "isVpcGateway": "0",
        "autoRenewFlag": "0",
        "deviceClass" : "TS60",
		"deviceClassCode" : "PI102v1"
      }
    ],
    "serverTimestamp": 1464164820301
  }
}
```

## Response Parameters
The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including servers.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | Device list. See details below. |


Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ---------- | ------------- | ------------------------------------- |
| totalNum | Int | Total number of devices |
| deviceList | Array (Object) | An array of objects. Array element is the device information. See details below. |

Parameter deviceList is composed as follows:

| Parameter Name | Type | Description |
| ------------- | ------ | ---------------------------------------- |
| instanceId | String | Device ID |
| vpcId | Int | VPC ID (Integer) |
| subnetId | Int | VPC subnet ID (Integer) |
| unVpcId | String | VPC ID (String) |
| unSubnetId | String | VPC subnet ID (String) |
| deviceStatus | Int | Running status of the device. [See](#deviceStatus). |
| operateStatus | Int | Operation status of the device. [See](#operateStatus). |
| osTypeId | Int | Operating system ID. For the meaning of operating system, please see the API [Query OS List (DescribeOs)](/doc/api/456/6727). |
| raidId | Int | RAID mode ID. For the meaning of RAID, please see the API [Query RAID Mode of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370). |
| alias | String | Device alias |
| wanIp | String | EIP |
| lanIp | String | Business private IP |
| deliverTime | String | Device delivery time |
| deadline | String | Device expiration time |
| autoRenewFlag | Int | Auto renewal flag. 0: Disable auto renewal. 1: Enable auto renewal. |
| deviceClass | String | Device class |
| deviceClassCode | String | Device classes sold on Tencent Cloud |

#### Running Status of Device

| Status ID | Meaning |
| ---- | ------- |
| 1 | Applying for device |
| 2 | Initializing device |
| 3 | Initialization failed |
| 4 | Running |
| 5 | Hardware failure |
| 6 | Network configuration error |
| 7 | Isolating |
| 8 | Isolated |
| 9 | Isolation failed |
| 10 | De-isolating |
| 11 | De-isolation failed |
| 12 | Deactivating |
| 13 | Deactivated |
| 14 | Expired |

#### Operation Status of Device

| Status ID | Meaning |
| ---- | ------ |
| 1 | Running |
| 2 | Shutting down |
| 3 | Shut down |
| 4 | Shutdown failed |
| 5 | Starting up |
| 6 | Startup failed |
| 7 | Restarting |
| 8 | Restart failed |
| 9 | Reinstalling system |
| 10 | System reinstallation failed |
| 11 | Resetting password |
| 12 | Binding EIP |
| 13 | Unbinding EIP |
| 14 | Binding BM load balancer |
| 15 | Unbinding BM load balancer |

## Error Codes

| Error Code | Error Message | Error Description |
| ----- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |
| 10001 | InvalidParameter | Invalid parameter |


## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDevice
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
	&offset=1
	&limit=30
	&unVpcId=vpc-8e0ypm3z
    &deviceClass=M10
    &instanceIds.0=cpm-34xw423x
    &instanceIds.1=cpm-34xw234y
    &lanIps.0=10.1.1.1
    &lanIps.1=10.1.2.2
	&alias=Instance name
```

### Output

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "totalNum": 2,
    "deviceList": [
      {
        "instanceId": "cpm-d1y5rcex3",
        "subnetId": "3",
        "vpcId": "1025",
		"unVpcId": "vpc-8e0ypm3z",
        "unSubnetId" : "subnet-34xt45as",
        "lanIp": "10.6.10.67",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "Gateway device",
        "appId": "1251000000",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "",
        "deliverTime": "2016-05-10 17:54:48",
        "deadline": "2018-05-10 00:00:00",
        "isVpcGateway": "1",
        "autoRenewFlag": "1",
        "deviceClass" : "M10",
		"deviceClassCode" : "PS100v1"
      },
      {
        "instanceId": "cpm-lad4pu06",
        "subnetId": "4",
        "vpcId": "1025",
		"unVpcId": "vpc-8e0ypm3z",
        "unSubnetId" : "subnet-34xt45as",
        "lanIp": "10.6.10.73",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "Server",
        "appId": "1251001002",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "115.159.240.23",
        "deliverTime": "2016-05-17 18:23:24",
        "deadline": "2017-03-18 22:40:09",
        "isVpcGateway": "0",
        "autoRenewFlag": "0",
        "deviceClass" : "TS60",
		"deviceClassCode" : "PI102v1"
      }
    ],
    "serverTimestamp": 1464164820301
  }
}
```
