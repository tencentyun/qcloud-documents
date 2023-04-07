
## 操作场景
当您在生产环境上已经使用了自建的 Nacos 集群，并希望将其上已运行的服务迁移至腾讯云的 TSE Nacos 时，可以通过本指引进行服务注册发现的平滑迁移，以保证在迁移过程中不影响现网服务的可用性和稳定性。

本文主要介绍 TSE Nacos 通过双注册双发现实现服务平滑迁移的迁移方案和操作步骤，帮助您将自建 Nacos 集群平滑迁移到 TSE Nacos 集群。

## 迁移原理
Nacos 的核心功能为服务注册发现与配置管理，故一次完整的迁移任务涉及以下两方面：

- 配置管理热迁移：Nacos 的配置数据、用户信息、命名空间数据、访问控制等信息在数据库中持久化存储，因此首先需要使用 TSE Nacos 的数据同步功能实现源数据库到 TSE Nacos 数据库的全量迁移与实时增量同步。
- 服务注册发现热迁移：采用 Java agent 的形式，在不改变业务代码的情况下，通过字节码增强的方式，实现服务的双注册和发现，以此达到运行中的服务平滑迁移的目的。


## 架构图

![](https://qcloudimg.tencent-cloud.cn/raw/714c1489be567240072ae1802c5f85e3.png)

## 前提条件
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，新建一个 nacos 实例，并获取客户端访问地址。详细操作请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
![](https://qcloudimg.tencent-cloud.cn/raw/343ea18a5103e2a7529e1dcc74426d67.png)
2. 访问 [Github 地址](https://github.com/polarismesh/polaris-java-agent/releases/tag/v1.1.0-beta.0)，下载 Polaris Java Agent（支持 Nacos 双注册双发现）。
![](https://qcloudimg.tencent-cloud.cn/raw/53bb8ef2c64e23114e0b86d1c5eb2f35.png)

## 操作步骤

### 步骤1：配置数据同步
通过 TSE Nacos 的数据同步功能，将源 Nacos 数据库导入与同步至 TSE Nacos 集群。请参见 [Nacos 数据同步](https://cloud.tencent.com/document/product/1364/84650)。

### 步骤2：服务注册发现迁移
1. 将提前下载好的 polaris java agent zip 包上传到您的服务所部署的云服务器 CVM 或者容器中，并解压，确认该位置可以被正常访问。
2. [](id:step2)依次将当前注册至自建 Nacos 集群中的服务重新部署并双注册至 TSE Nacos，部署时需要添加如下参数。
<dx-codeblock>
:::  sh
-javaagent:/***/polaris-java-agent-v*/polaris-java-agent-bootstrap.jar  -Dtarget.nacos.server.addr=**.**.***.**
:::
</dx-codeblock>
>?三处`*`分别表示 polaris java agent zip 所在的目录路径、版本号和 TSE Nacos 客户端访问地址。
3. 部署成功后，在 TSE Nacos 原生控制台的服务管理页面可以看到注册的服务。Nacos 原生控制台的访问方式请参见 [访问控制](https://cloud.tencent.com/document/product/1364/63998)。此时服务在自建 Nacos 集群和 TSE Nacos 集群中均进行了注册。
4. 观察自建的 Nacos 集群和 TSE 的 Nacos 集群，依次验证下注册、发现、反注册，看是否均符合预期。待所有服务均重新部署完毕后，在自建 Nacos 集群和 TSE Nacos 集群的控制台均能看到所有服务以及其下的实例信息。
5. 重复上面的步骤，依次再次部署服务。部署时需要移除 [步骤2](#step2) 中添加的参数，并且将服务中原有的自建 Nacos 集群访问地址更新成 TSE Nacos 集群的客户端访问地址，此时用户的服务只在 TSE Nacos 集群中进行了注册。
>?如果您使用了域名访问，则无需重新部署服务，只需要更新域名对应的 Nacos 客户端访问 IP 即可。
6. 持续观察一段时间，如果一切均正常，则可以下线自建的 Nacos 集群，并终止配置数据同步任务。


 





