## Development of Recording for ILVB
Recorded files are stored in VOD service provided by Tencent Cloud. Users can perform operations such as management, transcoding and distribution on these files using VOD console and APIs.<br/><br/>
**Make sure the Tencent VOD service is activated before using the recording feature.**

### 1 Client SDK APIs
#### Android
##### Start recording
###### 1. Set recording parameters

```
ILiveRecordOption option = new ILiveRecordOption();
option.fileName(filename);
option.addTag(tag);
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

Method | Parameter | Description
:--:|:--:|:--:
addTag | String | Add a video tag

###### 2. Start recording

```
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

##### End recording

```
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

For more information on how to implement recording feature on Android, please see [New FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos)

#### iOS
##### Start recording
###### 1. Set recording parameters

```
ILiveRecordOption *option = [[ILiveRecordOption alloc] init];
option.fileName = @"Recorded files of New FreeShow";
option.tags = tags;
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

###### 2. Start recording

```
[[ILiveRoomManager getInstance] startRecordVideo:option succ:^{
        NSLog(@"Recording started");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"Failed to start recording");
    }];
```

##### End recording

```
[[ILiveRoomManager getInstance] stopRecordVideo:^(id selfPtr) {
            NSArray *fileIds = (NSArray *)selfPtr;
            NSLog(@"Recording ended");
        } failed:^(NSString *module, int errId, NSString *errMsg) {
            NSLog(@"Failed to end recording");
        }];
```

* Callback result: NSArray (List of file IDs in an NSString form is returned )

For more information on how to implement recording feature on iOS, please see [New FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)

### 2 Video Management

Videos recorded through audio/video communication SDK are stored in VOD service.

(1) You can manage recorded files by logging in to [Management Console](http://console.cloud.tencent.com/vod).<br/>
(2) You can also manage recorded filed through APIs provided by VOD. For more information, please see [API Overview](https://cloud.tencent.com/document/product/266/7788).<br/>
(3) DescribeVodPlayInfo obtains the download address of the recorded file based on the file name entered in the recording parameters of the API "Start Recording".
 For more information, please see [relevant document](https://cloud.tencent.com/document/product/266/8586).

### 3 Prices and billing method

The charge is billed based on the maximum concurrent channels for the recording month, with a price of 30 CNY/channel/month.
In addition, recording involves VOD features, which give rise to charges for storage and traffic. [Billing Rules](https://cloud.tencent.com/doc/product/268/5129#2..E5.BD.95.E5.88.B6.E7.9B.B8.E5.85.B3.E8.AE.A1.E8.B4.B9):


Please note that, if you have activated the VOD service and selected a billing method from package and postpaid mode, the selected billing method is adopted. If you have not activated the VOD service, the billing method of pay-by-traffic (postpaid) is used by default.

### 4 Notes

(1) Recording feature is not supported for one-on-one audio/video room
(2) Type of recorded file defaults to MP4.
(3) During recording, one MP4 file is generated every 90 minutes, which means multiple MP4 files are generated for a recording length of more than 90 minutes. If the entire recording length is less than 90 minutes, one MP4 file is generated.
(4) When App crashes or exits due to exception in the running process, the recording ends automatically if no data is received within 1 minute. The audio/video before the exit is recorded at the backend.
(5) The current version does not support the merging or mixing of multi-channel upstream videos.

### 5 Error Codes


| Error Code | Description | Solution |
|---------|---------|---------|
| 1 | User has no permission for recording ||
| 2 | User has insufficient balance for VOD service ||
| 30000000 | Failed to resolve SDK request | [Check whether the recording request fields are complete ]
| 30000001 | Failed to resolve SDK request - Recording request packet is missing | [Check whether the recording request fields are complete ]
| 30000002 | Failed to resolve SDK request - Filename field for recorded file is missing | [Check whether the recording request fields are complete]
| 30000003 | Failed to resolve SDK request - Recording request operation field is missing | [Check whether the recording request fields are complete]
| 30000004 | Failed to resolve SDK request - Incorrect video source type (such as camera, desktop) | [Check whether the recording request fields are complete ]
| 30000201 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service]
| 30000202 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service]
| 30000203 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service]
| 30000207 | A communication error occurred while requesting recording server - Failed to fetch the address of recording server | [Report to Tencent customer service]
| 30000208 | A communication error occurred while requesting recording server - Timeout of request for recording server | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000301 |An error occurred while resolving the response packet from recording server - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000302 |An error occurred while resolving the response packet from recording server - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000303 | An error occurred while resolving the response packet from recording server - No IP is returned | [Report to Tencent Cloud customer service] |
| 30000304 |An error occurred while resolving the response packet from recording server - No port is returned | [Report to Tencent Cloud customer service]
| 30000305 | An error occurred while resolving the response packet from recording server - No result is returned | [Report to Tencent customer service]
| 30000401 |An error occurred while obtaining the grocery service IP by querying room |[This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000402 | An error occurred while fetching grocery data by querying room |[This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000403 | grocery does not exist and cannot be fetched by querying room (room does not exist) | [Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered]
| 30000404 | Timeout while querying room stream-control server | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000405 | An error occurred with the response packet while querying room - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000406 | An error occurred with the response packet while querying room - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000407 | An error occurred with the response packet while querying room - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000408 | An error occurred with the response packet while querying room - No result is returned | [Report to Tencent customer service] |
| 30000409 | An error occurred with the response packet while querying room - Failed to resolve the data packet |[Report to Tencent customer service]
| 30000410 |Recording room does not exist | [Check whether the room has been activated successfully, whether the user ID and groupid for recording are correctly entered, or whether the user has exited the room]
| 30000411 | Recording room or the initiator of recording does not exist | [Check whether the room has been activated successfully, whether the user ID and groupid for recording are correctly entered, or whether the user has exited the room]
| 30000412 | Request for ending recording has been sent more than once. The user has ended recording	|[This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this.]
| 30000413 | Request for ending recording has been sent more than once. The user has ended recording	|[This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this.]
| 30000414 | An error occurred with internal server operation type while querying room | [Report to Tencent customer service]
| 30000415 |Request for starting recording has been sent more than once and recording has started; or the initiator of recording does not exist |[Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered] |



