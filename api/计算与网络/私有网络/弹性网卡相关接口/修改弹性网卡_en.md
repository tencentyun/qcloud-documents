## 1. API Description

This API (ModifyNetworkInterface) is used to modify elastic NICs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/245/4772" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyNetworkInterface.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of elastic NIC, for example: vpc-7t9nf3pu.  |
| networkInterfaceId | Yes | String | Elastic NIC ID assigned by the system,  for example: eni-m6dyj72l.  |
| eniName | No | String | Elastic NIC name. You can specify any name you like, but its length should be limited to 60 characters. The name must be unique within the same VPC.  |
| eniDescription | No | String | Elastic NIC description. You can specify any name you like, but its length should be limited to 60 characters. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |

## 4. Error Code List
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. You can query the VPC by using the <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNetworkInterface.NotFound | Invalid elastic NIC, Elastic NIC resource does not exist. Please verify that you have entered resource information correctly. You can query the elastic NIC via the <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API.  |
| InvalidEniName.InUse | The elastic NIC name has already been used.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNetworkInterface
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
&networkInterfaceId=eni-m6dyj72l
&eniName=barrytest
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


