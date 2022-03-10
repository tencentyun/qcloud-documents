## 功能简介
支持 HTTP/2 (HTTP 2.0) 请求，加速站点、提升 Web 性能。

#### 什么是 HTTP/2？
HTTP/2（即 HTTP 2.0，超文本传输协议第2版），是 HTTP 协议的第二个主要版本，能有效减少网络延迟，提高站点页面加载速度。


## 前提条件
仅配置 HTTPS 证书后才生效，请先配置 HTTPS 证书。


## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/teo) ，在左侧菜单栏中，单击**站点加速** > **网络优化**。
2. 在网络优化页面，选择所需站点，单击 HTTP/2 模块的![](https://qcloudimg.tencent-cloud.cn/raw/6bfbd5ffb275d58e46f69740ed95a63c.png)，开启 HTTP/2 功能。
 - 开启状态（默认）：使用 HTTP/2 加速站点。
 - 关闭状态：不支持使用 HTTP/2 加速站点。

## 注意事项
- 若客户端不支持 HTTP/2，则使用 HTTP 1.x。
- 此处仅支持请求访问，不支持 HTTP/2 回源。若需配置 HTTP/2 回源，请前往 [规则引擎]() 。
