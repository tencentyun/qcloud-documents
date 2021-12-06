## 介绍
Redis Connector 提供了对 Redis 写入和维表的支持。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持（写入，维表）|
| 1.13      | 支持（写入） |

## 使用范围
- 可以作为维表的使用。
- 可以作为 Tuple、Upsert 数据流的目的表。

## DDL 定义
### set 命令（字符串键）

```sql
-- 第1列为 key，第2列为 value。Redis 命令为 set key value
CREATE TABLE `redis_set_sink_table` (  
 `key` STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'set',         -- set 命令
  'nodes' = '<host>:<port>', -- redis 连接地址
  'password' = '<password>', 
  'database' = '<database>'  
);
```

### lpush 命令（列表键）

```sql
-- 第1列为 key，第2列为 value。Redis 命令为 lpush key value
CREATE TABLE `redis_lpush_sink_table` (  
 `key` STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'lpush',       -- lpush 命令
  'nodes' = '<host>:<port>', -- redis 连接地址
  'password' = '<password>', 
  'database' = '<database>'  
);

```

### sadd 命令（集合键）

```sql
-- 第1列为 key，第2列为 value。Redis 命令为 sadd key value
CREATE TABLE `redis_sadd_sink_table` (  
 `key`   STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'sadd',        -- sadd 命令
  'nodes' = '<host>:<port>', -- redis 连接地址
  'password' = '<password>', 
  'database' = '<database>'  
);

```

### hset 命令（哈希键）

```sql
-- 第1列为 hash_key，第2列为 hash_value。Redis 命令为 hset key hash_key hash_value。
CREATE TABLE `redis_hset_sink_table` (  
 `hash_key`   STRING,
 `hash_value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'hset',        -- hset 命令
  'nodes' = '<host>:<port>', -- redis 连接地址
  'password' = '<password>', 
  'database' = '<database>', 
  'additional-key' = '<key>' -- 哈希键
);

```

### zadd 命令（有序集合键）

```sql
-- 第1列为 hash_key，第2列为 hash_value。zadd key score value。
CREATE TABLE `redis_zadd_sink_table` (  
 `value` STRING,
 `score` DOUBLE
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'zadd',        -- zadd 命令
  'nodes' = '<host>:<port>', -- redis 连接地址
  'password' = '<password>', 
  'database' = '<database>', 
  'additional-key' = '<key>' -- 有序集合键
);

```

### get 命令（维表）

```sql
CREATE TABLE `redis_dimension_table` (  
 `key`   STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',          
  'command' = 'get',              -- get命令
  'nodes' = '<host>:<port>',     -- redis连接地址,集群模式多个节点使用'',''分隔。
  'lookup.cache.max-rows' = '500', -- 查询缓存中最多缓存的数据条数。
  'lookup.cache.ttl' = '10 min', -- 每条记录的最长缓存时间。
  'lookup.max-retries' = '5', -- 查询失败，最多重试次数。
  -- 'password' = '<password>',   -- 可选参数，密码
  -- 'database' = '<database>',   -- 可选参数，数据库：默认0
  -- 'redis-mode' = 'standalone' -- 可选参数，redis 部署模式，默认standalone。(可选：standalone 单机模式，cluster 集群模式)     
);
```

## WITH 参数

| 参数值         | 必填 |   默认值   | 描述                                                         |
| :------------- | :--: | :--------: | :----------------------------------------------------------- |
| connector      |  是  |     -      | 固定值为 redis                                               |
| command        |  是  |     -      | 操作命令。取值与对应的键类型如下：<li>set：字符串键</li><li>lpush：类别键<li>sadd：集合键</li><li>hset：哈希键 </li><li>zadd：有序集合键</li> |
| nodes          |  是  |     -      | redis server 连接地址，示例：127.0.0.1:6379。集群架构下多个节点使用','分隔 |
| password       |  否  |     空     | redis 密码，默认值为空，不进行权限验证                       |
| database       |  否  |     0      | 要操作的数据库的 DB number，默认值0                          |
| redis-mode     |  否  | standalone | redis 部署模式</li><li>standalone：标准架构，单机</li><li>cluster：集群架构，分布式</li> |
| ignore-delete  |  否  |   false    | 是否忽略 Retraction 消息                                     |
| additional-ttl |  否  |     -      | 过期时间，单位：秒。示例：60，设置过期是时间为60秒。**只有 set 命令支持设置过期时间** |
| additional-key |  -   |     -      | 用于指定 hset 和 zadd 的 key。执行 hset 和 zadd 命令时必须设置 |
| lookup.cache.max-rows |  否  |     -      | 查询缓存中最多缓存的数据条数                                 |
| lookup.cache.ttl      |  否  |    10s     | 每条记录的最长缓存时间                                       |
| lookup.max-retries    |  否  |     1      | 查询失败最多重试次数                                         |


## 代码示例

```sql
CREATE TABLE datagen_source_table ( 
	id INT, 
	name STRING 
) WITH ( 
   'connector' = 'datagen',
   'rows-per-second'='1'  -- 每秒产生的数据条数
);

CREATE TABLE `redis_set_sink_table` (  
 `key` STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到 Redis
  'command' = 'set',         -- set 命令
  'nodes' = '127.0.0.1:8121', -- redis 连接地址
  'password' = '<password>', 
  'database' = '0'  
);
insert into redis_set_sink_table select cast(id as string), name from datagen_source_table;
```

## 注意事项 
1. 自建 Redis 的集群模式不支持多数据库，集群模式下 database 参数无效。
2. 腾讯云数据库 Redis 的集群架构支持多数据库，可以使用 standalone 模式指定写入云数据库 Redis 集群架构中的非0数据库，例如：
```sql
CREATE TABLE `redis_set_sink_table` (  
 `key` STRING,
 `value` STRING
) WITH (
  'connector' = 'redis',     -- 输出到Redis
  'command' = 'set',         -- set命令
  'nodes' = '<host>:<port>', -- redis连接地址
  'password' = '<password>', 
  'redis-mode' = 'standalone',
  'database' = '1' 
);
```
