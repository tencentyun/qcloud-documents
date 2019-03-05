## 1. API Description

This API (MigratePrivateIpAddress) is used to migrate private IPs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) If a user of this API migrates a private IP from one ENI to another ENI, the primary IP address cannot be migrated.
2) The original ENI and the target ENI must be in the same subnet.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is MigratePrivateIpAddress.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of ENI, for example: vpc-7t9nf3pu.  |
| privateIpAddress | Yes | String | The private IP address to be migrated, for example: 10.0.0.6.  |
| oldNetworkInterfaceId | Yes | String | ID of the ENI before the private IP is migrated, for example: eni-m6dyj72l.  |
| newNetworkInterfaceId | Yes | String | ID of the ENI to which the private IP is migrated, for example: eni-dfddf454d.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed. |
| message | String | Error message. |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information you entered. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API.  |
| InvalidNetworkInterface.NotFound | ENI does not exist. Please check the information you entered. You can query the ENI via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=MigratePrivateIpAddress
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
&privateIpAddress=10.0.0.6
&oldNetworkInterfaceId=eni-m6dyj72l
&newNetworkInterfaceId=eni-dfddf454d
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data":
        {
            "taskId": 16284
        }
}
```


