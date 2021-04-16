## int 型范围 range 分区
```
DROP TABLE if exists t_range;
CREATE TABLE t_range(
  f1 bigint,
  f2 timestamp default now(), 
  f3 integer
) PARTITION BY range (f3) begin (1) step (50) partitions (3) with (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group;
INSERT INTO t_range(f1,f3) VALUES(1,150);    
```

## timestamp 类型 range 分区
```
DROP TABLE IF EXISTS t_time_range;
CREATE TABLE t_time_range(f1 bigint, f2 timestamp ,f3 bigint) **PARTITION BY range** (f2) **begin** (timestamp without time zone '2017-09-01 0:0:0') **step** (interval '1 month') **partitions** (12) with (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group;
```

## list 分区
```
CREATE TABLE t_native_list(
  f1 bigserial not null,
  f2 text, 
  f3 integer,
  f4 date
) PARTITION BY list(f2) with (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group; 
--two child tables
CREATE TABLE t_native_list_gd partition of t_native_list(f1 ,f2 , f3,f4) for VALUES in ('guangdong');
CREATE TABLE t_native_list_bj partition of t_native_list(f1 ,f2 , f3,f4) for VALUES in ('beijing');
```

## 二级分区
先 list 分区，再 range 分区：
```
CREATE TABLE t_native_mul_list(
  f1 bigserial not null,
  f2 integer,
  f3 text,
  f4 text, 
  f5 date) PARTITION BY list ( f3 ) WITh (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group;
--secondary tables
CREATE TABLE t_native_mul_list_gd partition of t_native_mul_list for VALUES in ('guangdong') PARTITION BY range(f5) with (orientation = 'column');
CREATE TABLE t_native_mul_list_bj partition of t_native_mul_list for VALUES in ('beijing') PARTITION BY range(f5) with (orientation = 'column'); 
CREATE TABLE t_native_mul_list_sh partition of t_native_mul_list for VALUES in ('shanghai') WITh (orientation = 'column');
--three level tables
CREATE TABLE t_native_mul_list_gd_201701 partition of t_native_mul_list_gd(f1,f2,f3,f4,f5) for VALUES FROM ('2017-01-01') to ('2017-02-01') WITh (orientation = 'column');
CREATE TABLE t_native_mul_list_gd_201702 partition of t_native_mul_list_gd(f1,f2,f3,f4,f5) for VALUES FROM ('2017-02-01') to ('2017-03-01') WITh (orientation = 'column');
CREATE TABLE t_native_mul_list_bj_201701 partition of t_native_mul_list_bj(f1,f2,f3,f4,f5) for VALUES FROM ('2017-01-01') to ('2017-02-01') WITh (orientation = 'column');
CREATE TABLE t_native_mul_list_bj_201702 partition of t_native_mul_list_bj(f1,f2,f3,f4,f5) for VALUES FROM ('2017-02-01') to ('2017-03-01') WITh (orientation = 'column');
DROP TABLE t_native_mul_list_bj_201702;
DROP TABLE t_native_mul_list_bj_201701;
DROP TABLE t_native_mul_list_gd_201702;
DROP TABLE t_native_mul_list_gd_201701;
DROP TABLE t_native_mul_list_sh;
DROP TABLE t_native_mul_list_gd;
DROP TABLE t_native_mul_list; 
```
