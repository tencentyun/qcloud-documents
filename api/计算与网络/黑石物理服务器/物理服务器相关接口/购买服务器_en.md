## 1. API Description
 
This API (BuyDevice) is used to purchase CPM. Charges will be automatically deducted.

Domain for API request: bm.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId | Yes | Int | Availability zone ID. You can acquire availability zone information of Cloud Physical Machines by using the [Query Regions and Availability Zones (DescribeRegions)](/doc/api/456/6634) API. |
| vpcId | Yes | Int | VPC ID. You can acquire VPC information by using the [Query VPC List (DescribeBmVpcEx)](/doc/api/456/6646) API. |
| subnetId | Yes | Int | Subnet ID. You can acquire private subnet information by using the [Query Subnet List (DescribeBmSubnetEx)](/doc/api/456/6648) API. |
| deviceClassCode | Yes | String | Device class code (the "code" displayed in the purchase page). You can acquire device class information by using the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636) API, where the "deviceClassDisplay" field is the value required by deviceClassCode |
| osTypeId | Yes | Int | Operating system type ID. You can acquire operating system information by using the [Query List of Operating Systems (DescribeOs)](/doc/api/456/6727) API. |
| raidId | Yes | Int | RAID type ID. You can acquire RAID information by using the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6640) API. |
| timeUnit | Yes | String | Measurement unit for purchased usage period. Available value: m: purchase by month.  |
| timeSpan | Yes | Int | Purchased usage period.  |
| goodsNum | Yes | Int | Number of CPMs to purchase.  |
| hasWanIp | No | Int | Whether to assign public IP. 0: Do not assign; 1: Assign. Default is 0. |
| needSecurityAgent | No | Int | Whether to install security Agent. 0: Do not install; 1: Install. Default is 0.  |
| needMonitorAgent | No | Int | Whether to install monitor Agent. 0: Do not install; 1: Install. Default is 0.  |
| alias | No | String | Device alias. The aliases will be automatically numbered if you purchase multiple machines.  |
| sysRootSpace | No | Int | System disk root partition size. Default is 10 G. For the size of system disk, please see the [Query RAID Method of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370) API |
| sysSwaporuefiSpace | No | Int | The size of swap partition or /boot/efi partition of system disk. When the machine boots in UEFI mode, the partition is /boot/efi with a default size of 2 G. The partition is swap for normal machines, in which case you don't need to specify this partition. To determine whether the machine boots in UEFI mode, please see the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636) API |
| sysUsrlocalSpace | No | Int | Size of /usr/local partition. This partition does not exist by default.  |
| sysDataSpace | No | Int | Size of /data partition. Any remaining space of the system disk will be allocated to the /data partition.  |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | obj | Returned order information.  |

data is the json information of the order. It contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealNames | Array | Array. Array elements are order numbers.  |
| resourceIds | Obj | key is order number, corresponding value is the array containing CPM IDs. | 


## 4. Module Error Codes

| code | codeDesc | Description |
|------|------| --------|
| 9009 | InternalError.TradeError | Tencent internal transaction error |
| 100001 | InvalidParameter | Incorrect parameter |
| 100004 | OperationDenied.NoPermission | The operation is not supported |
| 500008 | TradeError.QueryPriceError | Price query failed |
| 100002 | TradeError.DbError | DB operation of the transaction failed |
| 100612 | TradeError.CouponInvalid | Invalid coupon |
| 700104 | TradeError.GoodsConfigInvalid | Failed to obtain commodity configuration |
| 700108 | TradeError.GoodsCodeInvalid | Invalid commodity ID |
| 700102 | TradeError.CheckGoodsError | Service parameter verification failed |
| 700110 | TradeError.OperationDenied | The operation is not allowed for the commodity |
| 700007 | TradeError.ResourceLimit | Purchase quantity exceeded the limit |
| 100207 | TradeError.InsufficientMoney | Insufficient balance |
| 100200 | TradeError.PayFail | Payment failed |
| 100188 | TradeError.BillPartialError | Payment succeeded, but some of the ordered goods failed to be delivered |
| 500006 | TradeError.PayingError | Error occurred during payment procedure |


## 5. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=BuyDevice
	&zoneId=1000800001
	&vpcId=1042
	&subnetId=110
	&deviceClassCode=PS100
	&osTypeId=2
	&raidId=3
	&timeUnit=m
	&timeSpan=2
	&goodsNum=5
	&hasWanIp=1
	&needSecurityAgent=1
	&alias=Instance name
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

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
    },
    "dealIds": [
      "454013"
    ]
  }
}

```
