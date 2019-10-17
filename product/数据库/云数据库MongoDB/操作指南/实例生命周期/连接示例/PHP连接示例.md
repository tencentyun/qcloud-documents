### 相关说明
腾讯云 MongoDB 默认提供了 “rwuser” 和 “mongouser” 两个用户名分别支持 “MONGODB-CR” 和 “SCRAM-SHA-1” 两种认证方式，对于这两种认证方式，连接 URI 需要做不同的处理，具体参见 [连接示例](https://cloud.tencent.com/doc/product/240/3563) 文档。

在 PHP 里，有 [两套驱动](https://docs.mongodb.com/ecosystem/drivers/php/) 可用于连接操作 MongoDB 数据库，它们分别是：
- mongodb ([PHP官网文档](http://php.net/manual/en/set.mongodb.php))  - MongoDB 官方推荐 mongodb 驱动，但需要 PHP 5.4 以上版本。
- mongo ([PHP官网文档](http://php.net/manual/en/book.mongo.php)) - mongo 比较老旧，但也可以用，如果要用请选择 1.6 版本。

下面分别用上述两个驱动演示连接腾讯云 MongoDB 并进行读写。

### 使用 mongodb 驱动
mongodb 安装方法参考 [官方安装步骤](http://php.net/manual/zh/mongodb.installation.php)。
**mongodb 驱动可以用 “MONGODB-CR” 和 “SCRAM-SHA-1” 两种认证方式**，具体参见 [连接示例](https://cloud.tencent.com/doc/product/240/3563)。

示例代码:
```
<?php
// 拼接连接 URI
$uri = 'mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin';
$manager = new MongoDB\Driver\Manager($uri);

// 准备写入数据
$document1 = [
    'username' => 'lily',
    'age'      => 34,
    'email'    => 'lily@qq.com'
];

// 驱动预处理数据，这里可以看到 MongoDB 的 _id 是驱动生成的
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


### 使用 mongo 驱动
**mongo 驱动只支持 “MONGODB-CR” 认证**，对应的只能用 “rwuser” 进行连接，具体参见 [连接示例](https://cloud.tencent.com/doc/product/240/3563)。

示例代码:

```
<?php
// 推荐使用 URI 的方式连接，两种 URI 任选其一
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

### 推荐使用 PHPLIB 库（基于 mongodb 驱动封装）
使用 mongodb 驱动推荐搭配 [PHPLIB](http://php.net/manual/zh/mongodb.tutorial.library.php) 使用，[查看相关文档](http://mongodb.github.io/mongo-php-library/tutorial/crud/)。
PHPLIB 的安装方法参考 [官方安装步骤](http://mongodb.github.io/mongo-php-library/getting-started/)，请注意 PHPLIB 依赖与 mongodb 驱动。

示例代码:
```
<?php
require_once __DIR__ . "/vendor/autoload.php";

// 初始化
$mongoClient = new MongoDB\Client('mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin');

// 使用 demo 库下的 users 集合
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
