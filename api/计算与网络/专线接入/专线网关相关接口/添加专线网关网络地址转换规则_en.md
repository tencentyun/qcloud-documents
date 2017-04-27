## 1. API Description
Domain: vpc.api.qcloud.com
API name: AddDirectConnectGatewayNatRule

This API is used to add network address translation rules for Direct Connect gateway.

## 2. Input Parameters
| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID |
| natRule | Yes | String | Network address translation rules, which are divided into local IP translation (localIPTranslation), peer IP translation (peerIPTranslation), local source address translation (localSourceIPPortTranslation), and local destination port translation (localDestinationIPPortTranslation). If both the rules "local IP translation" and "local source address translation" are set, the latter rule is ignored. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message | String | Error message |


## 4. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=AddDirectConnectGatewayNatRule
&vpcId=vpc-1y7wcr29
&directConnectGatewayId=dcg-beyteaqt
&natRule={"peerIPTranslation":[{"translationIP":"192.167.0.2","originalIP":"10.100.89.20"}]}
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


