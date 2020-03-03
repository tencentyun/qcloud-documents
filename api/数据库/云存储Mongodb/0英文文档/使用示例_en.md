In order to help you get started with Tencent Cloud MongoDB APIs quickly, we provide an example on how to use these APIs.

This example will show you how to create an instance: First, you need to query the supported specification of the instance; then query the fee for creating the instance, then create the instance using the API "Create Instance", and finally query the instance creation progress using the API "Query Oder Details".

## 1.Querying Supported Instance Specifications
Before creating an instance, you first need to query the supported specification of the instance using the API [Query Supported Instance Specifications](/document/product/240/8318).

The input parameters for the API [Query Supported Instance Specifications (supporting custom availability zones and configurations) are as follows: 

| Parameter Name | Required | Type | Description | Value |
|---------|---------|---------|---------|---------|
| zoneIds.n | No | String | An array of availability zone IDs, with array subscript starting from 0. If this parameter is left empty, the product information of all the availability zones will be returned | 100002 |

Availability zones are defined as follows:

| Availability Zone | zoneId |
|:---------|---------|
| Guangzhou Zone 1 | 100001 |
| Guangzhou Zone 2 | 100002 |
| Guangzhou Zone 3 | 100003 |
| Shanghai Zone 1 | 200001 |
| Hong Kong Zone 1 | 300001 |
| Toronto Zone 1 | 400001 |
| Beijing Zone 1 | 800001 |

Returned values of API [Query Supported Instance Specifications (supporting custom availability zones and configurations) are the configuration information of creatable instances under each availability zone. Take the configuration of instance for Guangzhou Zone 2 in the returned values as an example, the fields are defined as below:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| region | String | Region ID. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976'>Common Request Parameters</a> | 
| isSupportVpc | Bool | Whether VPC is supported. Values: True and False | 
| types | Object | Content of supported instance specification |

Parameter types represents the supported instance specification content, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| typeId | String | Name of instance type |  GIO: High IO; TGIO: High IO (10 GB) |
| replicationNodeNum | Array | Number of nodes of replica set. Only 2 and 3 are supported currently | 
| memory | Int | Instance memory size. Each memory value corresponds to a selectable disk capacity range (in MB) |
| volumeMax | Int | The maximum value of the selectable capacity range of the instance hard disk (in GB) when the memory size is specified |
| volumeMin | Int | The minimum value of the selectable capacity range of the instance hard disk (in GB) when the memory size is specified |
| volumeStep | Int | Increment of hard disk capacity of the instance (in GB) after memory size is specified. For the creation of an instance, value for volume (capacity of hard disk) is: volume= volumeMin + volumeStep * n; (volumeMin <= volume <= volumeMax) |
| version | Array | Supported database version number, for example: MONGO_3_MMAP, MONGO_3_WT |

By combining common request parameters and API request parameters, you can get the final request as follows:
		
		https://mongodb.api.qcloud.com/v2/index.php?
		Action=DescribeMongoDBProduct
		&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
		&Signature=eSCz5paiDrXsdifc0Eq0GEihzsI%3D
		&Nonce=23284
		&Timestamp=1468329994
		&Region=gz
		&zoneIds.0=100002

The returned results of the above request are as follows:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "timeSpan": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            24,
            36
        ],
        "timeUnit": "m",
        "goodsDescription": {
            "100002": {
                "region": "gz",
                "isSupportVpc": true,
                "types": [
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 2048,
                        "volumeMax": 250,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 4096,
                        "volumeMax": 250,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 6144,
                        "volumeMax": 250,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 8192,
                        "volumeMax": 500,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 12288,
                        "volumeMax": 500,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 16384,
                        "volumeMax": 500,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 24576,
                        "volumeMax": 500,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 32768,
                        "volumeMax": 500,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 49152,
                        "volumeMax": 750,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 61440,
                        "volumeMax": 1000,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "GIO",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 65536,
                        "volumeMax": 1000,
                        "volumeMin": 25,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 4096,
                        "volumeMax": 300,
                        "volumeMin": 50,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 8192,
                        "volumeMax": 300,
                        "volumeMin": 100,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 16384,
                        "volumeMax": 600,
                        "volumeMin": 200,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 32768,
                        "volumeMax": 1200,
                        "volumeMin": 400,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 65536,
                        "volumeMax": 4000,
                        "volumeMin": 750,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 131072,
                        "volumeMax": 6000,
                        "volumeMin": 1500,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 245760,
                        "volumeMax": 6000,
                        "volumeMin": 1500,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    },
                    {
                        "typeId": "CY",
                        "replicationNodeNum": [
                            2,
                            3
                        ],
                        "memory": 524288,
                        "volumeMax": 6000,
                        "volumeMin": 4000,
                        "volumeStep": 5,
                        "version": [
                            "MONGO_3_MMAP",
                            "MONGO_3_WT"
                        ]
                    }
                ]
            }
        }
    }
}

```

## 2.Querying the Price of an Instance (Annual or Monthly Plan)
Creating a replica set instance will deduct involved fee from the account balance. You can use API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) to query the involved fee.  Let's suppose that we purchase a high IO instance from Guangzhou Zone 2, then the input parameters for querying the price are as follows: 

| Parameter Name | Required | Type | Description | Value |
|:---------|---------|---------|---------|---------|
| operation | Yes | String | newmongodb indicating the purchase of an instance should be input | newmongodb |
| zoneId | Yes | Int | Availability zone ID. You can use API [Query Supported Instance Specifications](/document/product/240/8318) to obtain the supported availability zones | 100002 |
| typeId | Yes | String | Name of instance type.  GIO: High IO; TGIO: High IO (10 GB) | GIO |
| memory | Yes | Int | Memory size of instance. Each memory value corresponds to a selectable disk capacity range (in MB) | 8192 |
| diskSize | Yes | Int | Disk capacity of instance (in GB) | 245 |
| secondaryNum | Yes | Int | Number of slave nodes of replica set instance. Only 1 and 2 are supported currently | 2 |
| version | Yes | Int | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |MONGO_3_MMAP |
| goodsNum | Yes | Int | Number of instances purchased at a time | 1 |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] | 1 |

By combining common request parameters and API request parameters, you can get the final request as follows:
	
	https://mongodb.api.qcloud.com/v2/index.php?
	Action=InquiryMongoDBReplSetPrice
	&Timestamp=1468328627
	&Nonce=51897
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=u34AneL09yCx50BwrUZtibiHxNw%3D
	&Region=gz
	&operation=newmongodb
	&zoneId=100002
	&typeId=GIO
	&memory=8192
	&diskSize=245
	&secondaryNum=2
	&version=MONGO_3_MMAP
	&goodsNum=1
	&period=1

According to the returned values, the total price for the instance with the above specification is 1888 CNY.
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

## 3.Creating a Replica Set Instance
Next, we will call the API [Create Instance (Annual or Monthly Plan](/document/product/240/8308) based on the above specification. The input parameters are as follows: 

| Parameter Name | Required | Type | Description | Value |
|:---------|---------|---------|---------|---------|
| zoneId | Yes | Int | Availability zone ID. You can use API [Query Supported Instance Specifications](/document/product/240/8318) to obtain the supported availability zones | 100002 |
| typeId | Yes | String | Name of instance type.  GIO: High IO; TGIO: High IO (10 GB) | GIO |
| memory | Yes | Int | Memory size of instance. Each memory value corresponds to a selectable disk capacity range (in MB) | 4096 |
| diskSize | Yes | Int | Disk capacity of instance (in GB) | 30 |
| secondaryNum | Yes | Int | Number of slave nodes of replica set. Only 1 and 2 are supported currently | 2 |
| version | Yes | Int | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT | MONGO_3_MMAP |
| goodsNum | Yes | Int | Number of instances purchased at a time | 1 |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] | 1 |
| password | Yes | String | Password for the instance. Rule: It should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, %, ^, ()) | 49A2d!e@f12e |
| vpcId | No | Int | VPC ID. In case of basic network, vpcId=0. Under VPC, the value is subject to the vpcid returned by the API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372) | 0 |
| subnetId | No | Int | subnetId is invalid under basic network; Under VPC, the value is subject to the subnetid returned by the API [Query VPC List](https://cloud.tencent.com/doc/api/245/1372) | 0 |
| projectId | No | Int | Project ID. The value is subject to the projectId returned via User Account > User Account-related APIs > [Query Project List](https://cloud.tencent.com/doc/api/403/4400) | 0 |

By combining common request parameters and API request parameters, you can get the final request as follows:
	
	https://mongodb.api.qcloud.com/v2/index.php?
	Action=CreateMongoDBReplSet
	&Timestamp=1468328920
	&Nonce=27412
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=4Dvpkk1bJov%2FUd%2FElWjAHfJaoD8%3D
	&zoneId=100002
	&typeId=GIO
	&memory=4096
	&diskSize=30
	&secondaryNum=2
	&version=MONGO_3_MMAP
	&goodsNum=1
	&period=1
	&password=49A2d!e@f12e

According to the returned values, the order ID for the purchase of the instance with the above specification is 3373037. You can query the details of this order through API [Query Order Details](/document/product/240/8313)

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

## 4. Querying Order Details
After creating the instance, you can use the API [Query Order Details](/document/product/240/8313) to query the order details based on the returned value of dealId.

| Parameter Name | Required | Type | Description | Value |
|---------|---------|---------|---------|
| dealIds.n | Yes | String | An array of order IDs, with array subscript starting from 0 | 3373037 |

By combining common request parameters and API request parameters, you can get the final request as follows:

	https://mongodb.api.qcloud.com/v2/index.php?
	Action=DescribeMongodbDealDetail
	&Timestamp=1468329117
	&Nonce=40727
	&SecretId=AKIDVxZ0PsvtPCgNEtsO0pSFwqkeTMFCu7z1
	&Signature=Y9rMVWyvjoijSl6zJxMW822edGk%3D
	&dealIds.0=3373037

The output is as follows: 
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "details": [
        {
            "dealId": "3373037",
            "dealName": "20170206121420",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3374998458",
            "creatTime": "2017-02-06 14:07:46",
            "overdueTime": "2017-02-21 14:07:46",
            "endTime": "2017-02-06 14:11:54",
            "status": 4,
            "price": 72200,
            "goodsDetail": {
                "memSize": 4096,
                "disksize": 30,
                "typeId": "GIO",
                "clusterType": "ReplSet",
                "secondaryNum": 2,
                "zoneId": 100002,
                "mongoVersion": "MONGO_3_MMAP",
                "timeSpan": 1,
                "timeUnit": "m",
                "SerialIds": [
                    "cmgo-6ozqe0uh"
                ]
            }
        }
    ]
}

```

The returned value "details" of API[Query Order Details] indicates the array of order details, with fields defined as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| details.dealId | String | Short order ID. Use this ID when calling the cloud API |
| details.dealName | String | Long order ID. Use this ID when reporting the order-related problems to customer service |
| details.zoneId | Int | Availability zone ID |
| details.goodsNum | Int | Number of instances associated with the order |
| details.creater | String | UIN of creator of order |
| details.creatTime | String | Creation time of order |
| details.overdueTime | String | Expiration time of order |
| details.endTime | String | Completion time of order |
| details.status | Int | Order status<br>1: Unpaid<br>2: Paid, Undelivered<br>3: Delivering<br>4: Delivery succeeded<br>5: Delivery failed<br>6: Refunded<br>7: Order closed<br>8: Order expired<br>9: Order invalidated<br>10: Product invalidated<br>11: Payment by agent rejected<br>12: Payment is in progress |
| details.price | Int | Actual total price of order (in 0.01 CNY) |
| details.goodsDetail | Object | Details of the commodity associated with the order |

**goodsDetail returned for the creation of an instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| memSize| int | Memory size of instance (in MB) |
| disksize | int | Disk capacity of instance (in GB) |
| typeId | String | Name of instance type |  GIO: High IO; TGIO: High IO (10 GB) |
| clusterType | Array | Instance cluster type. Only replica set is available currently |
| secondaryNum| Array | Number of slave nodes of replica set. Only 1 and 2 are supported currently |
| zoneId | Array | Availability zone ID |
| mongoVersion | Array | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |
| timeSpan | Array | Validity period of instance, with the unit being subject to the returned value of timeUnit |
| timeUnit | Array | Unit of validity period of instance (m: month; d: day) |
| SerialIds | Array | An array of instance IDs |

**goodsDetail returned for the renewal of instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| curDeadline | String | Expiration time of instance before renewal |
| timeSpan | int | Renewed period, with the unit being subject to the returned value of timeUnit |
| timeUnit | String | Unit of renewed period (m: month; d: day) |
| SerialIds | Array | An array of instance IDs |

**goodsDetail returned for the upgrade of instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| curDeadline | String | Expiration time of instance |
| newMemsize | int | Memory size of upgraded instance (in MB) |
| newDisksize | int | Disk capacity of upgraded instance (in GB) |
| oldMemsize | int | Memory size of instance before upgrade (in MB)|
| oldDisksize | int | Disk capacity of instance before upgrade (in GB)|
| SerialIds | Array | An array of instance IDs |

