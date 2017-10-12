## 1. API Description

This API (DescribeVpnConn) is used to query VPN tunnel list.
Domain for API request: vpc.api.qcloud.com

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | No | string | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-03vihbk9. It can be queried via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API.  | 
| vpnGwId | No  | String | VPN gateway ID assigned by the system, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv. It can be queried via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a> API.  |
| vpnConnId | No  | String | VPN tunnel ID assigned by the system, which can be `vpnConnId` or `unVpnConnId`. `unVpnConnId` is recommended. For example: `vpnx-ol6bcqp0`.  |  
| vpnConnName | No  | String | VPN tunnel name, fuzzy query is supported.  |  
| offset | No | Int | Offset of initial line. Default is 0.  |
| limit | No | Int | Number of rows per page. Default is 20. Supports up to 50.  |
| orderField | No | String | Sort by a certain field. Currently, the sorting can be performed only by `createTime` (default) and `vpnConnName`.  |
| orderDirection | No | String | Ascending (`asc`) or descending (`desc`). Default is `desc`.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
| totalCount |   Int | Return the total number of VPN tunnels in the result|
| data.n | Array  | Returned array |
| data.n.vpcId | String | Virtual private cloud ID assigned by the system, for example: gz_vpc_8849.  |
| data.n.unVpcId | String | Virtual private cloud ID assigned by the system, new ID is recommended. For example: vpc-0ox8fuhw.  |
| data.n.vpnGwId | Int | VPN gateway ID assigned by the system. For example: 122.  |
| data.n.unVpnGwId | String | New VPN gateway ID assigned by the system. New ID is recommended. For example: vpngw-nhg87nmg.  |
| data.n.vpnGwAddress | String | Public IP of VPN gateway. For example: 112.2.3.10.  |
| data.n.userGwId | String |Peer gateway ID assigned by the system. For example: 122.   |
| data.n.unUserGwId | String | New peer gateway ID assigned by the system. For example: cgw-e098slul.  |
| data.n.userGwAddress | String | Public IP of the peer gateway. For example: 183.12.0.1.  |
| data.n.vpnConnName | String | Tunnel name.  |
| data.n.preSharedKey | String | Pre-shared private key. For example: d!@#12d. |
| data.n.sourceCidr | Array | Source IP address range.  |
| data.n.destinationCidr | Array | Destination IP address range.  |
| data.n.vpcConnStatus | Int | VPN tunnel statuses, 0: Creating, 1: Creation error, 2: Modifying, 3: Modification error, 4: Deleting, 5: Deletion error, 6: Running properly. |
| data.n.netStatus | String | Network condition of the VPN tunnel, available: connected, unavailable: not connected. |
| data.n.IKEArr.n | Array | Information array of IKE configurations.  |
| data.n.IPSECArr.n | Array | Information array of IPsec configurations.  |

**Details of `data.n.IKEArr.n`**

| Parameter Name | Type | Description |
|---------|---------|---------|
| IKEArr.n.propoEncryAlgorithm |String | IKE configuration, identity authentication method. For example: 3des-cbc. See the product instruction for details.  |
| IKEArr.n.propoAuthenAlgorithm | String | IKE configuration, authentication algorithm. For example: md5. See the product instruction for details.  |
| IKEArr.n.exchangeMode |String | IKE configuration, negotiation mode. For example: aggressive. See the product instruction for details.  |
| IKEArr.n.localIdentity | String | IKE configuration, local identity type. For example: address. See the product instruction for details.  |
| IKEArr.n.remoteIdentity | String | IKE configuration, peer identity type. For example: address. See the product instruction for details.  |
| IKEArr.n.localAddress | String | IKE configuration, local identity. localAddress is the public IP of the VPN gateway by default. See the product instruction for details.  |
| IKEArr.n.remoteAddress | String | IKE configuration, peer identity. See the product instruction for details.  |
| IKEArr.n.localFqdnName | String | IKE configuration, local identity. See the product instruction for details.  |
| IKEArr.n.remoteFqdnName | String | IKE configuration, peer identity. See the product instruction for details.  |
| IKEArr.n.dhGroupName | String | IKE configuration, DH group, specifies the DH group used for exchanging the private key. For example: group1. See the product instruction for details.  |
| IKEArr.n.ikeSaLifetimeSeconds | Int | IKE configuration, IKE SA Lifetime, unit: second, sets the SA lifetime of IKE security proposal. For example: 3600. See the product instruction for details.  |

**Details of `data.n.IPSECArr.n`**

| Parameter Name | Type | Description |
|---------|---------|---------|
| IPSECArr.n.encryptAlgorithm | String | IPsec configuration, encryption algorithm. For example: 3des-cbc. See the product instruction for details.  |
| IPSECArr.n.integrityAlgorith | String | IPsec configuration, authentication algorithm. For example: md5. See the product instruction for details.  |
| IPSECArr.n.ipsecSaLifetimeSeconds |  Int | IPsec configuration, IPsec SA lifetime (s), unit: second. For example: 360. See the product instruction for details.  |
| IPSECArr.n.ipsecSaLifetimeTraffic |  Int | IPsec configuration, IPsec SA lifetime (KB), unit: KB. For example: 3600. See the product instruction for details.  |
| IPSECArr.n.pfsDhGroup |  String | IPsec configuration, PFS. For example: dh-group1. See the product instruction for details.  |


## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please check the information you entered. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidVpnGw.NotFound | Invalid VPN gateway. VPN gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the VPN gateway via the API <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| InvalidVpnGw.NotFound | Invalid VPN tunnel. VPN tunnel resource does not exist. Please verify that the resource information you entered is correct. You can query the VPN tunnel via the API <a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>.  |


## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpnConn
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
            "vpcId": "gz_vpc_76",
            "unVpcId": "vpc-03vihbk9",
            "vpcName": "pan-vpc2",
            "vpcCidrBlock": "10.100.2.0\/24",
            "vpnGwId": 547,
            "unVpnGwId": "vpngw-kfldykuz",
            "vpnGwName": "test-76",
            "vpnGwAddress": "183.60.249.32",
            "vpnConnId": 399,
            "unVpnConnId": "vpnx-ol6bcqp0",
            "vpnConnName": "399_vpnconn",
            "userGwId": 315,
            "unUserGwId": "cgw-e098slul",
            "userGwName": "9101",
            "userGwAddress": "183.60.249.39",
            "vpcConnStatus": 6,
            "preSharedKey": "tencent",
            "remoteSlaIp": "169.254.112.2",
            "sourceCidr": [
                "10.100.2.0\/24"
            ],
            "destinationCidr": [
                "10.100.25.0\/24"
            ],
            "vpnProto": "ip-sec",
            "createTime": "2015-11-06 11:20:39",
            "IKEArr": {
                "propoAuthenAlgorithm": "sha",
                "propoEncryAlgorithm": "des-cbc",
                "exchangeMode": "main",
                "localIdentity": "address",
                "remoteIdentity": "address",
                "localAddress": "183.60.249.32",
                "remoteAddress": "183.60.249.39",
                "localFqdnName": null,
                "remoteFqdnName": null,
                "dhGroupName": "group1",
                "ikeSaLifetimeSeconds": "86400"
            },
            "IPSECArr": {
                "encryptAlgorithm": "aes-cbc-128",
                "integrityAlgorith": "sha1",
                "encapMode": "tunnel",
                "securityProto": "ESP",
                "pfsDhGroup": "null",
                "ipsecSaLifetimeSeconds": "3600",
                "ipsecSaLifetimeTraffic": "1843200"
            }
        },
        {
            "vpcId": "gz_vpc_80",
            "unVpcId": "vpc-fyvpmam9",
            "vpcName": "pan-vpc6",
            "vpcCidrBlock": "10.100.6.0\/24",
            "vpnGwId": 453,
            "unVpnGwId": "vpngw-ncr48l69",
            "vpnGwName": "huasan-8080",
            "vpnGwAddress": "183.60.249.42",
            "vpnConnId": 301,
            "unVpnConnId": "vpnx-85ao9zdy",
            "vpnConnName": "301_vpnconn",
            "userGwId": 245,
            "unUserGwId": "cgw-7ihaps8r",
            "userGwName": "183.60.249.44",
            "userGwAddress": "183.60.249.44",
            "vpcConnStatus": 6,
            "preSharedKey": "tencent",
            "remoteSlaIp": "169.254.112.4",
            "sourceCidr": [
                "10.100.6.0\/24"
            ],
            "destinationCidr": [
                "10.100.2.0\/24"
            ],
            "vpnProto": "ip-sec",
            "createTime": "2015-08-08 16:23:04",
            "IKEArr": {
                "propoAuthenAlgorithm": "sha",
                "propoEncryAlgorithm": "des-cbc",
                "exchangeMode": "main",
                "localIdentity": "address",
                "remoteIdentity": "address",
                "localAddress": "183.60.249.42",
                "remoteAddress": "183.60.249.44",
                "localFqdnName": null,
                "remoteFqdnName": null,
                "dhGroupName": "group1",
                "ikeSaLifetimeSeconds": "86400"
            },
            "IPSECArr": {
                "encryptAlgorithm": "aes-cbc-128",
                "integrityAlgorith": "sha1",
                "encapMode": "tunnel",
                "securityProto": "ESP",
                "pfsDhGroup": "null",
                "ipsecSaLifetimeSeconds": "3600",
                "ipsecSaLifetimeTraffic": "1843200"
            }
        },
        {
            "vpcId": "gz_vpc_80",
            "unVpcId": "vpc-fyvpmam9",
            "vpcName": "pan-vpc6",
            "vpcCidrBlock": "10.100.6.0\/24",
            "vpnGwId": 453,
            "unVpnGwId": "vpngw-ncr48l69",
            "vpnGwName": "huasan-8080",
            "vpnGwAddress": "183.60.249.42",
            "vpnConnId": 292,
            "unVpnConnId": "vpnx-p0j71qf6",
            "vpnConnName": "292_testtest",
            "userGwId": 232,
            "unUserGwId": "cgw-esg61xg5",
            "userGwName": "183.60.249.24",
            "userGwAddress": "183.60.249.24",
            "vpcConnStatus": 6,
            "preSharedKey": "tencent",
            "remoteSlaIp": "169.254.112.3",
            "sourceCidr": [
                "10.100.6.0\/24"
            ],
            "destinationCidr": [
                "10.100.12.0\/24"
            ],
            "vpnProto": "ip-sec",
            "createTime": "2015-08-06 20:29:25",
            "IKEArr": {
                "propoAuthenAlgorithm": "md5",
                "propoEncryAlgorithm": "3des-cbc",
                "exchangeMode": "main",
                "localIdentity": "address",
                "remoteIdentity": "fqdn",
                "localAddress": "183.60.249.42",
                "remoteAddress": null,
                "localFqdnName": null,
                "remoteFqdnName": "vpn86",
                "dhGroupName": "group2",
                "ikeSaLifetimeSeconds": "11180"
            },
            "IPSECArr": {
                "encryptAlgorithm": "aes-cbc-192",
                "integrityAlgorith": "md5",
                "encapMode": "tunnel",
                "securityProto": "ESP",
                "pfsDhGroup": "dh-group1",
                "ipsecSaLifetimeSeconds": "500",
                "ipsecSaLifetimeTraffic": "80000"
            }
        }
    ]
}

```


