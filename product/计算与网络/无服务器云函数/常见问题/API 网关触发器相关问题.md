### SCF 运行返回 504 怎么办？

1. 检查函数及网关配置的超时时间，并尝试增加一定的网关超时时间。
2. 可参见 [API 网关日志管理](https://cloud.tencent.com/document/product/628/19552) 配置日志，通过分析日志定位具体原因。

### SCF 运行返回 "error":403,"error":"Invalid scf response format. please check your scf response format." 怎么办？

API 网关会将云函数的返回内容进行解析，并根据解析内容构造 HTTP 响应。通过使用集成响应，可以通过代码自主控制响应的状态码、headers、body 内容，可以实现自定义格式的内容响应，例如响应 XML、HTML、JSON 甚至 JS 内容。在使用集成响应时，需要按照 [API 网关触发器的集成响应返回数据结构](https://cloud.tencent.com/document/product/583/12513#apiStructure)，才可以被 API 网关成功解析，否则会出现 `{"errno":403,"error":"requestId xxx , Invalid scf response. expected scf response valid JSON."}` 错误信息。

### 如何使用自定义域名？

用户可通过域名绑定功能，将用户所拥有的独立域名绑定到服务，使得服务能以用户自身独立域名的方式提供，详情可参考 API 文档 [配置自定义域名](https://cloud.tencent.com/document/product/628/11791)。域名配置完成后，在需要使用自定义域名的函数下选择**使用已有API服务**创建 API 网关触发器。

### 函数如何实现跨域？

可参考 [腾讯云 SCF + 腾讯云 API 网关实现跨域](https://cloud.tencent.com/developer/article/1531402) 进行配置。
