
## 配置场景

腾讯云 CDN 支持添加回源请求头部：

- 支持通过 X-Forward-For 头部携带真实客户端 IP 至源站。
- 支持通过 X-Forward-Port 头部携带真实客户端端口至源站，用于源站侧分析。
- 支持添加各类自定义头部。

## 配置指南

### 配置约束

- 自定义请求头部配置规则最多可配置10条。
- 生效类型支持全部文件、文件类型、文件目录、指定文件路径四种模式，暂不支持正则匹配。
- 若用户端发起请求中已存在头部信息，配置的 Request Header 在回源时会覆盖原有头部。
- 多条规则头部设置重复时，优先级为从上到下从低到高，底部优先级高于顶部。
- 自定义头部的 Key 值长度默认为1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。
- 自定义头部的 Value 长度为1 - 1000个字符，不支持中文。
- 部分标准头部不支持自助添加，具体清单请看文档最后部分说明。

### 配置说明

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可在【回源配置】中看到回源 Request Header 配置，默认情况下为关闭状态，无任何配置：
![](https://main.qcloudimg.com/raw/253c67e926455bd17f2cda79fa46d2ba.png)
关闭状态下，可新增回源头部规则：
![](https://main.qcloudimg.com/raw/895adcd7cebdb0d75bbde1c22244a2a5.png)

> !
> 1. 用于携带用户端真实 IP 的头部为：X-Forward-For，其值默认为 $client_ip 变量，不允许修改。
> 2. 用于携带用户端真实端口的头部为：X-Forward-Port，其值默认为 $remote_port 变量，不允许修改。

规则添加完毕后，此时整体配置为关闭状态，不会生效：
![](https://main.qcloudimg.com/raw/6d66d2ae51509aa787409ad4d0f301e1.png)
可通过【调整优先级】按钮，调整规则上下顺序，如需发布至全网 CDN 节点，单击上方配置开关即可：
![](https://main.qcloudimg.com/raw/f984682c540bdd219c85a3dd3e51d7ca.png)

## 配置示例

若加速域名`cloud.tencent.com`的回源 Request Header 配置如下：
![](https://main.qcloudimg.com/raw/18b181e351aaf4a176ebcb9656921986.png)
若访问资源为：`http://cloud.tencent.com/test/test.mp4`
1. 命中`*`规则，增加头部`X-Forward-For:$client_ip`头部，回源时将 $client_ip 替换为真实客户端 IP。
2. 命中`.mp4`文件类型及`/test`路径，底部优先级大于顶部优先级，因此增加`x-cdn:Tencent`头部。

## 注意事项

以下标准头部暂时不支持添加回源 Request Header：

<table>
<tbody><tr>
<td>www-authenticate</td>
<td>authorization</td>
<td>proxy-authenticate</td>
<td>proxy-authorization</td>
</tr>
<tr>
<td>age</td>
<td>cache-control</td>
<td>clear-site-data</td>
<td>expires</td>
</tr>
<tr>
<td>pragma</td>
<td>warning</td>
<td>accept-ch</td>
<td>accept-ch-lifetime</td>
</tr>
<tr>
<td>early-data</td>
<td>content-dpr</td>
<td>dpr</td>
<td>device-memory</td>
</tr>
<tr>
<td>save-data</td>
<td>viewport-width</td>
<td>width</td>
<td>last-modified</td>
</tr>
<tr>
<td>etag</td>
<td>if-match</td>
<td>if-none-match</td>
<td>if-modified-since</td>
</tr>
<tr>
<td>if-unmodified-since</td>
<td>vary</td>
<td>connection</td>
<td>keep-alive</td>
</tr>
<tr>
<td>accept</td>
<td>accept-charset</td>
<td>expect</td>
<td>max-forwards</td>
</tr>
<tr>
<td>access-control-allow-origin</td>
<td>access-control-max-age</td>
<td>access-control-allow-headers</td>
<td>access-control-allow-methods</td>
</tr>
<tr>
<td>access-control-expose-headers</td>
<td>access-control-allow-credentials</td>
<td>access-control-request-headers</td>
<td>access-control-request-method</td>
</tr>
<tr>
<td>origin</td>
<td>timing-allow-origin</td>
<td>dnt</td>
<td>tk</td>
</tr>
<tr>
<td>content-disposition</td>
<td>content-length</td>
<td>content-type</td>
<td>content-encoding</td>
</tr>
<tr>
<td>content-language</td>
<td>content-location</td>
<td>forwarded</td>
<td>x-forwarded-host</td>
</tr>
<tr>
<td>x-forwarded-proto</td>
<td>via</td>
<td>from</td>
<td>host</td>
</tr>
<tr>
<td>referer</td>
<td>referer-policy</td>
<td>allow</td>
<td>server</td>
</tr>
<tr>
<td>accept-ranges</td>
<td>range</td>
<td>if-range</td>
<td>content-range</td>
</tr>
<tr>
<td>cross-origin-embedder-policy</td>
<td>cross-origin-opener-policy</td>
<td>cross-origin-resource-policy</td>
<td>content-security-policy</td>
</tr>
<tr>
<td>content-security-policy-report-only</td>
<td>expect-ct</td>
<td>feature-policy</td>
<td>strict-transport-security</td>
</tr>
<tr>
<td>upgrade-insecure-requests</td>
<td>x-content-type-options</td>
<td>x-download-options</td>
<td>x-frame-options(xfo)</td>
</tr>
<tr>
<td>x-permitted-cross-domain-policies</td>
<td>x-powered-by</td>
<td>x-xss-protection</td>
<td>public-key-pins</td>
</tr>
<tr>
<td>public-key-pins-report-only</td>
<td>sec-fetch-site</td>
<td>sec-fetch-mode</td>
<td>sec-fetch-user</td>
</tr>
<tr>
<td>sec-fetch-dest</td>
<td>last-event-id</td>
<td>nel</td>
<td>ping-from</td>
</tr>
<tr>
<td>ping-to</td>
<td>report-to</td>
<td>transfer-encoding</td>
<td>te</td>
</tr>
<tr>
<td>trailer</td>
<td>sec-websocket-key</td>
<td>sec-websocket-extensions</td>
<td>sec-websocket-accept</td>
</tr>
<tr>
<td>sec-websocket-protocol</td>
<td>sec-websocket-version</td>
<td>accept-push-policy</td>
<td>accept-signature</td>
</tr>
<tr>
<td>alt-svc</td>
<td>date</td>
<td>large-allocation</td>
<td>link</td>
</tr>
<tr>
<td>push-policy</td>
<td>retry-after</td>
<td>signature</td>
<td>signed-headers</td>
</tr>
<tr>
<td>server-timing</td>
<td>service-worker-allowed</td>
<td>sourcemap</td>
<td>upgrade</td>
</tr>
<tr>
<td>x-dns-prefetch-control</td>
<td>x-firefox-spdy</td>
<td>x-pingback</td>
<td>x-requested-with</td>
</tr>
<tr>
<td>x-robots-tag</td>
<td>x-ua-compatible</td>
<td>max-age</td>
<td></td>
</tr>
</tbody></table>
