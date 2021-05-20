## 功能介绍
该功能主要通过限制某些 SQL 语句的操作，来避免由于 SQL 语句使用不当所导致的系统资源占用过大、系统整体性能下降或假死的情况发生。

## 支持版本
- 内核版本 MySQL 5.7 20200331 及以上
- 内核版本 MySQL 5.6 20200915 及以上

## 适用场景
该功能适用于由于 SQL 语句使用不当所导致的系统资源占用过大、系统整体性能下降或假死的场景。

## 使用说明
参数 cdb_sql_filter_enable 用于 SQL 限流开关，默认值为 false。
参数 cdb_sql_filter 用于修改 SQL 限流规则。
参数 cdb_sql_filter_seperator 用于控制 SQL 限流规则的分隔符，默认为`,`。

使用示例如下：
- 设置需要限流的语句和限流方式：
```
set global cdb_sql_filter = '+,[select | update | delete | insert | replace], expire_time, concurrence,key1,key2,key3'
set global cdb_sql_filter = 'reset_all'
set global cdb_sql_filter = '-id'
set global cdb_sql_filter = '+,select,1,2,key1,key2,key3'
```

- 查询限流设置
```
show cdb_sql_filters;
select * from information_schema.cdb_sql_filter_info; 
```
