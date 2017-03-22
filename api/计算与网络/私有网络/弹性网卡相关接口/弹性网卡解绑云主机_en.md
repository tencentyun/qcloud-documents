## 1. API Description

This API (DetachNetworkInterface) is used to unbind elastic NICs.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) Unbind elastic NICs from the CVM.
2) After the elastic NICs are unbound, all the EIP addresses will be unassociated with the elastic NICs and be charged accordingly. For details on the billing methods, refer to <a href="https://www.qcloud.com/doc/product/213/1941#6.-.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91ip.E7.9A.84.E8.AE.A1.E8.B4.B9" title="EIP Billing Method">EIP Billing Method</a>.
3) Only CVMs that are in a running/shutdown status can bind elastic NICs. For details on the CVM status, refer to <a href="https://www.qcloud.com/doc/api/229/831" title="Query Tencent CVM Information">Query Tencent CVM Information.</a>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/245/4772" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DetachNetworkInterface.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of elastic NIC, for example: vpc-7t9nf3pu |
| networkInterfaceId | Yes | String | Elastic NIC ID, for example: eni-m6dyj72l |
| instanceId | Yes | String | CVM instance ID, for example: ins-xx44545f |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed.
| message | String | Error message |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Code Table
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNetworkInterface.NotFound | Invalid elastic NIC, Elastic NIC resource does not exist. Please verify that the resource information you entered is correct. You can query the elastic NIC via the <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API |
| InvalidInstance.NotFound | Invalid CVM instance. The CVM instance resource does not exist. Please verify that the resource information you entered is correct. You can query the CVM instance via the <a href="https://www.qcloud.com/doc/api/229/831" title="DescribeInstances">DescribeInstances</a> API |
| InvalidNetworkInterface.NotAttached | The elastic NIC is already unbound from the CVM |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DetachNetworkInterface
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-7t9nf3pu
&networkInterfaceId=eni-m6dyj72l
&instanceId=ins-xx44545f
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":16284
}
```


