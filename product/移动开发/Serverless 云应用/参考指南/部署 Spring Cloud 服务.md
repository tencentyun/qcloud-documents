## 概述

[Spring Cloud](https://spring.io/projects/spring-cloud) 是基于 Spring Boot 的一整套实现微服务的框架，提供了微服务开发所需的配置管理、服务发现、断路器、智能路由、微代理、控制总线、全局锁、决策竞选、分布式会话和集群状态管理等组件。

## 部署示例

在下面的例子中，我们将部署一套基于 Spring Cloud 的微服务，包含：

- 1 个服务提供者（**hello-service**），使用 CloudBase 云托管部署；
- 1 个服务调用者（**hello-client**），使用 CloudBase 云托管部署；
- 注册中心（**eureka-server**）和配置中心（**config-server**），使用腾讯云 CVM 部署

![](https://main.qcloudimg.com/raw/c0e1f659d2521c29863bfcb6a74efa44.png)

>?详情请参见 [示例代码仓库](https://github.com/TencentCloudBase/Cloudbase-Examples/tree/master/cloudbaserun/spring-cloud-docker-demo)。

## 部署流程

以下所有涉及的 CVM 实例、云托管实例，都处于同一个 VPC 内。您可以在云托管详情内看到您的应用所属的 VPC。

### 步骤1：部署注册中心（eureka-server）

1. 首先需要您准备一个腾讯云 CVM 实例，如果您没有实例，可以前往腾讯云 CVM 购买。
>? CVM 实例需要与云托管服务处于同一 VPC 内。您可以在购买 CVM 时指定，也可以修改已有的 CVM 实例所处的 VPC 网络。
>
2. 下载 [项目示例代码](https://github.com/TencentCloudBase/Cloudbase-Examples/tree/master/cloudbaserun/spring-cloud-docker-demo)，进入 `eureka-server` 目录下，执行：
<dx-codeblock>
:::  sh
mvn compile & mvn package
:::
</dx-codeblock>
3. 在 `target` 目录下，可以看到构建产物：`app.jar`。使用任意方法将 `app.jar` 上传至您 CVM 内的 `/root` 目录下，这里我们使用 [scp](https://www.runoob.com/linux/linux-comm-scp.html) 命令：
<dx-codeblock>
:::  sh
scp app.jar root@1.2.3.4:/root/
:::
</dx-codeblock>
4. 登录到 CVM 内，在 `/root` 目录下，运行：
<dx-codeblock>
:::  sh
java -jar app.jar &
:::
</dx-codeblock>
>? 此处需要您的 CVM 已经预先安装好了 Java，如果没有安装 Java，请参阅相关文档进行安装。
5. 安装成功后，打开 CVM 对应公网的 IP 和端口（项目默认为 `8280`）可查看到如下的界面：
![](https://main.qcloudimg.com/raw/8dd203402c84ae0a43419edc177dbc9b.png)

### 步骤2：部署配置中心（config-server）

1. 首先需要您准备一个腾讯云 CVM 实例，如果您没有实例，可以前往腾讯云 CVM 购买。
>? 为了更接近真实的服务场景，我们建议您使用与上文的注册中心不同的 CVM 示例。
2. 进入示例项目的 `config-server/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为上文的 **注册中心（eureka-server）** 的地址，如下图：
![](https://main.qcloudimg.com/raw/95ad69f5382dc93fb796cddeb92f5abf.png)
3. 进入 `config-server` 目录，执行：
<dx-codeblock>
:::  sh
mvn compile & mvn package
:::
</dx-codeblock>
4. 在 `target` 目录下，可以看到构建产物：`app.jar`。使用任意方法将 `app.jar` 上传至您 CVM 内的 `/root` 目录下，这里我们使用 [scp](https://www.runoob.com/linux/linux-comm-scp.html) 命令：
<dx-codeblock>
:::  sh
scp app.jar root@1.2.3.4:/root/
:::
</dx-codeblock>
5. 登录到 CVM 内，在 `/root` 目录，运行：
<dx-codeblock>
:::  sh
java -jar app.jar &
:::
</dx-codeblock>
6. 安装成功后，打开 CVM 对应公网的 IP 、端口（默认为 `8210`）、路径 `/config-client-dev.yml`（例如 http://{IP 地址}:8210/config-client-dev.yml ）可查看到如下输出：
![](https://qcloudimg.tencent-cloud.cn/raw/aae84ceb08a222eac629b1819d83b120.png)

### 步骤3：部署服务提供方（hello-service）

1. 首先 [开通云托管](https://cloud.tencent.com/document/product/1243/47080)，选择与上文 CVM 同样的 VPC，以及对应的子网:
![](https://main.qcloudimg.com/raw/1c806169425abc409786af835a33af03.png)
2. 新建服务 `hello-service`：
<img src = "https://main.qcloudimg.com/raw/13d4ce31e4eb7562ac3cf54424751720.png" style="width: 80%"> 
3. 进入示例项目 `hello-service/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为对应地址，如下图：
![](https://main.qcloudimg.com/raw/8cb877698c7c77a7fccf36804dede364.png)
4. 然后登录 CloudBase 云托管控制台，选择新建版本，将示例项目的 `/hello-service` 目录上传，同时版本配置参考如下：
<img src = "https://main.qcloudimg.com/raw/0b944188e40dd10d7fe13e5a906f030f.png" style="width: 80%"> 
5. 部署成功后，会在云开发控制台看到版本状态为**正常**：
![](https://main.qcloudimg.com/raw/c1eaf2ecef7c9d059fd534349bbbe0ac.png)
6. 并且在 Eureka 控制台，可以看到有新的注册节点：
![](https://qcloudimg.tencent-cloud.cn/raw/120aa0f4c02969e884e65770e6ec0456.png)

### 步骤4：部署服务调用方（hello-client）

1. 新建服务 `hello-client`，单击**提交**。
<img src = "https://main.qcloudimg.com/raw/975d6625c4539fa668658a2387db5210.png" style="width: 80%"> 
2. 进入示例项目 `hello-client/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为对应地址，如下图：
![](https://main.qcloudimg.com/raw/0831b976cb9a2eb3fc6e8feadf7c8270.png)
3. 然后登录 CloudBase 云托管控制台，选择新建版本，将示例项目的 `/hello-client` 目录上传，同时版本配置参考如下：
<img src = "https://main.qcloudimg.com/raw/0cf33eb86864e78a264b4e5d888e3e72.png" style="width: 80%"> 
4. 部署成功后，会在云开发控制台看到版本状态为**正常**：
![](https://main.qcloudimg.com/raw/fbaf54c3e056714fb2a7fe44c679a8a3.png)
5. 并且在 Eureka 控制台，可以看到有新的注册节点：
![](https://qcloudimg.tencent-cloud.cn/raw/4ca108f591c849fb9730a4f8e98fbd40.png)

## 验证服务

访问 `hello-client` 的 HTTP 地址，可以看到如下输出：
![](https://qcloudimg.tencent-cloud.cn/raw/b216d7929b1ffa393ca46053a4d90be0.png)

[1]: https://github.com/TencentCloudBase/Cloudbase-Examples/tree/master/cloudbaserun/spring-cloud-docker-demo
