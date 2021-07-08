# 容器场景下 Spring Cloud 服务注册与发现 --以TEM部署服务为例



## 操作场景

本文为您介绍如何通过弹性微服务（TEM）+ 微服务引擎（TSE）注册中心实现服务注册与发现。

## 操作步骤
### 步骤1：服务部署

#### 1. 准备Spring Cloud 应用
Spring Cloud 应用使用如下的配置接入 Consul / Eureka /Zookeeper 注册中心：
>?
>- 您可以点击以下页签，查看对应配置。
>- 您需要将配置中的 x.x.x.x 替换为您 TSE 实例的 【访问方式】 中的 IP 地址。
<dx-tabs>
::: Consul 
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    consul:
      host: x.x.x.x
      port: 8500
      discovery:
        prefer-ip-address: true
:::
</dx-codeblock>
:::
::: Eureka
<dx-codeblock>
:::  plaintext
eureka:
  client:
    serviceUrl:
      defaultZone: http://x.x.x.x:8761/eureka/
  instance:
    prefer-ip-address: true
:::
</dx-codeblock>
:::
::: Zookeeper
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    zookeeper:
      connect-string: x.x.x.x:2181
      discovery:
        register: true
        enabled: true
        prefer-ip-address: true
:::
</dx-codeblock>
:::
</dx-tabs>




您可以下载我们提供的demo，快速完成快速入门教程。

[Demo 代码仓库 >>](https://github.com/tencentyun/tse-simple-demo)



#### 2. 编译Jar包

在工程的主目录下，使用 maven 命令 `mvn clean package` 进行打包，即可在 target 目录下找到打包好的 Jar 文件。

#### 3. 创建 TEM 环境

弹性微服务（Tencent Cloud Elastic Microservice，TEM）是面向微服务应用的 Serverless PaaS 平台，提供开箱即用的微服务解决方案。在开始部署您的应用前，您将需要 [在TEM中创建环境](https://console.cloud.tencent.com/tem)。

#### 4. 关联 TSE 注册中心

在 [TEM控制台](https://console.cloud.tencent.com/tem) 中的【环境】页面，选择您创建的环境，进入环境基本信息页面。在资源详情模块中，单击【添加】即可关联您注册中心资源。

#### 5. 部署服务

一键部署demo至您已创建的TEM环境中。具体可参考[在TEM中部署微服务应用指南](https://cloud.tencent.com/document/product/1371/57689)。


### 步骤2：验证服务注册

待部署的应用实例开始运行后，可进入 [TSE注册中心](https://console.cloud.tencent.com/tse/registry?rid=4) 实例的服务管理页面。若出现以下页面，则证明服务注册成功。

![](https://main.qcloudimg.com/raw/a27e06771f854fc411fb96d93e968baf.png)

### 步骤3：验证服务发现

1. 配置公网访问

请参照 [在TEM中部署微服务应用指南](https://cloud.tencent.com/document/product/1371/57689)，为部署的demo工程创建访问配置，以通过公网被访问。


2. 验证访问

在浏览器中输入以下URL

``` http://公网访问IP/ping-provider/test```

如果返回以下结果，则说明应用部署成功。

``` ```test, response from consul-demo-provider
