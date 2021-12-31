
TDSQL PostgreSQL版 是基于分布式架构，支持自动水平拆分的高性能数据库，为您有效解决业务快速发展时的数据库性能瓶颈，随着业务量的变化，您可以随时调整 TDSQL PostgreSQL版 实例的规格。 

## 测试环境
在腾讯云购买不同规格的实例，进行 OLTP 和 SELECT 场景性能测试。
>?OLTP 场景测试指混合读写测试，读写比例14:4。SELECT 场景测试指简单的主键查询。
>
- 地域可用区：广州四区。
- 实例资源：指定配置按照上述资源配置进行 CGroup 隔离。
- 压测机器：由于压测机器需要安装额外的编译工具，同时在压测过程中需要消耗额外的系统资源，需要单独购买云服务器进行压力测试，建议使用计算型云服务器进行压力测试。
- 测试环境实例规格配置：用户在购买指定规格后，集群通过 CGroup 实现规格限制。
<table>
<thead><tr><th>节点配置</th><th>GTM</th><th>CN</th><th>DN</th></tr></thead>
<tbody><tr>
<td>入门型</td><td>1核4GB</td><td>1核4GB</td><td>1核6GB</td></tr>
<tr>
<td>基础Ⅰ型</td><td>1核4GB</td><td>2核8GB</td><td>2核12GB</td></tr>
<tr>
<td>基础Ⅱ型</td><td>4核4GB</td><td>4核16GB</td><td>4核24GB</td></tr>
<tr>
<td>中等Ⅰ型</td><td>4核4GB</td><td>8核32GB</td><td>8核48GB</td></tr>
<tr>
<td>中等Ⅱ型</td><td>8核8GB</td><td>16核64GB</td><td>16核96GB</td></tr>
<tr>
<td>高配Ⅰ型</td><td>16核16GB</td><td>32核128GB</td><td>32核192GB</td></tr>
<tr>
<td>高配Ⅱ型</td><td>16核16GB</td><td>64核256GB</td><td>64核384GB</td></tr>
</tbody></table>
- 测试环境集群配置。
<table>
<thead><tr><th>节点类型</th><th>配置模式</th><th>数量</th></tr></thead>
<tbody><tr>
<td>GTM</td><td>1主1备</td><td>1</td></tr>
<tr>
<td>CN</td><td>1主1备</td><td>2</td></tr>
<tr>
<td>DN</td><td>1主1备</td><td>2</td></tr>
</tbody></table>

## 测试工具
Sysbench 是一款基于 LuaJITde 开源的、模块化的、跨平台的模块化多线程性能测试工具，可以执行数据库、CPU、内存、线程、IO 等方面的性能测试。
工具内置数据库测试模型，采用多线程并发操作来评估数据库的性能，目前支持的数据库：MySQL、Oracle 和 PostgreSQL。
本次采用 Sysbench 作为 TDSQL PostgreSQL版 在 OLTP 和 SELECT 场景中的性能测试工具。

本次测试使用的 Sysbench 版本为1.0.12，详细源码及其他说明信息请参考 [sysbench](https://github.com/akopytov/sysbench)。

#### 安装和编译命令
```shell
# 切换目录
mkdir -p /data/sysbench && cd /data/sysbench
# 安装编译插件和库包
yum install make automake libtool pkgconfig libaio-devel postgresql-devel
# 获取源码
wget -c https://github.com/akopytov/sysbench/archive/1.0.12.zip
# 解压并进行编译
unzip 1.0.12.zip && cd sysbench-1.0.12
./autogen.sh
./configure --with-pgsql --without-mysql
make
make install
# 编译安装完成后，sysbench 工具所在目录
ls /usr/local/bin/sysbench
```

#### 压力测试参数说明
```shell
--test: 压力测试使用的 Lua 模型场景文件
--db-driver: 指定数据库类型
--pgsql-db: 压力测试操作的数据库名
--pgsql-user： 连接数据库的用户名
--pgsql-password: 连接数据库的密码
--pgsql-host: 主 CN 的 IP
--pgsql-port: 主 CN 的数据库端口
--oltp-tables-count: 压力测试的数据库表数量
--oltp-tables-size: 压力测试单表的数据量
--num-threads: 压力测试的并发线程数
--max-time: 压力测试时间，取值为0，表示不限时间，单位为秒
--max-requests: 压力请求数量，取值为0，表示不限请求数量，单位为单次 Lua 场景请求数
--report-interval: 压测报告输出周期，单位为秒
--force-shutdown: 压力完成后是否强制终止测试
```

## 测试指标
- **TPS**：Transaction Per Second，数据库每秒执行的事务数，每个事务中包含18条 SQL 语句。
- **QPS**：Query Per Second，数据库每秒执行的 SQL 数。


## 测试模型
### 表结构
```sql
CREATE TABLE `sbtest` (
       `id` INTEGER IDENTITY(1,1) NOT　NULL,
       `k` INTEGER DEFAULT '0' NOT NULL,
       `c` CHAR(120) DEFAULT '' NOT NULL,
       `pad` CHAR(60) DEFAULT '' NOT NULL,
       PRIMARY KEY (`id`)
   )
```

### OLTP 压力场景
Sysbench 中 OLTP 场景的事务中包含18条 SQL，具体执行的语句如下：
- 主键 SELECT 语句，包含10条：
```sql
SELECT c FROM ${rand_table_name} where id=${rand_id};
```
- 范围 SELECT 语句， 包含4条：
```sql
SELECT c FROM ${rand_table_name} WHERE id BETWEEN ${rand_id_start} AND ${rand_id_end};
SELECT SUM(K) FROM ${rand_table_name} WHERE id BETWEEN ${rand_id_start} AND ${rand_id_end};
SELECT c FROM ${rand_table_name} WHERE id BETWEEN ${rand_id_start} AND ${rand_id_end} ORDER BY c;
SELECT DISTINCT c FROM ${rand_table_name} WHERE id BETWEEN ${rand_id_start} AND ${rand_id_end} ORDER BY c;
```
- UPDATE 语句，包含2条：
```sql
UPDATE ${rand_table_name} SET k=k+1 WHERE id=${rand_id}
UPDATE ${rand_table_name} SET c=${rand_str} WHERE id=${rand_id}
```
- DELETE 语句，包含1条：
```sql
DELETE FROM ${rand_table_name} WHERE id=${rand_id}
```
- INSERT 语句，包含1条：
```sql
INSERT INTO ${rand_table_name} (id, k, c, pad) VALUES (${rand_id},${rand_k},${rand_str_c},${rand_str_pad})
```

### SELECT 压力场景
- 主键 SELECT 语句
```sql
SELECT c FROM ${rand_table_name} where id=${rand_id};
```

## 测试步骤
测试过程中，请根据实例的配置修改 CN IP [host]、CN Port  [port]、用户名 [user] 和 密码 [password]。
1. 导入数据。
 1. 创建数据库 loadtest：
```shell
psql -h $host -p [host] -U [user] postgres -c "create database loadtest"
```
 2. 使用 Sysbench 工具构造压测数据到 loadtest 库中，根据不同的实例规格场景修改背景数据量：
```shell
sysbench --test=./tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-db=loadtest --pgsql-user=[user] --pgsql-password=[password] --pgsql-port=[port] --pgsql-host=[host] --oltp-tables-count=20 --oltp-table-size=2000000 --num-threads=20 prepare
```
2. 压力测试，根据不同的实例规格场景修改压测参数。
```shell
sysbench --test=./tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-db=loadtest --pgsql-user=[user] --pgsql-password=[password] --pgsql-port=[port] --pgsql-host=[host] --oltp-tables-count=20 --oltp-table-size=2000000 --max-time=3600 --max-requests=0 --num-threads=150 --report-interval=3 --forced-shutdown=1 run
```
3. 清理数据，压力测试完成后，清理压力数据。
```shell
sysbench --test=./tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-db=loadtest --pgsql-user=[user] --pgsql-password=[password] --pgsql-port=[port] --pgsql-host=[host] --oltp-tables-count=20 --oltp-table-size=2000000 --max-time=3600 --max-requests=0 --num-threads=20 --report-interval=3 --forced-shutdown=1 cleanup
```
  
