## 1. API Description

This API (ModifyNetworkInterface) is used to modify ENIs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/245/4772" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyNetworkInterface.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of ENI, for example: vpc-7t9nf3pu.  |
| networkInterfaceId | Yes | String | ENI ID assigned by the system,  for example: eni-m6dyj72l.  |
| eniName | No | String | ENI name; up to 60 characters; unique within the same VPC.  |
| eniDescription | No | String | ENI description, up to 60 characters. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information you entered. You can query the VPC by using the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNetworkInterface.NotFound | ENI does not exist. Please check the information you entered. You can query the ENI via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API.  |
| InvalidEniName.InUse | The ENI name has already been used.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNetworkInterface
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
&networkInterfaceId=eni-m6dyj72l
&eniName=barrytest
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}
```


