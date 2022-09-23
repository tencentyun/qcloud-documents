## q’ 转义字符
一个 Q-quote 的表达式，用来简化 SQL 或 PLSQL 中字符串的表示。

示例：
```
select q'qMy "good" Name''q' names from dual;
```
    
## WITH FUNCTION
在子查询的 WITH 子句中定义函数，并在普通 SQL 语句中使用。

### 语法
```
WITH
  FUNCTION <NAME_FUNCTION>
  BEGIN
    ...
  END;
SELECT <NAME_FUNCTION>
FROM <TABLE>;
/
```
    
### 示例
```
create table tw(t1 int, t2 int);
insert into tw values(3, 4);
insert into tw values(1, 2);
    
WITH FUNCTION raise_test_wf(int) returns int as $$
begin
raise notice 'This message has too many parameters %', $1;
return $1 + 1;
end;
$$ language plpgsql;
FUNCTION raise_test_wf2(int) returns int as $$
begin
raise notice 'This message has too many parameters %', $1;
return $1 + 1000;
end;
$$ language plpgsql;
select raise_test_wf2(t2), raise_test_wf(t1) from tw where raise_test_wf(t2) > 0 order by 1;
/
```
    
## BULK COLLECT
BULK COLLECT 可以使 SELECT 语句，可通过一次提取来检索多行，从而提高数据检索速度。

示例：
```
create table t5(f1 integer,f2 varchar(10));
    
insert into t5 values(1,'tbase1'); 
    
insert into t5 values(2,'tbase2'); 
    
DECLARE
TYPE name_tbl IS TABLE OF VARCHAR2(50);
emp_name name_tbl;
BEGIN
SELECT f2 
  BULK COLLECT INTO emp_name
  FROM t5;
FOR i IN emp_name.FIRST .. emp_name.LAST
LOOP
perform Dbms_output.put_line(i);
END LOOP;
    
END;
/
```
   
## 集合 FIRST 与 LAST
可以使用 FIRST 与 LAST 来遍历集合中的元素。

示例：
```
create table t5(f1 integer,f2 varchar(10));
insert into t5 values(1,'tbase1'); 
insert into t5 values(2,'tbase2'); 
    
DECLARE
TYPE name_tbl IS TABLE OF VARCHAR2(50);
emp_name name_tbl;
BEGIN
SELECT f2 
  BULK COLLECT INTO emp_name
  FROM t5;
FOR i IN emp_name.FIRST .. emp_name.LAST
LOOP
perform Dbms_output.put_line(i);
END LOOP;
    
END;
/
```
    
## 匿名块
没有名称的块是匿名块。匿名块仅供一次性使用。

示例：
```
create table t5(f1 integer,f2 varchar(10));
    
insert into t5 values(1,'tbase1'); 
    
insert into t5 values(2,'tbase2'); 
    
DECLARE
TYPE name_tbl IS TABLE OF VARCHAR2(50);
emp_name name_tbl;
BEGIN
SELECT f2 
  BULK COLLECT INTO emp_name
  FROM t5;
FOR i IN emp_name.FIRST .. emp_name.LAST
LOOP
perform Dbms_output.put_line(i);
END LOOP;
    
END;
/
```

## CONNECT BY
CONNECT BY 级联查询，常用于对具有树状结构的记录查询某一节点的所有子孙节点或所有祖辈节点，或通过 CONNECT BY  结合 LEVEL 来构造数据。
LEVEL 关键字，代表树形结构中的层级编号；第一层是数字1，第二层数字2，依次递增。
CONNECT_BY_ROOT 方法，能够获取第一层集结点结果集中的任意字段的值；如 CONNECT_BY_ROOT（字段名）。

### 语法
```
SELECT { * | COLUMN | expression ,...} 
FROM table [START WITH condition1]
CONNECT BY [PRIOR] id=parentid
```
一般用来查找存在父子关系的数据，也就是树形结构的数据，其返还的数据也能够明确区分出每一层的数据。
START WITH condition1 是用来限制第一层的数据，或者叫根节点数据，以这部分数据为基础来查找第二层数据，然后以第二层数据查找第三层数据，以此类推。
CONNECT BY [PRIOR] id=parentid 这部分是用来指明 Oracle 在查找数据时，以怎样的一种关系去查找，例如，查找第二层的数据时用第一层数据的 ID 去跟表里面记录的 parentid 字段进行匹配，如果这个条件成立那么查找出来的数据就是第二层数据，同理查找第三层第四层，以此类推。

另一种写法：
```
SELECT { * | COLUMN | expression ,...} 
FROM table [START WITH condition1]
CONNECT BY id=[PRIOR] parentid
```
这种用法就表示从下往上查找数据，可以理解为从叶子节点往上查找父级几点，用第一层数据的parentid去跟表记录里面的id进行匹配，匹配成功那么查找出来的就是第二层数据；上面的那种就是从父级节点往下查找叶子节点。

### 使用限制
- connect by 用法较多，当前 TDSQL PostgreSQL-O版 能支持常用的写法，某些写可能不支持。
- 暂时不支持 CONNECT_BY_ROOT 方法。
- 暂不支持基于临时表的 connect by。
- select * 输出的字段里多了隐藏字段 ctid、xc_node_id、tableoid、\_level_1，需要根据需要输出指定字段。
- Connect by 和 rownum 结合计算，可能会存在逻辑错误。

### 示例
```
postgres=# create table tab_test (id int, fid int,remark varchar(16));
CREATE TABLE
postgres=# insert into tab_test values(0,-1,'根节点');
INSERT 0 1
postgres=# insert into tab_test values(1,0,'第二层节点1');
INSERT 0 1
postgres=# insert into tab_test values(2,0,'第二层节点2');
INSERT 0 1
postgres=# insert into tab_test values(3,1,'第三层节点1');
INSERT 0 1
postgres=# insert into tab_test values(4,1,'第三层节点2');
INSERT 0 1
  
1）从根节点查找叶子节点
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 0
connect by prior t.id = t.fid;
  id | fid |   remark| level 
----+-----+-------------+-------
  0 |  -1 | 根节点  | 1
  1 |   0 | 第二层节点1 | 2
  2 |   0 | 第二层节点2 | 2
  3 |   1 | 第三层节点1 | 3
  4 |   1 | 第三层节点2 | 3
(5 rows)
    
2）从叶子节点查询上层节点
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 4
connect by t.id = prior t.fid;
  id | fid |   remark| level 
----+-----+-------------+-------
  4 |   1 | 第三层节点2 | 1
  1 |   0 | 第二层节点1 | 2
  0 |  -1 | 根节点  | 3
(3 rows)
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 4
connect by prior t.fid = t.id;
  id | fid |   remark| level 
----+-----+-------------+-------
  4 |   1 | 第三层节点2 | 1
  1 |   0 | 第二层节点1 | 2
  0 |  -1 | 根节点  | 3
(3 rows)
    
3）生成数字序列结果集
postgres=# select rownum from dual connect by rownum<=10;
  rownum 
--------
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
(10 rows)
postgres=# select rownum from dual connect by level<=10;
  rownum 
--------
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
(10 rows)
    
4）字符串分割，由一行变为多行
postgres=# select REGEXP_SUBSTR('01#02#03#04', '[^#]+', 1, rownum::int) as newport 
from dual connect by rownum <= REGEXP_COUNT('01#02#03#04', '[^#]+');
  newport 
---------
  01
  02
  03
  04
(4 rows)
    
5）暂不支持临时表的connect by
postgres=# select t.*, level
  from (select 1 as num from dual
union
select 2 as num from dual
) t
connect by level <= 3;
ERROR:  connect by support one table yet
```

## DBLINK
数据库链接（DATABASE LINK），简写 DBLINK。它是一个存在于本地库中的指针，它可以访问远端库上的数据和对象。为了让应用可以访问分布式数据库系统中，非本地库中的数据和用户对象，就需要使用 DBLINK。
数据库链接定义了从一个数据库到另一个数据库的通信路径。当应用程序使用数据库链接访问远程数据库时，Oracle 数据库代表本地应用程序请求在远程数据库中建立数据库会话。
支持两种主要类型的 DBLINK：私有 DBLINK 和 公有DBLINK。私有 DBLINK 只有创建 DBLINK 的用户才可以使用；公有 DBLINK 可以被所有的数据库用户使用。

此处 DBLINK 是指从 TDSQL PostgreSQL-O版 访问 Oracle，如需 Oracle 访问 TDSQL PostgreSQL-O版，可通过透明网关实现，TDSQL PostgreSQL-O版 访问 TDSQL PostgreSQL-O版 可用 postgres_fdw 扩展创建外部表实现。

### 语法
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
在表或视图名后加 @dblink 表示访问的是远端数据库对象。
    
删除 DBLINK：
```
DROP [ PUBLIC ] DATABASE LINK dblink;
```

### 相关系统表
系统表 PG_DBLINK 中存储了已创建的 DBLINK 信息。

### 使用限制
- 创建 DBLINK 前需要先创建扩展 ORACLE_FDW。
- DBLINK 支持增删改操作，但删除、修改需要表有主键。
- 暂不支持访问远端 Oracle 中同义词对象。
- 只有超级用户可创建 PUBLIC DBLINK。
- 普通用户创建 DBLINK 报错：`permission denied for foreign-data wrapper oracle_fdw` 可通过授权解决：`grant usage on foreign data wrapper oracle_fdw to user`。
- Oracle 字符集与 TDSQL PostgreSQL-O版 可能会有差异，当前 TDSQL PostgreSQL-O版 数据库字符集为 GBK 或 GB18030 时，DBLINK 访问 Oracle 端都会设置为 ZHS16GBK。
- 由于占⽤了关键字“@”，导致原 TDSQL PostgreSQL-O版 ⽀持的“@”操作符失效，如需使⽤，⽤ abs 函数代替之 。

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
  
### 示例
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

## 分布键为 NULL
开启 Oracle 兼容参数设置后，分布键支持为 NULL。

示例：
```
postgres=# set enable_oracle_compatible to on;
SET
postgres=# create table tbl_shard_null(f1 int,f2 varchar(16)) distribute by shard(f1);
CREATE TABLE
postgres=# \d+ tbl_shard_null
  Table "public.tbl_shard_null"
  Column | Type  | Collation | Nullable | Default | Storage  | Stats target | Description 
--------+-----------------------+-----------+----------+---------+----------+--------------+------------
  f1 | integer   |   |  | | plain|  | 
  f2 | character varying(16) |   |  | | extended |  | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
postgres=# insert into tbl_shard_null select null,'null';
INSERT 0 1
postgres=# select * from tbl_shard_null ;
  f1 |  f2  
----+------
  | null
(1 row)
```
    
## 支持不同字段类型 UNION ALL 合并
PostgreSQL 只支持相同字段类型 UNION ALL 合并，TDSQL PostgreSQL-O版 则支持不同字段类型的合并。

示例：
```
postgres=# select 1 as f1,2 as f2,'111' as f3 union all select 11,'22',33;
  f1 | f2 | f3  
----+----+-----
  1 |  2 | 111
  11 | 22 |  33
(2 rows)
```
   
## 支持只读事务时可以获取序列的下一个值
Oracle 支持只读事务时可以获取序列的下一个值，TDSQL PostgreSQL-O版 兼容 Oracle 该用法。

示例：
```
postgres=# CREATE SEQUENCE seq_userid;
CREATE SEQUENCE
postgres=# select nextval('seq_userid');
  nextval 
---------
  1
(1 row)
postgres=# begin transaction read only;
BEGIN
postgres=# select nextval('seq_userid');
  nextval 
---------
  2
(1 row)
postgres=# rollback ;
ROLLBACK
postgres=# select nextval('seq_userid');
  nextval 
---------
  3
(1 row)
```
    
## 支持非分布键关联删除和更新数据
支持非分布键关联删除和更新数据。
    
示例：
```
postgres=# create table t1(f1 int not null,f2 int);
CREATE TABLE
postgres=# create table t2 (f1 int not null, f2 int);
CREATE TABLE
postgres=# \d+ t1
Table "public.t1"
  Column |  Type   | Collation | Nullable | Default | Storage | Stats target | Description 
--------+---------+-----------+----------+---------+---------+--------------+-------------
  f1 | integer |   | not null | | plain   |  | 
  f2 | integer |   |  | | plain   |  | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
    
postgres=# \d+ t2
Table "public.t2"
  Column |  Type   | Collation | Nullable | Default | Storage | Stats target | Description 
--------+---------+-----------+----------+---------+---------+--------------+-------------
  f1 | integer |   | not null | | plain   |  | 
  f2 | integer |   |  | | plain   |  | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
表 t1、t2 的 f1 字段为分布键
    
postgres=# insert into t1 values (1,1),(2,2),(3,3),(4,4),(5,5);
COPY 5
postgres=# insert into t2 values (4,4),(5,5),(6,6),(7,7),(8,8);
COPY 5
    
用非分布键关联删除数据
postgres=# delete from t1 where f2 in (select f2 from t2);
DELETE 2
postgres=# select * from t1;
  f1 | f2 
----+----
  1 |  1
  2 |  2
  3 |  3
(3 rows)
    
删除符合条件的数据应该是 t1.f2 为4、5的两条数据
postgres=# insert into t1 values(4,4),(5,5);
COPY 2
    
用非分布键关联更新数据
postgres=# update t1 set f2=100 where exists (select 1 from t2 where t1.f2=t2.f2);
UPDATE 2
    
同样关联更新的应该是 t1.f2 为4、5的两条数据
postgres=# select * from t1;
  f1 | f2  
----+-----
  1 |   1
  2 |   2
  5 | 100
  3 |   3
  4 | 100
(5 rows)
```
    
## 支持带复杂子查询删除功能
支持带复杂子查询删除功能。

示例：
```
postgres=# create table t1( id int not null,a int);
CREATE TABLE
postgres=# create table t2(a int not null,b int);
CREATE TABLE
postgres=# insert into t1 values(1,2),(2,3),(3,4);
COPY 3
postgres=# insert into t2 values(1,2),(2,3),(3,4);
COPY 3
    
子查询中两表关联
postgres=# delete from t1 where id in(select a.id from t1 a join t2 b on a.a=b.a where a.id>1);
DELETE 1
    
子查询关联结果符合条件的是 t1.id=2 这一条   
postgres=# select * from t1;
  id | a 
----+---
  1 | 2
  3 | 4
(2 rows)
```

## PIVOT
PIVOT 是 Oracle 的行转列函数，通过 PIVOT 函数，可以快速实现行转列的输出，而不需要用 DECODE 或 CASE 结合 GROUP BY 复杂的 SQL 实现。
TDSQL PostgreSQL-O版 兼容 PIVOT 用法。

### 语法
```
SELECT STATEMENT
PIVOT (aggreate_function FOR pivot_column IN ( list of values) )
[ ORDER BY { column_name | expr } [, ...] ];
```
    
### 示例
```
postgres=# create table stu_score (stu_name varchar2(16),course varchar2(16),score number(5,2));
CREATE TABLE
postgres=# insert into stu_score values('STU_A','CHINESE',70);
INSERT 0 1
postgres=# insert into stu_score values('STU_A','ENGLISH',80);
INSERT 0 1
postgres=# insert into stu_score values('STU_A','MATH',81);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','CHINESE',86);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','ENGLISH',77);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','MATH',69);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','CHINESE',80);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','ENGLISH',82);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','MATH',88);
INSERT 0 1
postgres=# select * from stu_score;
  stu_name | course  | score 
----------+---------+-------
  STU_B| CHINESE | 86.00
  STU_B| ENGLISH | 77.00
  STU_B| MATH| 69.00
  STU_C| CHINESE | 80.00
  STU_C| ENGLISH | 82.00
  STU_C| MATH| 88.00
  STU_A| CHINESE | 70.00
  STU_A| ENGLISH | 80.00
  STU_A| MATH| 81.00
(9 rows)
    
postgres=# select * from stu_score
pivot ( max(score) for course in ('CHINESE' as CHINESE,'ENGLISH' as ENGLISH,'MATH' as MATH));
  stu_name | chinese | english | math  
----------+---------+---------+-------
  STU_B|   86.00 |   77.00 | 69.00
  STU_C|   80.00 |   82.00 | 88.00
  STU_A|   70.00 |   80.00 | 81.00
(3 rows)
```
    
## UNPIVOT
UNPIVOT 是 Oracle 的列转行函数，通过 UNPIVOT 函数，可以快速实现列转行的输出，而不需要用多个 SQL UNION [ALL]  实现。
TDSQL PostgreSQL-O版 兼容 UNPIVOT 用法。

### 语法
```
SELECT STATEMENT
UNPIVOT( column_name FOR unpivot_column IN ( list of values))
[ ORDER BY { column_name | expr } [, ...] ];
```
    
### 示例
```
postgres=# create table stu_score_b as select stu_name,
max(case when course='CHINESE' then score end) CHINESE,
max(case when course='ENGLISH' then score end) ENGLISH,
max(case when course='MATH' then score end) MATH
from stu_score
group by stu_name;
INSERT 0 3
postgres=# select * from stu_score_b;
  stu_name | chinese | english | math  
----------+---------+---------+-------
  STU_B|   86.00 |   77.00 | 69.00
  STU_C|   80.00 |   82.00 | 88.00
  STU_A|   70.00 |   80.00 | 81.00
(3 rows)
    
postgres=# select *
from stu_score_b   
unpivot ( score for course in (CHINESE ,ENGLISH ,MATH )) 
order by stu_name;
  stu_name | score | course  
----------+-------+---------
  STU_A| 81.00 | MATH
  STU_A| 80.00 | ENGLISH
  STU_A| 70.00 | CHINESE
  STU_B| 86.00 | CHINESE
  STU_B| 77.00 | ENGLISH
  STU_B| 69.00 | MATH
  STU_C| 88.00 | MATH
  STU_C| 82.00 | ENGLISH
  STU_C| 80.00 | CHINESE
(9 rows)
    
postgres=# select stu_name,score,course
from stu_score_b unpivot ( score for course in (CHINESE ,ENGLISH ))
order by stu_name;
  stu_name | score | course  
----------+-------+---------
  STU_A| 70.00 | CHINESE
  STU_A| 80.00 | ENGLISH
  STU_B| 86.00 | CHINESE
  STU_B| 77.00 | ENGLISH
  STU_C| 80.00 | CHINESE
  STU_C| 82.00 | ENGLISH
(6 rows)
```
    
## MERGE INTO
Oracle 中 MERGE INTO 语句是将 INSERT 和 UPDATE 语句结合，同时实现 INSERT 和 UPDATE，与表匹配的行进行更新，不匹配的行写入表中。
TDSQL PostgreSQL-O版 兼容 MERGE INTO 语法。

### 语法
```
MERGE INTO [schema.]{table|view} [t_alias]
USING { [schema.]{table|view} | subquery } [t_alias] ON (condition)
[ merge_update_clause ]
[ merge_insert_clause ];
    
merge_update_clause:
WHEN MATCHED THEN 
UPDATE SET 
column = {expr | DEFAULT} [, column = {expr | DEFAULT}, ... ]
where condition
DELETE where condition
    
merge_insert_clause:
WHEN NOT MATCHED THEN INSERT 
( column [, column , ... ]
VALUES ({expr | DEFAULT} [, ... ]
where_clause
```
其中，ON (condition) 匹配条件，必须能从被关联的表、视图、子查询得到唯一的记录，否则报错。
    
### 示例
```
drop table test1;
create table test1(id int primary key,name varchar2(10));
insert into test1 values(1,'test1');
insert into test1 values(2,'test1');
insert into test1 values(3,'test1');
    
drop table test2;
create table test2(id int primary key,name varchar2(10));
insert into test2 values(2,'test2');
insert into test2 values(3,'test2');
insert into test2 values(4,'test2');
insert into test2 values(5,'test2'); 
    
postgres=# MERGE INTO test1 t
USING (
  select * from test2
) t2 ON (t.id = t2.id)
WHEN MATCHED THEN UPDATE SET t.name = t2.name WHERE t.id = t2.id 
WHEN NOT MATCHED THEN INSERT (id,name) VALUES (t2.id, t2.name) ;
MERGE 4
上面的 sql 实现的功能为：将 test2 表的数据与 test1 表的数据用 id 关联匹配，匹配到的行用 test2.name 更新 test1.name，将没有匹配到 test2 的行写入 test1 表中


查询 test1 表，id=2、3 的数据 name 更新为 test2 表 name 值 test2，test2 表 id=4、5 的数据写入 test1 表，结果符合预期
postgres=# select * from test1;
  id | name  
----+-------
  1 | test1
  2 | test2
  5 | test2
  3 | test2
  4 | test2
(5 rows)
```

## DELETE table_name 支持不带 FROM
通常标准的 SQL 语法在 DELETE 时，需要带 FROM 关键字，如 DELETE FROM table WHERE expr，Oracle 中可以省略 FROM 关键字。
TDSQL PostgreSQL-O版 兼容 DELETE 时省略 FROM 关键字用法。

### 语法
```
DELETE [ FROM] table_name [ WHERE expr ];
```
    
#### 示例
```
postgres=# create table tbl_del (id int,info varchar(16));
CREATE TABLE
postgres=# insert into tbl_del values(1,'a'),(2,'b'),(3,'c');
COPY 3
postgres=# delete tbl_del where id=3;
DELETE 1
postgres=# delete from tbl_del where id=2;
DELETE 1
```
    
## UPDATE 支持 表名.字段名 = xxx 付值
UPDATE 更新表时，支持字段名前加表名，或表别名的写法。

### 语法
```
UPDATE table_name [ [ as ] table_alias ] 
SET [{ table_name | table_alias }.]column_name = { value | expr | column_name } [, ... ] 
[ WHERE expr ];
```
    
### 示例
```
postgres=# create table tbl_upd (id int, info varchar(16));
CREATE TABLE
postgres=# insert into tbl_upd values(1,'a'),(2,'b'),(3,'c');
COPY 3
postgres=# update tbl_upd set tbl_upd.info=tbl_upd.info||'1' where tbl_upd.id=3;
UPDATE 1
postgres=# select * from tbl_upd where id=3;
  id | info 
----+------
  3 | c1
(1 row)
postgres=# update tbl_upd t1 set t1.info=t1.info||'1' where t1.id=2;
UPDATE 1
postgres=# select * from tbl_upd where id=2;
  id | info 
----+------
  2 | b1
(1 row)
postgres=# update tbl_upd as t1 set t1.info=t1.info||'1' where t1.id=1;
UPDATE 1
postgres=# select * from tbl_upd where id=1;
  id | info 
----+------
  1 | a1
(1 row)
```
    
## HINT
对于一些执行计划不是最优的 SQL，可以通过 SQL HINT 来干预执行计划的生成，例如，对指定表的全表扫描，用指定的索引，用指定的表关联算法等。
TDSQL PostgreSQL-O版 兼容常用 Oracle 的 HINT 用法，同时支持基于 pg_hint_plan 的 HINT 用法。

### 语法
```
{ DELETE |INSERT | SELECT | UPDATE } /*+ hint1 [hint2 ...] */ statement;
```
其中：
- DELETE、INSERT、SELECT 和 UPDATE 是标识一个语句块开始的关键字，包含提示的注释只能出现在这些关键字的后面，否则提示无效。
- '+'号表示该注释是一个 HINTS，该加号必须立即跟在 '/\*' 的后面，中间不能有空格。
- HINT 是下面介绍的具体提示之一，如果包含多个提示，则每个提示之间需要用一个或多个空格隔开。
- 如果没有正确的指定 HINTS，将忽略该 HINTS。
- 大小写忽略。

常用 HINT 场景：

| HINT 场景        | 兼容 Oracle 写法            | TDSQL PostgreSQL-O版 写法                |
| --------------- | ------------------------- | ------------------------ |
| 强制走 mergejoin | use_merge(table1, table2) | MergeJoin(table1 table2) |
| 强制走 nestloop  | use_nl(table1, table2)    | NestLoop(table1 table2)  |
| 强制走 hashjoin  | use_hash(table1, table2)  | hashJoin(table1 table2)  |
| 强制走索引      | index(table，index)       | indexscan(table index)   |
| 强制全表扫描    | full(table)               | SeqScan(table)           |

更多介绍请参见 [pg_hint_plan](http://pghintplan.sourceforge.jp/hint_list.html)。

### 示例
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t;
INSERT 0 10000
postgres=# create index hint_t6_f1_idx on hint_t6(f1);
CREATE INDEX
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t;
INSERT 0 10000
postgres=# create index hint_t7_f1_idx on hint_t7(f1);
CREATE INDEX
    
1）强制走 MergeJoin
兼容 Oracle 写法
postgres=# select /*+use_merge(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  f1   |  f2   |  f1   |  f2   
-------+-------+-------+-------
  10000 | 10000 | 10000 | 10000
(1 row)
postgres=# explain select /*+use_merge(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Merge Join  (cost=0.56..163.78 rows=1 width=16)
  Merge Cond: (t.f1 = t1.f1)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..148.87 rows=5039 width=8)
(7 rows)
    
TDSQL PostgreSQL-O版 写法
postgres=# select /*+ MergeJoin(t t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  f1   |  f2   |  f1   |  f2   
-------+-------+-------+-------
  10000 | 10000 | 10000 | 10000
(1 row)
postgres=# explain select /*+ MergeJoin(t t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Merge Join  (cost=0.56..163.78 rows=1 width=16)
  Merge Cond: (t.f1 = t1.f1)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..148.87 rows=5039 width=8)
(7 rows)
    
2）强制走 nestloop
兼容 Oracle 写法：
postgres=# explain select /*+use_nl(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>999 ; 
  QUERY PLAN  
---------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.28..1624.87 rows=4548 width=16)
  ->  Seq Scan on hint_t6 t  (cost=0.00..102.99 rows=4548 width=8)
    Filter: (f1 > 999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..0.32 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
TDSQL PostgreSQL-O版 写法：
postgres=# explain select /*+NestLoop(t t1) */* from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t1.f1>999 ;
  QUERY PLAN 
--------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.28..1624.87 rows=4548 width=16)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..102.99 rows=4548 width=8)
    Filter: (f1 > 999)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..0.32 rows=1 width=8)
    Index Cond: (f1 = t1.f1)
(7 rows)
    
3）强制走 hashjoin
兼容 Oracle 写法：
postgres=# explain select /*+use_hash(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
  QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=2.31..111.61 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=2.30..2.30 rows=1 width=8)
    ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
  Index Cond: (f1 > 9999)
(8 rows)
    
TDSQL PostgreSQL-O版 写法：
postgres=# explain select /*+ hashJoin(t t1) SeqScan(t) SeqScan(t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
-----------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=103.00..212.30 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=102.99..102.99 rows=1 width=8)
    ->  Seq Scan on hint_t6 t  (cost=0.00..102.99 rows=1 width=8)
  Filter: (f1 > 9999)
(8 rows)
    
4）强制走索引
postgres=# create index idx_hint_t6_f1f2 on hint_t6(f1,f2);
CREATE INDEX
postgres=# create index idx_hint_t7_f1 on hint_t7(f1);
CREATE INDEX
postgres=# explain select * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
---------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..6.61 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1 on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
在没有 hint 强制走索引时，执行计划用到索引 idx_hint_t6_f1、idx_hint_t7_f1
    
强制走索引 idx_hint_t6_f1f2
兼容 Oracle 写法：
postgres=# explain select /*+ index(t idx_hint_t6_f1f2) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
----------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..7.48 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
TDSQL PostgreSQL-O版 写法：
postgres=# explain select /*+ indexscan(t idx_hint_t6_f1f2) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
----------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..7.48 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
postgres=# 
    
5）强制全表扫描
postgres=# explain select /*+ index(t idx_hint_t6_f1f2) SeqScan(t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN 
----------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=3.19..112.48 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=3.17..3.17 rows=1 width=8)
    ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
  Index Cond: (f1 > 9999)
(8 rows)
指定 SeqScan(t1) 后，执行计划中 t1 表由索引扫描变为全表扫描
```
   
## SQL PROFILE
Oracle 中的 PROFILE 可以用来对用户所能使用的数据库资源进行限制。
TDSQL PostgreSQL-O版 兼容 PROFILE 用法。 

### 语法
创建 PROFILE：
```
CREATE PROFILE profile
LIMIT { resource_parameters
  | password_parameters
  }
    [ resource_parameters
    | password_parameters
    ]... ;
     
<resource_parameters> 
{ { SESSIONS_PER_USER
  | CPU_PER_SESSION
  | CPU_PER_CALL
  | CONNECT_TIME
  | IDLE_TIME
  | LOGICAL_READS_PER_SESSION
  | LOGICAL_READS_PER_CALL
  | COMPOSITE_LIMIT
  }
  { integer | UNLIMITED | DEFAULT }
| PRIVATE_SGA
  { integer [ K | M ] | UNLIMITED | DEFAULT }
}
     
< password_parameters >
{ { FAILED_LOGIN_ATTEMPTS
  | PASSWORD_LIFE_TIME
  | PASSWORD_REUSE_TIME
  | PASSWORD_REUSE_MAX
  | PASSWORD_LOCK_TIME
  | PASSWORD_GRACE_TIME
  }
  { expr | UNLIMITED | DEFAULT }
| PASSWORD_VERIFY_FUNCTION
  { function | NULL | DEFAULT }
}
```
    
profile 分配给用户：
```
ALTER USER user_name PROFILE profile_name;
```
    
删除 profile：
```
DROP PROFILE profile_name;
```
    
### 示例
```
cpu_per_call limit
postgres=# create profile app_user limit
   sessions_per_user 10
   cpu_per_session 1000
   cpu_per_call 100
   connect_time 100
   logical_reads_per_session 1000
   logical_reads_per_call 1000
   composite_limit 5000000
   Idle_Time 1000
   private_sga 1000
   failed_login_attempts 5 
   password_life_time 1 
   password_reuse_time 2 
   password_reuse_max 5 
   password_lock_time 0.042 
   password_grace_time 0.042;
CREATE PROFILE
postgres=# ALTER RESOURCE COST CPU_PER_SESSION 3 CONNECT_TIME 3 private_sga 2 LOGICAL_READS_PER_SESSION 2; 
ALTER RESOURCE COST
postgres=# create user cpu_call password '123';
CREATE ROLE
postgres=# create profile profile_cpu_call limit cpu_per_call 10;
CREATE PROFILE
postgres=# alter user cpu_call profile profile_cpu_call;
ALTER ROLE
postgres=# \c - cpu_call
You are now connected to database "postgres" as user "cpu_call".
postgres=> create table bb(id int,name varchar(20));
ERROR:  node:dn001, backend_pid:13359, nodename:dn002,backend_pid:20303,message:exceeded call limit on CPU usage
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user cpu_call;
drop profile profile_cpu_call;DROP ROLE
postgres=# drop profile profile_cpu_call;
DROP PROFILE
    
cpu_per_session limit
postgres=# create user cpu_session password '123';
CREATE ROLE
postgres=# create profile profile_cpu_session limit cpu_per_session 10;
CREATE PROFILE
postgres=# alter user cpu_session profile profile_cpu_session;
ALTER ROLE
postgres=# \c - cpu_session
You are now connected to database "postgres" as user "cpu_session".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user cpu_session;
drop profile profile_cpu_session;
FATAL:  node:dn002, backend_pid:21503, nodename:dn001,backend_pid:14480,message:exceeded session limit on CPU usage, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user cpu_session;
DROP ROLE
postgres=# drop profile profile_cpu_session;
DROP PROFILE
postgres=# 
    
logical_reads_per_session limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user blk_session password '123';
alter user blk_session profile profile_blk_session;
CREATE ROLE
postgres=# create profile profile_blk_session limit logical_reads_per_session 10;
\c - blk_session
CREATE PROFILE
postgres=# alter user blk_session profile profile_blk_session;
create table bb(id int,name varchar(20));
ALTER ROLE
postgres=# \c - blk_session
You are now connected to database "postgres" as user "blk_session".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user blk_session;
drop profile profile_blk_session;
FATAL:  node:dn002, backend_pid:25880, nodename:dn001,backend_pid:18543,message:exceeded session limit on IO usage, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user blk_session;
DROP ROLE
postgres=# drop profile profile_blk_session;
DROP PROFILE
postgres=# 
    
logical_reads_per_call limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user blk_call password '123';
alter user blk_call profile profile_blk_call;
CREATE ROLE
postgres=# create profile profile_blk_call limit logical_reads_per_call 10;
CREATE PROFILE
postgres=# alter user blk_call profile profile_blk_call;
\c - blk_call
create table bb(id int,name varchar(20));
ALTER ROLE
postgres=# \c - blk_call
You are now connected to database "postgres" as user "blk_call".
postgres=> create table bb(id int,name varchar(20));
\c - tbase
drop user blk_call;
drop profile profile_blk_call;ERROR:  node:dn001, backend_pid:19447, nodename:dn002,backend_pid:26821,message:exceeded call limit on IO usage
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user blk_call;
DROP ROLE
postgres=# drop profile profile_blk_call;
DROP PROFILE
    
composite_limit limit
postgres=# \c - tbase
create user composite password '123';
create profile profile_composite limit composite_limit 10;
You are now connected to database "postgres" as user "tbase".
postgres=# create user composite password '123';
alter user composite profile profile_composite;
CREATE ROLE
postgres=# create profile profile_composite limit composite_limit 10;
\c - composite
create table bb(id int,name varchar(20));
CREATE PROFILE
postgres=# alter user composite profile profile_composite;
ALTER ROLE
postgres=# \c - composite
\c - tbase
drop user composite;
You are now connected to database "postgres" as user "composite".
postgres=> create table bb(id int,name varchar(20));
drop profile profile_composite;
FATAL:  node:dn002, backend_pid:27700, nodename:dn001,backend_pid:20266,message:exceeded COMPOSITE_LIMIT, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user composite;
DROP ROLE
postgres=# drop profile profile_composite;
DROP PROFILE
    
private_sga limit
postgres=# \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# create user sga password '123';
create profile profile_private_sga limit private_sga 10;
alter user sga profile profile_private_sga;
\c - sga
CREATE ROLE
postgres=# create profile profile_private_sga limit private_sga 10;
create table bb(id int,name varchar(20));
CREATE PROFILE
postgres=# alter user sga profile profile_private_sga;
\c - tbase
drop user sga;
ALTER ROLE
postgres=# \c - sga
You are now connected to database "postgres" as user "sga".
postgres=> create table bb(id int,name varchar(20));
drop profile profile_private_sga;FATAL:  node:dn001, backend_pid:21253, nodename:dn002,backend_pid:28723,message:exceeded private_sga, you are being logged off
server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
The connection to the server was lost. Attempting reset: Succeeded.
postgres=> \c - tbase
You are now connected to database "postgres" as user "tbase".
postgres=# drop user sga;
DROP ROLE
postgres=# drop profile profile_private_sga;
DROP PROFILE
```
    
