
### 集群版Redis
集群版 Redis 是腾讯云自研的一款高可用、高可靠的 Redis 服务。通过主从热备自动容灾提供高可用性，通过多份数据拷贝保证高可靠性。集群版 Redis 支持开源 V3.0 版本协议，集群版分布式的架构将数据分布存储在多台物理机上，彻底摆脱单机容量和资源限制，容量支持范围为 64~384G。

### 集群版使用场景
**1.单实例数据量较大**
由于集群版是分布式架构，所以适用于单实例容量较大的场景，容量可突破目前主从版 60GB 的上限

**2.QPS及并发要求高**
由于集群版是分布式架构，将读写分摊在多个节点上，在 Key 分布均匀的情况下，QPS 随节点数线性增涨

**3.协议支持不敏感**
集群版对比开源版本在协议支持上有少量协议不支持，请详见下文不支持的命令


## 集群版Redis 支持命令

| **connection 族** | **geo 族** | **hashes 族** | **hyperloglog 族** | **keys 族** | **lists 族** | **pub/sub 族** | **server 族** | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| auth | geoadd | hdel | pfadd | del | lindex | psubscribe | command |
| echo | geohash | hexists | pfcount | exists | linsert | pubsub | dbsize |
| ping | geopos | hget | pfmerge | expire | llen | publish | time |
| quit | geodist | hgetall | 　 | expireat| lpop | punsubscribe |  |
| select | georadius | hincrby | 　 | type | lpush | subscribe | 　 |
| 　 | georadiusbymember | hincrbyfloat |  | ttl| lpushx | unsubscribe | 　 |
| 　 | 　 | hkeys | 　 | persist | lrange | 　 | 　 |
| 　 | 　 | hlen | 　 | pexpire | lrem | 　 | 　 |
| 　 | 　 | hmget | 　 | pexpireat | lset | 　 | 　 |
| 　 | 　 | hmset | 　 | pttl | ltrim | 　 | 　 |
| 　 | 　 | hset | 　 | rename | rpop | 　 | 　 |
| 　 | 　 | hsetnx | 　 | renamenx | rpoplpush | 　 | 　 |
| 　 | 　 | hstrlen | 　 | sort | rpush | 　 | 　 |
| 　 | 　 | hvals | 　 |  | rpushx | 　 | 　 |
| 　 | 　 | hscan | 　 |  | 　 | 　 | 　 |



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
| 　 | zrevrank | set | 　 |
| 　 | zscan | setbit | 　 |
| 　 | zscore | setex | 　 |
| 　 | zunionstore | setnx | 　 |
| 　 | 　 | setrange | 　 |
| 　 | 　 | strlen | 　 |

## 集群版 Redis 不支持命令

| **cluster 族** | **connection 族** | **keys 族** | **lists 族** | **scripting 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- | --- | --- |
| cluster addslots | swapdb | touch | blpop | eval | bgrewriteaof | bitfield |
| cluster count-failure-reports | 　 | restore | brpop | evalsha | bgsave | 　 |
| cluster delslots | 　 | object | brpoplpush | script debug | client kill | 　 |
| cluster failover | 　 | unlink | 　 | script exists | client list | 　 |
| cluster forget | 　 | wait | 　 | script flush | client getname | 　 |
| cluster meet | 　 | migrate | 　 | script kill | client pause | 　 |
|cluster replicate  | 　 | dump | 　 | script load | client reply | 　 |
| cluster reset | 　 | scan | 　 | 　 | client setname | 　 |
| cluster saveconfig | 　 |keys 　 | 　 | 　 | command count | 　 |
|cluster set-config-epoch  | 　 |move 　 | 　 | 　 | command getkeys | 　 |
| cluster setslot | 　 |randomkey 　 | 　 | 　 | command info | 　 |
|cluster slaves  | 　 | 　 | 　 | 　 | config get | 　 |
|readonly  | 　 | 　 | 　 | 　 | config rewrite | 　 |
| readwrite | 　 | 　 | 　 | 　 | config set | 　 |
|  | 　 | 　 | 　 | 　 | config resetstat | 　 |
|  | 　 | 　 | 　 | 　 | debug object | 　 |
|  | 　 | 　 | 　 | 　 | debug segfault | 　 |
|  | 　 | 　 | 　 | 　 | flushall | 　 |
|  | 　 | 　 | 　 | 　 | flushdb | 　 |
|  | 　 | 　 | 　 | 　 | lastsave | 　 |
| 　 | 　 | 　 | 　 | 　 | monitor | 　 |
| 　 | 　 | 　 | 　 | 　 | role | 　 |
| 　 | 　 | 　 | 　 | 　 | save | 　 |
| 　 | 　 | 　 | 　 | 　 | shutdown | 　 |
| 　 | 　 | 　 | 　 | 　 | slaveof | 　 |
| 　 | 　 | 　 | 　 | 　 | slowlog | 　 |
| 　 | 　 | 　 | 　 | 　 | sync | 　 |
| 　 | 　 | 　 | 　 | 　 | info | 　 |

###  集群版连接示例
集群版仅支持以下密码格式
实例 “id:密码” 的格式类型，例如您的实例 id 是 crs-bkuza6i3，设置的密码是 abcd1234，则连接命令如下
redis-cli -h IP地址 -p 端口 -a crs-bkuza6i3:abcd1234


###  其他限制
1.与开源协议不一样，腾讯云 Redis 对于 pttl 等设置毫秒的过期时间，展示的最小单位为秒。
2.与开源协议不一样，腾讯云 Redis 目前支持 string 类型 32MB 最大 value。
3.除了 mset,mget 批量操作的时候不受限制之外，其他的批量操作，都要求这些批量的 key 都是在相同的 slot 中，否则会报错，提示 CROSSSLOT Keys in request don't hash to the same slot。
4.当分片写满后，subscribe/psubscribe 需要占用一定内存，新增全新订阅会受到影响，不影响已订阅 channel 的 publish。

###  特殊说明
1.目前集群版单个分片的大小默认是 4GB，因此建议不要单个 key 的 value 大小超过 4GB。
2.目前集群版提供的监控使集群维度的，shard 维度的监控敬请期待。
