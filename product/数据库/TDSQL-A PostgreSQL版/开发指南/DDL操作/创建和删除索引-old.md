
## 普通索引
```
postgres=# create index t_appoint_id_idx on t_appoint_col using btree(id);    
CREATE INDEX
```

## 唯一索引
创建唯一索引
```
postgres=# create unique index t_first_col_share_id_uidx on t_first_col_share using btree(id);
CREATE INDEX
```

非 shard key 字段不能建立唯一索引
```
postgres=# create unique index t_first_col_share_nickname_uidx on t_first_col_share using btree(nickname);
ERROR:  Unique index of partitioned table must contain the hash/modulo distribution column.
```

## 表达式索引
```
postgres=# create table t_upper(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# create index t_upper_mc on t_upper(mc);       
CREATE INDEX

postgres=# insert into t_upper select t,md5(t::text) from generate_series(1,10000) as t; 
INSERT 0 10000
postgres=# analyze t_upper;
ANALYZE

postgres=# explain select * from t_upper where upper(mc)=md5('1');
                               QUERY PLAN                               
\------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Seq Scan on t_upper  (cost=0.00..135.58 rows=25 width=37)
         Filter: (upper(mc) = 'c4ca4238a0b923820dcc509a6f75849b'::text)
(4 rows)

postgres=# create index t_upper_mc on t_upper(upper(mc));       
CREATE INDEX
postgres=# explain select * from t_upper where upper(mc)=md5('1');
                                    QUERY PLAN                                    
\----------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on t_upper  (cost=2.48..32.43 rows=25 width=37)
         Recheck Cond: (upper(mc) = 'c4ca4238a0b923820dcc509a6f75849b'::text)
         ->  Bitmap Index Scan on t_upper_mc  (cost=0.00..2.47 rows=25 width=0)
               Index Cond: (upper(mc) = 'c4ca4238a0b923820dcc509a6f75849b'::text)
(6 rows)
```


## 条件索引
```
postgres=# create table t_sex(id int,sex text) ;
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# create index t_sex_sex_idx on t_sex (sex);
CREATE INDEX
postgres=# insert into t_sex select t,'男' from generate_series(1,1000000) as t;                      
INSERT 0 1000000
postgres=# insert into t_sex select t,'女' from generate_series(1,100) as t;                     
INSERT 0 100
postgres=# analyze t_sex ;
ANALYZE
postgres=# 

postgres=# explain  select * from t_sex where sex ='女';           
                                    QUERY PLAN                                    
\----------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Index Scan using t_sex_sex_idx on t_sex  (cost=0.42..5.81 rows=67 width=8)
         Index Cond: (sex = '女'::text)
(4 rows)

\#索引对于条件为男的情况下无效

postgres=# explain  select * from t_sex where sex ='男';     
                            QUERY PLAN                             
\-------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Seq Scan on t_sex  (cost=0.00..9977.58 rows=500539 width=8)
         Filter: (sex = '男'::text)
(4 rows)

\#连接dn节点查看索引点用空间大，而且度数也高

[tdapg@VM_0_37_centos shell]$ psql -p 11010
psql (PostgreSQL 10.0 T)
Type "help" for help.

postgres=# \di+
                                    List of relations
 Schema |     Name      | Type  | Owner |  Table  | Size  | Allocated Size | Description 
--------+---------------+-------+-------+---------+-------+----------------+-------------
 dbadmin  | t_sex_sex_idx | index | dbadmin | t_sex   | 14 MB | 14 MB          | 
 dbadmin  | t_upper_mc    | index | dbadmin | t_upper | 14 MB | 14 MB          | 
(2 rows)

postgres=# \q

[tdapg@VM_0_37_centos shell]$ psql 
psql (PostgreSQL 10.0 TBase V3)
Type "help" for help.

postgres=# drop index t_sex_sex_idx;
DROP INDEX
postgres=#  create index t_sex_sex_idx on t_sex (sex) where sex='女';  
CREATE INDEX
postgres=# analyze t_sex;
ANALYZE
postgres=# explain  select * from t_sex where sex ='女';       
                                    QUERY PLAN                                    
\----------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Index Scan using t_sex_sex_idx on t_sex  (cost=0.14..6.69 rows=33 width=8)
(3 rows)

postgres=# explain  select * from t_sex where sex ='男';     
                            QUERY PLAN                             
\-------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Seq Scan on t_sex  (cost=0.00..9977.58 rows=500573 width=8)
         Filter: (sex = '男'::text)
(4 rows)

postgres=# \q
[tdapg@VM_0_37_centos shell]$ psql -p 11010
psql (PostgreSQL 10.0 TBase V3)
Type "help" for help.

postgres=# \di+
                                    List of relations
 Schema |     Name      | Type  | Owner |  Table  | Size  | Allocated Size | Description 
--------+---------------+-------+-------+---------+-------+----------------+-------------
 dbadmin  | t_sex_sex_idx | index | dbadmin | t_sex   | 16 kB | 16 kB          | 
 dbadmin  | t_upper_mc    | index | dbadmin | t_upper | 14 MB | 14 MB          | 
(2 rows)

postgres=# 
```

## gist 索引
暂不支持
```

## gin 索引
暂不支持

### pg_trgm 索引
```
postgres=# drop index t_trgm_trgm_idx;
DROP INDEX
Time: 55.954 ms
postgres=# create index t_trgm_trgm_idx on t_trgm using gin(trgm gin_trgm_ops);
CREATE INDEX
```

###  jsonb 索引
```
postgres=# create table t_jsonb(id int,f_jsonb jsonb);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# create index t_jsonb_f_jsonb_idx on t_jsonb using gin(f_jsonb);
CREATE INDEX
```

### 数组索引
```
postgres=# create table t_array(id int, mc text[]); 
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_array select t,('{'||md5(t::text)||'}')::text[] from generate_series(1,1000000) as t;     
INSERT 0 1000000
postgres=# analyze; 
ANALYZE
postgres=# \timing 
Timing is on.

postgres=# explain select * from t_array where mc @> ('{'||md5('1')||'}')::text[];
                                      QUERY PLAN                                       
\---------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Gather  (cost=1000.00..12060.25 rows=2503 width=61)
         Workers Planned: 2
         ->  Parallel Seq Scan on t_array  (cost=0.00..10809.95 rows=1043 width=61)
              Filter: (mc @> ('{c4ca4238a0b923820dcc509a6f75849b}'::cstring)::text[])
(6 rows)

Time: 4.105 ms
postgres=# select * from t_array where mc @> ('{'||md5('1')||'}')::text[];        
 id |                 mc                 
----+------------------------------------
  1 | {c4ca4238a0b923820dcc509a6f75849b}
(1 row)

Time: 494.371 ms

postgres=# create index t_array_mc_idx on t_array using gin(mc);
CREATE INDEX
Time: 8195.387 ms (00:08.195)
postgres=# explain select * from t_array where mc @> ('{'||md5('1')||'}')::text[];
                                        QUERY PLAN                                         
\-------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on t_array  (cost=29.40..3172.64 rows=2503 width=61)
         Recheck Cond: (mc @> ('{c4ca4238a0b923820dcc509a6f75849b}'::cstring)::text[])
         ->  Bitmap Index Scan on t_array_mc_idx  (cost=0.00..28.78 rows=2503 width=0)
               Index Cond: (mc @> ('{c4ca4238a0b923820dcc509a6f75849b}'::cstring)::text[])
(6 rows)

Time: 1.716 ms
postgres=# select * from t_array where mc @> ('{'||md5('1')||'}')::text[];
 id |                 mc                 
----+------------------------------------
  1 | {c4ca4238a0b923820dcc509a6f75849b}
(1 row)

Time: 2.980 ms

```
 
### Btree_gin 任意字段索引
```
postgres=# create table gin_mul(f1 int, f2 int, f3 timestamp, f4 text, f5 numeric, f6 text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# 

postgres=# insert into gin_mul select random()*5000, random()*6000, now()+((30000-60000*random())||' sec')::interval , md5(random()::text), round((random()*100000)::numeric,2), md5(random()::text) from generate_series(1,1000000);      
INSERT 0 1000000

postgres=# create extension btree_gin;
CREATE EXTENSION

postgres=# create index gin_mul_gin_idx on gin_mul using gin(f1,f2,f3,f4,f5,f6);       
CREATE INDEX
\#单字段查询

postgres=# explain select * from gin_mul where f1=10;
                                      QUERY PLAN                                       
\---------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn002
   ->  Bitmap Heap Scan on gin_mul  (cost=11.51..369.70 rows=194 width=90)
         Recheck Cond: (f1 = 10)
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..11.46 rows=194 width=0)
               Index Cond: (f1 = 10)
(6 rows)

postgres=# 

postgres=# explain select * from gin_mul where f3='2019-02-18 23:01:01'; 
                                     QUERY PLAN                                      
\-------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on gin_mul  (cost=10.01..12.02 rows=1 width=90)
         Recheck Cond: (f3 = '2019-02-18 23:01:01'::timestamp without time zone)
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..10.01 rows=1 width=0)
               Index Cond: (f3 = '2019-02-18 23:01:01'::timestamp without time zone)
(6 rows)

postgres=# explain select * from gin_mul where f4='2364d9969c8b66402c9b7d17a6d5b7d3';                 
                                     QUERY PLAN                                      
\-------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on gin_mul  (cost=10.01..12.02 rows=1 width=90)
         Recheck Cond: (f4 = '2364d9969c8b66402c9b7d17a6d5b7d3'::text)
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..10.01 rows=1 width=0)
               Index Cond: (f4 = '2364d9969c8b66402c9b7d17a6d5b7d3'::text)
(6 rows)

postgres=# explain select * from gin_mul where f5=85375.30;                                    
                                     QUERY PLAN                                      
\-------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on gin_mul  (cost=10.01..12.02 rows=1 width=90)
         Recheck Cond: (f5 = 85375.30)
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..10.01 rows=1 width=0)
               Index Cond: (f5 = 85375.30)
(6 rows)

\#二个字段组合
postgres=# explain select * from gin_mul where f1=2 and f3='2019-02-18 16:59:52.872523';          
                                                QUERY PLAN                                                 
\-----------------------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001
   ->  Bitmap Heap Scan on gin_mul  (cost=18.00..20.02 rows=1 width=90)
         Recheck Cond: ((f1 = 2) AND (f3 = '2019-02-18 16:59:52.872523'::timestamp without time zone))
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..18.00 rows=1 width=0)
               Index Cond: ((f1 = 2) AND (f3 = '2019-02-18 16:59:52.872523'::timestamp without time zone))
(6 rows)

\#三字段组合查询
postgres=# explain select * from gin_mul where f1=2 and f3='2019-02-18 16:59:52.872523' and f6='fa627dc16c2bd026150afa0453a0991d'; 
                                                                          QUERY PLAN                                                                           
\---------------------------------------------------------------------------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001
   ->  Bitmap Heap Scan on gin_mul  (cost=26.00..28.02 rows=1 width=90)
         Recheck Cond: ((f1 = 2) AND (f3 = '2019-02-18 16:59:52.872523'::timestamp without time zone) AND (f6 = 'fa627dc16c2bd026150afa0453a0991d'::text))
         ->  Bitmap Index Scan on gin_mul_gin_idx  (cost=0.00..26.00 rows=1 width=0)
               Index Cond: ((f1 = 2) AND (f3 = '2019-02-18 16:59:52.872523'::timestamp without time zone) AND (f6 = 'fa627dc16c2bd026150afa0453a0991d'::text))
(6 rows)

postgres=# 
```

## 多字段索引
```
postgres=# create table t_mul_idx (f1 int,f2 int,f3 int,f4 int);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
Time: 308.109 ms
postgres=# create index t_mul_idx_idx on t_mul_idx(f1,f2,f3); 
CREATE INDEX
Time: 108.734 ms
```

### 多字段使用注意事项
#### or 查询条件 bitmap scan 最多支持两个不同字段条件
```
postgres=# insert into t_mul_idx select t,t,t,t from generate_series(1,1000000) as t;
INSERT 0 1000000
postgres=# analyze ;
ANALYZE

postgres=# explain select * from t_mul_idx where f1=1 or f2=2 ;        
                                        QUERY PLAN                                         
\-------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on t_mul_idx  (cost=7617.08..7621.07 rows=2 width=16)
         Recheck Cond: ((f1 = 1) OR (f2 = 2))
         ->  BitmapOr  (cost=7617.08..7617.08 rows=2 width=0)
               ->  Bitmap Index Scan on t_mul_idx_idx  (cost=0.00..2.43 rows=1 width=0)
                     Index Cond: (f1 = 1)
               ->  Bitmap Index Scan on t_mul_idx_idx  (cost=0.00..7614.65 rows=1 width=0)
                     Index Cond: (f2 = 2)
(9 rows)

Time: 3.655 ms
postgres=# explain select * from t_mul_idx where f1=1 or f2=2 or f1=3 ;   
                                        QUERY PLAN                                         
\-------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Bitmap Heap Scan on t_mul_idx  (cost=7619.51..7625.49 rows=3 width=16)
         Recheck Cond: ((f1 = 1) OR (f2 = 2) OR (f1 = 3))
         ->  BitmapOr  (cost=7619.51..7619.51 rows=3 width=0)
               ->  Bitmap Index Scan on t_mul_idx_idx  (cost=0.00..2.43 rows=1 width=0)
                     Index Cond: (f1 = 1)
               ->  Bitmap Index Scan on t_mul_idx_idx  (cost=0.00..7614.65 rows=1 width=0)
                     Index Cond: (f2 = 2)
               ->  Bitmap Index Scan on t_mul_idx_idx  (cost=0.00..2.43 rows=1 width=0)
                     Index Cond: (f1 = 3)
(11 rows)

Time: 3.429 ms
postgres=# explain select * from t_mul_idx where f1=1 or f2=2 or f3=3 ;  
                             QUERY PLAN                             
\--------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Seq Scan on t_mul_idx  (cost=0.00..12979.87 rows=3 width=16)
         Filter: ((f1 = 1) OR (f2 = 2) OR (f3 = 3))
(4 rows)

Time: 1.679 ms
```
 

#### 如果返回字段全部在索引文件中，则只需要扫描索引，io 开销会更少
```
postgres=# explain select f1,f2,f3 from t_mul_idx where f1=1 ;        
                                        QUERY PLAN                                         
\-------------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001
   ->  Index Only Scan using t_mul_idx_idx on t_mul_idx  (cost=0.42..4.44 rows=1 width=12)
         Index Cond: (f1 = 1)
(4 rows)

Time: 1.564 ms
```
 

#### 更新性能比单字段多索引文件要好
多字段
```
postgres=# insert into t_simple_idx select t,t,t,t from generate_series(1,1000000) as t;   
INSERT 0 1000000
Time: 7143.754 ms (00:07.144)
```

单字段
```
postgres=# insert into t_mul_idx select t,t,t,t from generate_series(1,1000000) as t;         
INSERT 0 1000000
Time: 4034.208 ms (00:04.034)
```

#### 多字段索引走非第一字段查询时性能比独立的单字段差
多字段
```
postgres=# select * from t_mul_idx where f1=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 1.769 ms
postgres=# select * from t_mul_idx where f2=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 25.423 ms
postgres=# select * from t_mul_idx where f3=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 27.791 ms
```
 
独立字段
```
postgres=# select * from t_simple_idx where f1=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 1.530 ms
postgres=# select * from t_simple_idx where f2=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 2.315 ms
postgres=# select * from t_simple_idx where f3=1;
 f1 | f2 | f3 | f4 
----+----+----+----
  1 |  1 |  1 |  1
(1 row)

Time: 2.390 ms
```
 

## 删除索引
```
postgres=# drop index t_appoint_id_idx;
DROP INDEX
```

