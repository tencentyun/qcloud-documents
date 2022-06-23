目前 StarRocks 支持多种方式连接，下面简介使用 mysql 客户端连接 StarRocks 进行开发。

## Root 用户登录
使用 MySQL 客户端连接某一个 FE 实例的 query_port(9030), StarRocks 内置 root 用户，密码默认与集群密码相同：
```shell
mysql -h fe_host -P9030 -u root -p
```
清理环境：
```sql
mysql > drop database if exists example_db;

mysql > drop user test;
```

## 查看部署节点
1. 查看 FE 节点。
```
mysql> SHOW PROC '/frontends'\G

************************* 1. row ************************
             Name: 172.16.139.24_9010_1594200991015
               IP: 172.16.139.24
         HostName: starrocks-sandbox01
      EditLogPort: 9010
         HttpPort: 8030
        QueryPort: 9030
          RpcPort: 9020
             Role: FOLLOWER
         IsMaster: true
        ClusterId: 861797858
             Join: true
            Alive: true
ReplayedJournalId: 64
    LastHeartbeat: 2020-03-23 20:15:07
         IsHelper: true
           ErrMsg:
1 row in set (0.03 sec)
```
Role 为 FOLLOWER 说明这是一个能参与选主的 FE；IsMaster 为 true，说明该 FE 当前为主节点。


2. 查看 BE 节点。
```
mysql> SHOW PROC '/backends'\G

********************* 1. row **********************
            BackendId: 10002
              Cluster: default_cluster
                   IP: 172.16.139.24
             HostName: starrocks-sandbox01
        HeartbeatPort: 9050
               BePort: 9060
             HttpPort: 8040
             BrpcPort: 8060
        LastStartTime: 2020-03-23 20:19:07
        LastHeartbeat: 2020-03-23 20:34:49
                Alive: true
 SystemDecommissioned: false
ClusterDecommissioned: false
            TabletNum: 0
     DataUsedCapacity: .000
        AvailCapacity: 327.292 GB
        TotalCapacity: 450.905 GB
              UsedPct: 27.41 %
       MaxDiskUsedPct: 27.41 %
               ErrMsg:
              Version:
1 row in set (0.01 sec)
```
如果 isAlive 为 true，则说明 BE 正常接入集群。如果 BE 没有正常接入集群，请查看 log 目录下的 be.WARNING 日志文件确定原因。


3. 查看 Broker 节点。
```
MySQL> SHOW PROC "/brokers"\G
*************************** 1. row ***************************
          Name: broker1
            IP: 172.16.139.24
          Port: 8000
         Alive: true
 LastStartTime: 2020-04-01 19:08:35
LastUpdateTime: 2020-04-01 19:08:45
        ErrMsg: 
1 row in set (0.00 sec)
```
Alive 为 true 代表状态正常。

## 创建新用户
通过下面的命令创建一个普通用户：
```sql
mysql > create user 'test' identified by '123456';
```

## 创建数据库
StarRocks 中 root 账户才有权建立数据库，使用 root 用户登录，建立 example\_db 数据库:
```sql
mysql > create database example_db;
```
数据库创建完成之后，可以通过 show databases 查看数据库信息：
```
mysql > show databases;

+--------------------+
| Database           |
+--------------------+
| example_db         |
| information_schema |
+--------------------+
2 rows in set (0.00 sec)
```
information_schema 是为了兼容 mysql 协议而存在，实际中信息可能不是很准确，所以关于具体数据库的信息建议通过直接查询相应数据库而获得。

## 账户授权
example_db 创建完成之后，可以通过 root 账户 example_db 读写权限授权给 test 账户，授权之后采用 test 账户登录就可以操作 example\_db 数据库了：
```sql
mysql > grant all on example_db to test;
```
退出 root 账户，使用 test 登录 StarRocks 集群：
```sql
mysql > exit

mysql -h 127.0.0.1 -P9030 -utest -p123456
```

## 建表
StarRocks 支持支持单分区和复合分区两种建表方式。
在复合分区中：
- 第一级称为 Partition，即分区。用户可以指定某一维度列作为分区列（当前只支持整型和时间类型的列），并指定每个分区的取值范围。
- 第二级称为 Distribution，即分桶。用户可以指定某几个维度列（或不指定，即所有 KEY 列）以及桶数对数据进行 HASH 分布。

以下场景推荐使用复合分区：
- 有时间维度或类似带有有序值的维度：可以以这类维度列作为分区列。分区粒度可以根据导入频次、分区数据量等进行评估。
- 历史数据删除需求：如有删除历史数据的需求（例如仅保留最近 N天的数据）。使用复合分区，可以通过删除历史分区来达到目的。也可以通过在指定分区内发送 DELETE 语句进行数据删除。
- 解决数据倾斜问题：每个分区可以单独指定分桶数量。如按天分区，当每天的数据量差异很大时，可以通过指定分区的分桶数，合理划分不同分区的数据,分桶列建议选择区分度大的列。

用户也可以不使用复合分区，即使用单分区。则数据只做 HASH 分布。
下面分别演示两种分区的建表语句：
1. 首先切换数据库：mysql > use example_db;
2. 建立单分区表建立一个名字为 table1的逻辑表。使用全 hash 分桶，分桶列为 siteid，桶数为10。这个表的 schema 如下：
	- siteid：类型是 INT（4字节）, 默认值为10。
	- city_code：类型是 SMALLINT（2字节）。
	- username：类型是 VARCHAR, 最大长度为32, 默认值为空字符串。
	- pv：类型是 BIGINT（8字节）, 默认值是0; 这是一个指标列, StarRocks 内部会对指标列做聚合操作, 这个列的聚合方法是求和（SUM）。这里采用了聚合模型，除此之外StarRocks 还支持明细模型和更新模型，具体参考 [数据模型介绍](https://docs.starrocks.com/zh-cn/main/table_design/Data_model)。
建表语句如下:
```sql
mysql >
CREATE TABLE table1
(
    siteid INT DEFAULT '10',
    citycode SMALLINT,
    username VARCHAR(32) DEFAULT '',
    pv BIGINT SUM DEFAULT '0'
)
AGGREGATE KEY(siteid, citycode, username)
DISTRIBUTED BY HASH(siteid) BUCKETS 10
PROPERTIES("replication_num" = "1");
```

3. 建立复合分区表
建立一个名字为 table2的逻辑表。这个表的 schema 如下：
	- event_day：类型是 DATE，无默认值。
	- siteid：类型是 INT（4字节）, 默认值为10。
	- city_code：类型是 SMALLINT（2字节）。
	- username：类型是 VARCHAR, 最大长度为32, 默认值为空字符串。
	- pv：类型是 BIGINT（8字节）, 默认值是0; 这是一个指标列, StarRocks 内部会对指标列做聚合操作, 这个列的聚合方法是求和（SUM）。
我们使用 event_day 列作为分区列，建立3个分区: p1, p2, p3
	- p1：范围为 \[最小值, 2017-06-30)。
	- p2：范围为 \[2017-06-30, 2017-07-31)。
	- p3：范围为 \[2017-07-31, 2017-08-31)。

 每个分区使用 siteid 进行哈希分桶，桶数为10。
建表语句如下:
```sql
CREATE TABLE table2
(
event_day DATE,
siteid INT DEFAULT '10',
citycode SMALLINT,
username VARCHAR(32) DEFAULT '',
pv BIGINT SUM DEFAULT '0'
)
AGGREGATE KEY(event_day, siteid, citycode, username)
PARTITION BY RANGE(event_day)
(
PARTITION p1 VALUES LESS THAN ('2017-06-30'),
PARTITION p2 VALUES LESS THAN ('2017-07-31'),
PARTITION p3 VALUES LESS THAN ('2017-08-31')
)
DISTRIBUTED BY HASH(siteid) BUCKETS 10
PROPERTIES("replication_num" = "1");
```
表建完之后，可以查看 example\_db 中表的信息:
```
mysql> show tables;

+-------------------------+
| Tables_in_example_db    |
+-------------------------+
| table1                  |
| table2                  |
+-------------------------+
2 rows in set (0.01 sec)


mysql> desc table1;

+----------+-------------+------+-------+---------+-------+
| Field    | Type        | Null | Key   | Default | Extra |
+----------+-------------+------+-------+---------+-------+
| siteid   | int(11)     | Yes  | true  | 10      |       |
| citycode | smallint(6) | Yes  | true  | N/A     |       |
| username | varchar(32) | Yes  | true  |         |       |
| pv       | bigint(20)  | Yes  | false | 0       | SUM   |
+----------+-------------+------+-------+---------+-------+
4 rows in set (0.00 sec)


mysql> desc table2;

+-----------+-------------+------+-------+---------+-------+
| Field     | Type        | Null | Key   | Default | Extra |
+-----------+-------------+------+-------+---------+-------+
| event_day | date        | Yes  | true  | N/A     |       |
| siteid    | int(11)     | Yes  | true  | 10      |       |
| citycode  | smallint(6) | Yes  | true  | N/A     |       |
| username  | varchar(32) | Yes  | true  |         |       |
| pv        | bigint(20)  | Yes  | false | 0       | SUM   |
+-----------+-------------+------+-------+---------+-------+
5 rows in set (0.00 sec)
```
