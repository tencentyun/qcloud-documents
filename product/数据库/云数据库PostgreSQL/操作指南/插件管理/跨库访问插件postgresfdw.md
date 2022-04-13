## 简介
FDW（FOREIGN DATA WRAPPER，外部数据包装器）是 PostgreSQL 提供用于访问外部数据源的一类插件，外部数据源包括本实例其他库中数据或者其他实例的数据。使用过程包含以下步骤：
1. 使用 “CREATE EXTENSION” 语句安装 FDW 插件。
2. 使用 “CREATE SERVER” 语句，为每个需要连接的远程数据库创建一个外部服务器对象。指定除了 user 和 password 以外的连接信息作为服务器对象的选项。
3. 使用 “CREATE USER MAPPING” 语句，为每个需要通过外部服务器访问的数据库创建用户映射。指定远程的帐号和密码作为映射用户的 user 和 password。
4. 使用 “CREATE FOREIGN TABLE” 语句，为每个需要访问的远程表创建外部表。创建的外部表的对应列必须与远程表匹配。也可以在外部表中使用与远程表不同的表名和列名， 但前提是您必须将正确的远程对象名作为创建外部表对象的选项。

由于 FDW 插件可以直接跨实例访问或在同实例中进行跨 database 访问。云数据库 PostgreSQL 对创建外部服务器对象时进行了权限控制优化，根据目标实例所在环境进行分类管理。在开源版本基础上增加了额外辅助参数，来验证用户身份和调整网络策略。

## postgres_fdw 插件辅助参数    
 - **host**
   跨实例访问时候为必须项。目标实例的 IP 地址，postgres_fdw 使用。
 - **port**
   跨实例访问时候为必须项。目标实例的 port。
 - **instanceid**
   实例 ID，在云数据库 PostgreSQL 间跨实例访问时使用，当跨实例访问时为必选项。格式类似 postgres-xxxxxx、pgro-xxxxxx，可在 [控制台](https://console.cloud.tencent.com/postgres) 查看，如 PostgreSQL 为：
![](https://qcloudimg.tencent-cloud.cn/raw/a5659bc6941fa163907e1315e4db43cc.png)
 - **dbname** 
 database 名，填写需要访问的远端 PostgreSQL 服务的 database 名字。若不跨实例访问，仅在同实例中进行跨库访问，则只需要配置此参数即可，其他参数都可为空。
 
## 使用 postgres_fdw 示例
使用 postgres_fdw 插件可以访问本实例其他库或者其他 postgres 实例的数据。

### 步骤1：前置条件
1. 在本实例中创建测试数据。
```
postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
postgres=>create database testdb1;
CREATE DATABASE
```
>! 若创建插件报错，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云售后协助处理。
>
2. 在目标实例中创建测试数据。
```
postgres=>create role user2 with LOGIN  CREATEDB PASSWORD 'password2';
postgres=> create database testdb2;
CREATE DATABASE
postgres=> \c testdb2 user2
You are now connected to database "testdb2" as user "user2".
testdb2=> create table test_table2(id integer);
CREATE TABLE
testdb2=> insert into test_table2 values (1);
INSERT 0 1
```

### 步骤2：创建 postgres_fdw 插件
>?若创建插件时，提示插件不存在或权限不足，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。
>
```
#创建
postgres=> \c testdb1
You are now connected to database "testdb1" as user "user1".
testdb1=> create extension postgres_fdw;
CREATE EXTENSION
#查看
testdb1=> \dx
                            List of installed extensions
      Name     | Version |   Schema   |                    Description
--------------+---------+------------+----------------------------------------------------
  plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
  postgres_fdw | 1.0     | public     | foreign-data wrapper for remote PostgreSQL servers
(2 rows)
```

### 步骤3：创建 SERVER
- 跨实例访问。
```
#从本实例的 testdb1 访问目标实例 testdb2 的数据
testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'postgres-xxxxx');
CREATE SERVER
```
- 不跨实例，仅跨 database 访问,仅需要填写 dbname 参数即可。
```
#从本实例的 testdb1 访问本实例 testdb2 的数据
create server srv_test1 foreign data wrapper postgres_fdw options (dbname 'testdb2');
```

### 步骤4：创建用户映射 
>? 同实例的跨 database 访问则可跳过此步骤。
```
testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
CREATE USER MAPPING
```

### 步骤5：创建外部表
```
testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(table_name 'test_table2');
CREATE FOREIGN TABLE
```   

### 步骤6：访问外部数据
```
testdb1=> select * from foreign_table1;
  id
----
   1
(1 row)
```

### 参考链接
[postgres_fdw 官方介绍](https://www.postgresql.org/docs/9.5/postgres-fdw.html)
[9.3 版本 SERVER 创建](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)
[9.5 版本 SERVER 创建](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)
[10 版本 SERVER 创建](https://www.postgresql.org/docs/10/sql-createserver.html)
[11 版本 SERVER 创建](https://www.postgresql.org/docs/11/sql-createserver.html)
[12 版本 SERVER 创建](https://www.postgresql.org/docs/12/sql-createserver.html)
[13 版本 SERVER 创建](https://www.postgresql.org/docs/13/sql-createserver.html)
