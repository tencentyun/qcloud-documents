In order to help you get started with Cloud Database for MySQL APIs quickly, we provide an example on how to use these APIs.
To use Cloud Database for MySQL service, you need to query the supported instance specifications first, which defines the specifications and restrictions for the creatable instances, and then create instances based on the required specifications. Finally, you need to initialize the newly created instances. The procedure is as follows:
First, use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to view the supported instance specifications for various regions. Then use API [Create an Instance (Annual or Monthly Plan)](/doc/api/253/1334) or [Create an Instance (Pay by Usage)](/doc/api/253/5175) to create an instance. Finally, use API [Initialize an Instance](/doc/api/253/5335) to initialize the instance. When initialized successfully, the instance can be put into use.


## 1. Query Supported Specifications (supporting custom availability zones and configurations)
Before creating a cloud database instance, we need to check which instance specifications are supported for the selected region. Only <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a> are required for this API.

By inputting <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>, you can get the final request as follows:

```
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbProductListNew
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=12276
&Timestamp=1467277235
&Region=bj
```

This API will return the instance usage period allowed to be purchased (in month), the maximum number of instances allowed to be purchased at a time, as well as the specification information of each zone within the specified region, including whether VPC is supported, memory size, disk range, database engine version and number of visits per second (QPS). The returned results for the above request is as follows:

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "configs":{
        "timeSpan":[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "12",
            "24",
            "36"
        ],
        "minGoodsNumPerDeal":"1",
        "maxGoodsNumPerDeal":"10",
        "goodsDescription":{
            "100002":{
                "isSupportVpc":true,
                "types":[
                    {
                        "typeName":"High IO",
                        "memory":"4000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"4400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"8000",
                        "volumeMax":"250",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"7200",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    }
                    //Part of the results are omitted. Please refer to the actual response content...
                ]
            }
            //Part of the results are omitted. Please refer to the actual response content...
        }
    }
}
```

## 2. Create Instances
After acquiring the supported instance specifications, you can use API [Create Instances (Annual or Monthly Plan)](/doc/api/253/1334) or API [Create Instances (Pay by Usage)](/doc/api/253/5175) to create an instance.
In the following example, custom specifications are used, cdbType is set to CUSTOM, memory size is 1000MB and disk size is 25GB. MySQL version is 5.6, period is 1 month, and number of instances is 1. The relevant API request parameters are as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbType | Yes | String | Instance specification. Both fixed specification and custom specification are supported. CUSTOM means custom specification. You can use API [Query Supported Specifications](/doc/api/253/1333) to obtain the value range of fixed specification. <font style='color:red'> Fixed specification type will become unavailable in the future. It is recommended to use custom specifications. </font>|
| engineVersion | Yes | String | MySQL version. Values include: 5.5 and 5.6. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to obtain the supported instance version.
| period | Yes | Int | Validity period of instance (in months). The minimum and maximum values are 1 and 36 respectively. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to obtain the supported validity period of the instance. The returned field "timeSpan" indicates the period value |
| goodsNum | Yes | Int | Number of instances. Default is 1, minimum is 1, and maximum is 10. You can acquire the number of instances that can be created using API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) |
| vpcId | No | String | VPC ID. If this is left empty, the default is basic network. Please use API [Query VPC List](/doc/api/245/1372) |
| subnetId | No | String | ID of subnet in VPC. If vpcId is set, subnetId is required. Please use API [Query Subnet List](/doc/api/245/1371) |
| projectId | No | Int | Project ID. If this is left empty, default project is used. Please use API [Query Project List](/document/product/378/4400) to acquire project ID |
| memory | No | Int | Size of instance memory (unit: GB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire the supported memory specification |
| volume | No | Int | Size of instance disk (unit: GB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported disk range |
| zoneId | No | Int | Availability zone ID. By default, the system will automatically select an availability zone. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported availability zones) |

By combining <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a> and API request parameters, you can get the final request as follows:

```
https://cdb.api.qcloud.com/v2/index.php?Action=CreateCdb
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=25476
&Timestamp=1467277631
&Region=bj
&cdbType=CUSTOM
&memory=1000
&volume=25
&engineVersion=5.6
&period=1
&goodsNum=1

```

The results returned for the API "Create Instances" contain short order ID (dealIds), long order ID (dealNames) and instance ID. Parameter dealIds is used to call the cloud API, dealNames to report order-related problems to Tencent Cloud customer service, and instance ID to manage cloud database instance. You can use API [Query List of Instances](/doc/api/253/1266) to view the instance you just created.
The result of the above request is as follows:

```
{
    "code": 0,
    "message": "",
    "dealIds": [
        "2196009"
    ],
    "data": {
        "dealNames": [
            "20161024110051"
        ],
        "dealIds": [
            "457605"
        ],
        "cdbInstanceIds": {
            "20161024110051": [
                "cdb-259sstXX"
            ]
        }
    }
}
```


## 3. Initialize Instances
When an instance is created, you need to initialize it. After being initialized successfully, the instance can be put into use. When initializing the instance, you can set the character set, port, whether table name is case-sensitive) and the password of root account for the instance. The relevant API request parameters are as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |
| charset | Yes | String | Character set. Supported character sets: latin1, utf8, gbk and utf8mb4 |
| port | Yes | Int | Custom port. Value range: [1024-65535] |
| lowerCaseTableNames | Yes | Int | Whether the table name only be saved in lowercase. Possible returned values: 1 - Only saved in lowercase; 0 - Case-sensitive |
| password | Yes | String | Password of root account, which should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, $, %, ^, *, ()) |

By combining <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a> and API request parameters, you can get the final request as follows:

```
https://cdb.api.qcloud.com/v2/index.php?Action=CdbMysqlInit
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=25476
&Timestamp=1467277631
&Region=bj
&cdbInstanceId=cdb-c1nl9rpv
&charset=utf8
&port=3306
&password=cloud123456
&lowerCaseTableNames=0
```

Initializing instances is an asynchronous process. If the task is successfully initialized, an task ID will be returned. You can use API [Query Initialization Task Details](/doc/api/253/5334) to query the progress of the initialization task. The result of the above request is as follows:

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "jobId":"11"
}
```

















