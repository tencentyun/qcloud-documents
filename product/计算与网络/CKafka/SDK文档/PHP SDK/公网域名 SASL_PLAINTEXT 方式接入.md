## 操作场景

该任务以 PHP 客户端为例，指导您使用公网 SASL_PLAINTEXT 方式接入消息队列 CKafka 并收发消息。

## 前提条件

- [安装 librdkafka](https://github.com/edenhill/librdkafka/)
- [安装 PHP 5.6 或以上版本](https://www.php.net/manual/en/install.php)
- [安装 PEAR](https://pear.php.net/manual/en/installation.getting.php)
- [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/phpkafkademo/PUBLIC_SASL)

## 操作步骤

### 步骤一：添加 Rdkafka 扩展

1. 在 [rdkafka 官方页面](http://pecl.php.net/package/rdkafka) 查找最新的 rdkafka php 扩展包版本。
   >?不同版本的包对 PHP 版本要求不同，这里仅以 4.1.2 为示例。

2. 安装 rdkafka 扩展。
   ```bash
   wget --no-check-certificate https://pecl.php.net/get/rdkafka-4.1.2.tgz
   pear install rdkafka-4.1.2.tgz
   # 安装成功会提示 "install ok" 和 "You should add "extension=rdkafka.so" to php.ini"
   # 如果安装失败，若提示could not extract the package.xml file from "rdkafka-4.1.2.tgz", 请手动解压后，把packge.xml文件复制进rdkafka目录中再执行pear install package.xml进行安装。
   # 其他错误请根据提示解决
   # 安装成功后在 php.ini 添加 extension=rdkafka.so
   # 执行 php --ini 后，Loaded Configuration File: 显示的就是 php.ini 所在位置 
   echo 'extension=rdkafka.so' >> /etc/php.ini
   ```

### 步骤二：准备配置

创建配置文件 CKafkaSetting.php。
```php
<?php
return [
    'bootstrap_servers' => 'bootstrap_servers1:port,bootstrap_servers2:port',
    'topic_name' => 'topic_name',
    'group_id' => 'php-demo',
    'ckafka_instance_id' => 'ckafka_instance_id',
    'sasl_username' => 'username',
    'sasl_password' => 'password'
];
```

| 参数               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| bootstrap_servers  | 接入网络，在控制台的实例详情页面【接入方式】模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/c5cf200a66f6dcf627d2ca6f1c747ecf.png) |
| topic_name         | Topic 名称，您可以在控制台上【topic管理】页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |
| group_id           | 消费者的组 Id，根据业务需求自定义，demo运行成功后可以在【Consumer Group】页面看到该消费者。 |
| ckafka_instance_id | 实例 ID，在 CKafka 控制台的实例详情页面的基本信息获取。<br/>![](https://main.qcloudimg.com/raw/9c417da4953669372fa4c13973096d3b.png) |
| sasl_username      | 用户名，在控制台【用户管理】页面创建用户时设置。               |
| sasl_password      | 用户密码，在控制台【用户管理】页面创建用户时设置。             |



### 步骤三：发送消息

1. 编写生产消息程序 Producer.php。
  ```php
<?php

$setting = require __DIR__ . '/CKafkaSetting.php';

$conf = new RdKafka\Conf();
// 设置入口服务，请通过控制台获取对应的服务地址。
$conf->set('bootstrap.servers', $setting['bootstrap_servers']);
// ---------- 启用 SASL 验证时需要设置 ----------
// SASL 验证机制类型默认选用 PLAIN
$conf->set('sasl.mechanism', 'PLAIN');
// 设置用户名：实例 ID + # + 【用户管理】中配置的用户名
$conf->set('sasl.username', $setting['ckafka_instance_id'] . '#' . $setting['sasl_username']);
// 设置密码：【用户管理】中配置的密码
$conf->set('sasl.password', $setting['sasl_password']);
// 在本地配置 ACL 策略。
$conf->set('security.protocol', 'SASL_PLAINTEXT');
// ---------- 启用 SASL 验证时需要设置 ----------
// Kafka producer 的 ack 有 3 种机制，分别说明如下：
// -1 或 all：Broker 在 leader 收到数据并同步给所有 ISR 中的 follower 后，才应答给 Producer 继续发送下一条（批）消息。
// 这种配置提供了最高的数据可靠性，只要有一个已同步的副本存活就不会有消息丢失。注意：这种配置不能确保所有的副本读写入该数据才返回，
// 可以配合 Topic 级别参数 min.insync.replicas 使用。
// 0：生产者不等待来自 broker 同步完成的确认，继续发送下一条（批）消息。这种配置生产性能最高，但数据可靠性最低
//（当服务器故障时可能会有数据丢失，如果 leader 已死但是 producer 不知情，则 broker 收不到消息）
// 1： 生产者在 leader 已成功收到的数据并得到确认后再发送下一条（批）消息。这种配置是在生产吞吐和数据可靠性之间的权衡
//（如果leader已死但是尚未复制，则消息可能丢失）
// 用户不显示配置时，默认值为1。用户根据自己的业务情况进行设置
$conf->set('acks', '1');
// 请求发生错误时重试次数，建议将该值设置为大于0，失败重试最大程度保证消息不丢失
$conf->set('retries', '0');
// 发送请求失败时到下一次重试请求之间的时间
$conf->set('retry.backoff.ms', 100);
// producer 网络请求的超时时间。
$conf->set('socket.timeout.ms', 6000);
$conf->set('reconnect.backoff.max.ms', 3000);

// 注册发送消息的回调
$conf->setDrMsgCb(function ($kafka, $message) {
    echo '【Producer】发送消息：message=' . var_export($message, true) . "\n";
});
// 注册发送消息错误的回调
$conf->setErrorCb(function ($kafka, $err, $reason) {
    echo "【Producer】发送消息错误：err=$err reason=$reason \n";
});

$producer = new RdKafka\Producer($conf);
// Debug 时请设置为 LOG_DEBUG
//$producer->setLogLevel(LOG_DEBUG);
$topicConf = new RdKafka\TopicConf();
$topic = $producer->newTopic($setting['topic_name'], $topicConf);
// 生产消息并发送
for ($i = 0; $i < 5; $i++) {
    // RD_KAFKA_PARTITION_UA 让 kafka 自由选择分区
    $topic->produce(RD_KAFKA_PARTITION_UA, 0, "Message $i");
    $producer->poll(0);
}

while ($producer->getOutQLen() > 0) {
    $producer->poll(50);
}

echo "【Producer】消息发送成功\n";
  ```

2. 运行 Producer.php 发送消息。
```bash
php Producer.php
```

3. 查看运行结果。
  ```bash
>【Producer】发送消息：message=RdKafka\Message::__set_state(array(
>   'err' => 0,
>   'topic_name' => 'topic_name',
>   'timestamp' => 1618800895159,
>   'partition' => 0,
>   'payload' => 'Message 0',
>   'len' => 9,
>   'key' => NULL,
>   'offset' => 0,
>   'headers' => NULL,
>))
>【Producer】发送消息：message=RdKafka\Message::__set_state(array(
>   'err' => 0,
>   'topic_name' => 'topic_name',
>   'timestamp' => 1618800895159,
>   'partition' => 0,
>   'payload' => 'Message 1',
>   'len' => 9,
>   'key' => NULL,
>   'offset' => 1,
>   'headers' => NULL,
>))

...

>【Producer】消息发送成功
  ```

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的【topic 管理】页面，选择对应的 Topic，单击【更多】>【消息查询】，查看刚刚发送的消息。
![](https://main.qcloudimg.com/raw/c18f71eecfa5f2d9ef9df19b7eb876fc.png)


### 步骤四：消费消息

1. 编写消息订阅消费程序 Consumer.php。
  ```php
<?php

$setting = require __DIR__ . '/CKafkaSetting.php';

$conf = new RdKafka\Conf();
$conf->set('group.id', $setting['group_id']);
// 设置入口服务，请通过控制台获取对应的服务地址。
$conf->set('bootstrap.servers', $setting['bootstrap_servers']);
// ---------- 启用 SASL 验证时需要设置 ----------
// SASL 验证机制类型默认选用 PLAIN
$conf->set('sasl.mechanism', 'PLAIN');
// 设置用户名：实例 ID + # + 【用户管理】中配置的用户名
$conf->set('sasl.username', $setting['ckafka_instance_id'] . '#' . $setting['sasl_username']);
// 设置密码：【用户管理】中配置的密码
$conf->set('sasl.password', $setting['sasl_password']);
// 在本地配置 ACL 策略。
$conf->set('security.protocol', 'SASL_PLAINTEXT');
// ---------- 启用 SASL 验证时需要设置 ----------
// 使用 Kafka 消费分组机制时，消费者超时时间。当 Broker 在该时间内没有收到消费者的心跳时，
// 认为该消费者故障失败，Broker 发起重新 Rebalance 过程。
$conf->set('session.timeout.ms', 10000);
// 客户端请求超时时间，如果超过这个时间没有收到应答，则请求超时失败
$conf->set('request.timeout.ms', 305000);
// 设置客户端内部重试间隔。
$conf->set('reconnect.backoff.max.ms', 3000);

$topicConf = new RdKafka\TopicConf();
#$topicConf->set('auto.commit.interval.ms', 100);
// offset重置策略，请根据业务场景酌情设置。设置不当可能导致数据消费缺失。
$topicConf->set('auto.offset.reset', 'earliest');
$conf->setDefaultTopicConf($topicConf);

$consumer = new RdKafka\KafkaConsumer($conf);
// Debug 时请设置为 LOG_DEBUG
//$consumer->setLogLevel(LOG_DEBUG);
$consumer->subscribe([$setting['topic_name']]);

$isConsuming = true;
while ($isConsuming) {
    $message = $consumer->consume(10 * 1000);
    switch ($message->err) {
        case RD_KAFKA_RESP_ERR_NO_ERROR:
            echo "【消费者】接收到消息：" . var_export($message, true) . "\n";
            break;
        case RD_KAFKA_RESP_ERR__PARTITION_EOF:
            echo "【消费者】等待信息消息中\n";
            break;
        case RD_KAFKA_RESP_ERR__TIMED_OUT:
            echo "【消费者】等待超时\n";
            $isConsuming = false;
            break;
        default:
            throw new \Exception($message->errstr(), $message->err);
            break;
    }
}
  ```


2. 运行 Consumer.php 消费消息。
```bash
php Consumer.php
```

3. 查看运行结果。
  ```bash
  >【消费者】接收到消息：RdKafka\Message::__set_state(array(
  >   'err' => 0,
  >   'topic_name' => 'topic_name',
  >   'timestamp' => 1618800895159,
  >   'partition' => 0,
  >   'payload' => 'Message 0',
  >   'len' => 9,
  >   'key' => NULL,
  >   'offset' => 0,
  >   'headers' => NULL,
  >))
  >【消费者】接收到消息：RdKafka\Message::__set_state(array(
  >   'err' => 0,
  >   'topic_name' => 'topic_name',
  >   'timestamp' => 1618800895159,
  >   'partition' => 0,
  >   'payload' => 'Message 1',
  >   'len' => 9,
  >   'key' => NULL,
  >   'offset' => 1,
  >   'headers' => NULL,
  >))
  
  ...
  ```

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的【Consumer Group】页面，选择对应的消费者组，在主题名称输入 Topic 名称，单击【查询详情】查看消费详情。
![](https://main.qcloudimg.com/raw/3020dcb5f8fd73e02949b20fef4f956f.png)
