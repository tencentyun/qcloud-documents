The prerequisite for publishing topic messages is that a subscriber must first subscribe a topic. If there is no subscriber, the message in the topic cannot be delivered. Thus, the publishing operation makes no sense.

## 1. Creating a Topic

```
	endpoint='' //Domain name of CMQ
	secretId ='' // User's ID and Key
	secretKey = ''
	account = Account(endpoint,secretId,secretKey)
	topicName = 'TopicTest8B'
	my_topic = account.get_topic(topicName)
	topic_meta = TopicMeta()
	my_topic.create(topic_meta)
```


You can view the created topic from the console. If QPS = 5,000, the maximum API calling frequency defaults to 5,000 counts/s. You can submit a ticket to apply for a higher quota if needed.

![](//mc.qcloudimg.com/static/img/22f31138a083444bb4f21fc9f2135f31/image.jpg)


## 2. Publishing a Message

You can publish a message using SDK, as shown below.

```
	message = Message()
	message.msgBody = "this is a test message"
	my_topic.publish_message(message)
```

<br>You can also publish a message from the console, as shown below.

Topic currently supports message filtering, such as message tag, message type, to differentiate message categories under the Topic of a certain CMQ. CMQ allows consumers to filter messages based on the tags and thus only consume the messages that they're interested in. The function is disabled by default. In this case, all messages are sent to all subscribers. But after a tag is added, subscribers can only receive messages with such tag. The message filter tag describes the tag used for message filtering for this subscription (only the messages with consistent tags will be pushed). Each tag is a string with no more than 16 characters. There can be at most 5 tags for a single Message.

![](//mc.qcloudimg.com/static/img/b1a9f1b88a1f4db1d49dfef37171911e/image.jpg)

Topic currently supports both tag filtering and routingKey filtering. Filtering rules are shown above.

**Publishing messages in batch:**

```
	vmsg = []
	for i in range(6):
	message = Message()
	message.msgBody = "this is a test message"
	vmsg.append(message)

	my_topic.batch_publish_message(vmsg)
```



## 3. Message Processing

When a topic publishes a message, it will be automatically pushed to subscribers. If the push fails, two retry strategies are available:

- Backoff retry: Retry 3 times with a random interval between 10 and 20 seconds. After that, the message will be discarded for the subscriber, and will not try again;
- Exponential decay retry: Retry 176 times. The total retry time is 1 day with the interval: 2^0, 2^1, ..., 512, 512, ..., 512 seconds. Exponential decay retry is used by default.


### Using a Queue to Process Messages

Subscribers can enter a Queue to receive published messages.

```
	subscription_name = "subsc-test"
	my_sub = my_account.get_subscription(topic_name, subscription_name)
	subscription_meta = SubscriptionMeta()
	# Enter the subscription name. Here is the queue name
	subscription_meta.Endpoint = "queue name  "
	subscription_meta.Protocal = "queue"
	my_sub.create(subscription_meta)
```


### Other Means to Process Messages

Besides Queue, subscribers can also process messages by other means. For example, a Web code is provided to process messages pushed by Topic.

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

Here, Web does not process the acquired messages, but only returns a "hellow world" string when receiving a message. CMQ will then use HTTP status codes to determine whether it is pushed successfully. If the returned status code is 2xx, the push succeeds.

Before using the Web, you need to create a subscription

```
    subscription_name = "subsc-test"
    my_sub = my_account.get_subscription(topic_name, subscription_name)
    subscription_meta = SubscriptionMeta()
    # Enter the subscription address. Here is your domain name or server IP
    subscription_meta.Endpoint = "your endpoint "
    subscription_meta.Protocal = "http"
    my_sub.create(subscription_meta)
```

Then, Topic will push messages automatically to the corresponding endpoint.


## 4. Routing Match
Binding key and Routing key are used at the same time, compatible with rabbitmq topic matching mode. The Routing key when client sends messages must be a string without wildcards. The Binding key for subscription creation is used to bind the topic and the subscriber.

**Service limits:**
- The maximum number of binding keys is 5. This field indicates the routing path for sending messages. The length of a binding key should be <= 64 bytes and contain up to 15 ".", i.e. 16 phrases at most;
- Routing key contains one string. It indicates the routing path for sending messages. The length of a routing key should be <= 64 bytes and contain up to 15 ".", i.e. 16 phrases at most.

**Wildcard description:**
- \* (Asterisk) can be a substitute for a word (a sequence of alphabetic string)
- # (Pound sign) can be used to match one or more characters
- Special case of rabbitmq: If routing_key is an empty string, \* cannot be matched, but # can.

**For example:**
- Subscribers to "1.*.0" receive all messages for "1.any characters.0".
- Subscribers to "1.#.0" receive all messages for "1.2.3.4.4.2.2.0". (It can be any elements in between.) 

### Enabling Route Matching

```
    endpoint='' //Domain name of CMQ
    secretId ='' // User's ID and Key
    secretKey = ''
    account = Account(endpoint,secretId,secretKey)
    topicName = 'TopicTest'
    my_topic = account.get_topic(topicName)
    topic_meta = TopicMeta()
    topic_meta.filterType = =2 //Indicates the routing match used when the message is delivered to the subscriber.
    //If filterType = 1, a tag is used for filtering.
    my_topic.create(topic_meta)

    subscription_name = "subsc-test"
    my_sub = my_account.get_subscription(topic_name, subscription_name)
    subscription_meta = SubscriptionMeta()
    //Enter the subscription name. Here is the queue name
    subscription_meta.Endpoint = "queue name  "
    subscription_meta.Protocal = "queue"
    subscription_meta.bindingKey=[1.*.0]  //If the tag of the message is "1.any characters.0", all subscribers can
    //receive the message
    my_sub.create(subscription_meta)
```


### Publishing a Message

```
    message = Message()
    message.msgBody = "this is a test message"
    routingKey = '1.test.0' //The message will be delivered to the subscription address in my_sub.
    my_topic.publish_message(message)
```

   

