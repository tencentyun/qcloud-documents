主题发布消息有一个前提，那就是需要有订阅者订阅主题，如果没有订阅者存在，那么主题中的消息不会被投递，这样发布消息这一操作就失去了意义。

## 1.创建主题

```
	endpoint='' //cmq的域名
	secretId ='' // 用户的id和key
	secretKey = ''
	account = Account(endpoint,secretId,secretKey)
	topicName = 'TopicTest8B'
	my_topic = account.get_topic(topicName)
	topic_meta = TopicMeta()
	my_topic.create(topic_meta)
```


可以从控制台上查看创建出来的主题。其中 QPS=5000，表示调用同一个接口的频率上限，默认的是5000次/s。如果您有需求提高上限，可以通过工单反馈。

![](//mc.qcloudimg.com/static/img/22f31138a083444bb4f21fc9f2135f31/image.jpg)


## 2.发布消息

使用 SDK 发送消息如下所示。

```
	message = Message()
	message.msgBody = "this is a test message"
	my_topic.publish_message(message)
```

<br>您也可以使用控制台发布消息，如下图所示。

Topic 目前支持消息过滤，即消息标签、消息类型，用来区分某个 CMQ 的 Topic 下的消息分类。MQ 允许消费者按照标签对消息进行过滤，确保消费者最终只消费到他关心的消息类型。该功能默认不开启，未开启时，所有消息向所有订阅者发送；增加标签后，订阅者将仅能收到带该标签的信息。消息过滤标签描述了该订阅中消息过滤的标签（标签一致的消息才会被推送）。单个标签不超过16个字符，单个 Message 可最多添加5个标签。

![](//mc.qcloudimg.com/static/img/b1a9f1b88a1f4db1d49dfef37171911e/image.jpg)

Topic 目前支持标签过滤和 routingKey 过滤两种方式。过滤规则如上图所示。

**批量发布消息：**

```
	vmsg = []
	for i in range(6):
	message = Message()
	message.msgBody = "this is a test message"
	vmsg.append(message)

	my_topic.batch_publish_message(vmsg)
```



## 3.消息处理

主题发布消息之后，会自动推送消息给订阅。若主题推送给订阅失败，有两种重试策略：

- 退避重试：重试3次，间隔时间10-20s之间的一个随机值，超过3次后，该条消息对于该订阅者丢弃，不会再重试；
- 衰退指数重试：重试176次，总计重试时间为1天，间隔时间依次为：2^0，2^1, …, 512, 512, …, 512秒。默认为衰退指数重试策略。


### 使用队列处理消息

订阅者可以填写一个 Queue，使用队列来接收发布的消息。

```
	subscription_name = "subsc-test"
	my_sub = my_account.get_subscription(topic_name, subscription_name)
	subscription_meta = SubscriptionMeta()
	# 填写订阅名称，这里填写队列名称
	subscription_meta.Endpoint = "queue name  "
	subscription_meta.Protocal = "queue"
	my_sub.create(subscription_meta)
```


### 使用其他方式处理消息

订阅者也可以不与 Queue 结合，自己来处理消息。这里提供一段 Web 代码来处理 Topic 推送的消息。

```
	class MainHandler(tornado.web.RequestHandler):
	def get(self):
	self.write("Hello, world")
	def post(self, *args, **kwargs):
	self.write('hello, world')
	def set_default_headers(self):
	self.set_header('Content-type','application;charset=utf-8')
	application = tornado.web.Application([(r"/",MainHandler),])
	if __name__ == "__main__" :
	application.listen(8889)
	tornado.ioloop.IOLoop.instance().start()
```

这里 Web 没有处理接收的消息，只是在收到消息的时候向服务器返回一个 hellow world 字符串，CMQ 通过 HTTP 状态码来判断是否成功推送，若返回的状态码为 2xx，则认为推送成功。

使用该 Web 时，首先需要创建一个订阅

```
    subscription_name = "subsc-test"
    my_sub = my_account.get_subscription(topic_name, subscription_name)
    subscription_meta = SubscriptionMeta()
    # 填写订阅地址，这里可以填写自己的域名或者填写机器的ip
    subscription_meta.Endpoint = "your endpoint "
    subscription_meta.Protocal = "http"
    my_sub.create(subscription_meta)
```

这样，Topic 发布消息就会自动向对应的 endpoint 推送消息了。


## 4.路由匹配
Binding key 、Routing key 是组合使用的，兼容 rabbitmq topic 匹配模式。发消息时配的 Routing key 是客户端发消息带的， 必须是字符串，不能有匹配符。创建订阅关系时配的 Binding key 是 topic 和 订阅者 的绑定关系。

**使用限制：**
- Binding key 的数量不超过5个。单个 binding key 的长度 <= 64字节，用于表示发送消息的路由路径，最多含有15个“.”，即最多16个词组；
- Routing key 的数量由1个字符串组成。单个 Routing key 的长度 <= 64字节，用于表示发送消息的路由路径，最多含有15个“.”，即最多16个词组。

**通配符说明：**
- \*（星号），可以替代一个单词（一串连续的字母串）
- #（井号）：可以匹配一个或多个字符
- rabbitmq的特例：routing_key为空字符串时，不匹配\* ，但可以匹配#

**举例：**
- 订阅者是『1.*.0』，此时消息为『1.任意字符.0』，则订阅者都能收到消息
- 订阅者是『1.#.0』，此时消息为『1.2.3.4.4.2.2.0』，则订阅者都能收到消息（消息中间元素随意） 

### 使用路由匹配功能

```
    endpoint='' //cmq的域名
    secretId ='' // 用户的id和key
    secretKey = ''
    account = Account(endpoint,secretId,secretKey)
    topicName = 'TopicTest'
    my_topic = account.get_topic(topicName)
    topic_meta = TopicMeta()
    topic_meta.filterType = =2 //表示消息投递给订阅的时候采用路由匹配。
    //若filterType =1 则表示使用标签过滤。
    my_topic.create(topic_meta)

    subscription_name = "subsc-test"
    my_sub = my_account.get_subscription(topic_name, subscription_name)
    subscription_meta = SubscriptionMeta()
    //填写订阅名称，这里填写队列名称
    subscription_meta.Endpoint = "queue name  "
    subscription_meta.Protocal = "queue"
    subscription_meta.bindingKey=[1.*.0]  //若消息的标签为[1.任意字符.0]则该订阅者都
    //能收到该标签
    my_sub.create(subscription_meta)
```


### 发布消息

```
    message = Message()
    message.msgBody = "this is a test message"
    routingKey = '1.test.0' //该消息会被投递到 my_sub订阅的地址。
    my_topic.publish_message(message)
```

   
