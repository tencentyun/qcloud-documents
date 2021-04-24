## 数组操作符
TDSQL-A PostgreSQL版 支持如下用于数组类型的操作符：

| **操作符** | **描述**       | **示例**                                 | **结果**                  |
| ---------- | -------------- | ---------------------------------------- | ------------------------- |
| =          | 等于           | ARRAY[1.1,2.1,3.1]::int[] = ARRAY[1,2,3] | t                         |
| <>         | 不等于         | ARRAY[1,2,3] <> ARRAY[1,2,4]             | t                         |
| <          | 小于           | ARRAY[1,2,3] < ARRAY[1,2,4]              | t                         |
| >          | 大于           | ARRAY[1,4,3] > ARRAY[1,2,4]              | t                         |
| <=         | 小于等于       | ARRAY[1,2,3] <= ARRAY[1,2,3]             | t                         |
| >=         | 大于等于       | ARRAY[1,4,3]>=ARRAY[1,4,3]               | t                         |
| @>         | 包含           | ARRAY[1,4,3] @> ARRAY[3,1]               | t                         |
| <@         | 被包含         | ARRAY[2,7] <@ ARRAY[1,7,4,2,6]           | t                         |
| &&         | 重叠           | ARRAY[1,4,3] && ARRAY[2,1]               | t                         |
| \|\|       | 数组和数组串接 | ARRAY[1,2,3] \|\| ARRAY[4,5,6]           | {1,2,3,4,5,6}             |
| \|\|       | 数组和数组串接 | ARRAY[1,2,3]\|\|ARRAY[[4,5,6],[7,8,9]]   | {{1,2,3},{4,5,6},{7,8,9}} |
| \|\|       | 元素到数组串接 | 3 \|\| ARRAY[4,5,6]                      | {3,4,5,6}                 |
| \|\|       | 数组到元素串接 | ARRAY[4,5,6] \|\| 7                      | {4,5,6,7}                 |


## 数组函数
| **函数**                        | **返回类型** | **描述**                                                     |
| --------------------------- | ------------ | -------------------------------------- |
| array_append(anyarray,  anyelement)                 | anyarray     | 向一个数组的末端追加一个元素                                 |
| array_cat(anyarray,  anyarray)                      | anyarray     | 连接两个数组                                                 |
| array_ndims(anyarray)                               | int          | 返回数组的维度数                                             |
| array_length(anyarray,  int)                        | int          | 返回被请求的数组维度的长度                                   |
| array_lower(anyarray,  int)                         | int          | 返回被请求的数组维度的下界                                   |
| array_position(anyarray,  anyelement [, int])       | int          | 返回数组中第二个参数第一次出现的下标。 起始于第三个参数或第一个元素指示的元素位置（数组必须是一维的) |
| array_prepend(anyelement,  anyarray)                | anyarray     | 向一个数组的首部追加一个元素                 |
| array_remove(anyarray,  anyelement)                 | anyarray     | 从数组中移除所有等于给定值的所有元素（数组必须是一维的）     |
| array_replace(anyarray,   anyelement,   anyelement) | anyarray  | 将每一个等于给定值的数组元素替换成一个新值      |
| array_to_string(  anyarray,   text [, text])        | text         | 使用提供的定界符和可选的空串连接数组元素                     |
| array_upper(anyarray,  int)                   | int          | 返回被请求的数组维度的上界                                   |
| string_to_array(text,   text [, text])         | text[]       | 使用提供的定界符和可选的空串将字符串划分成数组元素           |

示例：
```
postgres=# SELECT array_append(ARRAY[1,2], 3);
 array_append 
--------------
 {1,2,3}
(1 row) 

postgres=# SELECT array_cat(ARRAY[1,2,3], ARRAY[4,5]);
 array_cat 
-------------
 {1,2,3,4,5}
(1 row) 

postgres=# SELECT array_ndims(ARRAY[[1,2,3], [4,5,6]]);
 array_ndims 
-------------
      2
(1 row) 

postgres=# SELECT array_length(array[1,2,3], 1);
 array_length 
--------------
      3
(1 row) 

postgres=# SELECT array_lower('[0:2]={1,2,3}'::int[], 1);
 array_lower 
-------------
      0
(1 row) 

postgres=# SELECT array_position(ARRAY['sun','mon','tue','wed','thu','fri','sat'], 'mon');
 array_position 
----------------
       2
(1 row) 

postgres=# SELECT array_prepend(1, ARRAY[2,3]);
 array_prepend 
---------------
 {1,2,3}
(1 row)
 
postgres=# SELECT array_remove(ARRAY[1,2,3,2], 2);
 array_remove 
--------------
 {1,3}
(1 row) 

postgres=# SELECT array_replace(ARRAY[1,2,5,4], 5, 3);
 array_replace 
---------------
 {1,2,3,4}
(1 row)

postgres=# SELECT array_to_string(ARRAY[1, 2, 3, NULL, 5], ',', '*');
 array_to_string 
-----------------
 1,2,3,*,5
(1 row) 

postgres=# SELECT array_upper(ARRAY[1,8,3,7], 1);
 array_upper 
-------------
      4
(1 row)

postgres=# SELECT string_to_array('xx~^~yy~^~zz', '~^~', 'yy');
 string_to_array 
-----------------
 {xx,NULL,zz}
(1 row)
```
以上是一些比较常用的数组函数，更多说明请参考 [官网](http://www.postgres.cn/docs/10/functions-array.html)。
