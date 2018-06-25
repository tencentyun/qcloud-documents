## 1. API Description
This API (DescribeRedisProduct) is used to query supported specifications.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

This API can be used to query the supported specifications for CRS instances under specified availability zone and instance type. Users who are not in the purchaser whitelist cannot query the details of supported specifications under this availability zone and instance type. You can apply for the purchase of the whitelist of a region by submitting a [Ticket](https://console.cloud.tencent.com/workorder/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS).

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/239/7200' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeRedisProduct.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneIds.n | No | String | An array of availability zone IDs, with the array subscript starting from 0. If this parameter is not specified, the product information of all the availability zones will be returned. The available values are subject to the returned values of API [Query Supported Availability Zones](http://cloud.tencent.com/doc/api/260/4951) |
| typeId | No | UInt | Instance type: 1 - Cluster, 2 - Standalone, 0 - Both |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array | Returned instance data array |

**Array data is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| zoneId | Array | ID of availability zone | 
| name | String | Name of availability zone |
| data.types | Array | Array of instance types | 

**Array data.types is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.types.typeId | UInt | Array of instance type IDs | 

**Array data.types.typeId is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.types.typeId.type | UInt | Instance type: 1 - Cluster; 2 - Standalone | 
| data.types.typeId.typeName | String | Name of instance type | 
| data.types.typeId.minMemSize | UInt | Minimum capacity of an instance (in MB) | 
| data.types.typeId.maxMemSize | UInt | Maximum capacity of an instance (in MB) | 
| data.types.typeId.minBuyNum | UInt | Minimum number of instances allowed to be purchased at a time | 
| data.types.typeId.maxBuyNum | UInt | Maximum number of instances allowed to be purchased at a time |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 11052 | UserNotInWhiteList |The user is not in the whitelist |

## 5. Example
Input
```
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedisProduct
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&zoneIds.0=100002
&typeId=1
```
Output
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
    "data": [
        {
            "zoneId": 100002,
            "name": "Guangzhou Zone 2",
            "types": {
                "1": {
                    "type": 1,
                    "typeName": "Cluster",
                    "minMemSize": 1024,
                    "maxMemSize": 204800,
                    "minBuyNum": 1,
                    "maxBuyNum": 10
                }
            }
        }
    ]
}
```
