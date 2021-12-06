## 功能介绍

腾讯云 CDN 默认支持携带一些头部回源，也支持自定义配置回源 HTTP 请求头部，供您统计和分析源站业务状况。

>!
>- 腾讯云 CDN 默认支持携带 X-Forwarded-For（真实客户端 IP）和 X-Forwarded-Proto（真实客户端请求协议），您无需再配置。
>- 若您已对全部文件配置增加头部 X-Forward-For，建议您删除该规则，使用默认的标准头部 X-Forwarded-For 即可**（请注意此处头部参数的名称变化）**。

## 操作指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可在【回源配置】中看到回源 HTTP 请求头配置，默认情况下为关闭状态，无任何配置：
![](https://qcloudimg.tencent-cloud.cn/raw/74c6b1b281a8e72476d27a2a092f632e.png)

### 操作类型

| 操作类型 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 设置     | 变更指定请求头部参数的取值为设置后的值。<br/>若设置的头部不存在，则会增加该头部。<br/>若回源请求头部参数已存在，则设置的请求头会覆盖原有头部且唯一。 |
| 增加     | 增加指定的回源请求头部参数。<br/>若设置的头部已存在，则增加的请求头会覆盖原有头部且唯一。 |
| 删除     | 删除指定的请求头参数。                                       |

>!
> - 底部优先级大于顶部 - 此相对位置的优先级仅限于同类型头部操作中，例如多条增加头部规则之间、多条删除头部规则之间或多条设置头部规则之间。
> - 当不同的头部操作类型同时作用于同一个回源请求头参数的时候，按照操作类型的优先级来执行，顺序为：增加 > 删除 > 设置。例如：同时存在增加、删除和设置X-CDN头部的规则时，会先增加，再删除，最后再设置。

### 头部参数

| 头部参数       | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| X-Forward-Port | 用于携带用户端真实端口的头部。其值默认为 $remote_port 变量，不允许修改。 |
| 自定义头部     | 自定义头部的Key 值长度默认为1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。<br>Value 长度为1 - 1000个字符，不支持中文。<br>部分标准头部不支持自助设置/增加/删除，具体清单请参见文档 [注意事项](#noice)。 |

> !
> - 回源 HTTP 请求头配置规则最多可配置10条。
> - 生效类型支持全部文件、文件类型、文件目录、指定文件路径四种模式，暂不支持正则匹配。



## 配置示例

若加速域名 `cloud.tencent.com` 的回源 HTTP 请求头配置如下：
![](https://main.qcloudimg.com/raw/cd018a8767ffdbd57862db197af48141.png)
若访问资源为：`http://cloud.tencent.com/test/test.mp4`

命中 `mp4` 文件后缀及/test路径，因是同一头部操作类型 - 增加，则底部优先级大于顶部，因此增加 `x-cdn:Tencent` 头部。

## 注意事项[](id:noice)

以下标准头部暂时不支持设置/增加/删除回源 HTTP 请求头：

| www-authenticate              | authorization                    | proxy-authenticate             | proxy-authorization                 |
| ----------------------------- | -------------------------------- | ------------------------------ | ----------------------------------- |
| age                           | cache-control                    | clear-site-data                | expires                             |
| pragma                        | warning                          | accept-ch                      | accept-ch-lifetime                  |
| early-data                    | content-dpr                      | dpr                            | device-memory                       |
| save-data                     | viewport-width                   | width                          | last-modified                       |
| etag                          | if-match                         | if-none-match                  | if-modified-since                   |
| if-unmodified-since           | vary                             | connection                     | keep-alive                          |
| accept                        | accept-charset                   | expect                         | max-forwards                        |
| access-control-allow-origin   | access-control-max-age           | access-control-allow-headers   | access-control-allow-methods        |
| access-control-expose-headers | access-control-allow-credentials | access-control-request-headers | access-control-request-method       |
| origin                        | timing-allow-origin              | dnt                            | tk                                  |
| content-disposition           | content-length                   | content-type                   | content-encoding                    |
| content-language              | content-location                 | forwarded                      | x-forwarded-host                    |
| x-forwarded-proto             | via                              | from                           | host                                |
| referer-policy                | allow                            | server                         | accept-ranges                       |
| range                         | if-range                         | content-range                  | cross-origin-embedder-policy        |
| cross-origin-opener-policy    | cross-origin-resource-policy     | content-security-policy        | content-security-policy-report-only |
| expect-ct                     | feature-policy                   | strict-transport-security      | upgrade-insecure-requests           |
| x-content-type-options        | x-download-options               | x-frame-options(xfo)           | x-permitted-cross-domain-policies   |
| x-powered-by                  | x-xss-protection                 | public-key-pins                | public-key-pins-report-only         |
| sec-fetch-site                | sec-fetch-mode                   | sec-fetch-user                 | sec-fetch-dest                      |
| last-event-id                 | nel                              | ping-from                      | ping-to                             |
| report-to                     | transfer-encoding                | te                             | trailer                             |
| sec-websocket-key             | sec-websocket-extensions         | sec-websocket-accept           | sec-websocket-protocol              |
| sec-websocket-version         | accept-push-policy               | accept-signature               | alt-svc                             |
| date                          | large-allocation                 | link                           | push-policy                         |
| retry-after                   | signature                        | signed-headers                 | server-timing                       |
| service-worker-allowed        | sourcemap                        | upgrade                        | x-dns-prefetch-control              |
| x-firefox-spdy                | x-pingback                       | x-requested-with               | x-robots-tag                        |
| x-ua-compatible               | max-age                          |                                |                                     |
