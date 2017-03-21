## 1. API Description

This API (DescribeSSLVpnDomain) is used to query sslVPN domain.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeSSLVpnDomain.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | Int | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| sslVpnId | No | Int | SSLvpn gateway ID assigned by the system, for example: vpngw-l2tlvgb9. Can be queried via the API <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2sslVPN?viewType=preview" title="DescribeSSLVpn">DescribeSSLVpn</a>.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| data.n | Array | Returned ssl vpn domain information |
| data.n.groupId | String | Workgroup ID, for example: ugrp-8zbvqpea. |
| data.n.ipPool | Array | Terminal IP range. |
| data.n.acl.n | Array | Information array of acl rules. |

Information array of acl rules

| Parameter Name | Type | Description |
|---------|---------|---------|
| acl.n.proto | String | acl protocol, for example tcp. |
| acl.n.action | String | ACL rule, 0: Allow, 1: Reject. |
| acl.n.destinationPort | String | Destination port. |
| acl.n.sourceCidr | String | Source IP or source network segment. |
| acl.n.destinationCidr | String | Destination IP or network segment. |

## 4. Error Code Table
 The API does not have a business error code. For common error codes, see <a href="https://www.qcloud.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>
 
## 5. Example
 
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSSLVpnDomain
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=93
&sslVpnId=vpngw-l2tlvgb9
&groupId=dgdgd
&sslVpnPort=442
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": [
        {
            "groupId": "ugrp-8zbvqpea",
            "ipPool": [
                "172.23.138.16-172.23.138.20"
            ],
            "acl": [
                {
                    "proto": "all",
                    "action": 1,
                    "destinationPort": 0,
                    "sourceCidr": "0.0.0.0\/0",
                    "destinationCidr": "0.0.0.0\/0"
                }
            ]
        }
    ]
}
```


