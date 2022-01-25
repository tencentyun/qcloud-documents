## 操作步骤

本文以 PHP SDK 为例介绍客户端接入 TDMQ CMQ 版服务并收发消息的操作步骤。

## 前提条件

- [安装 PHP 5.6 或以上版本](https://www.php.net/manual/en/install.php)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-php-sdk-demo.zip)

## 一、队列模型
1. 在控制台创建符合需求的队列服务，参见 [创建队列服务](https://cloud.tencent.com/document/product/1496/61015)。
   > ? 目前创建消息队列可以在控制台，或者通过云 API 方式来创建，使用云API 需要安装相关 SDK，SDK 安装可参见 [PHP SDK 3.0安装使用](https://cloud.tencent.com/document/sdk/PHP)。
2. 添加依赖。
<dx-codeblock>
:::  shell
composer require tencentcloud/tencentcloud-sdk-php
:::
</dx-codeblock>
3. 添加引用。
<dx-codeblock>
:::  php
require '/path/to/vendor/autoload.php';
:::
</dx-codeblock>
4. 创建消息队列。
<dx-codeblock>
:::  php
   $cred = new Credential($secretId, $secretKey);
   $httpProfile = new HttpProfile();
   $httpProfile->setEndpoint($endPoint);
   
   $clientProfile = new ClientProfile();
   $clientProfile->setHttpProfile($httpProfile);
   $client = new TdmqClient($cred, "ap-guangzhou", $clientProfile);
   
   $req = new CreateCmqQueueRequest();
   
   $params = array(
       "QueueName" => "queue_api",  // 消息队列名称
       // 以下是死信队列相关配置
       "DeadLetterQueueName" => "dead_queue_api", // 死信队列名称
       "Policy" => 0,  // 死信策略。0为消息被多次消费未删除，1为Time-To-Live过期
       "MaxReceiveCount" => 3  // 最大接收次数 1-1000
       // MaxTimeToLive  policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds
   );
   $req->fromJsonString(json_encode($params));
   
   $resp = $client->CreateCmqQueue($req);
:::
</dx-codeblock>
<table>
    <thead>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>$endPoint</td>
        <td>API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt;
            <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png"
                                             referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td>$secretId、$secretKey</td>
        <td>云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt;
            <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png"
                                              referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    </tbody>
</table>
5. 在项目中引入 [CMQ 相关文件](https://github.com/tencentyun/cmq-php-sdk)。
6. 发送消息。
<dx-codeblock>
:::  php
// 消息队列名称
$queue_name = "php_queue";
// 认证信息
$my_account = new Account($this->endpoint, $this->secretId, $this->secretKey);

$my_queue = $my_account->get_queue($queue_name);

$queue_meta = new QueueMeta();
$queue_meta->queueName = $queue_name;
$queue_meta->pollingWaitSeconds = 10;
$queue_meta->visibilityTimeout = 10;
$queue_meta->maxMsgSize = 1024;
$queue_meta->msgRetentionSeconds = 3600;

try {
    // 消息内容
    $msg_body = "I am test message.";
    $msg = new Message($msg_body);
    // 发送消息
    $re_msg = $my_queue->send_message($msg);
    echo "Send Message Succeed! MessageBody:" . $msg_body . " MessageID:" . $re_msg->msgId . "\n";
} catch (CMQExceptionBase $e) {
    echo "Create Queue Fail! Exception: " . $e;
    return;
}
:::
</dx-codeblock>
<table>
<thead>
<tr><th >参数</th><th >说明</th></tr></thead>
<tbody><tr><td >endpoint</td><td >API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt; <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >secretId、secretKey</td><td >云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt; <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td style='text-align:left;' >$queue_name</td><td style='text-align:left;' >队列名称，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong>列表页面获取。</td></tr></tbody>
</table>
7. 消费消息。
<dx-codeblock>
:::  php
// 消息队列名称
$queue_name = "php_queue";
// 认证结果
$my_account = new Account($this->endpoint, $this->secretId, $this->secretKey);

$my_queue = $my_account->get_queue($queue_name);

$queue_meta = new QueueMeta();
$queue_meta->queueName = $queue_name;
$queue_meta->pollingWaitSeconds = 10;
$queue_meta->visibilityTimeout = 10;
$queue_meta->maxMsgSize = 1024;
$queue_meta->msgRetentionSeconds = 3600;

try {
    // 获取消息
    $recv_msg = $my_queue->receive_message(3);
    echo "Receive Message Succeed! " . $recv_msg . "\n";
    // 消费成功，删除消息
    $my_queue->delete_message($recv_msg->receiptHandle);
} catch (CMQExceptionBase $e) {
    echo "Create Queue Fail! Exception: " . $e;
    return;
}
:::
</dx-codeblock>
<table>
<thead>
<tr><th >参数</th><th >说明</th></tr></thead>
<tbody><tr><td >endpoint</td><td >API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt; <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >secretId、secretKey</td><td >云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt; <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >$queue_name</td><td >队列名称，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong>列表页面获取。</td></tr></tbody>
</table>

## 二、主题模型

1. 准备所需资源，创建主题订阅和订阅者。
   1. 创建主题订阅，创建主题订阅可通过控制台，或云 API 进行创建，使用云 API 需要安装相关 SDK，SDK 安装可参见 [PHP SDK 3.0安装使用](https://cloud.tencent.com/document/sdk/PHP)。
<dx-codeblock>
:::  php
      $cred = new Credential($secretId, $secretKey);
      $httpProfile = new HttpProfile();
      $httpProfile->setEndpoint($endPoint);
      
      $clientProfile = new ClientProfile();
      $clientProfile->setHttpProfile($httpProfile);
      $client = new TdmqClient($cred, "ap-guangzhou", $clientProfile);
      
      $req = new CreateCmqTopicRequest();
      
      $params = array(
          "TopicName" => "topic_api1", // 主题名字，在单个地域同一帐号下唯一
          "FilterType" => 2, // 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略
          "MsgRetentionSeconds" => 86400 // 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天）
      );
      $req->fromJsonString(json_encode($params));
      
      // 创建topic
      $resp = $client->CreateCmqTopic($req);
:::
</dx-codeblock>
<table>
<thead>
<tr><th >参数</th><th >说明</th></tr></thead>
<tbody><tr><td >$endPoint</td><td >API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt; <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >$secretId、$secretKey</td><td >云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt; <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png" referrerpolicy="no-referrer" alt="img"></td></tr></tbody>
</table>
   2. 创建订阅者，创建订阅者可通过控制台，或云 API 进行创建，使用云 API 需要安装相关 SDK，SDK 安装可参见 [PHP SDK 3.0安装使用](https://cloud.tencent.com/document/sdk/PHP)。
<dx-codeblock>
:::  php
      $cred = new Credential($secretId, $secretKey);
      $httpProfile = new HttpProfile();
      $httpProfile->setEndpoint($endPoint);
      
      $clientProfile = new ClientProfile();
      $clientProfile->setHttpProfile($httpProfile);
      $client = new TdmqClient($cred, "ap-guangzhou", $clientProfile);
      
      $req = new CreateCmqSubscribeRequest();
      
      $params = array(
          // 创建订阅的topic名称
          "TopicName" => "topic_api1",
          // 订阅名称
          "SubscriptionName" => "sub1",
          // 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。
          "Protocol" => "queue",
          // 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“http://”开头，host可以是域名或IP；对于Queue，则填QueueName。
          "Endpoint" => "topic_queue_api",
          // CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。
          "NotifyStrategy" => "BACKOFF_RETRY",
          // BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略
          "BindingKey" => array("a.b"),
          // 消息标签（用于消息过滤)。标签数量不能超过5个
          // "FilterTag" => array("TAG"),
          // 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。
          "NotifyContentFormat" => "SIMPLIFIED"
      );
      $req->fromJsonString(json_encode($params));
      
      // 创建订阅
      $resp = $client->CreateCmqSubscribe($req);
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
BindingKey 与 FilterTag 要根据所订阅 Topic 类型进行设置，否则无效。
</dx-alert>
<table>
<thead>
<tr><th >参数</th><th >说明</th></tr></thead>
<tbody><tr><td >$endPoint</td><td >API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt; <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >$secretId、$secretKey</td><td >云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt; <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png" referrerpolicy="no-referrer" alt="img"></td></tr></tbody>
</table>
2. 在项目中引入 [CMQ 文件](https://github.com/tencentyun/cmq-php-sdk)。
3. 创建 my_topic，用来发布消息。
<dx-codeblock>
:::  php
   // 主题订阅名称
   $topic_name = "php_topic_tag";
   // 认证信息
   $my_account = new Account($this->endpoint, $this->secretId, $this->secretKey);
   $my_topic = $my_account->get_topic($topic_name);
:::
</dx-codeblock>
<table>
<thead>
<tr><th >参数</th><th >说明</th></tr></thead>
<tbody><tr><td >endpoint</td><td >API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt; <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >secretId、secretKey</td><td >云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt; <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png" referrerpolicy="no-referrer" alt="img"></td></tr><tr><td >$topic_name</td><td >主题订阅名称，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>主题订阅</strong>列表页面获取。</td></tr></tbody>
</table>
4. 发送 TAG 类型消息。
<dx-codeblock>
:::  php
   // 发送tag消息
   $msg = "this is a test message for tag.";
   $msgid = $my_topic->publish_message($msg, array("TAG","TAG1"));
:::
</dx-codeblock>
5. 发送 route 消息。
<dx-codeblock>
:::  php
   // 发送route消息
   $msg = "this is a test message for route.";
   $msgid = $my_topic->publish_message($msg, array(), "a.b.c");
:::
</dx-codeblock>
6. 消费者消费订阅者订阅的消息队列即可。

>?以上是 CMQ 两种模型下的生产和消费方式的简单介绍，更多使用可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-php-sdk-demo.zip) 或 [CMQ 代码仓库](https://github.com/tencentyun/cmq-php-sdk)。
