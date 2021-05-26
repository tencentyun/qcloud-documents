
## 相关说明
云数据库 MongoDB 默认提供 rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式，对于这两种认证方式，连接 URI 需要做不同的处理，具体参见 [连接实例](https://cloud.tencent.com/document/product/240/7092)。

[Node.js MongoDB 驱动文档](https://docs.mongodb.com/ecosystem/drivers/node/)

## 快速开始
### Node.js 原生示例代码
Shell 安装驱动包：
```
npm install mongodb --save
( 如遇安装不成功可以尝试更换源，npm config set registry http://registry.cnpmjs.org )
npm init
```
程序代码：
```
'use strict';

var mongoClient = require('mongodb').MongoClient,
    assert = require('assert');

// 拼接 URI
var url = 'mongodb://mongouser:thepasswordA1@10.66.161.177:27017/admin';

mongoClient.connect(url, function(err, db) {
	assert.equal(null, err);
	var db = db.db('testdb'); // 选择一个 db
	var col = db.collection('demoCol'); // 选择一个集合(表)
   // 插入数据
    col.insertOne(
        {
            a: 1,
            something: "yy"
        },
        //可选参数
        //{
        //    w: 'majority' // 开启 “大多数”模式，保证数据写入 Secondary 节点
        //},
        function(err, r) {
            console.info("err:", err);
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

输出：

```
[root@VM_2_167_centos node]# node index.js
docs: [ { _id: 567a1bf26773935b3ff0b42a, a: 1, something: 'yy' } ]
```

## Node.js mongoose 连接示例
```
var dbUri = "mongodb://" + user + ":" + password + "@" + host + ":" + port + "/" + dbName;
var opts = {
    auth: {
        authMechanism: 'MONGODB-CR', // 如果使用 SCRAM-SHA-1 认证则不需要此参数
        authSource: 'admin'
    }
};
var connection = mongoose.createConnection(dbUri, opts);
```
