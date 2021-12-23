## TDSQL PostgreSQL相关开发规范

### 命名规范

1. DB object: database， schema， table， column， view， index， sequence， function， trigger等名称：

   - 建议使用小写字母、数字、下划线的组合。

   -   建议不使用双引号即"包围，除非必须包含大写字母或空格等特殊字符。

   -   长度不能超过63个字符。

   -   不建议以pg_开头或者pgxc_（避免与系统DB object混淆），不建议以数字开头。

   -   禁止使用 SQL 关键字例如 type， order 等。

2. table能包含的column数目，根据字段类型的不同，数目在 250 到 1600 之间；

3. 临时或备份的DB object:table，view 等，建议加上日期， 如dba_ops.b2c_product_summay_2014_07_12 (其中dba_ops 为DBA专用schema)；

4. index命名规则为: 普通索引为 表名_列名_idx，唯一索引表名_列名_uidx，如student_name_idx，student_id_uidx。

### COLUMN设计

1. 建议能用数值类型的，就不用字符类型；


2. 建议能用varchar(N) 就不用char(N)，以利于节省存储空间；
3. 建议能用varchar(N) 就不用text，varchar；
4. 建议使用default NULL，而不用default ''，以节省存储空间；
5. 建议如有国际货业务的话，使用timestamp with time zone(timestamptz)，而不用timestamp without time zone，避免时间函数在对于不同时区的时间点返回值不同，也为业务国际化扫清障碍；
6. 建议使用NUMERIC(precision， scale)来存储货币金额和其它要求精确计算的数值， 而不建议使用real， double precision；

### Constraints 设计

1. 建议每个table都使用shard key做为主键或者唯一索引。
2. 建议建表时一步到位把主键或者唯一索引也一起建立。
3. 注意，非shard key不可以建立primary key或者 unique index。

### Index 设计

1. TDSQL PostgreSQL提供的index类型: B-tree， Hash， GiST (Generalized Search Tree)， SP-GiST (space-partitioned GiST)， GIN (Generalized Inverted Index)， BRIN (Block Range Index)，目前不建议使用Hash，通常情况下使用B-tree；

2. 建议create 或 drop index 时，加 CONCURRENTLY参数，这是个好习惯，达到与写入数据并发的效果；

3. 建议对于频繁update， delete的包含于index 定义中的column的table， 用create index CONCURRENTLY ， drop index CONCURRENTLY 的方式进行维护其对应index；

4. 建议用unique index 代替unique constraints，便于后续维护；

5. 建议对where 中带多个字段and条件的高频 query，参考数据分布情况，建多个字段的联合index；

6. 建议对固定条件的（一般有特定业务含义）且选择比好（数据占比低）的query，建带where的Partial Indexes；

   > select * from test where status=1 and col=?; -- 其中status=1为固定的条件
   >
   > create index on test (col) where status=1;

7. 建议对经常使用表达式作为查询条件的query，可以使用表达式或函数索引加速query；

   > select * from test where exp(xxx);
   >
   > create index on test ( exp(xxx) );   

8. 建议不要建过多index，一般不要超过6个，核心table（产品，订单）可适当增加index个数。

### 关于NULL

1. NULL 的判断：IS NULL ，IS NOT NULL；  

2.  注意boolean 类型取值 true，false， NULL；

3. 小心NOT IN 集合中带有NULL元素；

 ```
 postgres=# select * from tdsql_pg;
  id |  nickname   
 ----+---------------
  1 | hello tdsql_pg
  2 | tdsql_pg好
  3 | tdsql_pg好
  4 | tdsql_pg default
 (4 rows)
 
 postgres=# select * from tdsql_pg where id not in (null);
  id | nickname 
 ----+----------
 (0 rows)
 ```



4. 建议对字符串型NULL值处理后，进行 || 操作；

 ```
 postgres=# select id，nickname from tdsql_pg limit 1;
  id |  nickname  
 ----+-------------
  1 | hello tdsql_pg
 (1 row)
  
 postgres=# select id，nickname||null from tdsql_pg limit 1;
  id | ?column? 
 ----+----------
  1 | 
 (1 row)
 postgres=# select id，nickname||coalesce(null，'') from tdsql_pg limit 1;
  id |  ?column?  
 ----+-------------
  1 | hello tdsql_pg
 (1 row)
 ```

5. 建议使用count(1) 或count(*) 来统计行数，而不建议使用count(col) 来统计行数，因为NULL值不会计入；

> 注意: count(多列列名)时，多列列名必须使用括号，例如count( (col1，col2，col3) ); 注意多列的count，即使所有列都为NULL，该行也被计数，所以效果与count(*) 一致；

```
postgres=# select * from tdsql_pg ;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 5 | 
 3 | tdsql_pg好
 4 | tdsql_pg default
(5 rows)

postgres=# select count(1) from tdsql_pg;
 count 
\-------
   5
(1 row)
 
postgres=# select count(*) from tdsql_pg; 
 count 
\-------
   5
(1 row)   
 
postgres=# select count(nickname) from tdsql_pg;     
 count 
\-------
   4
(1 row)
 
postgres=# select count((id，nickname)) from tdsql_pg;  
 count 
\-------
   5
(1 row)
```

6. count(distinct col) 计算某列的非NULL不重复数量，NULL不被计数；

> 注意: count(distinct (col1，col2，...) ) 计算多列的唯一值时，NULL会被计数，同时NULL与NULL会被认为是相同的；

```
postgres=# select count(distinct nickname) from tdsql_pg;
 count 
\-------
   3
(1 row)
 
postgres=# select count(distinct (id，nickname)) from tdsql_pg;
 count 
\-------
   5
(1 row)
 
```

7. 两个null的对比方法

```
postgres=# select null is not  distinct from null as tdsql_pgnull;    
 tdsql_pgnull 
\-----------
 t
(1 row)
```



### 开发相关规范

- **建议对DB object 尤其是COLUMN 加COMMENT，便于后续新人了解业务及维护；**

注释前后的数据表可读性对比，有注释的一看就明白

```
postgres=# \d+ tdsql_pg_main
           Table "public.tdsql_pg_main"
 Column |  Type  | Modifiers | Storage  | Stats target | Description 
--------+---------+-----------+----------+--------------+-------------
 id   | integer |      | plain   |        | 
 mc   | text   |      | extended |        | 
Indexes:
  "tdsql_pg_main_id_uidx" UNIQUE， btree (id)
Has OIDs: no
Distribute By SHARD(id)
    Location Nodes: ALL DATANODES
 
postgres=# comment on column tdsql_pg_main.id is 'id号';
COMMENT
postgres=# comment on column tdsql_pg_main.mc is '产品名称';
COMMENT
postgres=# \d+ tdsql_pg_main
           Table "public.tdsql_pg_main"
 Column |  Type  | Modifiers | Storage  | Stats target | Description 
--------+---------+-----------+----------+--------------+-------------
 id   | integer |      | plain   |        | id号
 mc   | text   |      | extended |        | 产品名称
Indexes:
  "tdsql_pg_main_id_uidx" UNIQUE， btree (id)
Has OIDs: no
Distribute By SHARD(id)
    Location Nodes: ALL DATANODES
```

- **建议非必须时避免select *，只取所需字段，以减少包括不限于网络带宽消耗**

 ```
 postgres=#  explain (verbose) select * from tdsql_pg_main where id=1;
                      QUERY PLAN                      
 ---------------------------------------------------------------------------------------------
  Index Scan using tdsql_pg_main_id_uidx on public.tdsql_pg_main  (cost=0.15..8.17 rows=1 width=36)
   Output: id， mc
   Index Cond: (tdsql_pg_main.id = 1)
 (3 rows)
  
 postgres=#  explain (verbose) select tableoid from tdsql_pg_main where id=1;  
                      QUERY PLAN                     
 --------------------------------------------------------------------------------------------
  Index Scan using tdsql_pg_main_id_uidx on public.tdsql_pg_main  (cost=0.15..8.17 rows=1 width=4)
   Output: tableoid
   Index Cond: (tdsql_pg_main.id = 1)
 (3 rows)
 ```

*是返回36个字符，而另一个一条记录只能4个字段的长度

 

-  **建议update 时尽量做 <> 判断，比如update table_a set column_b = c where column_b <> c；**


 ```
 postgres=# update tdsql_pg_main set mc='tdsql_pg' ;
 UPDATE 1
 postgres=# select xmin，* from tdsql_pg_main;
  xmin | id |  mc  
 ------+----+-------
  2562 |  1 | tdsql_pg
 (1 row)
  
 postgres=# update tdsql_pg_main set mc='tdsql_pg' ;
 UPDATE 1
 postgres=# select xmin，* from tdsql_pg_main;   
  xmin | id |  mc  
 ------+----+-------
  2564 |  1 | tdsql_pg
 (1 row)
  
 postgres=# update tdsql_pg_main set mc='tdsql_pg' where mc!='tdsql_pg';
 UPDATE 0
 postgres=# select xmin，* from tdsql_pg_main;           
  xmin | id |  mc  
 ------+----+-------
  2564 |  1 | tdsql_pg
 (1 row)
 ```

上面的效果是一样的，但带条件的更新不会产生一个新的版本记录，不需要系统执行vacuum回收垃圾数据。

 

- **建议将单个事务的多条SQL操作，分解、拆分，或者不放在一个事务里，让每个事务的粒度尽可能小，尽量lock少的资源，避免lock 、dead lock的产生；**



\#sesseion1把所有数据都更新而不提交，一下子锁了2000千万条记录

```
postgres=# begin;
BEGIN
postgres=# update tdsql_pg_main set mc='tdsql_pg_1.3';
UPDATE 200000000
```



\#sesseion2 等待

```
postgres=# update tdsql_pg_main set mc='tdsql_pg_1.4'  where id=1;
```



\#sesseion3 等待

```
postgres=# update tdsql_pg_main set mc='tdsql_pg_1.5'  where id=2;
```

如果#sesseion1分布批更新的话，如下所示

```
postgres=# begin;
BEGIN
postgres=# update tdsql_pg_main set mc='tdsql_pg_1.3' where id>0 and id <=100000;
UPDATE 100000
postgres=#COMMIT;
 
postgres=# begin;
BEGIN
postgres=# update tdsql_pg_main set mc='tdsql_pg_1.3' where id>100000 and id <=200000;
UPDATE 100000
postgres=#COMMIT;
```

则session2和session3中就能部分提前完成，这样可以避免大量的锁等待和出现大量的session占用系统资源，在做全表更新时请使用这种方法来执行

 

- **建议 大批量的数据入库时， 使用copy ，不建议使用insert，以提高写入速度；**

 ```
 postgres=# insert into tdsql_pg_main select t，'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' from generate_series(1，100000) as t;
 INSERT 0 100000
 Time: 9511.755 ms
  
 postgres=# copy  tdsql_pg_main to '/data/pgxz/tdsql_pg_main.txt';    
 COPY 100002
 Time: 179.428 ms
  
 postgres=# copy  tdsql_pg_main from  '/data/pgxz/tdsql_pg_main.txt';
 COPY 100002
 Time: 1625.803 ms
 postgres=# 
 ```

性能相差5倍

 

- **建议对报表类的或生成基础数据的查询，使用物化视图(MATERIALIZED VIEW)定期固化数据快照， 避免对多表（尤其多写频繁的表）重复跑相同的查询，且物化视图支持 REFRESH MATERIALIZED VIEW CONCURRENTLY， 支持并发更新；**

如有一个程序需要不断查询tdsql_pg_main的总记录数，那么我们这样做

```
postgres=# select count(1) from tdsql_pg_main;
 count  
--------
 200004
(1 row)
 
Time: 27.948 ms
 
postgres=# create MATERIALIZED VIEW tdsql_pg_main_count as select count(1) as num from tdsql_pg_main;
SELECT 1
Time: 322.372 ms
postgres=# select num from  tdsql_pg_main_count ;
 num  
--------
 200004
(1 row)
 
Time: 0.421 ms
```

性能提高上百倍



有数据变化时刷新方法

```
postgres=#  copy  tdsql_pg_main from  '/data/pgxz/tdsql_pg_main.txt';
COPY 100002
Time: 1201.774 ms
postgres=# select count(1) from tdsql_pg_main;
 count  
--------
 300006
(1 row)
 
Time: 23.164 ms
postgres=# REFRESH MATERIALIZED VIEW tdsql_pg_main_count;     
REFRESH MATERIALIZED VIEW
Time: 49.486 ms
postgres=# select num from tdsql_pg_main_count ;
 num  
--------
 300006
(1 row)
 
Time: 0.301 ms
```



-  **建议复杂的统计查询可以尝试窗口函数** 


请参考高级sql语句编写中窗口函数的用法

 

- **两表join时尽量的使用分布key进行join**

所似在建立业务的主表，明细表时，就需要使用他们的关联键来做分布键，如下所示

 ```
 [pgxz@VM_0_29_centos pgxz]$ psql -p 15001        
 psql (PostgreSQL 10 (tdsql_pg 2.01))
 Type "help" for help.
  
 postgres=# create table tdsql_pg_main(id integer，mc text) distribute by shard(id);
 CREATE TABLE
 postgres=# create table tdsql_pg_detail(id integer，tdsql_pg_main_id integer，mc text) distribute by shard(tdsql_pg_main_id);  
 CREATE TABLE
 postgres=# explain select tdsql_pg_detail.* from tdsql_pg_main，tdsql_pg_detail where tdsql_pg_main.id=tdsql_pg_detail.tdsql_pg_main_id;    
                  QUERY PLAN                 
 ----------------------------------------------------------------------------
  Data Node Scan on "__REMOTE_FQS_QUERY__"  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001， dn002
 (2 rows)
  
 postgres=# explain (verbose) select tdsql_pg_detail.* from tdsql_pg_main，tdsql_pg_detail where tdsql_pg_main.id=tdsql_pg_detail.tdsql_pg_main_id; 
                                            QUERY PLAN                                           
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Data Node Scan on "__REMOTE_FQS_QUERY__"  (cost=0.00..0.00 rows=0 width=0)
   Output: tdsql_pg_detail.id， tdsql_pg_detail.tdsql_pg_main_id， tdsql_pg_detail.mc
   Node/s: dn001， dn002
   Remote query: SELECT tdsql_pg_detail.id， tdsql_pg_detail.tdsql_pg_main_id， tdsql_pg_detail.mc FROM public.tdsql_pg_main， public.tdsql_pg_detail WHERE (tdsql_pg_main.id = tdsql_pg_detail.tdsql_pg_main_id)
 (4 rows)
  
 postgres=# 
 ```



-  **分布键用唯一索引代替主键**


 ```
 postgres=# create unique index tdsql_pg_main_id_uidx on tdsql_pg_main using btree(id);
 CREATE INDEX
 ```

因为唯一索引后期的维护成本比主键要低很多

 

- **分布键无法建立唯一索引则要建立普通索引，提高查询的效率**

 ```
 postgres=# create index tdsql_pg_detail_tdsql_pg_main_id_idx on tdsql_pg_detail using btree(tdsql_pg_main_id);          
 CREATE INDEX
 ```

这样两表在join查询时返回少量数据时的效率才会高。

 

- **不要对字段建立外键**

目前TDSQL PostgreSQL还不支持多dn外键约束

