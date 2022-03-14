## MariaDB 和开源 MariaDB 的兼容性
完全兼容 MariaDB。

## MariaDB 与 MySQL 5.6 兼容性
MariaDB 与 MySQL 5.6 高度兼容，已用于 MySQL 数据库的代码、应用程序、驱动程序和工具，无需更改（或少量调整），即可与 MariaDB 配合使用。
- 数据文件和表定义文件二进制兼容。
- 所有的客户端 API 和协议都兼容。
- 所有的文件名、二进制文件、路径、端口号等都是相同。
- 所有的连接器，包括 PHP、Perl、Python、Java、.NET、Ruby、MySQL 的连接器在 MariaDB 上都可以正常使用，无需进行任何改动。
- 可使用 MySQL 客户端连接到 MariaDB。

## MariaDB 和 MySQL 5.6 的不兼容性
### 1. GTID 不兼容
MariaDB 的 GTID 和 MySQL 5.6 的 GTID 不兼容，即 MySQL 不能作为 MariaDB 的从库。

### 2. Binlog 默认配置不同
MariaDB 的 Binlog 默认采用 row 格式，而原生 MySQL 5.6 和原生 MariaDB 10.2.3 之前的版本，都默认采用 statement 格式。

### 3. CREAT TABLE ... SELECT 命令在基于行模式复制和基于命令模式复制
为使 CREAT TABLE ... SELECT 命令在基于行模式复制和基于命令模式复制的情况下都能正常工作，MariaDB 中的 CREAT TABLE ... SELECT 命令在从库上将会被转化为 CREAT OR RPLACE 命令执行，好处是即使从库中途宕机恢复后仍然能够正常工作。

#### 3.1 默认值推导
Create table ... Select from 语句建表时，varchar(N) 类型的字段的缺省值的区别：
- MariaDB 10.1 没有默认值。
- MySQL 5.7 的默认值是NULL。
- MySQL 5.5、5.6 的默认值是空串 ‘’。

decimal 列的默认值：MySQL 5.5、5.6 把推导为0.00，MariaDB 10.1 推导为 NULL。
示例：
```
---------------- MySQL 5.5 -----------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=latin1
-------------------- MySQL 5.7 ---------------------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1
------------------- MariaDB 10.1* --------------------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1


```

#### 3.2 处理子查询中 select 语句的区别
在这条语句中`SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;`

- MySQL 5.5、5.6 处理子查询 SELECT MAX(x), 12 时，如果该子查询位于 in 后面则相当于 SELECT MAX(x), 12 from t1，如果子查询位于 = 后面，则相当于 SELECT x, 12，其中 x 就是当前行中 a 的别名。
- MySQL 5.7 和 MariaDB 10.1.\* 中，子查询 SELECT MAX(x), 12 都等于 SELECT x, 12 ，其中 x 就是当前行中 a 的别名。
示例：
```
----------------- MySQL 5.5/5.6 -----------------------
CREATE TABLE t1 (a INT);
INSERT INTO t1 VALUES (1), (2), (11);
SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;
x   ROW(11, 12) = (SELECT MAX(x), 12)   ROW(11, 12) IN (SELECT MAX(x), 12)
1   0   1
2   0   1
11  1   1
--------------------------- MariaDB 10.1.* or MySQL 5.7------------------------------
CREATE TABLE t1 (a INT);
INSERT INTO t1 VALUES (1), (2), (11);
SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;
x   ROW(11, 12) = (SELECT MAX(x), 12)   ROW(11, 12) IN (SELECT MAX(x), 12)
1   0   0
2   0   0
11  1   1
```

#### 3.3 对 NULL 在 ALL 和 SOME 中的处理
MySQL 5.5 中对于 10 >=  ALL (NULL, 1, 10) 或者 1 <= ALL (NULL, 1, 10) 的判断中，因为 NULL 不可比，所以直接跳过与 NULL，即当作该 NULL 不存在。
MySQL 5.7 和 MariaDB 中，由于 NULL 属于未知值，在上述的对比中结果也应该是未知的，所以返回 NULL。

#### 3.4 alter table inplace 操作
如果 alter table 仅交换列的顺序，MariaDB 允许使用 inplace 算法，但 MySQL 不允许。
MariaDB 执行 inplace alter table 后，show create table t1 后发现运行结果与 MySQL 用 ALGORITHM=COPY 时运行结果相同。

### 4. MySQL 和 MariaDB 的未定义行为
未定义行为（undefined behavior）：指 MySQL、MariaDB 可以按照任意方式实现这种功能和行为，且版本之间可能发生变化而不需要通知用户或者明确指出。MySQL、MariaDB 对这些行为的实现可能产生相同的结果或者不同的结果。

对于现在和未来版本的这类不同或者相同之处，MariaDB 不会做任何结果保证，也不保证提供内核优化保证完全一致，[未定义行为官方说明](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-compatibility/)。

#### 4.1 字符类型列与大小写无关的排序
字符类型列，排序（order by 子句）一般按照大小写无关的方式排序，这意味着对于除大小写有区别之外，内容完全相同的字段，排序后的顺序是未定义的。您可以使用 BINARY 关键字来强制大小写相关的排序：ORDER BY BINARY 列名。
示例：
```
MySQL 和 MariaDB 对如下示例的排序可能是完全随机的
mysql> SELECT email FROM t2 LEFT JOIN t1  ON kid = t2.id WHERE t1.id IS NULL order by email;

+-------+
| email |
+-------+
| email |
| eMail |
| EMail |
+-------+
3 rows in set (0.00 sec)
```

#### 4.2 Auto_increment 字段溢出后的处理方式不同
INNODB 特定的未定义行为：
- 在所有自增列锁定模式下（0，1，2），如果给自增列字段指定负数，自增机制的行为是未定义的。
- 在所有自增列锁定模式下（0，1，2），如果自增列字段值大于该自增列整数类型可以存储的最大整数值，那么自增机制的行为是未定义的。

>?请不要向自增列随意插入（错误）数字。

#### 4.3 FOUND ROWS 统计方式不同
FOUND_ROWS() 返回值只有在查询语句中使用了 UNION ALL 时才精确。
如果**只使用 UNION 不使用 ALL，那么 MariaDB 会去重统计， MySQL 不会去重统计**。如果使用了 UNION 的查询语句不使用 LIMIT 子句那么 SQL_CALC_FOUND_ROWS 关键字会被忽略，FOUND_ROWS() 返回的就是执行 UNION 时创建的临时表中的行数。

#### 4.4 LOCK TABLES 语句上锁顺序不同
LOCK TABLES 语句按照如下方法上锁：第一步是把所有要锁住的表按内部定义的方式排序；但从用户角度来看，MySQL、MariaDB 这个顺序是未定义的。例如，写一个 LOCK TABLES t1, t2, t3，MySQL、Mariadb 不会按照 t1, t2, t3 的顺序上锁。
因为对 MySQL、MariaDB 来说，这个是未定义行为，MySQL 和 MariaDB 可能采用不同的方式去排序 t1, t2, t3，然后再按照那个排好的顺序依次给他们上锁。

因此，用户写的存储过程或者查询代码不应该依赖任何上锁顺序来保持正确性，否则可能会发生死锁。

#### 4.5 执行 RESET MASTER 语句的时机
RESET MASTER 不可以在有任何复制备机运行期间被执行，此时执行 RESET MASTER 时候主机和备机的行为对 MariaDB 和 MySQL 是未定义的（也是不支持的）；执行 RESET MASTER 期间可能发生各种错误（不具有可预见性，甚至不会发生错误），且这些错误 MariaDB 和 MySQL 的官方开发团队不会认为是 bug，也不会对发生的错误负责。 

#### 4.6  日期和时间类型转换为 year 类型
MySQL 5.5 中 year 与 date 类型的变量在比较时，会将 date 类型转为 year 类型进行对比，即“2011-01-01”被转为2011。

MySQL 5.7 和 MariaDB 中 date 类型的变量仍然为 date，所以在和 year 对比时不相等。
类似地，MariaDB 不能够把时间类型转换为 year 类型，而 MySQL 5.6 会使用当前 session 的 timestamp 值的 year 部分作为每一个 TIME 类型值的 year，因此当需要把一个 time 类型的值转换为 year 类型时，就使用这个 session 的 timestamp 的 year。

#### 4.7 未知字符的处理方式
- 不同版本的 MySQL 和 MariaDB 在做字符编码转换时是有区别的：例如，unhex 如果不识别一个编码字节串，那么在 MySQL 5.5、5.6、5.7 中它返回空串’’，但是 MariaDB 10.1 会返回问号字符(?)。
- 语句`UPDATE t1 SET a=unhex(code) ORDER BY code`对表 t1 中的 a 字段进行赋值，但由于 unhex 只能识别和转换特定范围内的字节串，因此部分赋值是失败的。
 - MySQL 5.5 默认的存储引擎是 MyISAM，不支持事务。当对 t1 某行中的 a 赋值失败后就会退出该语句，而已经赋值的仍然存储在 t1 中。
 - MySQL 5.7 默认的存储引擎是 InnoDB，因此当对 t1 某行中的 a 赋值失败后这个事务就会进行回滚，因此已经赋值都会被回滚。
 - MariaDB 默认的存储引擎为 InnoDB，且当 unhex 无法找到一个字节串对应的字符时，就会返回问号字符，0x3F，即字符'?'，因此不管存储引擎是 InnoDB 和 MyISAM，都会是操作成功。
- 当使用 insert into 语句插入16进制的字节串时，如果无法找到对应的 utf8mb4 编码的字符时，
 - MySQL 5.5、5.6 使用 heap 存储引擎时，忽略此未知字符。
 - MariaDB 10.1 和 MySQL 5.7 用 0x3F（即问号字符）代替。
- 对于非法编码的字符串字段，MySQL 使用 InnoDB 存储引擎时直接返回错误，而 MariaDB 则将其替换为 3F 再将其插入。

#### 4.8 时间类型精度
``` 
SELECT CAST(CAST('10:11:12.098700' AS TIME) AS DECIMAL(20,6));
CAST(CAST('10:11:12.098700' AS TIME) AS DECIMAL(20,6))
``` 	
出现类似语句时，MySQL 5.5、5.6 与 MariaDB 10.1、MySQL 5.7 之间采用不同的处理方式：
- 在 MySQL 5.5、5.6 中返回101112.098700，仍然能够保持精度。
- 在 MySQL 5.7 和 MariaDB 10.1 中返回101112.000000，这是因为该语句没有指定 TIME 的精度，而 TIME 的默认精度为0，因此“CAST('10:11:12.098700' AS TIME)”会丢失小数点后面的数值。

为了保证时间的精度不变，可以使用如下语句。
```
SELECT CAST(CAST('10:11:12.098700' AS TIME(6)) AS DECIMAL(20,6));
+-----------------------------------------------------------+
| CAST(CAST('10:11:12.098700' AS TIME(6)) AS DECIMAL(20,6)) |
+-----------------------------------------------------------+
| 101112.098700 |
+-----------------------------------------------------------+
```
>?对于 TIME 默认的精度不统一，如果对时间精度有要求，为了升级或者迁移都应该明确制定 time 的具体精度。

```
CREATE TABLE t1(f1 TIME);
INSERT INTO t1 VALUES ('23:38:57');
SELECT TIMESTAMP(f1,'1') FROM t1;
```
MySQL 5.5、5.6 返回 NULL，MariaDB 10.1 和 MySQL 5.7 返回 2016-08-03 23:38:58。
- TIMESTAMP() 的第一个参数为 time 类型时，MySQL 5.5 无法自动转换为 timestamp 类型，因而返回 NULL。
- MySQL 5.7 和 MariaDB 则将 time 类型自动转为 timestamp 类型，即将当前的日期+输入的 time 变量。

### 5. 附录：MariaDB 参数和 MySQL 参数
#### 5.1 相同变量名不同参数
变量名相同意味着主要功能也相同。

<table>
<tr><th width="20%">参数名</th><th width="30%">MariaDB 10.1</th><th width="30%">MySQL 5.6</th></tr>
<tr>
<td>old_passwords</td>
<td>OFF</td>
<td>0</td></tr>
<tr>
<td>tmpdir</td>
<td>/tmp/5cXm2hHsWi/mysqld.1</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1</td></tr>
<tr>
<td>version</td>
<td>10.1.9-MariaDB-log</td>
<td>5.6.31-log</td></tr>
<tr>
<td>slow_query_log_file</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/mysqld-slow.log</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/mysqld-slow.log</td></tr>
<tr>
<td>table_definition_cache</td>
<td>400</td>
<td>1400</td></tr>
<tr>
<td>datadir</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/data/</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/data/</td></tr>
<tr>
<td>pid_file</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/run/mysqld.1.pid</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/run/mysqld.1.pid</td></tr>
<tr>
<td>max_seeks_for_key</td>
<td>4294967295</td>
<td>18446744073709500000</td></tr>
<tr>
<td>slave_load_tmpdir</td>
<td>/tmp/5cXm2hHsWi/mysqld.1</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1</td></tr>
<tr>
<td>secure_file_priv</td>
<td>	/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/</td></tr>
<tr>
<td>sql_mode</td>
<td>NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION	</td>
<td>NO_ENGINE_SUBSTITUTION</td></tr>
<tr>
<td>ssl_cert</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/server-cert.pem</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/server-cert.pem</td></tr>
<tr>
<td>ssl_ca</td>
<td>	/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/cacert.pem</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/cacert.pem</td></tr>
<tr>
<td>open_files_limit</td>
<td>1024</td>
<td>4161</td></tr>
<tr>
<td>binlog_checksum</td>
<td>NONE</td>
<td>CRC32</td></tr>
<tr>
<td>basedir</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6</td></tr>
<tr>
<td>query_alloc_block_size</td>
<td>16384</td>
<td>8192</td></tr>
<tr>
<td>innodb_max_dirty_pages_pct</td>
<td>75.000000</td>
<td>75</td></tr>
<tr>
<td>ssl_key</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/server-key.pem</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/server-key.pem</td></tr>
<tr>
<td>myisam_sort_buffer_size</td>
<td>134216704</td>
<td>8388608</td></tr>
<tr>
<td>skip_name_resolve</td>
<td>ON</td>
<td>OFF</td></tr>
<tr>
<td>pseudo_thread_id</td>
<td>3</td>
<td>2</td></tr>
<tr>
<td>character_sets_dir</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/sql/share/charsets/</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/sql/share/charsets/</td></tr>
<tr>
<td>innodb_adaptive_flushing_lwm</td>
<td>10</td>
<td>10</td></tr>
<tr>
<td>myisam_recover_options</td>
<td>DEFAULT</td>
<td>OFF</td></tr>
<tr>
<td>performance_schema_max_statement_classes</td>
<td>179</td>
<td>168</td></tr>
<tr>
<td>innodb_version</td>
<td>5.6.26-74.0</td>
<td>5.6.31</td></tr>
<tr>
<td>max_write_lock_count</td>
<td>4294967295</td>
<td>18446744073709500000</td></tr>
<tr>
<td>thread_cache_size</td>
<td>0</td>
<td>9</td></tr>
<tr>
<td>innodb_checksum_algorithm</td>
<td>INNODB</td>
<td>innodb</td></tr>
<tr>
<td>optimizer_switch</td>
<td>
index_merge=on,<br>index_merge_union=on,<br>index_merge_sort_union=on,<br>index_merge_intersection=on,<br>index_merge_sort_intersection=off,<br>engine_condition_pushdown=off,<br>index_condition_pushdown=on,<br>derived_merge=on,<br>derived_with_keys=on,<br>firstmatch=on,<br>loosescan=on,<br>materialization=on,<br>in_to_exists=on,<br>semijoin=on,<br>partial_match_rowid_merge=on,<br>partial_match_table_scan=on,<br>subquery_cache=on,<br>mrr=off,<br>mrr_cost_based=off,<br>mrr_sort_keys=off,<br>outer_join_with_cache=on,<br>semijoin_with_cache=on,<br>join_cache_incremental=on,<br>join_cache_hashed=on,<br>join_cache_bka=on,<br>optimize_join_buffer_size=off,<br>table_elimination=on,<br>extended_keys=on,<br>exists_to_in=on</td>
<td>
index_merge=on,<br>index_merge_union=on,<br>index_merge_sort_union=on,<br>index_merge_intersection=on,<br>engine_condition_pushdown=on,<br>index_condition_pushdown=on,<br>mrr=on,<br>mrr_cost_based=on,<br>block_nested_loop=on,<br>batched_key_access=off,<br>materialization=on,<br>semijoin=on,<br>loosescan=on,<br>firstmatch=on,<br>subquery_materialization_cost_based=on,<br>use_index_extensions=on
</td></tr>
<tr>
<td>timestamp</td>
<td>1471938276</td>
<td>1471937901</td></tr>
<tr>
<td>general_log_file</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/mysqld.log</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/mysqld.log</td></tr>
<tr>
<td>myisam_stats_method</td>
<td>NULLS_UNEQUAL</td>
<td>nulls_unequal</td></tr>
<tr>
<td>innodb_log_compressed_pages</td>
<td>OFF</td>
<td>ON</td></tr>
<tr>
<td>query_prealloc_size</td>
<td>24576</td>
<td>0</td></tr>
<tr>
<td>rand_seed2</td>
<td>297895171</td>
<td>0</td></tr>
<tr>
<td>rand_seed1</td>
<td>605568929</td>
<td>0</td></tr>
<tr>
<td>socket</td>
<td>/tmp/5cXm2hHsWi/mysqld.1.sock</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1.sock</td></tr>
<tr>
<td>innodb_max_dirty_pages_pct_lwm</td>
<td>0.001</td>
<td>0</td></tr>
<tr>
<td>lc_messages_dir</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/sql/share/</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/sql/share/</td></tr>
<tr>
<td>max_relay_log_size</td>
<td>1073741824</td>
<td>0</td></tr>
<tr>
<td>plugin_dir</td>
<td>/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/lib/plugin/</td>
<td>/data/home/tdengine/dongzhi/src/mysql-server-5.6/lib/plugin/</td></tr>
<tr>
<td>thread_stack</td>
<td>294912</td>
<td>262144</td></tr>
</table>

#### 5.2 仅存在于 MariaDB 中的变量
- aria_block_size     8192
- aria_checkpoint_interval     30
- aria_checkpoint_log_activity     1048576
- aria_encrypt_tables     OFF
- aria_force_start_after_recovery_failures     0
- aria_group_commit     none
- aria_group_commit_interval     0
- aria_log_file_size     1073741824
- aria_log_purge_type     immediate
- aria_max_sort_file_size     9223372036853727232
- aria_page_checksum     ON
- aria_pagecache_age_threshold     300
- aria_pagecache_buffer_size     134217728
- aria_pagecache_division_limit     100
- aria_pagecache_file_hash_size     512
- aria_recover     NORMAL
- aria_repair_threads     1
- aria_sort_buffer_size     268434432
- aria_stats_method     nulls_unequal
- aria_sync_log_dir     NEWFILE
- aria_used_for_temp_tables     ON
- autoremoverelaylog     ON
- binlog_annotate_row_events     OFF
- binlog_commit_wait_count     0
- binlog_commit_wait_usec     100000
- binlog_optimize_thread_scheduling     ON
- deadlock_search_depth_long     15
- deadlock_search_depth_short     4
- deadlock_timeout_long     50000000
- deadlock_timeout_short     10000
- debug_no_thread_alarm     OFF
- default_master_connection      
- default_regex_flags      
- encrypt_binlog     OFF
- encrypt_tmp_disk_tables     OFF
- encrypt_tmp_files     OFF
- enforce_storage_engine      
- expensive_subquery_limit     100
- extra_max_connections     20
- extra_port     0
- flush_relay_logs_for_strong_consistency     ON
- gtid_binlog_pos      
- gtid_binlog_state      
- gtid_current_pos      
- gtid_domain_id     0
- gtid_ignore_duplicates     OFF
- gtid_seq_no     0
- gtid_slave_pos      
- gtid_strict_mode     OFF
- histogram_size     0
- histogram_type     SINGLE_PREC_HB
- in_transaction     0
- innodb_adaptive_hash_index_partitions     1
- innodb_background_scrub_data_check_interval     3600
- innodb_background_scrub_data_compressed     OFF
- innodb_background_scrub_data_interval     604800
- innodb_background_scrub_data_uncompressed     OFF
- innodb_buf_dump_status_frequency     0
- innodb_buffer_pool_populate     OFF
- innodb_cleaner_lsn_age_factor     HIGH_CHECKPOINT
- innodb_compression_algorithm     none
- innodb_corrupt_table_action     assert
- innodb_default_encryption_key_id     1
- innodb_defragment     OFF
- innodb_defragment_fill_factor     0.900000
- innodb_defragment_fill_factor_n_recs     20
- innodb_defragment_frequency     40
- innodb_defragment_n_pages     7
- innodb_defragment_stats_accuracy     0
- innodb_disallow_writes     OFF
- innodb_empty_free_list_algorithm     BACKOFF
- innodb_encrypt_log     OFF
- innodb_encrypt_tables     OFF
- innodb_encryption_rotate_key_age     1
- innodb_encryption_rotation_iops     100
- innodb_encryption_threads     0
- innodb_fake_changes     OFF
- innodb_fatal_semaphore_wait_threshold     600
- innodb_force_primary_key     OFF
- innodb_foreground_preflush     EXPONENTIAL_BACKOFF
- innodb_idle_flush_pct     100
- innodb_immediate_scrub_data_uncompressed     OFF
- innodb_instrument_semaphores     OFF
- innodb_kill_idle_transaction     0
- innodb_locking_fake_changes     ON
- innodb_log_arch_dir     ./
- innodb_log_arch_expire_sec     0
- innodb_log_archive     OFF
- innodb_log_block_size     512
- innodb_log_checksum_algorithm     INNODB
- innodb_max_bitmap_file_size     104857600
- innodb_max_changed_pages     1000000
- innodb_mtflush_threads     8
- innodb_prefix_index_cluster_optimization     OFF
- innodb_sched_priority_cleaner     19
- innodb_scrub_log     OFF
- innodb_scrub_log_speed     256
- innodb_show_locks_held     10
- innodb_show_verbose_locks     0
- innodb_simulate_comp_failures     0
- innodb_stats_modified_counter     0
- innodb_stats_traditional     ON
- innodb_track_changed_pages     OFF
- innodb_use_atomic_writes     OFF
- innodb_use_fallocate     OFF
- innodb_use_global_flush_log_at_trx_commit     ON
- innodb_use_mtflush     OFF
- innodb_use_stacktrace     OFF
- innodb_use_trim     OFF
- join_buffer_space_limit     2097152
- join_cache_level     2
- key_cache_file_hash_size     512
- key_cache_segments     0
- last_gtid      
- log_slow_filter     admin,filesort,filesort_on_disk,full_join,full_scan,query_cache,query_cache_miss,tmp_table,tmp_table_on_disk
- log_slow_rate_limit     1
- log_slow_verbosity      
- log_tc_size     24576
- loglevel     3
- max_long_data_size     4194304
- max_statement_time     0.000000
- mrr_buffer_size     262144
- myisam_block_size     1024
- mysql56_temporal_format     ON
- old_mode      
- optimizer_selectivity_sampling_limit     100
- optimizer_use_condition_selectivity     1
- plugin_maturity     unknown
- progress_report_time     5
- query_cache_strip_comments     OFF
- relay_log_sync_threshold     134217728
- relay_log_sync_timeout     200
- relay_log_sync_txn_count     5
- replicate_annotate_row_events     OFF
- replicate_do_db      
- replicate_do_table      
- replicate_events_marked_for_skip     REPLICATE
- replicate_ignore_db      
- replicate_ignore_table      
- replicate_wild_do_table      
- replicate_wild_ignore_table      
- rowid_merge_buff_size     8388608
- rpl_semi_sync_master_enabled     OFF
- rpl_semi_sync_master_timeout     10000
- rpl_semi_sync_master_trace_level     32
- rpl_semi_sync_master_wait_no_slave     ON
- rpl_semi_sync_master_wait_point     AFTER_COMMIT
- rpl_semi_sync_slave_enabled     OFF
- rpl_semi_sync_slave_trace_level     32
- skip_parallel_replication     OFF
- skip_replication     OFF
- slave_current_parallel_transactions     0
- slave_ddl_exec_mode     IDEMPOTENT
- slave_domain_parallel_threads     0
- slave_max_parallel_transactions     0
- slave_parallel_max_queued     131072
- slave_parallel_mode     conservative
- slave_parallel_threads     0
- slave_run_triggers_for_rbr     NO
- sqlasyn     OFF
- sqlasyntimeout     10
- sqlasynwarntimeout     3
- strict_password_validation     ON
- thread_pool_high_prio_mode     transactions
- thread_pool_high_prio_tickets     4294967295
- thread_pool_idle_timeout     60
- thread_pool_max_threads     1000
- thread_pool_oversubscribe     3
- thread_pool_oversubscribe_parall     1
- thread_pool_size     8
- thread_pool_stall_limit     500
- use_stat_tables     NEVER
- userstat     OFF
- version_malloc_library     system
- version_ssl_library     OpenSSL 1.0.2d 9 Jul 2015
- wsrep_auto_increment_control     ON
- wsrep_causal_reads     OFF
- wsrep_certify_nonpk     ON
- wsrep_cluster_address      
- wsrep_cluster_name     my_wsrep_cluster
- wsrep_convert_lock_to_trx     OFF
- wsrep_data_home_dir     /data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/data/
- wsrep_dbug_option      
- wsrep_debug     OFF
- wsrep_desync     OFF
- wsrep_dirty_reads     OFF
- wsrep_drupal_282555_workaround     OFF
- wsrep_forced_binlog_format     NONE
- wsrep_gtid_domain_id     0
- wsrep_gtid_mode     OFF
- wsrep_load_data_splitting     ON
- wsrep_log_conflicts     OFF
- wsrep_max_ws_rows     131072
- wsrep_max_ws_size     1073741824
- wsrep_mysql_replication_bundle     0
- wsrep_node_address      
- wsrep_node_incoming_address     AUTO
- wsrep_node_name      
- wsrep_notify_cmd      
- wsrep_on     OFF
- wsrep_osu_method     TOI
- wsrep_patch_version     wsrep_25.11
- wsrep_provider     none
- wsrep_provider_options      
- wsrep_recover     OFF
- wsrep_replicate_myisam     OFF
- wsrep_restart_slave     OFF
- wsrep_retry_autocommit     1
- wsrep_slave_fk_checks     ON
- wsrep_slave_threads     1
- wsrep_slave_uk_checks     OFF
- wsrep_sst_auth      
- wsrep_sst_donor      
- wsrep_sst_donor_rejects_queries     OFF
- wsrep_sst_method     rsync
- wsrep_sst_receive_address     AUTO
- wsrep_start_position     00000000-0000-0000-0000-000000000000:-1
- wsrep_sync_wait     0

#### 5.3 仅存在于 MySQL 5.6 中的变量

- avoid_temporal_upgrade     OFF
- bind_address     *
- binlog_error_action     IGNORE_ERROR
- binlog_gtid_simple_recovery     OFF
- binlog_max_flush_queue_time     0
- binlog_order_commits     ON
- binlog_rows_query_log_events     OFF
- binlogging_impossible_mode     IGNORE_ERROR
- block_encryption_mode     aes-128-ecb
- core_file     ON
- disconnect_on_expired_password     ON
- end_markers_in_json     OFF
- enforce_gtid_consistency     OFF
- eq_range_index_dive_limit     1
- gtid_executed      
- gtid_mode     OFF
- gtid_next     AUTOMATIC
- gtid_owned      
- gtid_purged      
- innodb_tmpdir      
- log_bin_use_v1_row_events     OFF
- log_slow_admin_statements     OFF
- log_slow_slave_statements     OFF
- log_throttle_queries_not_using_indexes     0
- master_info_repository     FILE
- new     OFF
- optimizer_trace     enabled=off,one_line=off
- optimizer_trace_features     greedy_search=on,range_optimizer=on,dynamic_range=on,repeated_subselect=on
- optimizer_trace_limit     1
- optimizer_trace_max_mem_size     16384
- optimizer_trace_offset     -1
- relay_log_info_repository     FILE
- rpl_stop_slave_timeout     31536000
- server_id_bits     32
- server_uuid     9078a55d-6904-11e6-bfa9-ecf4bbcdc829
- sha256_password_private_key_path     private_key.pem
- sha256_password_public_key_path     public_key.pem
- show_old_temporals     OFF
- simplified_binlog_gtid_recovery     OFF
- slave_allow_batching     OFF
- slave_checkpoint_group     512
- slave_checkpoint_period     300
- slave_parallel_workers     0
- slave_pending_jobs_size_max     16777216
- slave_rows_search_algorithms     TABLE_SCAN,INDEX_SCAN
- table_open_cache_instances     1
- transaction_allow_batching     OFF

