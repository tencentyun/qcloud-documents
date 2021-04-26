## Description
TencentDB for MongoDB provides two usernames "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM-SHA-1" authentication respectively. The connecting URIs for the two types of authentication are formed differently. For more information, see [Connection Example](https://cloud.tencent.com/doc/product/240/3563).

Documentation for Node.js MongoDB Driver:
https://docs.mongodb.org/ecosystem/drivers/node-js/

## Quick Start
### Example of Node.js native codes
Install driver package via Shell:
```
npm install mongodb --save
( In case of an unsuccessful installation, you can replace the source,npm config set registry http://registry.cnpmjs.org )
npm init
```
The application code:
```
'use strict';

var mongoClient = require('mongodb').MongoClient,
    assert = require('assert');

// Form the URI
var url = 'mongodb://mongouser:thepasswordA1@10.66.161.177:27017/admin';

mongoClient.connect(url, function(err, db) {
	assert.equal(null, err);
	var db = db.db('testdb'); // Select a "db"
	var col = db.collection('demoCol'); // Select a collection (table)
   // Insert data
    col.insertOne(
        {
            a: 1,
            something: "yy"
        }, 
        //Optional parameters
        //{
        //    w: 'majority' // Enable the "Majority" mode to ensure that data are written to the Secondary nodes
        //}, 
        function(err, r) {
            console.info("err:", err);
            assert.equal(null, err);
            // Assert is written successfully
            assert.equal(1, r.insertedCount);
            // Query data
            col.find().toArray(function(err, docs) {
                assert.equal(null, err);
                console.info("docs:", docs);
                db.close();
            });
        }
    );
});
```

Output:

```
[root@VM_2_167_centos node]# node index.js 
docs: [ { _id: 567a1bf26773935b3ff0b42a, a: 1, something: 'yy' } ]
```

## Example of Connecting Node.js Mongoose

```
var dbUri = "mongodb://" + user + ":" + password + "@" + host + ":" + port + "/" + dbName;
var opts = {
    auth: {
        authMechanism: 'MONGODB-CR', // This parameter is not required for SCRAM-SHA-1 authentication
        authSource: 'admin'
    }
};
var connection = mongoose.createConnection(dbUri, opts);
```

