
## 查询版本
```
postgres=# select cynosdb_version(); cynosdb_version
————————
 CynosDB 1.0
(1 row)
```

## 建表使用
```
postgres=# create table x(x1 int, x2 int);
CREATE TABLE

postgres=# insert into x values(1, 2);
INSERT 0 1

postgres=# update x set x1 = 1;
UPDATE 1
```

## 创建视图
```
postgres=# create view v_x as select * from x;
CREATE VIEW

postgres=# select * from v_x;

 x1 | x2
——+——
  1 |  2
(1 row)
```

## 查询使用
```
postgres=# select * from x;


 x1 | x2
——+——
  1 |  2
(1 row)
```

## 系统表
TDSQL-C for PostgreSQL 完全支持 PG10 系统表，例如 pg_class, pg_proc 等。

## GUC 参数
TDSQL-C for PostgreSQL 兼容 PG10 的 GUC 参数，使用 SHOW 或者 SET 命令可以显示和设置 GUC 参数。

## index
TDSQL-C for PostgreSQL 支持多种索引：B-tree、Hash、GiST、SP-GiST、GIN 以及 BRIN，默认的 CREATE INDEX 创建的是 B-tree 索引。

## 多列和单列索引
```
postgres=# CREATE TABLE test2 (
postgres(#   major int,
postgres(#   minor int,
postgres(#   name varchar
postgres(# );
CREATE TABLE
```

## 支持多列索引
```
postgres=# CREATE INDEX test2_mm_idx ON test2 (major, minor);
CREATE INDEX
```

## 支持单列索引
```
postgres=# CREATE INDEX test2_mm ON test2 (name);
CREATE INDEX
```

## 表达式索引
与 PG10 兼容，TDSQL-C for PostgreSQL 支持表达式索引。
```
postgres=# CREATE INDEX test2_expr ON test2 ((major + minor));
CREATE INDEX
```

