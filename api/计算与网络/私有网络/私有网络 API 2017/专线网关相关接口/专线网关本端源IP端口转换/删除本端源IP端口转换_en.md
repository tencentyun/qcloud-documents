## 1. API Description
This API (DeleteLocalSourceIPPortTranslationNatRule) is used to delete the local source IP port translation for Direct Connect gateway.
Domain for API request:<font style='color:red'>vpc.api.qcloud.com </font>

Errors will occur when deleting a rule that does not exist.
## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DeleteLocalSourceIPPortTranslationNatRule.


| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system. Support both vpcId before the upgrade and unVpcId after the upgrade. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system. |
| localSourceIPPortTranslation.n  | Yes | array | local source address translation array.  |
| localSourceIPPortTranslation.n.translationIPPool  | Yes | string | Translated IP pool.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned data.  |
| data.taskId | Int  | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |
| codeDesc | String | Error code.  |

 ## 4. Error Code Table
  The following list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="Querying Virtual Private Cloud List">Query Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="Querying Direct Connect Gateway">Query Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidTranslationIPPool.NotFound | Invalid translated IP pool. Translated IP pool does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3%e6%9c%ac%e7%ab%af%e6%ba%90IP%e7%ab%af%e5%8f%a3%e8%bd%ac%e6%8d%a2" title="查询专线网关本端源IP端口转换">Query Local Source IP Port Translation for Direct Connect gateway</a> (DescribeLocalSourceIPPortTranslationNatRule) API. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteLocalSourceIPPortTranslationNatRule
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&localSourceIPPortTranslation.0.translationIPPool=183.12.63.0-183.12.63.20
&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "taskId":"17923"
    },
    "codeDesc":"Success"
}
```


