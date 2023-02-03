
## 操作场景
当您在生产环境上已经使用了自建的 Nacos 集群，并希望将其上已运行的服务迁移至腾讯云的 TSE Nacos 时，可以根据您的业务需求，在本指引中选择适合您的迁移方案。

本文主要介绍 TSE Nacos 冷迁移与热迁移的方案和操作步骤，帮助您将自建 Nacos 集群迁移到 TSE Nacos 集群。

## 迁移原理
Nacos 的核心功能为服务注册发现与配置管理，故一次完整的迁移任务涉及以下两方面：

- 配置数据迁移：Nacos 的配置数据、用户信息、命名空间数据、访问控制等信息在数据库中持久化存储，如果您的自建集群中已经存在配置数据，需要首先将自建集群中的持久化数据导入至 TSE Nacos。
	- 配置数据冷迁移：可以通过 Nacos 的配置数据导入功能，在迁移之初导入自建集群的持久化数据。
	- 配置数据热迁移：可以通过 TSE Nacos 的数据同步功能实现源数据库到 TSE Nacos 数据库的全量迁移与实时增量同步。
- 服务注册发现迁移：在服务注册发现迁移时，需要切换客户端的注册配置中心地址。
	- 服务冷迁移：如果您的业务可以进行停机迁移，可以直接将服务注册配置中心地址修改为 TSE Nacos。
	- 服务热迁移：通过双注册发现 Java agent 的方式，在不改变业务代码的情况下，通过字节码增强的方式实现服务的双注册和发现，以此达到运行中的服务平滑迁移的目的。



## 前提条件
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，新建一个 nacos 实例，并获取客户端访问地址。详细操作请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
![](https://qcloudimg.tencent-cloud.cn/raw/343ea18a5103e2a7529e1dcc74426d67.png)
2. 访问 [Github 地址](https://github.com/polarismesh/polaris-java-agent/releases/tag/v1.1.0-beta.0)，下载 Polaris Java Agent（支持 Nacos 双注册双发现）。
![](https://qcloudimg.tencent-cloud.cn/raw/53bb8ef2c64e23114e0b86d1c5eb2f35.png)

## 操作步骤

### 步骤一：配置数据迁移

**方式1：配置数据冷迁移**

1. 创建命名空间与权限控制信息

    在开始导入配置数据前，前往 TSE Nacos 原生控制台（访问方式请参见 [访问控制](https://cloud.tencent.com/document/product/1364/63998)），并根据您的业务需求，创建与自建集群相应的命名空间与权限控制信息。

2. 导出自建集群配置数据

    前往自建 Nacos 集群控制台，在配置列表中依次导出各个命名空间的配置数据。

3. 配置数据导入 TSE Naocs

    再次前往 TSE Nacos 原生控制台，在配置管理 - 配置列表中依次导入各个命名空间的配置数据。

**方式2：配置数据热迁移**

通过 TSE Nacos 的数据同步功能，将源 Nacos 数据库导入与同步至 TSE Nacos 集群。请参见 [Nacos 数据同步](https://cloud.tencent.com/document/product/1364/84650)。


### 步骤二：服务注册发现迁移

**方式1：服务冷迁移**
>? 请注意，服务冷迁移过程中将会导致业务不可用，如果您需要平滑迁移生产环境中的业务，建议采用服务热迁移。

1. 将当前注册至自建 Nacos 集群中的服务的注册地址改为 TSE Nacos 的客户端访问地址，并依次重新部署。

    如果您使用了域名访问，则无需重新部署服务，只需要更新域名对应的 Nacos 客户端访问 IP 即可。

2. 部署成功后，在 TSE Nacos 原生控制台的服务管理页面可以看到注册的服务。Nacos 原生控制台的访问方式请参见 [访问控制](https://cloud.tencent.com/document/product/1364/63998)。此时服务仅在 TSE Nacos 集群中进行了注册。

3. 持续观察一段时间，依次验证注册、发现、反注册，如果一切均正常，则可以下线自建的 Nacos 集群。如果您采用了配置数据热迁移，则可以终止数据同步任务。


**方式2：服务热迁移**

服务热迁移通过 Java Agent 字节码注入的方式，帮助您在不修改代码的情况下，同时将服务注册至自建集群与 TSE Nacos 集群，已达到服务迁移过程中不停机的效果。

**服务热迁移部署架构图**
![](https://qcloudimg.tencent-cloud.cn/raw/714c1489be567240072ae1802c5f85e3.png)

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




