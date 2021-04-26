## 操作场景

在 HTTP 场景中，对响应数据进行压缩处理可有效降低数据传输量，达到减少响应时间、节省服务端网络带宽、提升客户端性能等目的。
该任务将指导您在 API 网关中配置响应压缩。

## 交互流程

![](https://main.qcloudimg.com/raw/d3516bd26fc3087dc3f48571cec0e038.svg)

## 操作说明

API 网关默认已经支持了基于 gzip 压缩算法的响应压缩，该功能的依赖条件如下：

- 客户端请求中携带 Accept-Encoding 头，并且该字段的值包含 gzip。
- 客户端响应 body 大于1KB。
- 响应 body 的 Content-Type 为 text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、application/xml、application/json、application/octet-stream。

当客户端请求满足以上条件时，API 网关会将响应 body 压缩后再返回给客户端，并在响应中携带 Content-Encoding: gzip 头。

## 注意事项

- 仅支持协议为 HTTP 和 HTTPS 时启用响应压缩功能，协议为 websocket 时不支持。
- 后端对接 SCF，且启用响应集成时，云函数返回给API网关的结构体中不能包含  Content-Encoding: gzip 头，否则响应压缩将不生效。
