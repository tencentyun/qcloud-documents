Non-interactive broadcasting is available as of ILVB SDK1.4. Combined with Tencent Cloud LVB service, it allows the live broadcasting streaming based on HLS and RTMP. You can use the non-interactive broadcasting feature only after the Tencent Cloud LVB service is activated.

The following is the non-interactive broadcasting development guide:

## 1 Timing Diagram
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/hudongzhibolz-2.png)

## 2. Start Non-interactive Broadcasting

### 2.1 Android

Prototype:

```
public void requestMultiVideoStreamerStart(TIMAvManager.RoomInfo roomInfo,
                                           TIMAvManager.StreamParam streamParam,
                                           TIMValueCallBack<TIMAvManager.StreamRes> cb)

```

Initiate request for starting non-interactive broadcasting

Parameters:


```
roomInfo - Information of non-interactive broadcasting room. For more information, please see TIMAvManager.RoomInfo
streamParam - Parameter of non-interactive broadcasting. For more information, please see TIMAvManager.StreamParam
cb - Callback. Channel ID and playback URL are returned in onSuccess. For more information, please see TIMAvManager.StreamRes
```

Example:

```
TIMAvManager.getInstance().requestMultiVideoStreamerStart(roomInfo,
                    streamParam, new TIMValueCallBack<TIMAvManager.StreamRes>() {
	@Override
	public void onError(int code, String desc) {
    	Log.d(tag, "create channel failed. code " + code + ", descr " + desc);
	}

	@Override
	public void onSuccess(TIMAvManager.StreamRes streamRes) {
    	Log.d(tag, "create channel succ. channelid: " + streamRes.getChnlId()
               	+ ", addr size " + streamRes.getUrls().size());
    	}
	});
```

>Note: In none-interactive broadcasting, a user can only initiate one-channel broadcasting at a time. If there is already a channel in the process of broadcasting when the user initiates a request, an error message indicating a LVB channel already exits is returned.

### 2.2 iOS

Prototype:

```
/**
*  Send request for creating LVB channel to start non-interactive broadcasting
*
* @param roomInfo Room information
* @param streamInfo LVB channel information
* @param succ Callback is successful
* @param fail Callback failed. Error code is returned
*
*  @return 0 Packet sent successfully
*/
- (int)requestMultiVideoStreamerStart:(OMAVRoomInfo *)roomInfo 
                      streamInfo:(AVStreamInfo *)streamInfo 
                         okBlock:(OMMultiVideoStreamerStartSucc)succ 
                         errBlock:(OMMultiFail)fail;

@end
```

Parameter Description:


```
roomInfo Audio/video room information
streamInfo Non-interactive broadcasting parameter
succ Callback is successful. Channel ID and URL (NSString) list are returned
fail Callback failed. Error code and error massage are returned. For more information, please see Error Codes.
OMAVRoomInfo {
   Uint32 relationId;    Group ID
   Uint32 roomId;      Room ID
}
LVBChannelInfo {
   NSString *channelName;      Name of LVB channel
   NSString *channelDescribe;    Description of LVB channel
   NSString *playerPassword;     Password set for receiver's player
}
AVStreamInfo {
   AVEncodeType encodeType;    Encoding format
   AVSDKType avSdkType;         SDK business type
   LVBChannelInfo *channelInfo;   Channel information
}
AVStreamerResp {
   Uint64 channelID;    Channel ID
   NSArray *urls;        URL list
}
```

Returned value:

0 indicates that the data has been successfully sent

Example:


```
[[IMSdkInt sharedInstance] 
 requestMultiVideoStreamerStart:(OMAVRoomInfo *)roomInfo 
                      streamInfo:(AVStreamInfo *)streamInfo 
                         okBlock:(AVStreamerResp *rsp) {
   NSLog(@"create LVBChannel succ:channelID=%@", rsp.channelID);
   for (NSString *url in rsp.urls) {
     NSLog(@"LVBChannel url=%@", url);
   } 
 }
                         errBlock:^(int code, NSString *err) {
     NSLog(@"create LVBChannel failed:code=%d err=%@", code, err);
}];
```

### 2.3 Windows

Prototype:


```
void RequestMultiVideoStreamerStart(const TIMRoomInfo& room_info, 
const TIMStreamParam& para, TIMValueCallBack<TIMStreamRsp&> *cb); 
```

Initiate request for starting non-interactive broadcasting

Parameter:


```
room_info - Room information
para - Non-interactive broadcasting parameter
cb - URL list for sharing returned in onSuccess parameter

struct TIMRoomInfo
{
	TIMRoomInfo():relation_id(0), room_id(0) {}
	int relation_id; // Discussion group ID
	int room_id;	 // Room ID
};
relation_id - Discussion group ID
struct TIMStreamParam
{
	TIMStreamParam()
		:encode(HLS), sdk_type(SDKType_Normal), push_data_type(0){}
	E_TIMStreamEncode encode;
	E_TIMSDKType sdk_type;
	std::string channel_name;
	std::string channel_desc;
	std::string channel_password;
	uint32_t	push_data_type; //Push data type 0: Camera 1: Sub-stream 
};
};
```

Example:


```
//Create callback
class DemoReqMutilStreamStartCB :public TIMValueCallBack < TIMStreamRsp& >
{
	void OnSuccess(TIMStreamRsp& value) override
	{
		delete this;
	}
	void OnError(int code, const std::string &desc) override
	{
		delete this;
	}
};
//Start push
void DemoRequestMutli()
{
	AVPre();				 //prepare
	TIMRoomInfo room_info;
	room_info.relation_id = 15000; //relation id used when creating room
	room_info.room_id = 0; //room id returned when creating room
	TIMStreamParam stream_para;
	stream_para.encode = HLS;
	TIMIntManager::get().RequestMultiVideoStreamerStart(room_info, stream_para, new DemoReqMutilStreamStartCB);
	SLEEP(5);
}
```

>Note: In none-interactive broadcasting, a user can only initiate one-channel broadcasting at a time. If there is already a channel in the process of broadcasting when the user initiates a request, an error message indicating a LVB channel already exits is returned.

## 3. Stop Non-interactive Broadcasting

### 3.1 Android

Prototype:

```
public void requestMultiVideoStreamerStop(TIMAvManager.RoomInfo roomInfo,
                                          java.util.List<java.lang.Long> channelIDs,
                                          TIMCallBack cb)
```

Initiate request for stopping non-interactive broadcasting

Parameters:

```
roomInfo - Information of non-interactive broadcasting room. For more information, please see TIMAvManager.RoomInfo
channelIDs - Set of IDs of channels to be closed
cb - Callback
```

Example:


```
TIMAvManager.getInstance().requestMultiVideoStreamerStop(roomInfo,
        ids, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
        Log.d(tag, "stop channel failed. code " + code + ", descr " + desc);
    }

    @Override
    public void onSuccess() {
        Log.d(tag, "stop channel succ");
    }
});
```


### 3.2 iOS

Prototype:


```
/**
*  Send request for closing LVB channel to stop non-interactive broadcasting
*
* @param roomInfo Room information
* @param channelIDs Channel ID (NSString) list
* @param succ Callback is successful
* @param fail Callback failed. Error code is returned
*
*  @return 0 Packet sent successfully
*/
- (int) requestMultiVideoStreamerStop:(OMAVRoomInfo *)roomInfo 
                          channelIDs:(NSArray *)channelIDs 
                             okBlock:(OMMultiSucc)succ 
                             errBlock:(OMMultiFail)fail;
@end
```

Parameter Description:


```
roomInfo Audio/video room information
channelIDs Channel ID (NSString) list
succ Callback is successful
fail Callback failed. Error code and error massage are returned. For more information, please see Error Codes.
```

Returned value:

0 indicates that the data has been successfully sent

Example:


```
[[IMSdkInt sharedInstance] 
  requestMultiVideoStreamerStop:(OMAVRoomInfo *)roomInfo 
                      channelIDs:(NSArray *)channelIDs
                         okBlock:^{
    NSLog(@"stop LVBChannel succ");
} 
                     errBlock:^(int code, NSString *err) {
    NSLog(@"stop LVBChannel failed:code=%d err=%@", code, err);
}];
```

### 3.3 Windows

Prototype: 

```
 void RequestMultiVideoStreamerStop(const TIMRoomInfo& room_info, const 
TIMStreamParam& para, const std::list<uint64_t>& channel_ids, TIMCallBack *cb); 
```

Initiate request for stopping non-interactive broadcasting

Parameter:

```
room_info			Room information
para				Non-interactive broadcasting parameter
channel_ids		channel_id returned in RequestMultiVideoStreamerStart
param cb			Callback response
```

Example:


```
//Create callback
class DemoReqMutilStreamStopCB : public TIMCallBack
{
	void OnSuccess() override
	{
		delete this;
	}
	void OnError(int code, const std::string &desc) override
	{
		delete this;
	}
};
//End Push
void DemoRequestMutli()
{
	AVPre();				 //prepare
	TIMRoomInfo room_info;
	room_info.relation_id = 15000; //relation id used when creating room
	room_info.room_id = 0; //room id returned when creating room
	TIMStreamParam stream_para;
	stream_para.encode = HLS;
	std::list<uint64_t> channel_ids;
	channel_ids.push_back(1000); //Enter actual channel_id here
	TIMIntManager::get().RequestMultiVideoStreamerStop(room_info, stream_para, channel_ids, new DemoReqMutilStreamStopCB);
	SLEEP(5);
}
```

## 4 LVB Management

Non-interactive broadcasting is initiated through ILVB SDK. Live broadcasting streaming is implemented using Tencent Cloud LVB service.

(1) Users can access LVB console http://console.cloud.tencent.com/live for management
(2) Users can also perform management-related operations using LVB APIs. For more information on how to use the APIs, please see:
http://cloud.tencent.com/wiki/直播API

## 5 Price and Billing
Non-interactive broadcasting is a paid service, with the same billing method as that of Tencent Cloud LVB service. For more information, please see:
http://cloud.tencent.com/wiki/腾讯云直播价格与计费说明

Please note that if you have activated the LVB service and selected the package and one of the postpaid billing methods, the selected billing method is adopted. If you have not activated the LVB service, the pay-by-traffic billing method (postpaid) is used by default.

## 6 Notes

(1) Recording feature is not supported for one-on-one audio/video room
(2) The current version does not support the merging or mixing of multi-channel upstream videos

## 7 Error Codes

40000000-40000099: An error occurred while resolving client's push request packet
40000200-40000299: An error occurred while requesting push server
40000300-40000399: An error occurred while resolving response packet from push server
40000400-40000499: An error occurred while requesting push server
