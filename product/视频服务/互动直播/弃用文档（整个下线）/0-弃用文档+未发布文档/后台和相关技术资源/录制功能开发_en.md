ILVB SDK1.3 provides video recording feature. Users can use this feature by calling relevant API. Recorded files are stored in VOD service provided by Tencent Cloud. Users can perform operations such as management, transcoding and distribution on these files using VOD console and APIs.

You can use the recording feature only after the Tencent Cloud VOD service is activated.

Here's the recording feature development guide:

## 1 Timing Diagram
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/hudongzhibolz-1.png)

## 2 Start Recording

### 2.1 Android Platform

Prototype:

```
public void requestMultiVideoRecorderStart(TIMAvManager.RoomInfo roomInfo,
                                           TIMAvManager.RecordParam param,
                                           TIMCallBack cb)
```

Initiate the request for starting recording

Parameters:

```
roomInfo - Relevant information of recording room. For more information, please see TIMAvManager.RoomInfo
param - Recording parameters. For more information, please see TIMAvManager.RecordParam
cb - Callback
```

Example:

```
TIMAvManager.getInstance().requestMultiVideoRecorderStart(roomInfo, param,  new TIMCallBack(){

    @Override
    public void onError(int code, String desc) {
        // TODO Auto-generated method stub
        Log.e(tag, "Recorder start failed: " + code + " desc " + desc);
    }

    @Override
    public void onSuccess() {
        // TODO Auto-generated method stub
        Log.d(tag, "Recorder start succ");
    }

});
```

>Note: You can only initiate request for one-channel recording at a time when recording video of the same user.


### 2.2 iOS Platform

Prototype:
 
```
 */**
  * Send request for starting recording

  * @param roomInfo Room information
  * @paramrecordInfo Parameters of recording request
  * @param succ Callback is successful
  * @param fail Callback failed. Error code is returned
  *
  *@return 0 Packet sent successfully
  */
- (int)requestMultiVideoRecorderStart:(OMAVRoomInfo *)roomInfo 
recordInfo:(AVRecordInfo *)recordInfo 
okBlock:(OMMultiSucc)succ 
errBlock:(OMMultiFail)fail;

  @end
```

Parameter Description:


```
roomInfo Audio/video room information
recordInfo Recording parameter
succ Callback is successful
fail Callback failed. Error code and error massage are returned. For more information, please see Error Codes.
OMAVRoomInfo {
  Uint32 relationId;    Group ID
  Uint32 roomId;      Room ID
}
AVRecordInfo {
  NSString *fileName;    Name of recorded file
  NSArray *tags;		List of video tags (NSString)
  UInt32 classId;		Video category ID
  AVSDKType avSdkType;		SDK business type
  BOOL isTransCode;		Whether to transcode
  BOOL isScreenShot;		Whether to take screenshot
  BOOL isWaterMark;		Whether to add watermark
}
```

Returned value:

0 indicates that the data has been successfully sent

Example:

```
[[IMSdkInt sharedInstance] 
requestMultiVideoRecorderStart:(OMAVRoomInfo *)roomInfo 
recordInfo:(AVRecordInfo *)recordInfo 
okBlock:^{
NSLog(@"start recordersucc");
}
errBlock:^(int code, NSString *err) {
NSLog(@"start recorder failed:code=%d err=%@", code, err);
}];
```

>Note: You can only initiate request for one-channel recording at a time when recording video of the same user.


### 2.3 Windows Platform

Prototype:

```
void RequestMultiVideoRecorderStart(const TIMRoomInfo& room_info, const 
TIMRecordParam& para, TIMCallBack* cb);     

```

Initiate request for starting push

Parameter:

```
room_info - Room information
para - Recording parameter
cb - Shared URL list returned in onSuccess parameter

struct TIMRoomInfo
{
	TIMRoomInfo():relation_id(0), room_id(0) {}
	int relation_id; // Discussion group ID
	int room_id;	 // Room ID
};
relation_id - Discussion group ID
room_id - Room ID

struct TIMStreamParam
{
		TIMRecordParam()
		:class_id(0)
		, is_transcode(false)
		, is_screenshot(false)
		, is_watermark(false)
		, sdk_type(SDKType_Normal)
		, record_data_type(0){}
	std::string filename;				//Name of recorded file
	int class_id;				 		//Category ID of the video
	bool is_transcode;					//Whether to transcode
	bool is_screenshot;				 	//Whether to take screenshot
	bool is_watermark;					//Whether to add watermark
	std::list<std::string> tags;	 	//List of tags of the video
	E_TIMSDKType	sdk_type;
	uint32_t		record_data_type; //Data type of recording: 0: Camera video; 1: Sub stream
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

>Note: You can only initiate request for one-channel push at a time when pushing stream to the same user. If there is one-channel push in the process of LVB, when you initiate request repeatedly, a massage indicating an error occurred in the push channel is returned.

### 2.4 Web Platform
Prototype:
                              
```
StartRecordVideo(videotype, filename, classid,transcode,snapshot, watermark)   
```

Start recording video
Parameter:

```
videotype: Video source type. 0: Camera; 1: Sub stream (not supported currently)
filename: File name. Name suffix is not required
classid: Custom business ID (integer)
transcode: Whether to transcode. 1: Transcode; 0: Do not transcode (unavailable currently)
snapshot: Whether to take snapshot. 1: Take snapshot; 0: Do not take snapshot (unavailable currently)
watermark: Whether to add watermark. 1: Add watermark; 0: Do not add watermark (unavailable currently)
```

Example:

```
//Start recording video
function startRecordVideo(type){
    if (currentStatus < StatusType.enter_room) {
        alert('Failed to start recording video: You have not joined the room');
        return;
    }
    if(curRecordVideoType!=null){
        alert('The video is being recorded, which cannot be recorded repeatedly');
        return;
    }
    /If /type=0, the camera is video source; if type=1, the sub stream is video source, that is, the image on PC display is used as video source (sub stream cannot be recorded through web currently)
    curRecordVideoType=type;
    var fileName;//Save the video file name. Name suffix is not required
    var curTimestamp=new Date().getTime();
    if(type==0){
        fileName='web_video_camera_'+curTimestamp;
    }else{
        fileName='web_video_desktop_'+curTimestamp;
    }
    var classId=Math.ceil(Math.random()*1000000);//Custom business ID (integer)
    var isTransCode=0;//Whether to transcode (unavailable currently)
    var isSnapShot=0;//Whether to take snapshot (unavailable currently)
    var isWaterMark=0;//Whether to add watermark (unavailable currently)
    log.info('start StartRecordVideo,curRecordVideoType='+curRecordVideoType+',filename='+fileName+',classId='+classId);
    qavSdk.StartRecordVideo(type,fileName,classId,isTransCode,isSnapShot,isWaterMark);
    log.info('after StartRecordVideo');
}

```

## 3 Stop Recording

### 3.1 Android Platform

Prototype:
  
```
public void requestMultiVideoRecorderStop(TIMAvManager.RoomInfo roomInfo,
TIMValueCallBack<java.util.List<java.lang.String>> cb)
```

Initiate request for stopping recording

Parameters:
  
```
roomInfo - relevant information of recording room. For more information, please see TIMAvManager.RoomInfo
cb - Callback. File name ID is returned in the parameter onSuccess
```

Example:

```
TIMAvManager.getInstance().requestMultiVideoRecorderStop(roomInfo, new TIMValueCallBack<List<String>>(){

    @Override
    public void onError(int code, String desc) {
        Log.e(tag, "Recorder stop failed: " + code + " desc " + desc);
    }

    @Override
    public void onSuccess(List<String> fileIds) {
        Log.d(tag, "Recorder stop succ");
        for(String fileId : fileIds){
            Log.d(tag, "fileId: " + fileId);
        }
    }

});
```

### 3.2 iOS Platform

Prototype:


```
/**
* Send request for stopping recording
*
* @param roomInfo Room information
* @param succ Callback is successfull. File ID is returned
* @param fail Callback failed. Error code is returned
*
* @return 0 Packet sent successfully
*/
- (int)requestMultiVideoRecorderStop:(OMAVRoomInfo *)roomInfo 
okBlock:(OMMultiVideoRecorderStopSucc)succ 
errBlock:(OMMultiFail)fail;
@end
```

Parameter Description:


```
roomInfo Audio/video room information
succ Callback is successfull. File ID is returned
fail Callback failed. Error code and error massage are returned. For more information, please see Error Codes.
```

Returned value:

0 indicates that the data has been successfully sent

Example:


```
[[IMSdkInt sharedInstance] 
requestMultiVideoRecorderStop:(OMAVRoomInfo *)roomInfo 
okBlock:^(NSArray *fileIDs){
NSLog(@"stop recordersucc");
   for (NSString *fileId in fileIDs) {
    NSLog(@"fileID = %@", fileId);
   }
} 
errBlock:^(int code, NSString *err) {
NSLog(@"stop recorder failed:code=%d err=%@", code, err);
}];
```

### 3.3 Windows Platform

Prototype:

```
void RequestMultiVideoRecorderStop(const TIMRoomInfo& room_info, const TIMRecordParam& para,
TIMValueCallBack<std::list<std::string>&> *cb);   
```

Initiate request for stopping push

Parameter:

```
room_info			Room information
para				Recording information
cb			callback. file_id of recorded file is returned
```

Example:


```
//Create callback
class DemoReqMutilStreamStopCB : public TIMValueCallBack<std::list<std::string>&>
{
	void OnSuccess(std::list<std::string>& value) override
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
### 3.4 Web Platform
Prototype:

```
StopRecordVideo(videotype)
```
Stop recording video
Parameter:

```
videotype: Video source type. 0: Camera; 1: Sub stream (not supported currently)
```
Example:

```
		//Stop recording video
function stopRecordVideo(){
    if (currentStatus < StatusType.enter_room) {
        alert('Failed to stop recording video: You have not joined the room');
        return;
    }
    if (curRecordVideoType==null) {
        alert('Please start recording video first');
        return;
    }
    log.info('before StopRecordVideo,curRecordVideoType='+curRecordVideoType);
    qavSdk.StopRecordVideo(curRecordVideoType);
    log.info('after StopRecordVideo');
}
```

## 4 Video Management

Videos recorded through audio/video communication SDK are stored in VOD service

(1) Log in to VOD console (http://console.cloud.tencent.com/vod) to manage recorded files
(2) Users can also manage files using VOD API. Here is how to use API:
https://cloud.tencent.com/doc/api/257/API%E6%A6%82%E8%A7%88
(3) DescribeVodPlayInfo can obtain the download address of the recorded file based on the file name entered in the recording parameters of the API "Start Recording".
For more information, please see https://cloud.tencent.com/doc/api/257/%E8%8E%B7%E5%8F%96%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE%E4%BF%A1%E6%81%AF%E5%88%97%E8%A1%A8
(4) Query video address using FileId returned when the recording ends, and configure the callback API DescribeRecordPlayInfo (it is generally called by the third party backend of customer). For more information, please see:
http://cloud.tencent.com/doc/api/257/获取录播视频播放信息-互动直播用户专用


## 5 Price and Billing

Recording feature is provided free of charge. However, since it uses VOD service capacity, fees for storage and traffic are generated in cloud VOD. For more information about the billing rules, please see:
https://cloud.tencent.com/doc/product/268/5129#2..E5.BD.95.E5.88.B6.E7.9B.B8.E5.85.B3.E8.AE.A1.E8.B4.B9

Please note that, if you have activated the VOD service and selected the package and one of the postpaid billing methods, the selected billing method is adopted. If you have not activated the VOD service, the pay-by-traffic billing method (postpaid) is used by default.

## 6 Notes

(1) During recording, one MP4 file is generated every 90 minutes, which means multiple MP4 files are generated for a recording length of more than 90 minutes. If the entire recording length is less than 90 minutes, one MP4 file is generated.
(2) When App crashes or exits due to exception in the running process, the recording ends automatically if no data is received within 1 minute. The audio/video before the user exits due to exception is recorded at the backend.
(3) The current version does not support the combining or mixing of multi-channel uplink videos

## 7 Error Codes

1: User has no permission for recording 
2. User's VOD service balance is insufficient 
30000000-30000099: An error occurred while resolving client's recording request packet 
30000200-30000299: An error occurred while requesting recording server
30000300-30000399: An error occurred while resolving recording request response packet
30000400-30000499: An error occurred while requesting stream-controlling server 
