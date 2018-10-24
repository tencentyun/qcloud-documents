## 1. API Description
 
This API (AttachClassicLinkVpc) is used to connect VPC and basic network devices.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) VPC and basic network devices must be in the same region.
2) For the differences between VPCs and basic networks, see <a href="https://cloud.tencent.com/doc/product/215/535#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C" title="私有网络与基础网络">here</a>.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is AttachClassicLinkVpc.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | The Virtual Private Cloud ID assigned by the system. Both the vpcId before upgrading and the upgraded unVpcId are supported. For example: vpc-dgd44d.  |
| instanceIds.n | Yes | Array | Basic network CVM ID, for example: instanceIds.0=ins-5d8a23rs. It can be queried via API <a href="https://cloud.tencent.com/doc/api/229/831" title="Query Instance List">DescribeInstances</a>.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>. |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
 | Error Code | Description |
|---------|---------|
| InvalidInstance.NotFound | The CVM does not exist. Please check the information you entered. To query the CVMs under the VPC, please see <a href="https://cloud.tencent.com/doc/api/229/831" title="Query CVM Instance List">Query CVM Instance List</a>.  |
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered. |
| InstanceLimitExceeded | Reached the upper limit of basic network devices linked to the VPC in the specified region. If you need more resources, please contact customer service. For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>.  |
| InstanceAlreadyLinked | The basic network CVM has been bound to another VPC. For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title=">VPC Service Limits">VPC Service Limits</a>.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=AttachClassicLinkVpc
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
	&vpcId=vpc-2ari9m7h
	&instanceIds.0=ins-df454d
</pre>

Output
```

{
    "code": 0,
    "message": "",
		"taskId":135254
}

```


