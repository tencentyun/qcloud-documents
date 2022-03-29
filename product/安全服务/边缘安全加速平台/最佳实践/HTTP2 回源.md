## 功能简介

支持以 HTTP/2 协议请求回源。

#### 什么是 HTTP/2？
HTTP/2（即 HTTP 2.0，超文本传输协议第2版），是 HTTP 协议的第二个主要版本，能有效减少网络延迟，提高站点页面加载速度。

## 操作步骤

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需配置 HTTP/2 回源规则。
>!目前仅支持匹配条件为 Host 时配置修改 HTTP/2 回源操作。
>
参数说明：
<table>
<thead>
<tr>
<th>开关</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>开启</td>
<td>支持以 HTTP/2 协议请求回源<br>注意：仅源站服务器支持 HTTPS 协议回源才生效</td>
</tr>
<tr>
<td>关闭</td>
<td>不支持以 HTTP/2 协议请求回源</td>
</tr>
</tbody></table>
