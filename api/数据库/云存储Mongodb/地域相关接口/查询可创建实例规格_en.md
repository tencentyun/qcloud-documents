## 1. API Description
This API (DescribeMongoDBProduct) is used to query supported instance specifications. It can return the purchased usage period of creatable instances, and return the machine type, number of nodes of replica set, memory size, disk range and database version number of creatable instances by availability zone types.
You can also use API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) to query the prices of creatable instances, and use API [Create Instance (Annual or Monthly Plan)](/document/product/240/8308) to create a new instance.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>

This API can be used to query the supported specifications under specified availability zone. Users who are not in the purchaser whitelist cannot query the details of supported specifications under the availability zone. You can apply for the purchase of the whitelist of a region by submitting a [Ticket](https://console.cloud.tencent.com/workorder/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS).

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeMongoDBProduct.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneIds.n | No | String | An array of availability zone IDs, with array subscript starting from 0. If this parameter is left empty, the product information of all the availability zones will be returned |

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

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Configuration information of supported instance specification |

Parameter data indicates the configuration information of supported instance specification, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| timeSpan | Array | Purchasable usage period of instance | 
| timeUnit | String | Unit of purchasable usage period of instance (m: month; d: day) |
| goodsDescription | Object | Information of supported instance specification |

Parameter goodsDescription indicates the configuration information of instance, and is composed as follows: 

| Parameter Name | Type | Description |
|:---------|---------|---------|
| 100002/100003/... | Object | Availability Zone ID|

100002 is the availability zone ID and its value indicates the instance specification information supported under the availability zone. It is composed as follows: 

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

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter | Incorrect business parameter |
| 11060 | ServiceUnavailable| The service is unavailable in the requested region currently |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=DescribeMongoDBProduct
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&zoneIds.0=100002
&zoneIds.1=200001
</pre>
Output
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
                    }
                ]
            },
            "200001": {
                "region": "sh",
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
                    }
                ]
            }
        }
    }
}

```
