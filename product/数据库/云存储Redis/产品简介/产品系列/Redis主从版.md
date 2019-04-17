Redis 主从版（社区）是最通用的 Redis 版本，兼容 Redis 2.8 版本的协议和命令，采用主从节点部署架构，提供数据持久化和备份，适用于对数据可靠性、可用性都有要求的场景。主节点提供日常服务访问，从节点提供 HA 高可用，当主节点发生故障，系统会自动切换至从节点，保证业务平稳运行。
![](https://main.qcloudimg.com/raw/37626b6980e25a1ddf4fd3efcf4bbd4a.png)

## 功能特性
-   **服务可靠**
采用双机主从架构，主从节点位于不同物理机。主节点对外提供访问，用户可通过 Redis 命令行和通用客户端进行数据的增、删、改、查操作。当主节点出现故障，自研的 HA 系统会自动进行主从切换，保证业务平稳运行。        
-   **数据可靠**
默认开启数据持久化功能，主从版支持数据备份功能，用户可以针对备份集回滚实例或者克隆实例，有效的解决数据误操作等问题。

## 使用限制
- Redis 主从版支持0.25GB - 60GB规格，需要更大的主从版规格可选择 CKV 主从版最大可支持384GB，或者集群版最大可支持48TB的容量。
- Redis 主从版的性能最大支持10万 QPS，需要更高的 QPS 请选择 Redis 集群版或 CKV 集群版，可支持千万级 QPS。

## 兼容性
云数据库 Redis 主从版兼容 Redis 2.8 协议命令。自建的 Redis 数据库可以平滑迁移至 Redis 标准版，并且提供数据传输工具（DTS）可以进行增量的 Redis 迁移，保证业务平稳过渡。

>?2018年11月1日之前购买的实例，不支持 client list、monitor、scritp 命令，如需要开通，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。

**主从版 Redis 支持的命令:**

| **connection 族** | **hashes 族** | **keys 族** | **lists 族** | **pub/sub 族** | **server 族** | 
| --- | --- | --- | --- | --- | --- |
| auth | hdel | del | lindex | psubscribe | command | 
| echo | hexists | scan | linsert | pubsub | dbsize |
| ping | hget | exists | llen | publish | info | 
| quit | hgetall | expire | lpop | punsubscribe | time | 
| select | hincrby | expireat | lpush | subscribe | client list  | 
| -  | hincrbyfloat | keys | lpushx | unsubscribe | config get  | 
| -　 | hkeys | type | lrange | -　 | monitor  | 
| -　 | hlen | move | lrem | -　 | flushdb  |
| -　 | hmget | ttl | lset | -　 | flushall  |
| -　 | hmset | persist | ltrim | -　 | slowlog  |
| -　 | hset | pexpire | rpop | -　 | -  |
| -　 | hsetnx | pexpireat | rpoplpush | -　 | -  |
| -　 | hstrlen | pttl | rpush | -　 |-  |
| -　 | hvals | randomkey | rpushx | -　 | -  |
| -　 | hscan | rename | blpop | -　 | -  |
| -　 | -　 | renamenx | brpop | -　 | -　 |
| -　 | -　 | sort | brpoplpush | -　 | -　 |


|**sets 族** | **sorted sets 族** | **strings 族** | **transactions 族** |**hyperloglog 族** |**scripting 族** |
| --- | --- | --- | --- | --- | -- |
| sadd | zadd | append | discard |pfadd |eval |
| scard | zcard | bitcount | exec |pfcount| evalsha |
| sdiff | zcount | bitop | multi |pfmerge| script debug |
| sdiffstore | zincrby | bitpos | unwatch |  |script exists|
| sinter | zinterstore | decr | watch | | script flush |
| sinterstore | zlexcount | decrby | -　 | | script load |
| sismember | zrange | get | -　 | |script kill |
| smembers | zrangebylex | getbit | -　 |
| smove | zrangebyscore | getrange | -　 |
| spop | zrank | getset | -　 |
| srandmember | zrem | incr | -　 |
| srem | zremrangebylex | incrby | -　 |
| sscan | zremrangebyrank | incrbyfloat | -　 |
| sunion | zremrangebyscore | mget | -　 |
| sunionstore | zrevrange | mset | -　 |
| -　 | zrevrangebylex | msetnx | -　 |
|- 　 | zrevrangebyscore | psetex | -　 |
| -　 | zscore | setex | -　 |
| -　 | zrevrank | set | -　 |
| -　 | zscan | setbit | -　 |
| -　 | zunionstore | setnx | -　 |
| -　 | -　 | setrange | -　 |
| -　 | -　 | strlen | -　 |

**主从版 Redis 不支持的命令：**

| **connection 族** | **geo 族** | **keys 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- |
| swapdb | geoadd | touch |  bgrewriteaof | bitfield |
| -　 | geohash |  restore |  bgsave |- 　 |
| -　 | geopos |  object |  client kill | -　 |
| -　 | geodist |  unlink |  sync | -　 |
| -　 | georadius |  wait | client getname | -　 |
| -　 | georadiusbymember | migrate | client pause |- 　 |
| -　 | -　 | dump | client reply | -　 |
| -　 | -　 |  -　 | client setname |- 　 |
| -　 | -　 |  -　 |  command count | -　 |
| -　 | -　 | - 　 |  command getkeys | -　 |
| -　 | -　 |  -　 | command info |- 　 |
| -　 | -　 |  -　 | slaveof | -　 |
| -　 | -　 | -　 | config rewrite |- 　 |
| -　 | -　 | - 　 |  config set | 　- |
| -　 | -　 |  - | config resetstat | -　 |
| -　 | -　 |  -　 |  debug object | -　 |
| -　 | -　 |  -　 | debug segfault | -　 |
| -　 | -　 | -　 | role  | -　 |
| -　 | -　 | -　 | save  | -　 |
| -　 | -　 | -　 | lastsave |- 　 |
| -　 | -　 |  -　 | shutdown  | -　 |

    


