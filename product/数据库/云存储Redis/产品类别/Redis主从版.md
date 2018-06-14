主从版 Redis 是腾讯云基于开源的 Redis 打造的一款高可用、高可靠的 Redis 服务。通过主从热备自动容灾提供高可用性，通过多份数据拷贝保证高可靠性。主从版 Redis 支持开源 V2.8 版本协议，容量支持范围为 1~60G。

## 主从版 Redis 支持命令
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

## 主从版 Redis 不支持命令
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
