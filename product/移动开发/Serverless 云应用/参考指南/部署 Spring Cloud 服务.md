## 概述

[Spring Cloud](https://spring.io/projects/spring-cloud) 是基于 Spring Boot 的一整套实现微服务的框架，提供了微服务开发所需的配置管理、服务发现、断路器、智能路由、微代理、控制总线、全局锁、决策竞选、分布式会话和集群状态管理等组件。

## 部署示例

在下面的例子中，我们将部署一套基于 Spring Cloud 的微服务，包含：

- 1 个服务提供者（**hello-service**），使用 CloudBase 云托管部署；
- 1 个服务调用者（**hello-client**），使用 CloudBase 云托管部署；
- 注册中心（**eureka-server**）和配置中心（**config-server**），使用腾讯云 CVM 部署

![](https://main.qcloudimg.com/raw/c0e1f659d2521c29863bfcb6a74efa44.png)

示例代码仓库：[https://github.com/TencentCloudBase/Cloudbase-Examples/tree/master/cloudbaserun/spring-cloud-docker-demo][1]

## 部署流程

>? 以下所有涉及的 CVM 实例、云托管实例，都处于同一个 VPC 内。您可以在云托管详情内看到您的应用所属的 VPC。

## 第 1 步：部署注册中心（eureka-server）

首先需要您准备一个腾讯云 CVM 实例，如果您没有实例，可以前往腾讯云 CVM 购买。

>? CVM 实例需要与云托管服务处于同一 VPC 内。您可以在购买 CVM 时指定，也可以修改已有的 CVM 实例所处的 VPC 网络。

下载 [项目示例代码][1]，进入 `eureka-server` 目录下，执行：

```sh
mvn compile & mvn package
```

在 `target` 目录下，可以看到构建产物：`app.jar`。

使用任意方法将 `app.jar` 上传至您 CVM 内的 `/root` 目录下，这里我们使用 [scp](https://www.runoob.com/linux/linux-comm-scp.html) 命令：

```
scp app.jar root@1.2.3.4:/root/
```

登录到 CVM 内，在 `/root` 目录下，运行：

```
java -jar app.jar &
```

>? 此处需要您的 CVM 已经预先安装好了 Java，如果没有安装 Java，请参阅相关文档进行安装。

安装成功后，打开 CVM 对应公网的 IP 和端口（项目默认为 `8280`）可查看到如下的界面：

![](https://main.qcloudimg.com/raw/8dd203402c84ae0a43419edc177dbc9b.png)

## 第 2 步：部署配置中心（config-server）

首先需要您准备一个腾讯云 CVM 实例，如果您没有实例，可以前往腾讯云 CVM 购买。

>? 为了更接近真实的服务场景，我们建议您使用与上文的注册中心不同的 CVM 示例。

进入示例项目的 `config-server/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为上文的 **注册中心（eureka-server）** 的地址，如下图：

![](https://main.qcloudimg.com/raw/95ad69f5382dc93fb796cddeb92f5abf.png)

进入 `config-server` 目录，执行：

```
mvn compile & mvn package
```

在 `target` 目录下，可以看到构建产物：`app.jar`。

使用任意方法将 `app.jar` 上传至您 CVM 内的 `/root` 目录下，这里我们使用 [scp](https://www.runoob.com/linux/linux-comm-scp.html) 命令：

```
scp app.jar root@1.2.3.4:/root/
```

登录到 CVM 内，在 `/root` 目录，运行：

```
java -jar app.jar &
```

安装成功后，打开 CVM 对应公网的 IP 、端口（默认为 `8210`）、路径 `/config-client-dev.yml`（例如 http://81.68.219.131:8210/config-client-dev.yml ）可查看到如下输出：

![](https://main.qcloudimg.com/raw/c7f1289760e74b6b3d6d9a865648d828.png)

## 第 3 步：部署服务提供方（hello-service）

首先[开通云托管](https://cloud.tencent.com/document/product/1243/47080)，选择与上文 CVM 同样的 VPC，以及对应的子网:

![](https://main.qcloudimg.com/raw/1c806169425abc409786af835a33af03.png)

新建服务 `hello-service`：

![](https://main.qcloudimg.com/raw/432c74209219f377a5c13dbf44dac433.png)

进入示例项目 `hello-service/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为对应地址，如下图：

![](https://main.qcloudimg.com/raw/8cb877698c7c77a7fccf36804dede364.png)

然后登录 CloudBase 云托管控制台，选择新建版本，将示例项目的 `/hello-service` 目录上传，同时版本配置参考如下：

![](https://main.qcloudimg.com/raw/bfd406578dd8aa7874a766bf0616630b.png)

部署成功后，会在云开发控制台看到版本状态为【正常】：

![](https://main.qcloudimg.com/raw/c1eaf2ecef7c9d059fd534349bbbe0ac.png)

并且在 Eureka 控制台，可以看到有新的注册节点：

![](https://main.qcloudimg.com/raw/971a7de259d940ae85bdf5c4579719c6.png)

## 第 4 步：部署服务调用方（hello-client）

新建服务 `hello-client`：

![](https://main.qcloudimg.com/raw/f6c9694f9aca40e038d387ae6653a2d7.png)

进入示例项目 `hello-client/src/main/resources` 目录，修改 `application.yml`，将 Eureka 的地址改为对应地址，如下图：

![](https://main.qcloudimg.com/raw/0831b976cb9a2eb3fc6e8feadf7c8270.png)

然后登录 CloudBase 云托管控制台，选择新建版本，将示例项目的 `/hello-client` 目录上传，同时版本配置参考如下：

![](https://main.qcloudimg.com/raw/3c08d7b04f6cc9ef82fef4273bf4107c.png)

部署成功后，会在云开发控制台看到版本状态为【正常】：

![](https://main.qcloudimg.com/raw/fbaf54c3e056714fb2a7fe44c679a8a3.png)

并且在 Eureka 控制台，可以看到有新的注册节点：

![](https://main.qcloudimg.com/raw/bb3abd669b8c15e576067b49f576ed46.png)

## 验证服务

访问 `hello-client` 的 HTTP 地址，可以看到如下输出：

![](https://main.qcloudimg.com/raw/f8e9882379c25e8089cd25e3dd52a7be.png)

[1]: https://github.com/TencentCloudBase/Cloudbase-Examples/tree/master/cloudbaserun/spring-cloud-docker-demo
