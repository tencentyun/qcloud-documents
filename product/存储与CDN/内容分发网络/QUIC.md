<blockquote class="d-mod-alarm">
<div class="d-mod-title d-alarm-title">
<i class="d-icon-alarm"></i>公告：
</div>
<p>关于腾讯云 CDN 将于2022年1月5日正式发布 QUIC 访问功能及计费的周知<br>腾讯云内容分发网络 CDN 将于2022年1月5日正式发布 QUIC 访问功能。CDN 届时将增加增值服务计费项 - 按 QUIC 请求数次数计费。<li>当您启用 QUIC 访问功能后， 产生的 QUIC 请求数将按量后付费，默认按小时结算。详见 计费说明。</li><li>若您已使用或即将使用 QUIC 访问功能，请您关注确认，谢谢！</li></p>
</blockquote>



## 功能介绍

QUIC (Quick UDP Internet Connections) 是一个通用的网络协议，能够保障网络安全性，同时减少传输和连接时的延时，避免网络拥塞。当前腾讯云 CDN 默认支持 h3 Draft 28, h3-Q050, h3-Q046, h3-Q043, Q046, Q043 版本。

您可开启 QUIC 访问，保障客户端访问 CDN 节点时数据传输的安全性，提升访问效率。

## 内测时间

腾讯云 CDN 已于 **2021-08-31 23:59:59** 结束 QUIC 访问 内测申请，感谢您的参与！请关注等待后续正式发布。

## 内测指南

若您通过了内测审核，则可以在控制台上为新添域名开启 QUIC 平台，进行测试：

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，新添域名时，您可通过选中 QUIC 平台项，为域名接入 QUIC 平台：
![](https://qcloudimg.tencent-cloud.cn/raw/307971b5c4f53bc07e9d75d8926dd6ba.png)

2. 成功添加域名后，可进入域名管理，切换 Tab 至 **HTTPS 配置**，即可找到 **QUIC** 配置：默认为关闭状态，您可自助开启。
   **注：**开启前请先配置 HTTPS 证书。
![](https://qcloudimg.tencent-cloud.cn/raw/8cdd0d82eea3652f8639f727b78fbe14.png)

>!
>- 通过内测后，仅支持对新添加域名开启 QUIC 平台，不支持存量已添加的域名。
>- QUIC 平台现为测试平台，尚未全量，建议您仅对测试域名开启 QUIC 平台，不要使用业务域名。
>- 业务类型切换涉及资源平台调度，接入 QUIC 平台后，建议您不要再切换域名的业务类型。
>- 当前不支持 QUIC 回源。

## 配置约束

- 音视频点播业务类型的域名暂不支持 QUIC。
- 域名开启 IPv6 访问后不可开启 QUIC。

## 计费规则

- QUIC 访问增值服务将按 QUIC 请求数次数计费，按量后付费，详细说明请见 [计费说明](https://cloud.tencent.com/document/product/228/2949#m8)。**后续进行线上计费时，我们会提前推送消息以及在控制台和文档发布公告周知，请您关注确认。**
- 收到计费提示消息和公告后，您仍可管理 QUIC 访问功能：
  - 若您通过官网内测申请使用：请自行于控制台管理 QUIC 访问功能。
  - 若您通过后端配置开启了 QUIC，则也属于使用了 QUIC 访问功能，CDN 侧会正常统计对应的 QUIC 数据：请联系您的售后人员。
