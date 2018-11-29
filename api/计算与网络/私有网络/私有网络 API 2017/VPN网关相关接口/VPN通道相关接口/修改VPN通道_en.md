## 1. API Description

This API (ModifyVpnConnEx) is used to modify VPN tunnel.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is ModifyVpnConnEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | string | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-03vihbk9. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| vpnGwId | Yes | String | VPN gateway ID assigned by the system, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| vpnConnId | Yes | String | VPN tunnel ID assigned by the system, which can be vpnConnId or unVpnConnId. unVpnConnId is recommended. For example: vpnx-ol6bcqp0. Can be queried via the API <a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>.  | 
| vpnConnName | No | String | Tunnel name; up to 60 characters. |
| preSharedKey | No | String | Pre-shared private key.  |
| userGwCidrBlock.n | No | Array | CIDR address of the peer IP address range, multiple values can be entered. Specifies the IDC IP address range the VPC can communicate with, later upgraded to spdAcl (finer granularity). Either userGwCidrBlock or spdAcl must be entered.  |
| spdAcl.n | No | Array | SPD rule group. You can specify which IP address range in the VPC can communicate with which IP address range in your IDC, upgraded from userGwCidrBlock. Either userGwCidrBlock or spdAcl must be entered. See the product instruction for details.  |
| IKESet.n | No | Array | IKE configuration (Internet Key Exchange). IKE is provided with a self-protection mechanism. The network security protocol is configured by the user. See <a href="https://cloud.tencent.com/doc/product/215/VPN%e8%bf%9e%e6%8e%a5#4.3-ike.E9.85.8D.E7.BD.AE" title="VPN Connection-IKE Configuration">VPN Connection-IKE Configuration</a> for details.  |
| IPsecSet.n | No | Array | IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud. See [VPN Connection-IPSec Configuration](https://intl.cloud.tencent.com/document/product/215/4956) for details. |

IKE configuration details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| IKESet.n.propoEncryAlgorithm | No | String | IKE configuration, encryption algorithm. Available values include 3des-cbc, aes-cbc-128, aes-cbc-192, aes-cbc-256 and des-cbc. The default is 3des-cbc. See the product instruction for details.  |
| IKESet.n.propoAuthenAlgorithm | No | String | IKE configuration, authentication algorithm. Available values include md5 and sha. The default is md5. See the product instruction for details.  |
| IKESet.n.exchangeMode | No | String | IKE configuration, negotiation mode. Available values include aggressive　and main. The default is main. See the product instruction for details.  |
| IKESet.n.localIdentity | No | String | IKE configuration, local identity type. Available values include address and fqdn. The default is address. See the product instruction for details.  |
| IKESet.n.remoteIdentity | No | String | IKE configuration, peered identity type. Available values include address and fqdn. The default is address. See the product instruction for details.  |
| IKESet.n.localAddress | No | String | IKE configuration, local identity. When address is selected for localIdentity, localAddress is required. localAddress is the public IP of the VPN gateway by default. See the product instruction for details.  |
| IKESet.n.remoteAddress | No | String | IKE configuration, peered identity. When address is selected for remoteIdentity, remoteAddress is required. See the product instruction for details.  |
| IKESet.n.localFqdnName | No | String | IKE configuration, local identity. When fqdn is selected for localIdentity, localFqdnName is required. See the product instruction for details.  |
| IKESet.n.remoteFqdnName | No | String | IKE configuration, peered identity. When fqdn is selected for remoteIdentity, remoteFqdnName is required. See the product instruction for details.  |
| IKESet.n.dhGroupName | No | String | IKE configuration, DH group, specifies the DH group used for exchanging the private key. Available values include group1, group2, group5, group14 and group24. See the product instruction for details.  |
| IKESet.n.ikeSaLifetimeSeconds | No | Int | IKE configuration, IKE SA Lifetime, unit: second, sets the lifetime of IKE SA. Value range: 60-604800. See the product instruction for details.  |
| encryptAlgorithm | No | String | IPsec configuration, encryption algorithm. Available values include 3des-cbc, aes-cbc-128, aes-cbc-192, aes-cbc-256, des-cbc and null. The default is 3des-cbc. See the product instruction for more details.  |


IPsec configuration details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| IPsecSet.n.integrityAlgorith | No | String | IPsec configuration, authentication algorithm. Available values include md5 and sha. The default is md5. See the product instruction for details.  |
| IPsecSet.n.ipsecSaLifetimeSeconds | No | Int | IPsec configuration, IPsec SA lifetime(s), unit: second. Value range: 180-604800. See the product instruction for details.  |
| IPsecSet.n.ipsecSaLifetimeTraffic | No | Int | IPsec configuration, IPsec SA lifetime(KB), unit: KB. Value range: 2560-604800. See the product instruction for details.  |
| IPsecSet.n.pfsDhGroup | No | String | IPsec configuration, PFS. Available values include null, dh-group1, dh-group14, dh-group2, dh-group24 and dh-group5. The default is null. See the product instruction for details.  |

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
| data.taskId | Int  | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

 ## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | VPC does not exist. Please check the information you entered. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidVpnGw.NotFound |  VPN gateway does not exist. Please check the information you entered. You can query the VPN gateway via the API <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| InvalidVpnGw.NotFound |  VPN tunnel does not exist.Please check the information you entered. You can query the VPN tunnel via the API <a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>.  |
 

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpnConnEx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-03vihbk9
  &vpnGwId=vpngw-kfldykuz
  &vpnConnId=vpnx-ol6bcqp0
  &userGwCidrBlock.0=10.100.2.0/24
  &preSharedKey=tencenttest

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "vpnGwId": "vpngw-kfldykuz",
        "vpcConnId": "vpnx-ol6bcqp0",
        "taskId": 12614,
        "vpcConnStatus": 2,
        "preSharedKey": "tencenttest",
        "userGwSubnetList": [
            "10.100.2.0\/24"
        ],
        "userGwId": 315
    }
}

```


