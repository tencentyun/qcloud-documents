## 1. API Description

This API (SetSSLVpnDomain) is used to set sslVPN domain.
Domain for API request: vpc.api.qcloud.com

 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is SetSSLVpnDomain.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | Int | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| sslVpnId | No | Int | SSLvpn gateway ID assigned by the system, for example: vpngw-l2tlvgb9. Can be queried via the API <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2sslVPN?viewType=preview" title="DescribeSSLVpn">DescribeSSLVpn</a>.  |
| groupId | Yes | String |  Workgroup of domain. |
| ipPool.n | No | Array |  IP address range of sslVPN terminal. |
| acl.n | No | Array |  ACL rule. |
| acl.n.proto | Yes | String | ACL protocol, for example TCP. |
| acl.n.action | Yes | String | ACL rule, 0: Allow, 1: Reject. |
| acl.n.destinationPort | Yes | String | Destination port. |
| acl.n.sourceCidr | String | Yes | Source IP or IP address range. |
| acl.n.destinationCidr | String | Yes | Destination IP or IP address range. |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Codes
The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>

## 5. Example
 
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=SetSSLVpnDomain
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-39lpv32n
&sslVpnId=vpngw-m1ue61hx
&groupId=ugrp-975r1ku4
&sslvpnPort=443
&ipPool.0=192.168.16.119-192.168.16.121

</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "taskId": 13161
    }
}

```



