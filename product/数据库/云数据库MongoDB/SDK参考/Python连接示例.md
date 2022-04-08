
## 相关说明
云数据库 MongoDB 默认提供 rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式，对于这两种认证方式，连接 URI 需要做不同的处理，具体参见 [连接实例](https://cloud.tencent.com/document/product/240/7092)。

[Python 驱动下载](https://pypi.python.org/pypi/pymongo/) 

## 快速开始
### Python 示例代码 1
```
#!/usr/bin/python
import pymongo
import random

mongodbUri = 'mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin'

client = pymongo.MongoClient(mongodbUri)
db = client.somedb
db.user.drop()
element_num=10
for id in range(element_num):
    name = random.choice(['R9','cat','owen','lee','J'])
    sex = random.choice(['male','female'])
    db.user.insert_one({'id':id, 'name':name, 'sex':sex})

content = db.user.find()
for i in content:
    print i

```

###  Python 示例代码 2
```
#!/usr/bin/python
import pymongo
mongodbUri = 'mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin'
client = pymongo.MongoClient(mongodbUri)
db = client.someonedb

inserted_id = db.somecoll.insert_one({"somekey":"yiqihapi"}).inserted_id
print inserted_id

for doc in db.somecoll.find(dict(_id=inserted_id)):
        print doc

for doc in db.somecoll.find({"somekey":"yiqihapi"}):
        print doc
```

输出：
```
5734431e101e2f6d699b37ef
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
```
