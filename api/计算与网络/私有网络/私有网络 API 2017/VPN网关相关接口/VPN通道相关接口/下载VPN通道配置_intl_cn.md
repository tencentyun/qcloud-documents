## 1. 接口描述

本接口(GetVpnConnConfig)用于下载VPN通道配置。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetVpnConnConfig。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpnConnId | 是 | String | 系统分配的VPN通道ID，可使用vpnConnId或unVpnConnId，建议使用unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E9%80%9A%E9%81%93%E5%88%97%E8%A1%A8" title="DescribeVpnConn">DescribeVpnConn</a>接口查询。 |  
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
 该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc错误码</a>
 

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

