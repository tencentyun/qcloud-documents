In Tencent Cloud CVM, you can use the MongoDB shell client to connect TencentDB for MongoDB service for data import and export. For more information, see **Best Practice** -> [**Connection Example**]().
### mongodump and mongorestore
MongoDB provides two sets of official tools for data import and export. Generally, [mongodump](https://docs.mongodb.com/manual/reference/program/mongodump/) and [mongorestore](https://docs.mongodb.com/manual/reference/program/mongorestore/) are used to import and export the entire database. The data format, BSON, is used to facilitate massive data "dump" and "restore".<br>
The typical command for export is as follows:
```
mongodump --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb -o /data/dump_testdb
```
As shown below:
![mongodump example screenshot](https://mc.qcloudimg.com/static/img/4071cfd5d9b54c720349f41fc2e07b0c/dump_default.png)
```
mongorestore --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --dir=/data/dump_testdb
```

![mongorestore example screenshot](https://mc.qcloudimg.com/static/img/335dbef8f11a5417e42740472df1a5b8/restore_default.png)

### mongoexport and mongoimport
Generally, [mongoexport](https://docs.mongodb.com/manual/reference/program/mongoexport/) and [mongoimport](https://docs.mongodb.com/manual/reference/program/mongoimport/) are used to import and export a single collection. The data format, JSON, is used for higher readability.

Example of mongoexport:
```
mongoexport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection  -o /data/export_testdb_testcollection.json
```
In addition, you can include the "-f" parameter to specify a desired field, and "-q" to specify a query criteria so as to restrict the data to be exported.

Example of mongoimport:
```
mongoimport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection2  --file=/data/export_testdb_testcollection.json
```

### Parameters for different authentication methods
As described in the [Connection Example](https://cloud.tencent.com/doc/product/240/3563), TencentDB for MongoDB provides two user names "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM-SHA-1" authentication respectively.
For "mongouser" and all new users created in the console, simply follow the above examples to use the import and export tools.
**For "rwuser", the parameter "--authenticationMechanism=MONGODB-CR" should be included in each command.**
Take mongodump as an example:
```
mongodump --host 10.66.187.127:27017 -u rwuser -p thepasswordA1 --authenticationDatabase=admin --authenticationMechanism=MONGODB-CR --db=testdb -o /data/dump_testdb
```








