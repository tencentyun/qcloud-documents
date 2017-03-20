## 1. API Description

This API (AddVpnConnEx) is used to create VPN channel.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is AddVpnConnEx.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | string | VPC ID or unified ID (unified ID is recommended). Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| vpnGwId | Yes | String | VPN gateway ID assigned by the system, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| userGwId | Yes | String | Peered gateway ID, which can be userGwId or unUserGwId. unUserGwId is recommended. For example: cgw-e098slul. Can be queried via the API<a href="https://www.qcloud.com/document/product/215/5119" title=" DescribeUserGw"> DescribeUserGw</a>.  |
| vpnConnName | No | String | Channel name; you can specify any name you like, but its length should be limited to 60 characters.  |
| preSharedKey | No | String | Pre-shared private key.  |
| userGwCidrBlock.n | No | Array | CIDR address of the peered network segment, multiple values can be entered. Specifies the IDC network segments the VPC can communicate with, later upgraded to spdAcl (finer granularity). Either userGwCidrBlock or spdAcl must be entered.  |
| spdAcl | No | String | SPD rule group, json format. For example: {"10.0.0.5/24":["172.123.10.5/16"]}, 10.0.0.5/24 is a VPC private network segment, and 172.123.10.5/16 is an IDC network segment. You can specify which network segments in the VPC can communicate with which network segments in your IDC, upgraded from userGwCidrBlock. Either userGwCidrBlock or spdAcl must be entered.  |
| ikeSet.n | No | Array | IKE configuration (Internet Key Exchange). IKE is provided with a self-protection mechanism. The network security protocol is configured by the user. See <a href="https://www.qcloud.com/doc/product/215/VPN%e8%bf%9e%e6%8e%a5#4.3-ike.E9.85.8D.E7.BD.AE" title="VPN连接-IKE配置">VPN Connection-IKE Configuration</a> for details.  |
| ipsecSet.n | No | Array | IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud. See <a href="https://www.qcloud.com/doc/product/215/VPN%e8%bf%9e%e6%8e%a5#4.4-ipsec-.E4.BF.A1.E6.81.AF" title="VPN连接-IPSec配置">VPN Connection-IPsec Configuration</a> for details. |

IKE configuration details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| ikeSet.n.propoEncryAlgorithm | No | String | IKE configuration, encryption algorithm. Available values include 3des-cbc, aes-cbc-128, aes-cbc-192, aes-cbc-256 and des-cbc. The default is 3des-cbc. See the product instruction for details.  |
| ikeSet.n.propoAuthenAlgorithm | No | String | IKE configuration, authentication algorithm. Available values include md5 and sha. The default is md5. See the product instruction for details.  |
| ikeSet.n.exchangeMode | No | String | IKE configuration, negotiation mode. Available values include aggressive and main. The default is main. See the product instruction for details.  |
| ikeSet.n.localIdentity | No | String | IKE configuration, local identity type. Available values include address and fqdn. The default is address. See the product instruction for details.  |
| ikeSet.n.remoteIdentity | No | String | IKE configuration, peered identity type. Available values include address and fqdn. The default is address. See the product instruction for details.  |
| ikeSet.n.localAddress | No | String | IKE configuration, local identity. When address is selected for localIdentity, localAddress is required. localAddress is the public IP of the VPN gateway by default. See the product instruction for details.  |
| ikeSet.n.remoteAddress | No | String | IKE configuration, peered identity. When address is selected for remoteIdentity, remoteAddress is required. See the product instruction for details.  |
| ikeSet.n.localFqdnName | No | String | IKE configuration, local identity. When fqdn is selected for localIdentity, localFqdnName is required. See the product instruction for details.  |
| ikeSet.n.remoteFqdnName | No | String | IKE configuration, peered identity. When fqdn is selected for remoteIdentity, remoteFqdnName is required. See the product instruction for details.  |
| ikeSet.n.dhGroupName | No | String | IKE configuration, DH group, specifies the DH group used for exchanging the private key. Available values include group1, group2, group5, group14 and group24. See the product instruction for details.  |
| ikeSet.n.ikeSaLifetimeSeconds | No | Int | IKE configuration, IKE SA Lifetime, unit: second, sets the lifetime of IKE SA. Value range: 60-604800. See the product instruction for details.  |
| ikeSet.n.encryptAlgorithm | No | String | IPsec configuration, encryption algorithm. Available values include 3des-cbc, aes-cbc-128, aes-cbc-192, aes-cbc-256, des-cbc and null. The default is 3des-cbc. See the product instruction for more details.  |


IPsec configuration details

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| ipsecSet.n.integrityAlgorith | No | String | IPsec configuration, authentication algorithm. Available values include md5 and sha. The default is md5. See the product instruction for details.  |
| ipsecSet.n.ipsecSaLifetimeSeconds | No | Int | IPsec configuration, IPsec SA lifetime(s), unit: second. Value range: 180-604800. See the product instruction for details.  |
| ipsecSet.n.ipsecSaLifetimeTraffic | No | Int | IPsec configuration, IPsec SA lifetime(KB), unit: KB. Value range: 2560-604800. See the product instruction for details.  |
| ipsecSet.n.pfsDhGroup | No | String | IPsec configuration, PFS. Available values include null, dh-group1, dh-group14, dh-group2, dh-group24 and dh-group5. The default is null. See the product instruction for details.  |

 

## 3. Output Parameters
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
| data.taskId | Int  | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">API for Querying Task Execution Result</a>.  |

## 4. Error Codes

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidVpnGw.NotFound | Invalid VPN gateway. VPN gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the VPN gateway via the API <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| InvalidUserGw.NotFound | Invalid peer gateway. Peer gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the peered gateway via the API <a href="https://www.qcloud.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%af%b9%e7%ab%af%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeUserGw">DescribeUserGw</a>.  |
| InvalidVpnConnName | Invalid VPN name. You can specify any name you like, but its length should be limited to 60 characters.  |
| InvalidVpnConnName.InUse | VPN channel name already in use. The VPN channel name must be unique within the same VPC.  |
| VpnConnLimitExceeded | The limit of requested VPN channel resources for the specific region has been reached. Please contact customer service for more resources. For more information on VPC resource restrictions, see <a href="https://www.qcloud.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |



## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=AddVpnConnEx
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-amhnnao5
  &userGwId=cgw-e098slul
  &vpnGwId=vpngw-dystbrkv
  &userGwCidrBlock.0=10.56.20.1/24
  &preSharedKey=dgdgd33

</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "vpnGwId": "vpngw-dystbrkv",
        "userGwId": "cgw-e098slul",
        "vpnConnId": 0,
        "taskId": 12613,
        "vpnConnStatus": 0,
        "preSharedKey": "dgdgd33",
        "userGwSubnetList": [
            "10.56.20.1/24"
        ]
    }
}

```


