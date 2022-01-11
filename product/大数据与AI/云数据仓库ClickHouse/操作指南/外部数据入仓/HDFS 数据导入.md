本文介绍如何从 [HDFS](https://cloud.tencent.com/product/chdfs) 中导入数据到云数据仓库 ClickHouse。

## 前提条件
1. 访问 HDFS 的数据需要具备对 HDFS 的读权限。如何设置权限，请参见访问控制概述。
2. 确保 HDFS 的实例和云数据仓库 ClickHouse 集群处在相同 VPC 中。

## 操作步骤
1. 登录云数据仓库 ClickHouse ，创建 HDFS 表。
```
CREATE TABLE hdfs_engine_table
(
    `int_id` UInt32
)
ENGINE = ENGINE=HDFS('hdfs://hdfs1:9000/other_storage', 'TSV')
```
<dx-alert infotype="explain" title="参考">
ENGINE = HDFS(URI, format)
URI 参数是 HDFS 中整个文件的 URI。 format 参数指定一种可用的文件格式，更多格式参考 [输入/输出格式](https://clickhouse.com/docs/zh/interfaces/formats/#formats)。 路径部分 URI 可能包含 glob 通配符。 在这种情况下，表将是只读的。
</dx-alert>



2. 创建 ClickHouse 目标表。
	- 如果您的集群是单副本版：
```
CREATE TABLE test.test on cluster default_cluster
(
    `int_id` UInt32
)
engine = MergeTree()
order by int_id;
```
	- 如果您的集群是双副本版：
```
create table test.test on cluster default_cluster
(
    `int_id` UInt32
)
engine = ReplicatedMergeTree('/clickhouse/tables/test/test/{shard}', '{replica}')
order by int_id;
```
	- 创建分布式表：
```
create table test.test_dis on cluster default
AS test.test
engine = Distributed('default_cluster', 'test', 'test', rand());
```
3. 向目标表写入数据。
```
INSERT INTO test.test SELECT * FROM hdfs_engine_table;
```
4. 查询数据。
```
select * from test.test
```

