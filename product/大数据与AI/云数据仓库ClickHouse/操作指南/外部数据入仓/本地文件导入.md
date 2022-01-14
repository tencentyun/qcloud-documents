本文介绍如何把本地文件的数据导入到云数据仓库 ClickHouse。

## 前提条件
1. 已经安装 clickhouse-client，没有安装可点击[下载](https://repo.yandex.ru/clickhouse/rpm/stable/x86_64/)并安装。
2. 支持导入到云数据仓库 ClickHouse 的常见文件格式为 TabSeparated、TabSeparatedRaw、TabSeparatedWithNames、TabSeparatedWithNamesAndTypes、Template、CSV和CSVWithNames 等。更多支持的文件格式，请参见[文件格式及说明](https://clickhouse.com/docs/zh/interfaces/formats/#tabseparated)。
3. 确保 clickhouse-client 所在的本地服务器和云数据仓库 ClickHous 集群处于同一 VPC 下。

>!
- 不同的客户端和服务器版本彼此兼容，但是一些特性可能在旧客户机中不可用。我们建议使用与服务器应用相同版本的客户端。当您尝试使用旧版本的客户端时，服务器上的 clickhouse-client 会显示如下信息: “ClickHouse client version is older than ClickHouse server. It may lack support for new features.”可使用如下命令进行导入：`cat <data_file> | ./clickhouse-client --host=<host> --port=<port> --user=<username> --password=<password> --query="INSERT INTO <table_name> FORMAT <format>";`
- 在批量模式中，默认的数据格式是 TabSeparated 分隔的。您可以根据查询来灵活设置 FORMAT 格式。
默认情况下，在批量模式中只能执行单个查询。为了从一个 Script 中执行多个查询，可以使用--multiquery 参数。除了 INSERT 请求外，这种方式在任何地方都有用。查询的结果会连续且不含分隔符地输出。 同样的，为了执行大规模的查询，您可以为每个查询执行一次 clickhouse-client。但注意到每次启动 clickhouse-client 程序都需要消耗几十毫秒时间。

## 操作步骤
以下以本地文件 test.csv 为例说明整个数据导入的过程。
1. 准备本地文件 test.csv，并写入数据如下。
```
$ cat /test.csv
    1,2,3
    3,2,1
    78,43,45
```
2. ClickHouse 目标表创建。
    - 如果您的集群是单副本版：
```
CREATE TABLE test.test on cluster default_cluster
(
    `column1` UInt32,
    `column2` UInt32,
    `column3` UInt32
)
engine = MergeTree()
order by column1;
```
    - 如果您的集群是双副本版：
```
create table test.test on cluster default_cluster
(
    `column1` UInt32,
    `column2` UInt32,
    `column3` UInt32
)
engine = ReplicatedMergeTree('/clickhouse/tables/test/test/{shard}', '{replica}')
order by column1;
```
    - 创建分布式表：
```
create table test.test_dis on cluster default
AS test.test
engine = Distributed('default_cluster', 'test', 'test', rand());
```


3. 向目标表写入数据。
```
cat data.csv | clickhouse-client --query="INSERT INTO test FORMAT CSV"
```

4. 查询。
```
select * from test;
```
