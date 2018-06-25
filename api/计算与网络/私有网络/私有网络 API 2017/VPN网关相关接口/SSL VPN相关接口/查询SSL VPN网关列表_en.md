## 1. API Description

This API (DescribeSSLVpn) is used to query sslVPN.
Domain for API request: vpc.api.qcloud.com 

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------| 
| vpcId | No | String | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-amhnnao5. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| sslVpnId | No | String | SSL VPN gateway ID assigned by the system, for example: vpngw-dystbrkv.  |
| sslVpnName | No | String | SSL VPN gateway name. Fuzzy search is supported. |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of rows per page. Default is 20. Supports up to 50.  |
| orderField | No | String | Sort by a certain field. Currently, the sorting can be performed only by `createTime` (default) and `sslVpnName`.  |
| orderDirection | No | String | Ascending (`asc`) or descending (`desc`). Default is desc.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
|  totalCount |   Int | Returned total number of SSL VPN. |
| sslVpnSet.n | array  | Returned array. |
| sslVpnSet.n.sslVpnId | Int | SSL VPN gateway ID assigned by the system, for example: vpngw-l2tlvgb9.  |
| sslVpnSet.n.sslVpnName | String | SSL VPN network name.  |
| sslVpnSet.n.sslVpnStatus | Int | Operation statuses of SSL VPN gateway; 0: To be paid, 1: Payment error, 2: Delivering, 3: Delivery error, 4: Terminating, 5: Termination error, 6: Running.  |
| sslVpnSet.n.vpnGwStatus | Int |   Operation statuses of VPN gateway, 0: To be paid, 1: Payment error, 2: delivering, 3: Delivery Error, 4: Terminating, 5: Termination error, 6: Running.  |
| sslVpnSet.n.bandwidth | Int | SSL VPN bandwidth.  |
| sslVpnSet.n.sslVpnPort | String | sslVpn port.  |
| sslVpnSet.n.sslVpnDomainAclNum | Int | Number of sslVPN domain ACL policies.  |
| sslVpnSet.n.isAutoRenewals | Int | Indicate whether auto renewal is enabled; 1: On, 0: Off.  |
| sslVpnSet.n.expireTime | String | The expiry time of vpn gateway, for example: 2015-11-06 20:55:12. The VPN gateway will be terminated by the system when the expiry time is due, so timely renewal is necessary.  |
| sslVpnSet.n.createTime | String | Creation time of VPN gateway, for example: 2015-11-06 20:55:12.  |

## 4. Error Codes
This API does not have service error codes. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>

## 5. Example
 
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSSLVpn
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&openid=12345
&openkey=12345
&pf=qzone
&appid=12345
&format=json
&userip.0=10.0.0.1

</pre>

Output
```
{
    "code": 0,
    "message": "",
    "totalCount": 2,
    "sslVpnSet": [
        {
            "sslVpnName": "test",
            "sslVpnStatus": 6,
            "sslVpnId": "vpngw-l2tlvgb9",
            "sslVpnQuota": "mini",
            "bandwidth": 5,
            "vpcId": "gz_vpc_93",
            "isAutoRenewals": 1,
            "expireTime": "2016-11-17 15:33:03",
            "sslVpnAddress": "183.60.249.91",
            "sslVpnPort": 8000,
            "sslVpnDomainAclNum": 3,
            "unVpcId": "vpc-dsp338hz",
            "dealId": "2015991116"
        },
        {
            "sslVpnName": "test",
            "sslVpnStatus": 6,
            "sslVpnId": "vpngw-2csvvdob",
            "sslVpnQuota": "mini",
            "bandwidth": 5,
            "vpcId": "gz_vpc_75",
            "isAutoRenewals": 1,
            "expireTime": "2016-11-04 10:20:28",
            "sslVpnAddress": "183.60.249.44",
            "sslVpnPort": 8080,
            "sslVpnDomainAclNum": 2,
            "unVpcId": "vpc-fj1msp8l",
            "dealId": "20150718"
        }
    ]
}

```


