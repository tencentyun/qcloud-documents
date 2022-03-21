
## 功能简介
支持自定义变更/增加/删除 HTTP 请求头（从节点向源站请求回源时的 HTTP 请求头）。
>?
>- 目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>- EdgeOne 默认支持携带 X-Forwarded-For（真实客户端 IP）和 X-Forwarded-Proto（真实客户端请求协议），您无需再配置。

## 操作指南
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需修改 HTTP 请求头规则。
>!目前仅支持匹配条件为 全部（任意请求） 或 Host 时配置修改 HTTP 请求头操作。
>
参数说明：
<table>
<thead>
<tr>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>变更</td>
<td>变更指定头部参数的取值为设置后的值<br>注意：<ul><li>若指定头部不存在，则会增加该头部</li><li>若头部已存在，则会覆盖原有头部且唯一</li></td>
</tr>
<tr>
<td>增加</td>
<td>增加指定的头部<br>注意：若头部已存在，则会覆盖原有头部且唯一</td>
</tr>
<tr>
<td>删除</td>
<td>删除指定的头部</td>
</tr>
</tbody></table>




## 注意事项

- 头部参数格式要求如下：
  - 参数名：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成
  - 参数值：1 - 1000个字符，不支持中文
- 一个修改 HTTP 请求头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：
<table>
<thead>
<tr>
<th align="left">www-authenticate</th>
<th align="left">authorization</th>
<th align="left">proxy-authenticate</th>
<th align="left">proxy-authorization</th>
</tr>
</thead>
<tbody><tr>
<td align="left">age</td>
<td align="left">cache-control</td>
<td align="left">clear-site-data</td>
<td align="left">expires</td>
</tr>
<tr>
<td align="left">pragma</td>
<td align="left">warning</td>
<td align="left">accept-ch</td>
<td align="left">accept-ch-lifetime</td>
</tr>
<tr>
<td align="left">early-data</td>
<td align="left">content-dpr</td>
<td align="left">dpr</td>
<td align="left">device-memory</td>
</tr>
<tr>
<td align="left">save-data</td>
<td align="left">viewport-width</td>
<td align="left">width</td>
<td align="left">last-modified</td>
</tr>
<tr>
<td align="left">etag</td>
<td align="left">if-match</td>
<td align="left">if-none-match</td>
<td align="left">if-modified-since</td>
</tr>
<tr>
<td align="left">if-unmodified-since</td>
<td align="left">vary</td>
<td align="left">connection</td>
<td align="left">keep-alive</td>
</tr>
<tr>
<td align="left">accept</td>
<td align="left">accept-charset</td>
<td align="left">expect</td>
<td align="left">max-forwards</td>
</tr>
<tr>
<td align="left">access-control-allow-origin</td>
<td align="left">access-control-max-age</td>
<td align="left">access-control-allow-headers</td>
<td align="left">access-control-allow-methods</td>
</tr>
<tr>
<td align="left">access-control-expose-headers</td>
<td align="left">access-control-allow-credentials</td>
<td align="left">access-control-request-headers</td>
<td align="left">access-control-request-method</td>
</tr>
<tr>
<td align="left">origin</td>
<td align="left">timing-allow-origin</td>
<td align="left">dnt</td>
<td align="left">tk</td>
</tr>
<tr>
<td align="left">content-disposition</td>
<td align="left">content-length</td>
<td align="left">content-type</td>
<td align="left">content-encoding</td>
</tr>
<tr>
<td align="left">content-language</td>
<td align="left">content-location</td>
<td align="left">forwarded</td>
<td align="left">x-forwarded-host</td>
</tr>
<tr>
<td align="left">x-forwarded-proto</td>
<td align="left">via</td>
<td align="left">from</td>
<td align="left">host</td>
</tr>
<tr>
<td align="left">referer-policy</td>
<td align="left">allow</td>
<td align="left">server</td>
<td align="left">accept-ranges</td>
</tr>
<tr>
<td align="left">range</td>
<td align="left">if-range</td>
<td align="left">content-range</td>
<td align="left">cross-origin-embedder-policy</td>
</tr>
<tr>
<td align="left">cross-origin-opener-policy</td>
<td align="left">cross-origin-resource-policy</td>
<td align="left">content-security-policy</td>
<td align="left">content-security-policy-report-only</td>
</tr>
<tr>
<td align="left">expect-ct</td>
<td align="left">feature-policy</td>
<td align="left">strict-transport-security</td>
<td align="left">upgrade-insecure-requests</td>
</tr>
<tr>
<td align="left">x-content-type-options</td>
<td align="left">x-download-options</td>
<td align="left">x-frame-options(xfo)</td>
<td align="left">x-permitted-cross-domain-policies</td>
</tr>
<tr>
<td align="left">x-powered-by</td>
<td align="left">x-xss-protection</td>
<td align="left">public-key-pins</td>
<td align="left">public-key-pins-report-only</td>
</tr>
<tr>
<td align="left">sec-fetch-site</td>
<td align="left">sec-fetch-mode</td>
<td align="left">sec-fetch-user</td>
<td align="left">sec-fetch-dest</td>
</tr>
<tr>
<td align="left">last-event-id</td>
<td align="left">nel</td>
<td align="left">ping-from</td>
<td align="left">ping-to</td>
</tr>
<tr>
<td align="left">report-to</td>
<td align="left">transfer-encoding</td>
<td align="left">te</td>
<td align="left">trailer</td>
</tr>
<tr>
<td align="left">sec-websocket-key</td>
<td align="left">sec-websocket-extensions</td>
<td align="left">sec-websocket-accept</td>
<td align="left">sec-websocket-protocol</td>
</tr>
<tr>
<td align="left">sec-websocket-version</td>
<td align="left">accept-push-policy</td>
<td align="left">accept-signature</td>
<td align="left">alt-svc</td>
</tr>
<tr>
<td align="left">date</td>
<td align="left">large-allocation</td>
<td align="left">link</td>
<td align="left">push-policy</td>
</tr>
<tr>
<td align="left">retry-after</td>
<td align="left">signature</td>
<td align="left">signed-headers</td>
<td align="left">server-timing</td>
</tr>
<tr>
<td align="left">service-worker-allowed</td>
<td align="left">sourcemap</td>
<td align="left">upgrade</td>
<td align="left">x-dns-prefetch-control</td>
</tr>
<tr>
<td align="left">x-firefox-spdy</td>
<td align="left">x-pingback</td>
<td align="left">x-requested-with</td>
<td align="left">x-robots-tag</td>
</tr>
<tr>
<td align="left">x-ua-compatible</td>
<td align="left">max-age</td>
<td align="left"></td>
<td align="left"></td>
</tr>
</tbody></table>
