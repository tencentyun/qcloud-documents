格式化函数用于把各种数据类型（日期/时间、整数、浮点、数字）转换成格式化的字符串，以及反过来从格式化的字符串转换成指定的数据类型。
下表列出了这些函数。这些函数都遵循一个公共的调用习惯：第一个参数是待格式化的值，而第二个是一个定义输出或输入格式的模版。

| **函数**                        | **返回类型**              | **描述**                 |
| ------------------------------- | ------------------------- | ------------------------ |
| to_char(timestamp,text)         | text                      | 把时间戳转成字符串       |
| to_char(interval,text)          | text                      | 把间隔转成字符串         |
| to_char(int,text)               | text                      | 把整数转成字符串         |
| to_char(double  precision,text) | text                      | 把实数或双精度转成字符串 |
| to_char(numeric,text)           | text                      | 把数字转成字符串         |
| to_date(text,text)              | date                      | 把字符串转成日期         |
| to_number(text,text)            | numeric                   | 把字符串转成数字         |
| to_timestamp(text,text)         | timestamp  with time zone | 把字符串转成时间戳       |

示例：
```
postgres=# SELECT to_char(interval '15h 2m 12s', 'HH24:MI:SS');
 to_char 
----------
 15:02:12
(1 row)
 
postgres=# SELECT to_char(125, '999');
 to_char 
---------
 125
(1 row)
 
postgres=# SELECT to_char(125.8::real, '999D9');
 to_char 
---------
 125.8
(1 row)
 
postgres=# SELECT to_char(-125.8, '999D99S');
 to_char 
---------
 125.80-
(1 row)
 
postgres=# SELECT to_date('05 Dec 2000', 'DD Mon YYYY');
 to_date 
------------
 2000-12-05
(1 row)
```
