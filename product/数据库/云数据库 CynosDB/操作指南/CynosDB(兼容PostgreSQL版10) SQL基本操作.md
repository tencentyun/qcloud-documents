# CynosDB(兼容PostgreSQL版10) SQL基本操作
* 查询版本
postgres=# select cynosdb_version();
 
cynosdb_version 
————————
 CynosDB 1.0
(1 row)


* 建表使用
postgres=# create table x(x1 int, x2 int);
CREATE TABLE

postgres=# insert into x values(1, 2);
INSERT 0 1

postgres=# update x set x1 = 1;
UPDATE 1

* 创建视图
postgres=# create view v_x as select * from x;
CREATE VIEW

postgres=# select * from v_x;

 x1 | x2 
——+——
  1 |  2
(1 row)

* 查询使用
postgres=# select * from x;


 x1 | x2 
——+——
  1 |  2
(1 row)

* 查询cynosdb元数据IP
postgres=# show cynosdb_filesystem_endpoint ;

 cynosdb_filesystem_endpoint 
——————————————
 100.121.151.14:2379
(1 row)

* 系统表
CynosDB完全支持PG10系统表，例如：pg_class, pg_proc等。

* GUC参数
CynosDB兼容PG10的GUC参数，使用SHOW或者SET命令可以显示和设置GUC参数。

* index
CynosDB支持多种索引：B-tree、Hash、GiST、SP-GiST、GIN以及BRIN，默认的CREATE INDEX创建的是B-tree索引。

* 多列和单列索引
postgres=# CREATE TABLE test2 (
postgres(#   major int,
postgres(#   minor int,
postgres(#   name varchar
postgres(# );
CREATE TABLE

* 支持多列索引
postgres=# CREATE INDEX test2_mm_idx ON test2 (major, minor);
CREATE INDEX

* 支持单列索引
postgres=# CREATE INDEX test2_mm ON test2 (name);
CREATE INDEX

* 表达式索引
与PG10兼容，CynosDB支持表达式索引
postgres=# CREATE INDEX test2_expr ON test2 ((major + minor));
CREATE INDEX
