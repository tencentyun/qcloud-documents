## Ranger 简介
Ranger 是大数据领域的一个集中式安全管理框架，实现对 Hadoop 生态组件的集中式安全管理。用户可以通过 Ranger 实现对集群中数据的安全访问，它主要是对 Hadoop 平台组件进行监管、启动服务以及资源访问进行控制，其核心思想为：
- 用户可以使用 Ranger 提供的 REST API 或者使用 Ranger 提供 Web UI 对大数据组件进行集中化管理。
- 可以针对大数据组件进行基于角色、属性进行授权。
- 针对大数据组件所涉及到安全的审计进行集中管理。

## Ranger 架构
Ranger 主要是由 Ranger Admin、Ranger UserSync、Ranger Plugin 三个组件构成的，其中 Ranger Admin、Ranger UserSync 都是一个单独的 JVM 进程，而 Ranger Plugin 需要根据不同组件安装在不同节点上。

![](https://main.qcloudimg.com/raw/0da76efca9b7bbf806f287116112193a.png)
- Ranger Admin：管理用户配置好的策略及创建的服务、审计日志及 Report、将配置好的策略及创建的服务持久化到数据库中并提供给 Plugin 定期查询。
- Ranger UserSync：将 LDAP、File、Unix 的相关信息同步到 Ranger Admin 中，例如，将用户的 LDAP 目录访问系统或者 Unix 中用户的信息及组信息进行同步，同步 Unix 用户及组信息需要开启 unixAuthenticationService 进程，同时对同步过来的信息进行持久化。
- Ranger Plugin：Plugin 会被部署在需要的服务节点中，并会定期到 Ranger Admin 同步策略信息。

组件集成 Ranger 请参照如下表格：

| **Service** | **install Node**     | **EMR 版本**       |
| ----------- | -------------------- | ----------------- |
| HDFS        | NameNode             | EMR-V 2.0.1 及以上版本 |
| Hbase       | Master、RegionServer | EMR-V 2.0.1 及以上版本 |
| Hive        | HiveServer2          | EMR-V 2.0.1 及以上版本 |
| Yarn        | ResourceManager      | EMR-V 2.0.1 及以上版本 |
| Presto      | All Coordinator      | EMR-V 2.0.1 及以上版本 |
| Impala      | All Daemon           | EMR-V 2.2.0 及以上版本 |
| Kudu        | All Master           | EMR-V 3.2.0 版本      |

