序列对象被称为序列生成器或序列，使用 CREATE SEQUENCE 创建的特殊单行表，通常用于为表的行生成唯一标识符。
序列是非事务的，setval 造成的改变不会因事务的回滚而撤销。
常用的序列函数如下：

| **函数**                                    | **返回值** | **描述**                                  |
| ------------------------------------------- | ---------- | ----------------------------------------- |
| currval(regclass)                         | bigint     | 返回最近一次用 nextval 获取的指定序列的值 |
| lastval()                                   | bigint     | 返回最近一次用 nextval 获取的任何序列的值 |
| nextval(regclass)                         | bigint     | 递增序列并返回新值                        |
| setval(regclass,   bigint)              | bigint     | 设置序列的当前值                          |
| setval(regclass,   bigint,   boolean) | bigint     | 设置序列的当前值以及 is_called 标志       |

示例：
```
postgres=# CREATE SEQUENCE seq;
CREATE SEQUENCE
postgres=# SELECT nextval('seq');
 nextval 
---------
    1
(1 row)
 
postgres=# SELECT nextval('seq');
 nextval 
---------
    2
(1 row)
 
postgres=# SELECT currval('seq');
 currval 
---------
    2
(1 row)
 
postgres=# SELECT setval('seq',188);
 setval 
--------
  188
(1 row)
 
postgres=# SELECT currval('seq');
 currval 
---------
   188
(1 row)
 
postgres=# SELECT lastval();
 lastval 
---------
   188
(1 row)
```
