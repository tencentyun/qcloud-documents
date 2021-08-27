Oracle 中 MERGE INTO 语句是将 INSERT 和 UPDATE 语句结合，同时实现 INSERT 和 UPDATE，与表匹配的行进行更新，不匹配的行写入表中。

TDSQL PostgreSQL版（Oracle 兼容）兼容 MERGE INTO 语法。

## 语法
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
    
## 示例
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
