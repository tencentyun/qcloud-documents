## 简介

跨域访问即通过 HTTP 请求，从一个域去请求另一个域的资源。只要协议、域名、端口有任何一个不同，都会被当作是不同的域。

对象存储服务针对跨域访问，支持响应 OPTIONS 请求 ，并根据开发者设定的规则向浏览器返回具体设置的规则。但服务端并不会校验随后发起的跨域请求是否符合规则。

更多详细资料请参阅 [Mozilla Developer Network 关于 HTTP 访问控制的说明](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)。

## 设置说明

### Allow-Origin

允许跨域请求的来源。

- 可以同时指定多个来源,每行只能填写一个。
- 配置支持`*`，表示全部域名都允许，不推荐。
- 支持单个具体域名，形如 `http://www.abc.com`。
- 支持二级泛域名，形如`http://*.abc.com` ,但是每行只能有一个`*`号。
- 注意不要遗漏协议名 http 或 https，若端口不是默认的 80，还需要带上端口。

### Allow-Methods

枚举允许的跨域请求方法（一个或者多个）。
例如：GET、PUT、POST、DELETE、HEAD。

### Allow-Header

在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部。 例如：x-cos-meta-md5

- 可以同时指定多个来源,每行只能填写一个。
- Header 容易遗漏，没有特殊需求的情况下，建议设置为 * ，表示允许所有。
- 大小写不敏感。
- 在 Access-Control-Request-Headers 中指定的每个 Header，都必须在 Allowed-Header 中有对应项。

### Expose-Headers

- 具体的配置需要根据应用的需求确定，默认推荐填写 Etag。
- 不允许使用通配符，大小写不敏感，每行只能填写一个。

### Max-Age

设置 OPTIONS 请求得到结果的有效期。
例如：`600`

## 设置步骤

控制台提供了响应 OPTIONS 请求的配置，支持多条规则。

1. 登录 [对象存储桶控制台](https://console.cloud.tencent.com/cos4/index)，选择左侧菜单栏【 Bucket 列表】，进入 Bucket 列表页面。单击需要配置回源的存储桶（如 example），进入存储桶。
   ![访问权限1](//mc.qcloudimg.com/static/img/b51d5a77d53c3416324ea3eb283c788c/image.png)
2. 单击【基础配置】，进入存储桶的基础配置页，找到跨域访问 CORS 设置，单击【编辑】进入可编辑状态。
   ![跨域访问1](//mc.qcloudimg.com/static/img/bed8cadfb4bc6b9f0571227844d8cd32/image.png)
3. 修改当前状态为开启，单击【+ 新增规则】或【修改】进入编辑规则的弹窗。
   ![跨域访问2](//mc.qcloudimg.com/static/img/6fc0d7edf0729c326016a9de3f8dbdae/image.png)
4. 分别设置Allow-Origin、Allow-Methods、Allow-Credentials、Allow-Headers、Expose-Headers 以及 Max-Age（带 * 号的为必填项），设置完成单击【提交】。
   ![跨域访问3](//mc.qcloudimg.com/static/img/f42ff7306010af443c8ba4876a725446/image.png)
5. 单击【保存】完成跨域访问设置。