

### CKV主从版简介
- **CKV引擎简介**：腾讯云数据库CKV引擎是腾讯自主研发的高性能、低延时、持久化、分布式KV存储服务。在腾讯的微信平台、开放平台、腾讯云、腾讯游戏和电商平台广泛使用，日访问量超过万亿次。腾讯云CKV支持主从版、集群版，能够满足不同的业务场景;

- **CKV主从版简介**： CKV主从版采用主从节点部署架构，提供数据持久化和备份，适用于对数据可靠性、可用性都有要求的场景。主节点提供日常服务访问，备节点提供 HA(高可用)，当主节点发生故障，系统会自动切换至备节点，保证业务平稳运行。CKV主从版兼容Redis3.2版本的命令和协议，支持4～384GB的规格，满足大容量存储的需求；<br>

![](https://main.qcloudimg.com/raw/6f25e510793817075cf017844ca1cf03.svg)

### CKV主从版特点

- **服务可靠**<br>
采用双机主备架构，主备节点位于不同物理机。主节点对外提供访问，用户可通过 Redis 命令行和通用客户端进行数据的增删改查操作，备节点提供数据备份以及高可用。当主节点出现故障，自研的 HA 系统会自动进行主备切换，保证业务平稳运行；        
- **数据可靠**<br>
默认开启数据持久化功能，数据全部存储到磁盘。支持数据备份功能，用户可以针对备份集回滚实例或者克隆实例，有效的解决数据误操作等问题；
- **更低时延**<br>
CKV采用高性能网络平台、以及无Proxy架构，极大的降低的访问延迟和网络延迟。在高负载场景下，时延最多降低高达60%；
- **从机只读**<br>
CKV主从版可以通过开启从机来显著提升读性能，平均情况可以提升40%的读性能，CKV主从版默认未开启从机只读，目前可以提工单申请从机只读。由于CKV主节点和从节点存在复制延迟，开通从机只读后，会出现读到旧版本数据的情况，开通此功能前请确认业务可以接受读数据不一致的情况；
- **平滑升级**<br>
CKV主从版通过独有的方案，保证版本升级做到业务无感知，从而保证服务的最大可用性；



### 使用限制

- CKV主从版的性能最大支持12+万QPS，需要更高的QPS请选择CKV集群版，最大可支持1000万QPS；
- CKV对于pttl的设置毫秒的过期时间，展示的最小单位为秒，与社区版Redis不一致；
- CKV目前支持的string类型Key，Value最大Size为32MB，与社区版Redis不一致；

###  连接示例
CKV主从版仅支持以下密码格式，“实例 id:密码” 的格式类型，例如您的实例 id 是 crs-bkuza6i3，设置的密码是 abcd1234，则连接命令如下redis-cli -h IP地址 -p 端口 -a crs-bkuza6i3:abcd1234。

### 兼容性
- CKV主从版支持的命令<br>

| **connection 族** | **geo 族** | **hashes 族** | **hyperloglog 族** | **keys 族** | **lists 族** | **pub/sub 族** | **server 族** | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| auth | geoadd | hdel | pfadd | del | lindex | psubscribe | command |
| echo | geohash | hexists | pfcount | scan | linsert | pubsub | dbsize |
| ping | geopos | hget | pfmerge | exists | llen | publish | info |
| quit | geodist | hgetall | 　 | expire | lpop | punsubscribe | time |
| select | georadius | hincrby | 　 | expireat | lpush | subscribe | 　 |
| 　 | georadiusbymember | hincrbyfloat | 　 | keys | lpushx | unsubscribe | 　 |
| 　 | 　 | hkeys | 　 | type | lrange | 　 | 　 |
| 　 | 　 | hlen | 　 | move | lrem | 　 | 　 |
| 　 | 　 | hmget | 　 | ttl | lset | 　 | 　 |
| 　 | 　 | hmset | 　 | persist | ltrim | 　 | 　 |
| 　 | 　 | hset | 　 | pexpire | rpop | 　 | 　 |
| 　 | 　 | hsetnx | 　 | pexpireat | rpoplpush | 　 | 　 |
| 　 | 　 | hstrlen | 　 | pttl | rpush | 　 | 　 |
| 　 | 　 | hvals | 　 | randomkey | rpushx | 　 | 　 |
| 　 | 　 | hscan | 　 | rename | 　 | 　 | 　 |
| 　 | 　 | 　 | 　 | renamenx | 　 | 　 | 　 |
| 　 | 　 | 　 | 　 | sort | 　 | 　 | 　 |


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

- CKV主从版不支持的命令<br>

| **cluster 族** | **connection 族** | **keys 族** | **lists 族** | **scripting 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- | --- | --- |
| cluster addslots | swapdb | touch | blpop | eval | bgrewriteaof | bitfield |
| cluster count-failure-reports | 　 | restore | brpop | evalsha | bgsave | 　 |
| cluster countkeyinslot | 　 | object | brpoplpush | script debug | client kill | 　 |
| cluster delslots | 　 | unlink | 　 | script exists | client list | 　 |
| cluster failover | 　 | wait | 　 | script flush | client getname | 　 |
| cluster forget | 　 | migrate | 　 | script kill | client pause | 　 |
| cluster getkeysinslot | 　 | dump | 　 | script load | client reply | 　 |
| cluster info | 　 | 　 | 　 | 　 | client setname | 　 |
| cluster keyslot | 　 | 　 | 　 | 　 | command count | 　 |
| cluster meet | 　 | 　 | 　 | 　 | command getkeys | 　 |
| cluster nodes | 　 | 　 | 　 | 　 | command info | 　 |
| cluster replicate | 　 | 　 | 　 | 　 | config get | 　 |
| cluster reset | 　 | 　 | 　 | 　 | config rewrite | 　 |
| cluster saveconfig | 　 | 　 | 　 | 　 | config set | 　 |
| cluster set-config-epoch | 　 | 　 | 　 | 　 | config resetstat | 　 |
| cluster setslot | 　 | 　 | 　 | 　 | debug object | 　 |
| cluster slaves | 　 | 　 | 　 | 　 | debug segfault | 　 |
| cluster slots | 　 | 　 | 　 | 　 | flushall | 　 |
| readonly | 　 | 　 | 　 | 　 | flushdb | 　 |
| readwrite | 　 | 　 | 　 | 　 | lastsave | 　 |
| 　 | 　 | 　 | 　 | 　 | monitor | 　 |
| 　 | 　 | 　 | 　 | 　 | role | 　 |
| 　 | 　 | 　 | 　 | 　 | save | 　 |
| 　 | 　 | 　 | 　 | 　 | shutdown | 　 |
| 　 | 　 | 　 | 　 | 　 | slaveof | 　 |
| 　 | 　 | 　 | 　 | 　 | slowlog | 　 |
| 　 | 　 | 　 | 　 | 　 | sync | 　 |
