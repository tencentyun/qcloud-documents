## 操作场景

本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 TKE 部署的 Spring Cloud 应用接入微服务引擎托管的 Eureka 注册中心，并实现简单的服务访问。帮助您快速了解如何使用 TSE Eureka 注册中心。



## 前提条件

- 已创建 TSE Eureka 注册中心，请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/58408)。
- 本地编译构建打包机器环境已安装了 Java JDK、Maven，并且能够访问 Maven 中央库。



## 操作步骤

1. 创建 TKE 容器集群。
   登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster)，新建一个标准集群，容器集群所在的私有网络 VPC 需要与已创建好的 Eureka 引擎所在的私有网络保持一致。具体操作参见 [快速创建一个标准集群](https://cloud.tencent.com/document/product/457/54231)。
2. 获取 Eureka 注册中心实例访问 IP。
   登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，单击已创建好的 Eureka 引擎实例的“ID”，进入基本信息页面，在接入方式模块可以获取 Eureka 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5c8c38057973e961cceb90a37eaee475.png)
3. 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
4. 打包 Demo 源码成 jar 包。
   在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 `mvn clean package` 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Eureka Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">\tse-simple-demo-main\tse-eureka-provider-demo\target</td>
<td align="left">tse-eureka-provider-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">\tse-simple-demo-main\tse-eureka-consumer-demo\target</td>
<td align="left">tse-eureka-consumer-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
5. 制作 provider 和 consumer 应用容器镜像并上传至镜像仓库。
   1. 编写 dockerfile 并生成镜像，dockerfile 内容参见：
     ```shell
   FROM openjdk:8
    
   ADD ./[jar包名称.jar] /root/app.jar
       
   ENTRYPOINT  [ "sh", "-c", "java $JAVA_OPTS -jar /root/app.jar"]
     ```
   2. 参见 [镜像仓库快速入门](https://cloud.tencent.com/document/product/1141/63910) 上传 Spring Cloud 应用镜像至 TKE 镜像仓库。
6. 在 TKE 容器集群中创建工作负载并选择对应镜像文件。
   1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster)，找到已创建好的 TKE 容器集群，单击集群 ID，进入集群的**工作负载** >  **Deployment**页面，创建工作负载并选择对应镜像文件，详细操作参见 [Deployment 管理](https://cloud.tencent.com/document/product/457/31705)。
      - 镜像：选择已上传的 Spring Cloud 应用镜像。
      - 镜像版本：选择已上传的 Spring Cloud 应用镜像版本。
      - 环境变量：新增环境变量 `JAVA_OPTS` 并指定为 `-Deureka.client.serviceUrl.defaultZone=http://[TSE Eureka注册中心实例访问IP:8761]/eureka/ `
      ![](https://qcloudimg.tencent-cloud.cn/raw/9215d5db0dfaa0300eb5d0e8ad0d0047.png)
   2. Deployment 信息填写完成后，单击**创建 Deployment**，出现如下页面时，代表 Deployment 创建成功。
      ![](https://qcloudimg.tencent-cloud.cn/raw/00938ece73a8d6b3636b9cfb96404a75.png)
7. 验证服务注册成功。
   登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，在左侧导航栏选择 **eureka**，单击目标实例的 ID，进入基本信息页面。在页面上方选择**服务管理**页签，若出现以下页面，则证明服务注册成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/29ec7f49a939b99b5adafffa6fef92b8.png)
8. 验证服务调用。
   登录 Consumer 服务所在的 Pod，执行 curl 命令调用 Consumer 接口访问 Provider 服务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/def43371d4479282905e8ee4d213186a.png)
   ```curl
   curl localhost:18082/ping-provider/test
   ```
   访问结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/16e8a06aa23a7b6402730a64a1f2f743.png)







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

