## CDB for MySQL使用pt-online-schema-change问题

CDB for MySQL 5.6版本开始支持Online DDL。5.5的版本做变结构变更时，为了避免锁表导致的业务影响，仍然建议用户使用pt-online-schema-change等开源工具完成该类操作，但不少用户通过CVM使用pt-online-schema-change对CDB表结构变更时，遇到问题；

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
从代码上看是在通过processlist的方式寻找slave的信息,由于CDB对复制账号相关的信息做过处理，导致通过processlist拿不到slave的信息；

修复方式：

使用pt-osc的时候加上如下参数，不去检查slave的状态；

    `--recursion-method=none`
 