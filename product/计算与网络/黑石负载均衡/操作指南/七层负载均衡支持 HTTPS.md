## 实现功能
黑石七层负载均衡支持 HTTPS 协议，实现功能具体如下：
- 提供外网七层 HTTPS 负载均衡能力；
- 对外网七层 HTTPS 提供七层健康检查、cookies 插入方式七层会话保持、通过域名 +URL 路径方式实现前端请求向后端不同服务器转发、实现后端服务器与转发 URL 细粒度绑定功能，此四项功能同外网七层 HTTP；
- 实现 SSL（Secure Sockets Layer）/TLS（transport layer security）鉴权；
- 实现 SSL（Secure Sockets Layer）/TLS（transport layer security）证书管理；
- 平台侧卸载 TLS：使用 HTTPS 监听转发时，客户端到负载均衡访问，使用 HTTPS 协议进行加密，负载均衡到后端服务器不进行 SSL/TLS 加密，实现平台卸载 TLS；
 
## 操作指南
- 名称：用户自定义监听器名称；
- 协议类型与端口：协议类型为 HTTPS，端口为前端端口；
- SSL 解析方式：当前有如下两种：
 - 单向认证：只是客户对服务器证书进行认证；
 - 双向认证：客户和服务器对双方证书都进行认证；

>?对于一般 Web 应用，单向认证即可，但对金融行业用户，可能会要求对客户端做身份验证，这时就需要双向认证。
