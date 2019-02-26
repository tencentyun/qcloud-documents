### Why do some actions not exist when I call CMQ?

For example, API "Create Topic" does not exist
CMQServerException {"code":4000,"data":"{\"code\":4000,\"message\":\"(10430)action name CreateTopic is not existed\"

You may fill wrong endpoint
Queue and Topic correspond to different endpoints, as shown below:
Queue: <font style="color:red">http: //cmq-queue-region.api.tencentyun.com/</font>
Topic: <font style="color:red">http: //cmq-topic-region.api.tencentyun.com/</font>
Please replace region with gz (Guangzhou), sh (Shanghai) or bj (Beijing) accordingly.
> Note: The above endpoint uses the private network domain. If the public network domain is required, replace tencentyun with qcloud. It is recommended that you use the private network domain instead of the public network domain, for public network needs to be paid by traffic and has relatively high delay.

### Can CMQ use the public network domain?

Yes, just replace tencentyun in the private network domain with qcloud. Note that public network needs to be paid by traffic and has relatively high delay.


### Does CMQ support https?

No, the current private network domain does not support https, but the public network domain does.

### Can collaborator account use CMQ?

No, currently it cannot.

### How many SDKs does CMQ provide? What if these SDKs are not suitable for me?

CMQ provides four SDKs, including c++, php, python and java. If you don't find an SDK with appropriate language, you can assemble the packet and call your own CMQ service following the specific documentation on the official website.

### If the number of messages in the queue is smaller than the requested number of messages consumed in batch in the API "Batch Consume" of CMQ, will the request be blocked?

No, it won't.


### As the API key is applicable to all APIs, is there any way that can make this key only applicable to the API of CMQ?

CMQ does not have the permission to control it, but it is connecting to CAM, which is expected to take effect in March. By then, you will be able to use CAM for permission control.

### Is the SDK asynchronous?

No, all operations of the SDK are synchronous.


### Why can't I delete a message?

Probably because the message handle timed out. The queue attribute visibilityTimeout 
indicates the visible time of the message. If you delete the consumed message after the visible time, the message handle will be invalid, and you cannot delete the message.


### Is there a Graph Manager interface in CMQ? Where can I check the details of the queue?

CMQ provides a visual console for you to check the current queue.
[Enter the console >>](https://console.cloud.tencent.com/mq/)

### Does CMQ support mqtt protocol?

No, it doesn't, but it will do in the future.

### Why does the error "10250	qps throttling" occur when I call CMQ?

This is because QPS has reached the upper limit. By default, the upper limit of QPS is 5000, indicating that the API can be called up to 5000 counts per second. If you have a higher demand for QPS, you can submit a ticket to apply for increasing the upper limit of qps.
 
### Is there a limit to the number of queues/topics?

Yes, the limits are as follows:
The number of queues/topics per account cannot exceed 1,000; and the number of subscriptions per topic cannot exceed 100.

### Does CMQ support kafka?

No, it doesn't. Ckafka is working on it. It will be fully available in the future.

### Is there a limit to the size of message sent to/from CMQ?

Yes, it shall not exceed 64KB.
If the message exceeds 64KB, two solutions are available:
- Store the message in the COS, and put the Object address in the CMQ message. If you want to consume the message, download it from COS.
- Split the message into multiple parts.


### Which protocol does CMQ use to access?

CMQ uses HTTP protocol, and CMQ SDK maintains TCP persistent connections.

### Does CMQ remove the duplicate message or retry after failure?

No, it doesn't. Such actions are subject to the business layer.


### How does pull implement long polling when CMQ is consuming messages?

When CMQ is consuming messages, pull implements as follows:
The queue has the attribute of pollingWaitSeconds, which indicates the default long polling time of the queue.
When a message is consumed, if there is a message, the message is returned directly;
if there is no message in the current queue, it will wait for the pollingWaitSeconds time. If there is a message during this period, the message is returned;
if there is no message during this period, it will report the exception of "No Message".
You can set the attribute of the queue according to your needs. You can also specify the pollingWaitSeconds time when consuming the message, instead of using the default value every time.


