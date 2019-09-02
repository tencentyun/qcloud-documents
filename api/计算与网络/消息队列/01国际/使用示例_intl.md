In order to help you get started with Cloud Message Queue (CMQ) API quickly, we provide an example on how to use it. This article provides the guide on how to use the API to create a queue, send messages, consume messages, delete messages, and delete queues.
> Note: The following parameters are examples, and are for reference only. The actual value is subject to the return value of the system. For the sake of simplicity, we take single operations as the examples of message operations, but batch API (such as [Send Messages in Batch](/doc/api/431/5838), [Delete Messages in Batch](/doc/api/431/5841)) is also supported.

Domain for public network API request: <font style="color:red">cmq-queue-region.api.qcloud.com</font>

Domain for private network API request: <font style="color:red">cmq-queue-region.api.tencentyun.com</font>

- region should be replaced with a specific region: gz (Guangzhou), sh (Shanghai), or bj (Beijing). The region value in the common parameters should be consistent with the region value of the domain. If there is an inconsistency, the request will be sent to the region specified by the domain.
- Public network domain requests both support http and https. Private network requests only support http.

## Queue Model
Take private network as an example (for public network, replace "tencentyun" in the domain with "qcloud"). The composition of request domain is `cmq-queue-region.api.tencentyun.com/v2/index.php`, where the region field should be replaced with a specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). The region value in the [Common Parameters](/doc/api/431/5883) should be consistent with the region value of the domain. If there is an inconsistency, the request will be sent to the region specified by the domain.

For more information about the generation rules of parameter Signature, refer to [Signature Method](https://cloud.tencent.com/document/product/406/5906).

### Create a Queue

Before creating a queue, please refer to the instructions of [Create Queue API](/doc/api/431/5832), and adjust the attribute values of the queue according to your business needs.
If we create a queue in Guangzhou and the expected business messages are faster than production, the required request parameters are shown in the table below:


| Parameter Name | Description | Example Value |
|---------|---------|---------|---------|
| queueName| The queue name must be unique under the same account in the same region. The queue name is a string of no more than 64 characters, which can contain letters, numbers, and hyphens (-) and must begin with a letter. | test-queue-1 |
| pollingWaitSeconds | [Waiting time for messages to be received when using long-polling](https://cloud.tencent.com/doc/product/406/4552). The value ranges from 0 to 30 seconds. Default is 0. | 30 |

By combining common request parameters and API request parameters, you can get the final request as follows:

```
http://cmq-queue-gz.api.tencentyun.com/v2/index.php?
Action=CreateQueue
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&queueName=test-queue-1
&pollingWaitSeconds=30 
```

The returned result of the above request is as follows:

```
{
"code" : 0,
"message" : "",
"requestId":"14534664555",
"queueId":"queue-ajksdfasdowe"
}
```

We successfully created a queue. Users can manage the queue, send and consume messages, and perform other operations.

### Send a Message

Before sending a message, please refer to the instructions of [Send Message API](/doc/api/431/5837).
If we send a message to the `test-queue-1` queue created in the example above, the required request parameters are shown in the table below:


| Parameter Name | Description | Example Value |
|---------|---------|---------|---------|
| queueName| The queue name must be unique under the same account in the same region. The queue name is a string of no more than 64 characters, which can contain letters, numbers, and hyphens (-) and must begin with a letter. | test-queue-1 |
| msgBody| Message text. The size is at least 1 Byte, and the maximum length is limited by the set maximum length attribute of the queue message. | This'is test message (After encoded with URL, it should be This%27is+test+message) |

The request is as follows:

```
http://cmq-queue-gz.api.tencentyun.com/v2/index.php?
Action=SendMessage
&Region=gz
&Timestamp=1465750149
&Nonce=46365
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWagTTyk18V2g%2FYi56hqls%3D
&queueName=test-queue-1
&msgBody=This%27is+test+message
```

The returned result of the above request is as follows:

```
{
"code" : 0,
"message" : "",
"requestId":"145346456555",
"msgId":"123345346"
}
```

### Consume a Message

Before consuming a message, please refer to the instructions of [Consume Message API](/doc/api/431/5837). You can choose the value of pollingWaitSeconds according to your business features.
If we consume a message from the `test-queue-1` queue created in the example above, the required request parameters are shown in the table below:


| Parameter Name | Description | Example Value |
|---------|---------|---------|---------|
| queueName| The queue name must be unique under the same account in the same region. The queue name is a string of no more than 64 characters, which can contain letters, numbers, and hyphens (-) and must begin with a letter. | test-queue-1 |
| pollingWaitSeconds| Waiting time for the request when using long-polling. The value ranges from 0 to 30 seconds. Default is 0. | 10 |

The request is as follows:

```
http://cmq-queue-gz.api.tencentyun.com/v2/index.php?
Action=ReceiveMessage
&Region=gz
&Timestamp=1465750150
&Nonce=46368
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUaagTTyk18V2g%2FYi56hqls%3D
&queueName=test-queue-1
&pollingWaitSeconds=10
```

The returned result of the above request is as follows:

```
{
"code" : 0,
"message" : "",
"requestId":"145346635355",
"msgBody":"This is test message",
"msgId":"123345346",
"receiptHandle": "283748239349283",
"enqueueTime": 1462351990,
"firstDequeueTime": 1462352990,
"nextVisibleTime": 1462352999,
"dequeueCount": 1
}
```

### Delete a Message

In general, the message that has been consumed once should be deleted, unless your business has the demand for repeated consumption. Before deleting a message, please refer to the instructions of [Delete Message API](/doc/api/431/5837).
If we consume a message from the queue `test-queue-1` and delete it after consuming, please be sure to <font color="red">delete it before the time of nextVisibleTime</font>. Otherwise, the receiptHandle will become invalid, and the deletion operation will fail. The required request parameters are shown in the table below:


| Parameter Name | Description | Example Value | 
|---------|---------|---------|---------|
| queueName| The queue name must be unique under the same account in the same region. The queue name is a string of no more than 64 characters, which can contain letters, numbers, and hyphens (-) and must begin with a letter. | test-queue-1 |
| receiptHandle| The unique message handle returns after each consumption, which is used to delete messages. Only the message handle generated when the message was consumed last time can be used to delete this message. | "283748239349283" (receiptHandle in the example above) |


The request is as follows:

```
http://cmq-queue-gz.api.tencentyun.com/v2/index.php?
Action=DeleteMessage
&Region=gz
&Timestamp=1465750151
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUaagTasdfk18V2g%2FYi56hqls%3D
&queueName=test-queue-1
&receiptHandle=283748239349283
```

The returned result of the above request is as follows:

```
{
"code" : 0,
"message" : "",
"requestId":"14534454555"
}
```


### Delete a Queue

Before deleting a queue, please refer to the instructions of [Delete Queue API](/doc/api/431/5837). When the queue is no longer used, it needs to be deleted. The required request parameters are shown in the table below:


| Parameter Name | Description | Value |
|---------|---------|---------|---------|
| queueName| The queue name must be unique under the same account in the same region. The queue name is a string of no more than 64 characters, which can contain letters, numbers, and hyphens (-) and must begin with a letter. | test-queue-1 |


The request is as follows:

```
http://cmq-queue-gz.api.tencentyun.com/v2/index.php?
Action=DeleteQueue
&Region=gz
&Timestamp=1465750152
&Nonce=46370
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUaagTasasdl18V2g%2FYi56hqls%3D
&queueName=test-queue-1
```

The returned result of the above request is as follows:

```
{
"code" : 0,
"message" : "",
"requestId":"14534454555"
}
```

