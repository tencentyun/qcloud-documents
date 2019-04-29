When running some statements using the database, large amount of data may lead to deadlock without response. In this case, you must kill a query statement that is consuming resources. The syntax of the KILL command is as follows:
```
	KILL [CONNECTION | QUERY] thread_id
```
Every connection with "mysqld" is running in an independent thread. You can check which threads are running with the SHOW PROCESSLIST statement, and kill a thread with the KILL thread_id statement.
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
If your business has many threads and you cannot accurately determine which transactions are committed, you can use similar SQL to query a thread ID (for example):
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
If your business has many threads and you cannot accurately determine which transactions are in the status of lock wait, you can use similar SQL to query a thread ID (for example):
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

> Risk warning: After a large transaction is killed, it needs to be rolled back. If the data volume is large, you need to wait for a long time. At this time, you can click the master/slave switch in the console to switch from the slave to the master to resume the business quickly. **However, when using async and strongsync (degradable) replication programs, the delay of master/slave data sync may cause data loss or data corruption. Please be careful with the master/slave switch.**

