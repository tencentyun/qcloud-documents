Presto 是一个开源的分布式 SQL 查询引擎，适用于交互式分析查询，数据量支持 GB 到 PB 字节。Presto 的设计和编写是为了解决大规模的甚至超大规模商业数据仓库的交互式分析和处理速度的问题。Presto 支持在线数据查询，包括 Hive, Cassandra, 关系数据库以及专有数据存储。一条 Presto 查询可以将这些多个数据源的数据进行合并，可以跨越整个组织进行分析。

MR 把 Presto 原生 Web UI 代理了出来，可以直接在 EMR 控制台查看。查看方法为进入 EMR 控制台详情页面的快捷入口切页，单击 Presto 的入口即可。登录用户名为 root，密码为创建集群时设置的密码。如下图

![登录](https://mc.qcloudimg.com/static/img/9d0b33741cb53c9a78f30f0b98e7bba6/5-6-1.png)
