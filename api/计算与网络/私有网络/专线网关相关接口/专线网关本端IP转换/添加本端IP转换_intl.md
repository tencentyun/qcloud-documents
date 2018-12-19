## 1. API Description
This API (CreateLocalIPTranslationNatRule) is used to add local IP translation for Direct Connect gateway.
Domain for API request:<font style='color:red'>vpc.api.qcloud.com </font>

1) The original IP within the VPC is mapped to a new IP, which is used to communicate with the Direct Connect peer. Only NAT gateways are supported.
2) The original IP must be in the VPC network segment, while the translated IP cannot be in the VPC network segment.
3) Duplication of original IP and duplication of translated IP are not allowed in the local IP translation rules under the same NAT gateway.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CreateLocalIPTranslationNatRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | The Virtual Private Cloud ID assigned by the system. Both the vpcId before upgrading and the upgraded unVpcId are supported. For example: vpc-ddg454. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, for example: dcg-dgd54g. |
| localIPTranslation.n | Yes | Array | Local IP translation. |
| localIPTranslation.n.originalIP | Yes | String | Original IP. |
| localIPTranslation.n.translationIP | Yes | String | Translated IP. |
| localIPTranslation.n.description | No | String | Note. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/215/4781' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned information. |
| data.taskId | Int  | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |
| codeDesc | String | Error code. |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="Querying Virtual Private Cloud List">Querying Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="Querying Direct Connect Gateway">Querying Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidOriginalIP.NotInVpcCidr | Invalid original IP. The original IP is not in the VPC network segment. |
| InvalidOriginalIP.Duplicate | Invalid original IP. Duplication of original IP. The original IP has already existed in the local IP Direct Connect rules of the gateway. Duplication of original IP is not allowed. |
| InvalidTranslationIP.InVpcCidr | Invalid translated IP. The translated IP is in the VPC network segment. |
| InvalidTranslationIP.Duplicate | Invalid translated IP.  Duplication of translated IP. The translated IP has already existed in the local IP translation rules of the gateway. Duplication of translated IP is not allowed. |
| LocalIPTranslationLimitExceeded | The local IP translation rules you added have reached the upper limit. Please contact customer service for more resources. For more information on VPC resource restrictions, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions"> VPC Usage Restrictions</a>. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateLocalIPTranslationNatRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&localIPTranslation.0.originalIP=10.100.10.2
&localIPTranslation.0.translationIP=10.100.10.2
&localIPTranslation.0.description=183.0.0.1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "taskId":"17934"
    },
    "codeDesc":"Success"
}
```


