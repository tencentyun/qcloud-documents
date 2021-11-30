开启 Oracle 兼容参数设置后，分布键支持为 NULL。

示例：
```
postgres=# set enable_oracle_compatible to on;
SET
postgres=# create table tbl_shard_null(f1 int,f2 varchar(16)) distribute by shard(f1);
CREATE TABLE
postgres=# \d+ tbl_shard_null
  Table "public.tbl_shard_null"
  Column | Type  | Collation | Nullable | Default | Storage  | Stats target | Description 
--------+-----------------------+-----------+----------+---------+----------+--------------+------------
  f1 | integer   |   |  | | plain|  | 
  f2 | character varying(16) |   |  | | extended |  | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
postgres=# insert into tbl_shard_null select null,'null';
INSERT 0 1
postgres=# select * from tbl_shard_null ;
  f1 |  f2  
----+------
  | null
(1 row)
```
