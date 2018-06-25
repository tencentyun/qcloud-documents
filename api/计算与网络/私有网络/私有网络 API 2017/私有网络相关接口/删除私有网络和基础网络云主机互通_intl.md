## 1. API Description
 
This API (DetachClassicLinkVpc) is used to delete the link between VPC and CVMs in basic network.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DetachClassicLinkVpc.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade.  |
| instanceIds.n | Yes | Array | Basic network CVM ID, for example: instanceIds.0=ins-df454d. It can be queried via API <a href="https://cloud.tencent.com/doc/api/229/831" title="Query Instance List">DescribeInstances</a>.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="https://intl.cloud.tencent.com/document/product/215/4781" title="Common Error Codes">Common Error Codes</a>. |
| message | String | Module error message description depending on API. |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, please see <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">Query Task Execution Result</a>. |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidInstance.NotFound | The CVM does not exist. Please verify that the instanceId you entered is correct. To query the CVMs under the VPC, please see <a href="https://cloud.tencent.com/doc/api/229/831" title="Query CVM Instance List">Query CVM Instance List</a>.  |
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered.  |

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DetachClassicLinkVpc
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


