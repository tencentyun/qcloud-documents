
关键字 sequence 语法和 mariadb/Oracle 兼容，但是保证分布式全局递增且唯一，具体使用如下：

创建序列需要 CREATE SEQUENCE 系统权限。序列的创建语法如下：
```
　　CREATE SEQUENCE 序列名
　　[INCREMENT BY n]
　　[START WITH n]
　　[{MAXVALUE/ MINVALUE n| NOMAXVALUE}]
　　[{CYCLE|NOCYCLE}]
　　[{CACHE n| NOCACHE}];
```

>?目前 sequence 为保证分布式全局唯一，性能较差，适用于并发不高的场景。

## 创建
示例如下：
```
create sequence test.s1 start with 12 minvalue 10 maxvalue 50000  increment by 5  nocycle 
create sequence test.s2 start with 12 minvalue 10 maxvalue 50000  increment by 1  cycle 
```
参数有开始值，最小值，最大值，步长，是否回绕。

## 删除
示例如下：
```
drop sequence test.s1
```
当前限制条件：参数都为正整数。

## 查看
示例如下：
```
show create sequence test.s1
```

## 使用
#### 操作表的序列
```
select nextval(test.s1)
select next value for test.s1
```

示例：
```
mysql> select nextval(test.s1);
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.18 sec)

mysql> select nextval(test.s2);
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.13 sec)

mysql> select nextval(test.s1);
+----+
| 17 |
+----+
| 17 |
+----+
1 row in set (0.01 sec)

mysql> select nextval(test.s2);
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

nextval 可以用在 insert 等地方：
```
mysql> select * from test.t1;
+----+------+
| a  | b    |
+----+------+
| 11 |    2 |
+----+------+
1 row in set (0.00 sec)

mysql> insert into test.t1(a,b) values(nextval(test.s2),3);
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

#### 获取上次的值
如果之前没有用 nextval 获取过，则返回0：
```
select lastval(test.s1)
select previous value for test.s1;
```

示例：
```
mysql> select lastval(test.s1);
+----+
| 22 |
+----+
| 22 |
+----+
1 row in set (0.00 sec)

mysql> select previous value for test.s1;
+----+
| 22 |
+----+
| 22 |
+----+
1 row in set (0.00 sec)
```

#### 设置下一个值
只能变大，否则返回0：
```
select setval(test.s2,1000,bool use)  //  use 默认为1，表示1000这个值用过了，下一次不包含1000，如果为0，则下一个从1000开始
```

变小没反应：
```
mysql> select nextval(test.s2);
+----+
| 15 |
+----+
| 15 |
+----+
1 row in set (0.01 sec)

mysql> select setval(test.s2,10);
+---+
| 0 |
+---+
| 0 |
+---+
1 row in set (0.03 sec)

mysql> select nextval(test.s2);
+----+
| 16 |
+----+
| 16 |
+----+
```

变大，成功返回当前设置的值：
```
mysql> select setval(test.s2,20);
+----+
| 20 |
+----+
| 20 |
+----+
1 row in set (0.02 sec)
mysql> select nextval(test.s2);
+----+
| 21 |
+----+
| 21 |
+----+
1 row in set (0.01 sec)
```


需要注意，sequence 的部分关键字以 TDSQL_ 前缀开始：
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
