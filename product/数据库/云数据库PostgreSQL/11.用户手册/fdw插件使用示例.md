使用 postgres_fdw 插件可以访问本实例其他库或者其他 postgres 实例的数据。

## 前置条件
1. 在本实例中创建测试数据。
```
postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
postgres=>create database testdb1;
CREATE DATABASE
```   

2. 在目标实例中创建测试数据
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


## 创建 postgres_fdw 插件
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

## 创建 SERVER

1. 目标实例为 CDB 实例类型。
```
    #从本实例的testdb1访问目标实例testdb2的数据
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'postgres-xxxxx');
    CREATE SERVER
```
2. 目标实例在腾讯云 CVM 上，且网络类型为基础网络。
```
    testdb1=>create server srv_test foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx', dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou'，uin 'xxxxxx'，own_uin 'xxxxxx');
    CREATE SERVER
```
3. 目标实例在腾讯云 CVM 上，且网络类型为私有网络。
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpcid 'vpc-xxxxxx', subnetid 'subnet-xxxxx');
    CREATE SERVER
```

4. 目标实例在腾讯云外网自建。
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '3', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx');
    CREATE SERVER 
```

5. 目标实例在腾讯云 VPN 接入的实例。
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '4', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');
```

6. 目标实例在自建 VPN 接入的实例。
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '5', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');   
```

7. 目标实例在腾讯云专线接入的实例。
```
    testdb1=>create server srv_test1 foreign data wrapper postgres_fdw options (host 'xxx.xxx.xxx.xxx',dbname 'testdb2', port '5432', access_type '6', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', dcgid 'xxxxxx');    
    CREATE SERVER       
```

## 创建用户映射
```
    testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
    CREATE USER MAPPING
```
## 创建外部表
```
    testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(table_name 'test_table2');
    CREATE FOREIGN TABLE
```   
## 访问外部数据
```
    testdb1=> select * from foreign_table1;
     id
    ----
      1
    (1 row)
```
## postgres_fdw 使用注意
如果目标实例在 CVM 上，需要注意以下几点：
 1. 需要放开 PostgreSQL 的 hba 限制，允许创建的映射用户（如：user2）以 MD5 方式访问。hba 的修改可参考[PostgreSQL 官方说明](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html)
 2. 如果目标实例非 CDB 实例，且搭建有热备模式，当主备切换后，需要自行更新 server 连接地址或者重新创建 server。

## 参考文档

[postgres_fdw介绍](http://www.postgres.cn/docs/9.5/postgres-fdw.html)

[9.3版本SERVER创建](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)

[9.5版本SERVER创建](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

[9.3版本pg_hba介绍](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html)

[9.5版本pg_hba介绍](https://www.postgresql.org/docs/9.5/static/auth-pg-hba-conf.html)

 
