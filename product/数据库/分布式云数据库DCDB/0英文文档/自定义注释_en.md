Specific feature can by implemented by adding an annotation (hint) before SQL. TDSQL provides the following hints:

## Transparent Transfer of SQL to Specified Physical Shard
Transparent SQL transfer: SQL can be transferred to one or more corresponding physical shards (set) transparently and to the set of shardkey. Example:

```
	mysql> /*sets:set_1*/select * from test1 where a in (select a from test1);

Syntax:

	/*sets:set_1*/
	/*sets:set_1,set_2*/ 
	/*sets:allsets*/
	/*shardkey:10*/
```


## Achieving Read-write Separation by Implementing SQL in Slave Database Forcedly

DCDB for Percona and MariaDB support a variety of read-write separation solutions. The solution `/*slave*/` commonly used in the code implementation is solidified into business logic for the convenience of developers. Example:

```
	mysql> /*slave*/select * from test.ff limit 0;
```

## Others
Execute the specific SQL of DCDB for Percona and MariaDB. For more information, please see <control instructions>
