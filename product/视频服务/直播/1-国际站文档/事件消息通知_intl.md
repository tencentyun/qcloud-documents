## Feature Description
Events such as state change of an LVB stream, generation of a new recording file and generation of a screenshot file are internally managed in Tencent Cloud. But your backend server may also need to be informed of these events, in which case you can use the event notification service of Tencent Cloud to obtain these events.

You can register a callback URL from your backend server in Tencent Cloud console. When an event occurs, Tencent Cloud will deliver the event to your server using the HTTP POST method, with the event content organized in JSON format.

## Configuring a URL
When you enable the LVB Code mode in the **[LVB Console](https://console.cloud.tencent.com/live/livecodemanage)** -> **LVB Code Access** -> **Access Configuration**, you can specify a URL for receiving Tencent Cloud notifications, as shown below:
![](/https://main.qcloudimg.com/raw/e980e533a7c7f2e60c772373c0e369fc.png)

## Message Organizing Format
Notification messages are organized in JSON format and then placed in the HTTP POST protocol body. Note that the ContentType of the POST format here is application/json instead of multipart/form-data. Therefore, do not use the function for reading form fields in PHP or Java to read the messages.

## Common Header Information
The following fields are included in all types of notification messages:

| Field Name | Type | Description | Note | 
|------------|-------------|---------|---------|
| t           | string      | Validity period | UNIX timestamp (decimal) |
| sign      | string     | Security signature | MD5(KEY+t) |
| event_type | int     | Event type | Current available values: 0, 1, 100, 200 |
| stream_id | string     | LVB Code | Indicates the LVB stream from which the event is derived |
| channel_id | string     | LVB Code | Same as stream_id |

- **stream_id | channel_id (LVB Code)**
 In the LVB Code mode, the fields stream_id and channel_id have the same value. They have different names due to historical reasons.
- **t (expiration time)**
  The default expiration time of notifications from Tencent Cloud is 10 minutes. If the time specified by t in a notification has expired, the notification is invalid, which can prevent network replay attacks. The format of t is a decimal UNIX timestamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT).
- **sign (security signature)**
sign = MD5(key + t): Tencent Cloud computes the value of "sign" using MD5 algorithm after concatenating the strings of the encryption key and t, then places the value in a notification. Upon receiving the notification, your backend server can verify whether the "sign" value is correct by using the same algorithm so as to check whether the notification is truly from Tencent Cloud backend.
The encryption key here is the CGI call key, which can be specified when you activate the LVB Code service on the Tencent Cloud LVB console, as shown below:
![](https://main.qcloudimg.com/raw/576b8911b8661d4d9e22ef145e3368ad.png)
- **event_type (notification type)**
  Tencent Cloud supports the following types of notifications: 0 - Stream interruption; 1 - Push; 100 - Generation of a new recording file; 200 - Generation of a new screenshot file.
	
## Different Types of Message Bodies
### (1) Push (0) Stream Interruption
**event_type = 0** indicates stream interruption, and **event_type = 1** indicates push. These types of message bodies also contain the following information: 

| Field Name | Description | Type | Note | Required |
|-------------|-------------|--------------|-------------|--------------|
| appname | Push path | string  ||Y|
| app | Push domain name | string  ||Y|
|event_time|Generation time of the message |int|In second |Y|
|sequence|Sequence number of the message, which indicates a push event. A push event generates push and stream interruption messages with the same sequence number |string||Y|
|node	|Upload access point IP |String||	Y|
|user_ip	|User push IP |	String	|Client_ip	|Y|
|errcode	|Stream interruption error code |Int	|	|N|
|errmsg	|Stream interruption error message |String	|	|N|
|stream_param	|Push URL parameter |	String	|	|Y|
|push_duration| Duration of the push |	String	|In millisecond |N|


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

#### Stream interruption error codes
| Error Code | Error Description | Reason |
|---------|---------|---------|
|1|	recv rtmp deleteStream|	Active interruption at the VJ end |
|2|	recv rtmp closeStream	|Active interruption at the VJ end |
|3|	recv() return 0	|Active TCP disconnection at the VJ end | 
|4	|recv() return error	|TCP connection exception at the VJ end |
|7|	rtmp message large than 1M |	Exception in received stream data |
| Other error codes | Internal LVB service exceptions | To solve these errors, contact Tencent's service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100 |


### (100) New recording file
**event_type = 100** indicates that a new recording file is generated. This type of message body also contains the following information:

| Field Name  | Description        |  Type     | Note | Required |
|------------  |-------------|-------------|-------------|-------------|
| video_id  | vid | string      | VID for VOD. It can be used to locate a unique video file on the VOD platform  |Y|
| video_url  |Download address | string      | Download address of a VOD video  | Y|
| file_size  |File size | string       |  | Y|
| start_time |Starting time stamp of the part | int      | Start time (UNIX timestamp. The time cannot be accurate to seconds due to interference of the I frame position)  |Y|
| end_time |Ending time stamp of the part | int       | End time (UNIX timestamp. The time cannot be accurate to seconds due to interference of the I frame position)  |Y|
|file_id|file_id	|string||	Y|
|file_format	|File format	|string|	flv, hls, mp4	|Y|
|vod2Flag	|Indicates whether VOD 2.0 is enabled |Int	|0: Disabled; 1: Enabled |	N|
|record_file_id	|ID of the recording file |	String|	This field only exists when VOD 2.0 is enabled |	N|
|duration	|Duration of the push	|Int	|	|Y|
|stream_param|	Push URL parameter |	string|		|Y|

Example: A new FLV recording part is generated with the ID of 9192487266581821586. The playback address is `http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv`.
```json
{
  "appid": 1252033264,
   "channel_id": "2519_2500647",
   "duration": 272,
  "end_time": 1496220894,
  "event_type": 100,
  "file_format": "flv",
  "file_id": "9031868222958931071",
  "file_size": 30045521,
  "record_file_id": "9031868222958931071",
  "sign": "c2e3bdc344ddb62ab05229d01672a79e",
  "start_time": 1496220622,
  "stream_id": "2519_2500647",
  "stream_param":      "bizid=2519&record=hls|flv&txSecret=d5569fb19d1e858bf683b30c10dec908&txTime=592FBDD9&mix=layer:b;session_id:709036962551160107;t_id:1",
  "t": 1496221502,
  "video_id": "200011683_481565e0befe4e44903839aebe370ef6",
  "video_url": "http://1252033264.vod2.myqcloud.com/d7a4cabbvodgzp1252033264/0257ade99031868222958931071/f0.flv"
}
```

### (200) New screenshot file 
**event_type = 200** indicates that a new screenshot image is generated. This type of message body also contains the following information:

| Field Name  | Description        |  Type     | Note | Required |
|-------------------|-------------|---------|-------------|-------------|
| pic_url        | Image address   | string      | Path without the domain name |Y|
| create_time  | Time stamp of the screenshot | int           | Screenshot timestamp (UNIX timestamp. The time cannot be accurate to seconds due to interference of the I frame position) |Y|
|pic_full_url|	Full path of the screenshot |	String|	The domain name needs to be included	|Y|

Example: The LVB stream "2016090090936" generated a new screenshot image on Tencent Cloud:

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

>**Image download address:**
> 1. Previously, you needed to apply for the COS service to enable the screenshot feature, and the pic_url we returned to you was not the actual image download address but a download path. The actual download address was generated by combining the following:
> - Download prefix: `http://(cos_bucketname)-(cos_appid).file.myqcloud.com/`
> - Download path: `/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg`
> - Complete URL: `http://(cos_bucketname)-(cos_appid).file.myqcloud.com/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg`
> 
> cos_appid and cos_bucketname are only available after you activate [Cloud Object Storage](https://console.cloud.tencent.com/cos) on Tencent Cloud. Previously, you could only use the screenshot feature after activating the COS service and binding it to the LVB screenshot service. Now, you can use the feature without applying for the COS service. You can activate the screenshot feature in the console, or by calling related API after contacting us to configure relevant information.
> 2. Now, you don't need to activate the COS service, and we can call back the complete screenshot URL to you with an additional complete image URL field of `pic_full_url`so that you can directly get the complete image URL. In order not to affect the original business, the original callback information fields will remain unchanged (that is, the field pic_url still exists).
 
## Notification Reliability
Many customers are worried about message loss. For example, if a customer's server goes down for a while, will the messages be lost?
The message reliability guarantee mechanism of Tencent Cloud backend is implemented based on simple retransmission, that is, if a notification is not successfully sent to the specified callback URL, Tencent Cloud will retry 3 times with an interval of 60 seconds.
So how to tell if the message has been sent to your server successfully? This requires your assistance: When your server receives an HTTP event notification successfully, please make a reply as follows:
```
json
// Return error code 0 in the HTTP request for which a message notification is received to indicate that the message is received successfully, so as to prevent Tencent Cloud from sending the notification repeatedly
{ "code":0 }
```

This indicates: "I (customer server) have received your notification. You (Tencent Cloud) should not keep sending the message to me."




