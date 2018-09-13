
### Redis主从版简介
Redis主从版是最通用的Redis版本，兼容Redis 2.8版本的协议和命令，近期会推出兼容Redis 4.0的版本，采用主从节点部署架构，提供数据持久化和备份，适用于对数据可靠性、可用性都有要求的场景。主节点提供日常服务访问，备节点提供 HA 高可用，当主节点发生故障，系统会自动切换至备节点，保证业务平稳运行。<br>

![](https://main.qcloudimg.com/raw/a153968edd3ffb4b93288fa85b0783af.svg)

### Redis主从版特点

-   **服务可靠**<br>
    采用双机主备架构，主备节点位于不同物理机。主节点对外提供访问，用户可通过 Redis 命令行和通用客户端进行数据的增删改查操作。当主节点出现故障，自研的 HA 系统会自动进行主备切换，保证业务平稳运行。
        
-   **数据可靠**<br>
    默认开启数据持久化功能，数据全部落盘。支持数据备份功能，用户可以针对备份集回滚实例或者克隆实例，有效的解决数据误操作等问题。

### 使用限制

 - Redis主从版支持0.25～60GB规格，需要更大的主从版规格可以选择CKV主从版(最大可支持384GB)，或者选择集群版最大可支持2TB的容量；
 - Redis主从版的性能最大支持10万QPS，需要更高的QPS请选择Redis集群版，或者CKV集群版，最大可支持1000万QPS；

### 兼容性
云数据库 Redis 主从版在 Redis 2.8基础上进行开发，兼容 Redis 协议命令。自建的 Redis 数据库可以平滑迁移至 Redis 标准版。并且提供数据传输工具（DTS）可以进行增量的 Redis 迁移，保证业务平稳过渡。命令兼容性如下表：<vr>
- **主从版 Redis 支持命令**

| **connection 族** | **hashes 族** | **keys 族** | **lists 族** | **pub/sub 族** | **server 族** | 
| --- | --- | --- | --- | --- | --- |
| auth | hdel | del | lindex | psubscribe | command | 
| echo | hexists | scan | linsert | pubsub | dbsize |
| ping | hget | exists | llen | publish | info | 
| quit | hgetall | expire | lpop | punsubscribe | time | 
| select | hincrby | expireat | lpush | subscribe |   | 
|   | hincrbyfloat | keys | lpushx | unsubscribe |   | 
| 　 | hkeys | type | lrange | 　 |   | 
| 　 | hlen | move | lrem | 　 |   |
| 　 | hmget | ttl | lset | 　 |   |
| 　 | hmset | persist | ltrim | 　 |   |
| 　 | hset | pexpire | rpop | 　 |   |
| 　 | hsetnx | pexpireat | rpoplpush | 　 |   |
| 　 | hstrlen | pttl | rpush | 　 |   |
| 　 | hvals | randomkey | rpushx | 　 |   |
| 　 | hscan | rename | blpop | 　 |   |
| 　 | 　 | renamenx | brpop | 　 | 　 |
| 　 | 　 | sort | brpoplpush | 　 | 　 |



|**sets 族** | **sorted sets 族** | **strings 族** | **transactions 族** |
| --- | --- | --- | --- |
| sadd | zadd | append | discard |
| scard | zcard | bitcount | exec |
| sdiff | zcount | bitop | multi |
| sdiffstore | zincrby | bitpos | unwatch |
| sinter | zinterstore | decr | watch |
| sinterstore | zlexcount | decrby | 　 |
| sismember | zrange | get | 　 |
| smembers | zrangebylex | getbit | 　 |
| smove | zrangebyscore | getrange | 　 |
| spop | zrank | getset | 　 |
| srandmember | zrem | incr | 　 |
| srem | zremrangebylex | incrby | 　 |
| sscan | zremrangebyrank | incrbyfloat | 　 |
| sunion | zremrangebyscore | mget | 　 |
| sunionstore | zrevrange | mset | 　 |
| 　 | zrevrangebylex | msetnx | 　 |
| 　 | zrevrangebyscore | psetex | 　 |
| 　 | zscore | setex | 　 |
| 　 | zrevrank | set | 　 |
| 　 | zscan | setbit | 　 |
| 　 | zunionstore | setnx | 　 |
| 　 | 　 | setrange | 　 |
| 　 | 　 | strlen | 　 |

- **主从版 Redis 不支持命令**

| **cluster 族** | **connection 族** | **geo 族** | **hyperloglog 族** | **keys 族** | **scripting 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cluster addslots | swapdb | geoadd | pfadd | touch | eval | bgrewriteaof | bitfield |
| cluster count-failure-reports | 　 | geohash | pfcount | restore | evalsha | bgsave | 　 |
| cluster countkeyinslot | 　 | geopos | pfmerge | object | script debug | client kill | 　 |
| cluster delslots | 　 | geodist | 　 | unlink | script exists | client list | 　 |
| cluster failover | 　 | georadius | 　 | wait | script flush | client getname | 　 |
| cluster forget | 　 | georadiusbymember | 　 | migrate | script kill | client pause | 　 |
| cluster getkeysinslot | 　 | 　 | 　 | dump | script load | client reply | 　 |
| cluster info | 　 | 　 | 　 | 　 | 　 | client setname | 　 |
| cluster keyslot | 　 | 　 | 　 | 　 | 　 | command count | 　 |
| cluster meet | 　 | 　 | 　 | 　 | 　 | command getkeys | 　 |
| cluster nodes | 　 | 　 | 　 | 　 | 　 | command info | 　 |
| cluster replicate | 　 | 　 | 　 | 　 | 　 | config get | 　 |
| cluster reset | 　 | 　 | 　 | 　 | 　 | config rewrite | 　 |
| cluster saveconfig | 　 | 　 | 　 | 　 | 　 | config set | 　 |
| cluster set-config-epoch | 　 | 　 | 　 | 　 | 　 | config resetstat | 　 |
| cluster setslot | 　 | 　 | 　 | 　 | 　 | debug object | 　 |
| cluster slaves | 　 | 　 | 　 | 　 | 　 | debug segfault | 　 |
| cluster slots | 　 | 　 | 　 | 　 | 　 | flushall | 　 |
| readonly | 　 | 　 | 　 | 　 | 　 | flushdb | 　 |
| readwrite | 　 | 　 | 　 | 　 | 　 | lastsave | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | monitor | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | role | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | save | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | shutdown | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | slaveof | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | slowlog | 　 |
| 　 | 　 | 　 | 　 | 　 | 　 | sync | 　 |

    


