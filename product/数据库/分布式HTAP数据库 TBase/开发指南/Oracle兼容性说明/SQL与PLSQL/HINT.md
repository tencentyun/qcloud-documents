对于一些执行计划不是最优的 SQL，可以通过 HINT 干预执行计划的生成，例如对指定表的全表扫描，用指定的索引，用指定的表关联算法等等。
TDSQL PostgreSQL版（Oracle 兼容）兼容常用的 Oracle 的 HINT 用法，同时支持基于 `pg_hint_plan` 的 HINT 用法。

## 语法
```
{ DELETE |INSERT | SELECT | UPDATE } /*+ hint1 [hint2 ...] */ statement;
```
其中：
- DELETE、INSERT、SELECT 和 UPDATE 是标识一个语句块开始的关键字，包含提示的注释只能出现在这些关键字的后面，否则提示无效。
- '+'号表示该注释是一个 HINTS，该加号必须立即跟在 '/\*' 的后面，中间不能有空格。
- HINT 是下面介绍的具体提示之一，如果包含多个提示，则每个提示之间需要用一个或多个空格隔开。
- 如果没有正确的指定 HINTS，将忽略该 HINTS。
- 大小写忽略。

常用 HINT 场景：

| HINT 场景        | 兼容 Oracle 写法            | TDSQL PostgreSQL版 写法                |
| --------------- | ------------------------- | ------------------------ |
| 强制走 mergejoin | use_merge(table1, table2) | MergeJoin(table1 table2) |
| 强制走 nestloop  | use_nl(table1, table2)    | NestLoop(table1 table2)  |
| 强制走 hashjoin  | use_hash(table1, table2)  | hashJoin(table1 table2)  |
| 强制走索引      | index(table，index)       | indexscan(table index)   |
| 强制全表扫描    | full(table)               | SeqScan(table)           |

更多介绍请参见 [pg_hint_plan](http://pghintplan.sourceforge.jp/hint_list.html)。

## 示例
```
postgres=# create table hint_t6(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t6 select t as f1,t as f2 from generate_series(1,10000) as t;
INSERT 0 10000
postgres=# create index hint_t6_f1_idx on hint_t6(f1);
CREATE INDEX
postgres=# create table hint_t7(f1 integer,f2 integer) ;
CREATE TABLE
postgres=# insert into hint_t7 select t as f1,t as f2 from generate_series(1,10000) as t;
INSERT 0 10000
postgres=# create index hint_t7_f1_idx on hint_t7(f1);
CREATE INDEX
    
1）强制走 MergeJoin
兼容 Oracle 写法
postgres=# select /*+use_merge(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  f1   |  f2   |  f1   |  f2   
-------+-------+-------+-------
  10000 | 10000 | 10000 | 10000
(1 row)
postgres=# explain select /*+use_merge(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Merge Join  (cost=0.56..163.78 rows=1 width=16)
  Merge Cond: (t.f1 = t1.f1)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..148.87 rows=5039 width=8)
(7 rows)
    
TDSQL PostgreSQL-O版 写法
postgres=# select /*+ MergeJoin(t t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  f1   |  f2   |  f1   |  f2   
-------+-------+-------+-------
  10000 | 10000 | 10000 | 10000
(1 row)
postgres=# explain select /*+ MergeJoin(t t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Merge Join  (cost=0.56..163.78 rows=1 width=16)
  Merge Cond: (t.f1 = t1.f1)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..148.87 rows=5039 width=8)
(7 rows)
    
2）强制走 nestloop
兼容 Oracle 写法：
postgres=# explain select /*+use_nl(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>999 ; 
  QUERY PLAN  
---------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.28..1624.87 rows=4548 width=16)
  ->  Seq Scan on hint_t6 t  (cost=0.00..102.99 rows=4548 width=8)
    Filter: (f1 > 999)
  ->  Index Scan using hint_t7_f1_idx on hint_t7 t1  (cost=0.28..0.32 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
TDSQL PostgreSQL版 写法：
postgres=# explain select /*+NestLoop(t t1) */* from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t1.f1>999 ;
  QUERY PLAN 
--------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.28..1624.87 rows=4548 width=16)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..102.99 rows=4548 width=8)
    Filter: (f1 > 999)
  ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..0.32 rows=1 width=8)
    Index Cond: (f1 = t1.f1)
(7 rows)
    
3）强制走 hashjoin
兼容 Oracle 写法：
postgres=# explain select /*+use_hash(t,t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ; 
  QUERY PLAN
--------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=2.31..111.61 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=2.30..2.30 rows=1 width=8)
    ->  Index Scan using hint_t6_f1_idx on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
  Index Cond: (f1 > 9999)
(8 rows)
    
TDSQL PostgreSQL版 写法：
postgres=# explain select /*+ hashJoin(t t1) SeqScan(t) SeqScan(t1)*/ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
-----------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=103.00..212.30 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=102.99..102.99 rows=1 width=8)
    ->  Seq Scan on hint_t6 t  (cost=0.00..102.99 rows=1 width=8)
  Filter: (f1 > 9999)
(8 rows)
    
4）强制走索引
postgres=# create index idx_hint_t6_f1f2 on hint_t6(f1,f2);
CREATE INDEX
postgres=# create index idx_hint_t7_f1 on hint_t7(f1);
CREATE INDEX
postgres=# explain select * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
---------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..6.61 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1 on hint_t6 t  (cost=0.28..2.30 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
在没有 hint 强制走索引时，执行计划用到索引 idx_hint_t6_f1、idx_hint_t7_f1
    
强制走索引 idx_hint_t6_f1f2
兼容 Oracle 写法：
postgres=# explain select /*+ index(t idx_hint_t6_f1f2) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
----------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..7.48 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
TDSQL PostgreSQL版 写法：
postgres=# explain select /*+ indexscan(t idx_hint_t6_f1f2) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN  
----------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Nested Loop  (cost=0.56..7.48 rows=1 width=16)
  ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
    Index Cond: (f1 > 9999)
  ->  Index Scan using idx_hint_t7_f1 on hint_t7 t1  (cost=0.28..4.30 rows=1 width=8)
    Index Cond: (f1 = t.f1)
(7 rows)
    
postgres=# 
    
5）强制全表扫描
postgres=# explain select /*+ index(t idx_hint_t6_f1f2) SeqScan(t1) */ * from hint_t6 t,hint_t7 t1 where t.f1=t1.f1 and t.f1>9999 ;
  QUERY PLAN 
----------------------------------------------------------------------------------------------------
  Remote Fast Query Execution  (cost=0.00..0.00 rows=0 width=0)
    Node/s: dn001, dn002
    ->  Hash Join  (cost=3.19..112.48 rows=1 width=16)
  Hash Cond: (t1.f1 = t.f1)
  ->  Seq Scan on hint_t7 t1  (cost=0.00..90.39 rows=5039 width=8)
  ->  Hash  (cost=3.17..3.17 rows=1 width=8)
    ->  Index Scan using idx_hint_t6_f1f2 on hint_t6 t  (cost=0.28..3.17 rows=1 width=8)
  Index Cond: (f1 > 9999)
(8 rows)
指定 SeqScan(t1) 后，执行计划中 t1 表由索引扫描变为全表扫描
```
   
