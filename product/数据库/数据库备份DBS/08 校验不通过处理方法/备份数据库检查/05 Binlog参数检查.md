## 检查详情

源数据库 binlog 相关参数需要按照如下要求配置，如果校验不通过，请参考本文后续指导进行修复。

- `log_bin` 变量必须设置为 `ON`。
- `binlog_format` 变量必须设置为 `ROW`。
- `binlog_row_image` 必须设置为 `FULL`。
- `server_id` 参数需要手动设置，且值不能设置为0。

## 修复方法

### 开启 binlog 

`log_bin` 是 binlog 的开关控制参数，需要将 binlog 打开，以便记录所有的数据库表结构和表数据变更日志。 

如发生类似报错，请参考如下指导进行修复。

1. 登录源数据库。
2. 参考如下内容修改源数据库的配置文件 `my.cnf`。因 log_bin 参数修改后需要重启数据库，所以建议同步修改 binlog_format 和 binlog_row_image 参数为校验要求配置。
>?`my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。
>
```
log_bin = MYSQL_BIN
binlog_format = ROW
binlog_row_image = FULL
```
3. 参考如下命令重启源数据库。
```
[$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[$Mysql_Dir]/bin/safe_mysqld &
```
>?[\$Mysql_Dir] 指源数据库的安装路径，请替换为实际的源数据库安装目录。
4. 确认 binlog 功能是否已启用。
```
show variables like '%log_bin%';
```
系统显示结果类似如下：
```
mysql> show variables like '%log_bin%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| log_bin          | ON    |
+------------------+-------+
| binlog_format    | ROW   |
+------------------+-------+
| binlog_row_image | FULL  |
+------------------+-------+
1 row in set (0.00 sec)
```
5. 重新执行校验任务。

### 修改 binlog_format 参数

`binlog_format` 为 binlog 的记录模式，有以下三种：

- `STATEMENT`：每一条会修改数据的 SQL 都会记录到 master 的 binlog 中，slave 在复制的时候，会执行和原来 master 端相同的 SQL。该模式可以减少 binlog 日志量，但是对某些特定的函数进行复制时，slave 端不能正确复制。
- `ROW`：binlog 日志中会记录成每一行数据修改的形式，然后在 slave 端再对相同的数据进行修改。该模式会保证 master 和 slave 的正确复制，但是 binlog 日志量会增加。
- `MIXED`：前两种模式的结合，MySQL 会根据执行的每一条具体的 SQL 语句来区分对待记录的日志形式，在 `STATEMENT` 和 `ROW` 之间选择一种。 

综上，为了保证 master 和 slave 的正确复制，`binlog_format` 参数需要设置为 `ROW`。如发生类似报错，请参考如下指导进行修复。

1. 登录源数据库。
2. 参考如下命令修改`binlog_format`。
```
set global binlog_format = ROW;
```
3. 重启线程使配置生效，然后通过如下命令查看参数修改是否生效。
```
show variables like '%binlog_format%';
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

1. 登录源数据库。
2. 参考如下内容修改 `binlog_row_image`。
```
set global binlog_row_image = FULL;
```
3. 重启线程使配置生效，然后通过如下命令查看参数修改是否生效。
```
show variables like '%binlog_row_image%';
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

### 修改 server_id 参数

`server_id` 参数需要手动设置，且值不能设置为0。该参数系统预设值为`1`，如果查询该参数显示为`1`不一定正确，需要手动进行配置。

1. 登录源数据库。
2. 参考如下内容修改 `server_id`。
```
set global server_id = 2;  //建议设为大于1的整数，此处仅为示例
```
3. 通过如下命令查看参数修改是否生效。
```
show global variables like '%server_id%';
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

