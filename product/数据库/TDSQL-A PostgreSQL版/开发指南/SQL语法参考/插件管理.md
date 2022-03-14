TDSQL-A PostgreSQL版 支持多种模块，开放模块扩展接口。用户可以使用语法 CREATE EXTENSION 将一个新加的扩展载入到数据库中。不能有同名的拓展被载入。

载入一个扩展本质上是运行该扩展的脚本文件。该脚本通常将创建新的 SQL 对象，例如函数、数据类型、操作符以及索引支持方法。
CREATE EXTENSION 会额外地记录所有被创建对象的标识，发出 DROP EXTENSION 时可以删除它们。在使用 CREATE EXTENSION 载入扩展到数据库之前，必须先安装好该扩展的支持文件。

当前可以用于载入的扩展，可以在系统视图 [pg_available_extension_versions](http://postgres.cn/docs/10/view-pg-available-extension-versions.html) 中看到。
当前已经部署的拓展，可以通过系统表 pg_extension 查看，也可以通过 psql 的元命令 \dx 查看。
请勿删除系统默认已经存在的拓展，避免发生不可预知的集群故障。

## 插件管理
部分集群默认已有的插件如下：
- pageinspect：pageinspect 模块提供函数让用户从低层次观察数据库页面的内容，这对于调试目的很有用。
- pg_check：检查 catalog 一致性的工具。
- pg_clean：清理残留的二阶段事务提交的工具。
- pg_errcode_stat：跟踪集群进程的一场的插件。
可访问函数 pg_errcode_stat 查看当前集群异常，通过 pg_errcode_stat_reset 进行清理。
- pg_squeeze：回收部分无效空间资源的插件，相较于 vacuum full 不会有太长时间的锁表情况，导致无法进行读写。
- pg_stat_error：跟踪集群进程的一场的插件。
- pg_stat_log：跟踪所有 SQL 的执行信息。
- pg_stat_statements：模块提供一种方法追踪一个服务器所执行的所有 SQL 语句的执行统计信息。
- pg_unlock：用于检测和解除死锁的工具。
- plpgsql：PL/pgSQL 函数语言插件。
- Plpythonu：PL/python 函数语言插件。

### 查看插件
```
postgres=# SELECT e.extname AS "Name", e.extversion AS "Version", n.nspname AS "Schema", c.description
AS "Description" FROM pg_catalog.pg_extension e LEFT JOIN pg_catalog.pg_namespace n ON n.oid =
e.extnamespace LEFT JOIN pg_catalog.pg_description c ON c.objoid = e.oid AND c.classoid =
'pg_catalog.pg_extension'::pg_catalog.regclass ORDER BY 1;
Name | Version | Schema | Description
--------------------+---------+------------+-----------------------------------------------------------
pageinspect | 1.1 | public | inspect the contents of database pages at a low level
pg_errcode_stat | 1.1 | public | track error code of all processes
pg_stat_statements | 1.1 | public | track execution statistics of all SQL statements executed
plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
shard_statistic | 1.0 | public | tools for get shard statistic
(5 rows)
```

### 添加插件
```
postgres=# create extension "uuid-ossp" with schema tdapg;
CREATE EXTENSION
```
上面的语句把"uuid-ossp"创建到模式 tdapg 下。

### 删除插件
```
postgres=# drop extension "uuid-ossp" ;
DROP EXTENSION
```

## 插件 pg_trgm 使用
前模糊，后模糊，前后模糊，正则匹配都属于文本搜索领域常见的需求。TDSQL-A PostgreSQL版 在文本搜索领域除了全文检索，还有 TRGM。
对于前模糊和后模糊，TDSQL-A PostgreSQL版 与其他数据库一样，可以使用 btree 来加速。
对于前后模糊和正则匹配，则可以使用 TRGM，TRGM 是一个非常强的插件，对这类文本搜索场景性能提升非常有效，100万左右的数据量，性能提升有100倍以上。
创建插件：
```
postgres=# create extension pg_trgm;;
CREATE EXTENSION
```
创建需要进行全文检索的表：
```
postgres=# create table t_trgm (id int,trgm text,no_trgm text);
CREATE TABLE
```
插入测试数据：
```
postgres=# insert into t_trgm select t,md5(t::text),md5(t::text) from generate_series(1,1000000) as t;
INSERT 0 1000000
```
创建 trgm 索引：
```
postgres=# create index t_trgm_trgm_idx on t_trgm using gist(trgm gist_trgm_ops);
CREATE INDEX
```
