
连接数据库后，您可以创建数据库，写入数据。

## 创建数据库
MongoDB 创建数据库的语法格式如下： 
```
use DATABASE_NAME
```

创建一个名为 myFirstDB 的数据库，并插入文档。
```
> use myFirstDB
switched to db myFirstDB
> db.myFirstDB.insert({"test":"myFirstDB"})
WriteResult({ "nInserted" : 1 })
```

查询已创建的数据库。
```
> show dbs
admin      0.000GB
config     0.000GB
local      0.041GB
myFirstDB  0.000GB
```

## 创建集合
MongoDB 中使用 createCollection() 方法来创建集合。
语法格式：
```
db.createCollection(name, options)
```
参数说明：
- name：要创建的集合名称。
- options：可选参数, 指定有关内存大小及索引的选项。

| options 字段 | 类型 |      | 描述                                                         |
| ----------- | ---- | ---- | ------------------------------------------------------------ |
| capped      | BOOL | 否   | 指是否设置集合的最大字节数。如果为 true，需设置 size 参数。默认为 false。 |
| autoIndexId | BOOL | 否   | 设置是否自动创建索引。如为 true，自动在 \_id 字段创建索引。默认为 false。 |
| size        | 数值 | 否   | 设置集合的最大字节数。                                       |
| max         | 数值 | 否   | 设置集合包含文档的最大数量。                                 |

在 myFirstDB 数据库中创建 FirstCol 集合示例：
```
> use myFirstDB
switched to db myFirstDB
> db.createCollection("FirstCol")
{
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1634821900, 2),
                "signature" : {
                        "hash" : BinData(0,"WFu7yj8wjeUBWG3b+oT84Q8wIw8="),
                        "keyId" : NumberLong("6990600483068968961")
                }
        },
        "operationTime" : Timestamp(1634821900, 2)
}
```

查看创建的集合：
```
> show collections
FirstCol
```

创建集合 FirstCol，最大字节数为 6142800B，文档最大个数为10000个，示例如下：
```
> db.createCollection("FirstCol", { capped : true, autoIndexId : true, size : 6142800, max : 10000 } )
{
        "note" : "the autoIndexId option is deprecated and will be removed in a future release",
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1634821879, 1),
                "signature" : {
                        "hash" : BinData(0,"EuIbp2fu9Yh38HOBHLgYqljdKaE="),
                        "keyId" : NumberLong("6990600483068968961")
                }
        },
        "operationTime" : Timestamp(1634821879, 1)
}
```

## 插入文档
-  MongoDB 使用 insert() 或 save() 方法向集合中插入文档，示例如下：
```
> db.FirstCol.insert({name:"李四",sex:"女",age:25,status:"A"})
WriteResult({ "nInserted" : 1 })
```
查看集合中插入的文档：
```
> db.FirstCol.find()
{ "_id" : ObjectId("61716957a6fe1ef4d7eae979"), "name" : "李四", "sex" : "女", "age" : 25, "status" : "A" }
```
  
- db.collection.insertMany() 用于向集合插入一个多个文档，语法格式如下：
```
db.collection.insertMany(
   [ <document 1> , <document 2>, ... ]
   )
```
示例如下：
```
> db.FirstCol.insertMany([{name:"李三",sex:"女",age:25,status:"A"},{name:"王六",sex:"男",age:26,status:"B"},{name:"王五",sex:"男",age:26,status:"A",groups:["news","sports"]}])
{
       
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("617282a3a4bb72d733b5c6d7"),
                ObjectId("617282a3a4bb72d733b5c6d8"),
                ObjectId("617282a3a4bb72d733b5c6d9")
        ]
}
```

## 更新数据库
MongoDB使用 update() 更新集合中的文档。

更新 FirstCol 集合 name 为李三的数据，示例如下：
```
> db.FirstCol.update({name:"李三",sex:"女",age:25,status:"A"},{$set:{'age':28}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

查询修改结果：
```
> db.FirstCol.find().pretty()
{
        "_id" : ObjectId("618904b6258a6c38daf13abd"),
        "name" : "李三",
        "sex" : "女",
        "age" : 28,
        "status" : "A"
}
{
        "_id" : ObjectId("618904b6258a6c38daf13abe"),
        "name" : "王六",
        "sex" : "男",
        "age" : 26,
        "status" : "B"
}
{
        "_id" : ObjectId("618904b6258a6c38daf13abf"),
        "name" : "王五",
        "sex" : "男",
        "age" : 26,
        "status" : "A",
        "groups" : [
                "news",
                "sports"
        ]
}
```

## 删除数据库
MongoDB 使用 remove() 删除集合中的文档。示例如下：
```
> db.FirstCol.remove({name:"李三",sex:"女",age:28,status:"A"})
WriteResult({ "nRemoved" : 1 })
```

查询删除结果：
```
> db.FirstCol.find().pretty()
{
        "_id" : ObjectId("618904b6258a6c38daf13abe"),
        "name" : "王六",
        "sex" : "男",
        "age" : 26,
        "status" : "B"
}
{
        "_id" : ObjectId("618904b6258a6c38daf13abf"),
        "name" : "王五",
        "sex" : "男",
        "age" : 26,
        "status" : "A",
        "groups" : [
                "news",
                "sports"
        ]
}
```

## 更多信息
更多操作方法，请参见 [MongoDB 官网文档](https://docs.mongodb.com/manual/reference/connection-string/)。
