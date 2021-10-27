本节主要介绍 DML 语句中常用的Select（查询）、Insert（插入）、Replace（替换）、Update（更新）及Delete（删除）指令。
### **SELECT指令**
执行Select指令时，建议在条件中增加Shardkey字段，语句如下。
>?Proxy根据该字段的Hash值，将SQL指令请求路由至对应的数据库实例进行处理；否则SQL指令将发送到集群所有的数据库实例，Proxy再进行数据库返回的结果集进行聚合，将影响执行效率。

```
MySQL [test]> create table test1(a int not null primary key,b int,c char(10)) shardkey=a;
Query OK, 0 rows affected (2.64 sec)

MySQL [test]> insert into test1(a,b,c) values(2,3,'record2');
Query OK, 1 row affected (0.04 sec)

MySQL [test]> insert into test1(a,b,c) values(3,4,'record3');
Query OK, 1 row affected (0.03 sec)

MySQL [test]> select b,c from test1 where a=3;
+------+---------+
| b    | c       |
+------+---------+
|    4 | record3 |
+------+---------+
1 row in set (0.00 sec)

```
### INSERT/REPLACE指令
执行Insert/Replace命令时，字段必须包含Shardkey，否则系统会拒绝执行SQL命令，因为Proxy无法判断SQL语句发送的后端数据库节点位置。语句显示如下：

```
MySQL [test]> insert into test1 (b,c) values(10,"record3");
ERROR 683 (HY000): Proxy ERROR: Get shardkeys return error: insert/replace must contain shardkey column

MySQL [test]> insert into test1 (a,c) values(40,"records5");
Query OK, 1 row affected (0.03 sec)


MySQL [test]> truncate table test1;
Query OK, 0 rows affected (2.18 sec)

--重新插入数据后：
MySQL [test]> select a,b,c from test1;
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 3 |    4 | record3 |
| 2 |    3 | record2 |
+---+------+---------+
2 rows in set (0.03 sec)

MySQL [test]> replace into test1 (b,c) values(10,"record3");
ERROR 683 (HY000): Proxy ERROR: Get shardkeys return error: insert/replace must contain shardkey column

MySQL [test]> replace into test1(a,b,c) values(3,40,"record1");
Query OK, 2 rows affected (0.03 sec)

MySQL [test]> select a,b,c from test1;
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 3 |   40 | record1 |
| 2 |    3 | record2 |
+---+------+---------+
2 rows in set (0.00 sec)

```
### **DELETE/UPDATE指令**
执行Delete/Update命令时，为了安全考虑，分表和广播表执行该 SQL指令的时候必须带“ where ”条件，否则系统拒绝执行该SQL命令。语句如下：

```
MySQL [test]> delete from test1;
ERROR 658 (HY000): Proxy ERROR: Join internal error: delete query has no where clause

MySQL [test]> delete from test1 where a=2;
Query OK, 1 row affected (0.01 sec)

```
【建议】：为了防止用户误操作，建议尽量不要使用全表的Update/Delete指令；如必须使用该指令，可在SQL语句中增加where 1条件：

```
MySQL [test]> delete from test1 where 1;
Query OK, 1 row affected (0.01 sec)

MySQL [test]> select * from test1;
Empty set (0.01 sec)

```
