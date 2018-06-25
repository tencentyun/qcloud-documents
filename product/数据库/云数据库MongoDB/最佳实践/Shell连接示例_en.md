## Connect MongoDB via Shell
In Tencent Cloud CVM, you can use the MongoDB shell client ([See the Installation Documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/)) to connect Tencent Cloud MongoDB service for data management. Please use the latest version of MongoDB client suite.

### Quick Start
Typical connection commands are as follows:
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
As shown below:
![Screenshot Example of Typical Connection Commands](https://mc.qcloudimg.com/static/img/ce6b26f8cd6b1cc2981bc0cd44f9d09d/shell_default.png)

### Description on Connecting under Different Authentication Methods
As described in [Connection Examples](https://cloud.tencent.com/doc/product/240/3563), Tencent Cloud MongoDB provides two user names "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM - SHA - 1" authentication respectively.
For these two authentication methods, shell command parameters are not the same. Please see below for more information.

### SCRAM-SHA-1 Authentication (mongouser)
**SCRAM-SHA-1 Authentication is used with the default user "mongouser" and all new users created in the Console**. Shell connection parameters are the same as those described in [Quick Start](#.E5.BF.AB.E9.80.9F.E5.BC.80.E5.A7.8B), without additional parameters. Examples are as follows:
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
Specifically, if you want to enter a "db" directly, such as "singer", after connected with MongoDB, please proceed as the following example:
```
mongo 10.66.187.127:27017/singer -u mongouser -p thepasswordA1 --authenticationDatabase admin
```
As shown below:
![Screenshot Example of Connection Commands for Entering a "db" Directly](https://mc.qcloudimg.com/static/img/c30cc3e6e2db6c8bd3cce2e327ce63db/sha1_sonedb.png)

### MONGODB-CR Authentication (rwuser)
**Please note that MONGODB-CR authentication is used only with the default user "rwuser"**, and the authentication method of MONGODB-CR should be expressly specified in shell connection parameters. Please refer to the following example:
```
mongo 10.66.187.127:27017/admin -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR
```
As shown below:
![Screenshot Example of MONGODB-CR Authentication](https://mc.qcloudimg.com/static/img/ff200b49c3fa5c70812027dd89e3ebc3/cr_default.png)
Specifically, if you want to enter a "db" directly, such as "singer", after connected with MongoDB, please proceed as the following example:
```
mongo 10.66.187.127:27017/admin -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR --authenticationDatabase admin
```
As shown below:
![Screenshot Example of Connection Commands for Entering a "db" Directly](https://mc.qcloudimg.com/static/img/d31bfa612a295fd070ea5dd09c7ce6a3/cr_somedb.png)

### Import and Export Data Using Shell
For both authentication methods, you can use Shell to import and export data. Please [See Here](https://cloud.tencent.com/doc/product/240/5321).
