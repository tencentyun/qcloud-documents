Redis 集群版是腾讯云基于社区版 Redis 4.0 打造的全新版本，采用分布式架构，支持垂直和水平的扩缩容，拥有高度的灵活性、可用性和高达千万级 QPS 的高性能。Redis 集群版支持水平方向3分片 - 128分片的扩展，垂直方向1个 - 5个副本集的扩展，扩容、缩容、迁移过程业务几乎无感知，做到最大的系统可用性。![](https://main.qcloudimg.com/raw/28b67a0b4de50e751fd2119876019ffd.svg)

## 集群规格
- 分片规格（GB）：4、8、12、16、20、24、28、32
- 分片数量：3、5、8、12、16、24、32、64、96、128 
- 副本数量：1、2、3、4、5 

## 集群模式
- Redis集群模式数据将会自动分片，系统将提供数据均衡，数据迁移功能。
- 集群模式支持的分片规格为4GB - 32GB。
- 集群模式的命令相对与非集群模式有一定的兼容性，主要体现在跨 Slot（槽位）数据访问，详细说明请参见 [使用限制](https://cloud.tencent.com/document/product/239/18336?!preview&!editLang=zh#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6)。

## 副本说明
- 副本数等于1时，Redis 提供数据主从实时热备，提供数据高可靠和高可用，HA 系统监测到节点故障后，会将请求切换到从节点，并且新增一个从节点加入到系统。
- 副本数大于1时，Redis 提供数据主从实时热备，并且提供从节点只读功能。

## 功能特性
**灵活性** 
Redis 集群版支持最小3个节点到最大128个节点的水平扩容和缩容，支持垂直的1个副本集到5个副本集的扩容和缩容，通过实例的调整支持多种应用场景。
**可用性** 
Redis 集群版的水平方向（分片数量）和垂直方向（副本数量）的扩容、缩容对业务完全无感知，做到高度的系统可用性。
 **兼容性**
Redis 集群版在应用场景中，支持社区版原生 Cluster 的使用场景，兼容 Jedis 等智能客户端使用场景，兼容 Codis 使用场景。
 **可运维**
Redis 集群版将最大程度的开放系统的能力，提供分片级的监控和管理，分片数据迁移和均衡，以及大 Key 监控、热 Key 监控的高级功能，做到系统完整的可管理，可运维。

## 适用场景
**主从高可用场景**
选择单个节点并为节点选择1个副本集，从而达到主从高可用，提供双机热备，故障自动切换的能力，保证 Redis 服务的高可靠和高可用。
 **读写分离场景**  
节点副本数大于1，可开启云数据库 Redis 自动读写分离能力，在垂直方向提供单节点读性能扩充，最大支持5个副本集，支持配置主节点以及各副本节点的读访问权重。 
**多分片高性能场景**
Redis 集群版自动启动分片模式，通过将不同的 Key 分配到多个节点达到水平扩充系统性能的能力。

## 使用限制
集群版数据自动 Hash 分片，集群模式暂时不提供小于4GB的规格。
集群模式下，Redis 对命令对支持情况分为**支持**、**有限支持**、**自定义命令**、**不支持**，对于不支持的命令系统将返回如下错误：
```
 select 1
 (error) ERR unknown command 'select'
```

**不支持的命令：**
集群版不支持多 DB，但支持`select 0`命令，因其可能对性能产生负面影响，建议使用专用数据库。所以以下命令会被阻止，并在执行时产生错误：
-  MOVE
-  SWAPDB
    
因数据持久性和备份可通过控制台来管理，所以以下相关命令不支持：
- BGREWRITEAOF
- BGSAVE
- LASTSAVE
    
系统的复制和高可用由云数据库 Redis 后台统一管理，因对其的操作可能带来稳定性风险，所以以下命令将不支持：
- REPLCONF
- SLAVEOF
- SYNC / PSYNC

其他不支持的命令：
- DEBUG 
- PFDEBUG
- OBJECT
- SHUTDOWN
- MONITOR
- COMMAND
- SCRIPT-DEBUG
- LATENCY
- READONLy
- TIME
- WAIT
- MODULE
- DBSIZE

**有限支持的命令：**
为兼容 Jedis cluster 的使用场景，云数据库 Redis 对 Cluster 支持命令返回对 IP 列表进行了修改，返回信息中每个节点的 IP 地址为实例的 VIP。
- CLUSTER NODES
- CLUSTER SLOTS 
- CONFIG GET

跨 Slot 命令支持
集群版目前支持跨 Slot 访问的命令包括：
- MGET
- MSET
- DEL

目前不支持跨 Slot 执行的命令，系统会返回如下错误：
 `(error) CROSSSLOT Keys in request don't hash to the same slot`
 
不支持跨 Slot 访问的命令如下：
- UNLINK
- EXISTS
- BRPOP
- BLPOP
- SINTER
- STNTERSTORE
- SUNION
- SDIFF
- SDIFFSTORE
- MSETNX
- PFCOUNT
- PFMERGE

**事务支持**
集群版支持事务相关的命令，但是事务必须以 WATCH 命令开始，事务中的KEY要求存储在相同的 SLOT 中，WATCH 的 KEY 需要和事务相关的 KEY 保持在同一 SLOT，集群模式下的事务使用建议使用 HashTag。支持的相关命令包括如下：
- WATCH
- MULTI
- EXEC
- DISCARD
- UNWATCH
     
**自定义命令：**
Redis 集群版通过 VIP 封装，在集群模式下提供了单机版的使用体验，对业务的使用带来的极大的便利，但是对运维不够透明，因此通过自定义命令来弥补这块空缺，支持集群中每个节点的访问，支持方式为在原有命令的参数列表最右边新增一个参数【节点ID】，COMMAND arg1 arg2 ... [节点ID]，节点 ID 可通过`cluster nodes`命令，或者在控制台中获取：
  ```
	10.1.1.1:2000> cluster nodes
	25b21f1836026bd49c52b2d10e09fbf8c6aa1fdc 10.0.0.15:6379@11896 slave 36034e645951464098f40d339386e9d51a9d7e77 0 1531471918205 1 connected
	da6041781b5d7fe21404811d430cdffea2bf84de 10.0.0.15:6379@11170 master - 0 1531471916000 2 connected 10923-16383
	36034e645951464098f40d339386e9d51a9d7e77 10.0.0.15:6379@11541 myself,master - 0 1531471915000 1 connected 0-5460
	53f552fd8e43112ae68b10dada69d3af77c33649 10.0.0.15:6379@11681 slave da6041781b5d7fe21404811d430cdffea2bf84de 0 1531471917204 3 connected
	18090a0e57cf359f9f8c8c516aa62a811c0f0f0a 10.0.0.15:6379@11428 slave ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171 0 1531471917000 2 connected
	ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171 10.0.0.15:6379@11324 master - 0 1531471916204 0 connected 5461-10922

	原生命令：
	info server
	自定义命令:
	info server ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171
	
	SCAN 命令示例：
	scan 0 238b45926a528c85f40ae89d6779c802eaa394a2
	scan 0 match a* 238b45926a528c85f40ae89d6779c802eaa394a2
	
	KEYS 命令示例：
	keys a* 238b45926a528c85f40ae89d6779c802eaa394a2
  ```
  
 自定义命令列表：
- INFO	 
- MEMORY
- SLOWLOG
- FLUSHDB
- PING
- KEYS（支持 hashtag，优先匹配 hashtag）
- SCAN（支持 hashtag，优先匹配 hashtag）

**支持的命令：**
  Redis 集群版除上述命令以外的命令都支持。

