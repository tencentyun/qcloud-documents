
通常标准的 SQL 语法在 DELETE 时需要带 FROM 关键字，如 `DELETE FROM table WHERE expr`，Oracle 中可以省略 FROM 关键字。

TDSQL PostgreSQL版（Oracle 兼容）兼容 DELETE 时省略 FROM 关键字用法。

## 语法
```
DELETE [ FROM] table_name [ WHERE expr ];
```
    
## 示例
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
 
