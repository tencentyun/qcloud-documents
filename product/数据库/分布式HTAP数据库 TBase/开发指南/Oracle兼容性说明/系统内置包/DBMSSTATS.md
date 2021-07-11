DBMS_STATS 能良好地估计统计数据，尤其是针对较大的分区表，并能获得更好的统计结果，最终制定出速度更快的 SQL 执行计划。包含以下接口：

| 接口                  | 描述                                   |
| --------------------- | -------------------------------------- |
| GATHER_DATABASE_STATS | 分析数据库，包括所有用户对象和系统对象 |
| GATHER_TABLE_STATS    | 分析表                                 |
| GET_COLUMN_STATS      | 取得列的统计信息                       |
| GET_INDEX_STATS       | 取得索引的统计信息                     |
| GET_TABLE_STATS       | 取得表的统计信息                       |

示例：
```
CREATE EXTENSION IF NOT EXISTS tbase_oracle_package_function;
    
create user godlike_dbms_stats superuser;
create user joe;
create user no_privilege;
    
\c postgres godlike_dbms_stats
grant usage on schema dbms_stats to no_privilege;
grant usage on schema dbms_stats to joe;
    
\c postgres joe
-- table joe_t
create table joe_t (id integer not null PRIMARY KEY, test integer);
create index joe_t_test_idx on joe_t(test);
insert into joe_t SELECT generate_series(1,1000) as key, (random()*(10^3))::integer;
    
\c postgres joe
exec dbms_stats.gather_table_stats(ownname => 'joe',tabname => 'joe_t');
exec dbms_stats.get_table_stats(ownname => 'joe',tabname => 'joe_t');
exec dbms_stats.get_column_stats('joe', 'joe_t', 'test');
exec dbms_stats.get_index_stats('joe', 'joe_t_test_idx');
    
-- table joe_t_p
create table joe_t_p (id integer not null PRIMARY KEY, test integer) partition by range (id) begin (1) step (5) partitions (200) distribute by shard(id);
create index joe_t_p_test_idx on joe_t_p(test);
insert into joe_t_p SELECT generate_series(1,1000) as key, (random()*(10^3))::integer;
    
exec dbms_stats.gather_database_stats();
exec dbms_stats.get_table_stats(ownname => 'joe',tabname => 'joe_t_p');
exec dbms_stats.get_column_stats('joe', 'joe_t_p', 'test');
exec dbms_stats.get_index_stats('joe', 'joe_t_p_test_idx');
exec dbms_stats.get_table_stats('joe', 'joe_t_p', 'joe_t_p_part_0');
exec dbms_stats.get_index_stats('joe', 'joe_t_p_test_idx', 'joe_t_p_test_idx_part_0');
    
-- clean
\c postgres godlike_dbms_stats
drop table joe_t;
drop table joe_t_p;
REVOKE usage ON schema dbms_stats FROM joe;
REVOKE usage ON schema dbms_stats FROM no_privilege;
drop user joe;
drop user no_privilege;
```
