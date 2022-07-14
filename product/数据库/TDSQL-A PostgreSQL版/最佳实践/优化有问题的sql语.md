
## 查看是否为分布键查询
```
postgres=# explain select * from tdapg_1 where f1=1;        
                                   QUERY PLAN                                   
\--------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Gather  (cost=1000.00..7827.20 rows=1 width=14)
         Workers Planned: 2
         ->  Parallel Seq Scan on tdapg_1  (cost=0.00..6827.10 rows=1 width=14)
               Filter: (f1 = 1)
(6 rows) 

postgres=# explain select * from tdapg_1 where f2=1;
                                   QUERY PLAN                                   
\--------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001
   ->  Gather  (cost=1000.00..7827.20 rows=1 width=14)
         Workers Planned: 2
         ->  Parallel Seq Scan on tdapg_1  (cost=0.00..6827.10 rows=1 width=14)
               Filter: (f2 = 1)
(6 rows)
```
如上，第一个查询为非分布键查询，需要发往所有节点，这样最慢的节点决定了整个业务的速度，需要保持所有节点的响应性能一致，如第二个查询所示，业务设计查询时尽可能带上分布键。

## 查看是否使用索引
```
postgres=# create index tdapg_2_f2_idx on tdapg_2(f2); 
CREATE INDEX
postgres=# explain select * from tdapg_2 where f2=1;
                                     QUERY PLAN                                      
\-------------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Index Scan using tdapg_2_f2_idx on tdapg_2  (cost=0.42..4.44 rows=1 width=14)
         Index Cond: (f2 = 1)
(4 rows)

postgres=# explain select * from tdapg_2 where f3='1';
                                   QUERY PLAN                                   
\--------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Gather  (cost=1000.00..7827.20 rows=1 width=14)
         Workers Planned: 2
         ->  Parallel Seq Scan on tdapg_2  (cost=0.00..6827.10 rows=1 width=14)
               Filter: (f3 = '1'::text)
(6 rows)

postgres=# 
``` 
第一个查询使用了索引，第二个没有使用索引，通常情况下，使用索引可以加速查询速度，但索引也会增加更新的开销。

## 查看是否为分布 key join
```
postgres=# explain  select tdapg_1.* from tdapg_1,tdapg_2 where tdapg_1.f1=tdapg_2.f1 ;           
                                           QUERY PLAN                                           
\------------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001,dn002)  (cost=29.80..186.32 rows=3872 width=40)
   ->  Hash Join  (cost=29.80..186.32 rows=3872 width=40)
         Hash Cond: (tdapg_1.f1 = tdapg_2.f1)
         ->  Remote Subquery Scan on all (dn001,dn002)  (cost=100.00..158.40 rows=880 width=40)
               Distribute results by S: f1
               ->  Seq Scan on tdapg_1  (cost=0.00..18.80 rows=880 width=40)
         ->  Hash  (cost=18.80..18.80 rows=880 width=4)
               ->  Seq Scan on tdapg_2  (cost=0.00..18.80 rows=880 width=4)
(8 rows) 

postgres=# explain  select tdapg_1.* from tdapg_1,tdapg_2 where tdapg_1.f2=tdapg_2.f1 ;   
                                   QUERY PLAN                                    
\---------------------------------------------------------------------------------
 Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
   Node/s: dn001, dn002
   ->  Hash Join  (cost=18904.69..46257.08 rows=500564 width=14)
         Hash Cond: (tdapg_1.f2 = tdapg_2.f1)
         ->  Seq Scan on tdapg_1  (cost=0.00..9225.64 rows=500564 width=14)
         ->  Hash  (cost=9225.64..9225.64 rows=500564 width=4)
               ->  Seq Scan on tdapg_2  (cost=0.00..9225.64 rows=500564 width=4)
(7 rows)
```
第一个查询需要数据重分布，而第二个不需要，分布键 join 查询性能会更高。

## 查看 join 发生的节点
```
postgres=#  explain  select tdapg_1.* from tdapg_1,tdapg_2 where tdapg_1.f1=tdapg_2.f1 ;    
                                          QUERY PLAN                                           
\-----------------------------------------------------------------------------------------------
 Hash Join  (cost=29.80..186.32 rows=3872 width=40)
   Hash Cond: (tdapg_1.f1 = tdapg_2.f1)
   ->  Remote Subquery Scan on all (dn001,dn002)  (cost=100.00..158.40 rows=880 width=40)
         ->  Seq Scan on tdapg_1  (cost=0.00..18.80 rows=880 width=40)
   ->  Hash  (cost=126.72..126.72 rows=880 width=4)
         ->  Remote Subquery Scan on all (dn001,dn002)  (cost=100.00..126.72 rows=880 width=4)
               ->  Seq Scan on tdapg_2  (cost=0.00..18.80 rows=880 width=4)
(7 rows)

postgres=# set prefer_olap to on;
SET
postgres=# explain  select tdapg_1.* from tdapg_1,tdapg_2 where tdapg_1.f1=tdapg_2.f1 ;  
                                           QUERY PLAN                                           
\------------------------------------------------------------------------------------------------
 Remote Subquery Scan on all (dn001,dn002)  (cost=29.80..186.32 rows=3872 width=40)
   ->  Hash Join  (cost=29.80..186.32 rows=3872 width=40)
         Hash Cond: (tdapg_1.f1 = tdapg_2.f1)
         ->  Remote Subquery Scan on all (dn001,dn002)  (cost=100.00..158.40 rows=880 width=40)
               Distribute results by S: f1
               ->  Seq Scan on tdapg_1  (cost=0.00..18.80 rows=880 width=40)
         ->  Hash  (cost=18.80..18.80 rows=880 width=4)
               ->  Seq Scan on tdapg_2  (cost=0.00..18.80 rows=880 width=4)
(8 rows)
```
第一个 join 在 cn 节点执行，第二个在 dn 上重分布后再 join，业务设计上，一般 OLTP 类业务在 cn 上进行少数据量 join ，性能会更好。

## 查看并行的 worker 数
```
postgres=# explain select count(1) from tdapg_1;
                                      QUERY PLAN                                       
\---------------------------------------------------------------------------------------
 Finalize Aggregate  (cost=118.81..118.83 rows=1 width=8)
   ->  Remote Subquery Scan on all (dn001,dn002)  (cost=118.80..118.81 rows=1 width=0)
         ->  Partial Aggregate  (cost=18.80..18.81 rows=1 width=8)
               ->  Seq Scan on tdapg_1  (cost=0.00..18.80 rows=880 width=0)
(4 rows)

postgres=# analyze tdapg_1;
ANALYZE
postgres=# explain select count(1) from tdapg_1;
                                             QUERY PLAN                                             
\----------------------------------------------------------------------------------------------------
 Parallel Finalize Aggregate  (cost=14728.45..14728.46 rows=1 width=8)
   ->  Parallel Remote Subquery Scan on all (dn001,dn002)  (cost=14728.33..14728.45 rows=1 width=0)
         ->  Gather  (cost=14628.33..14628.44 rows=1 width=8)
               Workers Planned: 2
               ->  Partial Aggregate  (cost=13628.33..13628.34 rows=1 width=8)
                     ->  Parallel Seq Scan on tdapg_1  (cost=0.00..12586.67 rows=416667 width=0)
(6 rows)
```
上面第一个查询没走并行，第二个查询 analyze 后走并行才是正确的，建议大数据量更新再执行 analyze。

## 查看各节点的执行计划是否一致
```
./tdapg_run_sql_dn_master.sh "explain select * from tdapg_2 where f2=1"  
dn006 --- psql -h 172.16.0.13 -p 11227 -d postgres -U tdapg -c "explain select * from tdapg_2 where f2=1"
                                 QUERY PLAN                                  
\-----------------------------------------------------------------------------
 Bitmap Heap Scan on tdapg_2  (cost=2.18..7.70 rows=4 width=40)
   Recheck Cond: (f2 = 1)
   ->  Bitmap Index Scan on tdapg_2_f2_idx  (cost=0.00..2.18 rows=4 width=0)
         Index Cond: (f2 = 1)
(4 rows)

dn002 --- psql -h 172.16.0.42 -p 11012 -d postgres -U tdapg -c "explain select * from tdapg_2 where f2=1"
                                  QUERY PLAN                                   
\-------------------------------------------------------------------------------
 Index Scan using tdapg_2_f2_idx on tdapg_2  (cost=0.42..4.44 rows=1 width=14)
   Index Cond: (f2 = 1)
(2 rows)
```
两个 dn 的执行计划不一致，最大可能是数据倾斜或者是执行计划被禁用。
如有可能，DBA 可以配置在系统空闲时执行全库 analyze 和 vacuum。
