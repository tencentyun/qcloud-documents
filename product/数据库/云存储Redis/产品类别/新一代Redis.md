新一代 Redis 是腾讯云自研的一款高可用、高可靠的 Redis 服务。通过主从热备自动容灾提供高可用性，通过多份数据拷贝保证高可靠性。新一代 Redis 支持 3.0 如 geo 等大部分协议，容量支持范围为 32G~384G。
新一代 Redis 成熟稳定，容灾机制健全，服务成熟，服务于海量第三方用户以及腾讯自有业务，日访问量超过一万亿次，久经考验，开发者完全可以放心使用。

## 新一代 Redis 支持命令
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
| sscan | zremrangebyrank | incrbyfloat | 　 |
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

## 新一代 Redis 不支持命令
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
1. 与开源协议不一样，腾讯云 Redis 对于 pttl 等设置毫秒的过期时间，展示的最小单位为秒
2. 与开源协议不一样，腾讯云 Redis 目前支持 string 类型 32MB 最大 value

## 系统架构说明
![](https://mc.qcloudimg.com/static/img/2d76234a9bc57419f5b23b0398516600/jiagou.png)
新一代 Redis 系统包括如下几大模块： 
### 接入服务（Access）： 
Access 是接入服务，实现请求路由功能，用于分发用户数据请求。 
为了提升接入转发服务与数据引擎间的通讯效率，Access 与后续会提到的数据引擎（Cache）是同一个操作系统进程。该进程作为核心进程，兼顾了 Access 和 Cache 的能力，但如果一个核心进程不分配共享内存资源，则会作为一个专用的 Access 存在。因此，Access 本身具备一定的独立扩展能力，有就近接入、流量控制、API 访问等功能，可根据实际需要独立部署。 
 
### 数据引擎（Cache）： 
Cache 是一个完全自主研发的内存数据存储引擎，存储 Key-value 数据，一台物理服务器上部署一个 CKV 核心进程，同时承担 Access 和 Cache 的职能，并拥有一个共享内存空间，用于业务数据存储。单台 Cache 服务器逻辑上分为多个分片（Cache Unit，简称 CU，CU 最小 1GB），供不同的业务使用。每个 CU 是一个按业务容量分配的连续的共享内存空间来存放表数据，表由 65536 个存储单元（slot）构成,每个 Slot 存放一个或多个键值对。若干个 slot 存储在一个 CU 当中，单 slot 也可占用整个 CU。Cache 服务器中还有心跳（Heartbeat）组件，定期向管控模块反馈本机状态。

 
### 缓存组（KV Set）： 
Set 是一组 Cache 服务器的集合，是逻辑概念，SET 可横向扩展，由多个 SET 组成一个逻辑区域（Region），物理上称为集群。 
新一代 Redis 架构中，一个 SET 最少需要部署三台 Cache 服务器，Cache 服务器间并没有主从关系，当业务被创建时，会在不同 Cache 服务器分别建立三个分片 CU，分片类型分为主分片和备分片，主 CU 和备 CU 必须分布在不同的 Cache 服务器上。CU 的主备切换通过 Raft 协议自动实现。用户数据访问经过负载均衡服务到达 Access，由 Access 路由到相应的 Cache 服务器。所有数据的读写均发生在主 CU 上，备分片不对外提供读写功能。

 
### 管理控制模块（Control Master）： 
Control Master 提供服务路由、配置下发、heart beat、监控数据等功能，Master 进程负责相关的业务逻辑，ETCD 用于存储管控配置信息。新一代 Redis 默认采用一主一从模式存储分别部署在 2 台机器上，由主节点提供读写服务。


### 运维支持服务（OSS，Operating Support System）： 
OSS 由 OSS 服务器和其数据库构成，对接外部运维系统，实现日常运维管理操作。 
OSS 服务器实现对 CKV 其他组件状态管理、部署、迁移、备份、监控、告警、审计等功能，通过外部调用可实现自动化部署。建议配置两台 OSS 服务器，主备模式部署，出现异常需要手工切换。OSS 服务器有专用的数据库存储 OSS 的配置信息。
 

## 自动容灾流程
![](https://mc.qcloudimg.com/static/img/47589d17c709a7044ea59a244b9514e4/ronzai.png)
当业务 A 主分片所在的 Cache 服务器故障时，Cache 服务器内部从现有备分片中选举出新的主分片并进行切换，切换主分片后，在有可用空间的前提下（例如新增一台 Cache 服务器）通过重建备分片，切换过程不需要用户做任务处理。

 
 

##  扩缩容流程

### 物理计算资源角色灵活： 
系统的缓存物理服务器可按需灵活承担多种角色，在 Access 和 Cache 间灵活切换。Cache 和 Access 本身是同一个进程（提升性能，减少延时，有 33% 几率直接命中主分片），正常情况下同机部署，同步扩容或缩容。但是，在有需要的场景下，Cache 服务器不加载分片进行存储数据时则可退化为无状态的 Access，实现 Access 的独立扩展性。 
 
### Cache 服务器的弹性扩展： 
业务表空间使用率过高或者过低时，可对业务表进行容量扩容或者缩容；当 Set 中的 Cache 服务器剩余内存空间不足时，可以进行以 Set 为单位平行扩展。 

### 业务扩（缩）容：
业务扩缩容是通过分片迁移的模式实现的，方法是需要在集群内新增一台 CACHE 机器，业务会把主分片数据迁移到新的 CACHE 机器上，备分片也会迁移到集群内其他剩余内存容量满足要求的 CACHE 上，。若现有 Cache 服务器的未占用内存无法满足扩（缩）容要求，这需要在当前集群中调度满足要求的三台 Cache 服务器，创建符合新容量要求的 CU 分片，通过业务迁移功能实现扩（缩）容。 

### 业务搬迁：
过程如下图所示：目标分片向源分片请求 dump slot 命令；完成待搬迁 slots 的 dump；追加 binlog 如果是搬迁，还需要切换路由；封禁源分片当中 slots 的读写；发布新路由并广播。
![](https://mc.qcloudimg.com/static/img/7536ca8e3e66769f8a25a97c6eb2f8ff/kuorong.png)

