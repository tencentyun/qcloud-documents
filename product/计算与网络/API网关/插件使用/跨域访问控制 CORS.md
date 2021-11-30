## 操作场景

跨域资源共享（Cross-Origin Resource Sharing，CORS）是W3C的标准。CORS 允许 Web 应用服务器进行跨域访问控制，从而使跨域数据传输得以安全进行。目前API 网关支持对 CORS 规则的配置，从而根据需求允许或者拒绝相应的跨域请求。

当 API 网关的默认跨域配置不能满足您的需求时，您可通过跨域访问控制插件设置自定义的复杂跨域规则，并绑定到 API 生效。

## 操作步骤[](id:steps)

### 步骤1：创建插件

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏，单击【插件】，进入插件列表页。
3. 单击页面左上角的【新建】，选择插件类型为【跨域访问控制】，新建一个跨域访问控制插件。

| 参数           | 是否必填 | 说明                                                         |
| -------------- | -------- | ------------------------------------------------------------ |
| 来源 Origin    | 必填     | 允许跨域请求的来源；<br>可以同时指定多个来源，多个来源间用英文逗号分隔；<br>配置支持`*`，表示全部域名都允许；<br>注意不要遗漏协议名 http 或 https，若端口不是默认的80，还需要带上端口。 |
| 操作 Method    | 必填     | 支持 GET、PUT、POST、DELETE、HEAD。枚举允许一个或多个跨域请求方法。 |
| Allow-Headers  | 选填     | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部；<br>可以同时指定多个 Headers，Header 间用英文逗号分隔；<br>配置支持`*`，表示全部 Header 都允许；<br>不填时代表空，即全部 Header 都禁止。 |
| Expose-Headers | 选填     | 允许暴露给XMLHttpRequest对象的头；<br>可以同时指定多个 Headers，Header 间用英文逗号分隔；<br>配置支持`*`，表示全部 Header 都允许；<br>不填时代表空，即全部 Header 都禁止。 |
| 允许 Cookie    | 选填     | 是否允许 Cookie。                                              |
| 超时 Max-Age   | 必填     | 设置 OPTIONS 请求得到结果的有效期（秒）。数值必须为正整数，例如600。 |

![](https://main.qcloudimg.com/raw/b3f2573e0f935082099ed195a67c3dcf.png)

### 步骤2：绑定 API 并生效

1. 在列表中选中刚刚创建好的插件，点击操作列的【绑定API】。
2. 在绑定 API 弹窗中选择服务和环境，并选择需要绑定插件的 API。
   ![](https://main.qcloudimg.com/raw/d7fd3c3539d6f623f45ebfdf0674d97e.png)
3. 单击【确定】，即可将插件绑定到 API，此时插件的配置已经对 API 生效。

## 注意事项

目前 API 网关中有两个地方可以设置跨域访问控制规则：

- 创建 API - 前端配置 - 支持 CORS：在创建 API 时打开“支持CORS”配置项，开启后 API 网关将默认在响应头中添加 `Access-Control-Allow-Origin : *`。
- 本文所描述的“跨域访问控制”插件：参考 [操作步骤](#steps)。

“跨域访问控制“插件的优先级高于”支持CORS“配置项，当跨域访问控制插件绑定到某一API时，该 API 的“支持CORS”配置项将不生效。
