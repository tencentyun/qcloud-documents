### About CKV Master/Slave
 - **Overview of CKV engine**: Tencent Cloud CKV engine is a high-performance, low-latency and persistent distributed KV storage service independently developed by Tencent Cloud. It is widely used in Tencent's WeChat, open platform, Tencent Cloud, Tencent Game and e-commerce platforms, with more than one trillion visits per day. Tencent Cloud provides CKV Master/Slave and CKV Cluster, allowing flexible deployment in different business scenarios.

 - **Overview of CKV Master/Slave**: CKV Master/Slave uses master/slave node deployment architecture to provide data persistence and backup. It is suitable for scenarios that require data reliability and availability. The Master node provides daily service access and the Slave node provides HA (high availability). When the Master node fails, the system automatically switches the service to the Slave node to ensure the smooth business operation. CKV Master/Slave is compatible with Redis 3.2 commands and protocols, supporting the specifications of 4-384 GB to meet the mass storage needs.<br>
 ![](https://main.qcloudimg.com/raw/6f25e510793817075cf017844ca1cf03.svg)

 ### Features of CKV Master/Slave

 - **Robust service**<br>
 Adopts the master/slave backup architecture, with the master/slave nodes located on different physical servers. The master node supports external access. You can add, delete, modify and query data through Redis command lines and general clients. The slave node provides data backup and high availability. When the master node fails, the self-developed HA system automatically switches the service to the slave node to ensure the smooth business operation.        
 - **Reliable data**<br>
 The data persistence feature is enabled by default, and all data is stored to disks. It provides the data backup feature. You can roll back or clone instances using the corresponding backup set, so as to avoid misoperation on data.
 - **Lower latency**<br>
 CKV uses a high-performance network platform and a proxy-free architecture, greatly reducing access delay and network delay. The delay can be reduced as much as 60% in high load scenarios.
 - **Read-only slave**<br>
 CKV Master/Slave can improve the read performance by 40% in average by enabling the slave. Read-only Slave is disabled by default in CKV Master/Slave, and can be applied for by submitting tickets. Since might be a replication delay between CKV master and slave nodes, data from earlier versions may be read with the "Read-only Slave" enabled. Before enabling this feature, make sure it is acceptable to read inconsistent data.
 - **Smooth upgrade**<br>
 With unique schemes, CKV Master/Slave can ensure the business-unaware version upgrade, thus maximizing the service availability.



 ### Use limits

 - CKV Master/Slave supports the maximum performance of up to over 120,000 QPS. If you need higher QPS, select CKV Cluster, which supports up to 10 million QPS.
 - In CKV, the expiration time in milliseconds set by PTTL is displayed in the smallest unit (in sec), which is different with Redis Community.
 - For the Key of string type supported in CKV, the maximum size of the value is 32 MB, which is different with Redis Community.

 ### Connection example
 CKV Master/Slave only supports the password format: "Instance id:password". For example, if your instance ID is crs-bkuza6i3 and the password is abcd1234, the connection command is redis-cli -h IP address -p port -a crs-bkuza6i3:abcd1234.

 ### Compatibility
 - Commands supported in CKV Master/Slave<br>

 | **connection family** | **geo family** | **hashes family** | **hyperloglog family** | **keys family** | **lists family** | **pub/sub family** | **server family** | 
 | --- | --- | --- | --- | --- | --- | --- | --- |
 | auth | geoadd | hdel | pfadd | del | lindex | psubscribe | command |
 | echo | geohash | hexists | pfcount | scan | linsert | pubsub | dbsize |
 | ping | geopos | hget | pfmerge | exists | llen | publish | info |
 | quit | geodist | hgetall |   | expire | lpop | punsubscribe | time |
 | select | georadius | hincrby |   | expireat | lpush | subscribe |   |
 |   | georadiusbymember | hincrbyfloat |   | keys | lpushx | unsubscribe |   |
 |   |   | hkeys |   | type | lrange |   |   |
 |   |   | hlen |   | move | lrem |   |   |
 |   |   | hmget |   | ttl | lset |   |   |
 |   |   | hmset |   | persist | ltrim |   |   |
 |   |   | hset |   | pexpire | rpop |   |   |
 |   |   | hsetnx |   | pexpireat | rpoplpush |   |   |
 |   |   | hstrlen |   | pttl | rpush |   |   |
 |   |   | hvals |   | randomkey | rpushx |   |   |
 |   |   | hscan |   | rename |   |   |   |
 |   |   |   |   | renamenx |   |   |   |
 |   |   |   |   | sort |   |   |   | |


 | **sets family** | **sorted sets family** | **strings family** | **transactions family** |
 | --- | --- | --- | --- |
 | sadd | zadd | append | discard |
 | scard | zcard | bitcount | exec |
 | sdiff | zcount | bitop | multi |
 | sdiffstore | zincrby | bitpos | unwatch |
 | sinter | zinterstore | decr | watch |
 | sinterstore | zlexcount | decrby |   |
 | sismember | zrange | get |   |
 | smembers | zrangebylex | getbit |   |
 | smove | zrangebyscore | getrange |   |
 | spop | zrank | getset |   |
 | srandmember | zrem | incr |   |
 | srem | zremrangebylex | incrby |   |
 | sscan | zremrangebyrank | incrbyfloat |   |
 | sunion | zremrangebyscore | mget |   |
 | sunionstore | zrevrange | mset |   |
 |   | zrevrangebylex | msetnx |   |
 |   | zrevrangebyscore | psetex |   |
 |   | zrevrank | set |   |
 |   | zscan | setbit |   |
 |   | zscore | setex |   |
 |   | zunionstore | setnx |   |
 |   |   | setrange |   |
 |   |   | strlen |   | |

 - Commands not supported in CKV Master/Slave<br>

 | **cluster family** | **connection family** | **keys family** | **lists family** | **scripting family** | **server family** | **strings family** |
 | --- | --- | --- | --- | --- | --- | --- |
 | cluster addslots | swapdb | touch | blpop | eval | bgrewriteaof | bitfield |
 | cluster count-failure-reports |   | restore | brpop | evalsha | bgsave |   |
 | cluster countkeyinslot |   | object | brpoplpush | script debug | client kill |   |
 | cluster delslots |   | unlink |   | script exists | client list |   |
 | cluster failover |   | wait |   | script flush | client getname |   |
 | cluster forget |   | migrate |   | script kill | client pause |   |
 | cluster getkeysinslot |   | dump |   | script load | client reply |   |
 | cluster info |   |   |   |   | client setname |   |
 | cluster keyslot |   |   |   |   | command count |   |
 | cluster meet |   |   |   |   | command getkeys |   |
 | cluster nodes |   |   |   |   | command info |   |
 | cluster replicate |   |   |   |   | config get |   |
 | cluster reset |   |   |   |   | config rewrite |   |
 | cluster saveconfig |   |   |   |   | config set |   |
 | cluster set-config-epoch |   |   |   |   | config resetstat |   |
 | cluster setslot |   |   |   |   | debug object |   |
 | cluster slaves |   |   |   |   | debug segfault |   |
 | cluster slots |   |   |   |   | flushall |   |
 | readonly |   |   |   |   | flushdb |   |
 | readwrite |   |   |   |   | lastsave |   |
 |   |   |   |   |   | monitor |   |
 |   |   |   |   |   | role |   |
 |   |   |   |   |   | save |   |
 |   |   |   |   |   | shutdown |   |
 |   |   |   |   |   | slaveof |   |
 |   |   |   |   |   | slowlog |   |
 |   |   |   |   |   | sync |   | |
