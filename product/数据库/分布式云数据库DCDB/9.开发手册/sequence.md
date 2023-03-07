关键字 Sequence 语法和 MariaDB/Oracle 兼容，但是保证分布式全局递增且唯一，具体使用如下：

>?
>- 在 TDSQL MySQL版 分布式数据库当中使用 Sequence 时，须在该关键字前面加 `tdsql_` 前缀，且要求 proxy 版本最低为1.19.5-M-V2.0R745D005；可通过数据库管理语句 `/*Proxy*/show status` 查询 proxy 版本，若 proxy 版本较老可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行升级。
>- 目前 Sequence 为保证分布式全局数值唯一，导致性能较差，主要适用于并发不高的场景。

创建序列需要 CREATE SEQUENCE 系统权限。序列的创建语法如下：
```
　　CREATE TDSQL_SEQUENCE 序列名
　　[START WITH n]
　　[{TDSQL_MINALUE/ TDSQL_MAXMINVALUE n| TDSQL_NOMAXVALUE}]
　　[TDSQL_INCREMENT BY n]
　　[{TDSQL_CYCLE|TDSQL_NOCYCLE}]
```

## 创建 Sequence
```
create tdsql_sequence test.s1 start with 12 tdsql_minvalue 10 maxvalue 50000 tdsql_increment by 5 tdsql_nocycle
create tdsql_sequence test.s2 start with 12 tdsql_minvalue 10 maxvalue 50000 tdsql_increment by 1 tdsql_cycle
```
- 以上SQL语句包含开始值、最小值、最大值、步长、缓存大小及是否回绕6个参数，参数都应为正整数。
- 参数默认值，开始值（1）、最小值（1）、最大值（LONGLONG_MAX-1）、步长（1）、是否回绕（0）。

## 删除 Sequence
```
drop tdsql_sequence test.s1
```

## 查询 Sequence
```
show tdsql_sequence
```

## 使用 Sequence
#### 使用 Sequence 获取下一个数值
```
select tdsql_nextval(test.s2)
select next value for test.s2
```

```
mysql> select tdsql_nextval(test.s1);
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.18 sec)

mysql> select tdsql_nextval(test.s2);
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.13 sec)

mysql> select tdsql_nextval(test.s1);
+----+
| 17 |
+----+
| 17 |
+----+
1 row in set (0.01 sec)

mysql> select tdsql_nextval(test.s2);
+----+
| 13 |
+----+
| 13 |
+----+
1 row in set (0.00 sec)

mysql> select next value for test.s1;
+----+
| 22 |
+----+
| 22 |
+----+
1 row in set (0.01 sec)
```

#### nextval 可以用在 insert 等地方
```
mysql> select * from test.t1;
+----+------+
| a  | b    |
+----+------+
| 11 |    2 |
+----+------+
1 row in set (0.00 sec)

mysql> insert into test.t1(a,b) values(tdsql_nextval(test.s2),3);
Query OK, 1 row affected (0.01 sec)

mysql> select * from test.t1;
+----+------+
| a  | b    |
+----+------+
| 11 |    2 |
| 14 |    3 |
+----+------+
2 rows in set (0.00 sec)
```

如需获取上一次的值以连接相关数据：如果之前没有用 nextval 命令获取过数据，数值将返回为0。
```
select tdsql_lastval(test.s1)
select tdsql_previous value for test.s1;
```

```
mysql> select tdsql_lastval(test.s1);
+----+
| 22 |
+----+
| 22 |
+----+
1 row in set (0.00 sec)

mysql> select tdsql_previous value for test.s1;
+----+
| 22 |
+----+
| 22 |
+----+
1 row in set (0.00 sec)
```

设置下一个序列数值，只能比当前数值大，否则将返回数值为0。
```
select tdsql_setval(test.s2,1000,bool use)  //  use 默认为1，表示1000这个值用过了，下一次不包含1000，如果为0，则下一个从1000开始。
```

设置下一个序列数值时，如果比当前数值小，则系统将没有反应。
```
mysql> select tdsql_nextval(test.s2);
+----+
| 15 |
+----+
| 15 |
+----+
1 row in set (0.01 sec)

mysql> select tdsql_setval(test.s2,10);
+---+
| 0 |
+---+
| 0 |
+---+
1 row in set (0.03 sec)

mysql> select tdsql_nextval(test.s2);
+----+
| 16 |
+----+
| 16 |
+----+
```

如果比当前数值大，成功返回当前设置的值。
```
mysql> select tdsql_setval(test.s2,20);
+----+
| 20 |
+----+
| 20 |
+----+
1 row in set (0.02 sec)
mysql> select tdsql_nextval(test.s2);
+----+
| 21 |
+----+
| 21 |
+----+
1 row in set (0.01 sec)
```

强制设置下一个序列数值，允许设置比当前数值小的值。
```
select tdsql_resetval(test.s2,1000)
```

如果强制设置成功，返回当前设置的值，下一个序列数值从该值开始。
```
mysql> select tdsql_resetval(test.s2,14);
+----+
| 14 |
+----+
| 14 |
+----+
1 row in set (0.00 sec)

mysql> select tdsql_nextval(test.s2);
+----+
| 14 |
+----+
| 14 |
+----+
1 row in set (0.01 sec)
```

需要注意，Sequence 的部分关键字以 `TDSQL_` 前缀开始：
>?若已打开 oldstyle 配置项，proxy 将兼容标准 Sequence 关键字，即关键字前可不添加`TDSQL_` 前缀。
>
```
 TDSQL_CYCLE
 TDSQL_INCREMENT
 TDSQL_LASTVAL  
 TDSQL_MINVALUE 
 TDSQL_NEXTVAL  
 TDSQL_NOCACHE  
 TDSQL_NOCYCLE  
 TDSQL_NOMAXVALUE
 TDSQL_NOMINVALUE
 TDSQL_PREVIOUS 
 TDSQL_RESTART  
 TDSQL_REUSE    
 TDSQL_SEQUENCE 
 TDSQL_SETVAL   
```

