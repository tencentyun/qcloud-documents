## 新增 HTTP/HTTPS 监听器

1. 登录 [全球应用加速控制台](https://console.cloud.tencent.com/gaap)，进入“接入管理”页面，单击指定通道的**ID/通道名**。
2. 进入到下一级页面，选择 **HTTP/HTTPS 监听器管理** > **新增**，可选的协议有 HTTP 和 HTTPS（备注：IPv6 通道当前不支持 HTTP/HTTPS 监听器配置）。
3. 具体配置如下：
   1. 当选中 HTTP 时，仅需要输入监听端口即可，监听器会默认按照 HTTP 协议进行转发。
![](https://qcloudimg.tencent-cloud.cn/raw/29beac16f44c6b19468afec179760a90.png)
   2. 当选中 HTTPS 时，则需要额外配置证书和其他信息，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/fe628f0b60eb3934793220060f42ef61.png)
      - “监听器与源站之间使用 HTTP 协议”，指客户端到加速通道 VIP 之间使用 HTTPS 协议，而 VIP 到源站之间使用 HTTP 协议，需要源站开通HTTP协议端口；
        “监听器与源站之间使用 HTTPS 协议”，指客户端到源站之间全程使用 HTTPS 协议，需要源站开通 HTTPS 协议端口。
      - SSL 解析方式：支持单项认证、双向认证。
      - 服务器证书/客户端证书：需要在全球应用加速控制台的**证书管理**上传/更新，然后在新建/修改 HTTPS 监听器时从下拉列表中选择对应的证书，详见 [证书管理](https://cloud.tencent.com/document/product/608/60757)。

## 设置HTTP/HTTPS 监听器

单击**HTTP/HTTPS 监听器管理**标签页，在操作栏单击**设置规则**，可以进入下一级页面，进行域名和 URL 管理。

### 添加域名

为HTTP监听器添加域名只需直接输入域名即可，但须符合域名格式要求，且只支持精确匹配。监听器支持的字符集有：`a-z、0-9、_、.、–，长度3 - 80`。
 ![](https://main.qcloudimg.com/raw/057018c56c9219eed61d88fd3571122e.png)
为 HTTPS 监听器添加域名需输入域名并选择对应服务器证书，控制台默认使用创建监听器时选择的证书。如您在此处重新上传证书，则该域名将使用新证书进行认证。
 ![](https://main.qcloudimg.com/raw/053f63208b9a080d607dea634e23fdcd.png)

### 添加规则

完成“添加域名”操作后，单击**添加规则**，可以添加对应URL及选择源站类型。同一个域名下可以添加最多20条 URL 规则，具体如下：

1. 基本配置：
   ![](https://main.qcloudimg.com/raw/d42c66a8f2d208221546690bcd71ce96.png)
   - URL：支持字符集如下，`a-z、A-Z、0-9、_ 、.、- 、/，长度1 - 80`。
   - 源站类型：支持 IP 和域名两种类型，但同一个监听器只支持一种类型。 
2. 源站处理策略：
   设置源站的转发处理规则，即在同一个监听器绑定多个源站的情况下，选择源站之间的调度策略。
    ![](https://main.qcloudimg.com/raw/fcd51cf3681b1c464e29392ff8262d51.png)
   - 轮询：多个源站按轮询策略回源。
   - 轮询加权：多个源站按权重比例回源（源站类型为域名时不支持配置）。
   - 最小连接数：在所有源站中选择连接数最小的源站优先进行调度。
3. 源站健康检查机制：
   您可以选择针对当前域名启用监控检查机制。可以设置独立的检查 URL，请求方式可以支持HEAD及GET，检查状态码可支持 http_1xx，http_2xx，http_3xx，http_4xx，http_5xx，状态码可单选也可多选，即当检测到指定的状态码时，监听器认为后端源站属于正常状态。如果未检测到任何状态码时，监听器认为后端源站异常。
![](https://qcloudimg.tencent-cloud.cn/raw/2ef77eccf69b650bdf07f681f2a96cc7.png)

### 修改域名

完成“添加域名”操作后，单击**修改域名**，可以对域名进行修改。
 ![](https://main.qcloudimg.com/raw/cc48fd7ecebbb3c0fb9a3ec5a9314611.png)

### 删除域名

完成“添加域名”操作后，单击**删除**可删除域名。如果域名下已有规则绑定源站，则需要勾选“强制删除绑定有源站的规则”。
 ![](https://main.qcloudimg.com/raw/c2600b0ffaf0195dc55302e476322384.png)

### 修改规则

参考上文添加规则，主要差别在于域名和源站类型无法修改。

### 绑定源站

详情请参见绑定源站，可以对不同源站绑定不同的端口。有关“覆盖端口”及“补齐端口”功能，请参见TCP/UDP 监听器源站绑定。

> ! 一个规则绑定的源站总数最多为100个。

### 删除规则

完成“添加规则”操作后，单击**删除**可删除规则，如果规则下有绑定的源站，需要先勾选“强制删除绑定有源站的规则”。
 ![](https://main.qcloudimg.com/raw/721de157fd96d88b56b60bb3dbed80dc.png)

### 配置回源请求头

1. 完成“添加规则”操作后，在规则的操作栏选择**更多**，单击**配置回源请求头**
   ![](https://main.qcloudimg.com/raw/9bf54d20a31f34222875d8acf2e68640.png)
2. 单击**新增参数**，添加请求头的名称参数及取值；如需要携带用户真实IP的头部，其变量值为$remote_addr（默认已经有X-Forwarded-For头部携带客户IP回源），当前仅支持变量$remote_addr，其余带$变量暂未不支持。

> !
> 1. HTTP头部的名称Key值长度默认为1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 - _ : 空格 组成。Value 长度为1 - 100个字符，不支持中文，除了 $remote_addr之外， 不支持配置的文案地方出现 $ 字符；
> 2. 每条规则最多可配置10条回源 HTTP 请求头；
> 3. 部分标准头部不支持自助设置/增加/删除，具体清单请参见以下列表。

<table>
    <tr>
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
        <td>referer-policy</td>
        <td>allow</td>
        <td>server</td>
        <td>accept-ranges</td>
    </tr>
    <tr>
        <td>range</td>
        <td>if-range</td>
        <td>content-range</td>
        <td>cross-origin-embedder-policy</td>
    </tr>
    <tr>
        <td>cross-origin-opener-policy</td>
        <td>cross-origin-resource-policy</td>
        <td>content-security-policy</td>
        <td>content-security-policy-report-only</td>
    </tr>
    <tr>
        <td>expect-ct</td>
        <td>feature-policy</td>
        <td>strict-transport-security</td>
        <td>upgrade-insecure-requests</td>
    </tr>
    <tr>
        <td>x-content-type-options</td>
        <td>x-download-options</td>
        <td>x-frame-options(xfo)</td>
        <td>x-permitted-cross-domain-policies</td>
    </tr>
    <tr>
        <td>x-powered-by</td>
        <td>x-xss-protection</td>
        <td>public-key-pins</td>
        <td>public-key-pins-report-only</td>
    </tr>
    <tr>
        <td>sec-fetch-site</td>
        <td>sec-fetch-mode</td>
        <td>sec-fetch-user</td>
        <td>sec-fetch-dest</td>
    </tr>
    <tr>
        <td>last-event-id</td>
        <td>nel</td>
        <td>ping-from</td>
        <td>ping-to</td>
    </tr>
    <tr>
        <td>report-to</td>
        <td>transfer-encoding</td>
        <td>te</td>
        <td>trailer</td>
    </tr>
    <tr>
        <td>sec-websocket-key</td>
        <td>sec-websocket-extensions</td>
        <td>sec-websocket-accept</td>
        <td>sec-websocket-protocol</td>
    </tr>
    <tr>
        <td>sec-websocket-version</td>
        <td>accept-push-policy</td>
        <td>accept-signature</td>
        <td>alt-svc</td>
    </tr>
    <tr>
        <td>date</td>
        <td>large-allocation</td>
        <td>link</td>
        <td>push-policy</td>
    </tr>
    <tr>
        <td>retry-after</td>
        <td>signature</td>
        <td>signed-headers</td>
        <td>server-timing</td>
    </tr>
    <tr>
        <td>service-worker-allowed</td>
        <td>sourcemap</td>
        <td>upgrade</td>
        <td>x-dns-prefetch-control</td>
    </tr>
    <tr>
        <td>x-firefox-spdy</td>
        <td>x-pingback</td>
        <td>x-requested-with</td>
        <td>x-robots-tag</td>
    </tr>
    <tr>
        <td>x-ua-compatible</td>
        <td>max-age</td>
        <td></td>
        <td></td>
    </tr>
</table>

## 删除HTTP/HTTPS 监听器

单击**HTTP/HTTPS 监听器管理**标签页，在操作栏单击**删除**，可以删除指定的监听器，若监听器已绑定源站，则需要选中“允许强制删除绑定有源站的监听器”后，才能删除。删除后，该监听器的端口将停止加速。
 ![](https://main.qcloudimg.com/raw/2fc06509c4687838c077f3e0fac210c2.png)
