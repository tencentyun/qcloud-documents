
### 相关说明
云数据库 MongoDB 默认提供 rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式，对于这两种认证方式，连接 URI 需要做不同的处理，具体参见 [连接实例](https://cloud.tencent.com/document/product/240/7092)。

在 PHP 里，有驱动可用于连接操作 MongoDB 数据库：mongodb（[PHP 官网文档](http://php.net/manual/en/set.mongodb.php)）- MongoDB 官方推荐 mongodb 驱动，但需要 PHP 5.4 以上版本。

下面用上述驱动演示连接云数据库 MongoDB 并进行读写。

### 使用 mongodb 驱动
mongodb 安装方法参考 [官方安装步骤](http://php.net/manual/zh/mongodb.installation.php)。
**mongodb 驱动可以用 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式**，具体参见 [连接实例](https://cloud.tencent.com/doc/product/240/3563)。

示例代码：
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
$rows = $manager->executeQuery('tsdb.table1', $query); // 也可选择优先从从库读
foreach($rows as $r){
   print_r($r);
}


```
输出：
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
输出：
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
