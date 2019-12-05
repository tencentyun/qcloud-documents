FDW(FOREIGN DATA WRAPPER, 外部数据包装器)是 PostgreSQL 提供用于访问外部数据源的一类插件，外部数据源包括本实例其他库中数据或者其他实例的数据。FDW插件有很多分类，根据不同目标数据库实例类型可以定义不同的FDW插件，例如：postgres_fdw、mysql_fdw、mongo_fdw等。使用过程包含以下步骤：

 1. 使用 “CREATE EXTENSION” 语句安装 FDW 插件。
 2. 使用 “CREATE SERVER” 语句,为每个需要连接的远程数据库创建一个外部服务器对象。指定除了 user 和 password 以外的连接信息作为服务器对象的选项。
 3. 使用 “CREATE USER MAPPING” 语句，为每个需要通过外部服务器访问的数据库创建用户映射。指定远程的和密码作为映射用户的 user 和 password。
 4. 使用 “CREATE FOREIGN TABLE” 语句，为每个需要访问的远程表创建外部表。 创建的外部表的对应列必须与远程表匹配。也可以在外部表中使用与远程表不同的表名和列名， 但前提是你必须将正确的远程对象名作为创建外部表对象的选项。

由于 FDW 插件可以直接跨实例访问，基于安全性考虑，TencentDB For PostgreSQL 对创建外部服务器对象时进行了权限控制优化，根据目标实例所在环境进行分类管理。在开源版本基础上增加了额外辅助参数，来验证用户身份和调整网络策略。

## CREATE SERVER 辅助参数
#### postgres_fdw、mysql_fdw 等插件辅助参数    

 - host
    必须项。目标实例的内网 ip 地址，postgres_fdw 使用。
 - address
    必须项。目标实例的内网 ip 地址，mysql_fdw 使用。
 - port
    必须项。目标实例的内网 port。
 - instanceid
    必须项。目标实例的资源 ID。
     1. 如果目标实例类型为 CDB 类型，则为实例 ID，例如格式类似 postgres-xxxxx、mysql-xxxxx 等，可在实例控制台查看，如 PostgreSQL 为：
![](https://main.qcloudimg.com/raw/da92d46f8b152ffda53300fa577e9399.png)
     2. 如果目标实例在腾讯云 CVM 上，则为 CVM 机器的实例 ID，格式类似 ins-xxxxx。
![](https://main.qcloudimg.com/raw/9dd32f99dfb6ea8b3d1f39a89944aab1.png)

 - access_type
    非必须项。目标实例所属类型：
    1. 目标实例为 CDB 实例，包括 TencentDB For PostgreSQL、TencentDB For MySQL 等，如果不显示指定，则默认该项；
    2. 目标实例在腾讯云 CVM 机器上；
    3. 目标实例为腾讯云外网自建；
    4. 目标实例为云 vpn 接入的实例;
    5. 目标实例为自建 vpn 接入的实例;
    6. 目标实例为专线接入的实例;
    7. 目标实例为腾讯云 COS 数据；
 - uin
    非必须项。实例所属的账号 ID，通过该信息鉴定用户权限，可在这里查询：[查询uin](https://console.cloud.tencent.com/developer)
 - own_uin
    非必须项。实例所属的主账号 ID，同样需要该信息鉴定用户权限。
 - vpcid
    非必须项。私有网络 ID，目标实例如果在腾讯云 CVM 的 VPC 网络中，则需要提供该参数，可在 [VPC 控制台](https://console.cloud.tencent.com/vpc/vpc) 中查看。
 - subnetid
    非必须项。私有网络子网ID，目标实例如果在腾讯云CVM的VPC网络中，则需要提供该参数，可在[VPC 控制台](https://console.cloud.tencent.com/vpc/subnet) - 子网中查看。
 - dcgid
    非必须项。专线 ID，目标实例如果需要通过专线网络连接，则需要提供该参数值。
 - vpngwid
    非必须项。VPN 网关 ID，目标实例如果需要通过 vpn 网络连接，则需要提供该参数值。
 - region
    非必须项。目标实例所在地域，如 “ap-guangzhou” 表示广州。如果需要跨地域访问数据，则需要提供该参数值。

### COS_FDW 插件的辅助参数
  - host
    必须项。腾讯云对象存储 COS 的访问域名，例如：`https://xxxx-xxxxxx.cos.ap-beijing.myqcloud.com。`
  - bucket
    必须项。腾讯云对象存储 COS 的存储桶名。
  - id
    必须项。腾讯云 API 密钥的 SecretId 值，可从 [访问管理控制台](https://console.cloud.tencent.com/capi) - 云 API 密钥中查询。
  - key
    必须项。腾讯云 API 密钥的 SecretKey 值，可从 [访问管理控制台](https://console.cloud.tencent.com/capi) - 云 API 密钥中查询。

### FDW 支持

| 名称 			| 是否可直接使用 				| 跨地域使用 					|
| - 			| :-: 						| -: 						|
| postgres_fdw 	| 2018 年 4 月 26 日之前创建的实例重启后可使用，新实例可以直接使用							| 默认不支持，可【提交工单】申请 	|
| mysql_fdw 	| 2018 年 4 月 26 日之前创建的实例重启后可使用，新实例可以直接使用							| 默认不支持，可【提交工单】申请 	|
| cos_fdw 		| 灰度中，可【提交工单】申请试用	| 默认不支持，可【提交工单】申请 	|



### 参考链接

[9.3 版本 SERVER 创建](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)
[9.5 版本 SERVER 创建](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

## 使用postgres_fdw示例
使用 postgres_fdw 插件可以访问本实例其他库或者其他 postgres 实例的数据。

### 前置条件
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

### 创建 SERVER

1. 目标实例为 TencentDB 实例类型。
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


### 创建用户映射
```
    testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
    CREATE USER MAPPING
```
### 创建外部表
```
    testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(table_name 'test_table2');
    CREATE FOREIGN TABLE
```
### 访问外部数据
```
    testdb1=> select * from foreign_table1;
     id
    ----
      1
    (1 row)
```
### postgres_fdw 使用注意
如果目标实例在 CVM 上，需要注意以下几点：
 1. 需要放开 PostgreSQL 的 hba 限制，允许创建的映射用户（如：user2）以 MD5 方式访问。hba 的修改可参考 [PostgreSQL 官方说明](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html)。
 2. 如果目标实例非 CDB 实例，且搭建有热备模式，当主备切换后，需要自行更新 server 连接地址或者重新创建 server。

### 参考文档

[postgres_fdw介绍](http://www.postgres.cn/docs/9.5/postgres-fdw.html)

[9.3 版本 SERVER 创建](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)

[9.5 版本 SERVER 创建](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

[9.3 版本 pg_hba 介绍](https://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html)

[9.5 版本 pg_hba 介绍](https://www.postgresql.org/docs/9.5/static/auth-pg-hba-conf.html)

## 使用 mysql_fdw 示例
使用 mysql_fdw 插件可以访问其他 mysql 实例的数据。

### 前置条件

1. 在本实例中创建测试数据。
```
    postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
    postgres=>create database testdb1;
    CREATE DATABASE
```
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

### 创建 mysql_fdw 插件
```
    #创建
    postgres=> \c testdb1
    You are now connected to database "testdb1" as user "user1".
    testdb1=> create extension mysql_fdw;
    CREATE EXTENSION
    #查看
    testdb1=> \dx
                               List of installed extensions
         Name     | Version |   Schema   |                    Description
    --------------+---------+------------+----------------------------------------------------
     plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
     mysql_fdw    | 1.0     | public     | Foreign data wrapper for querying a MySQL server
    (2 rows)
```

### 创建 SERVER
1. 目标实例为 TencentDB 实例类型。
 ```
    #从本实例的testdb1访问目标实例testdb2的数据
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'cdb-xxxxx', uin 'xxxxxx', region 'ap-guangzhou');
    CREATE SERVER
 ```
2. 目标实例在腾讯云CVM上，且网络类型为基础网络。
```
    testdb1=>create server srv_test foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou'，uin 'xxxxxx'，own_uin 'xxxxxx');
    CREATE SERVER
```
3. 目标实例在腾讯云CVM上，且网络类型为私有网络。
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', instanceid 'ins-xxxxx', access_type '2', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpcid 'vpc-xxxxxx', subnetid 'subnet-xxxxx');
    CREATE SERVER
```
4. 目标实例在腾讯云外网自建
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '3', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx');
    CREATE SERVER   
```
5. 目标实例在腾讯云VPN接入的实例
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '4', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');
```
6. 目标实例在自建VPN接入的实例
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '5', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', vpngwid 'xxxxxx');   
```
7. 目标实例在腾讯云专线接入的实例
```
    testdb1=>create server srv_test1 foreign data wrapper mysql_fdw options (host 'xxx.xxx.xxx.xxx', port '3306', access_type '6', region 'ap-guangzhou', uin 'xxxxxx', own_uin 'xxxxxx', dcgid 'xxxxxx');    
    CREATE SERVER       
```


### 创建用户映射
```
    testdb1=> create user mapping for user1 server srv_test1 options (user 'user2',password 'password2');
    CREATE USER MAPPING
```
### 创建外部表
```
    testdb1=> create foreign table foreign_table1(id integer) server srv_test1 options(dbname 'testdb2', table_name 'test_table2');
    CREATE FOREIGN TABLE
```
### 访问外部数据
```
    testdb1=> select * from foreign_table1;
     id
    ----
      1
    (1 row)
```

### 参考链接

[9.3 版本 SERVER 创建](https://www.postgresql.org/docs/9.3/static/sql-createserver.html)
[9.5 版本 SERVER 创建](https://www.postgresql.org/docs/9.5/static/sql-createserver.html)

## 使用cos_fdw示例
使用 cos_fdw 插件可以在 TencentDB For PostgreSQL 实例中获取腾讯云对象存储COS中的文本数据。

### 前置条件
1. 在本实例中创建测试数据。
```
    postgres=>create role user1 with LOGIN  CREATEDB PASSWORD 'password1';
    postgres=>create database testdb1;
    CREATE DATABASE
```

2. 在 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket) 创建存储桶“test1”，在该存储桶中上传文本文件至“/testdir/test.txt”。


 ### 创建 cos_fdw 插件
```
    #创建
    postgres=> \c testdb1
    You are now connected to database "testdb1" as user "user1".
    testdb1=> create extension cos_fdw;
    CREATE EXTENSION
    #查看
    testdb1=> \dx
                               List of installed extensions
         Name     | Version |   Schema   |                    Description
    --------------+---------+------------+----------------------------------------------------
     plpgsql      | 1.0     | pg_catalog | PL/pgSQL procedural language
     cos_fdw      | 1.0     | public     | foreign-data wrapper for flat qcloud cos access
    (2 rows)
```

### 创建 SERVER
```
    #从本实例的testdb1访问对象存储test1上的数据
    testdb1=>create server srv_cos foreign data wrapper cos_fdw options(host 'test11-xxxxxx.cos.ap-chengdu.myqcloud.com', bucket 'test1', id 'xxxxxx', key 'xxxxxx');
    CREATE SERVER
```

### 创建外部表
参数：filepath，本文文件在存储桶中的相对路径
```
    testdb1=> create foreign table test_cos(id integer) server srv_cos options(filepath '/testdir/test.txt');
    CREATE FOREIGN TABLE
```
### 访问外部数据
```
    testdb1=> select * from test_cos;
     id
    ----
      1
    (1 row)

```
### 参考链接

[对象存储文档](https://intl.cloud.tencent.com/document/product/436)。

