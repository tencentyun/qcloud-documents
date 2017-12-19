## Introduction to Event Notification

When some events occur, or after an asynchronous task is performed, the VOD server can notify the APP client of such events. Currently, the VOD system supports the following event notifications:

| Event Type | eventType |
|---------|---------|
| Video upload completed | [NewFileUpload](/document/product/266/7830) |
| URL pulling completed | [PullComplete](/document/product/266/7831) |
| Video transcoding completed | [TranscodeComplete](/document/product/266/7832) |
| Video stitching completed | [ConcatComplete](/document/product/266/7834) |

VOD allows the APP to get event notifications in two ways:

- HTTP callback;
- Reliable notification based on message queue.

Comparison of the two methods: The former is simply configured; the latter is of high security and reliability, but its configuration is complicated.

## HTTP Callback

The basic process of HTTP callback is as follows: An HTTP service is built at the APP backend to receive the callback, and a callback URL is configured in the VOD console; when the event occurs, the VOD server will initiate an HTTP POST request to the URL, and specific event content will be delivered to the APP backend through HTTP Body.

### How to Configure
Enter the "Console" -> "Global Settings" -> "Callback Configuration" page, set the "Callback URL" to the address for the APP backend to receive the callback, select "Normal Callback" in the "Callback Model", and select the event callback type you need.

[1]://mc.qcloudimg.com/static/img/349c36d65d5c42163ec131e1689db5a4/image.png

### Callback Protocol
Request: HTTP POST request. The packet body content is JSON. For the specific packet body content for each type of callback, refer to the related documentation.
Response: The VOD server will ignore the response packet content.

### Common Parameter Description

| Name | Type | Description |
|---------|---------|---------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Event type. APP backend can distinguish different callbacks based on this field |
| data | Object | Specific callback data |
| data.status | Integer | Error code, 0: Succeeded; other values: Failed |
| data.message | String |　Error message  |

### Example of Callback Request

The following is an example of callback for a successful video stitching (complete HTTP request). We here assume that the callback URL is `https://www.example.com/path/to/your/service`.

```
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
```

### Example of Callback Response

For HTTP callback, the APP backend needs to respond to the callback request, and the VOD backend will ignore the HTTP error code and packet body. Example:

```
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 4

{
}
```

### Callback Timeout and Retry
The timeout for VOD server initiating an HTTP callback is 5 seconds; if the callback times out, the VOD backend will retry twice (i.e., a maximum of three attempts is allowed). If you are sensitive to the reliability of the callback, we recommend that you use reliable notifications based on message queue.

### Security Considerations
To ensure security, APP can set the callback URL to HTTPS. What the solution can achieve:
- VOD server can verify the validity of APP callback URL;
- The callback data cannot be monitored.

What the solution cannot achieve:
- The APP backend server cannot verify whether the requester is a VOD server.

If you need a higher security level, we recommend that you use reliable notifications based on message queue.

## Reliable Notification Based on Message Queue

APP server may encounter network problems or failures such as crashes. For simple HTTP callback, the reliability cannot be ensured even with more retries allowed. To ensure the callback reliability, VOD provides a second callback method: reliable notification based on message queue. Meanwhile, the security of this solution is much higher.

### Configuration Method
Enter the "Console" -> "Global Settings" -> "Callback Configuration" page, select "Reliable Callback" in the "Callback Model", and select the event callback type you need. Note: In the model of reliable callback, the "Callback URL" will not take effect.

[2]://mc.qcloudimg.com/static/img/e448c807e093ecae7651c9c94987137c/image.png

### Basic Principle

- The VOD backend will maintain a message queue for APP, and will play the role of producer;
- When a new event is generated, the VOD backend will put the message in the message queue;
- The APP backend plays the role of consumer, and acquires contents of the message queue through a long polling way. Long polling means that the APP backend must cyclically call the API [PullEvent](/document/product/266/7818) to pull the event notification. If there is a message in the current message queue, the API will return the content immediately; if there is no unconsumed event notification, the VOD backend will suspend the request until a new event is generated; each request can be suspended for up to 5 seconds.
- After the APP backend pulls the message via [PullEvent](/document/product/266/7818), it must call the API [ConfirmEvent](/document/product/266/7819) to confirm that the event notification has been consumed, otherwise the message may be consumed again.

[3]://mc.qcloudimg.com/static/img/740ef842285aef44ff4911cc702ee178/image.png "As shown in the following figure: The first dashed box describes the complete consumption process of an event notification; the second dashed box indicates that the PullEvent does not get a new event notification, and the APP backend needs to continue to call the PullEvent."

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

2. If there is an unconsumed event notification, the server response packet body is as follows. The msgHandle field in the eventList is critical and will be used later.
```javascript
{
    "code": 0,
    "message": "",
    "eventList": [  // The pulled list of server event notifications, which includes two event notifications
        {
            "msgHandle": "MsgHandle1",  // The handler of the first event notification
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
            "msgHandle": "MsgHandle2", // The handler of the second event notification
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

3. After the APP backend consumes an event notification, it will call the API [ConfirmEvent](/document/product/266/7819) to confirm that the event notification has been received. The eventList.msgHandle returned by PullEvent is used as the parameter.
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
