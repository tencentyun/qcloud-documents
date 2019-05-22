## Video Device Management
All video-related features and operations in the audio/video SDK are managed by the wrapper class QAVVideoCtrl of video controller. The instance of QAVVideoCtrl can be obtained by calling the getVideoCtrl method of QAVContext class.

```
QAVVideoCtrl *videoCtrl = [AVUtil sharedContext].videoCtrl;
```

## Acquire the Local Video Stream (video input device)
To acquire the local video stream, follow the three steps below:

### 1. Use local video delegation protocol
##### (1) First, use QAVLocalVideoDelegate in ViewController.h.

##### (2) Next, set the "delegate" to "self" in the ViewController.m.

```
[[AVUtil sharedContext].videoCtrl setLocalVideoDelegate:self];
```

### 2. Camera-related operations
#### (1) Enable/disable the camera
 The main video input device on iOS is camera. The API declaration for enabling/disabling camera is as follows:

`-(QAVResult)enableCamera:(cameraPos)pos isEnable:(BOOL)bEnable complete:(cameraOptionComplete)block;`

The switching between front and rear orientation of camera is achieved by setting pos, and between enabling and disabling camera is by setting bEnable.

Note:
    Enabling the camera involves two potential operations:

1. Applying for a video status.        

2. If the application is successful, the video views captured by local camera will be uploaded to the server.

Applying for a video status can be considered as acquiring the access to video. Currently, only 4 upstream video streams are allowed at a time by the SDK, which means a maximum of 4 people can enable the video. If four people have already enabled the video, no other people is allowed to enable the video, and "false" is returned asynchronously.


Sample code:
```
[[AVUtil sharedContext].videoCtrl enableCamera:CameraPosFront isEnable:YES complete:^(int result) {
        // to do 
}];
```
#### (2) Switch camera orientation
  The API for switching camera between front and rear orientation is as follows:
`-(QAVResult)switchCamera:(cameraPos)pos complete:(cameraOptionComplete)block;`
 The sample code for switching to rear camera is as follows:
```
[[AVUtil sharedContext].videoCtrl switchCamera:CameraPosBack complete:^(int result) {
        // to do
}];
```
### 3. Acquire and process the local video stream data
If the camera is enabled successfully, the local video preview callback can be returned through the following method:

`- (void)OnLocalVideoPreview:(QAVVideoFrame *)frameData`

## Acquire the Remote Video Stream (video output device)
To acquire the remote video stream, follow the three steps below:

### 1. Use the remote video delegation protocol
(1) First, use QAVRemoteVideoDelegate in ViewController.h.

(2) Next, set "delegate" to "self" in the ViewController.m.
```
[[AVUtil sharedContext].videoCtrl setRemoteVideoDelegate:self];
```

### 2. Request and cancel request for remote video
#### (1) Request multiple remote video streams

Requesting remote video stream involves requesting remote video views using the class method in QAVEndpoint. The API declaration is as follows:

```
+(int)requestViewList:(QAVContext*)context identifierList:(NSArray*)identifierList srcTypeList:(NSArray*)srcTypeList ret:(RequestViewListBlock)block;
```
 The parameter context is the current context instance; identifierList is the list of IDs of requested members and passes the identifier (NSString*) of member; srcTypeList is the list of video source types and passes the avVideoSrcType of member, which must be converted to (NSNumber *) before being added to the array.

The sample code is as follows:
```
    QAVMultiRoom *multiRoom = (QAVMultiRoom *)[AVUtil sharedContext].room;
    NSArray *memberList = [multiRoom GetEndpointList];
    if ([memberList count]) {
        QAVEndpoint *endpoint = [memberList objectAtIndex:0];//Request the video of the first person in the list
        NSMutableArray *identifierListArray = [NSMutableArray arrayWithObject:endpoint.identifier];
        
        NSMutableArray *scrTypeListArray = [NSMutableArray new];
        int requestingSrcType = QAVVIDEO_SRC_TYPE_NONE;
        if(endpoint.isCameraVideo)
        {
            requestingSrcType = QAVVIDEO_SRC_TYPE_CAMERA;
            [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
        }
        else if (endpoint.isScreenVideo)
        {
            requestingSrcType = QAVVIDEO_SRC_TYPE_SCREEN;
            [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
        }
        else
        {
            return;
        }
        
        [QAVEndpoint requsetViewList:[AVUtil sharedContext] identifierList:identifierListArray srcTypeList:scrTypeListArray ret:^(QAVResult result) {
            NSLog(@"requestView Result = %ld",(long)result);
        }];
    }
```
#### (2) Cancel all the requests for video views

```
+(int)cancelAllview:(QAVContext*)context ret:(CancelViewListBlock)block;
```
 Sample code:
```
[QAVEndpoint cancelAllview:[AVUtil sharedContext] ret:^(QAVResult result) {
    // to do                
}];
```

#### (3) Request a single remote video stream

After obtaining a QAVEndpoint instance, you can request the user's video stream. The API declaration is as follows:

```
-(QAVResult)requestView:(requestViewBlock)block;
```
Sample code:
```
[endpoint requestView:^(QAVResult result) 
{
    // to do
}];
```

#### (4) Cancel the request for the video view of a member

The API declaration is as follows:

```
-(QAVResult)cancelView:(requestViewBlock)block;
```
Sample code:

```
[endpoint cancelView:^(QAVResult result) 
{
    // to do        
}];
```

### 3. Acquire and process the remote video stream data
 
 If the request for video view is successful,  the remote view callback can be returned through the following method:

```
- (void)OnVideoPreview:(QAVVideoFrame *)frameData
```

## Acquire the Screen-sharing Views 
Similar to the process for acquiring remote video stream, the acquisition of screen-sharing video involves the following three steps:

### 1. Use the screen-sharing protocol

(1) First, use QAVScreenVideoDelegate in ViewController.h.

(2) Next, set "delegate" to "self" in the ViewController.m.

`[[AVUtil sharedContext].videoCtrl setScreenVideoDelegate:self];`
### 2. Request the screen-sharing video
The code for this step is the same as that for requesting remote video stream. After obtaining the endpoint, determine whether the endpoint has any video sent from screen-sharing. If any, change the enumeration value of requestingScrType. When the request is issued, the server determine whether to return screen-sharing data or remote video stream data, depending on the enumeration value of scrTypeList.
```
if (endpoint.isScreenVideo)
   {
      requestingSrcType = QAVVIDEO_SRC_TYPE_SCREEN;
      [scrTypeListArray addObject:[NSNumber numberWithInt:requestingSrcType]];
   }
[QAVEndpoint requestViewList:[AVUtil sharedContext] identifierList:identifierListArray srcTypeList:scrTypeListArray ret:^(QAVResult result) {
}];
```
### 3. Acquire and process the screen-sharing video stream data
 If the request for the video view is successful, the screen-sharing video stream callback can be returned through the following method:

`- (void)OnVideoPreview:(QAVVideoFrame *)frameData`
## Use Beauty Filter for Video
Nowadays, beauty filter feature is very popular among the majority of girls. Audio/video SDK provides a simple API for users to achieve one-tap beautifying.

Notes:
- 1. Beauty filter feature is only supported by iphone4s and above, ipad, as well as ipodtouch5 and above.

- 2. Beauty filter cannot be enabled until the user joins a room and enables the camera. That is to say, APIs enableBeauty () and inputBeautyParam take effect only if being called after the camera is enabled. For API isEnableBeauty, this restriction does not apply.

- 3. The parameter of beautifying level varies from 0 to 9. 0 indicates the lowest level, while 9 highest.


The API declaration is as follows:
```
-(bool)isEnableBeauty;                        //Query whether the phone model supports beauty filter
-(bool)enableBeauty:(bool)isEnable;           //Enable the beauty filter
-(void)inputBeautyParam:(float)beautyParam;   //Pass the beautifying level parameter
```
The sample code is as follows (isCameraOn is the camera switch flag):
```
float beautyParam = 9.0;    //Maximize the beautifying effect

if( [[AVUtil sharedContext].videoCtrl isEnableBeauty] && isCameraOn)
{
    [[AVUtil sharedContext].videoCtrl enableBeauty:YES];
    [[AVUtil sharedContext].videoCtrl inputBeautyParam:beautyParam];
}
```
