After your instance is initialized, you can access the database using MongoDB shell or drivers in various languages to perform management operations. The database can be accessed via the private network using CVM. Access via the public network is not supported.

## Details
### Client version
For the connection of the TencentDB for MongoDB service, the driver version 3.2 or above is required. Please use the **latest version** of the client driver to ensure the best compatibility, including shell kit, java jar package, php expansion, nodejs module, etc. For more information, see [MongoDB Drivers](https://docs.mongodb.com/ecosystem/drivers/).
### Use MongoDB shell
"mongo shell" is an interactive JavaScript shell in the MongoDB. It can interact with your MongoDB instance using the command line in the shell. You can also use "mongo shell" to query and update data or perform management operations. "mongo shell" is part of MongoDB distributions. You first need to download and install MongoDB, and then use "mongo shell" to connect to your MongoDB instance. Download a MongoDB distribution by clicking the [link](https://www.mongodb.com/download-center#community). Here is an example of connection:<br>

    cd <mongodb installation dir>
	./bin/mongo -umongouser -plxh2081* 172.16.0.56:27017/admin
> In the above example, "-u" indicates the username, "-p" indicates the password, and 172.16.0.56 and 27017 indicate the IP and port of the MongoDB instance respectively.
### Use URI
The MongoDB service can be connected by passing parameters, and most drivers can also be connected by using URI. Connection to the MongoDB service using URI is officially recommended by MongoDB. Typical URIs are as follows:

Example 1
```
mongodb://username:password@IP:27017/admin
```
Example 2
```
mongodb://username:password@IP:27017/somedb?authSource=admin
```
Example 3
```
mongodb://username:password@IP:27017/somedb?authSource=admin&readPreference=secondaryPreferred
```

The parameters in the above URIs are described as follows:

| Parameter | Description | Required |
|---------|---------|---------|
| mongodb:// | A specific string indicating MognoDB protocol | Required |
| username | The username used to log in to the MongoDB service | Yes. See "[Default username](#.E9.BB.98.E8.AE.A4.E7.94.A8.E6.88.B7.E5.90.8D)" on this page. |
| password | The user password used to log in to the MongoDB service | Yes |
| IP:27017 | IP and port of the MongoDB service | Yes |
| /admin | The database to be authenticated. TencentDB for MongoDB is always admin. | Yes. See "[Authentication database](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)" on this page. |
| authMechanism=MONGODB-CR | Authentication mechanism | See "[Authentication mechanism](#.E8.AE.A4.E8.AF.81.E6.9C.BA.E5.88.B6)" on this page |
| authSource=admin | The database for authentication. TencentDB for MongoDB is always admin. | Yes. See "[Authentication database](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)" on this page. |
| readPreference=secondaryPreferred | You can set up a priority to read slave database first | No. See "[Priority to read master and slave](#.E8.AF.BB.E6.93.8D.E4.BD.9C.E7.9A.84.E4.B8.BB.E4.BB.8E.E4.BC.98.E5.85.88.E7.BA.A7)" on this page. |
Only some of the parameters for the URI used to connect MongoDB are listed here. For more information, see [MongoDB official reference documentation](https://docs.mongodb.com/manual/reference/connection-string/).

### Default users

Depending on different versions of TencentDB for MongoDB, we have built two default users: "rwuser" and "mongouser" for new instances. Only rwuser is used for the instances created earlier (we will contact you before we upgrade these instances). You can also use the TencentDB for MongoDB console for account and permission management to meet your business needs.

#### Example of rwuser (MONGODB-CR authentication) URI
**MONGODB-CR authentication is used by rwuser only**
```
mongodb://rwuser:password@10.66.100.186:27017/admin?authMechanism=MONGODB-CR
or
mongodb://rwuser:password@10.66.100.186:27017/somedb?authMechanism=MONGODB-CR&authSource=admin
```

#### Example of mongouser (SCRAM-SHA-1 authentication) URI
**SCRAM-SHA-1 authentication is used by mongouser and users created in the console**
```
mongodb://mongouser:password@10.66.100.186:27017/admin
or
mongodb://mongouser:password@10.66.100.186:27017/somedb?authSource=admin
```

### Authentication database
TencentDB for MongoDB uses "admin" database as the authentication database for login authentication, so the port in the URI must be followed by "**/admin**" to specify the authentication database. After authentication, you can read and write the specific business database. URI example:

```
mongodb://username:password@IP:27017/admin
```

You can also directly access the destination database by specifying a destination database for read and write operation and an additional authentication database parameter (authSource = admin). URI example:

```
mongodb://username:password@IP:27017/somedb?authSource=admin
```

You must use one of the above methods to add admin as an authentication database into the URI.

### Authentication mechanism
MongoDB supports multiple authentication mechanisms, and SCRAM-SHA-1 is recommended officially.
TencentDB for MongoDB supports two authentication methods: "MONGODB-CR" and "SCRAM-SHA-1".
As mentioned above, there are two default users built in TencentDB for MongoDB: "rwuser" and "mongouser", and you can also create additional users in the TencentDB for MongoDB console. These users are classified into two types based on the following authentication mechanisms:

| Username | Authentication Mechanism | Required in URI |
|---------|---------|---------|
| rwuser | MONGODB-CR | The parameter "authMechanism = MONGODB-CR" must be added |
| mongouser and users created in the console | SCRAM-SHA-1 (recommended) | No parameter needs to be added |

### Priority to read master and slave
TencentDB for MongoDB provides a load balancer IP to access the entire replica set. If you need to specify the slave database for accessing, add the "readPreference" parameter in the URI. Relevant values are described below:

| Value | Description | Default |
|---------|---------|---------|
| primary | Reads the master node only | Yes |
| primaryPreferred | Reads master node first. If it is not available, read slave node. | |
| secondary | Reads slave node only. If it is not available, an error will occur. | |
| secondaryPreferred | Reads slave node first. If it is not available, read master node. | |

To set up a priority to read slave node first, you can configure the URI as follows:

```
mongodb://username:password@IP:27017/admin?readPreference=secondaryPreferred
```

## Examples of Languages

### Shell
[Shell Connection Example](https://cloud.tencent.com/doc/product/240/Shell%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### PHP
[PHP Connection Example](https://cloud.tencent.com/doc/product/240/PHP%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### Node.js
[Node.js Connection Example](https://cloud.tencent.com/doc/product/240/Node.js%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B) 
 [mongoose Example](https://cloud.tencent.com/doc/product/240/Node.js%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B#node.js-mongoose-.E8.BF.9E.E6.8E.A5.E7.A4.BA.E4.BE.8B)
### Java
[Java Connection Example](https://cloud.tencent.com/doc/product/240/Java%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### Python
[Python Connection Example](https://cloud.tencent.com/doc/product/240/Python%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### Reconnection mechanism
[Reconnection Mechanism](https://cloud.tencent.com/doc/product/240/4980)

