## 1. 接口描述

本接口(GetVpnConnConfig)用于下载 VPN 通道配置。
接口请求域名：`vpc.api.qcloud.com`。

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 GetVpnConnConfig。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpnConnId | 是 | String | 系统分配的 VPN 通道 ID，可使用 vpnConnId 或 unVpnConnId，建议使用 unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E9%80%9A%E9%81%93%E5%88%97%E8%A1%A8" title="DescribeVpnConn"> DescribeVpnConn </a>接口查询。 |  
| vendorname | 是 | string | 对端网关设备类型。 | 
| platform | 是 | String | 对端网关设备平台。 |
| software | 是 | String | 对端网关设备软件版本。 |  
| interfaceName | 是 | String | 通道接入设备物理接口名称。 |  



## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
| data.configFileInfo | String  | 配置文件内容 |

## 4. 错误码表
 该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码"> VPC 错误码</a>。
 

## 5. 示例
 
输入
<pre>
  https://domain/v2/index.php?Action=GetVpnConnConfig
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpnConnId=2
  &vendorname=cisco
  &platform=ios
  &software=V15.4
</pre>

输出
```
{
	"code": 0,
	"message": "ok",
	"data": [{
		"configFileInfo": "ike keychain keychain1\r \n                 pre-shared-key address 65.0.0.21 key simple key123\r  \n                 quit\rike proposal 1\r \n                 encryption-algorithm aes-cbc-128\r \n                 authentication-algorithm md5\r \n                 dh group14\r sa Lifetime 60\r \n                 quit\rike profile profile1\r \n                 keychain keychain1\r \n                 local-identity fqdn remote1\r \n                 match remote identity fqdn local1\r \n                 exchange-mode aggressive\r \n                 quit\rike invalid-spi-recovery enable\ripsec transform-set transform-set1\r \n                 esp authentication-algorithm sha1\r \n                 esp encryption-algorithm aes-cbc-128\r \n                 pfs dh-group1\r \n                 quit\racl advanced 3001\r \n                 rule permit ip source 55.55.55.55 0.0.0.255 destination 11.11.11.11 0.0.0.255\r\n                 ipsec policy policy1 1 isakmp\r \n                 transform-set transform-set1\r \n                 security acl 3001\r \n                 remote-address 65.0.0.21\r \n                 ike-profile profile1\r \n                 sa Lifetime time-based 180\r \n                 sa Lifetime traffic-based 2560\r \n                 quit\rip unreachables enable\rinterface GigabitEthernet0/0\r \n                 port link-mode route\r \n                 ipsec apply policy policy1\r quit"
	}]
}

```

