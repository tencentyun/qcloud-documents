## 操作场景

本文以 Java SDK 为例介绍客户端接入 TDMQ CMQ 版服务并收发消息的操作步骤。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-Java-sdk-demo.zip)

## 一、队列模型

1. 在控制台创建符合需求的队列服务，参见 [创建队列服务](https://cloud.tencent.com/document/product/1496/61015)。
2. 引入 CMQ 客户端相关依赖。
<dx-codeblock>
:::  xml
   <dependency>
       <groupId>com.qcloud</groupId>
       <artifactId>cmq-tcp-client</artifactId>
       <version>1.1.7</version>
   </dependency>
:::
</dx-codeblock>
3. 发送消息。
<dx-codeblock>
:::  java
   Producer producer = new Producer();
   // 设置 Name Server地址。必须设置 不同地域不同网络不同
   producer.setNameServerAddress(NameServerAddress);
   // 设置SecretId，在控制台上获取，必须设置
   producer.setSecretId(SecretId);
   // 设置SecretKey，在控制台上获取，必须设置
   producer.setSecretKey(SecretKey);
   // 设置签名方式，可以不设置，默认为SHA1
   producer.setSignMethod(ClientConfig.SIGN_METHOD_SHA256);
   // 设置发送消息失败时，重试的次数，设置为0表示不重试，默认为2
   producer.setRetryTimesWhenSendFailed(3);
   // 设置请求超时时间， 默认3000ms
   producer.setRequestTimeoutMS(3000);
   // 消息发往的队列，在控制台创建
   String queue = "queue1";
   try {
       // 启动对象前必须设置好相关参数
       producer.start();
       final String msg = "this is a cmq message.";
       // 同步单条发送消息
       SendResult result = producer.send(queue, msg);
       if (result.getReturnCode() == ResponseCode.SUCCESS) {
           // 发送成功
           System.out.println("==> send success! msg_id:" + result.getMsgId() + " request_id:" + result.getRequestId());
       } else {
           // 发送失败
           System.out.println("==> code:" + result.getReturnCode() + " error:" + result.getErrorMsg());
       }
   } catch (MQClientException | MQServerException e) {
       e.printStackTrace();
   }
   try {
       Thread.sleep(5000);
       producer.shutdown();
   } catch (InterruptedException e) {
       e.printStackTrace();
   }
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
        <td>NameServerAddress</td>
        <td>API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt;
            <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png"
                                             referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td>SecretId、SecretKey</td>
        <td>云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt;
            <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png"
                                              referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>queue</td>
        <td style='text-align:left;'>队列名称，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong>列表页面获取。
        </td>
    </tr>
    </tbody>
</table>
4. 消费消息。
<dx-codeblock>
:::  java
   final Consumer consumer = new Consumer();
   // 设置 Name Server地址。必须设置 不同地域不同网络不同
   consumer.setNameServerAddress("https://cmq-gz.public.tencenttdmq.com");
   // 设置SecretId，在控制台上获取，必须设置
   consumer.setSecretId("AKIDSiiRt87oENPEm33nGTP5UcU5QUHo55oH");
   // 设置SecretKey，在控制台上获取，必须设置
   consumer.setSecretKey("GGzSeaM5cttb2D7k6B0Yppb6LIzPYQ2O");
   // 设置签名方式，可以不设置，默认为SHA1
   consumer.setSignMethod(ClientConfig.SIGN_METHOD_SHA256);
   // 批量拉取时最大拉取消息数量，范围为1-16
   consumer.setBatchPullNumber(16);
   // 设置没有消息时等待时间，默认10s。可在consumer.receiveMsg等方法中传入具体的等待时间
   consumer.setPollingWaitSeconds(6);
   // 设置请求超时时间， 默认3000ms
   // 如果设置了没有消息时等待时间为6s，超时时间为5000ms，则最终超时时间为(6*1000+5000)ms
   consumer.setRequestTimeoutMS(5000);
   // 消息拉取的队列名称
   final String queue = "queue1";
   consumer.start();
   
   // 使用监听者获取消息，不用每次都调用receive方法了
   consumer.subscribe(queue, new MessageListener() {
       @Override
       public List<Long> consumeMessage(String queue, List<Message> messages) {
           List<Long> messageIds = new ArrayList<>();
           for (Message message : messages) {
               System.out.println("queue = " + queue + ", message = " + message);
               messageIds.add(message.getMessageId());
               // 消费成功后确认消息。消息消费失败时，不用删除消息，消息会在一段时间后可再次被消费者拉取到
               // 异步确认消息
               consumer.deleteMsg(queue, message.getReceiptHandle(), new DeleteCallback() {
                   @Override
                   public void onSuccess(DeleteResult deleteResult) {
                       if (deleteResult.getReturnCode() != 0) {
                           System.out.println("delete msg error, ret:" + deleteResult.getReturnCode() + " ErrMsg:" + deleteResult.getErrorMessage());
                       }
                   }
   
                   @Override
                   public void onException(Throwable e) {
                       e.printStackTrace();
                       System.out.println("delete msg error: " + e);
                   }
               });
           }
           return messageIds;
       }
   });
   
   // consumer.shutdown之前，取消监听
   try {
       System.in.read();
       consumer.unSubscribe(queue);
   } catch (IOException e) {
       e.printStackTrace();
   }
   
   try {
       Thread.sleep(3000);
       consumer.shutdown();
   } catch (InterruptedException e) {
       e.printStackTrace();
   }
:::
<table>
    <thead>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>NameServerAddress</td>
        <td>API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt;
            <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png"
                                             referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td>SecretId、SecretKey</td>
        <td>云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt;
            <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png"
                                              referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td>queue</td>
        <td>队列名称，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong>列表页面获取。</td>
    </tr>
    </tbody>
</table>
5. 主动获取消息。
<dx-codeblock>
:::  java
   // 单条消息拉取，没有消息可消费时等待10s，不传入该参数则使用consumer设置的等待时间
   // 建议在try-catch中接收，出现异常可以打印日志
   ReceiveResult result = consumer.receiveMsg(queue, 10);
   int ret = result.getReturnCode();
   if (ret == 0) {
       System.out.println("receive success, msgId:" + result.getMessage().getMessageId() + " ReceiptHandle:" + result.getMessage().getReceiptHandle() + " Data:" + result.getMessage().getData());
       // TODO 此处写入消费逻辑
       // 消费成功后确认消息。消息消费失败时，不用删除消息，消息会在一段时间后可再次被消费者拉取到
       // 异步确认消息
       consumer.deleteMsg(queue, result.getMessage().getReceiptHandle(), new DeleteCallback() {
           @Override
           public void onSuccess(DeleteResult deleteResult) {
               if (deleteResult.getReturnCode() != 0) {
                   System.out.println("delete msg error, ret:" + deleteResult.getReturnCode() + " ErrMsg:" + deleteResult.getErrorMessage());
               }
           }
   
           @Override
           public void onException(Throwable e) {
               e.printStackTrace();
               System.out.println("delete msg error: " + e);
           }
       });
   } else {
       System.out.println("receive Error, ret:" + ret + " ErrMsg:" + result.getErrorMessage());
   }
:::
</dx-codeblock>

## 主题模型

1. 在控制台创建资源。
   -  在控制台创建主题，参见 [主题管理](https://cloud.tencent.com/document/product/1496/61021)。
   -  给主题创建一个订阅者，参见 [订阅管理](https://cloud.tencent.com/document/product/1496/61022)。
2. 引入 CMQ 客户端相关依赖。
<dx-codeblock>
:::  xml
   <dependency>
       <groupId>com.qcloud</groupId>
       <artifactId>cmq-tcp-client</artifactId>
       <version>1.1.7</version>
   </dependency>
:::
</dx-codeblock>
3. 创建生产者。
<dx-codeblock>
:::  java
   Producer producer = new Producer();
   // 设置 Name Server地址。必须设置 不同地域不同网络不同
   producer.setNameServerAddress(NameServerAddress);
   // 设置SecretId，在控制台上获取，必须设置
   producer.setSecretId(SecretId);
   // 设置SecretKey，在控制台上获取，必须设置
   producer.setSecretKey(SecretKey);
   // 设置签名方式，可以不设置，默认为SHA1
   producer.setSignMethod(ClientConfig.SIGN_METHOD_SHA256);
   // 设置发送消息失败时，重试的次数，设置为0表示不重试，默认为2
   producer.setRetryTimesWhenSendFailed(3);
   // 设置请求超时时间， 默认3000ms
   producer.setRequestTimeoutMS(5000);
   producer.start();
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
        <td>NameServerAddress</td>
        <td>API 调用地址，在 <a href='https://console.cloud.tencent.com/tdmq'>TDMQ CMQ 版控制台</a> 的<strong>队列服务</strong> &gt;
            <strong>API请求地址</strong>处复制。<img src="https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png"
                                             referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td>SecretId、SecretKey</td>
        <td>云 API 密钥，登录 <a href='https://console.cloud.tencent.com/cam/overview'>访问管理控制台</a>，在<strong>访问密钥</strong> &gt;
            <strong>API密钥管理</strong>页面复制。<img src="https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png"
                                              referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    </tbody>
</table>
4. 发送 TAG 类型消息。
<dx-codeblock>
:::  java
   // 1. 向标签过滤的topic发布同步消息（也可发布异步消息和批量发布消息）
   String tag = "TAG";
   String msgTag = "This is a tag message. message tag:" + tag + ".";
   // 需要先在控制台创建一个 消息过滤类型为'标签'的主题
   String topicWithTag = "topic_tag";
   List<String> tagList = Arrays.asList(tag);
   try {
       PublishResult result = producer.publish(topicWithTag, msgTag, tagList);
       if (result.getReturnCode() == ResponseCode.SUCCESS) {
           System.out.println("===> publish tag message success, msgId : " + result.getMsgId());
       } else {
           System.out.println("===> publish error : " + result.getErrorMsg() + ", msgId :" + result.getMsgId());
       }
   } catch (MQClientException | MQServerException e) {
       e.printStackTrace();
   }
:::
</dx-codeblock>
5. 发送 route 消息。
<dx-codeblock>
:::  java
   // 路由键
   String route = "a.#";
   // 向路由消息匹配主题发布同步消息（也可发布异步消息和批量发布消息）
   String msgRoute = "This is a route message. message route:" + route + ".";
   // 需要现在控制台创建一个 消息过滤类型为'路由匹配'的主题
   String topicWithRoute = "topic_route";
   // routingKey与rabbitMQ中的相关概念相同，与订阅时指定的bindingKey配合使用
   try {
       PublishResult result = producer.publish(topicWithRoute, msgRoute, route);
       if (result.getReturnCode() == ResponseCode.SUCCESS) {
           System.out.println("===> publish route message success, msgId : " + result.getMsgId());
       } else {
           System.out.println("===> publish error : " + result.getErrorMsg() + ", msgId :" + result.getMsgId());
       }
   } catch (MQClientException | MQServerException e) {
       e.printStackTrace();
   }
:::
</dx-codeblock>
6. 消费者消费订阅者订阅的消息队列即可。

>?以上是 CMQ 两种模型下的生产和消费方式的简单介绍，更多使用可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-Java-sdk-demo.zip)。
