## 1. API Description

This API (DescribeVpnGw) is used to query VPN gateway list.
Domain for API request: vpc.api.qcloud.com  

 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | String | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-amhnnao5. You can query this through API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| vpnGwId | No | String |VPN gateway ID assigned by the system, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv.  |
| vpnGwName | No | String | VPN gateway name. Fuzzy search is supported. |
| dealId | No | String | Order number of purchased VPN gateway. You can query the details of purchased VPN gateway via the order number. |
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of lines per page. Default is 20. Maximum is 50.  |
| orderField | No | String | Sort by a certain field. Sorting by `createTime` (default) and `directConnectGatewayName` is supported.  |
| orderDirection | No | String | Ascending (asc) or descending (desc). Default is desc.  |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
|  totalCount |   Int | Return the total number of VPN gateways in the result. |
| data.n | array  | Returned array. |
| data.n.vpcId | String | Virtual private cloud ID assigned by the system, for example: gz_vpc_8849.  |
| data.n.unVpcId | String | Virtual private cloud ID assigned by the system, new ID is recommended. For example: vpc-0ox8fuhw.  |
| data.n.vpnGwId | Int | VPN gateway ID assigned by the system. For example: 122.  |
| data.n.unVpnGwId | String | New VPN gateway ID assigned by the system. New ID is recommended. For example: vpngw-nhg87nmg.  |
| data.n.vpnGwName | String | VPN network name.  |
| data.n.bandwidth | Int | VPN gateway bandwidth.  |
| data.n.vpnGwStatus | Int |  Operation statuses of VPN gateway, 0: To be paid, 1: Payment error, 2: delivering, 3: Delivery Error, 4: Terminating, 5: Termination error, 6: Running.  |
| data.n.vpnGwAddress | String | Public IP of VPN gateway.  |
| data.n.dealId | String | Production order ID of VPN gateway.  |
| data.n.isAutoRenewals | Int | Indicate whether auto renewal is enabled; 1: On, 0: Off.  |
| data.n.expireTime | String | The expiry time of VPN gateway, for example: 2015-11-06 20:55:12. The VPN gateway will be terminated by the system when the expiry time is due, so timely renewal is necessary.  |
| data.n.createTime | String | Creation time of VPN gateway, for example: 2015-11-06 20:55:12.  |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>. |
| InvalidVpnGw.NotFound | Invalid VPN gateway. VPN gateway resource does not exist. Please verify that the resource information you entered is correct.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpnGw
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-erxok83l

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "totalCount": 3,
    "data": [
        {
            "vpcId": "sh_vpc_389",
            "unVpcId": "vpc-aa3z6vxo",
            "vpcName": "joezou",
            "vpcCidrBlock": "172.16.0.0\/16",
            "vpnGwId": 122,
            "unVpnGwId": "vpngw-nhg87nmg",
            "vpnGwName": "test001",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.26.189",
            "dealId": "896973",
            "localSlaIp": "169.254.97.7",
            "isAutoRenewals": true,
            "expireTime": "2015-12-23 19:04:40",
            "createTime": "2015-11-23 19:02:54"
        },
        {
            "vpcId": "sh_vpc_390",
            "unVpcId": "vpc-36dt60su",
            "vpcName": "joezou-2",
            "vpcCidrBlock": "172.17.0.0\/16",
            "vpnGwId": 121,
            "unVpnGwId": "vpngw-d77hr4r8",
            "vpnGwName": "roy_test",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.72.143",
            "dealId": "896725",
            "localSlaIp": "169.254.97.5",
            "isAutoRenewals": true,
            "expireTime": "2016-01-23 17:01:05",
            "createTime": "2015-11-23 16:59:23"
        },
        {
            "vpcId": "sh_vpc_314",
            "unVpcId": "vpc-4w87vv5s",
            "vpcName": "test",
            "vpcCidrBlock": "10.0.0.0\/16",
            "vpnGwId": 120,
            "unVpnGwId": "vpngw-4tu3v388",
            "vpnGwName": "roy_test",
            "bandwidth": 5,
            "vpnGwStatus": 6,
            "vpnGwAddress": "115.159.92.113",
            "dealId": "896720",
            "localSlaIp": "169.254.97.3",
            "isAutoRenewals": true,
            "expireTime": "2016-01-23 17:00:25",
            "createTime": "2015-11-23 16:58:32"
        }
    ]
}

```


