## TEM 介绍

弹性微服务（Tencent Cloud Elastic Microservice，TEM）是面向微服务应用的 Serverless 平台，实现 Serverless 与微服务的完美结合，提供开箱即用的微服务解决方案。拥抱开源，应用零改造上云，提供应用托管、服务注册发现、微服务治理、多维度监控等能力，支持 Eureka 、ZooKeeper 等注册中心。弹性微服务帮助您创建和管理云资源，按量付费，免运维。具体请查看 [弹性微服务 TEM 官网文档](https://cloud.tencent.com/document/product/1371)。

## 操作场景

本文档主要介绍如何快速使用腾讯云 API 网关访问 TEM 应用并管理 TEM 应用的 API。使用 API 网关和 TEM 结合，可使 TEM 的用户享受到 API 网关提供的限流、认证、缓存等高级能力，助力业务获得成功。
<img src="https://main.qcloudimg.com/raw/3ba80d1325ca9550610d0f5712482274.png" width="650px">

## 前提条件

请登录 [弹性微服务 TEM 控制台](https://console.cloud.tencent.com/tem)，先完成 [环境创建](https://cloud.tencent.com/document/product/1371/53293) 和 [创建并部署应用](https://cloud.tencent.com/document/product/1371/53294)。

## 操作步骤

### 步骤1：为 TEM 应用配置 VPC 内网访问

1. 登录 [TEM 控制台](https://console.cloud.tencent.com/tem)，在左侧导航栏单击**应用管理**，单击您想要配置的应用进入应用详情页。
2. 单击访问配置栏的**编辑并更新**，进入应用访问配置页。
   ![](https://main.qcloudimg.com/raw/47630bde7bf37d8492aa9513c8c042ee.png)
3. 选择 VPC 内网访问（四层转发），选择子网、协议、容器端口和应用监听端口，并单击**提交**。此时 TEM 会为您自动创建四层转发的 VPC 内网应用型 CLB。
<img src="https://main.qcloudimg.com/raw/6035759e5464618638e98bdb5328e412.png" width="800px">


### 步骤2：创建 API 网关服务并绑定 TEM 应用[](id:step2)

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service)，在左侧导航栏，单击**服务**，进入服务列表页。
2. 选择与部署 TEM 应用相同的地域，单击页面左上角的**新建**，新建一个服务。
   新建服务时，前端类型可选择 HTTP、HTTPS、HTTP 与 HTTPS 任一种，访问模式选择可以选择 VPC 内网和公网，实例类型选择共享性、专享型。
>?关于实例类型的选择，请参考 [实例选择指南](https://cloud.tencent.com/document/product/628/55510)。
>
	 <img src="https://main.qcloudimg.com/raw/5e90d7876eeea6b257821507615b16be.png" width="500px">
3. 单击 API 网关服务 ID 进入 API 管理页面。单击**新建 API**。
4. 在前端配置中填写 API 名称，前端类型选择 HTTP&HTTPS，路径为“/”，请求方法选择 ANY 以包含所有请求，鉴权类型选择“免认证”，单击**下一步**。
   ![](https://main.qcloudimg.com/raw/6496aacc6e308c1a3bb599570415bfa1.png)
5. 在后端配置中，选择 VPC 内资源，选择 TEM 应用部署环境所在的 VPC。设置后端域名，选择 TEM 应用自动创建的 CLB（名字为“cls-xxxdefault{TEM应用名}”），选择相应的监听器（即上一步中所设置的端口映射），填写后端地址为“/”，完成 API 的创建。
   ![](https://main.qcloudimg.com/raw/f124d179b8a7dfe715b5e9dfb6bc4228.png)
	其中，后端域名的设置如下：
  <img src="https://main.qcloudimg.com/raw/f1d8b0d080aab985df46ec9a224b8e07.png" width="500px">
6. 此时您可看到您所配置的 API。并可以通过 API 网关提供的默认域名访问您的 TEM 应用。


### 步骤3：通过 API 网关访问 TEM 应用

访问 [步骤2](#step2) 中创建的 API 网关 API，即可通过 API 网关访问到 TEM 应用。
   ![](https://main.qcloudimg.com/raw/70ca90f3a189c79f09f0c8e334507b22.png)

## 注意事项

- 为保证应用无侵入的接入 API 网关，我们建议一个 API 网关服务只绑定一个 TEM 应用，前端地址和后端地址保持一致，同为“/”可以拦截所有 API，您也可以在服务中为您应用的某些 API 进行单独的配置。
- 您可以参考 [API 网关插件使用文档](https://cloud.tencent.com/document/product/628/53379)，为后端对接 TEM 的 API 网关 API 绑定插件，以享受 API 网关提供的高级功能。
