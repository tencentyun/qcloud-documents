在使用数据库运行某些语句时，会因数据量太大而导致死锁，没有反应。这个时候，就需要 KILL 掉某个正在消耗资源的 query 语句即可，KILL 命令的语法格式如下：
```
	KILL [CONNECTION | QUERY] thread_id
```
每个与 mysqld 的连接都在一个独立的线程里运行，您可以使用 SHOW PROCESSLIST 语句查看哪些线程正在运行，并使用 KILL thread_id 语句终止一个线程。
```
	mysql> show processlist;
	+--------+------------+----------------+------+---------+------+------------+---------------------+-----------+---------------+
	| Id     | User       | Host           | db   | Command | Time | State      | Info                | Rows_sent | Rows_examined |
	+--------+------------+----------------+------+---------+------+------------+---------------------+-----------+---------------+
	| 924107 | sutest | 10.0.0.8:38314 | NULL | Query   |    0 | starting   | show processlist    |         0 |             0 |
	| 924114 | sutest | 10.0.0.8:38318 | test | Query   |  264 | User sleep | select sleep(20000) |         0 |             0 |
	+--------+------------+----------------+------+---------+------+------------+---------------------+-----------+---------------+
	2 rows in set (0.00 sec)
	
	mysql> kill 924114;
	Query OK, 0 rows affected (0.00 sec)
```
如果您的业务有较多线程，无法准确判断哪些事务未提交，可以采用类似 SQL 进行查询线程 ID（举例）：
```
	SELECT 
	  it.trx_id AS trx_id,
	  it.trx_state AS trx_state,
	  it.trx_started AS trx_started,
	  it.trx_mysql_thread_id AS trx_mysql_thread_id,
	  CURRENT_TIMESTAMP - it.trx_started AS RUN_TIME,
	  pl.user AS USER,
	  pl.host AS HOST,
	  pl.db AS db,
	  pl.time AS trx_run_time,
	  pl.INFO as INFO
	FROM
	  information_schema.INNODB_TRX it,
	  information_schema.processlist pl
	WHERE
	  pl.id=it.trx_mysql_thread_id
	ORDER BY RUN_TIME DESC LIMIT 10;
```
如果您的业务有较多线程，无法准确判断哪些事务处于锁等待，可以采用类似 SQL 进行查询线程 ID（举例）：
```
	SELECT 
	r.trx_id waiting_trx_id, 
	r.trx_mysql_thread_id waiting_thread, 
	TIMESTAMPDIFF( SECOND, r.trx_wait_started, CURRENT_TIMESTAMP ) wait_time, 
	r.trx_query waiting_query, 
	l.lock_table waiting_table_lock, 
	b.trx_id blocking_trx_id, 
	b.trx_mysql_thread_id blocking_thread,
	SUBSTRING( p. HOST, 1, INSTR(p. HOST, ':') - 1 ) blocking_host, 
	SUBSTRING(p. HOST, INSTR(p. HOST, ':') + 1) blocking_port,
	IF (p.COMMAND = 'Sleep', p.TIME, 0) idel_in_trx, 
	b.trx_query blocking_query FROM information_schema.INNODB_LOCK_WAITS w INNER JOIN information_schema.INNODB_TRX b ON b.trx_id = w.blocking_trx_id INNER JOIN information_schema.INNODB_TRX r ON r.trx_id = w.requesting_trx_id INNER JOIN information_schema.INNODB_LOCKS l ON w.requested_lock_id = l.lock_id LEFT JOIN information_schema. PROCESSLIST p ON p.ID = b.trx_mysql_thread_id ORDER BY wait_time DESC;
```

风险提示：大事务 KILL 之后，事务需要回滚，数据量较大的情况下也需等待很久，此时可以到控制台单击主从切换，将从机切换为主，以快速恢复业务。**但请务必知悉：使用异步同步、强同步（可退化）复制方案时，由于主从数据同步有延迟，可能丢失/错乱部分数据，请谨慎操作主从切换。**
