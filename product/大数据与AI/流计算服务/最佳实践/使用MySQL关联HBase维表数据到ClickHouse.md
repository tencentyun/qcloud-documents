本文介绍了结合 MySQL 数据库、流计算 Oceanus、HBase 以及云数据仓库 ClickHouse 来构建实时数仓，并通过流计算 Oceanus 读取 MySQL 数据、关联 HBase 中的维表，最终将数据存入云数据仓库 ClickHouse 进行指标分析，实现完整实时数仓的全流程操作指导。

## 环境搭建
### 创建 Oceanus 集群
在 [流计算 Oceanus](https://console.cloud.tencent.com/oceanus/cluster) 控制台的**集群管理 > 新建集群**创建集群，选择地域、可用区、VPC、日志、存储、设置初始密码等。创建完后的集群如下：
>?
>- 若未使用过 VPC、日志、存储这些组件，需要先进行创建。
>- VPC 及子网需要和下面的 MySQL、EMR 集群使用同一个，否则需要手动打通（如对等连接）。

![](https://main.qcloudimg.com/raw/6dafa64073856583ce73ca85c7505e6b.png)

### 创建 VPC 私有网络
私有网络是一块您在腾讯云上自定义的逻辑隔离网络空间，在构建 MySQL、EMR、ClickHouse 集群等服务时选择的网络必须保持一致，网络才能互通，否则需要使用对等连接、VPN 等方式打通网络。

登录 [私有网络](https://console.cloud.tencent.com/vpc/vpc) 控制台，选择**私有网络 > +新建**，新建私有网络。
![](https://main.qcloudimg.com/raw/374c44a898b8fdb3c087900f9cc60ef9.png)![](https://main.qcloudimg.com/raw/3c7bd8b879b0fe89f5ff8a191e00be53.png)

### 创建云数据库 MySQL 服务
云数据库 MySQL（TencentDB for MySQL）是腾讯云基于开源数据库 MySQL 专业打造的高性能分布式数据存储服务，让用户能够在云中更轻松地设置、操作和扩展关系数据库。

登录 [云数据库 TencentDB](https://console.cloud.tencent.com/cdb) 控制台，选择**实例列表 > 新建**，新建实例。
![](https://main.qcloudimg.com/raw/5a38fde7d122e0e62cead18fb9f6b3f3.png)
**新建 MySQL 服务时，网络需要选择之前创建的。**
![](https://main.qcloudimg.com/raw/84304e9f282e3bc19ee01bb71598e5a9.png)
创建完 MySQL 服务后，需要修改 binlog 参数，如图修改为 FULL（默认值为 MINIMAL）。
![](https://main.qcloudimg.com/raw/1d9f3bc9e4c891e721982cbf468aba83.png)
修改完参数后，登录 MySQL 创建示例所需要的数据库和数据库表。

#### 创建数据库 mysqltestdb
登录 MySQL 创建示例所需要的数据库。
![](https://main.qcloudimg.com/raw/357959ba1fb1b659063bf09a150add3b.png)
打开 SQL 窗口或者单击可视化页面创建数据库及表。

#### 新建数据库
```
create database mysqltestdb;
```
在新建的数据库上新建表 student：
```
create table `student` (
  `id` int(11) not null auto_increment comment '主键id',
  `name` varchar(10) collate utf8mb4_bin default '' comment '名字',
  `age` int(11) default null comment '年龄',
  `create_time` timestamp null default current_timestamp comment '数据创建时间',
  primary key (`id`)
) engine=innodb auto_increment=4 default charset=utf8mb4 collate=utf8mb4_bin row_format=compact comment='学生表'
```

#### Student 表中插入数据
```
 insert into mysqltestdb.student(id,name,age) values(1,“xiaomin”,20);
```

### 创建 EMR 集群
弹性 MapReduce 是云端托管的弹性开源泛 Hadoop 服务，支持 Spark、HBase、Presto、Flink、Druid 等大数据框架，本次示例主要需要使用 HBase 组件。
1. 登录 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr)，选择**集群列表 > 新建集群**，开始新建集群，具体可参考 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。新建集群时，需选择安装 HBase 组件。
![](https://main.qcloudimg.com/raw/b8de93e041489aed3d8d9f847bd32f95.png)
如果是生产环境，服务器配置可根据实际情况选择。网络需要选择之前创建好的 VPC 网络，始终保持服务组件在同一 VPC 下。
![](https://main.qcloudimg.com/raw/a3a63a677543d6b0f1218ff622861ced.png)
2. 在集群列表中，单击新建的集群 **ID/名称**，进入集群详情页。选择**集群资源 > 资源管理**，即进入 HBase 的 Master 节点。
![](https://main.qcloudimg.com/raw/0aed82b69a85b438530a375a4a355493.png)
3. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，搜索 EMR **实例 ID**，然后单击**登录**进入服务器。
![](https://main.qcloudimg.com/raw/b0bb39c52bbb6bdf0fbc1853e0ed4cf5.png)
4. 创建 Hbase 表。
```
# 进入HBase命令
root@172~# hbase shell
```
进入 hbase shell，并新建表：
```
# 建表语句
  create ‘dim_hbase’, ‘cf’

# 插入数据
  put ‘dim_hbase’,’1’,’cf:name’,’MingDeSchool’
```

### 创建云数据仓库 ClickHouse
#### 新建集群
登录 [云数据仓库 ClickHouse](https://console.cloud.tencent.com/cdwch) 控制台，选择**集群列表 > 新建集群**，新建集群。
![](https://main.qcloudimg.com/raw/e61f2fcf1bc9aad69f13998289de2243.png)
选择网络选择之前新建的 VPC 网络（依然保证各服务在同一网络）。
![](https://main.qcloudimg.com/raw/677f5ec1774740abbcdffde01f25f807.png)

#### 登录 ClickHouse
在之前新建的 EMR 下选择一台云服务器单击**登录**，最好选择带有外网 IP 的节点。
![](https://main.qcloudimg.com/raw/c059974e303764a62d1128fd3e5a9aa7.png)

#### 安装 ClickHouse 客户端
在此机器上安装 ClickHouse 客户端，clickhouse-client 安装可参见 [快速入门](https://cloud.tencent.com/document/product/1299/49824)。

#### 登录客户端
登录客户端示例如下：
```
clickhouse-client -h用户自己的ClickHouse服务IP --port 9000
```
新建数据库：
```
create database testdb on cluster default_cluster;
```
新建表：
```
CREATE TABLE testdb.student_school on cluster default_cluster (
`id` Int32,
`name` Nullable(String),
`school_name` Nullable(String),
`Sign` Int8
) ENGINE = ReplicatedCollapsingMergeTree('/clickhouse/tables/{layer}-{shard}/testdb/ student_school, '{replica}', Sign) ORDER BY id;
```

## 数据清洗和运算加工
### 数据准备
按照上面的操作创建表，并向 MySQL 和 HBase 表中插入数据。

### 创建 Flink SQL 作业
在流计算 Oceanus 控制台创建 SQL 作业，选择响应的内置 Connector。

#### Source 端
MySQL-CDC Source：
```
--学生信息作为cdc源表
CREATE TABLE `student` (
  `id` INT NOT NULL,
  `name` varchar,
  `age` INT,
  proc_time AS PROCTIME(),
  PRIMARY KEY (`ID`) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',
  -- 必须为 'mysql-cdc'
  'hostname' = 'YoursIp',
  -- 数据库的 IP
  'port' = '3306',
  -- 数据库的访问端口
  'username' = '用户名',
  -- 数据库访问的用户名（需要提供 SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, SELECT, RELOAD 权限）
  'password' = 'YoursPassword,
  -- 数据库访问的密码
  'database-name' = 'mysqltestdb',
  -- 需要同步的数据库
  'table-name' = 'student' -- 需要同步的数据表名
);
```
HBase 维表：
```
--示例使用school学校信息作为维表
CREATE TABLE dim_hbase (
  rowkey STRING,
  cf ROW <school_name STRING>,  -- 如果有多个列簇，写法 cf Row<age INT,name String>
  PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
  'connector' = 'hbase-1.4',
  'table-name' = 'dim_hbase',
  'zookeeper.quorum' = '用户自己的hbase服务器zookeeper地址，多个用逗号隔开'
);
```

#### Sink 端
创建到 ClickHouse 的创建表语句。
```
--关联后存入clickhouse表
CREATE TABLE `student_school` (
  stu_id INT,
  stu_name STRING,
  school_name STRING,
  PRIMARY KEY (`id`) NOT ENFORCED
) WITH (
  -- 指定数据库连接参数
  'connector' = 'clickhouse',
  'url' = 'clickhouse://yourIP:8123',
  -- 如果ClickHouse集群未配置账号密码可以不指定
  --'username' = 'root',
  --'password' = 'root',
  'database-name' = 'testdb',
  'table-name' = ' student_school ',
  'table.collapsing.field' = 'Sign'
);
```

#### 进行逻辑运算
此示例中，只进行了简单的 Join 没有进行复杂的运算。详细运算逻辑可参见 [Oceanus 运算符和内置函数](https://cloud.tencent.com/document/product/849/18083) 或者 Flink 官网 [Flink SQL 开发](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/)。
```
INSERT INTO
  student_school
SELECT
  student.id as stu_id,
  student.name as stu_name,
  dim_hbase.cf.school_name
FROM
  student
  JOIN dim_hbase for SYSTEM_TIME as of student.proc_time
	ON CAST(student.school_id AS STRING) = dim_hbase.rowkey;
```

### 结果验证
在 ClickHouse 数据库中查询数据是否正确。
```
select * from testdb.student_school; 
```
