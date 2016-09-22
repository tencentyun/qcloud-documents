## 相关帮助
在PHP里，有[两套驱动](https://docs.mongodb.com/ecosystem/drivers/php/)可用于连接操作MongoDB数据库，它们分别是：
mongodb([PHP官网文档](http://php.net/manual/en/set.mongodb.php)) 和 mongo([PHP官网文档](http://php.net/manual/en/book.mongo.php))
推荐mongodb，但需要PHP 5.4及以上版本，使用mongodb驱动推荐搭配[PHPLIB](http://php.net/manual/zh/mongodb.tutorial.library.php)使用，[查看相关文档](http://mongodb.github.io/mongo-php-library/tutorial/crud/)；
mongo比较老旧，但也可以用，如果要用请选择1.6版本。
下面我们分别用上述两个驱动演示一下连接腾讯云MongoDB并进行读写：

## 使用mongodb驱动-原生API示例
mongodb安装方法参考[这里](http://php.net/manual/zh/mongodb.installation.php)
示例代码:
```
<?php
// 建立连接
$manager = new MongoDB\Driver\Manager(
    'mongodb://rwuser:********@10.66.122.28:27017/admin?authMechanism=MONGODB-CR'
    // 或者 'mongodb://rwuser:********@10.66.122.28:27017?authMechanism=MONGODB-CR&authSource=admin'
);

// 准备写入数据
$document1 = [ 
    'username' => 'lily',
    'age'      => 34, 
    'email'    => 'lily#qq.com'
];

// 驱动处理数据，这里可以看到MongoDB的_id是驱动生成的
$bulk = new MongoDB\Driver\BulkWrite;
$_id1 = $bulk->insert($document1);

// 打印_id查看
print_r($_id1);

$result = $manager->executeBulkWrite('testdb.testcollection', $bulk);

// 或者使用下面的方法确保数据写入到大多数节点
// $writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);
// $result = $manager->executeBulkWrite('testdb.testcollection', $bulk, $writeConcern);

// 查询
$filter = ['username' => 'lily'];
$query = new MongoDB\Driver\Query($filter);
$rows = $manager->executeQuery('testdb.testcollection', $query);
// 也可以选择优先从从库读哦，具体请参阅文档MongoDB\Driver\Query的选项部分（很强大）
foreach($rows as $r){
   print_r($r);
}

```
**输出：**
```
MongoDB\BSON\ObjectID Object
(
    [oid] => 577a4075101e2f36fc4b2831
)
stdClass Object
(
    [_id] => MongoDB\BSON\ObjectID Object
        (
            [oid] => 577a4075101e2f36fc4b2831
        )

    [username] => lily
    [age] => 34
    [email] => lily@qq.com
)
```
## 使用mongodb驱动-PHPLIB连接示例（推荐）
PHPLIB的安装方法参考[这里](http://mongodb.github.io/mongo-php-library/getting-started/)，请注意PHPLIB依赖与mongodb驱动。
示例代码:
```
<?php
require_once __DIR__ . "/vendor/autoload.php";

// 初始化
$mongoClient = new MongoDB\Client('mongodb://rwuser:********@10.66.155.29:27017/admin');

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

## 使用mongo驱动连接示例

示例代码:

```
<?php
// 推荐使用URI的方式连接
$connection = new MongoClient("mongodb://rwuser:********@10.66.122.28:27017/admin?authMechanism=MONGODB-CR");
// 或者 $connection = new MongoClient("mongodb://rwuser:********@10.66.122.28:27017?authMechanism=MONGODB-CR&authSource=admin");
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
?>
```

**输出：** 


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