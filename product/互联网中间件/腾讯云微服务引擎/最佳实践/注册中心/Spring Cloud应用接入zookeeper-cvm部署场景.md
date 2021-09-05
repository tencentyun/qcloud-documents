
## 操作场景
本文介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 zookeeper 注册中心。接入无需修改任何代码。

## 操作步骤

1. 在 [CVM 控制台](https://console.cloud.tencent.com/cvm) 创建 CVM 实例。具体操作请参见 [CVM 实例创建指引](https://cloud.tencent.com/document/product/213/44264)。

2. 准备 Spring Cloud 应用 Jar 包。我们同时为您提供了 Spring Cloud 应用 Demo 代码库：
[Demo 代码仓库 >>](https://github.com/tencentyun/tse-simple-demo)

3. 上传 Spring Cloud 应用 Jar 包至 CVM 实例。

4. 在 [TSE 控制台](https://console.cloud.tencent.com/tse) 创建 zookeeper 注册中心实例。具体操作请参见 [创建微服务引擎实例](https://cloud.tencent.com/document/product/1364/58416)。
<dx-alert infotype="explain" title="">
创建 zookeeper 注册中心实例时，若不开启公网访问，则所选定的 VPC 需要与 CVM 实例的 VPC 保持一致。
</dx-alert>

5. zookeeper 注册中心实例创建成功后，在 [TSE 控制台](https://console.cloud.tencent.com/tse) 获取 TSE Zookeeper 注册中心实例访问 IP。

6. 指定注册中心地址参数并运行该应用。登录至 CVM 实例中，运行以下命令：
```
nohup java 
-Dspring.cloud.zookeeper.connect-string=[TSE Zookeeper注册中心实例访问IP:2181]
-jar [jar包名称] &
```

7. 在 [TSE 控制台](https://console.cloud.tencent.com/tse) 验证服务注册。点击进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。
![](https://main.qcloudimg.com/raw/2f9befc1fee7efbbcd30542cbf3728fb.png)

## 注意事项
Spring Cloud 应用接入 Zookeeper 注册中心，配置文件格式需如下所示：
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    zookeeper:
      connect-string: [zookeeper注册中心IP:2181]
      discovery:
        register: true
        enabled: true
        prefer-ip-address: true
:::
</dx-codeblock>


