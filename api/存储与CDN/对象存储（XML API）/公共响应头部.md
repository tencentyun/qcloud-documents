## 描述

此篇文档将为您介绍在使用API时候会出现的公共返回头部（Response Header），下文提到的头部会在之后的具体API文档中不再赘述。

##  响应头部列表

| Header名称         | 描述                                       | 类型     |
| ---------------- | ---------------------------------------- | ------ |
| Content-Length   | RFC 2616 中定义的 HTTP 请求内容长度（字节）            | String |
| Content-Type     | RFC 2616 中定义的 HTTP 请求内容类型（MIME）          | String |
| Connection       | 声明客户端与服务端之间的通信状态。<br />枚举值：keep-alive，close | Enum   |
| Date             | 服务器端的响应时间，根据 RFC 1123 中定义的 GMT 时间。       | String |
| Etag             | ETag 全称 Entity Tag 是 Object 被创建时用于标识 Object 内容的信息标签。此参数并不一定返回 MD5 值，请根据不同请求的情况参考。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |
| Server           | 创建请求的服务器的名称，默认值：tencent-cos              | String |
| x-cos-request-id | 每次请求发送时，服务端将会自动为请求生成一个ID。                | String |
| x-cos-trace-id   | 每次请求出错时，服务端将会自动为这个错误生成一个ID。              | String |

