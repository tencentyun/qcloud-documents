## Overview
After the instance is initialized, you can access the database using various language drivers to access the data.
You need to use CVM to access through the private network. Currently, the access through the public network is not supported.
## Quick Start

### Example of rwuser (MONGODB-CR authentication) URI
**rwuser is the unique user who uses MONGODB-CR authentication **
```
mongodb://rwuser:password@10.66.100.186:27017/admin?authMechanism=MONGODB-CR
Or
mongodb://rwuser:password@10.66.100.186:27017/somedb?authMechanism=MONGODB-CR&authSource=admin
```

### Example of mongouser (SCRAM-SHA-1 authentication) URI
**Both mongouser and users created in the cloud console use SCRAM-SHA-1 authentication**
```
mongodb://mongouser:password@10.66.100.186:27017/admin
Or
mongodb://mongouser:password@10.66.100.186:27017/somedb?authSource=admin
```

## Details
### Client Version
For the connection of the Tencent Cloud MongoDB service, the driver version 3.2 or above is required. Please use **the latest version** of the client driver to ensure the best compatibility, including shell kit, java jar package, php expansion, nodejs module, etc. For more information, please see [MongoDB Drivers](https://docs.mongodb.com/ecosystem/drivers/).

### Recommending to Use URI
MongoDB services can be connected by passing parameters, and most drivers can also be connected by using URI.
The connection to MongoDB services using URI is officially recommended by MongoDB. Typical URIs are as follows:

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
| mongodb:// | A specific string, which indicates MongoDB protocol | Yes |
| username | The username used to log in to MongoDB service | Yes. For more information, please see "[Default User Name](#.E9.BB.98.E8.AE.A4.E7.94.A8.E6.88.B7.E5.90.8D)" on this page |
| password | The password used to log in to MongoDB service | Yes |
| IP:27017 | The IP and port of MongoDB service | Yes |
| /admin | The database to be authenticated. Tencent Cloud MongoDB is always admin | Yes. For more information, please see "[Authentication Database](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)" on this page |
| authMechanism=MONGODB-CR | Authentication mechanism | For more information, please see "[Authentication Mechanism](#.E8.AE.A4.E8.AF.81.E6.9C.BA.E5.88.B6)" on this page |
| authSource=admin | The database for authentication. Tencent Cloud MongoDB is always admin | Yes. For more information, please see "[Authentication Database](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)" on this page |
| readPreference = secondaryPreferred | You can set up a priority to read slave database first | No. For more information, please see "[Priority to Read Master and Slave](#.E8.AF.BB.E6.93.8D.E.BD.9C.E7. 9A.84.E4.B8.BB.E4.BB.8E.E4.BC.98.E5.85.88.E7.BA.A7)" on this page |
Only some of the parameters for the URI used to connect MongoDB are listed here. For more information, please see [MongoDB Official Reference Documentation](https://docs.mongodb.com/manual/reference/connection-string/).

### Default User Names

Depending on different versions of Tencent Cloud MongoDB, we have built two default users: "rwuser" and "mongouser" for new instances.
Only rwuser is used for the instances created earlier (we will contact you before we upgrade these instances).
You can also use the Tencent Cloud MongoDB console for account and permission management to meet your business needs.

### Authentication Database
Tencent Cloud MongoDB uses "admin" database as the authentication database for login authentication, so the port in the URI must be followed by "**/admin**" to specify the authentication database. After authentication, you can read and write the specific business database. URI example:

```
mongodb://username:password@IP:27017/admin
```

You can also directly access the destination database by specifying a destination database for read and write operation and an additional authentication database parameter (authSource = admin). URI Example:

```
mongodb://username:password@IP:27017/somedb?authSource=admin
```

In summary, you must use one of the above methods to add admin as an authentication database into the URI.

### Authentication Mechanism
MongoDB supports multiple authentication mechanisms, and "SCRAM-SHA-1" is recommended officially.
Tencent Cloud MongoDB supports two authentication methods: "MONGODB-CR" and "SCRAM-SHA-1".
As mentioned above, there are two default users built in Tencent Cloud MongoDB: "rwuser" and "mongouser", and you can also create additional users in Tencent Cloud MongoDB console. These users are classified into two types based on the following authentication mechanisms:

| Username | Authentication Mechanism | Required in URI |
|---------|---------|---------|
| rwuser | MONGODB-CR | Parameter "authMechanism = MONGODB-CR" must be added |
| The "mongouser" and users created in the cloud console | SCRAM-SHA-1 (recommended) | No parameter needs to be added |

### Priority to Read Master and Slave
Tencent Cloud MongoDB provides a cloud load balancer IP to access the entire replica set. If you need to specify the slave database for accessing, please add the "readPreference" parameter in the URI. Relevant values are described below:

| Value | Description | Default |
|---------|---------|---------|
| primary | Read master node only | Yes |
| primaryPreferred | Read master node first. If it is not available, read slave node |  |
| secondary | Read slave node only. If it is not available, an error will occur | 　|
| secondaryPreferred | Read slave node first. If it is not available, read master node |  |

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
### Reconnection Mechanism
[Reconnection Mechanism](https://cloud.tencent.com/doc/product/240/4980)

