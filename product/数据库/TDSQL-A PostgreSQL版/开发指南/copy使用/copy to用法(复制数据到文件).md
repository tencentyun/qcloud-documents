## 导出所有列
```
postgres=# copy public.t to '/data/pgxz/t.txt';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1       tdapg   \N      7
2               2017-10-28 18:24:05.643102      3
3       pgxz    2017-10-28 18:24:05.645691      \N
```

默认生成的文件内容为表的所有列，列与列之间使用 tab 分隔开来。NULL 值生成的值为\N。

## 导出部分列
```
postgres=# copy public.t(f1,f2) to '/data/pgxz/t.txt'; 
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1       tdapg
2
3       pgxz
postgres=# 

```
只导出f1和f2列。

## 导出查询结果
```
postgres=# copy (select f2,f3 from public.t order by f3) to  '/data/pgxz/t.txt';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
        2017-10-28 18:24:05.643102
pgxz    2017-10-28 18:24:05.645691
tdapg   \N
postgres=# 
```
查询可以是任何复杂查询。

## 指定生成文件格式
### 生成 csv 格式
```
postgres=# copy public.t to '/data/pgxz/t.txt' with csv;
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdapg,,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```

### 生成二进制格式

```
postgres=# copy public.t to '/data/pgxz/t.txt' with binary;
COPY 3
postgres=# \1
postgres=# \! cat  /data/pgxz/t.txt
PGCOPY
    tdapg
```
默认为 TEXT 格式。

## 使用 delimiter 指定列与列之间的分隔符
```
postgres=# copy public.t to '/data/pgxz/t.txt' with delimiter '@';      
COPY 3
postgres=# \! cat /data/pgxz/t.txt                                
1@tdapg@\N@7
2@pgxc@2017-10-28 18:24:05.643102@3
3@pgxz@2017-10-28 18:24:05.645691@\N
postgres=# copy public.t to '/data/pgxz/t.txt' with csv delimiter '@';
COPY 3
postgres=# \! cat /data/pgxz/t.txt                                    
1@tdapg@@7
2@pgxc@2017-10-28 18:24:05.643102@3
3@pgxz@2017-10-28 18:24:05.645691@
 
postgres=# copy public.t to '/data/pgxz/t.txt' with csv delimiter '@@';  
ERROR:  COPY delimiter must be a single one-byte character

postgres=# copy public.t to '/data/pgxz/t.txt' with binary delimiter '@';   
ERROR:  cannot specify DELIMITER in BINARY mode
```

指定分隔文件各列的字符。文本格式中默认是一个制表符， 而 CSV 格式中默认是一个逗号。分隔符必须是一个单一的单字节字符，即汉字是不支持的。使用 binary 格式时不允许这个选项。

## NULL 值的处理
```
postgres=# copy public.t to '/data/pgxz/t.txt' with NULL 'NULL';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1       tdapg   NULL    7
2       pgxc    2017-10-28 18:24:05.643102      3
3       pgxz    2017-10-28 18:24:05.645691      NULL

postgres=# copy public.t to '/data/pgxz/t.txt' with CSV NULL 'NULL';  
COPY 3
postgres=# \! cat /data/pgxz/t.txt                                  
1,tdapg,NULL,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,NULL

postgres=# copy public.t to '/data/pgxz/t.txt' with binary NULL 'NULL';   
ERROR:  cannot specify NULL in BINARY mode
postgres=# 
```

记录值为 NULL 时导出为 NULL 字符。使用 binary 格式时不允许这个选项。

## 生成列标题名
```
postgres=# copy public.t to '/data/pgxz/t.txt' with csv HEADER;   
COPY 3
postgres=# \! cat /data/pgxz/t.txt
f1,f2,f3,f4
1,tdapg,,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
postgres=# copy public.t to '/data/pgxz/t.txt' with  HEADER;   
ERROR:  COPY HEADER available only in CSV mode
```

只有使用 CSV 格式时才允许这个选项。

## 导出 oids 系统列
```
postgres=# drop table t;
DROP TABLE
postgres=# CREATE TABLE t (
postgres(#     f1 integer NOT NULL,
postgres(#     f2 text NOT NULL,
postgres(#     f3 timestamp without time zone,
postgres(#     f4 integer
postgres(# )
postgres-# with oids DISTRIBUTE BY SHARD (f1);
CREATE TABLE
postgres=# copy t from '/data/pgxz/t.txt' with csv ;         
COPY 3
postgres=# select * from t;
 f1 |      f2       |             f3             | f4 
----+---------------+----------------------------+----
  1 | tdapg         |                            |  7
  2 | pg'",      xc | 2017-10-28 18:24:05.643102 |  3
  3 | pgxz          | 2017-10-28 18:24:05.645691 |   
(3 rows)

postgres=# copy t to  '/data/pgxz/t.txt' with oids ;              
COPY 3
postgres=# \! cat /data/pgxz/t.txt
35055   1       tdapg   \N      7
35056   2       pg'",      xc   2017-10-28 18:24:05.643102      3
35177   3       pgxz    2017-10-28 18:24:05.645691      \N
```
创建表时使用了 with oids 才能使用 oids 选项。

## 使用 quote 自定义引用字符
```
postgres=# copy t to  '/data/pgxz/t.txt' with csv;          
COPY 3
postgres=#  \! cat /data/pgxz/t.txt
1,tdapg,,7
2,"pg'"",      xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```
默认引用字符为“双引号”。
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' csv;
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdapg,,7
2,%pg'",      xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```
上面指定了引用字符为百分号，系统自动把字段值为%的字符替换为双个%
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%';
ERROR:  COPY quote available only in CSV mode
```
只有使用 CSV 格式时才允许这个选项。
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%%' csv;
ERROR:  COPY quote must be a single one-byte character
postgres=# 
```
引用字符必须是一个单一的单字节字符，即汉字是不支持的。

## 使用 escape 自定义逃逸符
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' csv;           
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdapg,,7
2,%pg'",      xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```
不指定 escape 逃逸符，默认和 QUOTE 值一样。

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@' csv;
COPY 3
postgres=# \! cat /data/pgxz/t.txt                                     
1,tdapg,,7
2,%pg'",      xc@%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```

指定逃逸符为’@’。
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@@' csv; 
ERROR:  COPY escape must be a single one-byte character
```
这必须是一个单一的单字节字符。 
```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@';    
ERROR:  COPY quote available only in CSV mode
```
只有使用 CSV 格式时才允许这个选项。 

## 强制给某个列添加引用字符
```
postgres=# copy t to  '/data/pgxz/t.txt' (format 'csv',force_quote (f1,f2));      
COPY 3
postgres=# \! cat /data/pgxz/t.txt
"1","tdapg",,7
"2","pg'"",      xc%",2017-10-28 18:24:05.643102,3
"3","pgxz",2017-10-28 18:24:05.645691,
```
指定2列强制添加引用字符。

```
postgres=# copy t to  '/data/pgxz/t.txt' (format 'csv',force_quote (f1,f4,f3,f2));          
COPY 3
postgres=# \! cat /data/pgxz/t.txt
"1","tdapg",,"7"
"2","pg'"",      xc%","2017-10-28 18:24:05.643102","3"
"3","pgxz","2017-10-28 18:24:05.645691",
```

指定4列强制添加引用字符，字段的顺序可以任意排列。
```
postgres=# copy t to  '/data/pgxz/t.txt' (format 'text',force_quote (f1,f2,f3,f4));         
ERROR:  COPY force quote available only in CSV mode
postgres=# 
```
只有使用 CSV 格式时才允许这个选项。

## 使用 encoding 指定导出文件内容编码
```
postgres=# copy t to  '/data/pgxz/t.csv' (encoding utf8);      
COPY 3
```
导出文件编码为UTF8。

```
postgres=# copy t to  '/data/pgxz/t.csv' (encoding gbk);          
COPY 3
postgres=# 
```
导出文件编码为gbk。

使用set_client_encdoing to gbk;也可以将文件的内容设置为需要的编码，如下所示：
```
postgres=# set client_encoding to gbk;            
SET
postgres=# copy t to '/data/pgxz/t.csv' with csv ;
COPY 4
postgres=# 
```
 
