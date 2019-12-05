## Queue Endpoint Subscription

CMQ will push the message text for topic publishing to the subscription Queue, so that consumers can read the corresponding message from the Queue.

## Http Endpoint Subscription

### Delivery Description
CMQ pushes a topic message to the Http Endpoint of the subscription by sending a POST request. Two message formats are available: JSON and SIMPLIFIED.

JSON format: The Body of the HTTP request contains the body and attributes of the message.

SIMPLIFIED format: The Body of the HTTP request is the message body. Information such as msgId will be sent to the subscriber in the Header of the HTTP request.

If a standard 2xx response (e.g. 200) is returned by the subscriber's HTTP server, it means that the request has been successfully delivered; otherwise, it means that the delivery failed, and the retry policy will be triggered. Response timeout will be deemed as a failure by CMQ, and the retry policy will also be triggered. The duration for timeout checking is about 15 seconds.

### Header of HTTP Request
| Parameter Name | Description |
|---------|-------|
| x-cmq-request-id | requestId of the message for current push |
| x-cmq-message-id | msgId of the message for current push |
| x-cmq-message-tag | Tag of the message for current push |

### Body of HTTP Request
- If the format is JSON, the Body of the HTTP request contains the body and attributes of the message.

| Parameter Name | Type | Description |
|---------|-------|-------|
| TopicOwner |String| appid of subscribed topic owner |
| topicName |String| Topic name |
| subscriptionName |String| Subscription name |
| msgId |String| Message ID |
| msgBody |String| Message body |
| publishTime |Int| Time when the message is published |

- If the format is SIMPLIFIED, the Body of the HTTP request is the body of the message published by a publisher.

### Response to HTTP Request
A 2xx response is returned if the request is normally processed by the subscriber's HTTP server; other response codes or response timeout are errors, and the retry policy will be triggered.

### Request Example
Assume that the HTTP Endpoint of a subscription is```http://test.com/cgi```

JSON format:

```
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 761
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

{"TopicOwner":100015036,"topicName":"MyTopic","subscriptionName":"mysubscription","msgId":"6942316962","msgBody":"test message","publishTime":11203432}

```

SIMPLIFIED format:

```
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 123
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

test message
```

