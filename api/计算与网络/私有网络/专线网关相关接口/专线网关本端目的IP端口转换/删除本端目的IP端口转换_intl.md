## 1. API Description
This API (DeleteLocalDestinationIPPortTranslationNatRule) is used to delete the local destination IP port translation for Direct Connect gateway.
Domain for API request:<font style='color:red'>vpc.api.qcloud.com </font>

The translated IP pool cannot be in the VPC network segment. IP pool supports a single IP, IP segment (such as 183.63.0.1-183.63.0.10) and CIDR format.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DeleteLocalDestinationIPPortTranslationNatRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | The Virtual Private Cloud ID assigned by the system. Both the vpcId before upgrading and the upgraded unVpcId are supported. For example: vpc-dgd45.  |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, for example: dcg-dgd454d.  |
| localDestinationIPPortTranslation.n | Yes | Array | Array of local destination IP port translation rules.  |
| localDestinationIPPortTranslation.n.originalIP | Yes | String | Original IP.  |
| localDestinationIPPortTranslation.n.originalPort | Yes | String | Original port.  |
| localDestinationIPPortTranslation.n.translationIP | Yes | String | Translated IP.  |
| localDestinationIPPortTranslation.n.translationPort | Yes | String | Translated port.  |
| localDestinationIPPortTranslation.n.proto | Yes | String | Protocol.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/215/4781' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code.  |
| data | Array | Returned information.  |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c" title="Querying Virtual Private Cloud List">Querying Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3" title="Querying Direct Connect Gateway">Querying Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidLocalDestinationIPPortTranslation.NotFound | The local destination IP port translation to be modified does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3%e6%9c%ac%e7%ab%af%e7%9b%ae%e7%9a%84IP%e7%ab%af%e5%8f%a3%e8%bd%ac%e6%8d%a2" title="查询专线网关本端目的IP端口转换">Querying Local Destination IP Port Translation for Direct Connect Gateway</a> (DescribeLocalDestinationIPPortTranslationNatRule) API. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteLocalDestinationIPPortTranslationNatRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&localDestinationIPPortTranslation.0.originalIP=10.100.10.3
&localDestinationIPPortTranslation.0.originalPort=80
&localDestinationIPPortTranslation.0.translationIP=183.0.0.1
&localDestinationIPPortTranslation.0.translationPort=90
&localDestinationIPPortTranslation.0.proto=tcp
&localDestinationIPPortTranslation.0.description=183.0.0.1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        
    ]
}
```


