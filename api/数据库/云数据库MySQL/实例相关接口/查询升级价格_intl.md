## 1. API Description
This API (InquiryCdbUpgradePrice) is used to query the upgrade price of Cloud Database instances. Instance types include master instance, disaster recovery instance and read-only instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryCdbUpgradePrice.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| memory | Yes | Int | Memory size after upgrade (unit: MB). To ensure the validity of the passed memory value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire the available memory specifications |
| volume | Yes | Int | Disk size after upgrade (unit: GB). To ensure the validity of the passed volume value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire the available disk range |
| instanceRole | No | String | Instance type. Default is master. Possible values include: master - master instance or disaster recovery instance, ro - read-only instance.
| protectMode | No | Int | Data copy method. Default is 0, supported values include: 0 - indicates asynchronous copy, 1 - indicates semi-synchronized copy, 2 - indicates strong synchronized copy. You can specify this parameter when querying master instances, while this parameter will be ignored when querying read-only instances or disaster recovery instances |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| price | Int | Price for upgrading an instance (unit: RMB 0.01) For instances with an annual or monthly plan, the parameter represents the total price that needs to be paid for upgrading an instance. For instances paid by usage, the parameter represents the new billing rate after the instance is upgraded |


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
https://cdb.api.qcloud.com/v2/index.php?Action=InquiryCdbUpgradePrice
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-jcti2cuw
&memory=2000
&volume=60
&instanceRole=master
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "price":"73"
}
```


