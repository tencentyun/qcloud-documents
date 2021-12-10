## 操作场景

微服务引擎 TSE 提供将 K8s 集群关联到 Polarismesh 的能力，Polaris Controller 可以同步您 Kubernetes 集群上的 Namespace，Service，Endpoints 等资源到 Polaris 中，从而实现 K8s Service 自动注册到 Polarismesh ，使用 Polarismesh API 和多语言 SDK 可以访问，使用 gRPC 和 Spring Cloud 等开源框架也可以访问。主要适用于以下场景：
场景一：异构系统与多技术栈场景下，SpringCloud等框架服务调用 K8s 集群服务。
场景二：跨集群场景下的服务调用。

本文介绍通过 TSE 控制台使用 K8s 集群的能力。


## 操作步骤

### 创建引擎

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 在**治理中心**下的 **polarismesh** 页面，单击**新建**。

3. 在新建治理中心页，根据自身业务需求选择相关配置。

   > ？
   >
   > TSE治理中心默认支持同城多活高可用架构。
   
   ![](https://qcloudimg.tencent-cloud.cn/raw/b244f11147c8cc0b1d1c1c926ba1986d.png)

4. 单击**提交**，完成服务治理中心引擎创建。

5. 在 **polarismesh** 页面，您可以查看到引擎创建的进度。
   ![](https://qcloudimg.tencent-cloud.cn/raw/85190ace53b2ec2a7142dfc180cb6a5b.png)

6. 引擎实例创建完成后，点击引擎实例 ID，可以查看引擎详情。

### 访问方式
在引擎详情页的**基本信息**中，可以查看到引擎访问方式，客户端可通过配置服务端地址访问引擎。
![](https://qcloudimg.tencent-cloud.cn/raw/e796c879bd923851ed291a1633f6c350.png)
如 Java 应用，使用 polaris-java sdk 的方式，可在应用的 classpath 当前目录下，添加 polaris.yml 文件，配置服务端地址信息
```
global:
  serverConnector:
    addresses:
    - 10.10.0.31:8090
```

### 销毁引擎

> ！
>
> 服务治理中心引擎销毁后，治理中心服务不可用且数据销毁，该操作不可逆，请谨慎操作。

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，找到目标引擎，单击操作列的**删除**。
   ![img](https://qcloudimg.tencent-cloud.cn/raw/1788c5c442064c1b6d23bab4c3d1f2be.png)
3. 在二次确认的弹框中单击**删除**，完成服务治理中心引擎销毁。



