## 相关帮助
Node.js MongoDB驱动文档:
https://docs.mongodb.org/ecosystem/drivers/node-js/

Shell:
```
npm install mongodb sprintf-js --save
( 如遇安装不成功可以尝试更换源，npm config set registry http://registry.cnpmjs.org )
npm init
```

## Node.js 原生 示例代码

```
'use strict';

var mongoClient = require('mongodb').MongoClient,
    sprintf = require("sprintf-js").sprintf,
    assert = require('assert');

var username = 'rwuser',
    password = '********',
    host     = '10.66.117.214',
    port     = '27017',
    dbName   = 'havefun';

// 拼接URI， 注意需要使用鉴权参数 authMechanism=MONGODB-CR
var url = sprintf('mongodb://%s:%s@%s:%d/%s?authMechanism=MONGODB-CR&authSource=admin', username, password, host, port, dbName);
// 或者 mongodb://%s:%s@%s:%d/admin?authMechanism=MONGODB-CR
console.info("url:", url);

mongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
    console.log("Connected correctly to server");

    // 连接成功，选择一个集合(表)
    var col = db.collection('demoCol');

    // 插入数据
    col.insertOne(
        {
            a: 1,
            something: "yy"
        }, 
        //可选参数
        //{
        //    w: 'majority' // 开启 “大多数”模式，保证数据写入Secondary节点
        //}, 
        function(err, r) {
            assert.equal(null, err);
            // 断言写入成功
            assert.equal(1, r.insertedCount);
    
            // 查询数据
            col.find().toArray(function(err, docs) {
                assert.equal(null, err);
                console.info("docs:", docs);
                db.close();
            });   

        }
    );

});
```

**输出:**

```
[root@VM_2_167_centos node]# node index.js 
url: mongodb://rwuser:1234567a@10.66.117.214:27017/havefun?authMechanism=MONGODB-CR&authSource=admin
Connected correctly to server
docs: [ { _id: 567a1bf26773935b3ff0b42a, a: 1, something: 'yy' } ]
```

## Node.js mongoose 连接示例

```
var dbUri = "mongodb://" + user + ":" + password + "@" + host + ":" + port + "/" + dbName;
var opts = {
    auth: {
        authMechanism: 'MONGODB-CR',
        authSource: 'admin'
    }
};
var connection = mongoose.createConnection(dbUri, opts);
```