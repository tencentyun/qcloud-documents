## 操作场景

本文以调用 PHP SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [安装 PHP 5.6 或以上版本](https://www.php.net/manual/en/install.php)
- [安装 PEAR](https://pear.php.net/manual/en/installation.getting.php)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-php-sdk-demo.zip)

## 操作步骤

### 步骤1：安装 php-amqplib 库

根据 RabbitMQ 官网推荐使用 php-amqplib Client，首先需要在项目中引入 php-amqplib 库。

1. 在项目中添加 `composer.json` 文件。
   ```json
   {
       "require": {
           "php-amqplib/php-amqplib": ">=3.0"
       }
   }
   ```

2. 使用 Composer 进行安装。
   ```shell
   composer.phar install
   ```

   或者使用下述命令：
   ```shell
   composer install
   ```

3. 创建客户端需要引入库文件，在客户端文件中引入库文件。
   ```php
   require_once('../vendor/autoload.php');
   ```

   完成上述步骤即可创建连接与服务端进行交互。


### 步骤2：发送消息

创建并编译生产消息程序（以 direct 类型交换机为例）。

```php
require_once('../vendor/autoload.php');

use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$exchange_name = 'exchange_name';
$exchange_type = 'direct';

// 创建连接
$connection = new AMQPStreamConnection(
    $host,
    $port,
    $username,
    $password,
    $vhost,
    false,
    'PLAIN');
// 建立通道
$channel = $connection->channel();
// 声明交换机
$channel->exchange_declare($exchange_name, $exchange_type, false, true, false);

// 设定消息路由key
$routing_keys = array('info', 'waring', 'error');

for ($x = 0; $x < count($routing_keys); $x++) {
    // 消息内容
    $msg = new AMQPMessage('This is a direct[' . $routing_keys[$x] . '] message!');
    // 发送消息到指定的交换机并设置routing key
    $channel->basic_publish($msg, $exchange_name, $routing_keys[$x]);

    echo " [Producer(Routing)] Sent '" . $msg->body . "'\n";
}
// 资源释放
$channel->close();
$connection->close();
```

| 参数              | 说明                                                         |
| :---------------- | :----------------------------------------------------------- |
| $exchange_name    | Exchange 名称，在控制台 Exchange 列表获取。                  |
| $exchange_type    | 类型需与上述 Exchange 的类型保持一致。                         |
| $host             | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| $port             | 集群接入地址中的端口号。                                     |
| $username         | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| $password         | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| $vhost            | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| $routing_keys[$x] | 消费者消息队列绑定的 routing key，消息的路由规则，在控制台绑定关系列表的**绑定 Key**列获取。![img](https://main.qcloudimg.com/raw/66d31e7d7ec8519843a8fc67bff87265.png) |

### 步骤3：消费消息

创建并编译消费消息程序。

```php
<?php

require_once('../vendor/autoload.php');
require_once('../Constant.php');

use PhpAmqpLib\Connection\AMQPStreamConnection;

$exchange_name = 'exchange_name';
$exchange_type = 'direct';
$queue_name = 'route_queue1';

// 创建链接
$connection = new AMQPStreamConnection(
    $host,
    $port,
    $username,
    $password,
    $vhost,
    false,
    'PLAIN');
// 建立通道
$channel = $connection->channel();
// 声明交换机
$channel->exchange_declare($exchange_name, $exchange_type, false, true, false);
// 声明消息队列
$channel->queue_declare($queue_name, false, true, false, false);

// 设定队列路由key
$routing_keys = array('info', 'waring', 'error');
for ($x = 0; $x < count($routing_keys); $x++) {
    // 绑定消息队列到指定交换机并设置routingKey
    $channel->queue_bind($queue_name, $exchange_name, $routing_keys[$x]);
}

echo " [Consumer1(Routing: info/waring/error)] Waiting for messages. To exit press CTRL+C\n";

// 消息回调（消息消费逻辑）
$callback = function ($msg) {
    echo ' [Consumer1(Routing: info/waring/error)] Received ', $msg->body, "\n";
};
// 创建消费者监听指定消息队列
$channel->basic_consume($queue_name, '', false, true, false, false, $callback);

while ($channel->is_open()) {
    $channel->wait();
}
// 关闭资源
$channel->close();
$connection->close();

```

| 参数              | 说明                                                         |
| :---------------- | :----------------------------------------------------------- |
| $exchange_name    | Exchange 名称，可在控制台 Exchange 列表获取。                |
| $exchange_type    | 类型需与上述exchange的类型保持一致。                         |
| $queue_name       | Queue名称，可在控制台 Queue 列表获取。                       |
| $host             | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| $port             | 集群接入地址中的端口号。                                     |
| $username         | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| $password         | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| $vhost            | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| $routing_keys[$x] | 消息队列支持的routing key。消费者消息队列绑定的 routing key，消息的路由规则，在控制台绑定关系列表的**绑定 Key**列获取。![img](https://main.qcloudimg.com/raw/66d31e7d7ec8519843a8fc67bff87265.png) |



### 步骤4：查看消息

如果您想确认消息是否成功发送至 TDMQ RabbitMQ 版，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面查看接入的消费者情况。

![img](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)



完整示例或其他使用可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-php-sdk-demo.zip) 或者 [RabbitMQ 官方使用文档](https://www.rabbitmq.com/getstarted.html)。

