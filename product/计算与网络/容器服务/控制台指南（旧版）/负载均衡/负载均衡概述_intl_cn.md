## 负载均衡概述
容器的负载均衡是容器创建的服务的访问的入口，一个服务前端配置一个负载均衡，后端由容器组成，您无需关系这个负载均衡的类型。您只需关注提供的功能。

创建服务时：

- 选择公网，则自动创建能提供公网服务的支持TCP/UDP协议的负载均衡器
- 选择内网，则自动创建能提供内网服务的支持TCP/UDP协议的负载均衡器

若您需要支持HTTP/HTTPS转发，可在负载均衡页面创建Ingress，并配置转发规则。

## 使用说明

- [负载均衡的基本操作](https://cloud.tencent.com/document/product/457/9109)
- [Ingress的转发设置](https://cloud.tencent.com/document/product/457/9111)