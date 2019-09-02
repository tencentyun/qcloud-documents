### 从 MongoDB 数据库中导出数据，如何设置参数？
mongodump 的参数中设置 --readPreference=secondaryPreferred。

### MongoDB 支持哪些数据迁移？
目前支持两类迁移：云数据库 CVM 自建实例迁移、外网实例迁移，详情请参见 [MongoDB 数据迁移](https://cloud.tencent.com/document/product/240/8271)。

### 使用 mongodump（整库）或者 mongoexport（单个集合），如何把 MongoDB 的数据导出到本地？

在CVM 中可用 MongoDB 提供的 [shell 客户端](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/) 连接云数据库 MongoDB 进行数据导出，**请注意使用最新版本的 MongoDB 客户端套件**。
MongoDB 官方提供了两套数据导出工具，一般来说，进行整库导出时使用 mongodump，操作的数据是 BSON 格式，进行大量 dump 效率较高；进行单个集合导出时使用 mongoexport，操作的数据是 JSON 格式，可读性较高。
**1. 使用 mongodump 进行整库导出备份**
 导出命令如下：

```
 mongodump --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb -o /data/dump_testdb
```

![图片描述](//bot1024-1253841380.file.myqcloud.com/598299decb2a1.png)

**2. 使用 mongoexport 进行单个集合导出备份**
导出命令如下:

```
mongoexport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection  -o /data/export_testdb_testcollection.json
```

> ?您也可以加上 -f 参数指定需要的字段，-q 参数指定一个查询条件来限定要导出的数据。

**3. 关于 rwuser 和 mongouser 用户名在写导出命令时的参数说明** 
在 [连接示例](https://cloud.tencent.com/document/product/240/3563) 文档中有说明，腾讯云 MongoDB 默认提供了 rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式。

- 对于 mongouser 以及在控制台创建的所有新用户，在使用导出命令工具时按照上文示例操作即可。
- 对于 rwuser，需要在每个命令里加入参数 --authenticationMechanism=MONGODB-CR 。

mongodump 示例说明：

```
 mongodump --host 10.66.187.127:27017 -u rwuser -p thepasswordA1 --authenticationDatabase=admin --authenticationMechanism=MONGODB-CR --db=testdb -o /data/dump_testdb
```

### 使用 mongorestore（整库）或者 mongoimport（单个集合），如何把数据从本地导入到 MongoDB？

在 CVM 中可用 MongoDB 提供的 [shell 客户端](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/) 连接云数据库 MongoDB 进行数据导入，**请注意使用最新版本的 MongoDB 客户端套件**。
MongoDB 官方提供了两套数据导入工具，一般来说，进行整库导出时使用 mongorestore，操作的数据是 BSON 格式，进行大量 mongorestore 效率较高；进行单个集合导出时使用 mongoimport，操作的数据是 JSON 格式，可读性较高。    
**1. 使用 mongorestore 进行整库导入备份**
导入命令如下：

```
mongorestore --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --dir=/data/dump_testdb
```

![图片描述](//bot1024-1253841380.file.myqcloud.com/5982b30189287.png)
**2. 使用mongoimport进行单个集合导入备份**
导入命令如下:

```
mongoimport --host 10.66.187.127:27017 -u mongouser -p thepasswordA1 --authenticationDatabase=admin --db=testdb --collection=testcollection2  --file=/data/export_testdb_testcollection.json
```

**3.关于 rwuser 和 mongouser 用户名在写导入命令时的参数说明**
在 [连接示例](https://cloud.tencent.com/document/product/240/3563) 文档有说明，腾讯云 MongoDB 默认提供了  rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式。

- 对于 mongouser 以及在控制台创建的所有新用户，在使用导入命令工具时按照上文示例操作即可。
- 对于 rwuser，需要在每个命令里加入参数 --authenticationMechanism=MONGODB-CR。

用 mongorestore 示例：

```
 mongorestore --host 10.66.187.127:27017 -u rwuser -p thepasswordA1 --authenticationDatabase=admin --authenticationMechanism=MONGODB-CR --db=testdb -o /data/dump_testdb
```

### 为什么数据导入到 MongoDB 实例后，占用空间比自建的 MongoDB 小？

可能存在以下几个原因：
- 原始数据库长时间运行积累了大量的增删改操作。
- 写操作时 MongoDB 出于性能考虑在空间分配时分配了大于实际数据的空间。
- 删除数据后原空间没有被再次利用。
  综合下来导致整个数据库空间的空洞率较高，而导入数据时相当于做了一次类似磁盘整理的操作，使导入后的数据保存得相对紧凑，所以看起来数据变小了。

### MongoDB 的 mongodump 无法导出数据，如何处理？
mongodump 使用参见 [导入导出](https://cloud.tencent.com/document/product/240/5321)，mongodump 工具建议使用3.2.10以上版本。
