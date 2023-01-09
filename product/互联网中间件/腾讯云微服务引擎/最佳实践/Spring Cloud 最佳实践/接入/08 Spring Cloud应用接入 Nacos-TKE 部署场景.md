## 操作场景

本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 TKE 部署的 Spring Cloud 应用接入微服务引擎托管的 Nacos 注册中心，并实现简单的服务访问。帮助您快速了解如何使用 TSE Nacos 注册中心。



## 前提条件

- 已创建 TSE Nacos 注册中心，请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
- 本地编译构建打包机器环境已安装了 Java JDK、Maven，并且能够访问 Maven 中央库。



## 操作步骤

1. 创建 TKE 容器集群。
   登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster)，新建一个标准集群，容器集群所在的私有网络 VPC 需要与已创建好的 Nacos 引擎所在的私有网络保持一致。具体操作参见 [快速创建一个标准集群](https://cloud.tencent.com/document/product/457/54231)。
2. 获取 Nacos 注册中心实例访问 IP。
   登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，单击已创建好的 Nacos 引擎实例的“ID”，进入基本信息页面，在访问控制页签可以获取 Nacos 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e9a4b2e4430d337c153abc09a6bccf32.png)
3. 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
4. 打包 Demo 源码成 jar 包。
   在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 `mvn clean package` 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Nacos  Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">tse-nacos-spring-cloud-provider-demo\target</td>
<td align="left">tse-nacos-spring-cloud-provider-demo-2.0.1.RELEASE.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">tse-nacos-spring-cloud-consumer-demo\target</td>
<td align="left">tse-nacos-spring-cloud-consumer-demo-2.0.1.RELEASE.jar</td>
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
      - 环境变量：新增环境变量 `JAVA_OPTS` 并指定为 `-Dspring.cloud.nacos.discovery.server-addr=[Nacos 注册中心实例访问 IP:8848] `
      ![](https://qcloudimg.tencent-cloud.cn/raw/98548ec6884fa0a2a8eb99cad00b41f6.png)
   2. Deployment 信息填写完成后，单击**创建 Deployment**，出现如下页面时，代表 Deployment 创建成功。
      ![](https://qcloudimg.tencent-cloud.cn/raw/ad305cc2cd6ea3d7af3aa3c5cab2e1b3.png)
7. 验证服务注册成功。
   1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。在左侧导航栏选择 **nacos**，单击目标实例的 ID，进入基本信息页面。
   2. 在页面上方选择**访问控制**页签，找到控制台访问的公网地址和登录用户名密码，通过 web 访问 Nacos 原生控制台。
      ![](https://qcloudimg.tencent-cloud.cn/raw/c23a003df4bf59c8ae9dc47bc319a169.png)
   3. 在 Nacos 原生控制台页面，选择**服务管理** > **服务列表**，可以看到注册成功的服务。
      ![](https://qcloudimg.tencent-cloud.cn/raw/478abd75daf46d19f81e257dcd42f94b.png)
8. 验证服务调用。
   登录 Consumer 服务所在的 Pod，执行 curl 命令调用 Consumer 接口访问 Provider 服务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/9c9c3c128c826a647260d02d0fda14b8.png)
   ```
   curl localhost:8080/echo/str
   ```
   访问结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/e7c8e7fcbf51d6e3ed5b0a6669b0e765.png)





