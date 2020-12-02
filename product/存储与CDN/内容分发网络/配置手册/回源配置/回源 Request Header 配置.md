
## 配置场景

腾讯云 CDN 支持添加回源请求头部：

- 支持通过 X-Forward-For 头部携带真实客户端 IP 至源站。
- 支持通过 X-Forward-Port 头部携带真实客户端端口至源站，用于源站侧分析。
- 支持添加各类自定义头部。

也支持删除和变更自定义回源请求头部。


## 配置指南



### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可在【回源配置】中看到回源 Request Header 配置，默认情况下为关闭状态，无任何配置：
![](https://main.qcloudimg.com/raw/59069be8821b2987df5d0b3eeaae55d0.png)

### 新增规则
单击【新增回源头部规则】可配置回源 Request Header 规则：
<img src="https://main.qcloudimg.com/raw/27f604176964cc6e42aa4ac4b540d9bd.png" height="284" width="476" />

> !
> 1. 用于携带用户端真实 IP 的头部为：X-Forward-For，其值默认为 $client_ip 变量，不允许修改。
> 2. 用于携带用户端真实端口的头部为：X-Forward-Port，其值默认为 $remote_port 变量，不允许修改。

### 配置约束

- 回源 Request Header 配置规则最多可配置10条。
- 生效类型支持全部文件、文件类型、文件目录、指定文件路径四种模式，暂不支持正则匹配。
- 若用户端发起请求中已存在头部信息，生效的已配置的 Request Header 在回源时会覆盖原有头部。
- 多条规则支持调整优先级。
>!
>- 底部优先级大于顶部 - 此相对位置的优先级仅限于同类型头部操作中，例如多条增加头部规则之间、多条删除头部规则之间或多条变更头部规则之间。
>- 当不同的头部操作类型同时作用于同一个回源请求头参数的时候，按照操作类型的优先级来执行，顺序为：增加 > 删除 > 变更。例如：同时存在增加、删除和变更X-CDN头部的规则时，会先增加，再删除，最后再变更。
- 自定义头部的 Key 值长度默认为1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。
- 自定义头部的 Value 长度为1 - 1000个字符，不支持中文。
- 部分标准头部不支持自助增加/删除/变更，具体清单请参见文档 [注意事项](#noice)。






## 配置示例

若加速域名`cloud.tencent.com`的回源 Request Header 配置如下：
![](https://main.qcloudimg.com/raw/6c02e4901530e26def6b7c51c8916b36.png)
若访问资源为：`http://cloud.tencent.com/test/test.mp4`
1. 命中`*`规则，增加头部`X-Forward-For:$client_ip`头部，回源时将 $client_ip 替换为真实客户端 IP。
2. 命中`.mp4`文件类型及/test路径，因是同一头部操作类型 - 增加，则底部优先级大于顶部，因此增加`x-cdn:Tencent`头部。


<SPAN ID=noice></SPAN>
## 注意事项

以下标准头部暂时不支持增加/删除/变更回源 Request Header：

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
