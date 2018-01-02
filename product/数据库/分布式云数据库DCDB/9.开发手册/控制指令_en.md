## View Proxy Configuration and Status Information via SQL
With Tproxy, DCDB achieves automatic databases and tables splitting, manages the underlying physical database instances and provides a unique service port that is compatible with MySQL database.
The configuration information of proxy can be viewed via SQL control commands. For now, the following commands are supported:
### View available commands
```	
	mysql> /*proxy*/help;
	+-----------------------+-------------------------------------------------------+
	| command               | description                                           |
	+-----------------------+-------------------------------------------------------+
	| show config           | show config from conf                                 |
	| show status           | show proxy status,like route,shardkey and so on       |
	| set sys_log_level=N   | change the sys debug level N should be 0,1,2,3        |
	| set inter_log_level=N | change the interface debug level N should be 0,1      |
	| set inter_time_open=N | change the interface time debug level N should be 0,1 |
	| set sql_log_level=N   | change the sql debug level N should be 0,1            |
	| set slow_log_level=N  | change the slow debug level N should be 0,1           |
	| set slow_log_ms=N     | change the slow ms                                    |
	| set log_clean_time=N  | change the log clean days                             |
	| set log_clean_size=N  | change the log clean size in GB                       |
	+-----------------------+-------------------------------------------------------+
	10 rows in set (0.00 sec)
```
### View proxy configuration information
```
	mysql> /*proxy*/show config;
	+-----------------+--------------------+
	| config_name     | value              |
	+-----------------+--------------------+
	| version         | V2R120D001         |
	| mode            | group shard        |
	| rootdir         | /shard_922         |
	| sys_log_level   | 0                  |
	| inter_log_level | 0                  |
	| inter_time_open | 0                  |
	| sql_log_level   | 0                  |
	| slow_log_level  | 0                  |
	| slow_log_ms     | 1000               |
	| log_clean_time  | 1                  |
	| log_clean_size  | 1                  |
	| rw_split        | 1                  |
	| ip_pass_through | 0                  |
	+-----------------+--------------------+
	14 rows in set (0.00 sec)
```
### View proxy status information
```
	mysql> /*proxy*/show status;
	+-----------------------------+------------------------------------------------------------------------------+
	| status_name                 | value                                                                        |
	+-----------------------------+------------------------------------------------------------------------------+
	| cluster                     | group_1499858910_79548                                                       |
	| set_1499859173_1:ip         | 10.49.118.165:5025;10.175.98.109:5025@1@IDC_4@0,10.231.23.241:5025@1@IDC_2@0 |
	| set_1499859173_1:hash_range | 0---31                                                                       |
	| set_1499911640_3:ip         | 10.49.118.165:5026;10.175.98.109:5026@1@IDC_4@0,10.231.23.241:5026@1@IDC_2@0 |
	| set_1499911640_3:hash_range | 32---63                                                                      |
	| set                         | set_1499859173_1,set_1499911640_3                                            |
	| db_table:pavel.ff           | shardkey:a                                                                   |
```
	
## Enhance the Returned Result of "explain"
Proxy enhances the returned result of "explain", showing the modified SQL of proxy.
```	
	mysql> explain select * from test1;
	+------+-------------+-------+------+---------------+------+---------+------+------+-------+-----------------------------------------+
	| id   | select_type | table | type | possible_keys | key  | key_len | ref  | rows | Extra | info                                    |
	+------+-------------+-------+------+---------------+------+---------+------+------+-------+-----------------------------------------+
	|    1 | SIMPLE      | test1 | ALL  | NULL          | NULL | NULL    | NULL |   16 |       | set_2,explain select * from shard.test1 |
	|    1 | SIMPLE      | test1 | ALL  | NULL          | NULL | NULL    | NULL |   16 |       | set_1,explain select * from shard.test1 |
	+------+-------------+-------+------+---------------+------+---------+------+------+-------+-----------------------------------------+
	2 rows in set (0.03 sec)
```	

## "show create table" to Add Corresponding "shardkey" Information

```	
	mysql> show create table test.ff;
	+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Table | Create Table                                                                                                                                                                                                       |
	+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| ff    | CREATE TABLE `ff` (
	  `a` int(11) NOT NULL,
	  `c` int(11) DEFAULT NULL,
	  `d` datetime DEFAULT NULL,
	  `e` date DEFAULT NULL,
	  PRIMARY KEY (`a`)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=a |
	+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	1 row in set (0.02 sec)


	mysql> show create table test.global;
	+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Table  | Create Table                                                                                                                                                                     |
	+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| global | CREATE TABLE `global` (
	  `a` int(11) NOT NULL,
	  `b` int(11) DEFAULT NULL,
	  PRIMARY KEY (`a`)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=noshardkey_allset |
	+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	1 row in set (0.00 sec)
	
	mysql> show create table test.single;
	+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Table  | Create Table                                                                                                                                          |
	+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
	| single | CREATE TABLE `single` (
	  `a` int(11) NOT NULL,
	  `b` int(11) DEFAULT NULL,
	  PRIMARY KEY (`a`)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin |
	+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
	1 row in set (0.00 sec)
```



