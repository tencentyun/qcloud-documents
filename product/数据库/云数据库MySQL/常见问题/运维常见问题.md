### 云数据库 MySQL 使用 pt-online-schema-change 问题
云数据库 MySQL 5.6 版本开始支持 Online DDL。5.5版本做表结构变更时，为了避免锁表导致的业务影响，仍然建议用户使用 pt-online-schema-change 等开源工具完成该类操作，但不少用户通过 CVM 使用 pt-online-schema-change 对 MySQL 表结构变更时，遇到问题。

- 常见报错信息：
`Use of uninitialized value $host in string eq at /usr/local/percona-toolkit-3.0.3/bin/pt-online-schema-change line 4284.`
- 查看对应的源码：
``` perl
sub _find_slaves_by_processlist {
   my ( $self, $dsn_parser, $dbh, $dsn ) = @_;

   my @slaves = map  {
      my $slave        = $dsn_parser->parse("h=$_", $dsn);
      $slave->{source} = 'processlist';
      $slave;
   }
   grep { $_ }
   map  {
      my ( $host ) = $_->{host} =~ m/^([^:]+):/;
      if ( $host eq 'localhost' ) {
         $host = '127.0.0.1'; # Replication never uses sockets.
      }
      $host;
   } $self->get_connected_slaves($dbh);

   return @slaves;
}
```
从代码上看是在通过 processlist 的方式寻找 slave 的信息，由于 TencentDB 对复制账号相关的信息做过处理，导致通过  processlist 拿不到 slave 的信息。
- 修复方式：
使用 pt-osc 的时候加上如下参数，不去检查 slave 的状态。
    `--recursion-method=none`
 
### TencentDB 导入数据报错 Specified key was too long
**报错原因**：
客户通过 CVM 的命令行向 MySQL 导入 XXXX.sql 文件时，MySQL 返回 Specified key was too long 的报错。
报错信息 “ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes”，其意思是“索引字段长度太长，超过了767bytes”。
- innodb 存储引擎，多列索引的长度限制如下：
 每个列的长度不能大于767bytes，所有组成索引列的长度和不能大于3072bytes。
- myisam 存储引擎，多列索引的长度限制如下：
每个列的长度不能大于1000bytes，所有组成索引列的长度和不能大于1000bytes。
>?768 / 2 = 384个双字节或者767 / 3 = 255个三字节的字段（GBK 是双字节的、UTF8 是三字节的、UTF8MB4 是四字节的）

MySQL 5.6 及其以上版本，所有 myisam 表都会被自动转换为 innodb，所以在自建数据库上有超过767bytes的组合索引列，但是由于在自建库上 myisam 存储引擎，同样的建表语句在自建库上运行没问题，但是在 MySQL 5.6 版本以上就会有问题。

**解决方案：**
1. 修改备份文件中出错行组合索引列的长度。
常见：
`create table test(test varcahr(255) primary key)charset=utf8;`
-- 成功
`create table test(test varcahr(256) primary key)charset=utf8;`
-- 失败
`ERROR 1071（42000）:Specified key was too long; max key length is 767 bytes`
2. 使用 TencentDB 5.5 版本，myisam 引擎不会被自动转换为 innodb。

<span id = "outfile"></span>
### select * from XX into outfile xxxx 报错是什么原因呢？
由于平台安全性原因，不支持开通 file 权限，不支持使用 select into outfile 方式导出数据 ，建议您使用其他方式导出。

<span id = "emoji"></span>
### MySQL 数据库插入 emoji 表情乱码怎么办？
需排查 MySQL 实例内部、客户端、到 MySQL 实例的连接3个方面，是否未统一使用或者支持 utf8mb4 字符集。
要实现存储 emoji 表情到 MySQL 实例，需要 MySQL 实例内部、客户端、到 MySQL 实例的连接3个方面统一使用或者支持 utf8mb4 字符集。
1. 首先需要 MySQL 实例设置字符集为 utf8mb4。可以通过登录控制台修改`character_set_server`参数。
>!修改此参数会使数据库重启，建议您提前备份数据库，避免出现不必要的损失。
2. 用户的程序客户端需要保证输出的字符串的字符集为 utf8mb4。 
3. 应用程序创建连接是需要指定执行字符集，以常见的 jdbc 连接为例： 
对于jdbc连接，需要使用 MySQL Connector/J 5.1.13（含）以上的版本，示例代码如下： 
```
String query = “set names utf8mb4”; 
stat.execute(query);
```

<span id = "canshuxiugai"></span>
### 常见参数修改以及意义
云数据库 MySQL 已在官方的默认值基础上进行了优化，但基于客户不同的业务场景，在购买实例后，根据您的业务场景建议对以下参数进行合理的配置：

#### character_set_server
- 默认值：LATIN1
- 是否需要重启：是
- 作用：用于配置 MySQL 服务器的默认字符集。云数据库 MySQL 提供4种字符集，分别为 LATIN1、UTF8、GBK、UTF8MB4，其中 LATIN1 支持英文字符，一个字符占用一个字节；UTF8 包含全世界所有国家需要用到的字符，是国际编码，通用性强，一个字符占用三个字节；GBK 的文字编码是用双字节来表示的，即不论中、英文字符均使用双字节来表示；UTF8MB4 作为 UTF8 的超集，完全向下兼容，一个字符占用四个字节，且支持 emoji 表情。
- 建议：购买实例后，根据业务所需要支持的数据格式选择适合的字符集，确保客户端与服务器端设置相同的字符集，避免因字符集设置不正确而引发乱码的问题和不必要的重启操作。

#### lower_case_table_names
- 默认值：0
- 是否需要重启：是
- 作用：创建数据库及表时，存储与查询时是否大小写敏感。该参数可以设置的值为0、1，默认的参数值为0，表示创建数据库及表时，存储与查询均区分大小写，反之则不做区分。
- 建议：数据库 MySQL 默认大小写敏感，请根据您的业务需求及使用习惯进行合理的配置。

#### sql_mode
- 默认值：
```
NO_ENGINE_SUBSTITUTION（5.6版本），ONLY_FULL_GROUP_BY、STRICT_TRANS_TABLES、NO_ZERO_IN_DATE、NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO、NO_AUTO_CREATE_USER、NO_ENGINE_SUBSTITUTION（5.7版本）
```
- 是否需要重启：否
- 作用：MySQL 可以运行在不同 sql 模式，sql 模式定义了 mysql 应该支持的 sql 语法、数据校验等。
该参数5.6版本的默认参数值为`NO_ENGINE_SUBSTITUTION`，表示使用的存储引擎被禁用或未编译则抛出错误；5.7版本的默认参数值为`ONLY_FULL_GROUP_BY、STRICT_TRANS_TABLES、NO_ZERO_IN_DATE、NO_ZERO_DATE、ERROR_FOR_DIVISION_BY_ZERO、NO_AUTO_CREATE_USER、NO_ENGINE_SUBSTITUTION`。
其中：
 - `ONLY_FULL_GROUP_BY`表示在 GROUP BY 聚合操作时，如果在 SELECT 中的列、HAVING 或者 ORDER BY 子句的列，必须是 GROUP BY 中出现或者依赖于 GROUP BY 列的函数列。
 - `STRICT_TRANS_TABLES`为启用严格模式；NO_ZERO_IN_DATE 是否允许日期中的月份和日包含 0，且受是否开启严格模式的影响。
 - `NO_ZERO_DATE`数据库不允许插入零日期，且受是否开启严格模式的影响。
 - `ERROR_FOR_DIVISION_BY_ZERO`在严格模式下，INSERT 或 UPDATE 过程中，如果数据被零除，则产生错误而非警告，而非严格模式下，数据被零除时 MySQL 返回 NULL。
 - `NO_AUTO_CREATE_USER`禁止 GRANT 创建密码为空的用户。
 - `NO_ENGINE_SUBSTITUTION`使用的存储引擎被禁用或者未编译则抛出错误。
- 建议：由于不同的 SQL 模式支持不同的 SQL 语法，建议根据您的业务场景及开发习惯进行合理的配置。

#### long_query_time
- 默认值：10
- 是否需要重启：否
- 作用：用于指定慢查询的界定时间，默认值为10s。当某个查询执行时间为10s及以上，该查询的执行情况会记录于慢日志中，便于过后对慢查询进行分析。
- 建议：基于客户业务场景及性能敏感度不同，建议根据各自业务场景设置合理的值，以便事后进行性能分析。

