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



## 在TSF上配置命名空间Code

在 TSF 控制台上的操作步骤如下：

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/apigateway)。
2. 单击左侧导航栏 **命名空间**。
3. 选择目标集群后，单击命名空间列表左侧【配置 Code】。

![](https://main.qcloudimg.com/raw/223aa254491ae14751f5890b7648ea16.png)



## 在 API 网关上的操作

以 [TSF Demo](https://cloud.tencent.com/document/product/649/16619) 为例介绍在 API 网关上配置微服务 API 的流程。

前置条件：已经在 TSF 平台上部署了 `provider-demo` 应用，并在微服务所属命名空间配置 code ，名称为 `tsf-code` 。

在 API 网关上，创建微服务 API 的流程如下：

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。

2. 创建 API 服务。

    ![](https://main.qcloudimg.com/raw/2331e9463018b7dcda942370f1253fe2.png)

3. 创建微服务 API。

   ![](https://main.qcloudimg.com/raw/20e00a475d187dfc185beca94cd6db25.png) 

4. 前置配置，各字段详情含义参考 [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)。
   ![](https://main.qcloudimg.com/raw/8c7a1ddddc0802a9071f8389dc2bc3f5.png)

5. 后置配置，各字段详细含义参考  [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)。
   ![](https://main.qcloudimg.com/raw/a36e65e3021da965401df82b86b420b6.png)

6. 预览微服务 API 信息，单击【API调试】。
   ![](https://main.qcloudimg.com/raw/ef016392d649113c5835949be885c513.png)

7. 调试 API。   ![](https://main.qcloudimg.com/raw/a0f00acf1fb1a8590781c512d9092c71.png)



> 注：在 API 网关上的详细操作可以参考腾讯云 [API 网关产品文档](https://cloud.tencent.com/document/product/628)
