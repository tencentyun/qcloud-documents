## 1. API Description
This API (DeleteLocalIPTranslationNatRule) is used to delete the peer IP translation for Direct Connect gateway.
Domain for API request:<font style='color:red'>vpc.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DeletePeerIPTranslationNatRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID or unified ID (unified ID is recommended). |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID. |
| peerIPTranslation.n | Yes | Array | Array of peer IP translation rules.  |
| peerIPTranslation.n.originalIP | Yes | String | Original IP.  |
| peerIPTranslation.n.translationIP | Yes | String | Translated IP.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/215/4781' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code  |
| data | Array | Returned information.  |

 ## 4. Error Code Table
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c" title="Querying Virtual Private Cloud List">Query Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3" title="Querying Direct Connect Gateway">Query Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidPeerIPTranslation.NotFound | Invalid peer IP translation rules. Peer IP translation rule does not exist. Please verify that the resource information you entered is correct. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3%e5%af%b9%e7%ab%afIP%e8%bd%ac%e6%8d%a2" title="Querying Local IP Translation for Direct Connect Gateway">Query Peer IP Translation for Direct Connect Gateway</a> (DescribePeerIPTranslationNatRule) API. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeletePeerIPTranslationNatRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-csnmo39l
&directConnectGatewayId=dcg-mm01ughx
&peerIPTranslation.0.originalIP=10.100.10.3
&peerIPTranslation.0.translationIP=183.0.0.1
&peerIPTranslation.0.description=183.0.0.1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
        
    ]
}
```


