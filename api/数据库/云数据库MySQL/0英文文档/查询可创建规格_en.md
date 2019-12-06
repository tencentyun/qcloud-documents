## 1. API Description
This API (DescribeCdbProductList) is used to query the supported CDB instance specifications, return the purchased usage period of creatable instances and maximum number of instances allowed to be purchased at a time, and return the specification information of creatable instances under various database version numbers by basic network or VPC.<font style="color:red">** This API does not support custom availability zones and configurations. It is recommended to use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to query the supported specifications of instances**</font>.
You can also use API [Query Prices (Annual or Monthly Plan)](/doc/api/253/1332) or API [Query Prices (Pay by Usage)](/doc/api/253/5176) to query the prices of creatable instances, and use API [Create Instances (Annual or Monthly Plan)](/doc/api/253/1334) or [Create Instances (Pay by Usage)](/doc/api/253/5175) to create a new instance.
Domain for API request:<font style="color:red">cdb.api.qcloud.com</font>

## 2. Input Parameters
This API has no request parameters, and only common request parameters are needed when it is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeCdbProductList.

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| configs | Object | Configuration information of supported instance specification |
Parameter configs indicates the configuration information of supported instance specification, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed |
| message | String | Error message |
| timeSpan | Array | The usage period allowed to be purchased by current user in the current region (in months) |
| minGoodsNumPerDeal | Int | Minimum number of instances allowed to be purchased at a time |
| maxGoodsNumPerDeal | Int | Maximum number of instances allowed to be purchased at a time |
| goodsDescription | Object | Specification information of creatable instance |
Parameter goodsDescription indicates the configuration information of instance, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| baseNet | Object | Basic network, i.e. the network type of creatable instances. Possible returned values include: baseNet and VPCNet |
| VPCNet | Object | Virtual Private Cloud (VPC), i.e. the network type of creatable instances. Possible returned values include: baseNet and VPCNet |
Parameter baseNet indicates basic network, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| MySQL5.5 | Object | Version number of database engine of creatable instances in basic network. Possible returned values include: MySQL5.5 and MySQL5.6 |
| MySQL5.6 | Object | Version number of database engine of creatable instances in basic network. Possible returned values include: MySQL5.5 and MySQL5.6 |
MySQL5.5 or MySQL5.6 indicates the database version number of creatable instances, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| 20 | Object | Specification information of instance. Each instance specification is represented by a number and includes its configurations |
| 20.cdbType | Int | Instance specification. It can be used to query prices and create instances. For custom specification, its field value is CUSTOM. Please use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to query the instance specifications supporting availability zone and customization |
| 20.typeName | String | Name of instance type, such as: High IO |
| 20.subTypeName | String | Extension name of instance type, such as: Micro |
| 20.volume | Int | Capacity of instance disk (in GB) |
| 20.memory | Int | Capacity of instance memory (in MB) |
| 20.visits | Int | Allowed number of visits per second (counts per second) |
| 20.binlogSize | Int | Size of binlog (in GB) |
| 20.suitinfo | String | Scenario description recommended for each specification |
| 20.typeOrder | Int | Field for sorting |
| 20.subTypeOrder | Int | Field for sorting |
Parameter VPCNet indicates VPC, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| MySQL5.5 | Object | Version number of database engine of creatable instances in VPC. Possible returned values include: MySQL5.5 and MySQL5.6 |
| MySQL5.6 | Object | Version number of database engine of creatable instances in VPC. Possible returned values include: MySQL5.5 and MySQL5.6 |
MySQL5.5 or MySQL5.6 indicates the database engine version number of creatable instances, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| 20 | Object | Specification information of instance. Each instance specification is represented by a number and includes its configurations |
| 20.cdbType | Int | Instance specification. It can be used to query prices and create instances. For custom specification, its field value is CUSTOM. Please use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to query the instance specifications supporting availability zone and customization |
| 20.typeName | String | Name of instance type, such as: High IO |
| 20.subTypeName | String | Extension name of instance type, such as: Micro |
| 20.volume | Int | Capacity of instance disk (in GB) |
| 20.memory | Int | Capacity of instance memory (in MB) |
| 20.visits | Int | Allowed number of visits per second (counts per second) |
| 20.binlogSize | Int | Size of binlog (in GB) |
| 20.suitinfo | String | Scenario description recommended for each specification |
| 20.typeOrder | Int | Field for sorting |
| 20.subTypeOrder | Int | Field for sorting |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error message | Error Description |
|---------|---------|---------|
| 9013 | InternalError | System internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbProductList
&<<a href="/document/product/236/6921">Common request parameters</a>>
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc":"Success",
    "configs": {
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
            12,
            24,
            36
        ],
        "minGoodsNumPerDeal": 1,
        "maxGoodsNumPerDeal": 10,
        "goodsDescription": {
            "baseNet": {
                "MySQL5.5": {
                    "20": {
                        "cdbType": 20,
                        "typeName": "High IO",
                        "subTypeName": "Micro",
                        "volume": 25,
                        "visits": 1000,
                        "binlogSize": 3,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 1,
                        "memory": 1000
                    },
                    "21": {
                        "cdbType": 21,
                        "typeName": "High IO",
                        "subTypeName": "Small",
                        "volume": 50,
                        "visits": 2400,
                        "binlogSize": 7,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 2,
                        "memory": 2000
                    },
                    "22": {
                        "cdbType": 22,
                        "typeName": "High IO",
                        "subTypeName": "C",
                        "volume": 100,
                        "visits": 4400,
                        "binlogSize": 15,
                        "suitinfo": "Medium-sized game applications with hundreds of thousands of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 3,
                        "memory": 4000
                    },
                    "23": {
                        "cdbType": 23,
                        "typeName": "High IO",
                        "subTypeName": "Medium",
                        "volume": 250,
                        "visits": 15000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 5,
                        "memory": 12000
                    },
                    "24": {
                        "cdbType": 24,
                        "typeName": "High IO",
                        "subTypeName": "Large",
                        "volume": 500,
                        "visits": 23000,
                        "binlogSize": 100,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 7,
                        "memory": 24000
                    },
                    "25": {
                        "cdbType": 25,
                        "typeName": "High IO",
                        "subTypeName": "Extra Large",
                        "volume": 1000,
                        "visits": 37000,
                        "binlogSize": 200,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 8,
                        "memory": 48000
                    },
                    "26": {
                        "cdbType": 26,
                        "typeName": "High IO",
                        "subTypeName": "A",
                        "volume": 400,
                        "visits": 18000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 6,
                        "memory": 16000
                    },
                    "27": {
                        "cdbType": 27,
                        "typeName": "High IO",
                        "subTypeName": "B",
                        "volume": 200,
                        "visits": 7200,
                        "binlogSize": 30,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 4,
                        "memory": 8000
                    }
                },
                "MySQL5.6": {
                    "20": {
                        "cdbType": 20,
                        "typeName": "High IO",
                        "subTypeName": "Micro",
                        "volume": 25,
                        "visits": 1000,
                        "binlogSize": 3,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 1,
                        "memory": 1000
                    },
                    "21": {
                        "cdbType": 21,
                        "typeName": "High IO",
                        "subTypeName": "Small",
                        "volume": 50,
                        "visits": 2400,
                        "binlogSize": 7,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 2,
                        "memory": 2000
                    },
                    "22": {
                        "cdbType": 22,
                        "typeName": "High IO",
                        "subTypeName": "C",
                        "volume": 100,
                        "visits": 4400,
                        "binlogSize": 15,
                        "suitinfo": "Medium-sized game applications with hundreds of thousands of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 3,
                        "memory": 4000
                    },
                    "23": {
                        "cdbType": 23,
                        "typeName": "High IO",
                        "subTypeName": "Medium",
                        "volume": 250,
                        "visits": 15000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 5,
                        "memory": 12000
                    },
                    "24": {
                        "cdbType": 24,
                        "typeName": "High IO",
                        "subTypeName": "Large",
                        "volume": 500,
                        "visits": 23000,
                        "binlogSize": 100,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 7,
                        "memory": 24000
                    },
                    "25": {
                        "cdbType": 25,
                        "typeName": "High IO",
                        "subTypeName": "Extra Large",
                        "volume": 1000,
                        "visits": 37000,
                        "binlogSize": 200,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 8,
                        "memory": 48000
                    },
                    "26": {
                        "cdbType": 26,
                        "typeName": "High IO",
                        "subTypeName": "A",
                        "volume": 400,
                        "visits": 18000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 6,
                        "memory": 16000
                    },
                    "27": {
                        "cdbType": 27,
                        "typeName": "High IO",
                        "subTypeName": "B",
                        "volume": 200,
                        "visits": 7200,
                        "binlogSize": 30,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 4,
                        "memory": 8000
                    }
                }
            },
            "VPCNet": {
                "MySQL5.5": {
                    "20": {
                        "cdbType": 20,
                        "typeName": "High IO",
                        "subTypeName": "Micro",
                        "volume": 25,
                        "visits": 1000,
                        "binlogSize": 3,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 1,
                        "memory": 1000
                    },
                    "21": {
                        "cdbType": 21,
                        "typeName": "High IO",
                        "subTypeName": "Small",
                        "volume": 50,
                        "visits": 2400,
                        "binlogSize": 7,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 2,
                        "memory": 2000
                    },
                    "22": {
                        "cdbType": 22,
                        "typeName": "High IO",
                        "subTypeName": "C",
                        "volume": 100,
                        "visits": 4400,
                        "binlogSize": 15,
                        "suitinfo": "Medium-sized game applications with hundreds of thousands of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 3,
                        "memory": 4000
                    },
                    "23": {
                        "cdbType": 23,
                        "typeName": "High IO",
                        "subTypeName": "Medium",
                        "volume": 250,
                        "visits": 15000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 5,
                        "memory": 12000
                    },
                    "24": {
                        "cdbType": 24,
                        "typeName": "High IO",
                        "subTypeName": "Large",
                        "volume": 500,
                        "visits": 23000,
                        "binlogSize": 100,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 7,
                        "memory": 24000
                    },
                    "25": {
                        "cdbType": 25,
                        "typeName": "High IO",
                        "subTypeName": "Extra Large",
                        "volume": 1000,
                        "visits": 37000,
                        "binlogSize": 200,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 8,
                        "memory": 48000
                    },
                    "26": {
                        "cdbType": 26,
                        "typeName": "High IO",
                        "subTypeName": "A",
                        "volume": 400,
                        "visits": 18000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 6,
                        "memory": 16000
                    },
                    "27": {
                        "cdbType": 27,
                        "typeName": "High IO",
                        "subTypeName": "B",
                        "volume": 200,
                        "visits": 7200,
                        "binlogSize": 30,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 4,
                        "memory": 8000
                    }
                },
                "MySQL5.6": {
                    "20": {
                        "cdbType": 20,
                        "typeName": "High IO",
                        "subTypeName": "Micro",
                        "volume": 25,
                        "visits": 1000,
                        "binlogSize": 3,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 1,
                        "memory": 1000
                    },
                    "21": {
                        "cdbType": 21,
                        "typeName": "High IO",
                        "subTypeName": "Small",
                        "volume": 50,
                        "visits": 2400,
                        "binlogSize": 7,
                        "suitinfo": "Small-sized game applications with tens of thousands of daily active users or tool applications with millions of users",
                        "typeOrder": 3,
                        "subTypeOrder": 2,
                        "memory": 2000
                    },
                    "22": {
                        "cdbType": 22,
                        "typeName": "High IO",
                        "subTypeName": "C",
                        "volume": 100,
                        "visits": 4400,
                        "binlogSize": 15,
                        "suitinfo": "Medium-sized game applications with hundreds of thousands of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 3,
                        "memory": 4000
                    },
                    "23": {
                        "cdbType": 23,
                        "typeName": "High IO",
                        "subTypeName": "Medium",
                        "volume": 250,
                        "visits": 15000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 5,
                        "memory": 12000
                    },
                    "24": {
                        "cdbType": 24,
                        "typeName": "High IO",
                        "subTypeName": "Large",
                        "volume": 500,
                        "visits": 23000,
                        "binlogSize": 100,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 7,
                        "memory": 24000
                    },
                    "25": {
                        "cdbType": 25,
                        "typeName": "High IO",
                        "subTypeName": "Extra Large",
                        "volume": 1000,
                        "visits": 37000,
                        "binlogSize": 200,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 8,
                        "memory": 48000
                    },
                    "26": {
                        "cdbType": 26,
                        "typeName": "High IO",
                        "subTypeName": "A",
                        "volume": 400,
                        "visits": 18000,
                        "binlogSize": 65,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 6,
                        "memory": 16000
                    },
                    "27": {
                        "cdbType": 27,
                        "typeName": "High IO",
                        "subTypeName": "B",
                        "volume": 200,
                        "visits": 7200,
                        "binlogSize": 30,
                        "suitinfo": "Large-sized game applications with millions of daily active users",
                        "typeOrder": 3,
                        "subTypeOrder": 4,
                        "memory": 8000
                    }
                }
            }
        }
    }
}
```

