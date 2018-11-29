### How to Select the Instance Specification?
Use DCDB for functional testing with no special performance requirements: 2 shards, and the specification for each one: memory: 2 GB, disk: 25 GB.
In initial stage of business, total size of data is small but grows fast: 2 shards, and the specification for each one: memory: 16 GB, disk: 200 GB.
In stable development stage, sharding is based on actual business conditions: 4 shards, and the specification for each one: current business peak * growth rate/4.
For more information on instance specification, please see [DCDB Instance and Shard Configuration Document](https://cloud.tencent.com/document/product/557/9347).

### Compatibility and Restriction for DCDB Syntax and MySQL
For the current version of DCDB, you cannot configure user permission through command lines. You need to log in to Tencent Cloud console to configure.
Current version of DCDB does not support features including custom function, view, trigger, foreign key and sub-query.
For more information on the compatibility of MySQL syntax, please see [Use Restrictions Document](https://cloud.tencent.com/document/product/557/8765#sql.E9.99.90.E5.88.B6.E8.AF.A6.E8.BF.B0).

### How to Select a shardkey?
The shardkey is the data table field used to generate the split rules during the horizontal split, which should be specified when creating the table. It's recommended by DCDB that the shardkey can be used to find the business logic body of the data in data table and it's certain that major (or core) database operations are performed around the data of this body, and then the field corresponding to that body can be used as the shardkey for table split (the shard solution called Group-Shard). It's as shown below:
![](https://mc.qcloudimg.com/static/img/b7ed0dd48a27c0c534fa490f56b6605d/groupshard.png)
Group-Shard can ensure that some of the associated data and complex business logic computing of different split tables can be aggregated into one physical shard. For example, if both the order table and user table of an e-commerce platform are split based on the UserID, the platform can quickly calculate how many orders a user has recently placed through join query (without cross-node join or distributed transaction).

Some typical application scenarios of selecting a shardkey are as follows:
 - For user-based Internet applications, it's about a variety of operations based on users. The business logic body is user, and the field corresponding to the user can be used as a shardkey.
 - For e-commerce applications or O2O applications, it's about a variety of operations based on sellers/buyers. The business logic body is the seller/buyer and the field corresponding to the seller/buyer can be used as a shardkey. Please note that in some cases several super sellers account for the vast majority of transactions, resulting in significantly higher load and pressure in some of the shards. We will explain it in later chapters.
 - For game applications, it's about various operations based on players. The business logic body is the player and the field corresponding to the player can be used as a shardkey.
 - For Internet of Things (IOT) applications, it's about operations based on IOT information. The business logic body is sensor/SIM card and the field corresponding to the sensor, independent equipment and SIM card IMEI can be used as a shardkey.
 - For taxation/business/social insurance applications, it's mainly about developing foreground business based on the information of the taxpayer/legal person/resident. The business logic body is the taxpayer/legal person and the field corresponding to taxpayer/legal person can be used as a shardkey.
 - For most of other types of scenarios, the right business logic body can also be found as the choice for shardkey. Please note that there are some restrictions in selecting the shardkey. For more information, please see [Shard Key Selection Restrictions](https://cloud.tencent.com/document/product/557/8767).

### Can shardkey be Changed?
Once you have chosen the shard field (shardkey), you can not easily change it. If you need to modify the shard field of a table, you can only create a new table.
If you need to modify a shardkey value in a line of a sub-table, you need to "insert" and then "delete" it. Direct "update" operation can not modify the value of shard field.

### How does a shardkey Function?
When you use a sub-table, you'd better to execute the select operation with shardkey, and the routing will be automatically redirected to the corresponding shard, achieving a higher efficiency. You can also execute the operation without the shardkey, but the system will automatically scan the entire table, which is less efficient.
When you use a sub-table, shardkey must be included in the operation of insert/replace or delete/update, otherwise the operation will be denied. Performing the operation of insert/replace requires specifying the shardkey, indicating the location of the physical shard where the data is inserted. Performing the operation of delete/update requires specifying shardkey as validation, to avoid accidental deletion.

### Whether Distributed JOIN and TRANSACTION are Supported?
For now, DCDB only supports JOIN and TRANSACTION under a single shardkey and TRANSACTION across nodes. The JOIN across nodes is not supported yet.

