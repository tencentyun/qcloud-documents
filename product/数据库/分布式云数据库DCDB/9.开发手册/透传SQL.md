TDSQL MySQL版 实例会对 SQL 进行语法解析，有一定的限制，如果用户想在某个节点（set）中执行 MySQL 支持，但分布式实例不支持的 SQL 时，可以使用透传 SQL 的功能。
>?
>- 透传 SQL 时，proxy 不会解析 SQL，如果是往两个 set 进行透传写操作，不会使用分布式事务，特殊情况下会发生不一致问题，因此对于写操作建议一次透传一个 set。
>- 为保证透传语法生效，连接 MySQL 时请使用 -c 参数。


```
MySQL [test]> repair table test.t1;
ERROR 664 (HY000): Proxy ERROR:SQL is too complex, only applicable to noshard table: Shard table do not support repair
MySQL [test]> /*sets:allsets*/repair table test.t1;
+---------+--------+----------+----------+------------------+
| Table   | Op     | Msg_type | Msg_text | info             |
+---------+--------+----------+----------+------------------+
| test.t1 | repair | status   | OK       | set_1544429866_3 |
| test.t1 | repair | status   | OK       | set_1544429718_1 |
+---------+--------+----------+----------+------------------+
2 rows in set (0.01 sec)
```

具体语法：
- sets:set_1,set_2：代表指定某几个 set，set 名字可以通过`/*proxy*/show status`查询。
- sets:allsets：代表指定全部 set。
- shardkey:10：代表支持透传 SQL 到 shardkey 对应值上的 set。
- shardkey_hash:10：透传到负责 hash 值为10的 set，如果为0，则发送到第一个 set 上。

