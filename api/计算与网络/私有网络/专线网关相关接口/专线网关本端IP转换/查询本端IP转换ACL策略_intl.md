## 1. API Description

This API (DescribeLocalIPTranslationAclRule) is used to query the ACL rules for local IP translation.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeLocalIPTranslationAclRule.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID assigned by the system, for example: vpc-dfg5445.  |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID assigned by the system, for example: dcg-4d545d.  |
| originalIP | Yes | String | Original IP.  |
| translationIP | Yes | String | Translated IP.  |
| aclRules.n | No | Array | ID array of ACL rules, for example: aclRules.0=25.  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please refer to <a href="https://intl.cloud.tencent.com/document/product/215/4781" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| data.n | Array | Information array of acl rules.  |
| data.n.aclRuleId | Int | ACL rule ID, for example: 25.  |
| data.n.protocol | String | Protocol, for example TCP.  |
| data.n.sourcePort | String | The accessed source port, for example: 900.  |
| data.n.destinationCidr | String | The accessed destination IP, for example: 10.0.0.2/16.  |
| data.n.destinationPort | String | The accessed destination port, for example: 80-90. |

 ## 4. Error Code List
  The following list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e5%88%9b%e5%bb%ba%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c?viewType=preview" title="Querying Virtual Private Cloud List">Querying Virtual Private Cloud List</a> (DescribeVpcEx) API. |
| InvalidDirectConnectGateway.NotFound | Invalid Direct Connect gateway. Direct Connect gateway resource does not exist. Please verify that you have entered resource information correctly. This can be queried via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%b8%93%e7%ba%bf%e7%bd%91%e5%85%b3?viewType=preview" title="Querying Direct Connect Gateway">Querying Direct Connect Gateway</a> (DescribeDirectConnectGateway) API. |
| InvalidLocalIPTranslation.NotFound | Invalid local IP translation rule. Local IP translation rule does not exist. Please verify that you have entered resource information correctly. |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeLocalIPTranslationAclRule
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
&originalIP=10.0.0.5
&translationIP=138.0.0.11
</pre>
Output
```
{
    "code":"0",
    "message":""，
    "data":[
				{
							"aclRuleId":67,
							"protocol":"TCP",
							"sourcePort":"80",
							"destinationCidr":"10.0.0.2/18",
							"destinationPort":"90"
				}
		]
}
```


