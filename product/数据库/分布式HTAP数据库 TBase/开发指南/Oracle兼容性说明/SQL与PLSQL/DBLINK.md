数据库链接（DATABASE LINK），简写为 DBLINK。它是一个存在于本地库中的指针，它使您可以访问远端库上的数据和对象。为了使应用可以访问分布式数据库系统的非本地库中的数据和用户对象，就需要使用 DBLINK。

数据库链接定义了从一个数据库到另一个数据库的通信路径。当应用程序使用数据库链接访问远程数据库时，Oracle 数据库代表本地应用程序请求在远程数据库中建立数据库会话。

有两种主要类型的 DBLINK：私有 DBLINK 和公有 DBLINK。私有 DBLINK 只有创建 DBLINK 的用户才可以使用；公有 DBLINK 可以被所有的数据库用户使用。

此处 DBLINK 是指从 TDSQL PostgreSQL版（Oracle 兼容）访问 Oracle，如需 Oracle 访问 TDSQL PostgreSQL版（Oracle 兼容），可通过透明网关实现，TDSQL PostgreSQL版（Oracle 兼容）之间的访问可用 postgres_fdw 扩展创建外部表实现。

## 语法
创建插件：
```
CREATE EXTENSION ORACLE_FDW;
```
    
创建 DBLINK：
```
CREATE [ PUBLIC ] DATABASE LINK dblink CONNECT TO user IDENTIFIED BY password USING connect_string;
```
    
DBLINK 使用：
```
[ schema.]{ TABLE | VIEW }@dblink
```
在表或视图名后加 `@dblink` 表示访问的是远端数据库对象。
    
删除 DBLINK：
```
DROP [ PUBLIC ] DATABASE LINK dblink;
```
相关系统表：系统表 `PG_DBLINK` 中存储了已创建的 DBLINK 信息。

## 使用限制
- 创建 DBLINK 前需要先创建扩展 ORACLE_FDW。
- DBLINK 支持增删改操作，但删除、修改需要表有主键。
- 暂不支持访问远端 Oracle 中同义词对象。
- 只有超级用户可创建 PUBLIC DBLINK。
- 普通用户创建 DBLINK 报错：`permission denied for foreign-data wrapper oracle_fdw` 可通过授权解决：`grant usage on foreign data wrapper oracle_fdw to user`。
- Oracle 字符集与 TDSQL PostgreSQL版（Oracle 兼容）可能会有差异，当前 TDSQL PostgreSQL版（Oracle 兼容）数据库字符集为 GBK 或 GB18030 时，DBLINK 访问时 Oracle 端都会设置为 ZHS16GBK。
- 由于占⽤了关键字“@”，导致 TDSQL PostgreSQL版（Oracle 兼容）⽀持的“@”操作符失效，如需使⽤，使⽤ `abs` 函数代替之。

```
postgres=# select @ -0.5; 
ERROR: syntax error at or near "@" 
LINE 1: select @ -0.5; 
^ 
postgres=# select abs(-0.5); 

abs 
----- 

0.5 
(1 row) 
```
  
## 示例
```
postgres=# create extension ORACLE_FDW;
CREATE EXTENSION

创建 DBLINK：
postgres=# CREATE DATABASE LINK abc CONNECT TO "JENNY" IDENTIFIED BY 'jenny' USING '(DESCRIPTION = 
(ADDRESS = (PROTOCOL = TCP)(HOST = 100.98.176.136)(PORT = 1521)) 
(CONNECT_DATA = 
(SERVER = DEDICATED) 
(SERVICE_NAME = oracle.oracle) 
) 
)'; 
CREATE DATABASE LINK 

查询 dblink 系统表： 
postgres=# select * from pg_dblink ; 
dblinkname | dblinkowner | username | created | host 
| port | dblinkkind | dblink_foreign_server 
------------+-------------+----------+-------------------------------+------------ 
----+------+------------+----------------------- 
abc | weily | JENNY | 2020-08-11 18:24:30.425309+08 | 100.98.176. 
136 | 1521 | 0 | ora_dblink_abc 
(1 row) 

访问远程表： 
postgres=# select * from "JENNY"."FOO"@abc; 
ID | STR 
----+----- 
1 | a 
(1 row) 
postgres=# select * from PG_TEST@abc; 
ID | STR 
----+----- 
1 | a 
2 | b 
4 | d 
3 | c 
(4 rows) 
```

