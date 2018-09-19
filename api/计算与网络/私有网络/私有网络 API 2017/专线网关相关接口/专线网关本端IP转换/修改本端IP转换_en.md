## 1. API Description

This API (ModifyLocalIPTranslationNatRule) is used to modify the local IP translation rules for Direct Connect gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

This API is used to modify the local IP translation rules for the specified Direct Connect gateway

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyLocalIPTranslationNatRule.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID assigned by the system, for example: vpc-dfg5445. |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, for example: dcg-4d545d. |
| oldOriginalIP | Yes | String | The original IP before modification. |
| oldTranslationIP | Yes | String | The translated IP before modification. |
| originalIP | No | String | The new original IP. |
| translationIP | No | String | The new translated IP. |
| description | No | String | Note. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/document/product/215/4781" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |

 ## 4. Error Code List
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="Querying Virtual Private Cloud List">Querying Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="Querying Direct Connect Gateway">Querying Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidLocalIPTranslation.NotFound | Invalid local IP translation rule. Local IP translation rule does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3%e6%9c%ac%e7%ab%afIP%e8%bd%ac%e6%8d%a2" title="Querying Local IP Translation for Direct Connect Gateway">Querying Local IP Translation for Direct Connect Gateway</a> (DescribeLocalIPTranslationNatRule) API. |
| InvalidOriginalIP.NotInVpcCidr | Invalid original IP.  The original IP is not in the VPC network segment. |
| InvalidOriginalIP.Duplicate | Invalid original IP. Duplication of original IP. The original IP has already existed in the local IP Direct Connect rules of the gateway. Duplication of original IP is not allowed. |
| InvalidTranslationIP.InVpcCidr | Invalid translated IP.  The translated IP is in the VPC network segment. |
| InvalidTranslationIP.Duplicate | Invalid translated IP.  Duplication of translated IP. The translated IP has already existed in the local IP Direct Connect rules of the gateway. Duplication of translated IP is not allowed. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyLocalIPTranslationNatRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
&oldOriginalIP=10.0.0.1
&oldTranslationIP=138.0.0.1
&originalIP=10.0.0.5
&translationIP=138.0.0.11
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "taskId":"17922"
    },
    "codeDesc":"Success"
}
```


