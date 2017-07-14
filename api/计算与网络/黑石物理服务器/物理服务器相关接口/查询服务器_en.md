## 1. API Description
 
This API (DescribeDevice) is used to query the list of CPMs.

Domain for API request: bm.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| offset | No | Int | Offset. Default is 0 |
| limit | No | Int | Number of returned CPMs. Default is 20 | 
| vpcId | No | Int | VPC ID | 
| subnetId | No | Int | Private subnet ID |
| deviceClass | No | String | Device class. You can acquire device class information by using the [DescribeDeviceClass](/doc/api/456/6636) API |
| lanIps | No | Array | List of business private IPs |
| wanIps | No | Array | List of public IPs |
| instanceIds | No | Array | Unique device ID |
| alias | No | String | Device alias, used for fuzzy search |
| deadlineStartTime | No | String | Filter operation is based on device expiration time (start time). Time format: "2016-05-25 12:00:00" |
| deadlineEndTime | No | String | Filter operation is based on device expiration time (end time). Time format: "2016-05-25 13:00:00" |
| autoRenewFlag | No | Int | Auto-renewal flag. 0: Disable auto renewal. 1: Enable auto renewal |
  


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | obj | Device list |

data is the json information of the device list. It contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalNum | Int | Total number of devices |
| deviceList | Array | Array. Array element is device information |

Device information element in deviceList

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | Unique device ID |
| vpcId | Int | VPC ID |
| subnetId | Int | Private subnet ID |
| deviceStatus | Int | Running status of the device. [View](#deviceStatus) |
| operateStatus | Int | Operation status of the device. [View](#operateStatus) |
| osTypeId | Int | Operating system ID. For the meanings of operating systems, please see the [Query List of Operating Systems (DescribeOs)](/doc/api/456/6727) API |
| raidId | Int | RAID method ID. For the meanings of RAID, please see the [Query RAID Method of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370) API |
| alias | String | Device alias |
| wanIp | String | Elastic IP |
| lanIp | String | Business private IP |
| deliverTime | String | Device delivery time |
| deadline | String | Device expiration time |
| autoRenewFlag | Int | Auto-renewal flag. 0: Disable auto renewal. 1: Enable auto renewal |


<br/>
<span id="deviceStatus">Running status of the device</span>

| Status ID | Meaning |
|---------|---------|
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
| 12 | Going offline |
| 13 | Offline |
| 14 | Expired |

<br/>

<span id="operateStatus">Operation status of the device</span>

| Status ID | Meaning |
|---------|---------|
| 1 | Running |
| 2 | Shutting down |
| 3 | Shut down |
| 4 | Shut down failed |
| 5 | Booting |
| 6 | Boot failed |
| 7 | Rebooting |
| 8 | Reboot failed |
| 9 | Re-installing system |
| 10 | System re-installation failed |
| 11 | Resetting password |
| 12 | Binding EIP |
| 13 | Unbinding EIP |
| 14 | Binding BM load balancer |
| 15 | Unbinding BM load balancer |



## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10001 | InvalidParameter | Invalid parameter |


## 5. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=DescribeDevice
	&offset=1
	&limit=30
	&vpcId=1024
    &deviceClass=M10
    &instanceIds.1=cpm-34xw423x
    &instanceIds.2=cpm-34xw234y
    &lanIps.1=10.1.1.1
    &lanIps.2=10.1.2.2
	&alias=Instance name
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

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
        "lanIp": "10.6.10.67",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "Gateway Device",
        "appId": "1251000000",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "",
        "deliverTime": "2016-05-10 17:54:48",
        "deadline": "2018-05-10 00:00:00",
        "isVpcGateway": "1",
        "autoRenewFlag": "1"
      },
      {
        "instanceId": "cpm-lad4pu06",
        "subnetId": "4",
        "vpcId": "1025",
        "lanIp": "10.6.10.73",
        "deviceStatus": "4",
        "operateStatus": "1",
        "osTypeId": "1",
        "raidId": "1",
        "alias": "CPM",
        "appId": "1251001002",
        "zoneId": "1000800001",
        "projectId": "0",
        "wanIp": "115.159.240.23",
        "deliverTime": "2016-05-17 18:23:24",
        "deadline": "2017-03-18 22:40:09",
        "isVpcGateway": "0",
        "autoRenewFlag": "0",
        "updateTime": "2016-05-19 19:34:33"
      }
    ],
    "serverTimestamp": 1464164820301
  }
}

```
