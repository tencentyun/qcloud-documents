### Non-interactive Broadcasting under LVB Code Mode and Supported Recording Options

The method for enabling non-interactive broadcasting  | The method for recording non-interactive broadcasting  | Multiple record formats |  Record callback | Convenience for development | Reliability | Resource consumption
:-----: | :-----: | :-----: |:-----: |:-----: | :-----:| :-----:
Automatic | Automatic |FLV/HLS/MP4|✔️|※※※※|※※※※|※
Manual | Automatic |FLV/HLS/MP4|✔️|※※※|※※※|※※
Automatic | Manual |MP4|❌|※※|※※|※※※
Manual | Manual |MP4|❌|※|※|※※※※

### 1. Automatic Non-interactive Broadcasting

#### 1.1 How to Enable

You can enable it in `Non-interactive Broadcasting Configuration` of ILBV console.

#### 1.2 Timing for Enabling Automatic Non-interactive Broadcasting:

* When a user successfully enables camera or screen sharing, the logic for enabling non-interactive broadcasting is triggered. This process is generally completed within 3 seconds.
* If you fail to enable non-interactive broadcasting, it can be re-enabled at the backend every 5 seconds. If the non-interactive broadcasting is enabled successfully, you can receive a notification sent via callback URL.
* Non-interactive broadcasting stops after a user exits room.

### 2. Manual Non-interactive Broadcasting

##### 2.1 Note on Manual Non-interactive Broadcasting

* If you enable the camera after joining audio/video room or if you start non-interactive broadcasting after enabling screen sharing, you need to stop non-interactive broadcasting before exiting the room on the client.
* Considering the Internet access, packet loss, latency and other incidents may occur on the network. Retry mechanism is required for enabling non-interactive broadcasting, and retry interval should be no less than 3 seconds.
* Note: Parameters such as room ID, VJ ID should be specified to ensure the corresponding relationship.
* You can choose whether to enable recording in the parameters of non-interactive broadcasting.

##### 2.2 SDK API for Starting Non-interactive Broadcasting

Android

```java
ILivePushOption option = new ILivePushOption()
        .encode(ILivePushOption.Encode.HLS)         // Protocol type of non-interactive broadcasting
        .recordFileType(ILivePushOption.RecordFileType.RECORD_HLS_FLV_MP4)      // Type of recorded file
        .channelName("Channel 1")                                   // Channel name (this is ignored under LVB code mode)
        .channelDesc("My channel");                               // Channel description (this is ignored under LVB code mode)
ILiveRoomManager.getInstance().startPushStream(option, new ILiveCallBack<ILivePushRes>() {
    @Override
    public void onSuccess(ILivePushRes data) {
        iPushId = data.getChnlId();
        Log.d("PUSH_DBG", "startPush->success id: "+data.getChnlId());
        if (null != data.getUrls()){
            // Print push type and address
            for (ILivePushUrl url : data.getUrls()){
                Log.d("PUSH_DBG", "type:"+url.getEncode()+", "+url.getRateType()+":"+url.getUrl());
            }
        }
    }

    @Override
    public void onError(String module, int errCode, String errMsg) {
        Log.d("PUSH_DBG", "startPush->failed:"+module+"|"+errCode+"|"+errMsg);
    }
});
```
iOS

```c++
ILivePushOption *option = [[ILivePushOption alloc] init];
ILiveChannelInfo *info = [[ILiveChannelInfo alloc] init];
info.channelName = @"Test channel"; //This is ignored under LVB code mode
info.channelDesc = @"My channel description"; //Channel description (this is ignored under LVB code mode)
option.channelInfo = info;
option.encodeType = AV_ENCODE_HLS;
option.recrodFileType = AV_RECORD_FILE_TYPE_HLS;

[[ILiveRoomManager getInstance] startPushStream:option succ:^(id selfPtr) {
    AVStreamerResp *resp = (AVStreamerResp *)selfPtr;
    NSLog(@"Push is successful %@", [resp urls]);
    NSLog(@"Channel ID obtained from push: %llu", resp.channelID)
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"Push failed");
}];
```

PC

```c++
void OnStartPushStreamSuc( TIMStreamRsp& value, void* data )
{
	//Push started successfully
	m_channelId = value.channel_id;//Channel ID, which is used when stopping push
	m_pushUrls = value.urls;//Push URL
}

void OnStartPushStreamErr( int code, const std::string& desc, void* data )
{
	//Failed to start push
}

iLivePushOption pushOpt;
pushOpt.channel_name = channelName; //This is ignored under LVB code mode
pushOpt.channel_desc = channelDesc; //This is ignored under LVB code mode
pushOpt.push_data_type = (E_PushDataType)pushDataType;
pushOpt.encode = (imcore::E_TIMStreamEncode)encode;
iLiveRoomMgr::getInstance()->startPushStream( pushOpt, OnStartPushStreamSuc, OnStartPushStreamErr, NULL );
```

##### 2.3 SDK API for Stopping Non-interactive Broadcasting

Android

```java
ILiveRoomManager.getInstance().stopPushStream(iPushId, new ILiveCallBack() {
    @Override
    public void onSuccess(Object data) {
        Log.d("PUSH_DBG", "stopPush->success");
    }

    @Override
    public void onError(String module, int errCode, String errMsg) {
        Log.d("PUSH_DBG", "stopPush->failed:"+module+"|"+errCode+"|"+errMsg);
    }
});
```
iOS

```c++
//  pushID is the channel ID returned in startPushStream
NSArray *chids = @[(pushID)];
[[ILiveRoomManager getInstance] stopPushStreams:chids succ:^{
    NSLog(@"Push stopped successfully");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"Failed to stop push");
}];
```

PC

```c++
void OnStopPushStreamSuc( void* data )
{
	//Push stopped successfully
}

void OnStopPushStreamErr( int code, const std::string& desc, void* data )
{
	//Failed to stop push
}

iLiveRoomMgr::getInstance()->stopPushStream(m_channelId, OnStopPushStreamSuc, OnStopPushStreamErr, NULL);
```

### 3. Change in the Method for Constructing Playback URL

#### 3.1 Rule for Calculating LVB Code:<br/>

* LVB Code=**`BIZID_MD5 (Room ID_User ID_Data Type)`**.<br/>
* String is encoded using UTF-8 during transmission. Data types of camera and screen sharing are main and aux respectively. BIZID is a fixed parameter, which can be found on the top of LVB console.<br/>
* If BIZID=8888, user ID=14y2l2c, room ID=293710 and camera sharing is enabled, `MD5(293710_14y2l2c_main)=81265058829fd2e50c8ec2ac78d55127`. So the LVB code is `8888_81265058829fd2e50c8ec2ac78d55127`.

#### 3.2. Rule for Constructing Playback URL

* Playback URL=<font color='blue'>`Transmission protocol://BIZID.liveplay.myqcloud.com/live/LVB code[.format]`</font>
* According to the above example, the playback URLs in three formats are as follows:<br/>
rtmp:`rtmp://8888.liveplay.myqcloud.com/live/8888_81265058829fd2e50c8ec2ac78d55127`<br/>
flv:  `http://8888.liveplay.myqcloud.com/live/8888_81265058829fd2e50c8ec2ac78d55127.flv`<br/>
hls:`http://8888.liveplay.myqcloud.com/live/8888_81265058829fd2e50c8ec2ac78d55127.m3u8`<br/>
* We strongly recommend**<font color='blue'> you to construct playback URL at the backend, and send it to the client</font>**. In this way, it is easy for you to cope with any changes in playback URL rules.

### 4. Non-interactive Broadcasting Event Server Callback Notification

For more information about the parameter format and response solution of callback event, please see appendix.

#### Two event_type can be received by non-interactive broadcasting.** 0**: Non-interactive broadcasting is interrupted; **1**: Non-interactive broadcasting starts, and the following information are added in the message body:

| Field name  | Type        | Description        |
|-------------|-------------|--------------|
| appname | string      | Push path  |
| app         | string      | Push domain name  |
| appid | integer | User ID |

Example: Tencent Cloud notifies that a stream interruption (event_type=0) occurred for the LVB stream (1234_15919131751).

```json
{
    "app": "1234.livepush.myqcloud.com",
    "appid": 1251659802,
    "appname": "live",
    "channel_id": "1234_15919131751",
    "errorcode": 0,
    "event_time": 1484033909,
    "event_type": 0,
    "node": "123.126.122.22",
    "sequence": "2480768755672606517",
    "sign": "fef79a097458ed80b5f5574cbc13e1fd",
    "stream_id": "1234_15919131751",
    "t": 1473126233
    "user_ip": "123.112.131.123"
}
```

====================================================================

### Appendix

### 1. Parameter Format of Callback Event

## Message Organizing Format

Notification information is organized in JSON format and then placed in the HTTP POST protocol body.<br/>
Please note that the ContentType of the POST format here is application/json instead of multipart/form-data. Therefore, do not use the function for reading form fields in PHP or Java to read information.

#### Common Header Information

The following fields are included in all types of notification messages:

| Field name | Type | Description | Note |
|------------|-------------|---------|---------|
| t           | string      | Valid time  |UNIX timestamp (decimal) |
| sign      | string     | Security signature  | MD5 (KEY+t) |
| event_type | int     | Event type   | Current available values:  0, 1, 100, 200  |
| stream_id | string     | LVB code   |  Indicating the LVB stream from which the event is derived  |
| channel_id | string     | LVB code  | The same as stream_id   |

- **stream_id | channel_id (LVB code)**
 In LVB code mode, the fields stream_id and channel_id have the same value. They have different names for historical reasons.

- **t (expiration time)**
  The default expiration time for notifications from Tencent Cloud is 10 minutes. If a notification has expired according to the specified t value, then the notification is considered expired. This prevents network replay attacks. The format of t is a decimal UNIX timestamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT).

- **sign (security signature)**
  <font color='blue'>sign = MD5(key + t) </font>: Tencent Cloud computes the value of "sign" using MD5 algorithm after constructing the strings of the API authentication key and t, then places the value in a notification. Upon receiving the notification, your backend server can verify whether the "sign" value is correct by using the same algorithm so as to check whether the notification is truly from Tencent Cloud backend.

- **event_type (notification type)**
  Currently, Tencent Cloud supports three types of notifications: 0 - Stream interruption; 1 - Push; 100 - Generation of a new recorded file; 200 - Generation of a new screenshot file.

### 2. Response Method of Callback URL

Many customers are worried about message loss. For example, if a customer's server goes down for a while, will the messages be lost?<br/>
The message reliability guarantee mechanism in Tencent Cloud backend is implemented based on **simple retransmission**, that is, <br/>
<font color='blue'>if a notification is not successfully sent to the specified callback URL, Tencent Cloud may retry many times.</font>

So how to tell if the message has been sent to your server successfully? This requires your assistance: When your server receives an HTTP event notification successfully, please make a reply as follows: Status code 200, indicating that the message is received successfully, so as to prevent Tencent Cloud from sending the notification repeatedly.

This indicates: "I (customer server) have received your notification. You (Tencent Cloud) should not keep sending the message to me."

If Tencent Cloud does not receive the correct response packet, it may retry the logic for notification once per minute, with a maximum of 10 retries.
