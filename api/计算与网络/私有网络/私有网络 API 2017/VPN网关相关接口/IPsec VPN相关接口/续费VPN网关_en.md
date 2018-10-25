## 1. API Description

This API (RenewVpn) is used to renew the VPN.
Domain for API request: vpc.api.qcloud.com

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | string | VPC ID or unified ID (unified ID is recommended). For example: vpc-aa3z6vxo. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| vpnGwId | Yes | string | VPN gateway ID to be modified, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: pngw-nhg87nmg. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| period | Yes | Int | Number of month you want to renew (up to 36 months)| 



## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |

## 4. Error Codes
 This API does not have service error codes. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes</a>.

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=RenewVpn
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=gz_vpc_1111
	&period=1
	&vpnGwId=1
</pre>

Output
```
{
    "code" : 0,
    "message" : "ok",
}
```


