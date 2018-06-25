Video processing and other operations in VOD are offline tasks which consume more resources and take more time (maybe dozens of minutes) than traditional "real-time tasks". Thus, the "request-response" mode applied in "real-time tasks" is no longer applicable in this scenario. The VOD system provides a complete task submission and management mechanism for the offline tasks.

- Task request: Developers initiate offline tasks using certain methods (console, server API, etc.);
- Processing task: The VOD backend starts processing tasks and returns task ID to developers;
- Status query: Developers can query the task processing progress (in quene/running/completed) using task ID;
- Event notification: If the status of an offline task in progress changes (e.g. a sub-task is completed) or the entire task is completed, the VOD backend will initiate an event notification to the APP backend.

![](//mc.qcloudimg.com/static/img/d6fab9ad4ebff02f72bf1c932d64ccdd/image.png)

## Task Management

You can manage the offline tasks in progress via the following server APIs:
- [Task Status](/document/product/266/11721);
- [Query Task List](/document/product/266/11722);
- [Query Task Details](/document/product/266/11724);
- [Retry Task](/document/product/266/11725).

## Event Notification Overview

When some events occur or an asynchronous task is completed, the VOD server will send an event notification to the APP server. The VOD system supports the following event notifications:

| Event Type | EventType |
|---------|---------|
| Notification for task flow status changes | [ProcedureStateChanged](/document/product/266/9636) |
| Video upload completed | [NewFileUpload](/document/product/266/7830) |
| URL pulling completed | [PullComplete](/document/product/266/7831) |
| Video transcoding completed | [TranscodeComplete](/document/product/266/7832) |
| Video stitching completed | [ConcatComplete](/document/product/266/7834) |
| Video clipping completed | [ClipComplete](/document/product/266/10157) |
| Video screenshots capturing for image sprite completed | [CreateImageSpriteComplete](/document/product/266/8104) |
| Video screenshots at specified time point completed | [CreateSnapshotByTimeOffsetComplete](/document/product/266/8105) |
| Video deletion completed | [FileDeleted](https://cloud.tencent.com/document/product/266/13434) |

VOD allows the APP to get event notifications in two ways:

- HTTP callback;
- Reliable notification based on message queue.

Comparison of the two methods: The former is simply configured; the latter is of high security and reliability, but its configuration is complicated.

## HTTP Callback

The basic process of HTTP callback is as follows: An HTTP service is built at the APP backend to receive the callback, and a callback URL is configured in the VOD console; when the event occurs, the VOD server will initiate an HTTP POST request to the URL, and specific event content will be delivered to the APP backend through HTTP Body.

### How to Configure
Go to the "Console" -> "Global Settings" -> "Callback Configuration" page, set the "Callback URL" to the address for the APP backend to receive the callback, select "Normal Callback" in the "Callback Model", and select the event callback type you need.

See the figure below:

![](//mc.qcloudimg.com/static/img/349c36d65d5c42163ec131e1689db5a4/image.png)

### Callback Protocol
Request: HTTP POST request. The packet body content is JSON. For the specific packet body content for each type of callback, refer to the related documentation.
Response: The VOD server will ignore the response packet content.

### Common Parameter Description

| Name | Type | Description |
|---------|---------|---------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Event type. APP backend can distinguish different callbacks based on this field |
| data | Object | Specific callback data |
| data.status | Integer | Error code. 0: Successful; other values: Failed. |
| data.message | String |　Error message  |

### Example of Callback Request

The following is an example of callback for a successful video stitching (complete HTTP request). We here assume that the callback URL is `https://www.example.com/path/to/your/service`.

<pre>
POST /path/to/your/service
HOST: www.example.com

{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "vodTaskId": "concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": 0,
                "message": "",
                "fileId": "14508071098244931831",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8"
            },
            {
                "fileType": "mp4",
                "status": 0,
                "message": "",
                "fileId": "14508071098244929440",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
            }
        ]
    }
}
</pre>

### Example of Callback Response

For HTTP callback, the APP backend needs to respond to the callback request, and the VOD backend will ignore the HTTP error codes and packet body. Here is an example:

<pre>
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 4

{
}
</pre>

### Callback Timeout and Retry
The timeout for VOD server initiating an HTTP callback is 5 seconds; if the callback times out, the VOD backend will retry twice (i.e., a maximum of three attempts is allowed). If you are sensitive to the callback reliability, we recommend that you use reliable notifications based on message queue.

### Security Considerations
To ensure security, you can set the callback URL to HTTPS in the APP. This solution can ensure:
- The VOD server can verify the validity of APP callback URL;
- The callback data cannot be monitored.

What the solution cannot achieve:
- The APP backend server cannot verify whether the request is sent from the VOD server.

If you need a higher security level, we recommend that you use reliable notifications based on message queue.

## Reliable Notification Based on Message Queue

The APP server may encounter network problems or failures such as crashes. The reliability of the server cannot be ensured with simple HTTP callback even with more retries allowed. To ensure the callback reliability, VOD provides reliable notification based on message queue as another response method, which is more secure than HTTP callback.

### How to Configure
Go to the "Console" -> "Global Settings" -> "Callback Configuration" page, select "Reliable Callback" in "Callback Mode", and select the event callback type you need. Note: The "Callback URL" will not take effect in reliable callback mode.

See the figure below:

![](//mc.qcloudimg.com/static/img/e448c807e093ecae7651c9c94987137c/image.png)

### Basic Principle

- The VOD backend will maintain a message queue for APP, and will play the role of producer;
- When a new event is generated, the VOD backend will put the message in the message queue;
- The APP backend plays the role of consumer, and acquires contents of the message queue through a long polling way. Long polling means that the APP backend must cyclically call the API [PullEvent](/document/product/266/7818) to pull the event notification. If there is a message in the current message queue, the API will return the content immediately; if there is no unconsumed event notification, the VOD backend will suspend the request until a new event is generated; each request can be suspended for up to 5 seconds.
- After the APP backend pulls the message via [PullEvent](/document/product/266/7818), it must call the API [ConfirmEvent](/document/product/266/7819) to confirm that the event notification has been consumed, otherwise the message may be consumed again.

As shown in the following figure: The first dashed box describes the complete consumption process of an event notification; the second dashed box indicates that the PullEvent does not get a new event notification, and the APP backend needs to continue to call the PullEvent.

![](//mc.qcloudimg.com/static/img/740ef842285aef44ff4911cc702ee178/image.png)

### Related APIs
The reliable callback based on message queue is achieved through two server APIs:
- Pull event notification ([PullEvent](/document/product/266/7818));
- Confirm event notification ([ConfirmEvent](/document/product/266/7819)).

### Example

1. APP backend calls [PullEvent](/document/product/266/7818) to obtain unconsumed event notifications. The request URL is:

```
https://vod.api.qcloud.com/v2/index.php?Action=PullEvent
&COMMON_PARAMS
```

2. If an unconsumed event notification already exists, the server response packet body is as follows. The msgHandle field in the eventList is critical and will be used later.

```javascript
{
    "code": 0,
    "message": "",
    "eventList": [  // The pulled list of server event notifications, which includes two event notifications
        {
            "msgHandle": "MsgHandle1",  // The handle of the first event notification
            "eventContent": { // The content of the first event notification
                "version": "4.0",
                "eventType": "NewFileUpload", // This field indicates that the type of the event notification is "Video Upload Completed"
                "data": {
                    "fileId": "14508071098244959037",
                    "fileUrl": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
                    "transcodeTaskId": "transcode-0bee89b07a248e27c83fc3d5951213c1",
                    "porncheckTaskId": "porncheck-f5ac8127b3b6b85cdc13f237c6005d80"
                }
            }
        },
        {
            "msgHandle": "MsgHandle2", // The handle of the second event notification
            "eventContent": { // The content of the second event notification
                "version": 4,
                "eventType": "ConcatComplete", // This field indicates that the type of the event notification is "Video Stitching Completed"
                "data": {
                    "status": 0,
                    "message": "",
                    "vodTaskId": "concat-1edb7eb88a599d05abe451cfc541cfbd",
                    "fileInfo": [
                        {
                            "fileId": "14508071098244931831",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8",
                            "fileType": "m3u8"
                        },
                        {
                            "fileId": "14508071098244929440",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4",
                            "fileType": "mp4"
                        }
                    ]
                }
            }
        }
    ]
}
```

3. After the APP backend consumes an event notification, it will call the API [ConfirmEvent](/document/product/266/7819) to confirm that the event notification has been received. The eventList.msgHandle returned by PullEvent is required as a parameter.

```
https://vod.api.qcloud.com/v2/index.php?Action=ConfirmEvent
&msgHandle.1=MsgHandle1
&msgHandle.2=MsgHandle2
&COMMON_PARAMS
```

4. VOD server will respond as follows:

```javascript
{
    "code": 0,
    "message": ""
}
```

Now, both of the two server event notifications are received. The APP backend needs to call [PullEvent](/document/product/266/7818) again to Round Robin the server event notification.

