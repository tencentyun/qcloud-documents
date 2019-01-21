## Description
TencentDB for MongoDB provides two usernames "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM-SHA-1" authentication respectively. The connecting URIs for the two types of authentication are formed differently. For more information, see [Connection Example](https://cloud.tencent.com/doc/product/240/3563).

Download the Python driver [pymongo](https://pypi.python.org/pypi/pymongo/)

## Quick Start

### Python example code 1

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

### Python example code 2

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

Output:


```
5734431e101e2f6d699b37ef
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
{u'somekey': u'yiqihapi', u'_id': ObjectId('5734431e101e2f6d699b37ef')}
```

