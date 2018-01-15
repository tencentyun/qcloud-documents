集群版 Redis 是腾讯云自研的一款高可用、高可靠的 Redis 服务。通过主从热备自动容灾提供高可用性，通过多份数据拷贝保证高可靠性。集群版 Redis 支持开源 V2.8 版本协议，集群版分布式的架构将数据分布存储在多台物理机上，彻底摆脱单机容量和资源限制，容量支持范围为 60~300G。

但目前集群版处于维护阶段，暂不对外售卖

## 集群版 Redis 支持命令

|Key（键）|	String（字符串）|	Hash（哈希表）|	List（列表）|	Set（集合）	|SortedSet（有序集合）|
|---------|---------|---------|
|EXPIREAT	|APPEND|	HEXISTS|	LINDEX|	SADD|	ZADD|
|PERSIST|	BITCOUNT|	HGET|	LINSERT	|SCARD|	ZCARD|
|PEXPIRE	|BITOP|	HGETALL	|LLEN	|SDIFF|	ZCOUNT|
|PEXPIREAT	|DECR|	HINCRBY	|LPOP	|SDIFFSTORE|	ZINCRBY|
|PTTL|	DECRBY|	HINCRBYFLOAT|	LPUSH|	SINTER	| ZRANGE|
|RESTORE|	GET|	HKEYS|	LPUSHX|	SINTERSTORE|	ZRANGEBYSCORE|
|TTL	|GETBIT	|HLEN|	LRANGE|	SISMEMBER|	ZRANK|
|TYPE|	GETRANGE	|HMGET|	LREM	|SMEMBERS|	ZREM|
|DEL|	GETSET|	HMSET|	LSET	|SMOVE|	ZREMRANGEBYRANK|
|DUMP|	INCR	|HSET|	LTRIM|	SPOP|	ZREMRANGEBYSCORE
|EXISTS|	INCRBY|	HSETNX|	RPOP	|SRANDMEMBER|	ZREVRANGE
|EXPIRE|	INCRBYFLOAT|	HVALS|	RPOPLPUSH|	SREM|	ZREVRANGEBYSCORE
| 	|MGET|	HSCAN	|RPUSH|	SUNION|	ZREVRANK
| 	|MSET|	HDEL|	RPUSHX|	SUNIONSTORE|	ZSCORE
| 	|MSETNX|	 |	 |	SSCAN|	ZUNIONSTORE
| 	|PSETEX|	| 	 |	 |	ZINTERSTORE
| 	|SET|	 	| 	| 	|ZSCAN
| 	|SETBIT| |	 	| 	 	|ZRANGEBYLEX
| 	|SETEX|	 |	 	| 	|ZLEXCOUNT
| 	|SETNX|	 |	 	| 	|ZREMRANGEBYLEX
| 	|SETRANGE|	| 	| 	 |	 |
| 	|STRLEN|	 |	| 	 |	 ||



其他支持的命令

|Transaction（事务）|	Connection（连接）|
|---------|---------|
|DISCARD|	AUTH|
|EXEC|	ECHO|
|MULTI|	PING|
|UNWATCH|	QUIT|
|WATCH|	SELECT（仅 Select0）|


## 集群版 Redis 不支持命令

|Key(键)	|Script（脚本）|	Server（服务器）|	Pub/Sub（发布/订阅）|	HyperLogLog|
|---------|---------|---------|---------|---------|
|KEYS	|EVALSHA|BGREWRITEAOF|PSUBSCRIBE|PFADD|
|MIGRATE|	SCRIPT| EXISTS	|BGSAVE|	PUBLISH	PFCOUNT|
|MOVE|	SCRIPT FLUSH|	CLIENT GETNAME	|PUBSUB|	PFMERGE|
|OBJECT|	SCRIPT KILL|	CLIENT KILL|	PUNSUBSCRIBE	 ||
|RANDOMKEY|	SCRIPT LOAD|	CLIENT LIST	|SUBSCRIBE  ||	 
|RENAME	| |	CLIENT SETNAME|	UNSUBSCRIBE	| |
|RENAMENX	| 	|CONFIG GET|	 	 ||
|SORT	 |	|CONFIG RESETSTAT|||	 	 
|SCAN	| |	CONFIG REWRITE||| 
| 	| 	|CONFIG SET|  |  |
| 	| 	| 	 	DBSIZE	 |  |  |
| 	| 	|	 	DEBUG OBJECT	|  |  |
| 	| 	| 	 	DEBUG SEGFAULT|  |  |	 	 
| 	| 	| 	 	FLUSHALL	 |  |  | 
| 	| 	| 	 	FLUSHDB	|  |  |
| 	| 	| 	 	INFO	 	 |  |  |
| 	| 	| 	 	LASTSAVE	|  |  | 
| 	| 	| 	 	MONITOR	 	 |  |  |
| 	| 	| 	 	PSYNC	 	 |  |  |
| 	| 	| 	 	SAVE	 	 |  |  |
| 	| 	| 	 	SHUTDOWN	|  |  |	 
| 	| 	| 	 	SLAVEOF	 	 |  |  |
| 	| 	| 	 	SLOWLOG	 	 |  |  |
| 	| 	| 	 	SYNC	 	 |  |  |
| 	| 	| 	 	TIME	 	 |  |  | |



##  其他限制
1. Key 大小限制：127 Byte，单 key 下 value 数据大小限制：1,000,000 Byte。
2. 长连接若 30 分钟无请求会自动断开，请在业务中尝试重连。

## 集群版事务说明

1. 若事务部分成功，则失败部分不能回滚。
2. 事务进行时，所涉及的 Key 均被锁定，此时读写 Key 会失败。
3. 已支持的命令，均能在事务中使用。

