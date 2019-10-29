## 方案背景
云直播海外的推流和播放调度默认使用域名的 DNS 解析调度，它是一种最常见、最简单的接入方式。由于海外的网络环境较为复杂，导致域名解析错误或流量跨网的问题普遍存在，云直播推荐您使用 HttpDNS 方案来优化海外直播调度。

运营商 LocalDNS 的出口根据权威 DNS 目标 IP 地址进行 NAT，或者将解析请求转发至其他 DNS 服务器，导致权威 DNS 无法正确识别运营商的 LocalDNS IP，从而引发域名解析错误和流量跨网等问题。
腾讯云 HttpDNS 具有全球领先的 DNS 集群技术，可支持多运营商和自定义线路，进行优化调度。详细请参见 [移动解析 HttpDNS](https://cloud.tencent.com/document/product/379/3519)。


>?本文采用免费的 HttpDNS，为您阐述如何将 HttpDNS 调度方案用于腾讯云海外直播。免费版本 HttpDNS 接口请参见 [文档](https://cloud.tencent.com/document/product/379/3524)。 

## 上行推流使用 HttpDNS 进行调度

### 1. 请求上行接入点 IP
`http://119.29.29.29/d?dn=$push_domain.&ip=$ip` ，HTTP Get 请求，参数的含义如下：
- push_domain 代表推流域名。
- IP 字段代表请求端的外网出口 IP，这个 IP 代表最终会调度到的接入点 IP 所在的地区和运营商。


### 2. 拼接上行推流 URL
这里的 server_ip 为**请求上行接入点 IP** 中获取到的 IP，那么拼接的推流 URL 如下：
`rtmp://server_ip/live/streamname?txTime=xxx&txSecret=xxx&txHost=domain`，最重要的是在原有的推流参数中新增代表业务推流域名的字段 txHost。

## 下行播放使用 HttpDNS 进行调度

### 1. 请求下行接入点 IP
`http://119.29.29.29/d?dn=$domain.&ip=$ip`，HTTP Get 请求，参数的含义如下：
- domain 代表播放域名。
- IP 字段代表请求端的外网出口 IP，这个 IP 代表最终会调度到的接入点 IP 所在的地区和运营商。


### 2. 拼接下行播放 URL
- HTTP：包含 FLV 以及 HLS 的播放协议，这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，则 HTTP 的播放 URL 拼接如下：

```
http://server_ip/play_domain/live/streamname.flv?xxxxxxxxxx
http://server_ip/play_domain/live/ streamname.m3u8?xxxxxxxxxx
http://server_ip/play_domain/live/ streamname -123.ts?xxxxxxxxxx
```

- HTTPS：包含 FLV 以及 HLS 的播放协议，这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，HTTPS 的拼接规则依赖于播放器逻辑，**要求在 TCP 建立连接的目标 IP 为 HttpDNS 调度的 server_ip**，具体请求的播放 URL 需要是常规的播放请求：

```java
https://server_ip/play_domain/live/ streamname.flv?xxxxxxxxxx
https://server_ip/play_domain/live/ streamname.m3u8?xxxxxxxxxx
https://server_ip/play_domain/live/ streamname -123.ts?xxxxxxxxxx
```

- RTMP：这里的 server_ip 为**请求下行接入点 IP** 中获取到的 IP，play_domain 代表播放域名，则 RTMP 的播放 URL 拼接如下：

```
rtmp://server_ip/play_domain/live/ streamname?xxxxxxxxxx
```

>!以上方案均基于云直播海外的调度平台，不可完全参照在国内使用。
