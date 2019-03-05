### 1. CDB for MySQL 使用 pt-online-schema-change 问题
CDB for MySQL 5.6 版本开始支持 Online DDL。5.5 的版本做变结构变更时，为了避免锁表导致的业务影响，仍然建议用户使用 pt-online-schema-change 等开源工具完成该类操作，但不少用户通过 CVM 使用 pt-online-schema-change 对 CDB 表结构变更时，遇到问题；
常见报错信息：
`Use of uninitialized value $host in string eq at /usr/local/percona-toolkit-3.0.3/bin/pt-online-schema-change line 4284.`
查看对应的源码：
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
从代码上看是在通过 processlist 的方式寻找 slave 的信息，由于 CDB 对复制账号相关的信息做过处理，导致通过  processlist 拿不到 slave 的信息；
修复方式：
使用 pt-osc 的时候加上如下参数，不去检查 slave 的状态；
    `--recursion-method=none`
 ### 2. CDB 导入数据报错：Specified key was too long
 #### 报错原因
`ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes`
客户通过 CVM 的命令行向 CDB 导入 XXXX.sql 文件时，CDB 返回 Specified key was too long 的报错。
对于报错信息 “ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes”，其实意思就是“索引字段长度太长，超过了 767 bytes”。

1. innodb 存储引擎，多列索引的长度限制如下：
 每个列的长度不能大于 767 bytes；所有组成索引列的长度和不能大于 3072 bytes
2.  myisam 存储引擎，多列索引长度限制如下：
每个列的长度不能大于 1000 bytes，所有组成索引列的长度和不能大于 1000 bytes

	TIPS：768/2=384个双字节 或者767/3=255个三字节的字段（GBK 是双字节的，UTF8 是三字节的，UTF8MB4 是四字节的）

为什么在自建的数据库上是 OK 的，但是把数据导入 CDB 后就报 Specified key was too long 错误呢？
在 CDB5.6 及其以上版本，所有 myisam 表都会被自动转换为 innodb，所以在自建数据库上有超过 767 bytes 的组合索引列，但是由于在自建库上 myisam 存储引擎，同样的建表语句在自建库上运行没问题，但是在 CDB5.6 版本以上就会有问题。
#### 解决方案
1. 修改备份文件中出错行组合索引列的长度
常见：
`create table test(test varcahr(255) primary key)charset=utf8;`
-- 成功
`create table test(test varcahr(256) primary key)charset=utf8;`
-- 失败
`ERROR 1071（42000）:Specified key was too long; max key length is 767 bytes`
2. 使用 CDB5.5 版本，myisam 引擎不会被自动转换为 innodb。