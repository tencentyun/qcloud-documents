

### CKV 主从版简介
- **CKV 引擎简介**：腾讯云数据库 CKV 引擎是腾讯自主研发的高性能、低延时、持久化、分布式 KV 存储服务。在腾讯的微信平台、开放平台、腾讯云、腾讯游戏和电商平台广泛使用，日访问量超过万亿次。腾讯云 CKV 支持主从版、集群版，能够满足不同的业务场景;

- **CKV 主从版简介**： CKV 主从版采用主从节点部署架构，提供数据持久化和备份，适用于对数据可靠性、可用性都有要求的场景。主节点提供日常服务访问，备节点提供 HA(高可用)，当主节点发生故障，系统会自动切换至备节点，保证业务平稳运行。CKV 主从版兼容 Redis3.2 版本的命令和协议，支持 4～384GB 的规格，满足大容量存储的需求；

![](https://main.qcloudimg.com/raw/6f25e510793817075cf017844ca1cf03.svg)

### CKV 主从版特点

- **服务可靠**
采用双机主备架构，主备节点位于不同物理机。主节点对外提供访问，用户可通过 Redis 命令行和通用客户端进行数据的增删改查操作，备节点提供数据备份以及高可用。当主节点出现故障，自研的 HA 系统会自动进行主备切换，保证业务平稳运行；        
- **数据可靠**
默认开启数据持久化功能，数据全部存储到磁盘。支持数据备份功能，用户可以针对备份集回滚实例或者克隆实例，有效的解决数据误操作等问题；
- **更低时延**
CKV 采用高性能网络平台、以及无 Proxy 架构，极大的降低的访问延迟和网络延迟。在高负载场景下，时延最多降低高达 60%；
- **从机只读**
CKV 主从版可以通过开启从机来显著提升读性能，平均情况可以提升 40% 的读性能，CKV 主从版默认未开启从机只读，目前可以提工单申请从机只读。由于 CKV 主节点和从节点存在复制延迟，开通从机只读后，会出现读到旧版本数据的情况，开通此功能前请确认业务可以接受读数据不一致的情况；
- **平滑升级**
CKV 主从版通过独有的方案，保证版本升级做到业务无感知，从而保证服务的最大可用性；



### 使用限制

- CKV 引擎主从版的性能最大支持 12+万 QPS，需要更高的 QPS 请选择 CKV 集群版，最大可支持 1000万 QPS；
- CKV 引擎对于 pttl 的设置毫秒的过期时间，展示的最小单位为秒，与社区版 Redis 不一致；
- CKV 引擎目前支持的 string 类型 Key，Value 最大 Size 为 32MB；
- CKV 引擎的实例连接方式为“实例 id:密码”,这里和社区版连接方式不一致；
- CKV 引擎dbsize命令实现的时间复杂度为O(n),执行命令时需要遍历当前DB的所有Key，请谨慎使用；
- CKV 引擎会内置一个string类型的key：`{ckv_plus_pub_sub}_patterns`，该key用于支持pub、sub订阅功能，如果你使用订阅功能，请不要删除该Key否则订阅会失效；
- CKV 引擎事件通知暂时不支持过期和淘汰策略通知；
- CKV 引擎的淘汰策略，暂时只支持`volatile-lru`，或者关闭淘汰机制，对应的参数为`maxmemory-policy`


###  连接示例
CKV 主从版仅支持以下密码格式，“实例 id:密码” 的格式类型，例如您的实例 id 是 crs-bkuza6i3，设置的密码是 abcd1234，则连接命令如下 redis-cli -h IP地址 -p 端口 -a crs-bkuza6i3:abcd1234。

### 兼容性
- CKV 主从版支持的命令<br>

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


|**sets 族** | **sorted sets 族** | **strings 族** | **transactions 族** | **scripting 族** |
| --- | --- | --- | --- | --- |
| sadd | zadd | append | discard |eval|
| scard | zcard | bitcount | exec |script debug|
| sdiff | zcount | bitop | multi |script exists|
| sdiffstore | zincrby | bitpos | unwatch |script flush|
| sinter | zinterstore | decr | watch |script kill|
| sinterstore | zlexcount | decrby | 　 |script load |
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

- CKV 主从版不支持的命令<br>

| **cluster 族** | **connection 族** | **keys 族** | **lists 族** | **scripting 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- | --- | --- |
| cluster addslots | swapdb | touch | blpop | evalsha | bgrewriteaof | bitfield |
| cluster count-failure-reports | 　 | restore | brpop |  | bgsave | 　 |
| cluster countkeyinslot | 　 | object | brpoplpush |  | client kill | 　 |
| cluster delslots | 　 | unlink | 　 |  | client list | 　 |
| cluster failover | 　 | wait | 　 |  | client getname | 　 |
| cluster forget | 　 | migrate | 　 |  | client pause | 　 |
| cluster getkeysinslot | 　 | dump | 　 | | client reply | 　 |
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
