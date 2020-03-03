## 1. API Description
This API (InquiryMongoDB) is used to obtain the prices of replica set instances (annual or monthly plan). Queries of the prices for purchase, renewal and upgrade of instances are supported. |
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryMongoDB.

The input parameters vary with different products, as shown below:

#### 2.1 Querying the Price for the Purchase of an Instance

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| operation | Yes | String | newmongodb indicating the purchase of an instance should be input |
| zoneId | Yes | Int | Availability zone ID. You can use API [Query Supported Instance Specifications](/document/product/240/8318) to obtain the supported availability zones |
| typeId | Yes | String | Name of instance type GIO: High IO; TGIO: High IO (10 GB) |
| memory | Yes | Int | Memory size of instance. Each memory value corresponds to a selectable disk capacity range (in MB) |
| diskSize | Yes | Int | Disk capacity of instance (in GB) |
| secondaryNum | Yes | Int | Number of slave nodes of replica set instance. Only 1 and 2 are supported currently |
| version | Yes | Int | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |
| goodsNum | Yes | Int | Number of instances purchased at a time |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |

#### 2.2 Querying the Price for the Renewal of an Instance

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| operation | Yes | String | renewmongodb indicating the renewal of an instance should be input |
| instanceId | Yes | String | ID of instance to work with. This can be obtained from instanceId in the returned values of API [DescribeMongoDBInstances](/document/product/240/8312). |
| period | Yes | Int | Renewed usage period (in month), with the range of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |

#### 2.3 Querying the Price for the Upgrade of an Instance

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| operation | Yes | String | upgrademongodb indicating the upgrade of an instance should be input |
| instanceId | Yes | String | ID of instance to work with. This can be obtained from instanceId in the returned values of API [DescribeMongoDBInstances](/document/product/240/8312).  |
| memory | Yes | Int | Memory size of upgraded instance. Each memory value corresponds to a selectable disk capacity range (in MB) |
| diskSize | Yes | Int | Disk capacity of upgraded instance (in GB) |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Instance price content |

Parameter data indicates the instance price content, and is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.price | Int | Price of instance (in 0.01 CNY) | 

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
| 11056 | InstanceNotExists | Instance does not exist |
| 11051 | InstanceDeleted | The instance has been reclaimed upon expiration |
| 11068 | UpgradeNotAllowedOnZoneId | Upgrade of instances is not allowed for this zone |
| 11069 | DiskSizeLessThanRealSize | The requested disk capacity is less than the actual value |
| 11069 |DiskSizeLessThanRealSize| The requested memory size is less than the actual value |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=InquiryMongoDB
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&operation=newmongodb
&zoneId=100002
&typeId=GIO
&memory=8192
&diskSize=245
&secondaryNum=2
&version=MONGO_3_MMAP
&goodsNum=1
&period=1
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "price": 188800
    }
}
```
