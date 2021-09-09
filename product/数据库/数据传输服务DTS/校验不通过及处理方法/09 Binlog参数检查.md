
## MySQL/TDSQL MySQL/TDSQL-C 检查详情
源数据库 binlog 相关参数需要按照如下要求配置，如果校验不通过，请参考本文后续指导进行修复。
- `log_bin` 变量必须设置为 `ON`。
- `binlog_format` 变量必须设置为 `ROW`。
- `binlog_row_image` 必须设置为 `FULL`。
- 如果源数据库为 MySQL 5.6 及以上版本，`gtid_mode` 只支持设置为 `ON` 和 `OFF`，建议将 `gtid_mode` 设置为 `ON`，设置为 `OFF` 会报警告，设置为 `ON_PERMISSIVE` 和 `OFF_PERMISSIVE` 会报错。
- `server_id` 参数需要手动设置，且值不能设置为0。
- 不允许设置 `do_db`，`ignore_db`。
- 对于源实例为从库的情况，`log_slave_updates` 变量必须设置为 `ON`。

## 修复方法
### 开启 binlog 
`log_bin` 是 binlog 的开关控制参数，需要将 binlog 打开，以便记录所有的数据库表结构和表数据变更日志。 

如发生类似报错，请参考如下指导进行修复。
1. 登录源数据库。
2. 参考如下内容修改源数据库的配置文件 `my.cnf`。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
log_bin = MYSQL_BIN
binlog_format = ROW
server_id = 2         //建议设为大于1的整数，此处仅为示例。
binlog_row_image = FULL
```
3. 参考如下命令重启源数据库。
```
[\$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[\$Mysql_Dir]/bin/safe_mysqld &
```
>?[\$Mysql_Dir] 指源数据库的安装路径，请替换为实际的源数据库安装目录。
4. 确认 binlog 功能是否已启用。
```
show variables like '%log_bin%';
```
系统显示结果类似如下：
```
mysql> show variables like '%log_bin%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+
1 row in set (0.00 sec)
```
5. 重新执行校验任务。

### 修改 binlog_format 参数
`binlog_format` 为 binlog 的记录模式，有以下三种：
- `STATEMENT`：每一条会修改数据的 SQL 都会记录到 master 的 binlog 中，slave 在复制的时候，会执行和原来 master 端相同的 SQL。该模式可以减少 binlog 日志量，但是对某些特定的函数进行复制时，slave 端不能正确复制。
- `ROW`：binlog 日志中会记录成每一行数据修改的形式，然后在 slave 端再对相同的数据进行修改。该模式会保证 master 和 slave 的正确复制，但是 binlog 日志量会增加。
- `MIXED`：前两种模式的结合，MySQL 会根据执行的每一条具体的 SQL 语句来区分对待记录的日志形式，在 `STATEMENT` 和 `ROW` 之间选择一种。 

综上，为了保证 master 和 slave 的正确复制，`binlog_format` 参数需要设置为 `ROW`。如发生类似报错，请参考如下指导进行修复。
>?该参数修改可以不重启数据库，但是需要中断当前数据库上的所有业务连接，当源库为从库时，还需重启主从同步 SQL 线程，避免当前业务连接继续使用修改前的模式写入。

1. 登录源数据库。
2. 参考如下内容修改配置文件 `my.cnf`。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
binlog_format = ROW
```
3. 查看参数修改是否生效。
```
show variables like "%binlog_format%";
```
系统显示结果类似如下：
```
mysql> show variables like '%binlog_format%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+
1 row in set (0.00 sec)
```
5. 重新执行校验任务。

### 修改 binlog_row_image 参数
`binlog_row_image` 参数决定了 binlog 是如何记录前镜像（记录修改前的内容）和后镜像（记录修改后的内容）的，这会直接影响到数据闪回、主从复制等功能。
`binlog_row_image` 参数只在 `binlog_format` 配置为 `ROW` 模式下生效。具体取值影响如下：
- `FULL`：在 `ROW` 模式下，binlog 会记录前镜像和后镜像的所有列的数据信息。
- `MINIMAL`：在 `ROW` 模式下，当表没有主键或唯一键时，前镜像记录所有列，后镜像记录被修改的列；如果存在主键或唯一键，不管是前镜像还是后镜像，都只记录有影响的列。

综上，`binlog_row_image` 需要配置为 `FULL`，源数据库的 binlog 记录全镜像。如发生报错，请参考如下步骤修复。
>?该参数修改可以不重启数据库，但是需要中断当前数据库上的所有业务连接，当源库为从库时，还需重启主从同步SQL线程，避免当前业务连接继续使用修改前的模式写入。

1. 登录源数据库。
2. 参考如下内容修改源数据库的配置文件 `my.cnf`。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
binlog_row_image = FULL
```
3. 确认参数修改是否生效。
```
show variables like "%binlog_row_image%";
```
系统显示结果类似如下：
```
mysql> show variables like '%binlog_row_image%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| binlog_row_image | FULL  |
+------------------+-------+
1 row in set (0.00 sec)
```
4. 重新执行校验任务。

### 修改 gtid_mode 参数
GTID（Global Transaction Identifier， 全局事物标识），用于在 binlog 中唯一标识一个事务，使用 GTID 可以避免事务重复执行导致数据混乱或者主从不一致。
GTID 是 MySQL 5.6 的新特性，所以 MySQL 5.6 及之后版本存在此问题。DTS 只支持 `gtid_mode` 设置为 `ON` 和 `OFF`，建议将 `gtid_mode` 设置为 `ON`，否则校验时会报警告。

警告不影响迁移或同步任务进行，但是会对业务造成一定的影响：设置 GTID后，在增量数据同步阶段，如果源实例发生 HA 切换，DTS 服务切换重连，任务几乎无感知；反之，任务会中断后失败，且不可恢复。

`gtid_mode` 的取值如下，在修改 `gtid_mode` 的值时，只能从以下四个值逐级修改，例如，需要从 `OFF` 修改为 `ON`，则 `gtid_mode` 修改顺序为 `OFF` <-> `OFF_PERMISSIVE` <-> `ON_PERMISSIVE` <-> `ON`。
- `OFF`：主库所有新启的事务以及从库的事务都要求是匿名事务。
- `OFF_PERMISSIVE`：主库新启的事务是匿名事务，但从库事务允许是匿名的或者是 GTID 事务，但不允许只是 GTID 模式。
- `ON_PERMISSIVE`：主库新启的事务是 GTID 事务，从库事务允许是匿名的或者是 GTID 事务。
- `ON`：主库新启的事务是 GTID 事务，从库的事务也要求是 GTID 事务。

如果发生类似警告，请按照如下指导进行修复。
1. 登录源数据库。
2. 在主从复制结构两边都设置 `gtid_mode = OFF_PERMISSIVE`。
```
set global gtid_mode = OFF_PERMISSIVE;
```
3. 在主从复制结构两边都设置 `gtid_mode = ON_PERMISSIVE`。
```
set global gtid_mode = ON_PERMISSIVE;
```
4. 在各个实例节点上执行如下命令，检查匿名事务是否消耗完毕，参数值为`0`则代表消耗完毕。
```
show variables like "%ONGOING_ANONYMOUS_TRANSACTION_COUNT%";
```
系统显示结果类似如下：
```
mysql> show variables like '%ONGOING_ANONYMOUS_TRANSACTION_COUNT%';
+-------------------------------------+-------+
| Variable_name                       | Value |
+-------------------------------------+-------+
| Ongoing_anonymous_transaction_count | 0     |
+-------------------------------------+-------+
1 row in set (0.00 sec)
```
5. 在主从复制结构两边都设置 `gtid_mode = ON`。
```
set global gtid_mode = ON;
```
6. 在 `my.cnf` 文件中添加如下内容。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
gtid_mode = on
enforce_gtid_consistency = on
```
7. （可选）参考如下命令重启数据库。MySQL 5.7.6 之前的版本需要重启，5.7.6 及之后的版本不需要重启，但是需要中断所有业务连接。
```
[\$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[\$Mysql_Dir]/bin/safe_mysqld &
```
8. 重新执行校验任务。 

### 修改 server_id 参数
`server_id` 参数需要手动设置，且值不能设置为0。该参数系统预设值为`1`，如果查询该参数显示为`1`不一定正确，需要手动进行配置。
>?该参数修改可以不重启数据库，但是需要中断当前数据库上的所有业务连接，当源库为从库时，还需重启主从同步 SQL 线程，避免当前业务连接继续使用修改前的模式写入。

1. 登录源数据库。
2. 参考如下内容修改源数据库的配置文件 `my.cnf`。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
server_id = 2    //建议设为大于1的整数，此处仅为示例
```
3. 确认参数修改是否生效。
```
show global variables like "%server_id%";
```
系统显示结果类似如下：
```
mysql> show global variables like '%server_id%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| server_id     | 2     |
+---------------+-------+
1 row in set (0.00 sec)
```
4. 重新执行校验任务。

### 删除 do_db，ignore_db 设置
binlog 会记录数据库所有执行的 DDL 和 DML 语句，而 do_db，ignore_db 则是设置 binlog 记录的过滤条件。
- `binlog_do_db`：只记录指定数据库的二进制日志，默认全部记录。
- `binlog_ignore_db`：不记录指定的数据库的二进制日志。

设置 do_db，ignore_db 后，会导致一些跨库操作 binlog 记录不全，主从复制出现异常，因此不建议设置。如发生类似报错，请参考如下指导进行修复。
1. 登录源数据库。
2. 修改源数据库的配置文件 `my.cnf`，删除 do_db，ignore_db相关设置。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
3. 参考如下命令重启源数据库。
```
[\$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[\$Mysql_Dir]/bin/safe_mysqld &
```
>?[\$Mysql_Dir] 指源数据库的安装路径，请替换为实际的源数据库安装目录。
4. 确认参数修改是否生效。
```
show master status;
```
系统显示结果类似如下：
```
mysql> show master status;
+---------------+----------+--------------+------------------+-------------------+
| File          | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+---------------+----------+--------------+------------------+-------------------+
| binlog.000011 | 154      |              |                  |                   |
+---------------+----------+--------------+------------------+-------------------+
```
5. 重新执行校验任务。

### 修改 log_slave_updates 参数
在主从复用结构中，从库开启 `log-bin` 参数，直接在从库操作数据时，可以记录在 binlog 中，但是从库从主库上复制数据时，不能记录在 binlog 中，所以从库作为其他从库的主库时，需要打开 `log_slave_updates` 参数。 
1. 登录源数据库。
2. 修改 `log_slave_updates` 参数为`1`。
```
set global log_slave_updates = 1;
```
3. 参考如下命令重启源数据库。
```
[\$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[\$Mysql_Dir]/bin/safe_mysqld &
```
>?[\$Mysql_Dir] 指源数据库的安装路径，请替换为实际的源数据库安装目录。
4. 查看配置是否生效。
```
show global variables like '%log_slave_updates%';
```
系统显示结果类似如下：
```
mysql> show global variables like '%log_slave_updates%';
+-------------------+-------+
| Variable_name     | Value |
+-------------------+-------+
| log_slave_updates | 1     |
+-------------------+-------+
1 row in set (0.00 sec)
```
5. 重新执行校验任务。
