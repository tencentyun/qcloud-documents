### Non-interactive Broadcasting under LVB Code Mode and Supported Recording Options

The method for enabling non-interactive broadcasting  | The method for recording non-interactive broadcasting  | Multiple record formats |  Record callback | Convenience for development | Reliability | Resource consumption
:-----: | :-----: | :-----: |:-----: |:-----: | :-----:| :-----:
Automatic | Automatic |FLV/HLS/MP4|✔️|※※※※|※※※※|※
Manual | Automatic |FLV/HLS/MP4|✔️|※※※|※※※|※※
Automatic | Manual |MP4|❌|※※|※※|※※※
Manual | Manual |MP4|❌|※|※|※※※※


### 1. Recording Method

##### Automatic recording is recommended. Developers can control the recording by controlling the timing of push.

1.1 Method 1:  Globally automatic recording

* Choose `LVB Recording` when activating LVB code, so that all the non-interactive broadcastings can be recorded.

1.2 Method 2:  Specify recording format during non-interactive broadcasting

* See "non-interactive broadcasting parameters in Development Guide for Non-interactive Broadcasting under LVB Code Mode"

1.3 Manual Recording

For special business needs, you can still manually control the start and end time of recording. However, errors may occur in the process of manual recording, so developers need to pay much more attention. For more information, please see appendix.

### 2. Recording Event Notification for Recording Processing

For more information about the parameter format and response solution of callback event, please see appendix of Development Guide for Non-interactive Broadcasting under LVB Code Mode.

##### The event_type of recording notification is **100**, indicating that a new recorded file is generated. Meanwhile, the following information are contained in the message body:

| Field name  | Type        | Description        |
|------------  |-------------|-------------|
| file_id   | string      | ID for VOD. It can be used to locate a unique video file in VOD platform  |
|file_format|string| Format of recorded file |
| video_url  | string      | Download address of a VOD video  | 
| file_size  | string       | File size  |
| start_time  | int      | Start time (UNIX timestamp. The time cannot be accurate to seconds due to interference of the I frame position.)  |
| end_time  | int       | End time (UNIX timestamp. The time cannot be accurate to seconds due to interference of the I frame position.)  |
| stream_param  | string       | Parameters for recording, including room ID, sdkappid, etc. |

Example: A new recorded FLV part is generated, ID is 9192487266581821586, playback address is `http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv`.

```json
{
    "appid": XXXXX,
    "channel_id": "2519_2500647",
    "duration": 272,
    "end_time": 1496220894,
    "event_type": 100,
    "file_format": "flv",
    "file_id": "9031868222958931071",
    "file_size": 30045521,
    "record_file_id": "9031868222958931071",
    "sign": "XXXXX",
    "start_time": 1496220622,
    "stream_id": "2519_2500647",
    "stream_param": "txSecret=838113524b38ebbdc&txTime=596ae808&from=interactive&sdkappid=140000000&sdkapptype=1&groupid=218291828&ts=594351ff&mix=t_id:1;session_id:6013095252542427999;layer:b&record=mp4&record_name=8789_c9acaaaaaaaaaa44faf58a_20170616113527",
    "t": 1496221502,
    "video_id": "200011683_481565e0befe4e44903839aebe370ef6",
    "video_url": "http://1252033264.vod2.myqcloud.com/d7a4cabbvodgzp1252033264/0257ade99031868222958931071/f0.flv"
}

```

### 3. Change in the method for querying recorded files

* The download address for the video files that can be recorded in server callback event.
* You can use video name prefix to perform fuzzy query. Construction rule of video name prefix: LVB code_Recording ID<br/>
If the LVB code is `8888_81265058829fd2e50c8ec2ac78d55127`, the prefix of recorded file is `8888_81265058829fd2e50c8ec2ac78d55127`.
* [API documentation](https://cloud.tencent.com/document/product/266/7825) for querying recorded files

====================================================================

### Appendix

#### For special business needs, you can still manually control the start and end time of recording. However, errors may occur in the process of manual recording, so developers need to pay much more attention.

### 1. Note on Manual Recording

* For manual recording, videos can only be recorded in MP4 format, without recording callback event. A recorded file is generated every 90 minutes.
* If you enable the camera after joining audio/video room or if you start recording after enabling screen sharing, you need to stop recording before exiting the room on the client.
* Considering the Internet access, packet loss, latency and other incidents may occur on the network. Retry mechanism is required for enabling recording, and retry interval should be no less than 3 seconds.
* Note: Parameters such as room ID, VJ ID should be specified to ensure the corresponding relationship.

### 2. Android SDK Recording API

##### 2.1 Configure Recording Parameters

```java
ILiveRecordOption option = new ILiveRecordOption();
option.fileName(filename);
option.classId(Integer.parseInt(classId));
```

* Recording parameter: ILiveRecordOption

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
fileName | String | Required | Name of recorded file
classId | int | Required (enter 0 for current version) | Video category ID
transCode | boolean | (Not supported currently. Default is NO) | Whether to transcode
screenShot | boolean | (Not supported currently. Default is NO) | Whether to take screenshot
waterMark | boolean | (Not supported currently. Default is NO) | Whether to add watermark
sdkType | TIMAvManager.SDKType | Required (select Normal for current version) | Business type of SDK
recordType | AVRecordType | AV_RECORD_TYPE_VIDEO | Recording type


##### 2.2 Start Recording

```java
ILiveRoomManager.getInstance().startRecordVideo(option, new ILiveCallBack() {
        @Override
        public void onSuccess(Object data) {
            //Recording started successfully
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //Failed to start recording
        }
});
```

##### 2.3 End Recording

```java
ILiveRoomManager.getInstance().stopRecordVideo(new ILiveCallBack<List<String>>() {
        @Override
        public void onSuccess(List<String> data) {
            //Recording ended successfully
            for (String url : data){
                //File ID
            }
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //Failed to end recording
        }
});
```

### 3. iOS SDK Recording API

##### 3.1 Configure Recording Parameters

```c++
ILiveRecordOption *option = [[ILiveRecordOption alloc] init];
option.fileName = @"Recorded files of new FreeShow";
option.classId = [tag intValue];
option.avSdkType = sdkType;
option.recordType = recordType;
```

* Recording parameter: ILiveRecordOption

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
fileName | NSString | Required | The name of recorded file
tags | NSArray | Required | List of video tags
classId | UInt32 | Required (enter 0 for current version) | Video category ID
isTransCode | BOOL | (Not supported currently. Default is NO) | Whether to transcode
isScreenShot | BOOL | (Not supported currently. Default is NO) | Whether to take screenshot
isWaterMark | BOOL | (Not supported currently. Default is NO) | Whether to add watermark
sdkType | AVSDKType | Required (select AVSDK_TYPE_NORMAL for current version) | Business type of SDK
recordType | AVRecordType | AV_RECORD_TYPE_VIDEO | Recording type

##### 3.2 Start Recording

```c++
[[ILiveRoomManager getInstance] startRecordVideo:option succ:^{
        NSLog(@"Recording started");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"Failed to start recording");
}];
```

##### 3.3 End Recording

```c++
[[ILiveRoomManager getInstance] stopRecordVideo:^(id selfPtr) {
            NSArray *fileIds = (NSArray *)selfPtr;
            NSLog(@"Recording ended");
        } failed:^(NSString *module, int errId, NSString *errMsg) {
            NSLog(@"Failed to end recording");
}];
```

### 4. PC SDK Recording API

##### 4.1 Configure Recording Parameters

```c++
iLiveRecordOption recordOpt;
recordOpt.record_data_type = recordType;
recordOpt.filename = fileName;
recordOpt.class_id = classId;
```

* Recording parameter: iLiveRecordOption

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
record_data_type | E_RecordDataType | E_RecordCamera | Recording type
filename | string | Required | The name of recorded file
class_id | int | (Not supported currently. Default is 0) | Video category ID

##### 4.2 Start Recording

```c++
void onStartRecordVideoSuc(void* data)
{
	//Recording started
}

void onStartRecordVideoErr(int code, const std::string& desc, void* data)
{
	//Failed to start recording
}

iLiveRoomMgr::getInstance()->startRecordVideo(recordOpt, onStartRecordVideoSuc, onStartRecordVideoErr, NULL);
```

##### 4.3 End Recording

```c++
void onStopRecordVideoSuc(std::list<std::string>& value, void* data)
{
	//Recording ended
}

void onStopRecordVideoErr(int code, const std::string& desc, void* data)
{
	//Failed to end recording
}

iLiveRoomMgr::getInstance()->stopRecordVideo(onStopRecordVideoSuc, onStopRecordVideoErr, NULL);
```

