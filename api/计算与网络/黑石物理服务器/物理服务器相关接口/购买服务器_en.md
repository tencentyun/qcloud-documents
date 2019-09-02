## Description

This API (BuyDevice) is used to purchase CPMs. Charges will be automatically deducted.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example

```
https://bm.api.qcloud.com/v2/index.php?
	Action=BuyDevice
	&<Common request parameters>
	&zoneId=<Availability zone ID>
	&unVpcId=<Vpc ID>
	&unSubnetId=<Subnet ID>
	&deviceClassCode=<Device class code>
	&osTypeId=<Operating system type ID>
	&raidId=<RAID type ID>
	&timeUnit=<Measurement unit for purchased usage period>
	&timeSpan=<Purchased usage period>
	&goodsNum=<Number of CPMs to purchase>
	&hasWanIp=<Whether to assign public IP>
	&needSecurityAgent=<Whether to install security Agent>
	&needMonitorAgent=<Whether to install monitor Agent>
	&alias=<Device alias>
	&sysRootSpace=<System disk root partition size>
	&sysSwaporuefiSpace=<The size of swap partition or /boot/efi partition of system disk>
	&sysDataSpace=<Size of /data partition>
	&hyperThreading=<Whether to enable Hyper-Threading>
	&autoRenewFlag=<Whether to enable auto renewal>
	&ipList=<IP specified during the purchase>
```

### Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For other parameters, please see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is BuyDevice.

| Parameter Name | Required | Type | Description |
| ------------------ | ---- | ------------- | ---------------------------------------- |
| zoneId | Yes | Int | Availability zone ID. The availability zone information of CPM can be obtained via the API [Query Regions and Availability Zones (DescribeRegions)](/doc/api/456/6634). |
| unVpcId | Yes | String | VPC ID. You can obtain the VPC information using the API [Query VPC List (DescribeBmVpcEx)](/doc/api/456/6646), and take the value of unVpcId field, such as vpc-8e0ypm3z. |
| unSubnetId | Yes | String | Subnet ID. You can obtain the VPC subnet information using the API [Query Subnet List (DescribeBmSubnetEx)](/doc/api/456/6648), and take the value of unSubnetId field, such as subnet-34xt45as. |
| deviceClassCode | Yes | String | Device class code, i.e. the "code" on the Purchase page. You can obtain the device class information using the API [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636), where the "deviceClassCode" field is the value required by deviceClassCode. |
| osTypeId | Yes | Int | Operating system type ID. The operating system information can be obtained via the API [Query OS List (DescribeOs)](/doc/api/456/6727). |
| raidId | Yes | Int | RAID type ID. The RAID information can be obtained via the API [Query RAID Mode of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/api/386/7370).
| timeUnit | Yes | String | Measurement unit for purchased usage period. m: Purchase on a monthly basis. |
| timeSpan | Yes | Int | Purchased usage period |
| goodsNum | Yes | Int | Number of CPMs to purchase |
| hasWanIp | No | Int | Whether to assign public IP. 0: Do not assign (default); 1: Assign. |
| needSecurityAgent | No | Int | Whether to install security Agent. 0: Do not install (default); 1: Install. |
| needMonitorAgent | No | Int | Whether to install monitor Agent. 0: Do not install (default); 1: Install. |
| alias | No | String | Device alias. If you purchase multiple devices, aliases are automatically numbered. |
| sysRootSpace | No | Int | System disk root partition size (in GB). Default is 10 GB. For more information on system disk size, please see the API [Query RAID Mode of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370). |
| sysSwaporuefiSpace | No | Int | The size of swap partition or /boot/efi partition of system disk (in GB). When the machine starts in UEFI mode, the partition is /boot/efi with a default size of 2 GB. The partition is swap for normal machines, in which case you don't need to specify this partition. To determine whether the machine starts in UEFI mode, please see the API [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636). |
| sysDataSpace | No | Int | The size of /data partition (in GB). Any remaining space of the system disk will be assigned to the /data partition. (Note: If the free space is less than 10 GB and the /data partition is not specified, the remaining space is assigned to the Root partition.) |
| hyperThreading | No | Int | Whether to enable Hyper-Threading. 0: Disable; 1: Enable (default). |
| autoRenewFlag | No | Int | Whether to enable auto renewal. 0: Disable (default); 1: Enable. |
| ipList | No | Array (String) | The IP specified during the purchase. |
| fileSystem | No | String | Specify the file system format (ext4 and xfs) of the data disk. Default is ext4. This parameter applies to the data disk and Linux, and takes effect when isZoning is 1. |


## Response

### Response Example

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "dealNames": [
      "20160721110015"
    ],
    "resourceIds": {
      "20160721110015": [
        "dcpm-iizn577x",
        "dcpm-ntlsj9gh"
      ]
    }
  }
}
```

## Response Parameters

The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including order ID and CPM ID.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | Returned order information. See details below. |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ----------- | ------------- | ------------------------------- |
| dealNames | Array (String) | An array of strings. Array element is order ID. |
| resourceIds | Object | Order ID is the key, and the corresponding value is the array of strings. Array element is CPM ID. |


## Error Codes
| Error Code | Error Message | Error Description |
| ------ | ----------------------------- | ------------- |
| 9009 | InternalError.TradeError | Tencent internal transaction error |
| 100001 | InvalidParameter | Invalid parameter |
| 100004 | OperationDenied.NoPermission | The operation is not supported |
| 500008 | TradeError.QueryPriceError | Price query failed |
| 100002 | TradeError.DbError | DB operation of the transaction failed |
| 100612 | TradeError.CouponInvalid | Invalid coupon |
| 700104 | TradeError.GoodsConfigInvalid | Failed to obtain goods configuration |
| 700108 | TradeError.GoodsCodeInvalid | Invalid goods ID |
| 700102 | TradeError.CheckGoodsError | Service parameter verification failed |
| 700110 | TradeError.OperationDenied | The operation is not allowed for the commodity |
| 700007 | TradeError.ResourceLimit | Purchase quantity exceeded the limit |
| 100207 | TradeError.InsufficientMoney | Insufficient balance |
| 100200 | TradeError.PayFail | Payment failed |
| 100188 | TradeError.BillPartialError | Payment succeeded, but the delivery of some of the ordered goods failed |
| 500006 | TradeError.PayingError | An error occurred during payment |

## Practical Case

### Input

```
	https://bm.api.qcloud.com/v2/index.php?	
	Action=BuyDevice
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
	&zoneId=1000800001
	&unVpcId=vpc-8e0ypm3z
	&unSubnetId=subnet-34xt45as
	&deviceClassCode=PS100v1
	&osTypeId=2
	&raidId=3
	&timeUnit=m
	&timeSpan=2
	&goodsNum=5
	&hasWanIp=1
	&needSecurityAgent=1
	&alias=Instance name
```
### Output

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "dealNames": [
      "20160721110015"
    ],
    "resourceIds": {
      "20160721110015": [
        "dcpm-iizn577x",
        "dcpm-ntlsj9gh"
      ]
    }
  }
}
```

