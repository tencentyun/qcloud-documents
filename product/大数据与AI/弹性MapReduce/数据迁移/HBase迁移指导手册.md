Hbase 表是基于 hadoop HDFS 构建，所以 Hbase 的迁移可从两个维度来看，基于 hadoop HDFS 的 distcp 的迁移方式和基于 Hbase 表结构的 Hbase 层面提供的相关工具迁移。
 ![](https://main.qcloudimg.com/raw/36f02c654c9434b2ec5db05d77781b56.png)
如上图所示，HBase 迁移有多种方案，其中基于 Snapshot 的迁移方式是推荐的迁移方案。

### HBase 基于 Snapshot 迁移
1. 在新集群上建立表结构一样的表。
2. 使用`hbase shell`在原始集群中创建一个快照。
```
$ ./bin/hbase shell  
hbase>snapshot 'myTable', 'myTableSnapshot'  
```
这里`'myTable'`是 hbase 的表名， `'myTableSnapshot'`是快照的名称。创建完成后可使用 list_snapshots 确认是否成功，或使用 delete_snapshot 删除快照。
```
hbase> delete_snapshot 'myTableSnapshot'  
```
3. 在源集群中导出快照到目标集群。
```
hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot -snapshot myTableSnapshot -copy-to hdfs://10.0.0.38:4007/hbase/snapshot/myTableSnapshot  
```
这里`10.0.0.38:4007`是目标集群的`$activeip:$rpcport`，导出快照时系统级别会启动一个 mapreduce 的任务，可以在后面增加`-mappers 16 -bandwidth 200`来指定 mapper 和带宽。这里200指的是200MB/sec。
4. 快照还原到目标集群的目标 HDFS，在目标集群中执行如下命令。
```
hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot -snapshot myTableSnapshot -copy-from /hbase/snapshot/myTableSnapshot -copy-to /hbase/  
```
5. 在目标集群从 hdfs 恢复相应的 hbase 表及数据。
```
hbase> disable "myTable"  
hbase> restore_snapshot 'myTableSnapshot'  
hbase> enable 'myTable'  
```
6. 最后可通过简单的 HBase 表操作进行测试。
