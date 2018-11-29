### 1. A problem occurs when using pt-online-schema-change for CDB for MySQL
Online DDL is supported in CDB for MySQL 5.6 or above. For CDB for MySQL 5.5, you're still recommended to use such open source tools as pt-online-schema-change to change the table structure to prevent your business being affected by table lock. But many users encounter a problem when using pt-online-schema-change to change the CDB table structure via CVM.
The common error message is:
`Use of uninitialized value $host in string eq at /usr/local/percona-toolkit-3.0.3/bin/pt-online-schema-change line 4284.`
The source code is as follows:
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
In the code, the information of slave is located through processlist. Because CDB has processed the information of the replicated account, slave information cannot be obtained through processlist.
Solution:
When using pt-osc, add the following parameters to skip the check of slave status.
    `--recursion-method=none`
 ### 2. An error occurs when importing data to CDB: Specified key was too long
 #### Reason
`ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes`
CDB returns the error "Specified key was too long" when user imports XXXX.sql file to the CDB using the CVM command line.
The error message "ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes" indicates the index field exceeds the length limit: 767 bytes.

1. For innodb storage engine, the length limit on multi-column indexes is as follows:
 The maximum length of a single index column is 767 bytes, and the total length of all the index columns should not be greater than 3,072 bytes.
2. For myisam storage engine, the length limit on multi-column indexes is as follows:
The maximum length of a single index column is 1,000 bytes, and the total length of all the index columns should not be greater than 1,000 bytes.

	Tips: 768/2=384 double-byte fields or 767/3=255 three-byte fields, (GBK is double-byte encoding, UTF8 is three-byte, and UTF8MB4 is four-byte).

The data can be imported to a self-built database normally, but during the data import to CDB, the error "Specified key was too long" occurs - what is the reason for this problem?
When the total length of index columns exceeds 767 bytes in a self-built database, table-building statements can run on the database normally because the database uses myisam storage engine. But in the CDB5.6 or above, all the myisam tables are converted to to innodb ones automatically. In this case, when the total length of index columns exceeds 767 bytes, an error occurs. 
#### Solutions
1. Modify the length of index columns in the error lines in the backup file.
Examples:
`create table test(test varcahr(255) primary key)charset=utf8;`
-- Successful
`create table test(test varcahr(256) primary key)charset=utf8;`
-- Failed
`ERROR 1071(42000):Specified key was too long; max key length is 767 bytes`
2. Use CDB 5.5, in which myisam engine is not automatically converted to innodb.
