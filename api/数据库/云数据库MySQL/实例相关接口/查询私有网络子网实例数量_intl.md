## 1. API Description
This API (GetCdbInstanceNumByVpcSubnetId) is used to query the number of instances under the subnet of a VPC.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbInstanceNumByVpcSubnetId.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | Int | VPC ID. It can be obtained via [Query VPC List](/doc/api/245/1372) |
| subnetIds.n | No | String | One or more subnet IDs (n represents array subscript starting with 0). Subnet ID under a VPC. It can be obtained via [Query Subnet List](/doc/api/245/1371) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code description|
| info | Array | Returned data |
Parameter info is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | int | Number of instances under the subnet of a VPC |
| vpcId | int | VPC ID |
| subnetIds | Array | ID of subnet in VPC |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbInstanceNumByVpcSubnetId
&<<a href="/document/product/236/6921">Common request parameters</a>>
&vpcId=13
&subnetIds.1=1115
&subnetIds.2=220
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "total":"2",
        "vpcId":"13",
        "subnetIds":{
            "220":"1",
            "1115":"1"
        }
    }
}
```


