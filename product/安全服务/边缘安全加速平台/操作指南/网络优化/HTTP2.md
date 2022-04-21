## 功能简介
支持 HTTP/2 (HTTP 2.0) 请求，加速站点、提升 Web 性能。

#### 什么是 HTTP/2？
HTTP/2（即 HTTP 2.0，超文本传输协议第2版），是 HTTP 协议的第二个主要版本，能有效减少网络延迟，提高站点页面加载速度。


## 前提条件
- 仅配置 HTTPS 证书后才生效，请先配置 HTTPS 证书。
- 目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。



## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **网络优化**。
2. 在网络优化页面，选择所需站点，单击 HTTP/2 模块的“开关”，开启或关闭 HTTP/2 功能。
![](https://qcloudimg.tencent-cloud.cn/raw/243e5a84cb494e9b049ab3615d688055.png)
**参数说明：**
 - 开启状态（默认）：使用 HTTP/2 加速站点。
>! 仅配置 HTTPS 证书后才生效，请先配置 HTTPS 证书。
>
 - 关闭状态：不支持使用 HTTP/2 加速站点。

## 注意事项
1. 若客户端不支持 HTTP/2，则使用 HTTP 1.x。
2. 此处仅支持访问请求，不支持 HTTP/2 回源。若需配置 HTTP/2 回源，请前往 [规则引擎](https://cloud.tencent.com/document/product/1552/70901) 。
