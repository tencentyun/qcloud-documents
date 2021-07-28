## 使用 Phoenix salted 表
Hbase 的 Row Key 假如没有经过精心设计，如果它又是自增长的，那么顺序写很可能会导致热点问题。PHoenix 提供了一种透明的方法，关联 salt 和 RowKey 到一张指定表的方案。只需要在创建表的时候添加 SALT_BUCKETS 关键字，这个值的范围是1到256。例如：
``` sql
0: jdbc:phoenix:>CREATE TABLE table (a_key VARCHAR PRIMARY KEY, a_col VARCHAR) SALT_BUCKETS = 20;
```
可以免除使用 Hbase API 时需要精心设计 RowKey 的麻烦。如果用户对 Hbase Row Key 的设计理解不够，建议使用 salted 表。Phoenix 官方提供的写和查询，salted 表和非 salted 表性能对比：
![salted 表性能](https://mc.qcloudimg.com/static/img/8381e5a72ea654a488dd29b5d0effccf/5-4-4.png)  
更多 salte 性能或者操作说明，可查看 Phoenix salted 表 [社区文档](http://phoenix.apache.org/salted.html)。

## Phoenix 二级索引
对于 HBase 而言，如果想精确地定位到某行记录，唯一的办法是通过 rowkey 来查询。如果不通过 rowkey 来查找数据，就必须逐行地比较每一列的值，即全表扫瞄。对于较大的表，全表扫瞄的代价是不可接受的。但是，很多情况下，需要从多个角度查询数据。这需要二级索引（secondary index）来完成这件事。二级索引的原理很简单，但是如果自己维护的话则会麻烦一些。

## Phoenix 二级索引配置
EMR 中 Phoenix 直接可支持 Phoenix 的二级索引。如果需要使用非事务性的，可变的索引只需按照以下步骤配置即可。打开 EMR 组件管理页面，单击【Hbase】，选择【配置】>【配置管理】，增加 hbase-site.xml 的 `hbase.regionserver.wal.codec`、`hbase.region.server.rpc.scheduler.factory.class` 和 `hbase.rpc.controllerfactory.class` 三个配置项即可，详细配置如下：
 ``` xml
    <property>
      <name>hbase.regionserver.wal.codec</name>
      <value>org.apache.hadoop.hbase.regionserver.wal.IndexedWALEditCodec</value>
      </property>
    <property>
      <name>hbase.region.server.rpc.scheduler.factory.class</name>
      <value>org.apache.hadoop.hbase.ipc.PhoenixRpcSchedulerFactory</value>
      <description>Factory to create the Phoenix RPC Scheduler that uses separate queues for index and metadata updates</description>
    </property>
    <property>
      <name>hbase.rpc.controllerfactory.class</name>
      <value>org.apache.hadoop.hbase.ipc.controller.ServerRpcControllerFactory</value>
      <description>Factory to create the Phoenix RPC Scheduler that uses separate queues for index and metadata updates</description>
    </property>
```

## Phoenix 二级索引使用
创建二级索引，命令如下：
``` sql
0: jdbc:phoenix:>CREATE INDEX my_index ON my_table (v1) INCLUDE (v2)；
```
更多二级索引操作说明，可查看 [Phoenix 二级索引社区文档](http://phoenix.apache.org/secondary_indexing.html)。
