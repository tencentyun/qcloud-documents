Python 驱动下载 [pymongo](https://pypi.python.org/pypi/pymongo/)

Python 示例代码1:

```
#!/usr/bin/python
import pymongo
import random

mongodbUri = 'mongodb://rwuser:********@10.66.180.13:27017?authMechanism=MONGODB-CR&authSource=admin'
//或者 mongodbUri = 'mongodb://rwuser:********@10.66.180.13:27017/admin?authMechanism=MONGODB-CR'


client = pymongo.MongoClient(mongodbUri)
db = client.someonedb

#db = client.tage
db.authenticate("someonedb","test")
db.user.drop()
db.user.save({'id':1,'name':'kaka','sex':'male'})

for id in range(2,10):
    name = random.choice(['R9','cat','owen','lee','J'])
    sex = random.choice(['male','female'])
    db.user.insert({'id':id,'name':name,'sex':sex})
content = db.user.find()

for i in content:
    print i
```

Python 示例代码2:

```
#!/usr/bin/python
import pymongo
mongodbUri = 'mongodb://rwuser:********@10.66.122.28:27017/admin?authMechanism=MONGODB-CR&authSource=admin'
client = pymongo.MongoClient(mongodbUri)
db = client.someonedb

inserted_id = db.somecoll.insert_one({"somekey":"yiqihapi"}).inserted_id
print inserted_id

for doc in db.somecoll.find(dict(_id=inserted_id)):
        print doc

for doc in db.somecoll.find({"somekey":"yiqihapi"}):
        print doc
```

**输出：**


```
5734431e101e2f6d699b37ef
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
```
