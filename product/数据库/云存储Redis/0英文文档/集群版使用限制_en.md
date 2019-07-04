

### 1. Supported Commands

<table>
	<tbody>
		<tr>
			<th><strong>Key</strong></th>
			<th><strong>String</strong></th>
			<th><strong>Hash</strong></th>
			<th><strong>List</strong></th>
			<th><strong>Set</strong></th>
			<th><strong>SortedSet</strong></th>
		</tr>
		<tr>
			<td>EXPIREAT</td>
			<td>APPEND</td>
			<td>HEXISTS</td>
			<td>LINDEX</td>
			<td>SADD</td>
			<td>ZADD</td>
		</tr>
		<tr>
			<td>PERSIST</td>
			<td>BITCOUNT</td>
			<td>HGET</td>
			<td>LINSERT</td>
			<td>SCARD</td>
			<td>ZCARD</td>
		</tr>
		<tr>
			<td>PEXPIRE</td>
			<td>BITOP</td>
			<td>HGETALL</td>
			<td>LLEN</td>
			<td>SDIFF</td>
			<td>ZCOUNT</td>
		</tr>
		<tr>
			<td>PEXPIREAT</td>
			<td>DECR</td>
			<td>HINCRBY</td>
			<td>LPOP</td>
			<td>SDIFFSTORE</td>
			<td>ZINCRBY</td>
		</tr>
		<tr>
			<td>PTTL</td>
			<td>DECRBY</td>
			<td>HINCRBYFLOAT</td>
			<td>LPUSH</td>
			<td>SINTER</td>
			<td>ZRANGE</td>
		</tr>
		<tr>
			<td>RESTORE</td>
			<td>GET</td>
			<td>HKEYS</td>
			<td>LPUSHX</td>
			<td>SINTERSTORE</td>
			<td>ZRANGEBYSCORE</td>
		</tr>
		<tr>
			<td>TTL</td>
			<td>GETBIT</td>
			<td>HLEN</td>
			<td>LRANGE</td>
			<td>SISMEMBER</td>
			<td>ZRANK</td>
		</tr>
		<tr>
			<td>TYPE</td>
			<td>GETRANGE</td>
			<td>HMGET</td>
			<td>LREM</td>
			<td>SMEMBERS</td>
			<td>ZREM</td>
		</tr>
		<tr>
			<td>DEL</td>
			<td>GETSET</td>
			<td>HMSET</td>
			<td>LSET</td>
			<td>SMOVE</td>
			<td>ZREMRANGEBYRANK</td>
		</tr>
		<tr>
			<td>DUMP</td>
			<td>INCR</td>
			<td>HSET</td>
			<td>LTRIM</td>
			<td>SPOP</td>
			<td>ZREMRANGEBYSCORE</td>
		</tr>
		<tr>
			<td>EXISTS</td>
			<td>INCRBY</td>
			<td>HSETNX</td>
			<td>RPOP</td>
			<td>SRANDMEMBER</td>
			<td>ZREVRANGE</td>
		</tr>
		<tr>
			<td>EXPIRE</td>
			<td>INCRBYFLOAT</td>
			<td>HVALS</td>
			<td>RPOPLPUSH</td>
			<td>SREM</td>
			<td>ZREVRANGEBYSCORE</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>MGET</td>
			<td>HSCAN</td>
			<td>RPUSH</td>
			<td>SUNION</td>
			<td>ZREVRANK</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>MSET</td>
			<td>HDEL</td>
			<td>RPUSHX</td>
			<td>SUNIONSTORE</td>
			<td>ZSCORE</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>MSETNX</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SSCAN</td>
			<td>ZUNIONSTORE</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>PSETEX</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>ZINTERSTORE</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>SET</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>ZSCAN</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>SETBIT</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>ZRANGEBYLEX</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>SETEX</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>ZLEXCOUNT</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>SETNX</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>ZREMRANGEBYLEX</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>SETRANGE</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>STRLEN</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>Other Supported Commands</p>

<table>
	<tbody>
		<tr>
			<th><strong>Transaction</strong></th>
			<th><strong>Connection</strong></th>
		</tr>
		<tr>
			<td>DISCARD</td>
			<td>AUTH</td>
		</tr>
		<tr>
			<td>EXEC</td>
			<td>ECHO</td>
		</tr>
		<tr>
			<td>MULTI</td>
			<td>PING</td>
		</tr>
		<tr>
			<td>UNWATCH</td>
			<td>QUIT</td>
		</tr>
		<tr>
			<td>WATCH</td>
			<td>SELECT (Select0 only)</td>
		</tr>
	</tbody>
</table>

<p><br />
<br />
<a id="1.2.09.E5.8D.B3.E5.B0.86.E6.94.AF.E6.8C.81.E7.9A.84.E5.91.BD.E4.BB.A4" name="1.2.09.E5.8D.B3.E5.B0.86.E6.94.AF.E6.8C.81.E7.9A.84.E5.91.BD.E4.BB.A4"></a></p>

### 2. Commands to Be Supported

<table>
	<tbody>
		<tr>
			<th><strong>List</strong></th>
			<th><strong>Script</strong></th>
		</tr>
		<tr>
			<td>BLPOP</td>
			<td>EVAL</td>
		</tr>
		<tr>
			<td>BRPOP</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>BRPOPLPUSH</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

<p><br />
<br />
<a id="1.3.09.E4.B8.8D.E6.94.AF.E6.8C.81.E7.9A.84.E5.91.BD.E4.BB.A4" name="1.3.09.E4.B8.8D.E6.94.AF.E6.8C.81.E7.9A.84.E5.91.BD.E4.BB.A4"></a></p>

### 3. Unsupported Commands

<table>
	<tbody>
		<tr>
			<th><strong>Key</strong></th>
			<th><strong>Script</strong></th>
			<th><strong>Server</strong></th>
			<th><strong>Pub/Sub (Publish/Subscribe)</strong></th>
			<th><strong>HyperLogLog</strong></th>
		</tr>
		<tr>
			<td>KEYS</td>
			<td>EVALSHA</td>
			<td>BGREWRITEAOF</td>
			<td>PSUBSCRIBE</td>
			<td>PFADD</td>
		</tr>
		<tr>
			<td>MIGRATE</td>
			<td>SCRIPT EXISTS</td>
			<td>BGSAVE</td>
			<td>PUBLISH</td>
			<td>PFCOUNT</td>
		</tr>
		<tr>
			<td>MOVE</td>
			<td>SCRIPT FLUSH</td>
			<td>CLIENT GETNAME</td>
			<td>PUBSUB</td>
			<td>PFMERGE</td>
		</tr>
		<tr>
			<td>OBJECT</td>
			<td>SCRIPT KILL</td>
			<td>CLIENT KILL</td>
			<td>PUNSUBSCRIBE</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>RANDOMKEY</td>
			<td>SCRIPT LOAD</td>
			<td>CLIENT LIST</td>
			<td>SUBSCRIBE</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>RENAME</td>
			<td>&nbsp;</td>
			<td>CLIENT SETNAME</td>
			<td>UNSUBSCRIBE</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>RENAMENX</td>
			<td>&nbsp;</td>
			<td>CONFIG GET</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SORT</td>
			<td>&nbsp;</td>
			<td>CONFIG RESETSTAT</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SCAN</td>
			<td>&nbsp;</td>
			<td>CONFIG REWRITE</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>CONFIG SET</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>DBSIZE</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>DEBUG OBJECT</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>DEBUG SEGFAULT</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>FLUSHALL</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>FLUSHDB</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>INFO</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>LASTSAVE</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>MONITOR</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>PSYNC</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SAVE</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SHUTDOWN</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SLAVEOF</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SLOWLOG</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>SYNC</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>TIME</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

<p><br />
<br />
<a id="1.4.09.E5.85.B6.E4.BB.96.E9.99.90.E5.88.B6" name="1.4.09.E5.85.B6.E4.BB.96.E9.99.90.E5.88.B6"></a></p>

### 4. Other Limits

<p>Size limit of Key: 127 bytes; size limit of value data under a single key: 1,000,000 bytes.<br />
If there is no request for 30 minutes, CRS persistent connection will be automatically broken. Please try to make a reconnection in business.<br />
&nbsp;</p>

<p><a id="1.5___.E9.9B.86.E7.BE.A4.E7.89.88.E4.BA.8B.E5.8A.A1.E8.AF.B4.E6.98.8E" name="1.5___.E9.9B.86.E7.BE.A4.E7.89.88.E4.BA.8B.E5.8A.A1.E8.AF.B4.E6.98.8E"></a></p>

### 5. Notes About Cluster Instance Transactions

<p>1) If a transaction is partially completed, the failed part cannot be rolled back.</p>

<p>2) When a transaction is in progress, all the keys involved are locked, and the read/write access to the Key will fail.</p>

<p>3) All supported commands can be used in transactions.</p>

<p><a id="2..E5.8D.95.E6.9C.BA.E7.89.88.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6" name="2..E5.8D.95.E6.9C.BA.E7.89.88.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6"></a></p>


	
	











