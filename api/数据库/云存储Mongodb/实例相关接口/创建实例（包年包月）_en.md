## 1. API Description
This API (CreateMongoDB) is used to create a replica set instance (annual or monthly plan).
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>

1. Please first use API [Query Supported Instance Specifications (supporting custom availability zones and configurations)](/document/product/240/8318) to query the supported instance specifications, and then use API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) to query the price of creatable instance;
2. Supported instance types: GIO: High IO; TGIO: High IO (10 GB);
3. Supported cloud database versions: MONGO_3_MMAP, MONGO_3_WT;
4. Value range of validity period of instance in a single creation: [1,2,3,4,5,6,7,8,9,10,11,12,24,36] (in month).

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is CreateMongoDB.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| zoneId | Yes | Int | Availability zone ID. You can use API [Query Supported Instance Specifications](/document/product/240/8318) to obtain the supported availability zones |
| typeId | Yes | String | Name of instance type.  GIO: High IO; TGIO: High IO (10 GB) |
| memory | Yes | Int | Memory size of instance. Each memory value corresponds to a selectable disk capacity range (in MB) |
| diskSize | Yes | Int | Disk capacity of instance (in GB) |
| secondaryNum | Yes | Int | Number of slave nodes of replica set instance. Only 1 and 2 are supported currently |
| version | Yes | Int | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |
| goodsNum | Yes | Int | Number of instances purchased at a time |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |
| password | Yes | String | Password for the instance. Rule: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()) |
| unVpcId | No | String | VPC ID. If it is left empty, the default is basic network. This value is subject to the unVpcId returned by API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372), such as: vpc-kd7d06of |
| unSubnetId | No | String | subnetId is invalid under basic network; Under VPC, the value is subject to the unSubnetId returned by the API [Query Subnet List](https://cloud.tencent.com/document/product/215/1371), such as subnet-3lzrkspo |
| projectId | No | Int | Project ID. The value is subject to the projectId returned via User Account > User Account-related APIs > [Query Project List](https://cloud.tencent.com/doc/api/403/4400) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes </a>on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Returned order ID |

Parameter data indicates the order ID, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.dealId | String | Order ID. You can use API [DescribeMongodbDealDetail](/document/product/240/8313) to query order details |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter | Incorrect business parameter |
| 11060 | ServiceUnavailable | The service is unavailable in the requested zone currently |
| 11071 | UserNotInWhiteList |The user is not in the whitelist |
| 11061 | TypeIdIllegal | Invalid typeId |
| 11062 | MemSizeExceedMaxLimit | The requested memory size exceeds the upper limit |
| 11063 | MemSizeIllegal | The requested memory size is not an integral multiple of 1024 |
| 11064 | MemSizeNotInRange | The requested memory size is not in the supported range |
| 11065 | RequestSizeIllegal | The requested memory size or disk capacity is invalid. The memory size must be an integral multiple of 1024, and the disk capacity must be an integer |
| 11066 | DiskSizeNotInRange | The requested disk capacity is not in the supported range |
| 11067 | PeriodNotInRange | The requested period is not in the supported range. The value range is [1,2,3,4,5,6,7,8,9,10,11,12,24,36] (in month) |
| 11072 | SecondaryNumNotInRange | The number of slave nodes of replica set instance is not in the supported range. The value range is [1,2] |
| 11059 | PasswordRuleError | Incorrect password rule. The password must be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers and special characters (!, @, #, %, ^, *, ()) |
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient account balance. Please top it up |
| 11075 | UnVpcIdNotExists | unVpcId does not exist |
| 11076 | UnSubnetIdNotExists | unSubnetId does not exist |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=CreateMongoDB
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&zoneId=100002
&typeId=GIO
&memory=4096
&diskSize=30
&secondaryNum=2
&version=MONGO_3_MMAP
&goodsNum=1
&period=1
&password=49A2d!e@f12e
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "dealId": "3373037"
    }
}

```

