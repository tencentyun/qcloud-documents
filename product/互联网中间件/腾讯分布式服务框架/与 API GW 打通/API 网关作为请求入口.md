用户在腾讯云 API 网关上可以配置微服务 API 来将外部请求转发到 TSF 平台上部署的微服务。API 网关与 TSF 平台内的微服务之间的关系如下图：

![](https://main.qcloudimg.com/raw/efc43843783e9bd53afde3497abe14b1.png)





腾讯云 API 网关与腾讯云 TSF 是两个独立的产品，关于 API 网关可参考：

- 腾讯云 API 网关 [产品使用手册](https://cloud.tencent.com/document/product/628)
- 腾讯云 API 网关 [控制台](https://console.cloud.tencent.com/apigateway)



## 命名空间 Code

用户必须将给命名空间配置 code （Namespace Code）才能实现将 API 网关外部的请求转发到命名空间内的微服务。对于不同命名空间内的名称都是 product 的微服务来说，只有通过命名空间 ID 和微服务名称来唯一确定一个微服务。由于平台生成的命名空间 ID 较难辨识（通常是 namespaceid-xxxx) ，因此引入命名空间 Code 来作为唯一标示。命名空间 Code 具有如下特性：

- 跨集群唯一性
- 用户自定义
- 可读性强
- 不可修改



## 在TSF上的配置命名空间Code

在 TSF 控制台上的操作步骤如下：


1. 登录 [TSF 控制台](https://console.cloud.tencent.com/apigateway)。
2. 单击左侧导航栏 **命名空间**。
3. 选择目标集群后，单击命名空间列表左侧【配置 Code】。

![](https://main.qcloudimg.com/raw/79b6fc71f3c86f66173083d3b4051285.png)



## 在 API 网关上的操作

在 API 网关上的详细操作可以参考腾讯云 [API 网关产品文档](https://cloud.tencent.com/document/product/628)，其中与微服务相关的操作可参考：

- [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)
- [调试微服务API](https://cloud.tencent.com/document/product/628/17562)