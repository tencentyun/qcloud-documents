In order to help you get started with Tencent Cloud Redis (CRS) APIs quickly, we provide an example on how to use these APIs.

This example will show you how to create a CRS instance: First, you need to query the supported specification of the instance; then query the fee for creating the instance, then create the instance using the API "Create Instance", and finally query the instance creation progress using the API "Query Oder Details".

## 1. Query Supported Specifications
Before creating an instance, we first need to query the availability zones where the instance is available. You can use the API [Query Supported Availability Zones](http://cloud.tencent.com/doc/api/260/4951) for the query, or use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the instance creation.

Here, we use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the supported specifications for all availability zones by leaving the input parameter empty.

By combining common request parameters and API request parameters, you can get the final request as follows:
		
		https://redis.api.qcloud.com/v2/index.php?
		Action=DescribeRedisProduct
		&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
		&Signature=eSCz5paiDrXsdifc0Eq0GEihzsI%3D
		&Nonce=23284
		&Timestamp=1468329994
		&Region=gz

The returned results of the above request are as follows:
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
                },
                "2": {
                    "type": 2,
                    "typeName": "Standalone",
                    "minMemSize": 1024,
                    "maxMemSize": 512000,
                    "minBuyNum": 1,
                    "maxBuyNum": 10
                }
            }
        },
        {
            "zoneId": 200001,
            "name": "Shanghai Zone 1",
            "types": {
                "1": {
                    "type": 1,
                    "typeName": "Cluster",
                    "minMemSize": 1024,
                    "maxMemSize": 204800,
                    "minBuyNum": 1,
                    "maxBuyNum": 10
                },
				"2": {
                    "type": 2,
                    "typeName": "Standalone",
                    "minMemSize": 1024,
                    "maxMemSize": 204800,
                    "minBuyNum": 1,
                    "maxBuyNum": 10
                }
            }
        },
        {
            "zoneId": 300001,
            "name": "Hong Kong Zone 1",
            "types": {
                "2": {
                    "type": 2,
                    "typeName": "Standalone",
                    "minMemSize": 1024,
                    "maxMemSize": 40960,
                    "minBuyNum": 1,
                    "maxBuyNum": 10
                }
            }
        },
        {
            "zoneId": 400001,
            "name": "North America Zone 1",
            "types": {
                "2": {
                    "type": 2,
                    "typeName": "Standalone",
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
The returned values are the supported specifications for various availability zones, with each element referring to the supported specification for an availability zone. Take the specification of cluster instance for Guangzhou Zone 2 in the returned values as an example, the fields are defined as below:

| Parameter Name | Description  | Value |
|---------|---------|---------|
| zoneId |  Availability zone ID | 100002 |
| name | Availability zone name | Guangzhou Zone 2 |
| types.1 | Object of supported specification | Array  |
| types.1. type | Instance type, 1 - Cluster, 2 - Standalone |  1 |
| types.1. typeName | Type name |  Cluster |
| types.1. mimMemSize | Minimum capacity of a cluster instance allowed to be purchased (in MB)   |  1024 |
| types.1. maxMemSize | Maximum capacity of a cluster instance allowed to be purchased (in MB)   |  204800 |
| types.1. minBuyNum | Minimum number of cluster instances allowed to be purchased | 1 |
| types.1. minBuyNum | Maximum number of cluster instances allowed to be purchased |  10 |



## 2. Query the Price for Creating an Instance
A fee for the creation of an instance will be deducted from the account balance. You can use the API [Query Instance Price](https://cloud.tencent.com/doc/api/260/5324) to query the fee.  Let's suppose that we purchase a cluster instance from Guangzhou Zone 2, then the input parameters for querying the price are as follows: 

| Parameter Name | Description | Value |
|---------|---------|---------|
| zoneId | The availability zone to which the instance belongs |  100002 (Guangzhou Zone 2) |
| typeId |  1: Cluster; 2: Standalone | 1 (Cluster) |
| memSize | The capacity of the purchased instance (in MB); the value range is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) | 1024 |
| goodsNum | The number of the purchased instances. The value range is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) | 1 |
| period | The purchased usage period (in month); value range: [1, 36] | 2 |

By combining common request parameters and API request parameters, you can get the final request as follows:
	
	https://redis.api.qcloud.com/v2/index.php?
	Action=InquiryRedisPrice
	&Timestamp=1468328627
	&Nonce=51897
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=u34AneL09yCx50BwrUZtibiHxNw%3D
	&Region=gz
	&zoneId=100002
	&typeId=1
	&memSize=1024
	&goodsNum=1
	&period=2

According to the returned values, the total price for the instance with the above specification is 160 CNY.
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
    "data":{
        "price":16000
    }
}
```

## 3. Create an Instance
Next, we will call the API [Create Instance](http://cloud.tencent.com/doc/api/260/5325) based on the above specification. The input parameters are as follows: 

| Parameter Name | Description | Value |
|---------|---------|---------|
| zoneId | The availability zone to which the instance belongs |  100002 (Guangzhou Zone 2) |
| typeId |  Instance type. 1: Cluster; 2: Standalone | 1 (Cluster) |
| vpcId | VPC ID. Set to 0 if it is basic network | 0 (basic network) |
| memSize | The capacity of the purchased instance (in MB); the value range is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) | 1024 |
| goodsNum | The number of the purchased instances. The value range is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) | 1 |
| period | The purchased usage period (in month); value range: [1, 36] | 2 |
| password | Password for the instance | 49A2d!e@f12e |

By combining common request parameters and API request parameters, you can get the final request as follows:
	
	https://redis.api.qcloud.com/v2/index.php?
	Action=CreateRedis
	&Timestamp=1468328920
	&Nonce=27412
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=4Dvpkk1bJov%2FUd%2FElWjAHfJaoD8%3D
	&zoneId=100002
	&typeId=1
	&vpcId=0
	&memSize=1024
	&goodsNum=1
	&period=2
	&password=49A2d!e@f12e

Returned result:
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data": {
		"dealId":"432583"
	}
}
```

## 4. Query Order Details
After creating the instance, you can use the API [Query Order Details](http://cloud.tencent.com/doc/api/260/5329) to query the order details.

| Parameter Name | Description | Value |
|---------|---------|---------|
| dealIds.n |  List of order IDs | 432583 |

By combining common request parameters and API request parameters, you can get the final request as follows:

	https://redis.api.qcloud.com/v2/index.php?
	Action=DescribeRedisDealDetail
	&Timestamp=1468329117
	&Nonce=40727
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=Y9rMVWyvjoijSl6zJxMW822edGk%3D
	&dealIds.0=432583

The output is as follows: 
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
    "dealDetails": [
        {
            "dealId": "432583",
			"dealName": "20160712110021",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-06 21:10:11",
            "overdueTime": "2016-07-16 21:10:11",
            "endTime": "2016-07-06 21:11:17",
            "status": 4,
            "description": "Delivery succeeded",
            "price": 16000,
            "goodsDetail": {
                "memSize": 1024,
                "timeSpan": 2,
                "timeUnit": "m",
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        }
    ]
}
```

Descriptions of returned fields:

| Parameter Name | Description | Value |
|---------|---------|---------|
| dealId | Order ID | 432583 |
| dealName | Order name |  20160712110021 |
| zoneId | The availability zone to which the instance belongs |  100002 (Guangzhou Zone 2) |
| goodsNum | Number of purchased instances |  1 |
| creater | Creator of order |  3227991405 |
| creatTime | Creation time of order |  2016-07-06 21:10:11 |
| overdueTime | Expiration time of order |  2016-07-21 17:24:37 |
| endTime| Completion time of order | 2016-07-06 21:11:17 |
| status | Order status | 4 |
| description | Description of order status |  "Delivery succeeded" |
| price | Order amount (in 0.01 CNY) |  16,000 |
| goodsDetail.memsize | Instance specification (in MB) |  1024 |
| goodsDetail.timeSpan | Purchased usage period |  2 |
| goodsDetail.timeUnit | Unit of usage period: m - Month, d - Day |  m (Month) |
| goodsDetail.redisIds | List of redisIds for the purchased CRS instances in the order | crs-ifmymj41 |




