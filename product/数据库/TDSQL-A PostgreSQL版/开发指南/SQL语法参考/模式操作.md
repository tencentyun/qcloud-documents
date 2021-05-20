## 模式创建
标准语句：
```
postgres=# CREATE SCHEMA tdapg;
CREATE SCHEMA
```

扩展语法，不存在时才创建：
```
postgres=# CREATE SCHEMA IF NOT EXISTS tdapg ;  
NOTICE: schema "tdapg" already exists, skipping
CREATE SCHEMA
```

指定所属用户：
```
postgres=# CREATE SCHEMA tdapg_pgxz AUTHORIZATION pgxz;
CREATE SCHEMA

postgres=# \dn tdapg_pgxz
 List of schemas
  Name  | Owner 
------------+-------
 tdapg_pgxz | pgxz
(1 row)
```

## 模式修改
修改模式名：
```
postgres=# ALTER SCHEMA tdapg RENAME TO tdapg_new;
ALTER SCHEMA
```

修改所有者：
```
postgres=# ALTER SCHEMA tdapg_pgxz OWNER TO tdapg;
ALTER SCHEMA
```

## 模式删除
```
postgres=# DROP SCHEMA tdapg_new;
DROP SCHEMA
```

当模式中存在对象时，则会删除失败，提示如下：
```
postgres=# CREATE TABLE tdapg_pgxz.t(id int);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# DROP SCHEMA tdapg_pgxz;
ERROR: cannot drop schema tdapg_pgxz because other objects depend on it
DETAIL: table tdapg_pgxz.t depends on schema tdapg_pgxz
HINT: Use DROP ... CASCADE to drop the dependent objects too.
```

使用 CASCADE 强制删除：
```
postgres=# DROP SCHEMA tdapg_pgxz CASCADE;
NOTICE: drop cascades to table tdapg_pgxz.t
DROP SCHEMA
```

## 配置用户访问模式权限
普通用户对于某个模式下的对象访问除了访问对象要授权外，模式也需要授权：
```
[tdapg@VM_0_37_centos root]$ psql -U dbadmin
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.

postgres=# CREATE SCHEMA tdapg;
CREATE SCHEMA
postgres=# CREATE TABLE tdapg.t(id int);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
```

授权用户 pgxz 可以查询 tdapg.t 表：
```
postgres=# GRANT SELECT ON tdapg.t TO pgxz;
GRANT
postgres=# \q
[tdapg@VM_0_37_centos root]$ psql -U pgxz
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
```

在没授权用户可以使用 tdapg 模式前，还是无法访问：
```
postgres=> SELECT * FROM tdapg.t;
ERROR: permission denied for schema tdapg
LINE 1: SELECT * FROM tdapg.t;
           ^
postgres=> \q
[tdapg@VM_0_37_centos root]$ psql -U dbadmin
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.

postgres=# GRANT USAGE ON SCHEMA tdapg TO pgxz;
GRANT
postgres=# \q
[tdapg@VM_0_37_centos root]$ psql -U pgxz
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
```

授权用户可以使用 tdapg 模式后，可以访问 tdapg.t 表：
```
postgres=> SELECT * FROM tdapg.t;
 id 
----
(0 rows)
```

## 配置访问模式的顺序
TDSQL-A PostgreSQL版 数据库有一个运行变量叫 search_path，其值为模式名列表，用于配置访问数据对象的顺序，如下所示:

查看当前连接用户：
```
[tdapg@VM_0_37_centos root]$ psql -U dbadmin
psql (PostgreSQL 10.0 TDSQL-A for PostgreSQL)
Type "help" for help.
postgres=# SELECT current_user;
 current_user 
--------------
 dbadmin
(1 row)
```

总共两个模式：
```
postgres=# \dn
  List of schemas
   Name   | Owner 
--------------+-------
 public    | dbadmin
 tdapg    | dbadmin
(2 rows)
```

搜索路径只配置为 "$user", public，其中 "$user" 为当前用户名，即上面的 current_user 值 “dbadmin”：
```
postgres=# SHOW search_path ;
  search_path 
-----------------
 "$user", public
(1 row)
```

不指定模式创建数据表，则该表存放于第一个搜索模式下面：
```
postgres=# CREATE TABLE t_schema(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# \dt t_schema
     List of relations
 Schema |  Name  | Type | Owner 
--------+----------+-------+-------
 dbadmin| t_schema | table | dbadmin
(1 row)
```

指定表位于某个模式下，不同模式下表名可以相同：
```
postgres=# CREATE SCHEMA tdapg_schema;
CREATE SCHEMA
postgres=# CREATE TABLE tdapg_schema.t_schema (id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# \dt tdapg_schema.t_schema
      List of relations
  Schema  |  Name  | Type | Owner 
--------------+----------+-------+-------
 tdapg_schema | t_schema | table | dbadmin
(1 row)
```

访问不在搜索路径对象时，需要写全路径：
```
postgres=# CREATE TABLE tdapg_schema.t2 (id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE

postgres=# SELECT * FROM t2;
ERROR: relation "t2" does not exist
LINE 1: SELECT * FROM t2;
           ^
postgres=# SELECT * FROM tdapg_schema.t2;
 id | mc 
----+----
(0 rows)
```
上面出错是因为模式 tdapg_schema 没有配置在 search_path 搜索路径中。
