## 1. API Description

This API (GetVpnConnConfig) is used to download VPN tunnel configuration.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is GetVpnConnConfig.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpnConnId | Yes | String | VPN tunnel ID assigned by the system, which can be vpnConnId or unVpnConnId. unVpnConnId is recommended. For example: vpnx-ol6bcqp0. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E9%80%9A%E9%81%93%E5%88%97%E8%A1%A8" title="DescribeVpnConn">DescribeVpnConn</a>.  |  
| vendorname | Yes | string | Type of peer gateway device.  | 
| platform | Yes | String | Platform of peer gateway device.  |
| software | Yes | String | Software version of peer gateway device.  |  
| interfaceName | Yes | String | Name of the physical interface for tunnel access device.  |  



## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
| data.configFileInfo | String  | Content in configuration file |

## 4. Error Codes
 The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes for details</a>
 

## 5. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=GetVpnConnConfig
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpnConnId=2
	&vendorname=cisco
	&platform=ios
	&software=V15.4
</pre>

Output
```
{
    "code" : 0,
    "message" : "ok",
    "data" : [
		"configFileInfo" : "ike keychain keychain1\r 
                 pre-shared-key address 65.0.0.21 key simple key123\r  
                 quit\rike proposal 1\r 
                 encryption-algorithm aes-cbc-128\r 
                 authentication-algorithm md5\r 
                 dh group14\r sa Lifetime 60\r 
                 quit\rike profile profile1\r 
                 keychain keychain1\r 
                 local-identity fqdn remote1\r 
                 match remote identity fqdn local1\r 
                 exchange-mode aggressive\r 
                 quit\rike invalid-spi-recovery enable\ripsec transform-set transform-set1\r 
                 esp authentication-algorithm sha1\r 
                 esp encryption-algorithm aes-cbc-128\r 
                 pfs dh-group1\r 
                 quit\racl advanced 3001\r 
                 rule permit ip source 55.55.55.55 0.0.0.255 destination 11.11.11.11 0.0.0.255\r
                 ipsec policy policy1 1 isakmp\r 
                 transform-set transform-set1\r 
                 security acl 3001\r 
                 remote-address 65.0.0.21\r 
                 ike-profile profile1\r 
                 sa Lifetime time-based 180\r 
                 sa Lifetime traffic-based 2560\r 
                 quit\rip unreachables enable\rinterface GigabitEthernet0/0\r 
                 port link-mode route\r 
                 ipsec apply policy policy1\r quit"
	],
}

```


