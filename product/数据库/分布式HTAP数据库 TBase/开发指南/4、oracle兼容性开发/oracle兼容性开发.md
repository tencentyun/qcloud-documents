# oracle兼容性开发

oracle 兼容性开发针对的是 TDSQL PostgreSQL-v5.0版本。
## oracle GUC参数配置
### session中生效
```
SET enable_oracle_compatible to ON;
```



### 配置某个库默认生效

```
alter database postgres set enable_oracle_compatible to on;
```



### 配置某个用户默认生效

```
alter role tbase set enable_oracle_compatible to on;
```



## 数据类型
### varchar2
```
postgres=# create table t_varchar2(f1 varchar2,f2 int);
CREATE TABLE
postgres=# \d+ t_varchar2
                                 Table "public.t_varchar2"
 Column |   Type   | Collation | Nullable | Default | Storage  | Stats target | Description 
--------+----------+-----------+----------+---------+----------+--------------+-------------
 f1     | varchar2 |           | not null |         | extended |              | 
 f2     | integer  |           |          |         | plain    |              | 
 
postgres=#
```
### number
```
postgres=# create table t_number(f1 number,f2 number(10),f3 number(10,2));
CREATE TABLE
postgres=#  \d t_number 
                 Table "public.t_number"
 Column |     Type      | Collation | Nullable | Default 
--------+---------------+-----------+----------+---------
 f1     | numeric       |           | not null | 
 f2     | numeric(10,0) |           |          | 
 f3     | numeric(10,2) |           |          | 
 
postgres=#
```

系统转换成numeric
### blob
```
postgres=# create table t_blob(f1 int,f2 Blob);
CREATE TABLE
postgres=# \d t_blob
               Table "public.t_blob"
 Column |  Type   | Collation | Nullable | Default 
--------+---------+-----------+----------+---------
 f1     | integer |           | not null | 
 f2     | blob    |           |          | 
 
postgres=#
```

 TDSQL PG版的blob类型支持最大长度为1G
### clob
```
postgres=# create table t_clob(f1 int,f2 clob);
CREATE TABLE
postgres=# \d t_clob
               Table "public.t_clob"
 Column |  Type   | Collation | Nullable | Default 
--------+---------+-----------+----------+---------
 f1     | integer |           | not null | 
 f2     | clob    |           |          | 
 
postgres=#
```

 TDSQL PG版的clob类型支持最大长度为1G

 


## 兼容性函数
### 字符函数
#### regexp_count
REGEXP_COUNT 返回pattern 在source_char 串中出现的次数

```
postgres=# select REGEXP_COUNT('tdsql_pg_tdsql_pg','se') from DUAL;
 regexp_count 
--------------
            2
(1 row)
```
#### instr
instr函数返回要截取的字符串在源字符串中的位置

```
postgres=# select instr('helloworld','l') from dual;
 instr 
-------
     3
(1 row)
 
postgres=#
```
#### regexp_substr
string:需要进行正则处理的字符串 
pattern：进行匹配的正则表达式  
position：起始位置，从字符串的第几个字符开始正则表达式匹配（默认为1） 注意：字符串最初的位置是1而不是0   
occurrence：获取第几个分割出来的组（分割后最初的字符串会按分割的顺序排列成组）     
modifier：模式（‘i’不区分大小写进行检索；‘c’区分大小写进行检索。默认为’c’）针对的是正则表达式里字符大小写的匹配

```
postgres=# SELECT REGEXP_SUBSTR('17,20,23','[^,]+',1,1,'i') AS STR FROM DUAL;  
 str 
-----
 17
(1 row)
 
postgres=#
```
#### regexp_replace
```
regexp_replace(1,2,3,4,5,6)  
```
语法说明：1：字段   2：替换的字段  3：替换成什么  4：起始位置（默认从1开始）  5：替换的次数（0是无限次）  6：不区分大小写
```
postgres=# select regexp_replace('tbase_tbase','s','ee',1,1) from dual; 
 regexp_replace 
----------------
 tbaeee_tbase
(1 row)
 
postgres=#
```
#### nlssort
指定排序规则

```
postgres=# create table t_nlssort(f1 integer,f2 varchar2(10));
 
CREATE TABLE
postgres=# 
postgres=# insert into t_nlssort values(1,'腾讯');
INSERT 0 1
postgres=# 
postgres=# insert into t_nlssort values(2,'深圳');
INSERT 0 1
postgres=# 
postgres=# insert into t_nlssort values(3,'中国');
INSERT 0 1
postgres=# SELECT * FROM t_nlssort ORDER BY NLSSORT(f2,'NLS_SORT = SCHINESE_PINYIN_M');
 f1 |  f2  
----+------
  2 | 深圳
  1 | 腾讯
  3 | 中国
(1 rows)
```

目前 TDSQL PostgreSQL只能支持按拼音

#### nls_upper
将字符转换为大写

```
postgres=# select NLS_UPPER('tdsql_pg','nls_sort= SCHINESE_PINYIN_M')  from dual;
 nls_upper 
-----------
 TDSQL_PG
(1 row)
```
#### nchr
给出一个数字代码，返回其对应字符

```
postgres=# select NCHR(116) from dual;
 nchr 
------
 t
(1 row)
```
#### length
获取字符长度

```
postgres=# select length(1);
 length 
--------
      1
(1 row)
 
postgres=# select length('tdsql_pg');
 length 
--------
      8
(1 row)
 
postgres=# select length('阿弟'); 
 length 
--------
      2
(1 row)
 
postgres=# select length(12.12::numeric(10,2));
 length 
--------
      5
(1 row)
```
#### LENGTHB
返回字符的长度

```
postgres=# select LENGTHB('测试') from dual;
 lengthb 
---------
       6
(1 row)
 
postgres=# select LENGTH('测试') from dual; 
 length 
--------
      2
(1 row)
```
### 日期函数
#### NUMTODSINTERVAL
 numtodsinterval(<x>,<c>) ,x是一个数字,c是一个字符串,
表明x的单位,这个函数把x转为interval day to second数据类型

```
postgres=# select sysdate,sysdate+numtodsinterval(2,'hour') as res from dual; 
    orcl_sysdate     |         res         
---------------------+---------------------
 2020-08-02 21:55:35 | 2020-08-02 23:55:35
(1 row)
 
postgres=#
#### 10.3.2.2、DBTIMEZONE
postgres=# select DBTIMEZONE from dual;
 dbtimezone 
------------
 08:00:00
(1 row)
 
postgres=#
```
#### MONTHS_BETWEEN
```
MONTHS_BETWEEN(DATE1,DATE2), 函数返回两个日期之间的月份数
```
```
postgres=# select months_between(to_date('20210331', 'yyyymmdd'), to_date('20200131', 'yyyymmdd')) as months from dual;
 months 
--------
     14
(1 row)
 
postgres=#
#### 10.3.2.4、LAST_DAY
```

#### LAST_DAY

LAST_DAY函数返回指定日期对应月份的最后一天

 ```
 postgres=#  SELECT last_day('2020-05-01') FROM dual;            
        last_day        
------------------------
 2020-05-31 00:00:00+08
(1 row)
 ```

#### ADD_MONTHS
```
ADD_MONTHS(x,y)
```
x值为日期，y值为数量, 用于计算某个日期向前或者向后y个月后的时间

```
postgres=#  select add_months(sysdate,1) from dual;  
     add_months      
---------------------
 2020-09-04 16:08:11
(1 row)
 
postgres=#  select add_months(sysdate,-1) from dual;
     add_months      
---------------------
 2020-07-04 16:08:15
(1 row)
 
postgres=#
```
### 转换函数
#### to_clob
转换字符为clob类型

```
postgres=#  select to_clob('tbase') from dual;
 to_clob 
---------
 tbase
(1 row)
```
#### ROWIDTOCHAR
转换rowid值为varchar2类型

```
postgres=# \d+ t_rowid
                                  Table "public.t_rowid"
 Column |  Type   | Collation | Nullable | Default | Storage | Stats target | Description 
--------+---------+-----------+----------+---------+---------+--------------+-------------
 f1     | integer |           | not null |         | plain   |              | 
 f2     | integer |           |          |         | plain   |              | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
 
postgres=# SELECT ROWIDTOCHAR(rowid),rowid from t_rowid;
     rowidtochar      |        rowid         
----------------------+----------------------
 XPK3fw==AAAAAA==AQA= | XPK3fw==AAAAAA==AQA=
(1 row)
 
postgres=#
```

#### CHARTOROWID
```
CHARTOROWID(c1)
```
转换varchar2类型为rowid值,c1,字符串，长度为20的字符串，字符串必须符合rowid格式，ROWID

```
postgres=# select CHARTOROWID('AAAFd1AAFAAAABSACCAA') a1 from dual;
          a1          
----------------------
 AAAFdw==FAAAAA==CCA=
(1 row)
 
postgres=#
```
### 系统函数
### xml相关函数
#### extractvalue
xml文本解释
 ```
 
postgres=# SELECT extractvalue(XMLTYPE('
<AAA> 
<BBB>治愈</BBB> 
<BBB>好转</BBB>  
<BBB>其他</BBB>  
</AAA>   
'),'/AAA/BBB[2]') FROM dual;
 extractvalue 
--------------
 好转
(1 row)
 ```
#### extract
```
extract(xmltype类型,节点)
```

```
create table xmlexample(ID varchar(100),name varchar(20),data xmltype);
 
insert into xmlexample(id,name,data) values('xxxxxxxxxxxxxxx','my document','<?xml version="1.0" encoding="UTF-8" ?>
<collection xmlns="">
  <record>
    <leader>-----nam0-22-----^^^450-</leader>
    <datafield tag="200" ind1="1" ind2=" ">
      <subfield code="a">抗震救灾</subfield>
       <subfield code="f">奥运会</subfield>
    </datafield>
    <datafield tag="209" ind1=" " ind2=" ">
      <subfield code="a">经济学</subfield>
       <subfield code="b">计算机</subfield>
       <subfield code="c">10001</subfield>
       <subfield code="d">2005-07-09</subfield>
    </datafield>
    <datafield tag="610" ind1="0" ind2=" ">
       <subfield code="a">计算机</subfield>
       <subfield code="a">笔记本</subfield>
    </datafield>
  </record>
</collection>'::xmltype);
```

```
postgres=# select id,name, extract(x.data,'/collection/record/datafield/subfield') as A from xmlexample x;
       id        |    name     |                                                                                                                       
                            a                                                                                                                          
                         
-----------------+-------------+-----------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------
 xxxxxxxxxxxxxxx | my document | <subfield code="a">抗震救灾</subfield><subfield code="f">奥运会</subfield><subfield code="a">经济学</subfield><subfiel
d code="b">计算机</subfield><subfield code="c">10001</subfield><subfield code="d">2005-07-09</subfield><subfield code="a">计算机</subfield><subfield co
de="a">笔记本</subfield>
(1 row)
```

### 表达式函数
#### lnnvl
传入表达式为true 返回false；传入为false 返回true

```
postgres=# create table t_lnnvl(f1 integer, f2 integer);
CREATE TABLE
postgres=# 
postgres=# insert into t_lnnvl values(1,1);
INSERT 0 1
postgres=# 
postgres=# insert into t_lnnvl values(1,2);
INSERT 0 1
postgres=# 
postgres=# insert into t_lnnvl values(1,3);
INSERT 0 1
postgres=# 
postgres=# insert into t_lnnvl values(1,4);
INSERT 0 1
postgres=# 
postgres=# insert into t_lnnvl values(1,null);
INSERT 0 1
postgres=# select * from t_lnnvl where lnnvl(f2>2);
 f1 | f2 
----+----
  1 |  1
  1 |  2
  1 |   
(2 rows)
```
#### nvl2
```
NVL2(E1, E2, E3)
```
如果E1为NULL，则函数返回E3，若E1不为null，则返回E2

```
postgres=#  select NVL2('tbase', 'tbase1'::text, 'tbase2'::text) from dual;    
  nvl2  
--------
 tbase1
(1 row)
 
postgres=#
 
postgres=#  select NVL2(NULL, 'tbase1'::text, 'tbase2'::text) from dual;
  nvl2  
--------
 tbase2
(1 row)
```
### 二进制操作函数
#### empty_clob
初始化CLOB字段

```
postgres=# select empty_clob();
 empty_clob 
------------
 
(1 row)
 
postgres=# create table t1 (f1 int,f2 clob);
CREATE TABLE
postgres=# insert into t1(f1,f2) values (1,empty_clob());
INSERT 0 1
postgres=#
```
### 统计函数
#### listagg
```
listagg (filedname,',') WITHIN GROUP (ORDER BY filedname)
```
行转列函数

```
postgres=# create table person
postgres-# (
postgres(#    deptno varchar2(10),
postgres(#    ename  varchar(20)
postgres(# );
CREATE TABLE
postgres=# insert into person values('20','aaa');
INSERT 0 1
postgres=# 
postgres=# insert into person values('20','bbb');
INSERT 0 1
postgres=# 
postgres=# insert into person values('20','ccc');  
INSERT 0 1
postgres=# 
postgres=# insert into person values('21','ddd');
INSERT 0 1
postgres=# 
postgres=# insert into person values('21','eee');
INSERT 0 1
postgres=# select
postgres-#     deptno,
postgres-#     listagg (ename,',') WITHIN GROUP (ORDER BY ENAME)
postgres-# from
postgres-#     person   
postgres-# group by
postgres-#     deptno ;
 
 deptno |   listagg   
--------+-------------
 20     | aaa,bbb,ccc
 21     | ddd,eee
(2 rows)
```
## 系统特性
### dual
```
postgres=# select 1 as f1 from dual; 
 f1 
----
  1
(1 row)
 
postgres=#
```
### rowid
```
postgres=# create table t_rowid(f1 int,f2 int);
CREATE TABLE
postgres=# insert into t_rowid values(1,1);
INSERT 0 1
postgres=# select rowid,f1,f2 from  t_rowid;
        rowid         | f1 | f2 
----------------------+----+----
 XPK3fw==AAAAAA==AQA= |  1 |  1
(1 row)
 
postgres=#
```
### rownum
```
postgres=# create table t_rownum(f1 int,f2 int);
CREATE TABLE
postgres=# insert into t_rownum values(1,1);
INSERT 0 1
postgres=# insert into t_rownum values(2,2);
INSERT 0 1
postgres=# insert into t_rownum values(3,3);
INSERT 0 1
postgres=# insert into t_rownum values(4,4);
INSERT 0 1
postgres=# insert into t_rownum values(5,5);
INSERT 0 1
postgres=# select rownum,* from t_rownum;
 rownum | f1 | f2 
--------+----+----
      1 |  1 |  1
      2 |  2 |  2
      3 |  3 |  3
      4 |  4 |  4
      5 |  5 |  5
(5 rows)
 
postgres=# select rownum,* from t_rownum where rownum<3;
 rownum | f1 | f2 
--------+----+----
      1 |  1 |  1
      2 |  2 |  2
(2 rows)
```
### sysdate
```
postgres=# select sysdate from dual;
    orcl_sysdate     
---------------------
 2020-08-02 19:09:03
(1 row)
10.4.5、systimestamp
postgres=# select systimestamp from dual;        
       orcl_systimestamp       
-------------------------------
 2020-08-02 19:09:34.032923+08
(1 row)
```
### merge into
```
postgres=# create table test1(id int primary key,name varchar2(10));
CREATE TABLE
postgres=# insert into test1 values(1,'test1');
insert into test1 values(2,'test1');
INSERT 0 1
postgres=# insert into test1 values(2,'test1');
INSERT 0 1
postgres=# insert into test1 values(3,'test1');
INSERT 0 1
postgres=# create table test2(id int primary key,name varchar2(10));
CREATE TABLE
postgres=# insert into test2 values(2,'test2');
INSERT 0 1
postgres=# insert into test2 values(3,'test2');
INSERT 0 1
postgres=# insert into test2 values(4,'test2');
INSERT 0 1
postgres=# insert into test2 values(5,'test2');
INSERT 0 1
postgres=# MERGE INTO test1 t
postgres-# USING (
postgres(#   select * from test2
postgres(# ) t2 ON (t.id = t2.id)
postgres-# WHEN MATCHED THEN UPDATE SET t.name = t2.name WHERE t.id = t2.id 
postgres-# WHEN NOT MATCHED THEN INSERT (id,name) VALUES (t2.id, t2.name) ;
MERGE 4
postgres=# select * from test1;
 id | name  
----+-------
  1 | test1
  2 | test2
  3 | test2
  4 | test2
  5 | test2
(5 rows)
```
### connect by
使用level实现1到5的序列
```
postgres=# select level from dual connect by level<=5;
 level 
-------
     1
     2
     3
     4
     5
(5 rows)
```
### pivot
```
create table scores(student varchar(10) not null, course varchar(10) not null,score int not null);
insert into scores values('张三','语文',78);
insert into scores values('张三','语文',98);
insert into scores values('张三','数学',79);
insert into scores values('张三','英语',80);
insert into scores values('张三','物理',81);
insert into scores values('李四','语文',65);
insert into scores values('李四','数学',75);
insert into scores values('李四','英语',85);
insert into scores values('李四','物理',95);
 
select 
    t.*,
    (t.语+t.数+t.外+t.物) as total
from
(
    select 
        *
    from 
        scores pivot 
        ( 
            max(score) for course in ('语文' as 语 , '数学' as 数, '英语' as 外,'物理' as 物) 
        )
) t;
 
 student | 语 | 数 | 外 | 物 | total 
---------+----+----+----+----+-------
 李四    | 65 | 75 | 85 | 95 |   320
 张三    | 98 | 79 | 80 | 81 |   338
(2 rows)
```
### limit x offset 1
如果参数enable_oracle_compatible配置为on，则offset 1表示从第一条提取记录
 ```
postgres=# select * from test1;
 id | name  
----+-------
  1 | test1
  2 | test2
  3 | test2
  4 | test2
  5 | test2
(5 rows)
 
postgres=# select * from test1 limit 5 offset 1;
 id | name  
----+-------
  1 | test1
  2 | test2
  3 | test2
  4 | test2
  5 | test2
(5 rows)
 ```
## sql_hint
### 加载插件
```
postgres=# create extension pg_hint_plan ;
CREATE EXTENSION
postgres=# alter role all set session_preload_libraries='pg_hint_plan';
ALTER ROLE
postgres=# \c
```
### hint用例
#### full全表扫描
```
postgres=# create table hint_t1(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# create index hint_t1_f1_idx on hint_t1(f1);
CREATE INDEX
postgres=# insert into hint_t1 select t as f1,t as f2 from generate_series(1,10000) as t;
;INSERT 0 10000
 
postgres=# explain select /*+SeqScan(hint_t1) */ * from hint_t1 where f1=1;   
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.00..205.00 rows=1 width=8)
   ->  Seq Scan on hint_t1  (cost=0.00..205.00 rows=1 width=8)
         Filter: (f1 = 1)
(3 rows)
 
postgres=#  explain select  * from hint_t1 where f1=1;                       
                                     QUERY PLAN                                     
------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.16..4.18 rows=1 width=8)
   ->  Index Scan using hint_t1_f1_idx on hint_t1  (cost=0.16..4.18 rows=1 width=8)
         Index Cond: (f1 = 1)
(3 rows)
 
postgres=# explain select /*+full(hint_t1) */ * from hint_t1 where f1=1; 
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.00..205.00 rows=1 width=8)
   ->  Seq Scan on hint_t1  (cost=0.00..205.00 rows=1 width=8)
         Filter: (f1 = 1)
(3 rows)
```
#### index全表扫描
```
postgres=# create table hint_t2(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# create index hint_t2_f1_idx on hint_t2(f1);
insert into hint_t2 select t as f1,t as f2 from generate_series(1,1000) as t;    
CREATE INDEX
postgres=# insert into hint_t2 select t as f1,t as f2 from generate_series(1,1000) as t;    
INSERT 0 1000
postgres=# vacuum ANALYZE hint_t2;
VACUUM
postgres=#
 
postgres=# explain select /*+index(hint_t2) */ * from hint_t2 where f1>1; 
                                       QUERY PLAN                                       
----------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.15..28.65 rows=1000 width=8)
   ->  Index Scan using hint_t2_f1_idx on hint_t2  (cost=0.15..28.65 rows=1000 width=8)
         Index Cond: (f1 > 1)
(3 rows)
 
postgres=# explain select /*+index(hint_t2 hint_t2_f1_idx1) */ * from hint_t2 where f1>1; 
                                          QUERY PLAN                                          
----------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=10000000000.00..10000000020.50 rows=1000 width=8)
   ->  Seq Scan on hint_t2  (cost=10000000000.00..10000000020.50 rows=1000 width=8)
         Filter: (f1 > 1)
(3 rows)
```
#### no_index全表扫描
```
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# create index hint_t7_f1_idx on hint_t7(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t7;
VACUUM
 
postgres=# explain select /*+no_index(hint_t7) */ * from hint_t7 where f1=1 ;
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.00..200.00 rows=1 width=8)
   ->  Seq Scan on hint_t7  (cost=0.00..200.00 rows=1 width=8)
         Filter: (f1 = 1)
(3 rows)
 
postgres=# explain select  * from hint_t7 where f1=1 ;                       
                                     QUERY PLAN                                     
------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.16..4.18 rows=1 width=8)
   ->  Index Scan using hint_t7_f1_idx on hint_t7  (cost=0.16..4.18 rows=1 width=8)
         Index Cond: (f1 = 1)
(3 rows)
 
postgres=#
```
#### 别名使用
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t; 
create index hint_t6_f1_idx on hint_t6(f1);      
vacuum ANALYZE hint_t6;INSERT 0 10000
postgres=# create index hint_t6_f1_idx on hint_t6(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t6;
VACUUM
postgres=# select /*+full(hint_t6) */ * from hint_t6 a where f1=1;
 f1 | f2 
----+----
  1 |  1
(1 row)
 
postgres=# explain select /*+full(hint_t6) */ * from hint_t6 a where f1=1;;
                                      QUERY PLAN                                      
--------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.16..4.18 rows=1 width=8)
   ->  Index Scan using hint_t6_f1_idx on hint_t6 a  (cost=0.16..4.18 rows=1 width=8)
         Index Cond: (f1 = 1)
(3 rows)
 
postgres=# explain select /*+full(a) */ * from hint_t6 a where f1=1;  
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.00..200.00 rows=1 width=8)
   ->  Seq Scan on hint_t6 a  (cost=0.00..200.00 rows=1 width=8)
         Filter: (f1 = 1)
(3 rows)
```
#### 强制走nest loop
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# vacuum ANALYZE hint_t6;
VACUUM
postgres=#
 
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# vacuum ANALYZE hint_t7;
VACUUM
postgres=#
 
postgres=# explain select * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t1.f1>9999 ;  
                                  QUERY PLAN                                  
------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=200.01..412.52 rows=1 width=16)
   ->  Hash Join  (cost=200.01..412.52 rows=1 width=16)
         Hash Cond: (t.f1 = t1.f1)
         ->  Seq Scan on hint_t6 t  (cost=0.00..175.00 rows=10000 width=8)
         ->  Hash  (cost=200.00..200.00 rows=1 width=8)
               ->  Seq Scan on hint_t7 t1  (cost=0.00..200.00 rows=1 width=8)
                     Filter: (f1 > 9999)
(7 rows)
 
postgres=# explain select /*+use_nl(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>999 ; 
                                   QUERY PLAN                                    
---------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.00..1350547.50 rows=9001 width=16)
   ->  Nested Loop  (cost=0.00..1350547.50 rows=9001 width=16)
         Join Filter: (t.f1 = t1.f1)
         ->  Seq Scan on hint_t7 t1  (cost=0.00..175.00 rows=10000 width=8)
         ->  Materialize  (cost=0.00..245.00 rows=9001 width=8)
               ->  Seq Scan on hint_t6 t  (cost=0.00..200.00 rows=9001 width=8)
                     Filter: (f1 > 999)
(7 rows)
 
postgres=#
```
#### 强制走mergejoin
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# create index hint_t6_f1_idx on hint_t6(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t6;
VACUUM
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE 
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# create index hint_t7_f1_idx on hint_t7(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t7;
VACUUM
postgres=#
 
postgres=# explain select * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
                                         QUERY PLAN                                          
---------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.32..8.37 rows=1 width=16)
   ->  Nested Loop  (cost=0.32..8.37 rows=1 width=16)
         ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.16..4.18 rows=1 width=8)
               Index Cond: (f1 > 9999)
         ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.16..4.18 rows=1 width=8)
               Index Cond: (f1 = t.f1)
(6 rows)
 
postgres=# explain select /*+use_merge(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
                                            QUERY PLAN                                             
---------------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.32..257.35 rows=1 width=16)
   ->  Merge Join  (cost=0.32..257.35 rows=1 width=16)
         Merge Cond: (t.f1 = t1.f1)
         ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.16..4.18 rows=1 width=8)
               Index Cond: (f1 > 9999)
         ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.16..228.16 rows=10000 width=8)
(6 rows)
 
postgres=#
```
#### 强制走hashjoin
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# create index hint_t6_f1_idx on hint_t6(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t6;
VACUUM
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# create index hint_t7_f1_idx on hint_t7(f1);      
CREATE INDEX
postgres=# vacuum ANALYZE hint_t7;
VACUUM
postgres=#
 
postgres=#  explain select * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
                                         QUERY PLAN                                          
---------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=0.32..8.37 rows=1 width=16)
   ->  Nested Loop  (cost=0.32..8.37 rows=1 width=16)
         ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.16..4.18 rows=1 width=8)
               Index Cond: (f1 > 9999)
         ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.16..4.18 rows=1 width=8)
               Index Cond: (f1 = t.f1)
(6 rows)
 
postgres=# explain select /*+use_hash(t,t1) */  * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
                                            QUERY PLAN                                            
--------------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001)  (cost=4.19..216.70 rows=1 width=16)
   ->  Hash Join  (cost=4.19..216.70 rows=1 width=16)
         Hash Cond: (t1.f1 = t.f1)
         ->  Seq Scan on hint_t7 t1  (cost=0.00..175.00 rows=10000 width=8)
         ->  Hash  (cost=4.18..4.18 rows=1 width=8)
               ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.16..4.18 rows=1 width=8)
                     Index Cond: (f1 > 9999)
(7 rows)
```
#### 并行执行
```
postgres=# create table hint_t3(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t3 select t as f1,t as f2 from generate_series(1,1000000) as t;    
INSERT 0 1000000
postgres=# vacuum ANALYZE hint_t3;
VACUUM
postgres=#
 
postgres=#  explain select count(1) from hint_t3;                                      
                                     QUERY PLAN                                      
-------------------------------------------------------------------------------------
 Finalize Aggregate  (cost=20020.01..20020.02 rows=1 width=8)
   ->  Remote Subquery Scan on all (dn001)  (cost=20020.00..20020.01 rows=1 width=0)
         ->  Partial Aggregate  (cost=19920.00..19920.01 rows=1 width=8)
               ->  Seq Scan on hint_t3  (cost=0.00..17420.00 rows=1000000 width=0)
(4 rows)
 
postgres=# explain select /*+parallel(hint_t3 2) */ count(1) from hint_t3;
                                           QUERY PLAN                                            
-------------------------------------------------------------------------------------------------
 Parallel Finalize Aggregate  (cost=13728.35..13728.36 rows=1 width=8)
   ->  Parallel Remote Subquery Scan on all (dn001)  (cost=13728.33..13728.35 rows=1 width=0)
         ->  Gather  (cost=13628.33..13628.34 rows=1 width=8)
               Workers Planned: 2
               ->  Partial Aggregate  (cost=12628.33..12628.34 rows=1 width=8)
                     ->  Parallel Seq Scan on hint_t3  (cost=0.00..11586.67 rows=416667 width=0)
(6 rows)
 
postgres=#
```
## dml操作加强
### select支持别名不用as修饰
```
postgres=# select * from student as st where st.f1=1;
 f1 | f2 
----+----
  1 |  2
(1 row)

postgres=# select * from student st where st.f1=1;   
 f1 | f2 
----+----
  1 |  2
```
### update支持别名
```
postgres=# create table student(f1 int,f2 int);
CREATE TABLE
postgres=# insert into student  values(1,1);
INSERT 0 1
postgres=# update student st set st.f2=2 where f1=1;
UPDATE 1
postgres=# select * from student ;
 f1 | f2 
----+----
  1 |  2
```