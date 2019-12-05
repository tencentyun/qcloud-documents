Video recording feature is available as of ILVB SDK1.3. Users can use this feature by calling relevant APIs. Recorded files are stored in VOD service provided by Tencent Cloud. Users can perform operations such as management, transcoding and distribution on these files using VOD console and APIs.

You can use the recording feature only after the Tencent Cloud VOD service is activated.

The following is the recording feature development guide:

## 1 Timing Diagram
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/hudongzhibolz-1.png)

## 2 Start Recording

### 2.1 Android

Prototype:

```
public void requestMultiVideoRecorderStart(TIMAvManager.RoomInfo roomInfo,
                                           TIMAvManager.RecordParam param,
                                           TIMCallBack cb)
```

Initiate the request for starting recording

Parameters:

```
roomInfo - Information of recording room. For more information, please see TIMAvManager.RoomInfo
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

>Note: A user can only initiate request for one-channel recording at a time.


### 2.2 iOS

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

>Note: A user can only initiate request for one-channel recording at a time.


### 2.3 Windows

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
cb - URL list for sharing returned in onSuccess parameter

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
	int class_id;				 		//Video category ID
	bool is_transcode;					//Whether to transcode
	bool is_screenshot;				 	//Whether to take screenshot
	bool is_watermark;					//Whether to add watermark
	std::list<std::string> tags;	 	//List of video tags
	E_TIMSDKType	sdk_type;
	uint32_t		record_data_type; //Recorded data type: 0: Camera video; 1: Sub-stream
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

>Note: A user can only initiate request for one-channel push at a time. If there is already a push channel in the process of LVB when you initiate a request for push, an error message indicating a push channel already exits is returned.

### 2.4 Web
Prototype:
                              
```
StartRecordVideo(videotype, filename, classid,transcode,snapshot, watermark)   
```

Start recording video
Parameter:

```
videotype: Video source type. 0: Camera; 1: Sub-stream (not supported currently)
filename: File name. Name suffix is not required
classid: ID defined by service end (integer)
transcode: Whether to transcode. 1: Yes; 0: No (unavailable currently)
snapshot: Whether to take snapshot. 1: Yes; 0: No (unavailable currently)
watermark: Whether to add watermark. 1: Yes; 0: No (unavailable currently)
```

Example:

```
//Start recording video
function startRecordVideo(type){
    if (currentStatus < StatusType.enter_room) {
        alert('Failed to start recording video: User has not joined the room');
        return;
    }
    if(curRecordVideoType!=null){
        alert('The video is being recorded. Request for recording cannot be initiated again.');
        return;
    }
    //If type=0, the camera is video source; if type=1, the sub-stream is video source, that is, the image on PC display is used as video source (recording sub-stream is not supported on Web platform)
    curRecordVideoType=type;
    var fileName;//The saved video file name. Name suffix is not required
    var curTimestamp=new Date().getTime();
    if(type==0){
        fileName='web_video_camera_'+curTimestamp;
    }else{
        fileName='web_video_desktop_'+curTimestamp;
    }
    var classId=Math.ceil(Math.random()*1000000);//ID defined by service end (integer)
    var isTransCode=0;//Whether to transcode (unavailable currently)
    var isSnapShot=0;//Whether to take snapshot (unavailable currently)
    var isWaterMark=0;//Whether to add watermark (unavailable currently)
    log.info('start StartRecordVideo,curRecordVideoType='+curRecordVideoType+',filename='+fileName+',classId='+classId);
    qavSdk.StartRecordVideo(type,fileName,classId,isTransCode,isSnapShot,isWaterMark);
    log.info('after StartRecordVideo');
}

```

## 3 Stop Recording

### 3.1 Android

Prototype:
  
```
public void requestMultiVideoRecorderStop(TIMAvManager.RoomInfo roomInfo,
TIMValueCallBack<java.util.List<java.lang.String>> cb)
```

Initiate request for stopping recording

Parameters:
  
```
roomInfo - information of recording room. For more information, please see TIMAvManager.RoomInfo
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

### 3.2 iOS

Prototype:


```
/**
* Send request for stopping recording
*
* @param roomInfo Room information
* @param succ Callback is successful. File ID is returned
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
succ Callback is successful. File ID is returned
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

### 3.3 Windows

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
### 3.4 Web
Prototype:

```
StopRecordVideo(videotype)
```
Stop recording video
Parameter:

```
videotype: Video source type. 0: Camera; 1: Sub-stream (not supported currently)
```
Example:

```
		//Stop recording video
function stopRecordVideo(){
    if (currentStatus < StatusType.enter_room) {
        alert('Failed to stop recording video: User has not joined the room');
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

Videos recorded through audio/video messaging SDK are stored in VOD service

(1) Log in to VOD console (http://console.cloud.tencent.com/vod) to manage recorded files
(2) Users can also manage files using VOD APIs. For more information on how to use the APIs, please see:
http://cloud.tencent.com/wiki/云点播API
(3) DescribeVodPlayInfo can obtain the download address of the recorded file based on the file name entered in the recording parameters of the API "Start Recording".
For more information, please see http://cloud.tencent.com/wiki/v2/DescribeVodPlayInfo
(4) Query video address using FileId returned when the recording ends, and configure the callback API DescribeRecordPlayInfo (it is generally called by the third party backend of customer). For more information, please see:
http://cloud.tencent.com/doc/api/257/获取录播视频播放信息-互动直播用户专用
## 5 Price and Billing

Recording feature is provided free of charge. However, storage and traffic consumed in VOD are billable. For more information on the billing method, please see:
http://cloud.tencent.com/wiki/音视频云通信价格与计费说明

Please note that, if you have activated the VOD service and selected a billing method from package and postpaid mode, the selected billing method is adopted. If you have not activated the VOD service, the billing method of pay-by-traffic (postpaid) is used by default.

## 6 Notes

(1) Recording feature is not supported for one-on-one audio/video room
(2) Type of recorded file defaults to MP4.
(3) During recording, one MP4 file is generated every one hour, and more than one MP4 files are generated for a recording length of more than one hour. If the entire recording length is less than one hour, one MP4 file is generated.
(4) When App crashes or exits due to exception in the running process, the recording ends automatically if no data is received within one minute. The audio/video before the exit is recorded at the backend.
(5) The current version does not support the merging or mixing of multi-channel upstream videos

## 7 Error Codes

(1) User has no permission for recording 
(2) User has insufficient VOD balance 
30000000-30000099: An error occurred while resolving client's recording request packet 
30000200-30000299: An error occurred while requesting recording server
30000300-30000399: An error occurred while resolving response packet from recording request
30000400-30000499: An error occurred while requesting stream-control server 
