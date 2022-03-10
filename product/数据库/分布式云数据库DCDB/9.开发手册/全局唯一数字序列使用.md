关键字`auto_increment`，即支持一个全局的自增字段，auto_increment 可以保证该表某个字段全局唯一，但不保证单调递增，具体使用方法如下：

## 创建
```
mysql> create table auto_inc (a int,b int,c int auto_increment,d int,key auto(c),primary key p(a,d)) shardkey=d;
Query OK, 0 rows affected (0.12 sec)
```

## 插入
```
mysql>  insert into shard.auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,4,0);
Query OK, 2 rows affected (0.05 sec)
Records: 2  Duplicates: 0  Warnings: 0
	
mysql> select * from shard.auto_inc;
+---+------+---+---+
| a | b    | c | d |
+---+------+---+---+
| 1 |    2 | 2 | 4 |
| 1 |    2 | 1 | 3 |
+---+------+---+---+
2 rows in set (0.03 sec)
```

如果发生切换、重启等过程，自增长字段中间会有空洞，例如：
```
mysql> insert into shard.auto_inc ( a,b,d,c) values(11,12,13,0),(21,22,23,0);
Query OK, 2 rows affected (0.03 sec)
mysql> select * from shard.auto_inc;
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| a | b | c | d |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| 21 | 22 | 2002 | 23 |
| 1 | 2 | 2 | 4 |
| 1 | 2 | 1 | 3 |
| 11 | 12 | 2001 | 13 |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
4 rows in set (0.01 sec)
```

更改当前值：
```
alter table auto_inc auto_increment=100
```

通过`select last_insert_id()`获取最近一个自增值：
```	
mysql> insert into auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,4,0);
Query OK, 2 rows affected (0.73 sec)
		
mysql> select * from auto_inc;
+---+------+------+---+
| a | b    | c    | d |
+---+------+------+---+
| 1 |    2 | 4001 | 3 |
| 1 |    2 | 4002 | 4 |
+---+------+------+---+
2 rows in set (0.00 sec)
	
mysql> select last_insert_id();
+------------------+
| last_insert_id() |
+------------------+
| 4001             |
+------------------+
1 row in set (0.00 sec)
```

目前 select last_insert_id() 只能跟 shard 表和广播表的自增字段一起使用，不支持 noshard 表。
