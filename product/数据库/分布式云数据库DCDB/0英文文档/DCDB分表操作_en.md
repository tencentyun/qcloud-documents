Here is a brief introduction to some simple operations of database after connecting DCDB. We take sub-table as an example.
### Create Table
- For more information on the differences of sub-table, single table and broadcast table, please refer to [Document of the Relevant Table](https://cloud.tencent.com/document/product/557/8764#.E5.88.86.E8.A1.A8.EF.BC.9A.E5.8F.82.E8.80.83.26lt.3B.E5.88.86.E8.A1.A8.26gt.3B).
- For selection restrictions on shardkey, refer to [Document of shardkey Selection Restrictions](https://cloud.tencent.com/document/product/557/8767#shardkey.E9.80.89.E6.8B.A9.E7.9A.84.E9.99.90.E5.88.B6)
- When creating a sub-table, the shardkey needs to be specified. The example of codes is as follows:
```
mysql> create table test1(id int primary key,name varchar(20),addr varchar(20))shardkey=id;
Query OK,0 rows affected(0.15 sec)
```
		
### Insert Data
> **Note:**
> 
>  shardkey must be included in the field of "insert". Otherwise the operation will be denied.

- Insert the data into the table just created, and the example of codes is as follows:
```
mysql> insert into test1(id,name);
Query OK,1 rows affected(0.08 sec)
mysql> insert into test3(name,addr) values('example','shenzhen');
ERROR 7013 (HY000): Proxy ERROR:get_shardkeys return error
```

### Query Data
> **Note:**
> When you query data, you'd better include shardkey, and the distributed routing will be automatically redirected to the corresponding shard, achieving the highest efficiency. Otherwise, the data system automatically scans the whole table, and gathers the result at the gateway, which is less efficient.

- The example of codes for querying data is as follows:
```
mysql> select id from test1 where id=1;
```

### Delete Data
> **Note:**
> 
> "where" condition must be included in "delete" and "where" condition is recommended to include shardkey. The example of codes is as follows:

- The example of codes for deleting codes is as follows:
```
mysql> delete from test1 where a=1;
Query OK, 1 row affected (0.02 sec)
```
