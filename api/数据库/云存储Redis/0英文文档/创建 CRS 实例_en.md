## 1. API Description
This API (CreateRedis) is used to create an instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

1) Instance capacity, measured in MB, is an integral multiple of 1024 and has a range subject to the specification returned via API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974). Value range: [data.types.minMemSize, data.types.maxMemSize]. The default value ranges for standalone instance and cluster instance are [1024MB, 61440MB] and [1024MB, 307200MB], respectively.
2) Number of instances to be purchased at a time should be subject to the specification returned via the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974). Value range: [data.types.minBuyNum, data.types.maxBuyNum], and default is: [1, 100]
3) Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]
4) Rule on password: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()).
5) You can apply for the purchase of an instance from an availability zone by submitting a [Ticket](https://console.cloud.tencent.com/workorder/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS)


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is CreateRedis.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId | Yes | UInt | ID of the availability zone to which the instance belongs |
| typeId | Yes | UInt | Instance type. 1 - Cluster; 2 - Standalone |
| memSize | Yes | UInt | Instance capacity (in MB), with the value being subject to the specification returned via the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974). Value range: [data.types.minMemSize, data.types.maxMemSize] |
| goodsNum | Yes | UInt | Number of instances. The number of instances to be purchased at a time should be subject to the specification returned via the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974). Value range: [data.types.minBuyNum, data.types.maxBuyNum] |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |
| password | Yes | String | Password for the instance. Rule: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()) |
| vpcId | No | UInt | This parameter is retained for historical reasons. It is recommended to use the following parameter unVpcId.  VPC ID. If it is left empty, the default is basic network. |
| unVpcId | No | String | VPC ID. If it is left empty, the default is basic network. This value is subject to the unVpcId returned by API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372), such as: vpc-kd7d06of |
| subnetId | No | UInt | This parameter is retained for historical reasons. It is recommended to use the following parameter unSubnetId. Subnet ID under VPC. If vpcId is set, subnetId is required. |
| unSubnetId | No | String | subnetId is invalid under basic network; Under VPC, the value is subject to the unSubnetId returned by the API [Query Subnet List](https://cloud.tencent.com/document/product/215/1371), such as subnet-3lzrkspo |
| projectId | No | UInt | Project ID. The value is subject to the projectId returned via User Account > User Account-related APIs > [Query Project List](https://cloud.tencent.com/doc/api/403/4400) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array | Returned array of orders |

Array data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.dealId | String | Order ID. You can use [DescribeRedisDealDetail](https://cloud.tencent.com/doc/api/260/5329) to query order details |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11052 | UserNotInWhiteList |The user is not in the whitelist |
| 10000 | NoRedisService | The Redis service is not available in the requested zone |
| 11062 | NoTypeIdRedisService | The Redis service of the requested type is not available in the requested zone |
| 11053 | InvalidInstanceTypeId | The type of the instance to purchase is incorrect (TypeId 1: Cluster; 2: Master-Slave (the former Standalone version) |
| 10703 | InvalidMemSize | The requested capacity is not included in the supported specifications (memSize (in MB) should be an integral multiple of 1024) |
| 11063 | MemSizeNotInRange | The requested capacity is not within the range of supported capacities (please use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the capacity) |
| 11065 | PeriodExceedMaxLimit | The purchased usage period exceeds the maximum usage period |
| 11066 | PeriodLessThanMinLimit |The purchased usage period is less than the minimum usage period |
| 11064 | GoodsNumNotInRange | The number of instances purchased at a time exceeds the maximum number of instances allowed to be purchased (please use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the number of instances allowed to be purchased) |
| 11067 | OnlyVPCOnSpecZoneId | Only the Redis service under VPC is available in the requested zone |
| 11054 | InvalidSubnetId | ID of the subnet under the VPC does not exist |
| 10501 | PasswordEmpty | Password is left empty |
| 11058 | PasswordRuleError | Incorrect password rule. The password must be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers and special characters (!, @, #, %, ^, *, ()) |
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient account balance. Please top it up. |

## 5. Example
Input
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=CreateRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&zoneId=100002
&typeId=1
&memSize=1024
&goodsNum=1
&period=2
&password=49A2d!e@f12e
</pre>
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"432583"
	}
}
```
