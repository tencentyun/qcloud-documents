## 1. API Description

This API (ModifyVpnGw) is used to modify the attributes of VPN gateway.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyVpnGw.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-amhnnao5. You can query this through API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| vpnGwId | Yes | String | VPN gateway ID to be modified, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| vpnGwName | No | String | Modified gateway name. You can use any content as long as it does not exceed 60 characters. The name must be unique under the same VPC.  |
| isAutoRenewals | No | Int | Indicate whether auto renewal is enabled. 0 indicates that the instance is not automatically renewed; 1 indicates that the instance is automatically renewed.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |

## 4. Error Code Table
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidVpnGw.NotFound | Invalid VPN gateway. VPN gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the VPN gateway via the API <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| InvalidVpnGwState | Invalid VPN gateway status |
| InvalidVpnGwName | Invalid VPN gateway name. You can specify any name you like, but its length should be limited to 60 characters.  |
| InvalidVpnGwName.InUse | The VPN gateway name is already in use by other VPN gateways under the VPC. The VPN gateway name must be unique under the same VPC.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpnGw
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &vpnGwId=vpngw-dystbrkv
  &vpnGwName=test-9910
  &isAutoRenewals=0

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


