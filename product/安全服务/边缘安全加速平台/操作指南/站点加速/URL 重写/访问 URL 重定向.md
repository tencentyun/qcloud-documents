## 功能简介
节点通过响应特定状态码将客户端请求 URL 重定向到目标 URL。

## 适用场景
将您业务场景中原先需要源站生成并返回的 URL 重定向，改为直接由 EdgeOne 边缘节点构造并且返回，减少回源的网络延时和源站生成 URL 重定向的负载，提升客户端访问性能。

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置访问 URL 重定向规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
配置项说明：
<table>
<thead>
<tr>
<th align="left">配置项</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">目标 URL</td>
<td align="left">希望重定向的目标 URL，例如：<code>https://www.example.com/images/foo.jpg</code> 或 <code>https://www.example.com/foo/bar</code></td>
</tr>
<tr>
<td align="left">携带查询参数</td>
<td align="left">是否携带原查询参数至目标 URL ，默认会携带</td>
</tr>
<tr>
<td align="left">状态码</td>
<td align="left">选择重定向的响应状态码：<ul><li>302（默认）</li><li>301</li><li>303</li><li>307</li></ul></td>
</tr>
</tbody></table>

## 配置示例

若请求 URL `https://www.example.com/path/foo.html` 的访问 URL 重定向配置如下：

![](https://qcloudimg.tencent-cloud.cn/raw/f6fc8e8bdfc23f2e945bd060f759ba9a.png)

则客户端请求：`https://www.example.com/path/foo.html?key1=value1`，则节点响应 301 重定向至`https://www.example.com/newpath/bar.html`。
