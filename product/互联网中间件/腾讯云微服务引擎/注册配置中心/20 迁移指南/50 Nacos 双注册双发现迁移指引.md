
## 操作场景
当用户在生产环境上已经使用了自建的 Nacos 集群，想要将其上已运行的服务迁移到腾讯云的 TSE Nacos 集群上来时，需要保证在迁移过程中不影响现网服务的可用性和稳定性，从而做到平滑迁移，此时就需要使用到 **Nacos 双注册双发现迁移工具**。

本文主要介绍 TSE Nacos 双注册双发现迁移的功能原理，迁移方案和操作方法，帮助您快速平稳地将自建 Nacos 集群迁移到 TSE Nacos 集群。

## 迁移原理
Nacos 的核心功能主要是服务注册发现和配置管理，故热迁移需要包含这两种能力的平滑迁移。

- 服务注册发现热迁移：采用 Java agent 的形式，在不改变用户服务代码的情况下，通过字节码增强的方式，实现服务的双注册和发现，以此达到平滑迁移的目的。
- 配置管理热迁移：Nacos 的配置数据是持久化存储 DB 里面的，故首先需要实现 DB 数据的实时同步，其次 SDK 访问配置，会涉及到查询文件缓存，故需要实现 Nacos 集群节点的文件缓存实时更新。
 - DB 数据实时同步：采用腾讯云的 DTS 的数据同步服务，将源 Nacos 的 DB 以全量+增量的形式同步到目标 Nacos 的 DB。
 - Nacos 集群节点文件缓存更新：采用自研的配置同步服务以全量+增量的方式定时更新文件缓存。

## 架构图

### 注册发现迁移
![](https://qcloudimg.tencent-cloud.cn/raw/714c1489be567240072ae1802c5f85e3.png)

### 配置数据迁移
![](https://qcloudimg.tencent-cloud.cn/raw/74cc4d6c55630a5b04c55bec3695f528.png)

## 前提条件
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，新建一个 nacos 实例，并获取客户端访问地址。详细操作请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
![](https://qcloudimg.tencent-cloud.cn/raw/343ea18a5103e2a7529e1dcc74426d67.png)
2. 访问 [Github 地址](https://github.com/polarismesh/polaris-java-agent/releases/tag/v1.1.0-beta.0)，下载 Polaris Java Agent（支持 Nacos 双注册双发现）。
![](https://qcloudimg.tencent-cloud.cn/raw/53bb8ef2c64e23114e0b86d1c5eb2f35.png)

## 操作步骤
### 注册发现热迁移
1. 将提前下载好的 polaris java agent zip 包上传到部署 Nacos 服务所在的云服务器 CVM 或者容器中，并解压，可以被正常访问。
2. [](id:step2)依次将自建 Nacos 集群中运行的服务部署到 TSE Nacos 集群中，部署时需要添加如下参数。
<dx-codeblock>
:::  sh
-javaagent:/***/polaris-java-agent-v*/polaris-java-agent-bootstrap.jar  -Dtarget.nacos.server.addr=**.**.***.**
:::
</dx-codeblock>
>?三处`*`分别表示 polaris java agent zip 所在的目录路径、版本号和 TSE Nacos 客户端访问地址。
3. 部署成功后，在 Nacos 原生控制台的服务管理页面可以看到注册好的服务。Nacos 原生控制台的访问方式请参见 [访问控制](https://cloud.tencent.com/document/product/1364/63998) 。此时服务在自建 Nacos 集群和 TSE Nacos 集群中均进行了注册。
4. 观察自建的 Nacos 集群和 TSE 的 Nacos 集群，依次验证下注册、发现、反注册，看是否均符合预期。待所有服务均重新部署完毕后，在自建 Nacos 集群和 TSE Nacos 集群的控制台均能看到所有服务以及其下的实例信息。
5. 重复上面的步骤，再次部署服务。部署时需要移除 [步骤2](#step2) 中添加的参数，并且将服务中原有的自建 Nacos 集群访问地址更新成 TSE Nacos 集群的客户端访问地址，此时用户的服务只在 TSE Nacos 集群中进行了注册。
>?如果用户使用了域名访问，则无需重新部署服务，只需要更新域名对应的 Nacos 客户端访问 IP 即可。
6. 持续观察一段时间，如果一切均正常，则可以下线自建的 Nacos 集群。

### 配置迁移
1. 新建 DTS 数据同步任务。
	1. 用户提供 MySQL 的实例 ID、用户名、密码，还需要用户在腾讯云上面授权访问 MySQL 的权限。授权相关操作请参见 [云数据库跨账号实例间同步](https://cloud.tencent.com/document/product/571/68729) 中的授权账号章节。
	2. TSE 研发同学在 [数据同步](https://console.cloud.tencent.com/dts/replication) 页面新建数据同步任务，填写相关信息之后，启动任务，此时就会进行源 DB 到目标 DB 的数据实时同步。
2. 部署 Nacos-config-sync 服务。此服务由 TSE 研发侧部署，用户无需关注，在此不做详细介绍。
3. 等用户注册发现迁移完毕之后，即可以停止此服务。


 





