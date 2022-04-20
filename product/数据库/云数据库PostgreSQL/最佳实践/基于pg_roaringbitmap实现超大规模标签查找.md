业务应用场景中常有通过标签进行筛选查询的功能，在数据量较大且标签值较多的场景下，数据容量会占用很多，性能也会较差，如何高效快速且不占用太多数据容量的情况下进行目标资源筛查，成为业务管理优化的不变话题。

本文为您介绍如何基于 pg_roaringbitmap 插件轻松实现超大规模标签的查找。

## pg_roaringbitmap 概述
pg_roaringbitmap 是一个基于 roaringbitmap 而实现的压缩位图存储数据插件，支持 roaring bitmap 的存取、集合操作，聚合等运算。

## roaringbitmap 用途
roaringbitmap 在业务中常用来存储用户的属性标签，可增删改查这些属性标签以及根据这些存储的用户的标签，通过并集、交集等方法来筛选出特定的用户，以达到超大规模属性数据的精准快速查找，既提升了性能，同时也能降低存储空间，是大数据分析场景下极佳的应用实践。
如在传统模式下如有一张音乐类应用的用户标签表，如下表：

| 用户ID | 用户名 | 兴趣标签 |
|---------|---------|---------|
| 1 | 张三 | {古典,爵士,R&B,乡村} |
| 2 | 李四 | {民歌,中国风,纯音乐} |
| 3 | 王五 | {HipHop,爵士,R&B,嘻哈,雷鬼} |
| ... | ... | ... |
| 1000000000 | 文本2 | {摇滚,} |

如想要找到喜欢纯音乐的所有用户，就需要根据兴趣标签列进行搜索，找到标签中包含纯音乐的行，然后将此数据返回给应用。
一般最简单的做法是：首先按照上表的结构在数据库中建立一张用户兴趣表，然后执行数组查询语句，找到兴趣标签进行包含查找。但这么做会有一个问题，在数据量较大且标签值较多的场景下，不仅数据容量占用得更多，而且性能会极差。所以我们需要更换一种实现方案，将此表拆分为三张表，兴趣标签作为主键，包含此兴趣标签的用户作为 bitmap 存储。如下表所示：

**用户表：**

| 用户ID | 用户名 |
|---------|---------|
| 1 | 张三 |
| 2 | 李四 |
| N | ... |

**标签表：**

| 标签ID | 用户名 |
|---------|---------|
| 1 | 古典 |
| 2 | 民歌 |
| N | ... |

**用户标签表：**

| 标签ID | 用户名 |
|---------|---------|
| 1 | [ 1,3,7,123,423 ] |
| 2 | [ 5,31] |
| N | ... |

当需要查找同时喜欢听古典和民歌的用户时，直接在用户标签表对用户 ID 做 bitmap 查询即可，能够极大的提升性能并且容量占用可大幅降低。

## 传统方法与使用 roaringbitmap 方法查询性能对比
### 准备测试场景
1. 创建一个随机字符的函数。
```
create or replace function random_string(length integer) returns text as
$$
declare
chars text[] := '{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}';
result text := '';
i integer := 0;
length2 integer := (select trunc(random() * length + 1));
begin
if length2 < 0 then
raise exception 'Given length cannot be less than 0';
end if;
for i in 1..length2 loop
result := result || chars[1+random()*(array_length(chars, 1)-1)];
end loop;
return result;
end;
$$ language plpgsql;
```
2. 创建一个生成随机整形数组的函数。
```
create or replace function random_int_array(int, int)
returns int[] language sql as
$$
select array_agg(round(random()* $1)::int)
from generate_series(1, $2)
$$;
```
3. 创建一个生成随机字符数组的函数。
```
create or replace function random_string_array(int, int)
returns TEXT[] language sql as
$$
select array_agg(random_string($1)) from generate_series(1, $2);
$$;
```

### 方案1：传统方法
一张表解决一切。
1. 创建一个表包含所有数据。
```
create table account(
uin bigint primary KEY,
name varchar,
tag TEXT []
);
```
2. 模拟插入1000W个账号数据（需要使用到场景准备工作中的函数），并且创建 Gin 索引。
```
insert into account select generate_series(1,10000000), random_string(20),random_string_array(5,10);
create index tag_inx on account USING GIN(tag);
```
3. 执行查询，查找标签带 GN 和 o 的用户列表。
```
explain analyze select uin,name from account where tag @>ARRAY['GN','o'];

QUERY PLAN

----------------------------------------------------------------------------------------------------
-----------------
Bitmap Heap Scan on account (cost=52.81..466.86 rows=105 width=19) (actual time=4.263..4.502 rows=
184 loops=1)
Recheck Cond: (tag @> '{GN,o}'::text[])
Heap Blocks: exact=184
-> Bitmap Index Scan on tag_inx (cost=0.00..52.78 rows=105 width=0) (actual time=4.240..4.240 r
ows=184 loops=1)
Index Cond: (tag @> '{GN,o}'::text[])
Planning Time: 0.108 ms
Execution Time: 4.528 ms
```
4. 执行查询，查找标签 lvXe 和 Zt 的人有 xx 个（第一次查询会较慢）。
```
explain analyze select count(uin) from account where tag && ARRAY['lvXe','Zt'];

----------------------------------------------------------------------------------------------------
--------------------------
Aggregate (cost=21816.39..21816.40 rows=1 width=8) (actual time=8.236..8.238 rows=1 loops=1)
-> Bitmap Heap Scan on account (cost=109.08..21800.56 rows=6332 width=8) (actual time=1.655..7.
901 rows=5390 loops=1)
Recheck Cond: (tag && '{lvXe,Zt}'::text[])
Heap Blocks: exact=5327
-> Bitmap Index Scan on tag_inx (cost=0.00..107.49 rows=6332 width=0) (actual time=0.962.
.0.962 rows=5390 loops=1)
Index Cond: (tag && '{lvXe,Zt}'::text[])
Planning Time: 0.110 ms
Execution Time: 8.270 ms
```

### 方案2：优化方案
为了降低查询中标签字段的类型导致的性能减低，所以将上面表中的真实 tag 修改为 tagid。
1. 引入一个新的标签字典表。
```
create table tag_dict (  
tagid int primary key,
taginfo text
);
```
2. 假设一共有10W种字典类型。
```
insert into tag_dict select generate_series(1,100000), md5(random()::text);
```
3. 创建一个新表用来存储用户和标签信息。
```
create table account1(
uin bigint primary KEY,
name varchar,
tag INT []
);
```
4. 插入1000W个账号数据。
```
insert into account1 select generate_series(1,10000000), random_string(20),random_int_array(100000,10);
```
5. 查找同时有标签 ID 为100和5711的用户列表。
**索引前**：
```
test=> explain analyze select uin,name from account1 where tag @> ARRAY[100,5711];
QUERY PLAN
-----------------------------------------------------------------------------------------------------------------------------
Gather (cost=1000.00..191007.68 rows=250 width=19) (actual time=982.585..1000.806 rows=0 loops=1)
Workers Planned: 2
Workers Launched: 2
-> Parallel Seq Scan on account1 (cost=0.00..189982.68 rows=104 width=19) (actual time=962.640..962.640 rows=0 loops=3)
Filter: (tag @> '{100,5711}'::integer[])
Rows Removed by Filter: 3333333
Planning Time: 0.205 ms
JIT:
Functions: 12
Options: Inlining false, Optimization false, Expressions true, Deforming true
Timing: Generation 2.280 ms, Inlining 0.000 ms, Optimization 1.176 ms, Emission 14.189 ms, Total 17.645 ms
Execution Time: 1001.574 ms
(12 rows)
```
**加索引：**
```
create index tag_inx_2 on account1 USING GIN(tag);
```
**索引后：**
```
test=> explain analyze select uin,name from account1 where tag @> ARRAY[100,5711];
QUERY PLAN
---------------------------------------------------------------------------------------------------------------------
Bitmap Heap Scan on account1 (cost=49.94..1021.13 rows=250 width=19) (actual time=0.126..0.127 rows=0 loops=1)
Recheck Cond: (tag @> '{100,5711}'::integer[])
-> Bitmap Index Scan on tag_inx_2 (cost=0.00..49.87 rows=250 width=0) (actual time=0.124..0.124 rows=0 loops=1)
Index Cond: (tag @> '{100,5711}'::integer[])
Planning Time: 0.410 ms
Execution Time: 0.171 ms
(6 rows)
```
6. 查找同时有标签 ID 为61568，97350的用户列表。
```
test=> explain analyze select uin,name from account1 where tag @> ARRAY[61568,97350];
QUERY PLAN
---------------------------------------------------------------------------------------------------------------------
Bitmap Heap Scan on account1 (cost=49.94..1021.13 rows=250 width=19) (actual time=0.130..0.131 rows=1 loops=1)
Recheck Cond: (tag @> '{61568,97350}'::integer[])
Heap Blocks: exact=1
-> Bitmap Index Scan on tag_inx_2 (cost=0.00..49.87 rows=250 width=0) (actual time=0.125..0.125 rows=1 loops=1)
Index Cond: (tag @> '{61568,97350}'::integer[])
Planning Time: 0.071 ms
Execution Time: 0.151 ms
(7 rows)
```
7. 查找与 xx 有共同爱好（标签100和5711）的人有 xx 个。
```
test=> explain analyze select count(uin) from account1 where tag && ARRAY[61568,97350];
QUERY PLAN

---------------------------------------------------------------------------------------------------------------------------------
------
Gather (cost=1961.06..173801.15 rows=99750 width=19) (actual time=5.020..28.885 rows=2066 loops=1)
Workers Planned: 2
Workers Launched: 2
-> Parallel Bitmap Heap Scan on account1 (cost=961.06..162826.15 rows=41562 width=19) (actual time=1.623..3.305 rows=689 loo
ps=3)
Recheck Cond: (tag && '{61568,97350}'::integer[])
Heap Blocks: exact=2053
-> Bitmap Index Scan on tag_inx_2 (cost=0.00..936.12 rows=99750 width=0) (actual time=0.685..0.685 rows=2066 loops=1)
Index Cond: (tag && '{61568,97350}'::integer[])
Planning Time: 0.082 ms
JIT:
Functions: 12
Options: Inlining false, Optimization false, Expressions true, Deforming true
Timing: Generation 2.078 ms, Inlining 0.000 ms, Optimization 0.270 ms, Emission 3.489 ms, Total 5.836 ms
Execution Time: 29.725 ms
(14 rows)
```

### 方案3：roaringbitmap
1. 首先需要创建插件，云数据库 PostgreSQL 天然集成了此插件，无需关注编译等操作，直接进入数据库中创建即可。
```
create extension roaringbitmap;
```
2. 创建标签用户对应表。
```
create table tag_uin_list(
tagid int primary key,
uin_offset int,
uinbits roaringbitmap
);
```
3. 根据之前的标签表插入10W条标签以及标签对应的用户数据。
```
insert into tag_uin_list
select tagid, uin_offset, rb_build_agg(uin::int) as uinbits from
(
select
unnest(tag) as tagid,
(uin / (2^31)::int8) as uin_offset,
mod(uin, (2^31)::int8) as uin
from account1
) t
group by tagid, uin_offset;
```
4. 查询标签有1，3，10，200的用户个数。
```
explain analyze select sum(ub) from
(
select uin_offset,rb_or_cardinality_agg(uinbits) as ub
from tag_uin_list
where tagid in (1,3,10,200)
group by uin_offset
) t;


QUERY PLAN

---------------------------------------------------------------------------------------------------------------------------------
------------
Aggregate (cost=32.47..32.48 rows=1 width=32) (actual time=0.964..0.966 rows=1 loops=1)
-> GroupAggregate (cost=32.42..32.46 rows=1 width=12) (actual time=0.955..0.956 rows=1 loops=1)
Group Key: tag_uin_list.uin_offset
-> Sort (cost=32.42..32.43 rows=4 width=22) (actual time=0.107..0.109 rows=4 loops=1)
Sort Key: tag_uin_list.uin_offset
Sort Method: quicksort Memory: 25kB
-> Bitmap Heap Scan on tag_uin_list (cost=17.20..32.38 rows=4 width=22) (actual time=0.044..0.067 rows=4 loops=1
)
Recheck Cond: (tagid = ANY ('{1,3,10,200}'::integer[]))
Heap Blocks: exact=4
-> Bitmap Index Scan on tag_uin_list_pkey (cost=0.00..17.20 rows=4 width=0) (actual time=0.031..0.031 rows
=4 loops=1)
Index Cond: (tagid = ANY ('{1,3,10,200}'::integer[]))
Planning Time: 0.289 ms
Execution Time: 1.083 ms
(13 rows)
```
5. 查看标签有1，3，10，200的用户列表。
```
explain analyze select uin_offset,rb_or_agg(uinbits) as ub
from tag_uin_list
where tagid in (1,3,10,200)
group by uin_offset;
QUERY PLAN

---------------------------------------------------------------------------------------------------------------------------------
------
GroupAggregate (cost=32.42..32.46 rows=1 width=36) (actual time=0.246..0.246 rows=1 loops=1)
Group Key: uin_offset
-> Sort (cost=32.42..32.43 rows=4 width=22) (actual time=0.043..0.045 rows=4 loops=1)
Sort Key: uin_offset
Sort Method: quicksort Memory: 25kB
-> Bitmap Heap Scan on tag_uin_list (cost=17.20..32.38 rows=4 width=22) (actual time=0.029..0.036 rows=4 loops=1)
Recheck Cond: (tagid = ANY ('{1,3,10,200}'::integer[]))
Heap Blocks: exact=4
-> Bitmap Index Scan on tag_uin_list_pkey (cost=0.00..17.20 rows=4 width=0) (actual time=0.021..0.021 rows=4 loops=1)
Index Cond: (tagid = ANY ('{1,3,10,200}'::integer[]))
Planning Time: 0.119 ms
Execution Time: 0.310 ms
(12 rows)
```

### 查看索引以及表占用大小
```
test=> select relname, pg_size_pretty(pg_relation_size(relid)) from pg_stat_user_tables where schemaname='public' order by pg_relation_size(relid) desc;
   relname    | pg_size_pretty 
--------------+----------------
 account      | 1545 MB
 account1     | 1077 MB
 t_user       | 651 MB
 tag_dict     | 6672 kB
 tag_uin_list | 5888 kB
(5 rows)

test=> select indexrelname, pg_size_pretty(pg_relation_size(relid)) from pg_stat_user_indexes where schemaname='public' order by pg_relation_size(relid) desc;
   indexrelname    | pg_size_pretty 
-------------------+----------------
 tag_inx           | 1545 MB
 account_pkey      | 1545 MB
 tag_inx_2         | 1077 MB
 account1_pkey     | 1077 MB
 t_user_pkey       | 651 MB
 tag_dict_pkey     | 6672 kB
 tag_uin_list_pkey | 5888 kB
(7 rows)
```

### 结论
不同方案的查询性能对比如下表：

| 查询项 | 方案1 | 方案2 | roaringbitmap 方案 |
|---------|---------|---------|---------|
| 查询包含指定标签的用户列表 | 4.528ms | 0.151ms | 0.310ms |
| 查询具备共同标签的用户个数 | 8.27ms | 29.725ms | 1.083ms |
| 数据容量统计 | 4635MB | 3244.344MB | 1237.12MB |

基于上述三种方案可以明显看到，优化后效果非常明显，无论是容量还是性能都强于传统方案，roaringbitmap 方案整体上来看，无论是查询耗时还是数据容量占用都有很好的性能和效果。


