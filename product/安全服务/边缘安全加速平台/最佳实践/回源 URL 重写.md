## 功能简介

将从节点向源站发起回源请求时的 回源 URL 重写到目标 URL，不影响节点的缓存标识（Cache Key）。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需配置回源 URL 重写规则。
>!目前仅支持匹配条件为 URL path 或 Host And URL path 时配置回源 URL 重写操作。
>
参数说明：
<table>
<thead>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>目标 URL</td>
<td>希望重写的目标 URL，例如：<code>www.example.com/images/foo.jpg</code> 或 <code>www.example.com/foo/bar</code></td>
</tr>
</tbody></table>

