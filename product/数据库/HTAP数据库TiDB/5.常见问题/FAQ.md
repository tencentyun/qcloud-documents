### HTAP Database for TiDB 是基于 MySQL 开发的吗？

不是，但是HTAP Database for TiDB 支持 MySQL 语法和协议。

### 用起来简单吗？

是的，HTAP Database for TiDB 用起来很简单。启动整套服务后，就可以将 HTAP Database for TiDB 当做一个普通的 MySQL Server 来用，您可以将 HTAP Database for TiDB 用在任何以 MySQL 作为后台存储服务的应用中，基本上不需要修改应用代码，并且兼容大部分 MySQL 管理工具。

### 适用的场景？
原业务的 MySQL 的业务遇到单机容量或者性能瓶颈时，可以考虑使用 HTAP Database for TiDB 无缝替换 MySQL。

### 如何将运行在 MySQL 上的应用迁移到 HTAP Database for TiDB 上？

HTAP Database for TiDB 支持绝大多数 MySQL 语法，一般不需要修改代码，可以用工具Checker检查 MySQL 中的 Schema 是否兼容。

### 如何通过扩展 HTAP Database for TiDB 提高性能？

随着业务不断增长时，数据库可能会面临三方面瓶颈：

- 第一是存储资源不够，也就是磁盘空间不够；
- 第二是计算资源不够用，如 CPU 占用较高， 
- 第三是吞吐跟不上。

这时可以对数据库集群做水平扩展。

- 如果是存储资源不够，可以通过添加 TiKV Server 节点来解决。新节点启动后，PD 会自动将其他节点的部分数据迁移过去，无需人工介入。
- 如果是计算资源不够，可以查看 TiDB 节点 和 TiKV 节点的 CPU 消耗情况，再考虑添加 TiDB  节点或者是 TiKV 节点来解决。
- 如果是吞吐跟不上，一般可以考虑同时增加 TiDB 节点 和 TiKV 节点。



