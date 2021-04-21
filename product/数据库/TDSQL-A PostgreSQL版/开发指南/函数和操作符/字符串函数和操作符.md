TDSQL-A PostgreSQL版 支持类型多样、功能丰富的字符串函数和操作符，在此列举部分常用的字符串操作符和函数，更多详细信息可参考 [官网](http://www.postgres.cn/docs/10/functions-string.html)。

| **操作符/函数**                                              | **返回类型** | **描述**                                                     |
| ----------------------------------------- | ------------ | ------------------------------------------ |
| string \|\| string                                           | text         | 串接                                                         |
| char_length(string) or  character_length(string)        | int          | 串中字符数                                                   |
| lower(string)                                              | text         | 将字符串转换为小写形式                                       |
| overlay(string   placing   stringfrom int   [for int]) | text         | 替换子串                           |
| position(substring   in string)                          | int          | 定位指定子串                                                 |
| substring(  string [from int] [for int])               | text         | 提取子串                                                     |
| trim(  [leading \| trailing \| both]   [characters]  fromstring) | text         | 从 string 的开头、结尾、两端（默认是 both） 删除最长的只包含来自 characters 字符（默认是一个空格）的串 |
| upper(string)                                              | text         | 将字符串转换成大写形式                                       |
| ascii(string)                                              | int          | 参数第一个字符的 ASCII 代码。对于 UTF8 返回该字符的Unicode 代码点。对于其他多字节编码，该参数必须是一个 ASCII 字符 |
| btrim(string text   [, characterstext])                | text         | 从 string 的开头或结尾删除最长的只包含 characters（默认是一个空格）的串 |
| concat(str "any"   [, str "any"   [, ...] ])         | text         | 串接所有参数的文本表示。NULL 参数被忽略               |
| decode(string text,  format text)                    | bytea        | 从 string 中的文本表达解码二进制数据。format 的选项和 encode 中的一样 |
| left(str text,  n int)                               | text         | 返回字符串中的前 n 个字符。当 n 为负时，将返回除了最后\|n\|个字符之外的所有字符 |
| length(string)                                             | int          | string 中的字符数                                           |
| lpad(string text,  length int   [, fill text])   | text         | 将 string 通过前置字符 fill（默认是一个空格）填充到长度 length。如果 string 已经长于 length，则它被（从右边）截断 |
| ltrim(string text   [, characterstext])                | text         | 从 string 的开头删除最长的只包含 characters（默认是一个空格）的串 |
| repeat(string text,  number int)                     | text         | 重复 string 指定的 number 次                    |

示例：
```
postgres=# SELECT 'T'||'dapg';
 ?column? 
----------
 Tdapg
(1 row)
 
postgres=# SELECT char_length('jose');
 char_length 
-------------
      4
(1 row)
 
postgres=# SELECT overlay('Txxxxas' placing 'hom' from 2 for 4);
 overlay 
---------
 Thomas
(1 row)
 
postgres=# SELECT position('om' in 'Thomas');
 position 
----------
    3
(1 row)
 
postgres=# SELECT substring('Thomas' from 2 for 3);
 substring 
-----------
 hom
(1 row)
 
postgres=# SELECT trim(both from 'yxTomxx', 'xyz');
 btrim 
-------
 Tom
(1 row)
 
postgres=# SELECT ascii('x');
 ascii 
-------
  120
(1 row)
 
postgres=# SELECT btrim('xyxtrimyyx', 'xyz');
 btrim 
-------
 trim
(1 row)
 
postgres=# SELECT concat('abcde', 2, NULL, 22);
 concat 
----------
 abcde222
(1 row)
```

