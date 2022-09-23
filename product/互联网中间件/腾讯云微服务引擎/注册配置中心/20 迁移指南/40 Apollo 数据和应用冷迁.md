## 适用场景

将自建的 Apollo 集群冷迁移到 TSE Apollo 集群。

## 迁移步骤

[](id:step1)
### 步骤1：TSE 创建 Apollo 实例

通过 TSE 管控页面创建 Apollo 实例，创建的环境信息需跟自建的 Apollo 一致。迁移整体思路是通过数据库层面的数据导入，所以在迁移过程中需要确保创建的 TSE Apollo 实例的数据库为空库。

[](id:step2)
### 步骤2：导出自建 Apollo 数据

#### 1. 导出 Portal 数据
<dx-codeblock>
:::  shell
mysqldump -t -uroot -p --databases ApolloPortalDB --tables App AppNamespace Authorities Consumer ConsumerRole ConsumerToken Favorite Permission Role RolePermission UserRole Users --complete-insert > portal_dump.sql
:::
</dx-codeblock>
<dx-alert infotype="explain" title="参数说明">
- **`-t`**：只导出数据，不导出表结构。
- **`--databases`**：指定导出的数据库名。
- **`--tables`**：指定导出的表。
- **`--complete-insert`**：导出的 insert 语句包含字段信息。


注意：替换用户名。
</dx-alert>


#### 2. 导出每个环境的 Config 数据
<dx-codeblock>
:::  shell
mysqldump -t -uroot -p --databases ApolloConfigDB --tables App AppNamespace  AccessKey Cluster Commit Item Namespace Release ReleaseHistory --complete-insert > config_${环境名}_dump.sql
:::
</dx-codeblock>
<dx-alert infotype="explain" title="参数说明">
- **`-t`**：只导出数据，不导出表结构。
- **`--databases`**：指定导出的数据库名。
- **`--tables`**：指定导出的表。
- **`--complete-insert`**：导出的 insert 语句包含字段信息。


注意：替换用户名以及导出的文件名中的环境信息。
</dx-alert>

ConfigDB 中包含所有历史发布的配置内容，所以数据量会比较大。
![](https://qcloudimg.tencent-cloud.cn/raw/98ef76ce659268f176a7d9027f942341.png)

以上图两个环境为例，将会导出三份数据：

- portal_dump.sql
- config_dev_dump.sql
- config_pro_dump.sql

### 步骤3：提腾讯云工单导入数据

可通过 [快速提工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=14&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&step=1)，联系腾讯云助手导入数据。其中需提供以下两个内容：

1. [步骤1](#step1) TSE 创建的 Apollo 实例 ID。
2. [步骤2](#step2) 导出的 SQL 文件。

腾讯云助手将会手工把数据导入到 TSE Apollo 的数据库中。至此，Apollo 的数据即已完成迁移。如果业务迁移过程中涉及到配置的变更，需要同时在自建的 Apollo 集群以及 TSE Apollo 集群修改、发布配置内容，确保两边数据一致性。



### 步骤4：业务应用迁移

#### 方式一：原地迁移（推荐）

原地迁移为在原有的服务上，通过逐步修改服务实例的 Apollo 地址来完成整体的迁移。整个过程如下所示：

**阶段一：服务全部实例指向自建 Apollo**

![](https://qcloudimg.tencent-cloud.cn/raw/e2cdc982dc78a9a947596538dcfe0f40.png)

**阶段二：迁移部分实例到 TSE Apollo**

![](https://qcloudimg.tencent-cloud.cn/raw/c3428948638f1bf3480c6859873f576c.png)

1. 迁移前，人工校验服务的配置内容两边是否一致
2. 修改业务应用配置的 Apollo 服务地址，灰度部分服务实例指向 TSE Apollo 集群的服务地址
3. 灰度一段时间之后，再迁移剩余的服务实例

如果迁移过程中业务出现问题，则及时回滚配置，连回自建 Apollo。

**阶段三：迁移全部实例到 TSE Apollo**

![](https://qcloudimg.tencent-cloud.cn/raw/d0f1b58b9af8091f676ec13069d318ca.png)

迁移过程中，如果有配置变更则需要同时修改自建 Apollo 和 TSE Apollo 的配置。

**阶段四：下线自建 Apollo**

![](https://qcloudimg.tencent-cloud.cn/raw/71ecb2d9048a42b7a64ee06434972441.png)

可以通过以下两种方式确认自建 Apollo 集群是否还有客户端使用：

1. 查看 ConfigService 机器 8080 端口的连接数是否为0，如果为0表示没有客户端连接
2. 查看 ConfigDB 的 Instance 表，确认近期没有客户端拉取配置

如果以上两点都确认完成之后，建议的下线自建 Apollo 集群的流程：

1. Kill ConfigService 的进程，不 Kill AdminService 和 Portal 的进程。ConfigService 用于对客户端提供服务，Kill ConfigService 就可认为切断整个 Apollo 服务。只 Kill ConfigService 进程为了下线过程中如果有残留客户端，则可以快速拉起 ConfigService 恢复，减少影响面。
2. 当第一步灰度一段时间之后（1周到1个月），再回收其它服务的资源。

#### 方式二：先扩容再缩容

先扩再缩的方式，总的来说先部署一组新的服务并指向 TSE Apollo，通过流量切换的方式把流量从老的服务实例迁移到新的服务实例。最后再缩容掉老的服务实例。

**阶段一：部署一组新的服务实例，流量指向老的服务实例**

![](https://qcloudimg.tencent-cloud.cn/raw/109f610bc5ca2efd9e7d0ac8e937895a.png)

**阶段二：流量切换到新的服务实例**

![](https://qcloudimg.tencent-cloud.cn/raw/aad436337cae323a474425d2bf685ebe.png)

如果流量切换之后发现业务异常，则切回老的服务实例。

**阶段三：缩容老的服务实例**

![](https://qcloudimg.tencent-cloud.cn/raw/6ef6de4684f3cf8459b13bf4af97dd23.png)

当阶段二运行一段时间之后，下线老的服务实例。方式二由于依赖流量切换能力、镜像部署一套服务占用额外的资源等劣势，所以建议优先使用方式一迁移。
