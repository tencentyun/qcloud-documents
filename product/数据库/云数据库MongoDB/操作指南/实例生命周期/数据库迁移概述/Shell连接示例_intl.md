## Connecting MongoDB via Shell
In Tencent Cloud CVM, you can use the MongoDB shell client ([see the Installation Documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/)) to connect with TencentDB for MongoDB service for data management. Please use the latest version of MongoDB client suite.

### Quick start
A typical connection command is as follows:
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
As shown below:
![Example of typical connection command](https://mc.qcloudimg.com/static/img/ce6b26f8cd6b1cc2981bc0cd44f9d09d/shell_default.png)

### Connection under different authentication methods
As described in the [Connection Example](https://cloud.tencent.com/doc/product/240/3563), TencentDB for MongoDB provides two user names "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM-SHA-1" authentication respectively.
For these two authentication methods, shell command parameters are not the same. See below for more information.

### SCRAM-SHA-1 authentication (mongouser)
**SCRAM-SHA-1 authentication is used by the default user "mongouser" and all new users created in the console.** Shell connection parameters are the same as those described in [Quick Start](#.E5.BF.AB.E9.80.9F.E5.BC.80.E5.A7.8B), without additional parameters. See the example below:
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
Specifically, if you want to enter a "db" directly, such as "singer", after connected with MongoDB, please proceed as described below:
```
mongo 10.66.187.127:27017/singer -u mongouser -p thepasswordA1 --authenticationDatabase admin
```
As shown below:
![Example of connection command of inserting a DB](https://mc.qcloudimg.com/static/img/c30cc3e6e2db6c8bd3cce2e327ce63db/sha1_sonedb.png)

### MONGODB-CR authentication (rwuser)
**Please note that MONGODB-CR authentication is used only by the default user "rwuser",** and the authentication method of MONGODB-CR should be expressly specified in shell connection parameters. See the following example:
```
mongo 10.66.187.127:27017/admin -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR
```
As shown below:
![Example of MONGODB-CR authentication](https://mc.qcloudimg.com/static/img/ff200b49c3fa5c70812027dd89e3ebc3/cr_default.png)
Specifically, if you want to enter a "db" directly, such as "singer", after connected with MongoDB, please proceed as described below:
```
mongo 10.66.187.127:27017/singer -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR --authenticationDatabase admin
```
As shown below:
![Example of connection command of inserting a DB](https://mc.qcloudimg.com/static/img/d31bfa612a295fd070ea5dd09c7ce6a3/cr_somedb.png)

### Import and export data using shell
For both authentication methods, you can use Shell to import and export data. [See Here](https://cloud.tencent.com/doc/product/240/5321).

