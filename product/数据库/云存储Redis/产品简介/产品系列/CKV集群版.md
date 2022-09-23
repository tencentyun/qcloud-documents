
>?云数据库 Redis CKV 版已暂停售卖，建议您选择 [云数据库 Redis 内存版](https://cloud.tencent.com/document/product/239/18336)。

云数据库 Redis CKV 版（集群架构）提供双副本集群实例，突破单线程瓶颈，可极大满足对于大容量或高性能的业务需求，CKV 版（集群架构）兼容 Redis 3.2 版本协议和命令，最大支持128个分片，支持12GB - 48TB容量。

## 功能特性
- **服务可靠**
采用双机主从架构，主从节点位于不同物理机。主节点对外提供访问，用户可通过 Redis 命令行和通用客户端进行数据的增删改查操作，从节点提供数据备份以及高可用。当主节点出现故障，自研的 HA 系统会自动进行主从切换，保证业务平稳运行。        
- **数据可靠**
默认开启数据持久化功能，数据全部存储到磁盘。支持数据备份功能，用户可针对备份集回滚实例或者克隆实例，有效的解决数据误操作等问题。
- **更低时延**
CKV 采用高性能网络平台、以及无 Proxy 架构，极大的降低了访问延迟和网络延迟。在高负载场景下，时延最多降低高达60%。
- **从机只读**
CKV 版（集群架构）可以通过开启从机来显著提升读性能，平均情况可以提升40%的读性能，CKV 版（集群架构）默认未开启从机只读，目前可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请从机只读。由于 CKV 主节点和从节点存在复制延迟，开通从机只读后，会出现读到旧版本数据的情况，开通此功能前请确认业务可以接受读数据不一致的情况。
- **平滑升级**
CKV 版（集群架构）通过独有的方案，保证版本升级做到业务无感知，从而保证服务的最大可用性。

## 适用场景
- **单实例数据量较大**
CKV 版（集群架构）是分布式架构，适用于单实例容量较大的场景，容量可突破 CKV 标准版384GB上限。
- **QPS 及并发要求高**
由于 CKV 版（集群架构）是分布式架构，将读写分摊在多个节点上，在 Key 分布均匀的情况下，QPS 随节点数线性增涨，目前最大支持128个分片，千万级 QPS 性能 。
- **协议支持不敏感**
CKV 版（集群架构）对比开源版本在协议支持上有少量协议不支持。

##  连接示例
CKV 版（集群架构）仅支持“实例 ID:密码”的密码格式类型，例如您的实例 ID 是 crs-bkuza6i3，设置的密码是 abcd1234，则连接命令是 `redis-cli -h IP 地址 -p 端口 -a crs-bkuza6i3:abcd1234`。


##  使用限制
- CKV 引擎的 pttl 设置展示最小单位为秒，与社区版 Redis 不一致。
- 目前支持的 string 类型 Key，Value 最大 Size 为32MB，与社区版 Redis 不一致。
- 除 mset、mget 批量操作不受限制之外，其他批量操作，都要求批量的 Key 是在相同的 slot 中，否则会报错，提示`CROSSSLOT Keys in request don't hash to the same slot`。
- 当分片写满后，subscribe、psubscribe 需要占用一定内存，新增全新订阅会受到影响，不影响已订阅 channel 的 publish。

##  特殊说明
- 目前 CKV 版（集群架构）单个分片的大小默认是4GB，因此建议单个 key 的 value 大小不要超过4GB。
- 目前 CKV 版（集群架构）提供集群维度的监控。


## 兼容性

**CKV 版（集群架构）支持的命令**：
 
| **connection 族** | **geo 族** | **hashes 族** | **hyperloglog 族** | **keys 族** | **lists 族** | **pub/sub 族** | 
| --- | --- | --- | --- | --- | --- | --- |
| auth | geoadd | hdel | pfadd | del | lindex | psubscribe | 
| echo | geohash | hexists | pfcount | exists | linsert | pubsub | 
| ping | geopos | hget | pfmerge | expire | llen | publish | time |
| quit | geodist | hgetall | -　 | expireat| lpop | punsubscribe | - |
| select | georadius | hincrby | -　 | type | lpush | subscribe | -　 |
| -　 | georadiusbymember | hincrbyfloat | - | ttl| lpushx | unsubscribe | -　 |
| -　 | -　 | hkeys | -　 | persist | lrange | -　 | -　 |
| -　 | -　 | hlen | -　 | pexpire | lrem | -　 | -　 |
| -　 | -　 | hmget | -　 | pexpireat | lset | -　 | -　 |
| -　 | -　 | hmset | -　 | pttl | ltrim | -　 | -　 |
| -　 | -　 | hset | -　 | rename | rpop | -　 | -　 |
| -　 | -　 | hsetnx | -　 | renamenx | rpoplpush | -　 | -　 |
| -　 | -　 | hstrlen | -　 | sort | rpush | -　 | -　 |
| -　 | -　 | hvals | -　 | - | rpushx | -　 | -　 |
| -　 |- 　 | hscan | -　 |-  | -　 | -　 | -　 |

|**sets 族** | **sorted sets 族** | **strings 族** | **transactions 族** |**server 族** | 
| --- | --- | --- | --- | --- |
| sadd | zadd | append | discard | command |
| scard | zcard | bitcount | exec | dbsize |
| sdiff | zcount | bitop | multi |-
| sdiffstore | zincrby | bitpos | unwatch |-
| sinter | zinterstore | decr | watch |-
| sinterstore | zlexcount | decrby | -　 |-
| sismember | zrange | get | -　 |-
| smembers | zrangebylex | getbit | -　 |-
| smove | zrangebyscore | getrange | -　 |-
| spop | zrank | getset | -　 |-
| srandmember | zrem | incr | -　 |-
| srem | zremrangebylex | incrby | -　 |-
| sscan | zremrangebyrank | incrbyfloat | -　 |-
| sunion | zremrangebyscore | mget | -　 |-
| sunionstore | zrevrange | mset | -　 |-
| -　 | zrevrangebylex | msetnx | -　 |-
| -　 | zrevrangebyscore | psetex | -　 |-
| -　 | zrevrank | set | -　 |-
| -　 | zscan | setbit |- 　 |-
| -　 | zscore | setex | -　 |-
| -　 | zunionstore | setnx | -　 |-
| -　 | -　 | setrange | -　 |-
| -　 | -　 | strlen | -　 |-

**CKV 版（集群架构）不支持的命令：**

| **cluster 族** | **connection 族** | **keys 族** | **lists 族** | **scripting 族** | **server 族** | **strings 族** |
| --- | --- | --- | --- | --- | --- | --- |
| cluster addslots | swapdb | touch | blpop | eval | bgrewriteaof | bitfield |
| cluster count-failure-reports | -　 | restore | brpop | evalsha | bgsave | -　 |
| cluster delslots | -　 | object | brpoplpush | script debug | client kill | -　 |
| cluster failover | -　 | unlink | -　 | script exists | client list | -　 |
| cluster forget | -　 | wait | -　 | script flush | client getname | -　 |
| cluster meet | -　 | migrate | -　 | script kill | client pause | -　 |
|cluster replicate  | -　 | dump | -　 | script load | client reply | -　 |
| cluster reset | -　 | scan | -　 | -　 | client setname | -　 |
| cluster saveconfig | -　 |keys 　 | 　- | -　 | command count | -　 |
|cluster set-config-epoch  | -　 |move 　 | -　 | -　 | command getkeys | -　 |
| cluster setslot | -　 |randomkey 　 | -　 | -　 | command info | -　 |
|cluster slaves  | -　 | -　 | -　 | -　 | config get | 　- |
|readonly  | -　 | -　 | -　 | -　 | config rewrite |- 　 |
| readwrite |- 　 | -　 | -　 | -　 | config set | -　 |
| - | -　 | -　 | -　 | -　 | config resetstat | -　 |
| - | -　 | -　 | -　 | -　 | debug object | -　 |
| - | -　 | -　 | -　 | -　 | debug segfault | -　 |
| - | -　 | -　 | -　 | -　 | flushall | -　 |
|-  | -　 | -　 | -　 | -　 | flushdb | -　 |
| - | -　 | -　 | -　 | -　 | lastsave | -　 |
| -　 | -　 | -　 | -　 | -　 | monitor | -　 |
| -　 | -　 | -　 | -　 | -　 | role | -　 |
| -　 | -　 | -　 | -　 | -　 | save | -　 |
| -　 | -　 | -　 | -　 | -　 | shutdown | -　 |
| -　 | -　 | -　 | -　 | -　 | slaveof | -　 |
| -　 | -　 | -　 | -　 | -　 | slowlog | -　 |
| -　 | -　 | -　 | -　 | -　 | sync | -　 |
| -　 | -　 | -　 | -　 | -　 | info | 　- |


