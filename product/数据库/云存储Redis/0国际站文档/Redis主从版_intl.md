### About Redis Master/Slave
 Redis Master/Slave is the most common Redis version, which is compatible with protocols and commands in Redis 2.8, and will be compatible with Redis 4.0 soon. Redis Master/Slave uses a master/slave node deployment architecture to provide data persistence and backup. It is suitable for scenarios that require data reliability and availability. The master node provides daily service access and the slave node provides high availability (HA). When the master node fails, the system automatically switches the service to the slave node to ensure the smooth business operation.<br>

 ![](https://main.qcloudimg.com/raw/a153968edd3ffb4b93288fa85b0783af.svg)

 ### Features of Redis Master/Slave

 -   **Robust service**<br>
     Adopts the master/slave backup architecture, with the master/slave nodes located on different physical servers. The master node supports external access. You can add, delete, modify and query data through Redis command lines and general clients. When the master node fails, the self-developed HA system automatically switches the service to the slave node to ensure the smooth business operation.
         
 -   **Reliable data**<br>
     The data persistence feature is enabled by default, and all data is stored to disks. It provides the data backup feature. You can roll back or clone instances using the corresponding backup set, so as to avoid misoperation on data.

 ### Use limits

  - Redis Master/Slave is available with a capacity ranging from 0.25 GB to 60 GB. If you need higher specifications, you can select CKV Master/Slave, which supports up to 384 GB, or Redis Cluster, which supports up to 2 TB.
  - Redis Master/Slave provides the ability to handle up to 100,000 queries per second. If you need higher QPS, select Redis Cluster or CKV Cluster, which supports up to 10 million QPS.

 ### Compatibility
 Redis Master/Slave is built on Redis 2.8 and is compatible with Redis protocols and commands. Self-built Redis databases can be smoothly migrated to Redis Standard. A data transmission service (DTS) is also provided for migration of incremental Redis data to ensure the smooth business transition. Command compatibility is as follows:<vr>
 - **Commands supported by Redis Master/Slave**

 | **connection family** | **hashes family** | **keys family** | **lists family** | **pub/sub family** | **server family** | 
 | --- | --- | --- | --- | --- | --- |
 | auth | hdel | del | lindex | psubscribe | command | 
 | echo | hexists | scan | linsert | pubsub | dbsize |
 | ping | hget | exists | llen | publish | info | 
 | quit | hgetall | expire | lpop | punsubscribe | time | 
 | select | hincrby | expireat | lpush | subscribe |   | 
 |   | hincrbyfloat | keys | lpushx | unsubscribe |   | 
 |   | hkeys | type | lrange |   |   | 
 |   | hlen | move | lrem |   |   |
 |   | hmget | ttl | lset |   |   |
 |   | hmset | persist | ltrim |   |   |
 |   | hset | pexpire | rpop |   |   |
 |   | hsetnx | pexpireat | rpoplpush |   |   |
 |   | hstrlen | pttl | rpush |   |   |
 |   | hvals | randomkey | rpushx |   |   |
 |   | hscan | rename | blpop |   |   |
 |   |   | renamenx | brpop |   |   |
 |   |   | sort | brpoplpush |   |   |



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
 |   | zscore | setex |   |
 |   | zrevrank | set |   |
 |   | zscan | setbit |   |
 |   | zunionstore | setnx |   |
 |   |   | setrange |   |
 |   |   | strlen |   |

 - **Commands not supported by Redis Master/Slave**

 | **cluster family** | **connection family** | **geo family** | **hyperloglog family** | **keys family** | **scripting family** | **server family** | **strings family** |
 | --- | --- | --- | --- | --- | --- | --- | --- |
 | cluster addslots | swapdb | geoadd | pfadd | touch | eval | bgrewriteaof | bitfield |
 | cluster count-failure-reports |   | geohash | pfcount | restore | evalsha | bgsave |   |
 | cluster countkeyinslot |   | geopos | pfmerge | object | script debug | client kill |   |
 | cluster delslots |   | geodist |   | unlink | script exists | client list |   |
 | cluster failover |   | georadius |   | wait | script flush | client getname |   |
 | cluster forget |   | georadiusbymember |   | migrate | script kill | client pause |   |
 | cluster getkeysinslot |   |   |   | dump | script load | client reply |   |
 | cluster info |   |   |   |   |   | client setname |   |
 | cluster keyslot |   |   |   |   |   | command count |   |
 | cluster meet |   |   |   |   |   | command getkeys |   |
 | cluster nodes |   |   |   |   |   | command info |   |
 | cluster replicate |   |   |   |   |   | config get |   |
 | cluster reset |   |   |   |   |   | config rewrite |   |
 | cluster saveconfig |   |   |   |   |   | config set |   |
 | cluster set-config-epoch |   |   |   |   |   | config resetstat |   |
 | cluster setslot |   |   |   |   |   | debug object |   |
 | cluster slaves |   |   |   |   |   | debug segfault |   |
 | cluster slots |   |   |   |   |   | flushall |   |
 | readonly |   |   |   |   |   | flushdb |   |
 | readwrite |   |   |   |   |   | lastsave |   |
 |   |   |   |   |   |   | monitor |   |
 |   |   |   |   |   |   | role |   |
 |   |   |   |   |   |   | save |   |
 |   |   |   |   |   |   | shutdown |   |
 |   |   |   |   |   |   | slaveof |   |
 |   |   |   |   |   |   | slowlog |   |
 |   |   |   |   |   |   | sync |   |

