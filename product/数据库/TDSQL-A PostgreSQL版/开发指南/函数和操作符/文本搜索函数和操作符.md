##  文本搜索操作符
| **操作符** | **返回类型** | **描述**                      |
| ---------- | ------------ | ----------------------------- |
| @@         | bool         | tsvector 是否匹配 tsquery |
| @@@        | bool         | 同 @@                          |
| \|\|       | tsvector     | 连接 tsvector                |
| &&         | tsquery      | 将 tsvector 用 AND 连接起来    |
| \|\|       | tsquery      | 将 tsquery 用 OR 连接起来     |
| !!         | tsquery      | 对一个 tsquery 取反           |
| <->        | tsquery      | tsquery 后面跟着 tsquery    |
| @>         | bool         | tsquery 包含另一个 tsquery    |
| <@         | bool         | tsquery 是否被包含         |

示例：
```
postgres=# SELECT to_tsvector('fat cats ate rats') @@ to_tsquery('cat & rat');
 ?column? 
----------
 f
(1 row)
 
postgres=# SELECT 'a:1 b:2'::tsvector || 'c:1 d:2 b:3'::tsvector;
     ?column?     
---------------------------
 'a':1 'b':2,5 'c':3 'd':4
(1 row)
 
postgres=# SELECT 'fat | rat'::tsquery && 'cat'::tsquery;
     ?column?     
---------------------------
 ( 'fat' | 'rat' ) & 'cat'
(1 row)
 
postgres=# SELECT !! 'cat'::tsquery;
 ?column? 
----------
 !'cat'
(1 row)
 
postgres=# SELECT to_tsquery('fat') <-> to_tsquery('rat');
  ?column?  
-----------------
 'fat' <-> 'rat'
(1 row)
 
postgres=# SELECT 'cat'::tsquery @> 'cat & rat'::tsquery;
 ?column? 
----------
 f
(1 row)
```

## 文本搜索函数
| **函数**                                                     | **返回类型** | **描述**                                    |
| -------------------------------------------------- | ------------ | ------------------------------------ |
| array_to_tsvector(text[])                                  | tsvector     | 把词位数组转换成 tsvector                  |
| get_current_ts_config()                                      | regconfig    | 获得默认文本搜索配置                        |
| length(tsvector)                                           | integer      | tsvector 中的词位数                        |
| numnode(tsquery)                                           | integer      | tsquery 中词位外加操作符的数目             |
| querytree(query tsquery)                                 | text         | 获得一个 tsquery 的可索引部分               |
| setweight(tsvector, "char")                              | tsvector     | 为 tsvector 的每一个元素分配权重            |
| to_tsquery([ config regconfig , ]   query text)      | tsvector     | 规范化词并转换成 tsquery                  |
| to_tsvector([ config regconfig, ]   document text)  | tsvector     | 缩减文档文本成 tsvector                    |
| ts_delete(vector tsvector,   lexeme text)            | tsvector     | 从 vector 中移除给定的 lexeme         |
| ts_filter(vector tsvector,   weights "char"[])       | tsvector     | 从 vector 中只选择带有给定权重的元素 |
| ts_rewrite(query tsquery,   targettsquery,   substitute tsquery) | tsquery      | 在查询内用 substitute 替换  target     |
| ts_rewrite(query tsquery,   selecttext)                | tsquery      | 使用来自一个 SELECT 的目标和替换者进行替换  |
| tsvector_to_array(tsvector)                         | text[]       | 把 tsvector 转换为词位数组                  |

示例：
```
postgres=# SELECT array_to_tsvector('{fat,cat,rat}'::text[]);
array_to_tsvector
-------------------
 'cat' 'fat' 'rat'
(1 row)
 
postgres=# SELECT get_current_ts_config();
 get_current_ts_config 
-----------------------
 simple
(1 row)
 
postgres=# SELECT length('fat:2,4 cat:3 rat:5A'::tsvector);
 length 
--------
   3
(1 row)
 
postgres=# SELECT querytree('foo & ! bar'::tsquery);
 querytree 
-----------
 'foo'
(1 row)
 
postgres=# SELECT to_tsquery('english', 'The & Fat & Rats');
 to_tsquery 
---------------
 'fat' & 'rat'
(1 row)
 
postgres=# SELECT ts_delete('fat:2,4 cat:3 rat:5A'::tsvector, 'fat');
  ts_delete   
------------------
 'cat':3 'rat':5A
(1 row)
 
postgres=# SELECT tsvector_to_array('fat:2,4 cat:3 rat:5A'::tsvector);
 tsvector_to_array 
-------------------
 {cat,fat,rat}
(1 row)
```
以上列出了部分 TDSQL-A PostgreSQL版 支持的文本搜索函数，其他更多请参考 [官网](http://www.postgres.cn/docs/10/functions-textsearch.html)。
