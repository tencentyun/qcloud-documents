## 1 PHP Version

PHP MongoDB Driver Documentation:

http://cn2.php.net/manual/en/book.mongo.php

https://docs.mongodb.org/ecosystem/drivers/php/

PHP Sample Codes:

```
<?php
$connection = new MongoClient("mongodb://10.66.116.103:27017",
    array(
        "username" => "rwuser",
        "password" => "password",
        "authMechanism" => "MONGODB-CR",
    )
);
$db = $connection->tsdb;
$collection = $db->table1;

$q = array(
    'id' => 1,
    'test1' => 'xxx',
    'ss' => 'xxxxxxxx',
);

$collection->save($q);

$one = $collection->findOne();

var_dump($one);
?>
```

**Output:**


```
array(4) {
  ["_id"]=>
  object(MongoId)#7 (1) {
    ["$id"]=>
    string(24) "5673beed041ee2b1458b4567"
  }
  ["id"]=>
  int(1)
  ["test1"]=>
  string(3) "xxx"
  ["ss"]=>
  string(8) "xxxxxxxx"
}
```

## 2 Node.js Version

Node.js MongoDB Driver Documentation:

https://docs.mongodb.org/ecosystem/drivers/node-js/

Shell:

```
npm install mongodb sprintf-js --save
(In case of an unsuccessful installation, you can try to replace the source, npm config set registry http://registry.cnpmjs.org)
npm init
```

**Node.js Sample Codes:**

```
'use strict';

var mongoClient = require('mongodb').MongoClient,
    sprintf = require("sprintf-js").sprintf,
    assert = require('assert');

var username = 'rwuser',
    password = '1234567a',
    host     = '10.66.117.214',
    port     = '27017',
    dbName   = 'havefun';

// When stitching URI, note to use the authentication parameter authMechanism = MONGODB-CR
var url = sprintf('mongodb://%s:%s@%s:%d/%s?authMechanism=MONGODB-CR', username, password, host, port, dbName);
console.info("url:", url);

mongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
    console.log("Connected correctly to server");

    // After connected, select a collection (table)
    var col = db.collection('demoCol');

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

**Output:**

```
[root@VM_2_167_centos node]# node index.js 
url: mongodb://rwuser:1234567a@10.66.117.214:27017/havefun?authMechanism=MONGODB-CR
Connected correctly to server
docs: [ { _id: 567a1bf26773935b3ff0b42a, a: 1, something: 'yy' } ]
```

## 3 Java Version
Java MongoDB Driver Documentation
http://mongodb.github.io/mongo-java-driver/3.0/driver/getting-started/
Download Java Jar packet
https://oss.sonatype.org/content/repositories/releases/org/mongodb/mongo-java-driver/
Please select Version 3.0 or above to download

**Java Sample Codes: **
```
package mongodbdemo;

import org.bson.*;
import com.mongodb.*;
import com.mongodb.client.*;

public class MongodbDemo {

    public static void main(String[] args) {
        String mongoUri = "mongodb://rwuser:1234567a@10.66.122.28:27017/admin?authMechanism=MONGODB-CR";
        MongoClientURI connStr = new MongoClientURI(mongoUri);
        MongoClient mongoClient = new MongoClient(connStr);
        try {
            // Use the database named "someonedb"
            MongoDatabase database = mongoClient.getDatabase("someonedb");
            // Get the handle of the collection/table "someonetable"
            MongoCollection<Document> collection = database.getCollection("someonetable");

            // Prepare to write data
            Document doc = new Document();
            doc.append("key", "value");
            doc.append("username", "jack");
            doc.append("age", 31);

            // Write data
            collection.insertOne(doc);
            System.out.println("insert document: " + doc);

            // Read data
            BsonDocument filter = new BsonDocument();
            filter.append("username", new BsonString("username"));
            MongoCursor<Document> cursor = collection.find(filter).iterator();
            while (cursor.hasNext()) {
                System.out.println("find document: " + cursor.next());
            }

        } finally {
            //Close the connection
            mongoClient.close();
        }
    }
}
```

**Output:**

```
INFO: Opened connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017
insert document: Document{{key=value, username=jack, age=31, _id=56a6ebb565b33b771f9826dd}}
find document: Document{{_id=56a3189565b33b2e7ca150ba, key=value, username=jack, age=31}}
Jan 26, 2016 11:44:53 AM com.mongodb.diagnostics.logging.JULLogger log
INFO: Closed connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017 because the pool has been closed.
```
