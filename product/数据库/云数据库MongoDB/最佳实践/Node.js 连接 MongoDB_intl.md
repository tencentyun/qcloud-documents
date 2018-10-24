This example explains how to connect Node.js to MongoDB on Windows.
## Preconditions
1. [Purchase a CVM](https://buy.cloud.tencent.com/cvm) on Tencent Cloud. This document uses Windows Server 2012 R2 as an example.
2. [Purchase a MongoDB](https://buy.cloud.tencent.com/mongodb) on Tencent Cloud.
3. [Download Node.js](https://nodejs.org/en/download/) on the CVM.

## Installing the Drive
Go to the [Tencent Cloud console](https://console.cloud.tencent.com/cvm/index) and log in to the CVM you just purchased. Right-click on the **Start** button in the lower left corner, and then click the **Command Prompt** to open the cmd command line and go to the nodejs root directory.
```
cd C:\Program Files\nodejs
```
Install the driver using the npm command.
>**Note:**
>In case of an unsuccessful installation, you can replace the source, `npm config set registry http://registry.cnpmjs.org`。

```
npm install mongodb --save
```

The figure below indicates that the driver is installed successfully.
![](https://mc.qcloudimg.com/static/img/c00a020f550ffb3afe9f2f5ee38859d4/npm.png)

## Connection Example
Create a test.js file in the nodejs root directory. Save the code below:
```
'use strict';

var mongoClient = require('mongodb').MongoClient,
    assert = require('assert');

// Form the URI
var url = 'mongodb://Mongouser:[Password]@[Private network address]:27017/admin';

mongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
    var db = db.db('local'); // Select a "db"
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
Enter `node test.js` in the Command Prompt. The output result below indicates that Node.js is successfully connected to MongoDB.
![](https://mc.qcloudimg.com/static/img/18779d11d3619f1fcbc7bcd8cf253fb5/image.png)

This is just a connection example. You can write code to deploy your application as needed later on.

## Description
TencentDB for MongoDB provides two usernames "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM-SHA-1" authentication respectively. The connecting URLs for the two types of authentication are formed differently. For more information, see [Connection Example](https://cloud.tencent.com/document/product/240/3563).

