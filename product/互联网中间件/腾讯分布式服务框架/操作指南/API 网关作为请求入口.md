用户在腾讯云 API 网关上可以通过配置微服务 API，将外部请求转发到 TSF 平台上部署的微服务。API 网关与 TSF 平台内微服务的关系如下：
![](https://main.qcloudimg.com/raw/efc43843783e9bd53afde3497abe14b1.png)
腾讯云 API 网关与腾讯云 TSF 是两个独立的产品，关于 API 网关可参考：

- 腾讯云 API 网关 [产品文档](https://cloud.tencent.com/document/product/628)
- 腾讯云 API 网关 [控制台](https://console.cloud.tencent.com/apigateway)



## 命名空间 Code

用户必须给命名空间配置 Code（Namespace Code），才能将 API 网关外部的请求转发到命名空间内的微服务。对于在不同命名空间内且名称都是 product 的微服务，只有通过命名空间 ID 和微服务名称来唯一确定一个微服务。由于平台生成的命名空间 ID 较难辨识（通常是 namespaceid-xxxx），因此需要引入命名空间 Code 作为唯一标识。命名空间 Code 具有如下特性：

- 跨集群唯一性
- 用户自定义
- 可读性强
- 不可修改



## 在 TSF 上配置命名空间 Code

在 TSF 控制台上的操作步骤如下：

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
2. 在左侧导航栏单击**命名空间**，进入命名空间列表页。
3. 选择目标集群后，单击命名空间列表右侧**设置 Code**。

## 在 API 网关上的操作

以 [TSF Demo](https://cloud.tencent.com/document/product/649/20231) 为例介绍在 API 网关上配置微服务 API 的流程。

前置条件：已经在 TSF 平台上部署了`provider-demo`应用，并在微服务所属命名空间中配置 Code，名称为`tsf-code`。

在 API 网关上，创建微服务 API 的流程如下：

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)，在左侧导航栏中单击**服务**。
2. 在服务列表页，单击**新建**，创建 API 服务。
3. 选择**服务名**，进入服务详情页。
4. 在服务详情页，单击**管理API**标签页中的**微服务API**，单击**新建**，创建微服务 API。
5. 前置配置，各字段详情含义参考 [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)。
   ![](https://main.qcloudimg.com/raw/502249689f131ebc8c23aa001d0c626d.png)
6. 后置配置，各字段详细含义参考 [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)。
   ![](https://main.qcloudimg.com/raw/edf10a3eb00cc9742d07327f3881099d.png)
7. 预览微服务 API 信息，单击右侧**API调试**。
8. 调试 API。
   ![](https://main.qcloudimg.com/raw/e5729bb36b9d1a592cc4c67c4dfd9118.png)
> ? 
> - 目前 API 网关只支持将请求转发到 TSF 同一种部署类型（虚拟机或容器）的服务实例上。如果一个服务下既有虚拟机部署、又有容器部署的微服务实例，则不支持将 API 网关作为请求入口。
> - 关于 API 网关上的详细操作，请参考 [API 网关产品文档](https://cloud.tencent.com/document/product/628)。

如果 API 调试时发生超时错误，可能是服务所在云服务器 CVM 的安全组限制所导致，检查安全组放通的端口中是否包含了微服务的端口（如 provider-demo 的端口是18081），参考 [CVM-安全组](https://cloud.tencent.com/document/product/213/12452)。

![](https://main.qcloudimg.com/raw/532e8bd715689a93b7ec90f24c9fc402.png)
