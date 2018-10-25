## 1. API Description
This API (CreateLocalDestinationIPPortTranslationNatRule) is used to add local destination IP port translation for Direct Connect gateway.
Domain for API request:<font style='color:red'>vpc.api.qcloud.com </font>
1) The Direct Connect peer accesses the VPC actively and needs to access the mapped IP port in order to communicate with the original IP within the VPC. Response packets are not affected. Only NAT Direct Connect gateways are supported.



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CreateLocalDestinationIPPortTranslationNatRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID or unified ID (unified ID is recommended). |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID. |
| localDestinationIPPortTranslation.n | Yes | Array | Array of local destination IP port translation rules.  |
| localDestinationIPPortTranslation.n.originalIP | Yes | String | Original IP.  |
| localDestinationIPPortTranslation.n.originalPort | Yes | String | Original port.  |
| localDestinationIPPortTranslation.n.translationIP | Yes | String | Translated IP.  |
| localDestinationIPPortTranslation.n.translationPort | Yes | String | Translated port.  |
| localDestinationIPPortTranslation.n.proto | Yes | String | Protocol.  |
| localDestinationIPPortTranslation.n.description | No | String | Note.  |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code |
| data | Array | Returned information |

 ## 4. Error Code List
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="Querying Virtual Private Cloud List">Querying Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. The Direct Connect gateway does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="Querying Direct Connect Gateway">Querying Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidOriginalIP.NotInVpcCidr | Invalid original IP. The original IP is not in the VPC network segment. |
| InvalidTranslationIP.InVpcCidr | Invalid translated IP. The translated IP is in the VPC network segment. |
| InvalidTranslationIP.Duplicate | Invalid translated IP. Duplication of translated IP. The translated IP has already existed in the local IP Direct Connect rules of the gateway. Duplication of translated IP is not allowed. |
| LocalDestinationIPPortTranslationLimitExceeded | The local destination IP port translation rules you added have reached the upper limit. Please contact customer service for more resources. For more information on VPC resource restrictions, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateLocalDestinationIPPortTranslationNatRule
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


