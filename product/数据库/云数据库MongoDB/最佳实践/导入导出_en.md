## Import and Export Data from MongoDB
In Tencent Cloud CVM, you can use the MongoDB shell client ([See the Installation Documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/)) to connect Tencent Cloud MongoDB service for data import and export. Please use the latest version of MongoDB client suite.

### Quick Start
Use the MongoDB official "mongorestore" and "mongodump" tools to import and export MongoDB databases.
#### Import Data to Tencent Cloud MongoDB
Typical import commands are as follows:
```
mongorestore --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --dir=/data/dump_testdb
```
![Screenshot Example of "mongorestore"](https://mc.qcloudimg.com/static/img/335dbef8f11a5417e42740472df1a5b8/restore_default.png)

#### Export Data for Backup
Typical export commands are as follows:
```
mongodump --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb -o /data/dump_testdb
```
As shown below:
![Screenshot Example of "mongodump"](https://mc.qcloudimg.com/static/img/4071cfd5d9b54c720349f41fc2e07b0c/dump_default.png)

### "mongodump" and "mongorestore"
MongoDB provides two sets of official tools for data import and export. Generally speaking, use [mongodump](https://docs.mongodb.com/manual/reference/program/mongodump/) and [mongorestore](https://docs.mongodb.com/manual/reference/program/mongorestore/) to import and export entire database. The data format, BSON, will be used to facilitate massive data "dump" and "restore".
As for examples of "mongodump" and "mongorestore", please see the above [Quick Start](#.E5.BF.AB.E9.80.9F.E5.BC.80.E5.A7.8B).


### "mongoexport" and "mongoimport"
Generally speaking, use [mongoexport](https://docs.mongodb.com/manual/reference/program/mongoexport/) and [mongoimport](https://docs.mongodb.com/manual/reference/program/mongoimport/) to import and export a single collection. The data format, JSON, is used for higher readability.

Example of "mongoexport":
```
mongoexport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection  -o /data/export_testdb_testcollection.json
```
In addition, you can include the "-f" argument to specify desired field, and "-q" to specify a query criteria in order to restrict the data to be exported.

Example of "mongoimport":
```
mongoimport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection2  --file=/data/export_testdb_testcollection.json
```

### Description on Argument for Different Authentication Methods
As described in [Connection Examples](https://www.qcloud.com/doc/product/240/3563), Tencent Cloud MongoDB provides two user names "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM - SHA - 1" authentication respectively.
For "mongouser" and all new users created in the Console, simply follow the above examples to use the import and export tools.
**For "rwuser", the argument "--authenticationMechanism=MONGODB-CR" should be included in each command.**
Take "mongodump" as an example:
```
mongodump --host 10.66.187.127:27017 -u rwuser -p thepasswordA1 --authenticationDatabase=admin --authenticationMechanism=MONGODB-CR --db=testdb -o /data/dump_testdb
```








