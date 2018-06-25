## Interfacing
Short video recording is to capture the camera image and microphone sound, process the image and sound, implement encoding and compression, and finally generate an MP4 file with the desired definition.
You can experience the recording function through the DEMO project in the development package.
![](https://main.qcloudimg.com/raw/4f8195d62fdb7e78ccd11609aad0c87d.png )
## API Description 
Tencent Cloud UGC SDK provides relevant APIs used to record and publish short videos. These APIs are described below:

|  API File |  Feature |
| ------| --------|
| `TXUGCRecord.h` | Record short videos |
| `TXUGCRecordListener.h` | Record callback and publish callback for short videos |
| `TXUGCRecordEventDef.h` | Record event callback for short videos |
| `TXUGCRecordTypeDef.h` | Basic parameter definitions |
| `TXUGCPartsManager.h` | Video fragment management class, used for multi-fragment recording and deletion |

### 1. Video Preview
TXUGCRecord (located in TXUGCRecord.h) is used to record short videos. The startCamera function is used to launch preview. You need to open the camera and microphone when launching preview, thus you may receive a permission prompt.

```ObjectiveC
UIView *    preViewContainer;                    //Prepare a view used for previewing camera image
TXUGCSimpleConfig *config = [[TXUGCSimpleConfig alloc] init];
//config.videoQuality = VIDEO_QUALITY_LOW;       // For 360p, a video of 10 seconds is around 0.75 MB
config.videoQuality   = VIDEO_QUALITY_MEDIUM;    //For 540p, a video of 10 seconds is around 1.5 MB (encoding parameters are the same with WeChat iOS short videos)
//config.videoQuality = VIDEO_QUALITY_HIGH;      // For 720p, a video of 10 seconds is around 3 MB
config.frontCamera    = YES;                     //Whether to use front camera. Use switchCamera  to switch camera
config.minDuration    = 5;                       //The minimum length of video recording
config.maxDuration    = 60;                      //The maximum length of video recording
[TXUGCRecord shareInstance].delegate = self;     //The API TXVideoPublishListener is implemented by "self"
[[TXUGCRecord shareInstance] startCamera:param preview:preViewContainer];
```

### 2. Special Effect
You can use the special effect switches in TXUGCRecord to add certain special effects to your video or control the camera (either before or during a recording process).

```ObjectiveC
//////////////////////////////////////////////////////////////////////////
                        Supported special effects are shown below (1.9.1 version or above)
//////////////////////////////////////////////////////////////////////////

// Set video recording proportion: 3:4; 9:16; 1:1
[[TXUGCRecord shareInstance] setAspectRatio:videoRatio];

// Sets global watermark
// waterMark            Global watermark image
// normalizationFrame   The normalization frame of watermark relative to the video image
[[TXUGCRecord shareInstance] setWaterMark:waterMark  normalizationFrame:normalizationFrame];

// Switch between front and rear cameras. isFront: whether to use the front camera (default is front camera)
[[TXUGCRecord shareInstance] switchCamera:YES];

// Configure beautifying and whitening effect levels.
// beautyDepth     : Available value range for beautifying level: 0-9. 0 means to disable beautifying. A higher value means a stronger effect.
// whiteningDepth  : Available value range for whitening level: 0-9. 0 means to disable whitening. A higher value means a stronger effect.
[[TXUGCRecord shareInstance] setBeautyDepth: 7 WhiteningDepth: 1];

// Configure color filter: romantic, fresh, artistic, tender, vintage...
// image: Specify the color lookup table used by the filter. Note: Be sure to use PNG format.
//The filter lookup table image used in the Demo is located in RTMPiOSDemo/RTMPiOSDemo/resource/FilterResource.bundle
   setSpecialRatio :  Used to configure the effect level of the filter (0-1). A higher value means a stronger effect. Default is 0.5.
[[TXUGCRecord shareInstance] setFilter: filterImage];
[[TXUGCRecord shareInstance] setSpecialRatio: 0.5];

//Whether to enable flashlight
[[TXUGCRecord shareInstance] toggleTorch: YES];

// Adjust the focal distance (1-5). 1 means the farthest viewing angle (normal lens) and 5 means the closest viewing angle (enlarging lens). The maximum value is recommended to be 5. If it is set to a value larger than 5, the video data may become blurred and indistinct.
[[TXUGCRecord shareInstance]setZoom:1.0];

//////////////////////////////////////////////////////////////////////////
//                             Related to background music
//////////////////////////////////////////////////////////////////////////
// Play background music
[[TXUGCRecord shareInstance] playBGM:path
    withBeginNotify:beginNotify
 withProgressNotify:progressNotify
  andCompleteNotify:completeNotify];

//Stop background music
[[TXUGCRecord shareInstance] stopBGM];

// Pause background music
[[TXUGCRecord shareInstance] pauseBGM];

// Resume background music
[[TXUGCRecord shareInstance] resumeBGM];

// Set the microphone volume to control the microphone volume when playing the mixed background music.
// volume:  Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value.
[[TXUGCRecord shareInstance] setMicVolume:1.0];

// setBGMVolume Set the background music volume to control the background music volume when playing the mixed background music.
// volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the background music volume, you can set it to a larger value.
[[TXUGCRecord shareInstance]setBGMVolume:1.0];

//////////////////////////////////////////////////////////////////////////
//                       The following special effects are only supported by the VIP edition
// (These effects use the intellectual properties of YouTu team and are supported only by the VIP SDK edition. We cannot provide them for free)
//////////////////////////////////////////////////////////////////////////

// Set eye enlargement level (0-9)
[[TXUGCRecord shareInstance] setEyeScaleLevel: 0];

//Set face slimming level (0-9)
[[TXUGCRecord shareInstance] setFaceScaleLevel: 0];

// Set V-shaped face level (0-9)
[[TXUGCRecord shareInstance] setFaceVLevel:0];

//Set chin stretching or contracting level (-9-9) 
[[TXUGCRecord shareInstance] setChinLevel:0];

//Set short face level (0-9)
[[TXUGCRecord shareInstance] setFaceShortLevel:0];

// Set nose narrowing level (0-9)
[[TXUGCRecord shareInstance] setNoseSlimLevel:0];

// Set motion effect sticker tmplName - material name   tmplDir - path of the material package
[[TXUGCRecord shareInstance] selectMotionTmpl: tmplName inDir：tmplDir];

// Configure green screen effect. Green screen material is an MP4 file with an aspect ratio of 9:16 (for example, 368*640, 540*960, 720*1280)
[[TXUGCRecord shareInstance] setGreenScreenFile: file]; 
```


### 3. Video Recording
Call the startRecord function in TXUGCRecord to start recording process, and call the stopRecord function to stop recording process. Be sure to call these two functions in pairs.

```ObjectiveC
[[TXUGCRecord shareInstance] startRecord];
[[TXUGCRecord shareInstance] stopRecord];
``` 

The feedback of the recording process and result is provided via the API TXVideoRecordListener (defined in TXUGCRecordListener.h):

- "onRecordProgress" is used to provide the feedback of the recording progress. The parameter "millisecond" indicates record length (in ms):

```ObjectiveC
@optional
-(void) onRecordProgress:(NSInteger)milliSecond;
``` 

- "onRecordComplete" provides the feedback of the recording result. The fields "retCode" and "descMsg" indicate error code and error message. "videoPath" is the path of the recorded short video file. "coverImage" is the first frame image of the short video (automatically captured, this image can be used when you publish the video).

```ObjectiveC   
@optional
-(void) onRecordComplete:(TXRecordResult*)result;
``` 
    
### 4. Multi-fragment Recording and Deletion  
```ObjectiveC
//A video fragment is generated after pauseRecord is performed, which can be obtained in TXUGCPartsManager. 
[[TXUGCRecord shareInstance] pauseRecord];

 // resumeRecord  is used to resume video recording
[[TXUGCRecord shareInstance] resumeRecord];

//Get fragment management object
@property (nonatomic, strong, readonly) TXUGCPartsManager *partsManager; 

//Get the total duration of all current video fragments
[_partsManager getDuration];

//Get the paths of all video fragments
[_partsManager getVideoPathList];

// Delete the last video fragment
[_partsManager deleteLastPart];

// Delete a specified video fragment
[_partsManager deletePart:1];

// Delete all video fragments
[_partsManager deleteAllParts];  

//Synthesize all video fragments
[_partsManager joinAllParts: videoOutputPath];
```

### 5. Preview File
Use [Video Playback](https://cloud.tencent.com/document/product/584/9372) to preview the generated MP4 file. When calling startPlay, you need to specify playback type as [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9372#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6).

### 6. Obtain License Information
The verification of short video license is added in the new version of SDK. If you fail to pass the verification, you can use the API to query specific information in the license.

``` 
NSString *licenceInfo = [TXUGCBase getLicenceInfo];
``` 

