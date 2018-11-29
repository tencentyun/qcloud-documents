## 1. API Description
This API (InquiryCdbPriceHour) is used to query the price (pay-by-usage) of a certain cloud database instance type (unit: yuan/hour). You can query instance price by passing instance type, purchase quantity, memory size, hard disk size and availability zone ID.
You can also create a new instance using [Create Instance (Pay-by-usage)](/doc/api/253/5175) API.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryCdbPriceHour.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbType | Yes | String | Instance specification. Both fixed specification and custom specification are supported. CUSTOM means custom specification. You can acquire values for fixed specifications using [Query Supported Specifications](/doc/api/253/1333) API. <font style='color:red'> Fixed specification type will become unavailable in the future. It is recommended to use custom specifications. </font>|
| goodsNum | Yes | Int | Number of instances. Default is 1, minimum is 1, and maximum is 10. You can acquire the number of instances that can be created using [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) API |
| memory | No | Int | Size of instance memory (unit: MB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire creatable memory specifications |
| volume | No | Int | Size of instance disk (unit: GB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported disk range |
| zoneId | No | Int | Availability zone ID. By default, the system will automatically select an availability zone. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported availability zones |
| instanceRole | No | String | Instance type, default is master. Supported values​include: master - indicates master instance, dr - indicates disaster recovery instance, ro - indicates read-only instance |
| protectMode | No | Int | Data copy method. Default is 0, supported values include: 0 - indicates asynchronous copy, 1 - indicates semi-synchronized copy, 2 - indicates strong synchronized copy. You can specify this parameter when querying master instances, while this parameter will be ignored when querying read-only instances or disaster recovery instances |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| price | Int | Instance price (unit: cent (RMB) |

## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9301 | InvalidParameter | Incorrect transaction parameter |


## 5. Example

Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=InquiryCdbPrice
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbType=CUSTOM
&memory=1000
&volume=25
&goodsNum=1
&zoneId=100003
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "price": 35
}
```

