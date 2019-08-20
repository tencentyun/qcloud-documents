## 1. API Description
This API (DescribeCdbProductListNew) is used to query the specifications of creatable cloud database master instances, read-only instances and disaster recovery instances. It returns the restrictions about purchase period and purchase quantity in a single purchase for creatable instances, and, furthermore, returns database version number, memory size, and disk range of creatable instances according to types of availability zones. When the input parameter is empty, it returns the specification information of creatable master instances; when cdbInstanceId is passed and instanceRole is ro, it returns the specification information of creatable read-only instances for this master instance; when cdbInstanceId is passed and instanceRole is dr, it returns the specification information of creatable disaster recovery instances for this master instance.
You can also use API [Query Prices (Annual or Monthly Plan)](/doc/api/253/1332) or API [Query Prices (Pay by Usage)](/doc/api/253/5176) to query the prices of creatable instances, and use API [Create Instance (Annual or Monthly Plan)](/doc/api/253/1334) or [Create Instance (Pay by Usage)](/doc/api/253/5175) to create a new instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeCdbProductListNew.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | No | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| instanceRole | No | String | Instance type, default is master. Supported values​include: master - indicates master instance, dr - indicates disaster recovery instance, ro - indicates read-only instance |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| configs | Object | Configuration information of supported instance specification |
Parameter configs indicates the configuration information of supported instance specification, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| timeSpan | Array | Available purchase period for the current user, in the current region. Unit: month |
| minGoodsNumPerDeal | Int |  Minimum number of instances allowed to be purchased at a time
| maxGoodsNumPerDeal | Int | Maximum number of instances allowed to be purchased at a time |
| goodsDescription | Object | Specification information for the creatable instance |
Parameter goodsDescription indicates the configuration information of instance, and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| 100002/100003/... | Object | Availability zone ID |
100002 is the availability zone ID and its value indicates the information of supported instance under the availability zone. It is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| region | String | Region ID. For details, refer to [Common Request Parameters](/doc/api/229/6976) |
| isSupportVpc | Bool | Indicates whether VPC is supported. Values include: true, false |
| isSupportVpc | Bool | Indicates whether VPC is supported. Values include: true, false |
| types | Object | Contents of supported instance specifications |
types represents the contents of supported instance specifications, and it is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| typeName | String | Name of the instance type, for example: High IO version |
| memory | String | Instance memory size, each memory value corresponds to a selectable disk size range (unit: MB) |
| volumeMax | Int | Maximum selectable instance hard disk size after the memory is determined (unit: GB) |
| volumeMin | Int | Minimum selectable instance hard disk size after the memory is determined (unit: GB) |
| volumeStep | Int | Instance hard disk size increment after the memory is determined (unit: GB). When creating an instance, the value for volume is: volume= volumeMin + volumeStep * n; while volumeMin <= volume <= volumeMax  |
| qps | Int | Supported qps (queries per second) after the memory is determined. Unit: times/second |
| mysqlversion | Array | Supported MySQL versions, possible return values include 5.5 and 5.6 |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError |CDB error |
| 9649 | OperationDenied | Not allowed to create disaster recovery instance |
| 9650 | OperationDenied | Not allowed to create read-only instance |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbProductListNew
&<<a href="/document/product/236/6921">Common request parameters</a>>
</pre>

Output
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
                "region":"gz",
                "isSupportVpc":true,
                "types":[
                    {
                        "typeName":"High IO",
                        "memory":"360",
                        "volumeMax":"50",
                        "volumeMin":"10",
                        "volumeStep":"5",
                        "qps":"120",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"1000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"1000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"2000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"2400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
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
                    },
                    {
                        "typeName":"High IO",
                        "memory":"12000",
                        "volumeMax":"250",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"15000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    }
                ]
            },
            "100003":{
                "region":"gz",
                "isSupportVpc":true,
                "types":[
                    {
                        "typeName":"High IO",
                        "memory":"1000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"1000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"2000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"2400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"4000",
                        "volumeMax":"3000",
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
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"7200",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"16000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"18000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"32000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"25000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"64000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"37689",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"96000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"40919",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"128000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"61378",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"244000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"122755",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"High IO",
                        "memory":"488000",
                        "volumeMax":"6000",
                        "volumeMin":"6000",
                        "volumeStep":"5",
                        "qps":"245509",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    }
                ]
            }
        }
    }
}
```


