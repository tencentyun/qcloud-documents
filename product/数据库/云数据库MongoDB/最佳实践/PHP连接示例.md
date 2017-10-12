### 相关说明
腾讯云MongoDB默认提供了“rwuser”和“mongouser”两个用户名分别支持“MONGODB-CR”和“SCRAM-SHA-1”两种认证方式，对于这两种认证方式，连接URI需要做不同的处理，具体参见[连接示例](https://cloud.tencent.com/doc/product/240/3563)一文。

在PHP里，有[两套驱动](https://docs.mongodb.com/ecosystem/drivers/php/)可用于连接操作MongoDB数据库，它们分别是：
- mongodb([PHP官网文档](http://php.net/manual/en/set.mongodb.php))  - MongoDB官方推荐mongodb驱动，但需要PHP 5.4及以上版本。
- mongo([PHP官网文档](http://php.net/manual/en/book.mongo.php)) - mongo比较老旧，但也可以用，如果要用请选择1.6版本。

下面分别用上述两个驱动演示一下连接腾讯云MongoDB并进行读写。
 
### 使用mongodb驱动
mongodb安装方法参考[这里](http://php.net/manual/zh/mongodb.installation.php)。
**mongodb驱动可以用“MONGODB-CR”和“SCRAM-SHA-1”两种认证方式**，具体参见[连接示例](https://cloud.tencent.com/doc/product/240/3563)。

示例代码:
```
<?php
// 拼接连接URI
$uri = 'mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin';
$manager = new MongoDB\Driver\Manager($uri);

// 准备写入数据
$document1 = [
    'username' => 'lily',
    'age'      => 34,
    'email'    => 'lily@qq.com'
];

// 驱动预处理数据，这里可以看到MongoDB的_id是驱动生成的
$bulk = new MongoDB\Driver\BulkWrite;
$_id1 = $bulk->insert($document1);

$result = $manager->executeBulkWrite('tsdb.table1', $bulk);

// 或者根据实际需要使用下面的代码确保数据写入到大多数节点
// $writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);
// $result = $manager->executeBulkWrite('testdb.testcollection', $bulk, $writeConcern);

// 查询
$filter = ['_id' => $_id1];
$query = new MongoDB\Driver\Query($filter);
$rows = $manager->executeQuery('tsdb.table1', $query); // 也可以选择优先从从库读哦，具体请参阅文档
foreach($rows as $r){
   print_r($r);
}


```
**输出：**
```
stdClass Object
(
    [_id] => MongoDB\BSON\ObjectID Object
        (
            [oid] => 582c001618c90a16363abc31
        )

    [username] => lily
    [age] => 34
    [email] => lily@qq.com
)
```


### 使用mongo驱动
**mongo驱动只支持“MONGODB-CR”认证**，对应的只能用“rwuser”进行连接，具体参见[连接示例](https://cloud.tencent.com/doc/product/240/3563)。

示例代码:

```
<?php
// 推荐使用URI的方式连接，两种URI任选其一
$uri = "mongodb://rwuser:thepasswordA1@10.66.187.127:27017/admin?authMechanism=MONGODB-CR";
$uri = "mongodb://rwuser:thepasswordA1@10.66.187.127:27017/?authMechanism=MONGODB-CR&authSource=admin";
$connection = new MongoClient($uri);

/*
// 或者这样也可以
$connection = new MongoClient("mongodb://10.66.116.103:27017/admin",
    array(
        "username" => "rwuser",
        "password" => "password",
        "authMechanism" => "MONGODB-CR"
    )
);
*/
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
```

### 推荐使用PHPLIB库（基于mongodb驱动封装）
使用mongodb驱动推荐搭配[PHPLIB](http://php.net/manual/zh/mongodb.tutorial.library.php)使用，[查看相关文档](http://mongodb.github.io/mongo-php-library/tutorial/crud/)。
PHPLIB的安装方法参考[这里](http://mongodb.github.io/mongo-php-library/getting-started/)，请注意PHPLIB依赖与mongodb驱动。

示例代码:
```
<?php
require_once __DIR__ . "/vendor/autoload.php";

// 初始化
$mongoClient = new MongoDB\Client('mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin');

// 使用demo库下的users集合
$collection = $mongoClient->demo->users;

// 写入一条数据
$insertOneResult = $collection->insertOne(['name' => 'gomez']);

printf("Inserted %d document(s)\n", $insertOneResult->getInsertedCount());
var_dump($insertOneResult->getInsertedId());

// 查询数据
$document = $collection->findOne(['name' => 'gomez']);

var_dump($document);

```
输出
```
Inserted 1 document(s)
object(MongoDB\BSON\ObjectID)#11 (1) {
  ["oid"]=>
  string(24) "57e3bf20bf605714a53e69c1"
}
object(MongoDB\Model\BSONDocument)#16 (1) {
  ["storage":"ArrayObject":private]=>
  array(2) {
    ["_id"]=>
    object(MongoDB\BSON\ObjectID)#14 (1) {
      ["oid"]=>
      string(24) "57e3bf20bf605714a53e69c1"
    }
    ["name"]=>
    string(5) "gomez"
  }
}

```
