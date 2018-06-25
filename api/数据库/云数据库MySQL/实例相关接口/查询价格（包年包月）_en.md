## 1. API Description
This API (InquiryCdbPrice) is used to query the price (Annual and monthly plan) of a certain cloud database instance type (including master instance and read-only instance). You can pass instance type, purchase period and quantity, memory size, hard disk size and availability zone ID to query the instance price.
You can also create a new instance using [Create Instance (Annual and monthly plan)](/doc/api/253/1334) API.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryCdbPrice.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbType | Yes | String | Instance specification, fixed specification and custom specification are supported. CUSTOM means custom specification. You can acquire values for fixed specifications using [Query Supported Specifications](/doc/api/253/1333) API. <font style='color:red'> Fixed specification type will become unavailable in the future. It is recommended to use custom specifications. </font>|
| period | Yes | Int | Validity period of instance (Unit: month). The minimum and maximum values are 1 and 36 respectively. You can use [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) API to acquire the validity period of the instance that can be created. The returned field "timeSpan" represents the available period |
| goodsNum | Yes | Int | Number of instances. Default is 1, minimum is 1, and maximum is 10. You can acquire the number of instances that can be created using [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) API |
| memory | No | Int | Size of instance memory (unit: MB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire creatable memory specifications |
| volume | No | Int | Size of instance disk (unit: GB). This parameter is required if the value of cdbType is CUSTOM. This parameter will be ignored if the value of cdbType is an integer. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported disk range |
| zoneId | No | Int | Availability zone ID. By default, the system will automatically select an availability zone. You can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire supported availability zones |
| instanceRole | No | String | Instance type, default is master. Possible values include: master - master instance, ro - read-only instance |
| protectMode | No | Int | Data copy method. Default is 0, supported values include: 0 - indicates asynchronous copy, 1 - indicates semi-synchronized copy, 2 - indicates strong synchronized copy |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| price | Int | Instance price (unit: cent (RMB) |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9301 | InvalidParameter | Incorrect transaction parameter |
| 9006 | InternalError | Database internal error |
| 9003 | InvalidParameter | Incorrect parameter |


## 5. Example

Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=InquiryCdbPrice
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbType=CUSTOM
&memory=1000
&volume=25
&period=1
&goodsNum=1
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "price": 12804
}
```

