## EXISTS
EXISTS 语法格式如下：
```
EXISTS (subquery)
```
它的参数是一个任意的 SELECT 语句或者子查询。系统对子查询进行运算以判断它是否返回行。
- 如果它至少返回一行，那么 EXISTS 的结果为真。
- 如果子查询没有返回行，那么它的结果是假。

示例：
```
postgres=# SELECT EXISTS(SELECT 1<0);
 exists 
--------
 t
(1 row)
 
postgres=# SELECT EXISTS(SELECT 1 where 1<0);
 exists 
--------
 f
(1 row)
```

## IN
IN 的语法格式为：
```
expression IN (subquery)
```
右手边是一个圆括弧括起来的子查询，它必须正好只返回一个列。左手边表达式将被计算并与子查询结果逐行进行比较。 
- 如果找到任何等于子查询行的情况，那么 IN 的结果就是“真”。
- 如果没有找到相等行，那么结果是“假”（包括子查询没有返回任何行的情况）。

示例：
```
postgres=# SELECT (1>0) IN('true','false');
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT (2+3) IN(3,4);
 ?column? 
----------
 f
(1 row)
```

## NOT IN
NOT IN 的语法格式如下：
```
expression NOT IN (subquery)
```
右手边是一个用圆括弧包围的子查询，它必须返回正好一个列。左手边表达式将被计算并与子查询结果逐行进行比较。 
- 如果只找到不相等的子查询行（包括子查询不返回行的情况），那么 NOT IN 的结果是“真”。
- 如果找到任何相等行，则结果为“假”。

示例：
```
postgres=# SELECT (1>0) NOT IN('true','false');
 ?column? 
----------
 f
(1 row)

postgres=# SELECT (2+3) NOT IN(3,4);
 ?column? 
----------
 t
(1 row)
```

## ANY/SOME
语法格式如下：
```
expression operator ANY (subquery)
expression operator SOME (subquery)
```
这种形式的右手边是一个圆括弧括起来的子查询，它必须返回正好一个列。左手边表达式将被计算并使用给出的操作符对子查询结果逐行进行比较。
- 如果获得任何真值结果，那么 ANY 的结果就是“真”。
- 如果没有找到真值结果，那么结果是“假”（包括子查询没有返回任何行的情况）。
SOME 是 ANY的同义词。IN 等价于 = ANY。

示例：
```
postgres=# CREATE TABLE any_test(a int);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO any_test VALUES(1),(2),(3),(4),(5);
COPY 5
postgres=# SELECT * FROM any_test where a < ANY(SELECT AVG(a) FROM any_test);
 a 
---
 1
 2
(2 rows)
```

## ALL
ALL 的语法格式如下：
```
expression operator ALL (subquery)
```
ALL 这种形式的右手边是一个圆括弧括起来的子查询，它必须只返回一列。左手边表达式将被计算并使用给出的操作符对子查询结果逐行进行比较。该操作符必须生成布尔结果。
- 如果所有行得到真（包括子查询没有返回任何行的情况），ALL的结果就是“真”。
- 如果没有存在任何假值结果，那么结果是“假”。
- 如果比较为任何行都不返回假并且对至少一行返回 NULL，则结果为 NULL。
NOT IN 等价于 <> ALL。

示例：
```
postgres=# CREATE TABLE all_test(a INT);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO all_test VALUES(1),(2),(3),(4),(5);
COPY 5
postgres=# SELECT * FROM all_test WHERE a < ALL(SELECT * FROM all_test);
 a 
---
(0 rows)

postgres=# SELECT * FROM all_test WHERE 6 > ALL(SELECT * FROM all_test) order by 1;
 a 
---
 1
 2
 3
 4
 5
(5 rows)
```
