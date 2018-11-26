## Interfacing
Short video recording is to capture the camera image and microphone sound, process the image and sound, implement encoding and compression, and finally generate an MP4 file with the desired definition.
You can try out the recording feature using the DEMO project in the development package.
![](https://main.qcloudimg.com/raw/4f8195d62fdb7e78ccd11609aad0c87d.png )
The code of the recording feature for Android is placed under the package name com.tencent.liteav.demo.videorecord. TCVideoSettingActivity is the recording settings interface, and TCVideoRecordActivity is the recording interface. After the resource files required in the interfaces are copied, you can achieve the recording interface effect and feature.
## API Description 
Tencent Cloud UGC SDK provides relevant APIs used to record and publish short videos. These APIs are described below:

| API File                     | Feature                       |
| ------------------------ | ------------------------ |
| `TXUGCRecord.java`       | Record short videos               |
| `TXRecordCommon.java`    | Basic parameter definitions, including short video recording callback API and publishing callback API |
| `TXUGCPartsManager.java` | Video fragment management class, used for multi-fragment recording and deletion    |
| `ITXVideoRecordListener.java` | Recording callback for short videos                  |

### 1. Video Preview
TXUGCRecord (located in TXUGCRecord.java) is used to record short videos. Our first task is to realize the video preview feature. The startCameraSimplePreview function is used to launch preview. You need to open the camera and microphone when launching preview, thus you may receive a permission prompt.

```java
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					//Configure recording callback
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	//Prepare a view used for previewing camera image
mVideoView.enableHardwareDecode(true);
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;           //Whether to use front camera. Use switchCamera to switch camera.
param.minDuratioin = 5000;	//The minimum length of video recording (in ms)
param.maxDuration = 60000;	//The maximum length of video recording (in ms)
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);
```

### 2. Special Effect
You can use the special effect switches in TXUGCRecord to add certain special effects to your video or control the camera (either before or during a recording process).

```java
//////////////////////////////////////////////////////////////////////////
//                      Supported special effects are shown below (1.9.1 version or above).
//////////////////////////////////////////////////////////////////////////
//
// Switch between front and rear cameras. The parameter mFront indicates whether to use front camera. Default is front camera.
mTXCameraRecord.switchCamera(mFront);

//Configure beautifying and whitening effect levels.
// beautyDepth     : Available value range for beautifying level: 0-9. 0 means to disable beautifying. A higher value means a stronger effect.
// whiteningDepth  : Available value range for whitening level: 0-9. 0 means to disable whitening. A higher value means a stronger effect.
mTXCameraRecord.setBeautyDepth(beautyDepth, whiteningDepth);

// Configure color filter: romantic, fresh, artistic, tender, vintage...
// Bitmap     : Specify the color lookup table used by the filter. Note: Be sure to use PNG format.
//The filter lookup table used in the Demo is located in RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/.
// setSpecialRatio : Used to configure the effect level of the filter (0-1). A higher value means a stronger effect. Default is 0.5.
mTXCameraRecord.setFilter(filterBitmap);
mTXCameraRecord.setSpecialRatio(0.5);
// Set the normalization value of the global watermark TXRect-watermark relative to the video image. SDK automatically calculates the height according to the aspect ratio of watermark.
// For example, the size of a video image is (540,960). The three parameters of TXRect are set to 0.1, 0.1, 0.1
// The actual pixel coordinates of watermark are (540*0.1, 960*0.1, 540*0.1)
// 540 * 0.1 * watermarkBitmap.height / watermarkBitmap.width）
setWatermark(watermarkBitmap, txRect)
// Set the green screen file: The formats available in Android system are supported. That is, images in jpg/png and videos in mp4/3gp are supported.
setGreenScreenFile(path, isLoop);
// Set the beautifying style: Smooth, natural, and hazy
setBeautyStyle(style);

// Whether to enable flashlight. The parameter mFlashOn indicates whether to enable flashlight. Flashlight is disabled by default.
mTXCameraRecord.toggleTorch(mFlashOn);
// Get the maximum focal length supported by the camera
mTXCameraRecord.mTXCameraRecord();
// Set the focal length
mTXCameraRecord.setZoom(value);

//////////////////////////////////////////////////////////////////////////
//                      Related to background music
//////////////////////////////////////////////////////////////////////////
// Set the background music playback callback API .TXRecordCommon.ITXBGMNotify
setBGMNofify(notify);
// Play background music
mTXCameraRecord.playBGM(path);
// Stop background music
mTXCameraRecord.stopBGM();
// Pause background music
mTXCameraRecord.pauseBGM();
// Resume background music
mTXCameraRecord.resumeBGM();
// Set the microphone volume to control the microphone volume when playing the mixed background music.
// Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value.
mTXCameraRecord.setMicVolume(x);
// Set the background music volume to control the background music volume when playing the mixed background music.
// Normal volume is 1. The recommended value is 0-2. If you need to turn up the background music volume, you can set it to a larger value.
setBGMVolume(x);

//////////////////////////////////////////////////////////////////////////
//                       The following special effects are only supported by the VIP edition
// (These effects use the intellectual properties of YouTu team and are supported only by the VIP SDK edition. We cannot provide them for free)
//////////////////////////////////////////////////////////////////////////

// Configure motion effect stickers. The motion effect file motionTmplPath is located in: An empty string "" means to disable motion effect.
mTXCameraRecord.setMotionTmp(motionTmplPath);
// Set the green screen file: The formats available in Android system are supported. That is, images in jpg/png and videos in mp4/3gp are supported.
mTXCameraRecord.setGreenScreenFile();
// Set eye enlargement effect (0-9)
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);
// Set face slimming effect (0-9)
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);
// Set V-shaped face effect (0-9)
mTXCameraRecord.setFaceVLevel(level)
// Set chin stretching or contracting effect (0-9)
mTXCameraRecord.setChinLevel(scale)
// Set face contracting effect (0-9)
mTXCameraRecord.setFaceShortLevel(level)
// Set nose narrowing effect (0-9)
mTXCameraRecord.setNoseSlimLevel(scale)

```


### 3. Record File
Call the startRecord function in TXUGCRecord to start recording process, and call the stopRecord function to stop recording process. Be sure to call these two functions in pairs.
```java
mTXCameraRecord.startRecord();
mTXCameraRecord.stopRecord();
```

The feedback of the recording process and result is provided by the TXRecordCommon.ITXVideoRecordListener API (defined in TXRecordCommon.java):
- "onRecordProgress" is used to provide the feedback of the recording progress. The parameter "millisecond" indicates record length (in ms):
```java
@optional
void onRecordProgress(long milliSecond);
```
- "onRecordComplete" provides the feedback of the recording result. The fields "retCode" and "descMsg" indicate error code and error message. "videoPath" is the path of the recorded short video file. "coverImage" is the first frame image of the short video (automatically captured, this image can be used when you publish the video).
```java   
@optional
void onRecordComplete(TXRecordResult result);
```
- "onRecordEvent" recording event callback includes the event ID and event-related parameter (key, value) formats.
```java   
@optional
void onRecordEvent(final int event, final Bundle param);
```

### 4. Multi-fragment Recording and Deletion

```java
//A video fragment is generated after pauseRecord is performed, which can be obtained in TXUGCPartsManager. 
mTXCameraRecord.pauseRecord();
// Resume video recording
mTXCameraRecord.resumeRecord();
//Get fragment management object
mTXCameraRecord.getPartsManager();
// Get the total duration of all current video fragments
mTXUGCPartsManager.getDuration();
// Get the paths of all video fragments
mTXUGCPartsManager.getPartsPathList();
// Delete the last video fragment
mTXUGCPartsManager.deleteLastPart();
// Delete a specified video fragment
mTXUGCPartsManager.deletePart(index);
// Delete all video fragments
mTXUGCPartsManager.deleteAllParts();
```

### 5. Preview File

Use [Video Playback](https://cloud.tencent.com/document/product/584/9373) to preview the generated MP4 file. When calling startPlay, you need to specify playback type as [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9373#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.E5.99.A86).

### 6. Obtain License Information
The verification of short video license is added in the new version of SDK. If you fail to pass the verification, you can use the API to query specific information in the license.

``` 
mTXCameraRecord.getLicenceInfo();
``` 

