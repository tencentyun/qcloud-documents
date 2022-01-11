本文介绍如何将 [COS（腾讯云对象存储）](https://cloud.tencent.com/product/cos)数据导入到云数据仓库 ClickHouse。

## 前提条件
1. 数据源 COS 和云数据仓库 ClickHouse 集群须在同一个 VPC 下。
2. 表函数中填写的 acces-key-id、access-key-secret 必须对相应的 oss-file-path 有读取权限。
3. oss-file-path 参数的格式需要满足 OSS 路径规范，一般格式为 oss://<bucket-name/<path-to-file> 。

## 操作步骤
以下例子可以作为从 S3系统（本文以 COS 为例）将数据导入到云数据仓库 ClickHouse 的参考。
1. 登陆云数据仓库 ClickHouse ，创建 S3表。
```
CREATE TABLE cos_engine_table
(
    `int_id` UInt32
)
ENGINE = S3('http://clickhouse-xxx.myqcloud.com/clickhouse-xxx/cos/data.csv.gz', 'CSV', 'gzip')
```
 - S3引擎参数参考。
S3 表引擎提供与 Amazon S3生态系统的集成。其参数格式为：S3(path, [aws_access_key_id, aws_secret_access_key,] format, [compression])。
	- path — 带有文件路径的 Bucket url。在只读模式下支持以下通配符: *, ?, {abc,def} 和 {N..M} 其中 N, M 是数字, 'abc', 'def' 是字符串；
	- format — 文件的格式。
	- aws_access_key_id，aws_secret_access_key — COS对象存储账号的长期凭证。你可以使用凭证来对你的请求进行认证，参数是可选的。如果没有指定凭据，将从配置文件中读取凭据。更多信息参见 使用 S3 来存储数据。
	- compression — 压缩类型。支持的值： none， gzip/gz， brotli/br， xz/LZMA， zstd/zst。 参数是可选的， 默认情况下，通过文件扩展名自动检测压缩类型。

2. 创建目标表。

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
create table test.test_dis on cluster default_cluster
AS test.test
engine = Distributed('default_cluster', 'test', 'test', rand());
```

3. 向目标表写入数据。
```
INSERT INTO test.test SELECT * FROM cos_engine_table;
```

4. 查询。
```
select * from test.test
```
