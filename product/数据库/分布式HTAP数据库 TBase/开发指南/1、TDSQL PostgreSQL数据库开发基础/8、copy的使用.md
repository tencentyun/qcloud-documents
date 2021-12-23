## copy的使用

COPY用于 TDSQL PostgreSQL表和标准文件系统文件之间数据互相复制。COPY TO可以把一个表的内容复制到一个文件，COPY FROM可以从一个文件复制数据到一个表（数据以追加形式入库），COPY TO也能复制一个SELECT查询的结果到一个文件。如果指定了一个列清单，COPY将只把指定列的数据复制到文件或者从文件复制数据到指定列。如果表中有列不在列清单中，COPY FROM将会为那些列插入默认值。 使用COPY时TDSQL PostgreSQL服务器直接从“本地”一个文件读取或者写入到一个文件。该文件必须是TDSQL PostgreSQL用户（运行服务器的用户 ID）可访问的并且应该以服务器的视角来指定其名称。

### 实验表结构及数据

```
postgres=# \d+ t
                    Table "public.t"
 Column |       Type       |  Modifiers  | Storage  | Stats target | Description 
--------+-----------------------------+---------------+----------+--------------+-------------
 f1   | integer           | not null    | plain   |        | 
 f2   | character varying(32)    | not null    | extended |        | 
 f3   | timestamp without time zone | default now() | plain   |        | 
 f4   | integer           |        | plain   |        | 
Has OIDs: yes
Distribute By SHARD(f1)
    Location Nodes: ALL DATANODES
```


数据测试过程可以行再录入修改

```
postgres=# select * from t;
 f1 |  f2  |       f3       | f4 
----+-------+----------------------------+----
 3 | pgxz  | 2017-10-28 18:24:05.645691 |  
 1 | tdsql_pg |               |  7
 2 |    | 2017-10-28 18:24:05.643102 |  3
(3 rows)
```

### copy to——复制数据到文件中

#### 导出所有列

```
postgres=# copy public.t to '/data/pgxz/t.txt';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1    tdsql_pg  \N    7
2        2017-10-28 18:24:05.643102    3
3    pgxz   2017-10-28 18:24:05.645691    \N
 
```

默认生成的文件内容为表的所有列，列与列之间使用tab分隔开来。NULL值生成的值为\N

#### 导出部分列

```
postgres=# copy public.t(f1,f2) to '/data/pgxz/t.txt'; 
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1    tdsql_pg
2
3    pgxz
postgres=# 

```

只导出f1和f2列



#### 导出查询结果

```
postgres=# copy (select f2,f3 from public.t order by f3) to  '/data/pgxz/t.txt';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
    2017-10-28 18:24:05.643102
pgxz   2017-10-28 18:24:05.645691
tdsql_pg  \N
postgres=# 
 
```

查询可以是任何复杂查询



#### 指定生成文件格式

- **生成csv格式**

```
postgres=# copy public.t to '/data/pgxz/t.txt' with csv;
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdsql_pg,,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```

- **生成二进制格式**

```
postgres=# copy public.t to '/data/pgxz/t.txt' with binary;
COPY 3
postgres=# \1
postgres=# \! cat  /data/pgxz/t.txt
PGCOPY
   tdsql_pg
```

默认为TEXT格式



#### 使用delimiter指定列与列之间的分隔符

```
postgres=# copy public.t to '/data/pgxz/t.txt' with delimiter '@';
COPY 3
postgres=# \! cat /data/pgxz/t.txt                 
1@tdsql_pg@\N@7
2@pgxc@2017-10-28 18:24:05.643102@3
3@pgxz@2017-10-28 18:24:05.645691@\N
postgres=# copy public.t to '/data/pgxz/t.txt' with csv delimiter '@';
COPY 3
postgres=# \! cat /data/pgxz/t.txt                   
1@tdsql_pg@@7
2@pgxc@2017-10-28 18:24:05.643102@3
3@pgxz@2017-10-28 18:24:05.645691@
 
postgres=# copy public.t to '/data/pgxz/t.txt' with csv delimiter '@@';  
ERROR:  COPY delimiter must be a single one-byte character
 
postgres=# copy public.t to '/data/pgxz/t.txt' with binary delimiter '@';  
ERROR:  cannot specify DELIMITER in BINARY mode
 
```

指定分隔文件各列的字符。文本格式中默认是一个制表符， 而CSV格式中默认是一个逗号。分隔符必须是一个单一的单字节字符，即汉字是不支持的。使用binary格式时不允许这个选项。

#### NULL值的处理

```
postgres=# copy public.t to '/data/pgxz/t.txt' with NULL 'NULL';
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1    tdsql_pg  NULL   7
2    pgxc   2017-10-28 18:24:05.643102    3
3    pgxz   2017-10-28 18:24:05.645691    NULL
 
postgres=# copy public.t to '/data/pgxz/t.txt' with CSV NULL 'NULL';  
COPY 3
postgres=# \! cat /data/pgxz/t.txt                  
1,tdsql_pg,NULL,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,NULL
 
postgres=# copy public.t to '/data/pgxz/t.txt' with binary NULL 'NULL';  
ERROR:  cannot specify NULL in BINARY mode
postgres=# 
 
```

记录值为NULL时导出为NULL字符。使用binary格式时不允许这个选项。



#### 生成列标题名

```
postgres=# copy public.t to '/data/pgxz/t.txt' with csv HEADER;  
COPY 3
postgres=# \! cat /data/pgxz/t.txt
f1,f2,f3,f4
1,tdsql_pg,,7
2,pgxc,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
postgres=# copy public.t to '/data/pgxz/t.txt' with  HEADER;  
ERROR:  COPY HEADER available only in CSV mode
 
```

只有使用 CSV格式时才允许这个选项。



#### 导出oids系统列

```
postgres=# drop table t;
DROP TABLE
postgres=# CREATE TABLE t (
postgres(#   f1 integer NOT NULL,
postgres(#   f2 text NOT NULL,
postgres(#   f3 timestamp without time zone,
postgres(#   f4 integer
postgres(# )
postgres-# with oids DISTRIBUTE BY SHARD (f1);
CREATE TABLE
postgres=# copy t from '/data/pgxz/t.txt' with csv ;     
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+---------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
 
postgres=# copy t to  '/data/pgxz/t.txt' with oids ;        
COPY 3
postgres=# \! cat /data/pgxz/t.txt
35055  1    tdsql_pg  \N    7
35056  2    pg'",    xc  2017-10-28 18:24:05.643102    3
35177  3    pgxz   2017-10-28 18:24:05.645691    \N
 
```

创建表时使用了with oids才能使用oids 选项



#### 使用quote自定义引用字符

```
postgres=# copy t to  '/data/pgxz/t.txt' with csv;      
COPY 3
postgres=#  \! cat /data/pgxz/t.txt
1,tdsql_pg,,7
2,"pg'"",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```

默认引用字符为“双引号”

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' csv;
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdsql_pg,,7
2,%pg'",    xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
```

上面指定了引用字符为百分号，系统自动把字段值为%的字符替换为双个%

 ```
 postgres=# copy t to  '/data/pgxz/t.txt' with quote '%';
 ERROR:  COPY quote available only in CSV mode
  
 ```

只有使用 CSV格式时才允许这个选项。

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%%' csv;
ERROR:  COPY quote must be a single one-byte character
postgres=# 
 
```

引用字符必须是一个单一的单字节字符，即汉字是不支持的。

#### 使用escape自定义逃逸符

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' csv;      
COPY 3
postgres=# \! cat /data/pgxz/t.txt
1,tdsql_pg,,7
2,%pg'",    xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
 
```

不指定escape逃逸符，默认和QUOTE值一样

 ```
 postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@' csv;
 COPY 3
 postgres=# \! cat /data/pgxz/t.txt                   
 1,tdsql_pg,,7
 2,%pg'",    xc@%%,2017-10-28 18:24:05.643102,3
 3,pgxz,2017-10-28 18:24:05.645691,
  
 ```

指定逃逸符为’@’

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@@' csv; 
ERROR:  COPY escape must be a single one-byte character
 
```

这必须是一个单一的单字节字符。 

```
postgres=# copy t to  '/data/pgxz/t.txt' with quote '%' escape '@';   
ERROR:  COPY quote available only in CSV mode

```

 只有使用CSV格式时才允许这个选项。 

#### 强制给某个列添加引用字符

```
postgres=# copy t to  '/data/pgxz/t.txt' (format 'csv',force_quote (f1,f2));    
COPY 3
postgres=# \! cat /data/pgxz/t.txt
"1","tdsql_pg",,7
"2","pg'"",    xc%",2017-10-28 18:24:05.643102,3
"3","pgxz",2017-10-28 18:24:05.645691,
 
```

指定2列强制添加引用字符

```
postgres=# copy t to  '/data/pgxz/t.txt' (format 'csv',force_quote (f1,f4,f3,f2));      
COPY 3
postgres=# \! cat /data/pgxz/t.txt
"1","tdsql_pg",,"7"
"2","pg'"",    xc%","2017-10-28 18:24:05.643102","3"
"3","pgxz","2017-10-28 18:24:05.645691",
```

指定4列强制添加引用字符，字段的顺序可以任意排列

 ```
 postgres=# copy t to  '/data/pgxz/t.txt' (format 'text',force_quote (f1,f2,f3,f4));     
 ERROR:  COPY force quote available only in CSV mode
 postgres=# 
 ```

只有使用CSV格式时才允许这个选项。



#### 使用encoding指定导出文件内容编码

```
postgres=# copy t to  '/data/pgxz/t.csv' (encoding utf8);    
COPY 3
```

导出文件编码为UTF8

```
postgres=# copy t to  '/data/pgxz/t.csv' (encoding gbk);      
COPY 3
postgres=# 
```

导出文件编码为gbk

使用set_client_encdoing to gbk;也可以将文件的内容设置为需要的编码，如下所示

```
postgres=# set client_encoding to gbk;       
SET
postgres=# copy t to '/data/pgxz/t.csv' with csv ;
COPY 4
postgres=# 
```



### copy from——复制文件内容到数据表中

#### 导入所有列

```
postgres=# \! cat  /data/pgxz/t.txt        
1    tdsql_pg  \N    7
2    pg'",    xc%  2017-10-28 18:24:05.643102    3
3    pgxz   2017-10-28 18:24:05.645691    \N
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t from '/data/pgxz/t.txt';
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
```



#### 导入部分指定列

```
postgres=#  copy t(f1,f2) to '/data/pgxz/t.txt'; 
postgres=#  \! cat /data/pgxz/t.txt
1    tdsql_pg
2    pg'",    xc%
3    pgxz
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t(f1,f2) from  '/data/pgxz/t.txt';   
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     | 2017-10-30 11:54:16.559579 |  
 2 | pg'",    xc% | 2017-10-30 11:54:16.559579 |  
 3 | pgxz      | 2017-10-30 11:54:16.560283 |  
(3 rows)
 
```



有默认值的字段在没有导入时，会自动的将默认值付上

```
postgres=# \! cat /data/pgxz/t.txt 
1    \N    tdsql_pg
2    2017-10-28 18:24:05.643102    pg'",    xc%
3    2017-10-28 18:24:05.645691    pgxz
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t(f1,f3,f2) from '/data/pgxz/t.txt'; 
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
```



字段的顺序可以任意调整，但需要与导放文件的存放顺序一致

 ```
 postgres=# \! cat /data/pgxz/t.txt;
 1    tdsql_pg  \N    7
 2    pg'",    xc%  2017-10-28 18:24:05.643102    3
 3    pgxz   2017-10-28 18:24:05.645691    \N
 postgres=# copy t (f1,f2) from  '/data/pgxz/t.txt';
 ERROR:  extra data after last expected column
 CONTEXT:  COPY t, line 1: "1   tdsql_pg  \N    7"
 ```

数据文件的列表不能多于要导入的列数，否则会出错。



#### 指定导入文件格式

```
postgres=# \! cat /data/pgxz/t.txt
1    tdsql_pg  \N    7
2    pg'",    xc%  2017-10-28 18:24:05.643102    3
3    pgxz   2017-10-28 18:24:05.645691    \N
postgres=# copy t from '/data/pgxz/t.txt' (format 'text');
COPY 3
 
TRUNCATE TABLE
postgres=# \! cat /data/pgxz/t.csv
1,tdsql_pg,,7
2,"pg'"",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
postgres=#  copy t from '/data/pgxz/t.csv' (format 'csv');   
COPY 3
 
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# \! od -c /data/pgxz/t.bin
0000000  P  G  C  O  P  Y  \n 377  \r  \n  \0  \0  \0  \0  \0  \0
0000020  \0  \0  \0  \0 004  \0  \0  \0 004  \0  \0  \0 001  \0  \0  \0
0000040 005  T  b  a  s  e 377 377 377 377  \0  \0  \0 004  \0  \0
0000060  \0  \a  \0 004  \0  \0  \0 004  \0  \0  \0 002  \0  \0  \0 016
0000100  p  g  '  "  ,              x  c  %  \0  \0
0000120  \0  \b  \0 001 377 236  G  w 213  ^  \0  \0  \0 004  \0  \0
0000140  \0 003  \0 004  \0  \0  \0 004  \0  \0  \0 003  \0  \0  \0 004
0000160  p  g  x  z  \0  \0  \0  \b  \0 001 377 236  G  w 225  {
0000200 377 377 377 377 377 377
0000206
postgres=# copy t from '/data/pgxz/t.bin' (format 'binary');
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows) 
```



#### 使用delimiter指定列与列之间的分隔符

```
postgres=#  \! cat /data/pgxz/t.txt
1%tdsql_pg%\N%7
2%pg'",    xc\%%2017-10-28 18:24:05.643102%3
3%pgxz%2017-10-28 18:24:05.645691%\N
postgres=# copy t from  '/data/pgxz/t.txt' (format 'text',delimiter '%');    
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
 
postgres=# \! cat /data/pgxz/t.csv
1%tdsql_pg%%7
2%"pg'"",    xc%"%2017-10-28 18:24:05.643102%3
3%pgxz%2017-10-28 18:24:05.645691%
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t from  '/data/pgxz/t.csv' (format 'csv',delimiter '%');       
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
```



#### NULL值处理

```
postgres=#  \! cat /data/pgxz/t.txt
1    tdsql_pg  NULL   7
2    pg'",    xc%  2017-10-28 18:24:05.643102    3
3    pgxz   2017-10-28 18:24:05.645691    NULL
postgres=# copy t from '/data/pgxz/t.txt' (null 'NULL');
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
 
```

将文件中的NULL字符串当成NULL值处理,SQL SERVER导出来的文件中把NULL值替换成字符串NULL,所以入库时可以这样处理一下，注意字符串是区分大小写，如下面语句导入数据就会出错

 ```
 postgres=# copy t from '/data/pgxz/t.txt' (null 'null');  
 ERROR:  invalid input syntax for type timestamp: "NULL"
 CONTEXT:  COPY t, line 1, column f3: "NULL"
 ```





#### 自定义quote字符

```
postgres=# \! cat /data/pgxz/t.csv
1,tdsql_pg,,7
2,%pg'",    xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
 
```

如果不配置quote字符则无法导入文件

```
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv');
ERROR:  unterminated CSV quoted field
CONTEXT:  COPY t, line 4: "2,%pg'",    xc%%%,2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
"
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv',quote '%');
COPY 3
postgres=# 
 
postgres=# copy t from '/data/pgxz/t.csv' (format 'text',quote '%');  
ERROR:  COPY quote available only in CSV mode
```

只有csv格式导入时才能配置quote字符



#### 自定义escape字符

```
postgres=#  \! cat  /data/pgxz/t.csv
1,tdsql_pg,,7
2,"pg'@",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
postgres=#  copy t from '/data/pgxz/t.csv' (format 'csv'); 
ERROR:  unterminated CSV quoted field
CONTEXT:  COPY t, line 4: "2,"pg'@",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
"
 
```

不指定escape字符时，系统默认就是双写的quote字符，如双倍的“双引号”

 ```
 postgres=#  copy t from '/data/pgxz/t.csv' (format 'csv',escape '@');       
 COPY 3
 postgres=# select * from t;
  f1 |    f2    |       f3       | f4 
 ----+----------------+----------------------------+----
  1 | tdsql_pg     |               |  7
  2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
  3 | pgxz      | 2017-10-28 18:24:05.645691 |  
 (3 rows)
  
 postgres=# 
 ```



#### csv header忽略首行

```
postgres=# \! cat /data/pgxz/t.csv;
f1,f2,f3,f4
1,tdsql_pg,,7
2,"pg'"",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv');
ERROR:  invalid input syntax for integer: "f1"
CONTEXT:  COPY t, line 1, column f1: "f1"
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv',header true);
COPY 3
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
```

如果不忽略首行，则系统会把首行当成数据，造成导入失败



#### 导入oid列值

```
postgres=# \! cat /data/pgxz/t.txt
35242  1    tdsql_pg  \N    7
35243  2    pg'",    xc%  2017-10-28 18:24:05.643102    3
35340  3    pgxz   2017-10-28 18:24:05.645691    \N
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t from '/data/pgxz/t.txt' (oids true);
COPY 3
postgres=# select oid,* from t; 
 oid  | f1 |    f2    |       f3       | f4 
-------+----+----------------+----------------------------+----
 35242 |  1 | tdsql_pg     |               |  7
 35243 |  2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 35340 |  3 | pgxz      | 2017-10-28 18:24:05.645691 |  
(3 rows)
```



#### 使用FORCE_NOT_NULL把某列中空值变成长度为0的字符串，而不是NULL值

```
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# \! cat '/data/pgxz/t.csv' ;       
1,tdsql_pg,,7
2,"pg'"",    xc%",2017-10-28 18:24:05.643102,3
3,pgxz,2017-10-28 18:24:05.645691,
4,,2017-10-30 16:14:14.954213,4
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv');
ERROR:  node:16386, error null value in column "f2" violates not-null constraint
DETAIL:  Failing row contains (4, null, 2017-10-30 16:14:14.954213, 4).
postgres=# select * from t where f2='';
 f1 | f2 | f3 | f4 
----+----+----+----
(0 rows)
```



不使用FORCE_NOT_NULL处理的话就变成NULL值

```
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# copy t from '/data/pgxz/t.csv' (format 'csv' ,FORCE_NOT_NULL (f2));
COPY 4
postgres=# select * from t where f2='';
 f1 | f2 |       f3       | f4 
----+----+----------------------------+----
 4 |   | 2017-10-30 16:14:14.954213 |  4
(1 row)
 
```

使用FORCE_NOT_NULL处理就变成长度为0的字符串



#### encoding指定导入文件的编码

```
postgres=# \! enca -L zh_CN /data/pgxz/t.txt   
Simplified Chinese National Standard; GB2312
 
postgres=# copy t from '/data/pgxz/t.txt' ;
COPY 4
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
 4 |         | 2017-10-30 16:41:09.157612 |  4
(4 rows)
```

不指定导入文件的编码格式，则无法正确导入中文字符

 ```
 postgres=# truncate table t;
 TRUNCATE TABLE
 postgres=# copy t from '/data/pgxz/t.txt' (encoding gbk) ;
 COPY 4
 postgres=# select * from t;
  f1 |    f2    |       f3       | f4 
 ----+----------------+----------------------------+----
  1 | tdsql_pg     |               |  7
  2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
  3 | pgxz      | 2017-10-28 18:24:05.645691 |  
  4 | 腾讯      | 2017-10-30 16:41:09.157612 |  4
 (4 rows)
 ```

使用encoding gbk后便可以正确导入文件的内容，你也可以使用下面的方式转换导入文件的编码后再导入数据

```
postgres=# truncate table t;
TRUNCATE TABLE
postgres=# \! enconv -L zh_CN -x UTF-8 /data/pgxz/t.txt
postgres=# copy t from '/data/pgxz/t.txt';
COPY 4
postgres=# select * from t;
 f1 |    f2    |       f3       | f4 
----+----------------+----------------------------+----
 1 | tdsql_pg     |               |  7
 2 | pg'",    xc% | 2017-10-28 18:24:05.643102 |  3
 3 | pgxz      | 2017-10-28 18:24:05.645691 |  
 4 | 腾讯      | 2017-10-30 16:41:09.157612 |  4
(4 rows)
  
```



