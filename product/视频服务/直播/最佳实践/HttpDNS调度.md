## 方案背景
云直播海外的推流和播放调度默认使用域名的 DNS 解析调度，它是一种最常见、最简单的接入方式。由于国内外的网络环境较为复杂，导致域名解析错误或流量跨网的问题普遍存在，云直播推荐您使用 HTTPDNS 方案来优化直播调度。

运营商 LocalDNS 的出口根据权威 DNS 目标 IP 地址进行 NAT，或者将解析请求转发至其他 DNS 服务器，导致权威 DNS 无法正确识别运营商的 LocalDNS IP，从而引发域名解析错误和流量跨网等问题。腾讯云 HTTPDNS 具有全球领先的 DNS 集群技术，可支持多运营商和自定义线路，进行优化调度。详细请参见 [移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/3519)。

>?  本文为您阐述如何将 HTTPDNS 调度方案用于腾讯云国内和海外直播推流和播放的调度加速，HTTPDNS 接口请参见 [移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54976)。

## 前期准备
1. 开通 HTTPDNS 服务，请参见腾讯云移动解析 HTTPDNS 控制台的服务 [开通步骤](https://cloud.tencent.com/document/product/379/54577)。
2. 前往 [开发配置页](https://console.cloud.tencent.com/httpdns/configure)，查看鉴权信息：授权 ID、 DES 密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/57de24e2871bc76b85d5c8b38eb0e751.png)

## 上行推流使用 HTTPDNS 进行调度

### 请求上行接入点 IP

HTTPDNS 请求：`http://119.29.29.98/d?dn={$push_domain DES加密字符串}&ip={$ip DES加密字符串}&id=$id` ，HTTP Get 请求，参数的含义如下：

- push_domain 代表推流域名，该字段需要经过 DES 加密，密钥信息通过[HTTPDNS开发配置页](https://console.cloud.tencent.com/httpdns/configure)获取，具体请参见 [DES 加解密说明](https://cloud.tencent.com/document/product/379/3530#des-.E7.AE.97.E6.B3.95)。
- ip 字段代表请求端的外网出口 IP，这个 IP 代表最终会调度到的接入点 IP 所在的地区和运营商，该字段也同样需要经过 DES 加密。
- id 字段代表用户鉴权标识，唯一标识每个用户。

### 解密接入点IP

通过 HTTPDNS 获取到的数据为 DES 密文，需要经过 DES 解密，得到 server_ip，具体请参见 [DES 加解密说明](https://cloud.tencent.com/document/product/379/3530#des-.E7.AE.97.E6.B3.95)。

### 拼接上行推流 URL

这里的 server_ip 为**请求上行接入点 IP** 中获取到的 IP，那么拼接的推流 URL 如下：`rtmp://server_ip/live/streamname?txTime=xxx&txSecret=xxx&txHost=domain`，最重要的是在原有的推流参数中新增代表业务推流域名的字段 txHost。

## 下行播放使用 HTTPDNS 进行调度

### 请求下行接入点 IP

HTTPDNS 请求：`http://119.29.29.98/d?dn={$domain DES加密字符串}&ip={$ip DES加密字符串}&id=$id` ，HTTP Get 请求，参数的含义如下：

| 字段 | 含义 | 
|---------|---------|
| push_domain | 播放域名，该字段需要经过 DES 加密，密钥信息通过 [HTTPDNS开发配置页](https://console.cloud.tencent.com/httpdns/configure) 获取，具体请参见 [DES 加解密说明](https://cloud.tencent.com/document/product/379/3530#des-.E7.AE.97.E6.B3.95)。 | 
| ip | 请求端的外网出口 IP，这个 IP 代表最终会调度到的接入点 IP 所在的地区和运营商，该字段也同样需要经过 DES 加密。 | 
| id | 用户鉴权标识，唯一标识每个用户。 | 

### 解密接入点IP

通过 HTTPDNS 获取到的数据为 DES 密文，需要经过 DES 解密，得到 server_ip，具体请参见 [DES 加解密说明](https://cloud.tencent.com/document/product/379/3530#des-.E7.AE.97.E6.B3.95)。

### 拼接下行播放 URL
- **HTTP**：包含 FLV 以及 HLS 的播放协议，这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，则 HTTP 的播放 URL 拼接如下：
```
http://server_ip/play_domain/live/streamname.flv?xxxxxxxxxx
http://server_ip/play_domain/live/ streamname.m3u8?xxxxxxxxxx
http://server_ip/play_domain/live/ streamname -123.ts?xxxxxxxxxx
```
- **HTTPS**：包含 FLV 以及 HLS 的播放协议，这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，HTTPS 的拼接规则依赖于播放器逻辑，**要求在 TCP 建立连接的目标 IP 为 HTTPDNS 调度的 server_ip**，具体请求的播放 URL 需要是常规的播放请求：
```
https://server_ip/play_domain/live/ streamname.flv?xxxxxxxxxx
https://server_ip/play_domain/live/ streamname.m3u8?xxxxxxxxxx
https://server_ip/play_domain/live/ streamname -123.ts?xxxxxxxxxx
```
- **RTMP**：这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，则 RTMP 的播放 URL 拼接如下：
```
rtmp://server_ip/play_domain/live/ streamname?xxxxxxxxxx
```

>? 由于 HTTPDNS 请求有小概率异常，如 HTTPDNS 访问超时，或者返回的结果非 IP 格式，或者返回为空等等，请兜底至 LocalDNS 进行域名解析。
