
## Overview
Events such as state change of an LVB stream, generation of a new recording file and generation of a screenshot file are internally managed in Tencent Cloud, but your backend server may also require to be informed of these events, in which case you can use the event notification service of Tencent Cloud to acquire these events.

You can register a callback URL from your backend server on the console and provide it to Tencent Cloud. When an event occurs, Tencent Cloud will post the event to your server using HTTP POST method, with the event content organized in JSON format.

## Configure URL
When you enable LVB Code mode in the ["LVB Console" -> "LVB Code Access" -> "Access Configuration"](https://console.cloud.tencent.com/live/livecodemanage), you can specify a URL for receiving Tencent Cloud notifications, as shown below:

![](//mc.qcloudimg.com/static/img/b1df74884171a920e37940a17d2edac2/image.png)

## Message Organizing Format
Notification information is organized in JSON format and then placed in the HTTP POST protocol body. Please note that the ContentType of the POST format here is application/json instead of multipart/form-data. Therefore, do not use the function for reading form fields in PHP or Java to read information.

## Common Header Information
The following fields are included in all types of notification messages:

| Field name | Type | Description | Note | 
|------------|-------------|---------|---------|
| t           | string      | Validity period  |UNIX time stamp (decimal) |
| sign      | string     | Security signature  | MD5 (KEY+t) |
| event_type | int     | Event type   | Current available values:  0, 1, 100, 200  |
| stream_id | string     | LVB code   |  Indicating the LVB stream from which the event is derived  |
| channel_id | string     | LVB code  | The same as stream_id   |

- **stream_id | channel_id (LVB code)**
 In LVB code mode, the fields stream_id and channel_id have the same value. They have different names for historical reasons.

- **t (validity period)**
  The default validity period for notifications from Tencent Cloud is 10 minutes. If a notification has expired according to the specified t value, then the notification is considered expired. This prevents network replay attacks. The format of t is a decimal UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT).

- **sign (security signature)**
  <font color='blue'>sign = MD5(key + t) </font>: Tencent Cloud computes the value of "sign" using MD5 algorithm after concatenating the strings of the encryption key and t, then places the value in a notification. Upon receiving the notification, your backend server can verify whether the "sign" value is correct by using the same algorithm so as to check whether the notification is truly from Tencent Cloud backend.
	
	The encryption key here is CGI call key, which can be specified when you activate the LVB code service on the Tencent Cloud LVB console, as shown below:
![](//mc.qcloudimg.com/static/img/28a16dbab36fc3867301d2311204b8e4/image.png)

- **event_type (notification type)**
  Currently, Tencent Cloud supports three types of notifications: 0 - stream interruption; 1 - push; 100 - generation of a new recording file; 200 - generation of a new screenshot file.
	
## Different Types of Message Bodies
### (1) Push (0) Stream Interruption
**event_type = 0** indicates stream interruption, and **event_type = 1** indicates push. The message body also contains the following additional information: 

| Field Name  | Description |  Type     | Note | Required (Y/N) |
|-------------|-------------|--------------|-------------|--------------|
| appname | Push path   | string  || Y |
| app         | Push domain name  | string  || Y |
| update_time | Generation time of the message | int | In seconds | Y |
| sequence | Sequential number of the message which indicates a push event. Each push event generates push and stream interruption messages with the same sequential number | string || Y |
| node | Upload access point IP | String || Y |
| user_ip | User push IP | String | Client_ip | Y |
| errcode | Stream interruption error code | Int | | N |
| errmsg | Stream interruption error message | String | | N |
| stream_param | Parameter of push URL | String | | Y |
| push_duration | Duration of the push | String | In milliseconds | N |


Example: Tencent Cloud notifies that a stream interruption (event_type=0) occurred for the LVB stream (1234_15919131751).

```json
{
    "app": "3954.livepush.myqcloud.com", 
    "appname": "live",
    "channel_id": "16093425727656502238",
    "event_type": 0,
    "sign": "ab86d22870427e3f25bb1d9446b8f924", 
    "stream_id": "3954_ea88f7495ba711e6a2cba4dcbef5e35a", 
    "t": 1471256100,
    "event_time": 1471256200,
    "sequence": "5911795891871911817",
    "node":"123.10.1.1",
    "user_ip":"127.0.0.1",
    "errcode":0,
    "errmsg":"OK",
    "stream_param":""
}
```

#### Stream Interruption Error Codes
| Error Code | Error Description | Reason |
|---------|---------|---------|
| 1 | recv rtmp deleteStream | The VJ end actively interrupted the stream |
| 2 | recv rtmp closeStream | The VJ end actively interrupted the stream |
| 3 | recv() return 0 | The VJ end actively terminated the TCP connection |
| 4 | recv() return error | TCP connection exception at the VJ end |
| 7 | rtmp message large than 1M | Exception in received stream data |
| 18 | push url maybe invalid | Push authentication failed. Push rejected by the server
| 19 | 3rdparty auth failed | Third-party authentication failed. Push rejected by the server |
|Other error codes | Internal LVB service exceptions | To solve these errors, contact Tencent commercial personnel or submit a ticket. Tel: 4009-100-100 |


### (100) New Recording File
**event_type = 100** indicates that a new recorded file is generated. The message body contains the following additional information:

| Field Name  | Description        |  Type     | Note | Required (Y/N) |
|------------  |-------------|-------------|-------------|-------------|
| video_id  | vid | string      | vid used to locate a unique video file in VOD platform  | Y |
| video_url  | Download address | string      | Download address of the video  | Y |
| file_size  | File size | string       |  | Y |
| start_time | Starting time stamp of the part | int      | Start time (UNIX time stamp. The time cannot be accurate to seconds due to interference of the I frame position)  | Y |
| end_time | Ending time stamp of the part | int       | End time (UNIX time stamp. The time cannot be accurate to seconds due to interference of the I frame position)  | Y |
| file_id | file_id | string || Y |
| file_format | File format | string | flv, hls, mp4 | Y |
| vod2Flag | Indicates whether VOD 2.0 is enabled | Int | 0: No. 1: Yes | N |
| record_file_id | ID of recorded file | String | This field only exists when VOD 2.0 is enabled | N |
| duration | Duration of the push | Int | | Y |
| stream_param | Parameter of push URL | string |  | Y |

Example: A new recorded FLV part is generated, ID is 9192487266581821586, playback address is `http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv`.
```json
{
    "channel_id": "3891_@v_tls#3pfnm5fw35qt", 
    "end_time": 1471256054, 
    "event_type": 100, 
    "file_format": "flv", 
    "file_id": "16093425727657168197", 
    "file_size": 130938971, 
    "sign": "5c5e614ab58efc5a7ed6894dae22f471", 
    "start_time": 1471254513, 
    "stream_id": "3891_@v_tls#3pfnm5fw35qt", 
    "t": 1471256688, 
    "video_id": "200024424_a62017f6489748df9ee439360a8cc32c", 
    "video_url": "http://200024424.vod.myqcloud.com/200024424_a62017f6489748df9ee439360a8cc32c.f0.flv"
}
```

### (200) New Screenshot File 
**event_type = 200** indicates that a new screenshot picture is generated. The message body contains the following additional information:

| Field Name  | Description        |  Type     | Note | Required (Y/N) |
|-------------------|-------------|---------|-------------|-------------|
| pic_url        | Image address   | string      | Path without domain name | Y |
| create_time  | Time stamp of the screenshot | int           | Screenshot time stamp (UNIX time stamp. The time cannot be accurate to seconds due to interference of the I frame position) | Y |
| pic_full_url | Full path of the screenshot | String | Needs to include domain name | Y |

Example: The LVB stream "2016090090936" generated a new screenshot picture on Tencent Cloud:

```json
{
    "channel_id": "2016090090936", 
    "create_time": 1473645788, 
    "event_type": 200, 
    "pic_url": "/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg", //Path name of the file
    "sign": "8704a0297ab7fdd0d8d94f8cc285cbb7", 
    "stream_id": "2016090090936", 
    "t": 1473646392
}
```

>**Image download link**
>
> 1. Previously, you need to apply for COS service on your own when you enable the screenshot feature. The pic_url we returned to you is not the actual image download address, but a download path. The actual download address is generated by combining the followings:
> - Download prefix: `http://(cos_bucketname)-(cos_appid).file.myqcloud.com/`
> - Download path: "/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg"
> - Complete URL: `http://(cos_bucketname)-(cos_appid).file.myqcloud.com/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg`
> 
> **cos_appid and cos_bucketname are only available after you activate the [Cloud Object Storage](https://console.cloud.tencent.com/cos) in Tencent Cloud. Previously, you need to activate COS service on your own and bind the service to the LVB screenshot service before you can use screenshot feature. This approach is no longer applicable. Now you don't need to apply for COS service on your own. Currently, there are two approaches to activate screenshot feature. 1: Use the screenshot feature on the console; 2: Contact us to configure relevant information, then call the API to enable screenshot feature.**
>
> 2. You no longer need to enable COS service on your own, as we can now provide the complete URL address of the screenshot in a callback.
>  A complete image URL field is added in callback: pic_full_url, which helps you obtain the complete image URL. The original callback information fields are not changed in order not to affect original services (that is, the pic_url field still exists).
 
## Notification Reliability
Many customers are worried about message loss. For example, if a customer's server goes down for a while, will the messages be lost?
The message reliability guarantee mechanism in Tencent Cloud backend is implemented based on **simple retransmission**, that is, <font color='blue'>if a notification is not successfully sent to the specified callback URL, Tencent Cloud will retry for 3 times.</font> 

So how to tell if the message has been sent to your server successfully? This requires your assistance: When your server receives an HTTP event notification successfully, please make a reply as follows:

```json
// Return error code 0 in the HTTP request for which a message notification is received to indicate that the message is received successfully, so as to prevent Tencent Cloud from sending the notification repeatedly
{ "code":0 }
```

This indicates: "I (customer server) have received your notification. You (Tencent Cloud) should not keep sending the message to me."




