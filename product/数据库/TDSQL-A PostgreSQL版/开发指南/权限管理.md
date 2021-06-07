
## 用户
使用 CREATE USER和ALTER USER 可以创建和管理数据库用户。数据库集群包含一个或多个已命名数据库。用户和角色在整个集群范围内是共享的，但是其数据并不共享。 即用户可以连接任何数据库，但当连接成功后，任何用户都只能访问连接请求里声明的那个数据库。 
```
postgres=# **CREATE USER** tdapg_user1 PASSWORD 'tdapg@123';
CREATE ROLE
```

如果创建有“创建数据库”权限的用户，则需要加 CREATEDB 关键字。
```
postgres=# CREATE USER tdapg_user2 CREATEDB PASSWORD 'tdapg@123';
CREATE ROLE
```

将用户 tdapg_user2 的登录密码由 tdapg@123 修改为 Abcd@123。
```
postgres=# **ALTER USER** tdapg_user2 with password 'Abcd@123';
ALTER ROLE
```
- 为用户 tdapg_user2 追加 CREATEROLE 权限。 
```
ALTER USER tdapg_user2 CREATEROLE; 
```
- 删除用户。
```
DROP USER tdapg_user2;
```


## 角色
角色是一组权限的集合。通过 GRANT 把角色授予用户后，用户即具有了角色的所有权限。推荐使用角色进行高效权限分配。例如，可以为设计、开发和维护人员创建不同的角色，将角色 GRANT 给用户后，再向每个角色中的用户授予其工作所需数据的差异权限。在角色级别授予或撤消权限时，这些更改将作用到角色下的所有成员。

创建一个可以登录的角色，但是不给他设置口令：
```
postgres=# CREATE ROLE Tdapg_role1 LOGIN;
CREATE ROLE
```

创建一个可以创建数据库和管理角色的角色：
```
postgres=# CREATE ROLE Tdapg_role2 WITH CREATEDB CREATEROLE;
CREATE ROLE
```

将角色的权限赋予用户。
```
postgres=# GRANT Tdapg_role1 , Tdapg_role2 TO tdapg_user1; 
GRANT ROLE
```

## Schema
Schema 又称作模式。通过管理 Schema，允许多个用户使用同一数据库而不相互干扰，可以将数据库对象组织成易于管理的逻辑组，同时便于将第三方应用添加到相应 Schema 下而不引起冲突。 

每个数据库包含一个或多个 Schema。数据库中的每个 Schema 包含表和其他类型的对象。数据库创建初始，默认具有一个名为 public 的 Schema，且所有用户都拥有此 Schema 的权限。可以通过 Schema 分组数据库对象。Schema 类似于操作系统目录，但 Schema 不能嵌套。 

## 用户权限设置
### 库级权限管理
使用超级用户创建用户 user1，并创建测试数据库。
```
postgres=# create user user1 password 'tdapg@123';
CREATE ROLE

postgres=# create database testdb;
CREATE DATABASE
```

赋予用户 user1 测试库增删查改权限。
```
postgres=# grant create,connect on database testdb to user1;
GRANT
```

使用用户 user1 进行测试库的增删查改操作。
```
[tdapg@TENCENT64 ~]$ psql -d testdb -p 11347 -U user1
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.


testdb=> create schema schm_user1;
CREATE SCHEMA
testdb=> create table schm_user1.t1(id int);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
testdb=> INSERT INTO schm_user1.t1 VALUES(1);
INSERT 0 1
testdb=> select * from schm_user1.t1;
 id 
----
 1
(1 row) 


testdb=> delete from schm_user1.t1 ;
DELETE 1
```

使用用户 user1 进行登录，回收 user1 用户的权限。
```
postgres=# revoke all on database testdb from user1;
REVOKE
```

使用 user1 连接 testdb 数据库，执行创建 schema 无权限，权限回收成功。
```
[tdapg@TENCENT64 ~]$ psql -d testdb -p 11347 -U user1
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
 
testdb=> create schema schema_user1;
ERROR: permission denied for database testdb
```

### 表级权限管理
授权用户可以增删改查某个表记录。
使用管理员 dbadmin 连接到某个 CN 节点，下面操作相同。

授权用户可以访问某个模式。
```
postgres=# CREATE SCHEMA mysch;
CREATE SCHEMA
postgres=# CREATE USER user1 PASSWORD 'tdapg@123';
CREATE ROLE
postgres=# CREATE TABLE mysch.t2(id int,name text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# GRANT usage ON SCHEMA mysch TO user1; 
GRANT
```
>?默认情况下，普通用户是无法访问没授权的 schema，所以要授权用户访问某个表的访问权限，则需要先将表所在的 schema 使用权分配给用户。 
如果模式访问无权限，则提示 `ERROR: permission denied for schema mysch`。

授权用户可以增删改查某个表记录。
```
postgres=# GRANT SELECT ON mysch.t2 TO user1; 
GRANT
postgres=# GRANT ALL ON mysch.t2 TO user1; 
GRANT 
```
>?增，删，改，查分别对应 INSERT/DELETE/UPDATE/SELECT。 如果需要全部权限，则可以写成 all。

移除用户的访问权限。
```
postgres=# REVOKE ALL ON mysch.t2 FROM user1;
REVOKE 
postgres=# REVOKE SELECT ON mysch.t2 FROM user1; 
REVOKE 
```

将某个模式下所有表访问权限分配给某个用户。
```
postgres=# CREATE TABLE mysch.t4(f1 serial,f2 int); 
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# CREATE TABLE mysch.t5(f1 serial,f2 int); 
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# GRANT ALL ON ALL TABLES IN SCHEMA mysch TO user1; 
GRANT 
postgres=# \c - user1
You are now connected to database "postgres" as user "user1".
postgres=> SELECT * FROM mysch.t4;
 f1 | f2 
----+----
(0 rows)
 

postgres=> SELECT * FROM mysch.t5;
 f1 | f2 
----+----
(0 rows)
postgres=> \q
```

使用管理员 dbadmin 连接到某个 CN 节点，下面操作相同。
取消某个模式下所有表访问权限：
```
postgres=# REVOKE ALL ON ALL TABLES IN SCHEMA mysch FROM user1; 
REVOKE
```

### 字段级权限管理
使用超级用户创建不同的用户 user1，并创建测试数据库及表 `t0(id int ，name varchar(10)，num varchar(20));`。
```
postgres=# create user user1 password 'tdapg@123';
CREATE ROLE 
postgres=# create database testdb;
CREATE DATABASE
postgres=# \c testdb
You are now connected to database "testdb" as user "dbadmin".
testdb=# create table t0(id int,name varchar(10),num varchar(20)) distribute by replication; CREATE TABLE
```

赋予用户 user1 表 t0 的 ID 字段增删查改权限。
```
testdb=# grant select(id),insert(id),update(id) on t0 to user1;
GRANT
```

使用用户 user1 对 t0 表的增删查改操作，在单独进行 ID 列的操作。
```
[tdapg@TENCENT64 ~]$ psql -d testdb -p 11347 -U user1
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
 
testdb=> insert into t0 values(1,1,1);
ERROR: permission denied for relation t0
testdb=> update t0 set name=2;
ERROR: permission denied for relation t0
testdb=> select * from t0;
ERROR: permission denied for relation t0
testdb=> insert into t0(id) values(1);
INSERT 0 1
testdb=> update t0 set id=2;
UPDATE 1
testdb=> select id from t0;
id
----
  2
(1 row)
```
 
使用超级用户连接 testdb 数据库，收回 user1 全部权限并查看权限信息。
```
[tdapg@VM-16-32-tlinux ~]$ psql -d testdb -U dbadmin -p 11347
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.


testdb=# revoke all(id) on t0 from user1;
REVOKE
```

使用用户 user1 对 t0 表的增删查改操作，无操作权限，权限回收成功。
```
[tdapg@TENCENT64 ~]$ psql -d testdb -p 11347 -U user1
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
 
testdb=> insert into t0 values(1,1,1);
ERROR: permission denied for relation t0
testdb=> update t0 set id=2;
ERROR: permission denied for relation t0
testdb=> select * from t0;
ERROR: permission denied for relation t0
testdb=> insert into t0(id) values(1);
ERROR: permission denied for relation t0
testdb=> select id from t0;
ERROR: permission denied for relation t0
```

## 帐号安全
### 帐号安全策略
TDSQL-A PostgreSQL版 把传统数据库系统 DBA 的角色分解为三个相互独立的角色：安全管理员、审计管理员、数据管理员，这个三个角色之间相互制约，消除系统中的超级权限，从系统角色设计上了解决了数据安全问题 。

安全员职责：
- 定义强制访问、脱敏、加密策略。
- 安全员独立完成安全策略制定，不受管理员约束 。
- 安全策略，管理员也需要遵守，不例外。

审计员职责：
- 所有操作都可以被审计。
- 审计员独立完成审计策略制定，不受管理员约束 。
- 审计员操作被强制记录，不可更改。

原系统管理员：
- 仍具备自主访问控制权限、运维权限。
- 不可干预安全员、审计员操作。

### 帐号有效期
```
postgres=# create role user1 with login password 'user1@123' VALID UNTIL '2023-09-30 23:59:59'; 
CREATE ROLE
```
`VALID UNTIL '2023-09-30 23:59:59'` 表示用户密码到期时间戳，`VALID UNTIL 'infinity'` 让一个口令永远有效。

### 密码安全管理
TDSQL-A PostgreSQL版 中密码始终以加密方式存储在系统目录中。加密方式可以通过 password_encryption 参数配置。
```
postgres=# show password_encryption;
 password_encryption 
---------------------
 md5
(1 row)

postgres=# select passwd from pg_shadow where usename='user1';
        passwd         
-------------------------------------
 md57a215dcdf258f57c76edeec46243f85b
(1 row)
```

设置用户密码过时时间戳。
```
postgres=# alter role user1 with VALID UNTIL '2023-09-30 23:59:59';
ALTER ROLE 
postgres=# alter role user1 with VALID UNTIL 'infinity'; 
ALTER ROLE 
```
`VALID UNTIL '2023-09-30 23:59:59'` 表示用户密码到期时间戳，`VALID UNTIL 'infinity'` 让一个口令永远有效 。
