ODBC External Table Of Doris 提供了 Doris 通过数据库访问的标准接口（ODBC）来访问外部表，外部表省去了繁琐的数据导入工作，让 Doris 可以具有了访问各式数据库的能力，并借助 Doris 本身的 OLAP 的能力来解决外部表的数据分析问题：
- 支持各种数据源接入 Doris。
- 支持 Doris 与各种数据源中的表联合查询，进行更加复杂的分析操作。
- 通过 insert into 将 Doris 执行的查询结果写入外部的数据源。

本文档主要介绍该功能的实现原理、使用方式等。

## 名词解释
### Doris 相关
- FE：Frontend，Doris 的前端节点,负责元数据管理和请求接入。
- BE：Backend，Doris 的后端节点,负责查询执行和数据存储。

## 使用方法
### Doris 中创建 ODBC 的外表
具体建表语法参照：[CREATE TABLE](https://doris.apache.org/zh-CN/docs/dev/sql-manual/sql-reference/Data-Definition-Statements/Create/CREATE-TABLE)。

#### 不使用 Resource 创建 ODBC 的外表
```
CREATE EXTERNAL TABLE `baseall_oracle` (
  `k1` decimal(9, 3) NOT NULL COMMENT "",
  `k2` char(10) NOT NULL COMMENT "",
  `k3` datetime NOT NULL COMMENT "",
  `k5` varchar(20) NOT NULL COMMENT "",
  `k6` double NOT NULL COMMENT ""
) ENGINE=ODBC
COMMENT "ODBC"
PROPERTIES (
"host" = "192.168.0.1",
"port" = "8086",
"user" = "test",
"password" = "test",
"database" = "test",
"table" = "baseall",
"driver" = "Oracle 19 ODBC driver",
"odbc_type" = "oracle"
);
```

#### 通过 ODBC_Resource 来创建 ODBC 外表 (推荐使用的方式)
```sql
CREATE EXTERNAL RESOURCE `oracle_odbc`
PROPERTIES (
"type" = "odbc_catalog",
"host" = "192.168.0.1",
"port" = "8086",
"user" = "test",
"password" = "test",
"database" = "test",
"odbc_type" = "oracle",
"driver" = "Oracle 19 ODBC driver"
);
     
CREATE EXTERNAL TABLE `baseall_oracle` (
  `k1` decimal(9, 3) NOT NULL COMMENT "",
  `k2` char(10) NOT NULL COMMENT "",
  `k3` datetime NOT NULL COMMENT "",
  `k5` varchar(20) NOT NULL COMMENT "",
  `k6` double NOT NULL COMMENT ""
) ENGINE=ODBC
COMMENT "ODBC"
PROPERTIES (
"odbc_catalog_resource" = "oracle_odbc",
"database" = "test",
"table" = "baseall"
);
```
参数说明：

参数 | 说明
---|---
**hosts** | 外表数据库的 IP 地址
**driver** | ODBC 外表的 Drive r名，该名字需要和 be/conf/odbcinst.ini 中的 Driver 名一致。
**odbc_type** | 外表数据库的类型，当前支持 oracle，mysql，postgresql
**user** | 外表数据库的用户名
**password** | 对应用户的密码信息
**charset** | 数据库连接使用的字符集

>? `PROPERTIES` 中除了可以添加上述参数之外，还支持每个数据库的 ODBC driver 实现的专用参数，例如 mysql 的`sslverify` 等。


#### ODBC Driver 的安装和配置
各大主流数据库都会提供 ODBC 的访问 Driver，用户可以参照各数据库官方推荐的方式安装对应的 ODBC Driver lib 库。
安装完成之后，查找对应的数据库的Driver Lib库的路径，并且修改 be/conf/odbcinst.ini 的配置：
```
[MySQL Driver]
Description     = ODBC for MySQL
Driver          = /usr/lib64/libmyodbc8w.so
FileUsage       = 1 
```
- 上述配置`[]`里的对应的是 Driver 名，在建立外部表时需要保持外部表的 Driver 名和配置文件之中的一致。
- `Driver=`  这个要根据实际 BE 安装 Driver 的路径来填写，本质上就是一个动态库的路径，这里需要保证该动态库的前置依赖都被满足。

>! 切记，这里要求所有的 BE 节点都安装上相同的 Driver，并且安装路径相同，同时有相同的 be/conf/odbcinst.ini 的配置。


### 查询用法
完成在 Doris 中建立 ODBC 外表后，除了无法使用 Doris 中的数据模型（rollup、预聚合、物化视图等）外，与普通的 Doris 表并无区别。
```
select * from oracle_table where k1 > 1000 and k3 ='term' or k4 like '%doris';
```

### 数据写入
在 Doris 中建立 ODBC 外表后，可以通过 insert into 语句直接写入数据，也可以将 Doris 执行完查询之后的结果写入 ODBC 外表，或者是从一个 ODBC 外表将数据导入另一个 ODBC 外表。
```
insert into oracle_table values(1, "doris");
insert into oracle_table select * from postgre_table;
```
#### 事务
Doris 的数据是由一组 batch 的方式写入外部表的，如果中途导入中断，之前写入数据可能需要回滚。所以 ODBC 外表支持数据写入时的事务，事务的支持需要通过 session variable：`enable_odbc_transcation `设置。
```
set enable_odbc_transcation = true; 
```
事务保证了 ODBC 外表数据写入的原子性，但是一定程度上会降低数据写入的性能，可以考虑酌情开启该功能。

## 数据库 ODBC 版本对应关系

### Centos 操作系统

使用的 unixODBC 版本是：2.3.1，Doris 0.15，centos 7.9，全部使用 yum 方式安装。
#### mysql

| Mysql 版本 | Mysql ODBC 版本 |
| --------- | -------------- |
| 8.0.27    | 8.0.27, 8.026   |
| 5.7.36    | 5.3.11, 5.3.13  |
| 5.6.51    | 5.3.11, 5.3.13  |
| 5.5.62    | 5.3.11, 5.3.13  |

#### PostgreSQL
PostgreSQL 的 yum 源 rpm 包地址：
```
https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```
这里面包含 PostgreSQL 从9.x 到 14.x的全部版本，包括对应的 ODBC 版本，可以根据需要选择安装。

| PostgreSQL 版本 | PostgreSQL ODBC 版本          |
| -------------- | ---------------------------- |
| 12.9           | postgresql12-odbc-13.02.0000 |
| 13.5           | postgresql13-odbc-13.02.0000 |
| 14.1           | postgresql14-odbc-13.02.0000 |
| 9.6.24         | postgresql96-odbc-13.02.0000 |
| 10.6           | postgresql10-odbc-13.02.0000 |
| 11.6           | postgresql11-odbc-13.02.0000 |

#### Oracle

| Oracle 版本                                                   | Oracle ODBC 版本                            |
| ------------------------------------------------------------ | ------------------------------------------ |
| Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production | oracle-instantclient19.13-odbc-19.13.0.0.0 |
| Oracle Database 12c Standard Edition Release 12.2.0.1.0 - 64bit Production | oracle-instantclient19.13-odbc-19.13.0.0.0 |
| Oracle Database 18c Enterprise Edition Release 18.0.0.0.0 - Production | oracle-instantclient19.13-odbc-19.13.0.0.0 |
| Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production | oracle-instantclient19.13-odbc-19.13.0.0.0 |
| Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - Production | oracle-instantclient19.13-odbc-19.13.0.0.0 |

Oracle ODBC 驱动版本下载地址：
```
https://download.oracle.com/otn_software/linux/instantclient/1913000/oracle-instantclient19.13-sqlplus-19.13.0.0.0-2.x86_64.rpm
https://download.oracle.com/otn_software/linux/instantclient/1913000/oracle-instantclient19.13-devel-19.13.0.0.0-2.x86_64.rpm
https://download.oracle.com/otn_software/linux/instantclient/1913000/oracle-instantclient19.13-odbc-19.13.0.0.0-2.x86_64.rpm
https://download.oracle.com/otn_software/linux/instantclient/1913000/oracle-instantclient19.13-basic-19.13.0.0.0-2.x86_64.rpm
```

### Ubuntu 操作系统

使用的 unixODBC 版本是：2.3.4，Doris 0.15，Ubuntu 20.04。

#### Mysql

| Mysql 版本 | Mysql ODBC 版本 |
| --------- | -------------- |
| 8.0.27    | 8.0.11, 5.3.13  |

目前只测试了这一个版本其他版本测试后补充。

#### PostgreSQL

| PostgreSQL版本 | PostgreSQL ODBC版本 |
| -------------- | ------------------- |
| 12.9           | psqlodbc-12.02.0000 |

其他版本只要下载和数据库大版本相符合的 ODBC 驱动版本，这块后续会持续补充其他版本在 Ubuntu 系统下的测试结果。

#### Oracle
同上 Centos 操作系统的 Oracle 数据库及 ODBC 对应关系，在 ubuntu 下安装 rpm 软件包使用下面方式。
为了在 ubuntu 下可以进行安装 rpm 包，我们还需要安装一个 alien，这是一个可以将 rpm 包转换成 deb 安装包的工具。
```
sudo apt-get install alien
```
然后执行安装上面四个包：
```
sudo alien -i  oracle-instantclient19.13-basic-19.13.0.0.0-2.x86_64.rpm
sudo alien -i  oracle-instantclient19.13-devel-19.13.0.0.0-2.x86_64.rpm
sudo alien -i  oracle-instantclient19.13-odbc-19.13.0.0.0-2.x86_64.rpm
sudo alien -i  oracle-instantclient19.13-sqlplus-19.13.0.0.0-2.x86_64.rpm
```


## 类型匹配
各个数据库之间数据类型存在不同，这里列出了各个数据库中的类型和 Doris 之中数据类型匹配的情况。

### MySQL

|  MySQL  | Doris  |             替换方案              |
| :------: | :----: | :-------------------------------: |
|  BOOLEAN  | BOOLEAN  |       -                      |
|   CHAR   |  CHAR  |            当前仅支持 UTF8编码            |
| VARCHAR | VARCHAR |       当前仅支持 UTF8编码       |
|   DATE   |  DATE  |                  -                     |
|  FLOAT   |  FLOAT  |        -                               |
|   TINYINT   | TINYINT |  -    |
|   SMALLINT  | SMALLINT |  -    |
|   INT  | INT |  -    |
|   BIGINT  | BIGINT |  -    |
|   DOUBLE  | DOUBLE |  -    |
|   DATETIME  | DATETIME | -     |
|   DECIMAL  | DECIMAL |  -    |

### PostgreSQL

|  PostgreSQL  | Doris  |             替换方案              |
| :------: | :----: | :-------------------------------: |
|  BOOLEAN  | BOOLEAN  |            -                 |
|   CHAR   |  CHAR  |            当前仅支持 UTF8编码            |
| VARCHAR | VARCHAR |       当前仅支持 UTF8编码       |
|   DATE   |  DATE  |                            -           |
|  REAL   |  FLOAT  |                      -                 |
|   SMALLINT  | SMALLINT |  -    |
|   INT  | INT |  -    |
|   BIGINT  | BIGINT |  -    |
|   DOUBLE  | DOUBLE |  -    |
|   TIMESTAMP  | DATETIME |  -    |
|   DECIMAL  | DECIMAL |   -   |

### Oracle

|  Oracle  | Doris  |             替换方案              |
| :------: | :----: | :-------------------------------: |
|  不支持 | BOOLEAN  |          Oracle 可用 number(1) 替换 boolean               |
|   CHAR   |  CHAR  |             -              |
| VARCHAR | VARCHAR |      -           |
|   DATE   |  DATE  |                 -                      |
|  FLOAT   |  FLOAT  |                        -               |
|  无   | TINYINT | Oracle 可由 NUMMBER 替换 |
|   SMALLINT  | SMALLINT |   -   |
|   INT  | INT | -     |
|   无  | BIGINT |  Oracle 可由 NUMMBER 替换 |
|   无  | DOUBLE | Oracle 可由 NUMMBER 替换 |
|   DATETIME  | DATETIME | -     |
|   NUMBER  | DECIMAL |   -   |

### SQLServer

| SQLServer  | Doris  |             替换方案              |
| :------: | :----: | :-------------------------------: |
|  BOOLEAN  | BOOLEAN  |               -              |
|   CHAR   |  CHAR  |            当前仅支持 UTF8编码            |
| VARCHAR | VARCHAR |       当前仅支持 UTF8编码       |
|   DATE   |  DATE  |                      -             |
|  REAL   |  FLOAT  |                   -                    |
|   TINYINT   | TINYINT | -     |
|   SMALLINT  | SMALLINT |  -    |
|   INT  | INT |   -   |
|   BIGINT  | BIGINT |  -    |
|   FLOAT  | DOUBLE |  -    |
|   DATETIME/DATETIME2  | DATETIME | -     |
|   DECIMAL/NUMERIC | DECIMAL |   -   |

## 最佳实践
适用于少数据量的同步。
例如 Mysql 中一张表有100万数据，想同步到 Doris，就可以采用 ODBC 的方式将数据映射过来，在使用 [insert into](https://doris.apache.org/zh-CN/docs/dev/sql-manual/sql-reference/Data-Manipulation-Statements/Manipulation/INSERT) 方式将数据同步到 Doris 中，如果想同步大批量数据，可以分批次使用 [insert into](https://doris.apache.org/zh-CN/docs/dev/sql-manual/sql-reference/Data-Manipulation-Statements/Manipulation/INSERT) 同步（不建议使用）。

## 常见问题
1. 与原先的 MySQL 外表的关系。
在接入 ODBC 外表之后，原先的访问 MySQL 外表的方式将被逐渐弃用。如果之前没有使用过 MySQL 外表，建议新接入的 MySQL 表直接使用 ODBC 的 MySQL 外表。

2. 除了MySQL，Oracle，PostgreSQL，SQLServer是否能够支持更多的数据库？
目前 Doris 只适配了 MySQL，Oracle，PostgreSQL，SQLServer，关于其他的数据库的适配工作正在规划之中，原则上来说任何支持 ODBC 访问的数据库都能通过 ODBC 外表来访问。如果您有访问其他外表的需求，欢迎修改代码并贡献给 Doris。

3. 什么场合适合通过外表访问？
通常在外表数据量较小，少于100W条时，可以通过外部表的方式访问。由于外表无法发挥 Doris 在存储引擎部分的能力和会带来额外的网络开销，所以建议根据实际对查询的访问时延要求来确定是否通过外部表访问还是将数据导入 Doris 之中。

4. 通过 Oracle 访问出现乱码？
尝试在 BE 启动脚本之中添加如下参数：`export NLS_LANG=AMERICAN_AMERICA.AL32UTF8`， 并重新启动所有 BE。

5. ANSI Driver or Unicode Driver？
当前 ODBC 支持 ANSI 与 Unicode 两种 Driver 形式，当前 Doris 只支持 Unicode Driver。如果强行使用 ANSI Driver 可能会导致查询结果出错。

6. 报错 `driver connect Err: 01000 [unixODBC][Driver Manager]Can't open lib 'Xxx' : file not found (0)`。
没有在每一个BE上安装好对应数据的 Driver，或者是没有在 be/conf/odbcinst.ini 配置正确的路径，抑或是建表是 Driver 名与 be/conf/odbcinst.ini 不同。


7. 报错 `Fail to convert odbc value 'PALO ' TO INT on column:'A'`？
ODBC 外表的 A 列类型转换出错，说明外表的实际列与 ODBC 的映射列的数据类型不同，需要修改列的类型映射。

8. 同时使用旧的 MySQL 表与 ODBC 外表的 Driver 时出现程序 Crash？
这个是 MySQL 数据库的 Driver 与现有 Doris 依赖 MySQL 外表的兼容问题。推荐解决的方式如下：
   - 方式1：通过 ODBC 外表替换旧的 MySQL 外表，并重新编译 BE，关闭 WITH_MYSQL 的选项。
   - 方式2：不使用最新8.X 的 MySQL 的 ODBC Driver，而是使用5.X 的 MySQL 的 ODBC Driver。

9. 过滤条件下推？
当前 ODBC 外表支持过滤条件下推，目前 MySQL 的外表是能够支持所有条件下推的。其他的数据库的函数与 Doris 不同会导致下推查询失败。目前除 MySQL 外表之外，其他的数据库不支持函数调用的条件下推。Doris 是否将所需过滤条件下推，可以通过`explain` 查询语句进行确认。

10. 报错`driver connect Err: xxx`？
通常是连接数据库失败，Err 部分代表了不同的数据库连接失败的报错。这种情况通常是配置存在问题。可以检查是否错配了 IP 地址，端口或账号密码。
    
11. 读写 mysql 外表的 emoji 表情出现乱码？
Doris 进行 odbc 外表连接时，默认采用的编码为 utf8，由于 mysql 之中默认的 utf8编码为 utf8mb3，无法表示需要4字节编码的emoji表情。这里需要在建立 mysql 外表时设置`charset`=`utf8mb4`，便可以正常读写 emoji 表情。
