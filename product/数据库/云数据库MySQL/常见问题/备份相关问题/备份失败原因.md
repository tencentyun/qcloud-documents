### 单实例的表数量超过100万
单个实例的表数量超过100万后，可能会造成备份失败，同时也会影响数据库监控，请合理规范表的数量，控制单个实例表数量不超过100万。

### 无主键表导致的大事务
#### 原因分析
实例中存在无主键表且 binlog 为 row 格式时，当一条 sql 更新/删除了大量数据，在备机回放会造成大事务，从而导致备份线程无法获取锁，造成备份失败。

#### 处理方案
1. 通过 sql 检查实例中所有存在的无主键表。
```
select TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,TABLE_ROWS from information_schema.tables where (table_schema,table_name) not in (select table_schema,table_name from information_schema.columns where COLUMN_KEY='PRI') and table_schema not in ('sys','mysql','information_schema','performance_schema');
```
2. 对无主键表添加主键。
```
alter table table_name add primary key(`column_name`);
```
