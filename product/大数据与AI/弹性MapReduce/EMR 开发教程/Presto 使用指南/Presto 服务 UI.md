Presto 是一个开源的分布式 SQL 查询引擎，适用于交互式分析查询，数据量支持 GB 到 PB 字节。Presto 的设计和编写是为了解决大规模的甚至超大规模商业数据仓库的交互式分析和处理速度的问题。

Presto 支持在线数据查询，包括 Hive、Cassandra、关系数据库以及专有数据存储。一条 Presto 查询可以将这些多个数据源的数据进行合并，可以跨越整个组织进行分析。

EMR 代理了 Presto 原生 Web UI，可以直接在 EMR 控制台查看。登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，单击集群实例 ID，进入实例管理页面。单击左侧菜单栏【集群服务】，即可看到【WebUI 地址】页面快捷入口，单击 Presto 的入口即可。登录用户名为 root，密码为创建集群时设置的密码。如下图：
![](https://main.qcloudimg.com/raw/7961cafd57edce116106fc6ee0132698.png)
访问地址需要进行身份验证，用户名为 root，默认密码为创建集群时输入的密码，如需修改密码，可在该页面中单击【重置原生UI密码】进行修改。
