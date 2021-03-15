终止当前事务。

## 概要
```sql
ABORT [WORK | TRANSACTION]
```

## 描述
ABORT 当前事务并导致事务所做的所有更新都被丢弃。出于历史原因，此命令与标准 SQL 命令的行为相同。

## 参数
WORK
TRANSACTION
可选关键字，它们没有效果。

## 注解
使用 COMMIT 成功终止一个事务。

在一个事务块之外发出 ABORT 会发出一个警告信息并且不会产生效果。

## 示例

```sql
--创建表 table1。
 
CREATE TABLE table1
(
    a1                      INTEGER               NOT NULL,
    b1                             CHAR(10)                      ,
    c1                           INTEGER                       
)
WITH (
        APPENDONLY = TRUE,
    ORIENTATION = COLUMN,
    COMPRESSTYPE = ZLIB
)
DISTRIBUTED BY (a1);
 
--插入记录。
INSERT INTO table1 VALUES(20190117,'test', 11);
 
--查询数据。
select * from table1;
    a1    |     b1     | c1 
----------+------------+----
 20190117 | test       | 11
(1 row)
 
Time: 16.718 ms
 
--开启事务，等价于 START TRANSACTION。
BEGIN;
 
--更新字段值。
 
UPDATE table1 SET b1= 'yes';
UPDATE 1
Time: 13.510 ms
 
--查询数据，本事务中可以看到数据已经被更新。
select * from table1;
    a1    |     b1     | c1 
----------+------------+----
 20190117 | yes        | 11
(1 row)
 
Time: 6.378 ms
 
--终止事务，上面所执行的更新会被撤销掉，等价于 ROLLBACK。
ABORT; 
ROLLBACK
Time: 0.651 ms
 
--查询数据，数据被回滚。
select * from table1;
    a1    |     b1     | c1 
----------+------------+----
 20190117 | test       | 11
(1 row)
 
Time: 6.124 ms
```

## 兼容性
由于历史原因，此命令是数据库扩展名。ROLLBACK 是等效的标准 SQL 命令。ROLLBACK 是等效的标准 SQL 命令。

## 另见
BEGIN、COMMIT、ROLLBACK
