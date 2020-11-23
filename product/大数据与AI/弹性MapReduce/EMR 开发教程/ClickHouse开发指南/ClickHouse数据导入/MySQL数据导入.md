## 概述
本文介绍两种将 MySQL 数据库中的数据导入到 ClickHouse 集群的方案。
- 利用 ClickHouse 支持 MySQL 外表的特性来实现。
- 使用 Altinity 提供的`clickhouse-mysql-data-reader`工具来实现数据导入。

本文示例中，将 MySQL 数据表 test.clickhouse_test 中的数据导入到 ClickHouse 集群中，该表的 Schema 如下：
![](https://main.qcloudimg.com/raw/7403cab1c8f0a68fa2fe3ce0227225ab.jpg)
                         

## 基于 MySQL 表引擎来实现数据导入（简易方案）
ClickHouse 的 MySQL 表引擎可以对存储在远程 MySQL 服务器上的数据执行 SELECT 查询。基于这样能力，利用`CREATE ... SELECT * FROM`或者`INSERT INTO ... SELECT * FROM`语句即可完成数据导入。

**具体步骤：**
- 步骤1：在 ClickHouse 中创建 MySQL 表引擎。
![](https://main.qcloudimg.com/raw/4486adf6c262e1fec06d4ce8cc99fbb4.jpg)
- 步骤2：建立 ClickHouse 表。
![](https://main.qcloudimg.com/raw/296886441fadb3f57f8d9a9cd94906ec.jpg)
- 步骤3：将步骤1中的外表中数据，导入到 ClickHouse 表中。
![](https://main.qcloudimg.com/raw/e869a8ed58e91e9066849fb1073a910d.jpg)
 
还可以将步骤2/3合并成一个步骤，即采用`CREATE TABLE AS SELECT * FROM`方式来达到同样效果。

**ClickHouse 支持 MySQL 外表引擎，是否还有必要将数据导入到 ClickHouse 中？**      
是非常有必要的。MySQL 外表引擎，本身不存储数据，数据存储在 MySQL 中。在复制查询中，特别是有 JOIN 的情况下，访问外表是相当慢的，甚至不可能完成。该方案有明显缺陷，无法增量导入数据。

## 基于 Altinity 的工具实现数据导入（推荐方案）

Altinity 提供了一个工具 [clickhouse-mysql-data-reader](https://github.com/Altinity/clickhouse-mysql-data-reader) 来实现数据导入。该工具可以实现 MySQL 的存量数据导出和增量数据的导出。

按照官网推荐，使用 [pypy](https://github.com/squeaky-pl/portable-pypy#portable-pypy-distribution-for-linux) 工具能够显著提升 clickhouse-mysql-data-reader 导入数据的性能。

**工具准备**

- 步骤1：下载 [pypy3.6-7.2.0](https://github.com/squeaky-pl/portable-pypy/releases)，解压到 pypy 目录下。
- 步骤2：安装 clickhouse-mysql。**如果是在腾讯云 ClickHouse 集群，完成下面安装操作后，工具已经集成，开箱即用，无需配置。**
 - 安装 pip：执行`pypy/bin/pypy3 -m ensurepip`。
 - 安装 mysql-replication,clickhouse-driver，执行`pypy/bin/pip3 install mysql-replication`和`pypy/bin/pip3 install clickhouse-driver`。
 - 安装 clickhouse-mysql 并初始化，执行`pypy/bin/pip3 install clickhouse-mysql`，执行`pypy/bin/clickhouse-mysql --install`。
 - 安装 clickhouse-client，执行`yum install -y clickhouse-client`。
 - 安装 mysql-community-devel，执行`yum install -y mysql-community-devel`。
- 步骤3：数据库权限准备，所需权限为 SUPER、REPLICATION CLIENT。
```
CREATE USER 'root'@'%' IDENTIFIED BY 'cloud';
GRANT SELECT, REPLICATION CLIENT, REPLICATION SLAVE, SUPER ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;
```

## 数据导入
准备工作完成后，即可使用该工具完成数据从 MySQL 导入到 ClickHouse 集群中。具体步骤如下：
1. 使用 clickhouse-mysql-data-reader 生成建表 SQL。
![](https://main.qcloudimg.com/raw/aca912daf06add4f2bbcfc713c9762dc.jpg)
然后修改 SQL 语句，选择合适的表引擎（在本示例中使用 TinyLog）。执行建表语句`clickhouse-client -m < create.sql`。
2. 导入存量数据
![](https://main.qcloudimg.com/raw/396a932284dfaf0d1f6f8ce1d711e227.jpg)
3. 导入增量数据
![](https://main.qcloudimg.com/raw/f617557e73c30d7695848af7bf52074a.jpg)
其中，参数含义如下：
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>src-host</td>
<td>MySQL 数据库 IP</td>
</tr>
<tr>
<td>src-user</td>
<td>MySQL 数据库用户名</td>
</tr>
<tr>
<td>src-password</td>
<td>MySQL 数据库密码</td>
</tr>
<tr>
<td>create-table-sql-template</td>
<td>生产 ClickHouse 的建表脚本</td>
</tr>
<tr>
<td>with-create-database</td>
<td>建表脚本中增加创建数据库语句</td>
</tr>
<tr>
<td>src-tables</td>
<td>源表（MySQL 表）</td>
</tr>
<tr>
<td>mempool-max-flush-interval</td>
<td>mempool flush 的时间周期</td>
</tr>
<tr>
<td>src-server-id</td>
<td>源 MySQL 是否为 master 节点</td>
</tr>
<tr>
<td>src-resume</td>
<td>断点续传</td>
</tr>
<tr>
<td>src-wait</td>
<td>等待数据</td>
</tr>
<tr>
<td>nice-pause</td>
<td>如果没有数据，睡眠的时间间隔</td>
</tr>
</table>
