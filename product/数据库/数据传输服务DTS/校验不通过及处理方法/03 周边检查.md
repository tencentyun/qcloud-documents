
## MySQL/TDSQL MySQL/TDSQL-C 检查详情
- 检查要求：源数据库环境变量参数 `innodb_stats_on_metadata` 需要设置为 `OFF`。 
- 检查说明：
   - `innodb_stats_on_metadata` 参数开启时，每当查询 `information_schema` 元数据库里的表，Innodb 就会更新 `information_schema.statistics` 表，导致访问时间变长。关闭后可加快对于 schema 库表的访问。
   - MySQL 5.6.6 之前版本 `innodb_stats_on_metadata` 参数预设值为 `ON`，需要修改为 `OFF`。MySQL 5.6.6 及其以后的版本预设值为 `OFF`，不存在问题。

## 修复方法
>?该参数修改可以不重启数据库，但是需要中断当前数据库上的所有业务连接，当源库在从机时，还需重启主从同步 SQL 线程，避免当前业务连接继续使用修改前的模式写入。

1. 登录源数据库。
2. 修改 `innodb_stats_on_metadata` 为 `OFF`。
```
set global innodb_stats_on_metadata = OFF 
```
3. 查看配置是否生效。
```
show global variables like "%innodb_stats_on_metadata%";
```
系统显示结果类似如下：
```
mysql> show globle table status like '%innodb_stats_on_metadata%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| innodb_stats_on_metadata | OFF   |
+--------------------------+----- -+
1 row in set (0.00 sec)
```
4. 重新执行校验任务。

