## Questions About CDB for MySQL Using pt-online-schema-change

CDB for MySQL Version 5.6 and above starts to support Online DDL. In the table structure change with version 5.5, we advise that you use pt-online-schema-change and other open source tools to avoid any table lock which may impact your business. However, you may encounter some problems when using pt-online-schema-change to change the CDB table structure through CVM.

Common error messages:

   `Use of uninitialized value $host in string eq at /usr/local/percona-toolkit-3.0.3/bin/pt-online-schema-change line 4284.`

View its source code:

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
The code shows that the processlist is used to look for the information about slave. Because CDB has processed the information related to the copied account, slave information cannot be obtained through processlist;

Fixing method:

Add the following parameters when using pt-osc without checking the state of slave;

    `--recursion-method=none`
 
