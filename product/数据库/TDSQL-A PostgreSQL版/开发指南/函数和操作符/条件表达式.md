## CASE
CASE 表达式是一种通用的条件表达式，类似其他编程语言中的 if…else 语句，语法格式如下：
```
CASE WHEN condition THEN result
   [WHEN ...]
   [ELSE result]
END
```
或者：
```
CASE expression
  WHEN value THEN result
  [WHEN ...]
  [ELSE result]
END
```

示例：
```
postgres=# CREATE TABLE test(a INT); 
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO test VALUES(1),(2),(3);
COPY 3
postgres=# SELECT * FROM test;
a 
---
 1
 3
 2
(3 rows)
 
postgres=# SELECT a,
postgres-#    CASE WHEN a=1 THEN 'one'
postgres-#       WHEN a=2 THEN 'two'
postgres-#       ELSE 'other'
postgres-#    END
postgres-#   FROM test;
 a | case 
---+-------
 1 | one
 3 | other
 2 | two
(3 rows) 

postgres=# SELECT a,
postgres-#    CASE a WHEN 1 THEN 'one'
postgres-#        WHEN 2 THEN 'two'
postgres-#        ELSE 'other'
postgres-#    END
postgres-#   FROM test;
 a | case 
---+-------
 1 | one
 3 | other
 2 | two
(3 rows)
```

## COALESCE
COALESCE 函数返回它的第一个非空参数的值，仅当所有参数都为空时才返回空。它通常用于为显示目的检索数据时用缺省值替换空值。
语法格式如下：
```
COALESCE(value [, ...])
```

示例：
```
postgres=# SELECT COALESCE(null,'a',null,'hello');
 coalesce 
----------
 a
(1 row)
```

## NULLIF
NULLIF 语法格式如下：
```
NULLIF(value1, value2)
```
当 value1 和 value2 相等时，NULLIF 返回一个空值，否则返回 value1。
示例：
```
postgres=# SELECT NULLIF('hello','hello');
 nullif 
--------
(1 row)
 
postgres=# SELECT NULLIF(null,'hello');
 nullif 
--------
(1 row)

postgres=# SELECT NULLIF('hello',null);
 nullif 
--------
 hello
(1 row)
```

## GREATEST 和 LEAST
GREATEST 和 LEAST 函数从一个任意的数字表达式列表中选取最大或最小的数值，语法格式如下：
```
GREATEST(value [, ...])
LEAST(value [, ...])
```
示例：
```
postgres=# SELECT GREATEST(1,2,3,4,5);
 greatest 
----------
    5
(1 row)
 
postgres=# SELECT LEAST(1,2,3,4,5);
 least 
-------
   1
(1 row)
```
