## 1. Creating a Queue

```
		endpoint='' //Domain name of CMQ
		secretId ='' // User's ID and Key
		secretKey = ''
        account = Account(endpoint,secretId,secretKey)
        queueName = 'QueueForTest'
        queue=account.get_queue(queueName)
        queue_meta = QueueMeta()
        queue_meta.queueName = queueName
        queue_meta.visibilityTimeout = 10 
        queue_meta.maxMsgSize = 65536
        queue_meta.pollingWaitSeconds = 10
        try:
            queue.create(queue_meta)
        except CMQExceptionBase,e:
            print e
```

After the queue is created, you can view the created queue information from the console.

![](//mc.qcloudimg.com/static/img/25c1dcccefc7c05e0574af5e22e720c7/image.jpg)


## 2. Generating a Message
After obtaining the queue object, you can call Send Message API of the queue to send messages to the queue. You can perform the API by sending a message or sending messages in batch.

- **Generating a message:**
<br>
```
		msg_body = "I am test message."
    msg = Message(msg_body)
    re_msg = my_queue.send_message(msg)
```
<br>You can view the message attributes directly from the console.
<br>![](//mc.qcloudimg.com/static/img/73cb26b23c67ad63947e21253d941af0/image.jpg)


- **Generating messages in batch:**

```
    msg_count=3
    messages=[]
    for i in range(msg_count):
        msg_body = "I am test message %s." % i
        msg = Message(msg_body)
        messages.append(msg)

    re_msg_list = my_queue.batch_send_message(messages)	
```

## 3. Consuming a Message

The default parameter pollingWaitSeconds indicates the desired waiting time when consuming messages. If left empty, it will use the attribute value in the queue.

- **Consuming a message:**

```
    wait_seconds=3
    recv_msg = my_queue.receive_message(wait_seconds)
```


- **Consuming messages in batch:**

```
		wait_seconds = 3
    num_of_msg = 3
    recv_msg_list = my_queue.batch_receive_message(num_of_msg, wait_seconds)

```

### Note
- **Set the appropriate pollingWaitSeconds**
You can either customize the value of pollingWaitSeconds or use the default value of the queue. If the value is set to 0, it will not wait for messages. But if so, no messages may be returned (even if there is a message in the queue). That's because a large number of consumers may queue up for the queuing service when consuming messages at the same time. If you set the value to 0, you may receive the exception of no message since your request has timed out before your turn. Therefore, you are not recommended to set the waiting time to 0.

- **If number of messages in the queue < number of messages consumed in batch, your consumption will not be blocked.**
When consuming messages in batch, you need to fill in the number of messages to be received this time. If the number of messages in the queue is less than the number of messages to be consumed, your operation will not be blocked.

- **In the queue attributes, by setting invisibility time > message retention period, you can consume each message once.**
When the invisibility time > message retention period, the message consumed will become invisible and removed from the queue after the timeout of the retention period. In this way, the message is only consumed once and will not be consumed again. 
However, there may be duplicate generation and failed consumption in the process of generation and consumption. It is impossible to ensure that the queue is only consumed once by modifying the queue attributes. The service end need to involve in duplicate removal and fault tolerance for message consumption. Please see [Duplicate Message Removal](https://cloud.tencent.com/document/product/406/8303)



## 4. Message Rewind
Let's see the use of the message rewind in the following scenario:

Assuming that there are A/B services in normal generation and consumption scenarios, A generates messages and delivers them to the queue and B consumes messages from the queue. In this case, A and B work independently without interfering with each other. A only generates messages for delivery while B acquires and deletes messages from the queue and then consumes messages locally.

For example, although B service has consumed messages, an exception has occurred with the consumption in a period of time. At this time, the deleted messages cannot be re-consumed, thus affecting the service. In this case, B service will be suspended and can only be resumed after developers or O&M personnel repair the bug. But O&M personnel cannot provide real-time monitoring for B service. It may take a while before the exception is detected.

To prevent this situation, A service needs to interfere in the processing of B service, back up generated messages and delete such backup data until B service is running properly, so as to ensure the normal operation of existing networks.

In this case, you can use **message rewind** function. The developer will repair B service and rewind the message to the latest point in time with normal consumption. Then, B service will acquire messages from such point in time. Thus, A service don't need to interfere in the exception of B service. Please note B need to perform idempotent operations for the consumption.

[Learn more about Message Rewind >>](https://cloud.tencent.com/document/product/406/8129)


### Enabling Message Rewind

```
    endpoint='' //Domain name of CMQ
    secretId ='' // User's ID and Key
    secretKey = ''
    account = Account(endpoint,secretId,secretKey)
    queueName = 'QueueTest'
    my_queue = account.get_queue(queueName)
    queue_meta = QueueMeta()
    queue_meta.rewindSeconds = 43200 //Time allowed for message rewind (in seconds)
    my_queue.create(queue_meta)
```

### Using Message Rewind

```
    my_queue.rewindQueue(1488718862) //Point in time for this message rewind (Unix timestamp)
```

## 5. Delayed Messages

**Delayed messages**: When generating messages, you can specify a flight time, that is, the time spend in delivering messages to the queue. The message can only be consumed by consumers after such time.

Some services may fail, and then they need to re-consume messages after a certain period of time. In this case, you can use delayed messages.

**For example:**

```
    message_body='i am test'
    msg = Message(message_body)
    my_queue.send_message(msg)
    //Message consumption is found failed. You can re-deliver the message and set the message's flight time.
    my_queue.send_message(msg,600) //The flight time is set to 10 minutes.
    //You can view the number of delayed messages in the queue via message attributes
    queue_meta = my_queue.get_attributes()
    print queue_meta.delayMsgNum
    
```

