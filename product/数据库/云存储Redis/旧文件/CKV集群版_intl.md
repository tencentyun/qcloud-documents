### About CKV Cluster
 - **Overview of CKV engine**
 Tencent Cloud CKV engine is a high-performance, low-latency and persistent distributed KV storage service independently developed by Tencent Cloud. It is widely used in Tencent's WeChat, open platform, Tencent Cloud, Tencent Game and e-commerce platforms, with more than one trillion visits per day. Tencent Cloud provides CKV Master/Slave and CKV Cluster, allowing flexible deployment in different business scenarios.
 - **About CKV Cluster**
 CKV Cluster provides dual-replica Cluster instances, which helps easily break through the bottleneck of a single thread, so as to respond to the business needs for large capacity or high performance. CKV Cluster is compatible with Redis 3.2 protocols and commands, and supports up to 128 shards and a capacity of up to 2 TB.

 ### Features of CKV Cluster

 - **Robust service**<br>
 Adopts the master/slave backup architecture, with the master/slave nodes located on different physical servers. The master node supports external access. You can add, delete, modify and query data through Redis command lines and general clients. The slave node provides data backup and high availability. When the master node fails, the self-developed HA system automatically switches the service to the slave node to ensure the smooth business operation.        
 - **Reliable data**<br>
 The data persistence feature is enabled by default, and all data is stored to disks. It provides the data backup feature. You can roll back or clone instances using the corresponding backup set, so as to avoid misoperation on data.
 - **Lower latency**<br>
 CKV uses a high-performance network platform and a proxy-free architecture, greatly reducing access delay and network delay. The delay can be reduced as much as 60% in high load scenarios.
 - **Read-only slave**<br>
 CKV Cluster can improve the read performance by 40% in average by enabling the slave. Read-only Slave is disabled by default in CKV Cluster, and can be applied for by submitting tickets. Since might be a replication delay between CKV master and slave nodes, data from earlier versions may be read with the "Read-only Slave" enabled. Before enabling this feature, make sure it is acceptable to read inconsistent data.
 - **Smooth upgrade**<br>
 With unique schemes, CKV Cluster can ensure the business-unaware version upgrade, thus maximizing the service availability.


 ### Application scenarios
 - **Large volume of data in a single instance**
 As a distributed architecture, CKV Cluster is suitable for scenarios with large capacity in a single instance. The capacity can exceed the upper limit of 384 GB of CKV Master/Slave.

 - **High QPS and concurrence requirements**
 As a distributed architecture, CKV Cluster distributes the read and the write among multiple nodes. With Keys evenly distributed, QPS increases linearly with the number of nodes. CKV Cluster supports up to 128 shards, and QPS can reach 10 million at most.

 - **Insensitive protocol support**
 Few protocols supported by the open source version are not supported in CKV Cluster. For more information, see the commands not supported by CKV Cluster.

 ### Connection example
 CKV Cluster only supports the password format: "Instance id:password". For example, if your instance ID is crs-bkuza6i3 and the password is abcd1234, the connection command is redis-cli -h IP address -p port -a crs-bkuza6i3:abcd1234.


 ### Other limits
 - In CKV, the expiration time in milliseconds set by PTTL is displayed in the smallest unit (in sec), which is different with Redis Community.
 - For the Key of string type supported in CKV, the maximum size of the value is 32 MB, which is different with Redis Community.
 - Except mset and mget, other batch operations require that all the Keys in these batches be in the same slot, otherwise an error message "CROSSSLOT Keys in request don't hash to the same slot" may occur.
 - When a shard is full, subscribe/psubscribe takes up a certain amount of memory, which affects the addition of a new subscription, but does not affect the publish of the subscribed channel.

 ### Notes
 - The default size of a single shard in CKV Cluster is 4 GB, so it is recommended that the value size of a single Key do not exceed 4 GB.
 - CKV Cluster supports monitoring on clusters. The monitoring on shards will be available soon.


 ### Compatibility
 - **Commands supported by CKV Cluster**<br>

 | **connection family** | **geo family** | **hashes family** | **hyperloglog family** | **keys family** | **lists family** | **pub/sub family** | 
 | --- | --- | --- | --- | --- | --- | --- |
 | auth | geoadd | hdel | pfadd | del | lindex | psubscribe | 
 | echo | geohash | hexists | pfcount | exists | linsert | pubsub | 
 | ping | geopos | hget | pfmerge | expire | llen | publish | time |
 | quit | geodist | hgetall |   | expireat| lpop | punsubscribe |  |
 | select | georadius | hincrby |   | type | lpush | subscribe |   |
 |   | georadiusbymember | hincrbyfloat |  | ttl| lpushx | unsubscribe |   |
 |   |   | hkeys |   | persist | lrange |   |   |
 |   |   | hlen |   | pexpire | lrem |   |   |
 |   |   | hmget |   | pexpireat | lset |   |   |
 |   |   | hmset |   | pttl | ltrim |   |   |
 |   |   | hset |   | rename | rpop |   |   |
 |   |   | hsetnx |   | renamenx | rpoplpush |   |   |
 |   |   | hstrlen |   | sort | rpush |   |   |
 |   |   | hvals |   |  | rpushx |   |   |
 |   |   | hscan |   |  |   |   |   |

 | **sets family** | **sorted sets family** | **strings family** | **transactions family** |**server family** | 
 | --- | --- | --- | --- | --- |
 | sadd | zadd | append | discard | command |
 | scard | zcard | bitcount | exec | dbsize |
 | sdiff | zcount | bitop | multi | |
 | sdiffstore | zincrby | bitpos | unwatch | |
 | sinter | zinterstore | decr | watch | |
 | sinterstore | zlexcount | decrby |   | |
 | sismember | zrange | get |   | |
 | smembers | zrangebylex | getbit |   |  |
 | smove | zrangebyscore | getrange |   | |
 | spop | zrank | getset |   | |
 | srandmember | zrem | incr |   | |
 | srem | zremrangebylex | incrby |   | |
 | sscan | zremrangebyrank | incrbyfloat |   | |
 | sunion | zremrangebyscore | mget |   | |
 | sunionstore | zrevrange | mset |   | |
 |   | zrevrangebylex | msetnx |   | |
 |   | zrevrangebyscore | psetex |   | |
 |   | zrevrank | set |   | |
 |   | zscan | setbit |   | |
 |   | zscore | setex |   | |
 |   | zunionstore | setnx |   | |
 |   |   | setrange |   | |
 |   |   | strlen |   | | |

 - **Commands not supported by CKV Cluster**<br>

 | **cluster family** | **connection family** | **keys family** | **lists family** | **scripting family** | **server family** | **strings family** |
 | --- | --- | --- | --- | --- | --- | --- |
 | cluster addslots | swapdb | touch | blpop | eval | bgrewriteaof | bitfield |
 | cluster count-failure-reports |   | restore | brpop | evalsha | bgsave |   |
 | cluster delslots |   | object | brpoplpush | script debug | client kill |   |
 | cluster failover |   | unlink |   | script exists | client list |   |
 | cluster forget |   | wait |   | script flush | client getname |   |
 | cluster meet |   | migrate |   | script kill | client pause |   |
 |cluster replicate  |   | dump |   | script load | client reply |   |
 | cluster reset |   | scan |   |   | client setname |   |
 | cluster saveconfig |   |keys   |   |   | command count |   |
 |cluster set-config-epoch  |   |move   |   |   | command getkeys |   |
 | cluster setslot |   |randomkey   |   |   | command info |   |
 |cluster slaves  |   |   |   |   | config get |   |
 |readonly  |   |   |   |   | config rewrite |   |
 | readwrite |   |   |   |   | config set |   |
 |  |   |   |   |   | config resetstat |   |
 |  |   |   |   |   | debug object |   |
 |  |   |   |   |   | debug segfault |   |
 |  |   |   |   |   | flushall |   |
 |  |   |   |   |   | flushdb |   |
 |  |   |   |   |   | lastsave |   |
 |   |   |   |   |   | monitor |   |
 |   |   |   |   |   | role |   |
 |   |   |   |   |   | save |   |
 |   |   |   |   |   | shutdown |   |
 |   |   |   |   |   | slaveof |   |
 |   |   |   |   |   | slowlog |   |
 |   |   |   |   |   | sync |   |
 |   |   |   |   |   | info |   | |
