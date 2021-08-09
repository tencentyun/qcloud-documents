
## 操作场景
本文介绍如何将通过 TKE 部署的 Spring Cloud 应用接入微服务引擎托管的 Eureka 注册中心。接入无需修改任何代码。

## 操作步骤

1. 在 [TKE 控制台](https://console.cloud.tencent.com/tke) 中创建TKE容器集群。具体操作请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

2. 准备 Spring Cloud 应用镜像文件。我们同时为您提供了 Spring Cloud 应用 Demo 代码库：
[Demo 代码仓库 >>](https://github.com/tencentyun/tse-simple-demo)

3. 上传 Spring Cloud 应用镜像文件至 TKE 镜像仓库。具体操作请参见 [镜像仓库快速入门](https://cloud.tencent.com/document/product/1141/50332)。

4. 在 [TSE 控制台](https://console.cloud.tencent.com/tse) 创建 Eureka 注册中心实例。具体操作请参见 [创建 Eureka 实例](https://cloud.tencent.com/document/product/1364/58408)。
<dx-alert infotype="explain" title="">
创建 Eureka 注册中心实例时，若不开启公网访问，则所选定的 VPC 需要与 TKE 容器集群的 VPC 保持一致。
</dx-alert>

5. Eureka 注册中心实例创建成功后，在 [TSE 控制台](https://console.cloud.tencent.com/tse) 获取 TSE Eureka 注册中心实例访问 IP。

6. 在 TKE 容器集群中创建工作负载并选择对应镜像文件。具体操作请参见 [Deployment 管理](https://cloud.tencent.com/document/product/457/31705)。
<dx-alert infotype="explain" title="">
创建工作负载时，需将环境变量 `JAVA_OPTS` 指定为 `-Deureka.client.serviceUrl.defaultZone=http://[TSE Eureka注册中心实例访问IP:8761]/eureka/ `。
</dx-alert>

7. 在 [TSE 控制台](https://console.cloud.tencent.com/tse) 验证服务注册。点击进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。
![](https://main.qcloudimg.com/raw/43368b4a90fa23a8cf733de286b4c1d9.png)

## 注意事项
Spring Cloud 应用接入 Eureka 注册中心，配置文件格式需如下所示：
<dx-codeblock>
:::  plaintext
eureka:
  client:
    serviceUrl:
      defaultZone: http://[eureka注册中心实例访问IP:8761]/eureka/
  instance:
    prefer-ip-address: true
:::
</dx-codeblock>


