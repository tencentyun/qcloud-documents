ILVB SDK1.4 provides non-interactive broadcasting feature, and with Tencent Cloud LVB service, the distribution of LVB based on HLS, RTMP can be implemented. You can use the non-interactive broadcasting feature only after the Tencent Cloud LVB service is activated.

Here's the non-interactive broadcasting feature development guide:

## 1 Timing Diagram
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/hudongzhibolz-2.png)

## 2. Start Non-interactive Broadcasting

### 2.1 Android Platform

Prototype:

```
public void requestMultiVideoStreamerStart(TIMAvManager.RoomInfo roomInfo,
                                           TIMAvManager.StreamParam streamParam,
                                           TIMValueCallBack<TIMAvManager.StreamRes> cb)

```

Initiate request for starting non-interactive broadcasting

Parameters:


```
roomInfo - Relevant information of non-interactive broadcasting room. For more information, please see TIMAvManager.RoomInfo
streamParam - Relevant parameter of non-interactive broadcasting. For more information, please see TIMAvManager.StreamParam
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
　　//If you directly print the data for review, streamRes.getChnlId() is displayed as a negative value, so you should perform transcoding if needed. This value can be used directly without the need to transcode when the push ends.
　　Long num = streamRes.getChnlId();
　　BigInteger unsignedNum = BigInteger.valueOf(num); 
	if(num < 0) unsignedNum = unsignedNum.add(BigInteger.ZERO.flipBit(64));
    	Log.d(tag, "create channel succ. channelid: " + unsignedNum
               	+ ", addr size " + streamRes.getUrls().size());
    	}
	});

```

>Note: One user can only initiate one channel of LVB at a time during non-interactive broadcasting. If there is one channel of LVB in process, when you initiate request repeatedly, a massage indicating an error occurs in the LVB channel is returned.

### 2.2 iOS Platform

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
   NSString *playerPassword;     Password configured for receiver's player
}
AVStreamInfo {
   AVEncodeType encodeType;    Encoding type
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

### 2.3 Windows Platform

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
cb - Shared URL list returned in onSuccess parameter

struct TIMRoomInfo
{
	TIMRoomInfo():relation_id(0), room_id(0) {}
	int relation_id; // Discussion group ID
	int room_id;	 // Room number
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
	uint32_t	push_data_type; //Data type of push: 0: Camera video; 1: Sub stream 
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

>Note: One user can only initiate one channel of LVB at a time during non-interactive broadcasting. If there is one channel of LVB in process, when you initiate request repeatedly, a massage indicating an error occurs in the LVB channel is returned.

## 3. Stop Non-interactive Broadcasting

### 3.1 Android Platform

Prototype:

```
public void requestMultiVideoStreamerStop(TIMAvManager.RoomInfo roomInfo,
                                          java.util.List<java.lang.Long> channelIDs,
                                          TIMCallBack cb)
```

Initiate request for stopping non-interactive broadcasting

Parameters:

```
roomInfo - Relevant information of non-interactive broadcasting room. For more information, please see TIMAvManager.RoomInfo
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


### 3.2 iOS Platform

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

### 3.3 Windows Platform

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

Non-interactive broadcasting is initiated through ILVB SDK. The distribution of LVB is implemented using Tencent Cloud LVB service.

(1) Users can directly access LVB console http://console.cloud.tencent.com/live for management
(2) Users can also manage files using LVB API. Here is how to use API:
https://cloud.tencent.com/doc/api/258/4703

## 5 Price and Billing
Non-interactive broadcasting is not a free service. The specific billing rules are the same with that of Tencent Cloud LVB service. For more information, please see:
https://cloud.tencent.com/doc/product/268/5129#1..E6.97.81.E8.B7.AF.E7.9B.B4.E6.92.AD.E8.AE.A1.E8.B4.B9

Please note that, if you have activated the LVB service and selected the package and one of the postpaid billing methods, the selected billing method is adopted. If you have not activated the LVB service, the pay-by-traffic billing method (postpaid) is used by default.

## 6 Notes

(1) Recording feature is not supported for one-on-one audio/video room
(2) The current version does not support the combining or mixing of multi-channel uplink videos

## 7 Error Codes

40000000-40000099: An error occurred while resolving client's push request packet
40000200-40000299: An error occurred while requesting push server
40000300-40000399: An error occurred while resolving push server response packet
40000400-40000499: An error occurred while requesting push server
