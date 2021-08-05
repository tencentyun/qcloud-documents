UPDATE 更新表时，支持字段名前加表名，或表别名的写法。

## 语法
```
UPDATE table_name [ [ as ] table_alias ] 
SET [{ table_name | table_alias }.]column_name = { value | expr | column_name } [, ... ] 
[ WHERE expr ];
```
    
## 示例
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
    
