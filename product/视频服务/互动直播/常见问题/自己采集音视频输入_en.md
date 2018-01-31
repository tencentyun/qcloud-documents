

# Custom Video/Audio Input Streams

## Custom Audio Data

The following is a flow chart on how to process local audio data:

> For Viewer
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audio_member.jpg)

> For VJ
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audio_host.jpg)

As shown in the above diagram, developers can intercept the data in any step and process them accordingly.

### Mix

#### Android

1. Register callback

API | Description
:--|:--:
registAudioDataCallbackWithByteBuffer | The callback function to register a specific data type

Parameter type | Description
:--|:--:
int | Type of audio data (see above diagram)
RegistAudioDataCompleteCallbackWithByteBuffer | The callback function to direct to the audio data defined by the App

```java
ILiveSDK.getInstance().getAvAudioCtrl().registAudioDataCallbackWithByteBuffer(
    AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOURCE_MIXTOSEND, mAudioDataCompleteCallbackWithByffer);
```

2. Add audio data to be mixed

```java
private AVAudioCtrl.RegistAudioDataCompleteCallbackWithByteBuffer mAudioDataCompleteCallbackWithByffer = 
      new AVAudioCtrl.RegistAudioDataCompleteCallbackWithByteBuffer() {
        @Override
        public int onComplete(AVAudioCtrl.AudioFrameWithByteBuffer audioFrameWithByteBuffer, int srcType) {
            if (srcType==AudioDataSourceType.AUDIO_DATA_SOURCE_MIXTOSEND) {
                synchronized (obj){
                  /*************************************************
                    Write audio data to be mixed into audioFrameWithByteBuffer
                  *************************************************/
                }
            }
            return AVError.AV_OK;
        }
    };
```

#### iOS

**Audio pass-through** is mainly used to reprocess data captured by microphone in an LVB. Usually it's used to mix background sound in a live room. Audio data passed-through can only be of specific formats, and the default one is QAVAudioFrameDesc = {48000, 2, 16}. It usually is used in the following two ways:<br>
1. Microphone pass-through: Both the microphone side (the side capable of inputting upstream audio data) and the others receive the audio stream. The following codes are used to set microphone pass-through:

```
// Set audio processing callback
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:self];

// Note: It is QAVAudioDataSource_MixToSend
[[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToSend];
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataFormat:QAVAudioDataSource_MixToSend desc:pcmdesc];

```

2. Speaker pass-through: When the speaker side is configured, only the speaker side can receive the audio stream. The following codes are used to set speaker pass-through:

```
 // Set audio processing callback
 [[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:self];
 
 // Note: It is QAVAudioDataSource_MixToPlay
 [[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToPlay];
 [[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataFormat:QAVAudioDataSource_MixToPlay desc:pcmdesc];

```

3. Callback handling of audio pass-through: pay attention to the comments in three callbacks.

```
- (QAVResult)audioDataComes:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // Mainly used to save audio data of an LVB
    return QAV_OK;
}

- (void)handle:(QAVAudioFrame **)frameRef withPCM:(NSData *)data offset:(NSInteger *)offset
{
	// Illustrate how to add passed-through data to QAVAudioFrame
    const QAVAudioFrame *aFrame = *frameRef;
    NSInteger off = *offset;
    NSInteger length = [aFrame.buffer length];
    if (length)
    {
        NSMutableData *pdata = [NSMutableData data];
        const Byte *btyes = [data bytes];
        
        while (pdata.length < length)
        {
            if (off + length > data.length)
            {
                const Byte *byteOff = btyes + off;
                [pdata appendBytes:byteOff length:data.length - off];
                off = 0;
            }
            else
            {
                const Byte *byteOff = btyes + off;
                [pdata appendBytes:byteOff length:length];
                off += length;
            }
        }
        
        if (pdata.length == length)
        {
            *offset = off;
            
            const void *abbytes = [aFrame.buffer bytes];
            memcpy((void *)abbytes, [pdata bytes], length);
        }
    }
}

- (QAVResult)audioDataShouInput:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // The main callback of mixed input (microphone and speaker)
    
    // Microphone pass-through handling
    if (type == QAVAudioDataSource_MixToSend)
    {
    	// self.micAudioTransmissionData is the audio data to be passed-through. By default, the format is QAVAudioFrameDesc = {48000, 2, 16}. When handling data from outside, pay attention to related parameters.
        if (self.micAudioTransmissionData)
        {
            NSInteger off = self.micAudioOffset;
            [self handle:&audioFrame withPCM:self.micAudioTransmissionData offset:&off];
            self.micAudioOffset = off;
        }
    }
    // Speaker pass-through handling
    else if (type == QAVAudioDataSource_MixToPlay)
    {
    // self.speakerAudioTransmissionData is the audio data to be passed-through. By default, the format is QAVAudioFrameDesc = {48000, 2, 16}. When handling data from outside, pay attention to related parameters.
        if (self.speakerAudioTransmissionData)
        {
            NSInteger off = self.speakerAudioOffset;
            [self handle:&audioFrame withPCM:self.speakerAudioTransmissionData offset:&off];
            self.speakerAudioOffset = off;
        }
    }
//    NSLog(@"%@", audioFrame.buffer);
    return QAV_OK;
}

- (QAVResult)audioDataDispose:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // Mainly used to implement voice changer
    return QAV_OK;
}
```

4. Unregister pass-through callbacks when exiting a live room

```

// Unregister all audio pass-through callbacks.
[[[ILiveSDK getInstance] getAVContext].audioCtrl unregisterAudioDataCallbackAll];
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:nil];

// Or call AVSDK APIs to unregister different types of pass-through callbacks.
// For more information, please see QAVAudioCtrl in QAVSDK.framework.
/*!
 @abstract      Unregister audio data callbacks
 @discussion    The type of audio data to register for listening to. For more information, please see QAVAudioDataSourceType.
 @param         type            The type of audio data to unregister for listening to. For more information, please seeQAVAudioDataSourceType
 @return        QAV_OK is returned if the operation succeeds. For other cases, please see QAVResult.
 @see           QAVAudioDataSourceType QAVResult
 */
- (QAVResult)unregisterAudioDataCallback:(QAVAudioDataSourceType)type;

        
```

### Customizing Audio Capture

#### This feature was introduced in AVSDK 1.8.4. These currently unwieldy steps will be improved in the future.

1. The audio/video scenario of VJ hosts and join broadcasting audience should be set to "broadcasting" (to acquire local microphone permissions) in spear role configuration of Tencent Cloud backend. Alternatively, "viewing" could be set to avoid occupying local microphones.
2. Microphones and speakers should be enabled when joining a room.
3. After joining a room, call the interface AVAudioCtrl.changeAudioCategory to switch to "viewing" scenario (skip this step if the scenario has already been set to "viewing" in step 1).
4. Call enableExternalAudioDataInput to enable custom audio capture.
5. Call fillExternalAudioFrame to pass externally captured audio data to AVSDK.
6. All above interfaces should be called in the main thread.



### Customizing Video Data Capture

Below is a flow chart illustrating the process of custom video data capture:    

![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/custom_flow.png)

### Android

1. Enable camera, and call enableExternalCapture to prepare.

2. Get raw video data and start processing.
Having obtained the raw data from the system, you can now pre-process them, such as applying whitening, beauty filters, or performing face recognition. The video data after pre-process need to be rendered by the developers and are unrelated to iLiveSDK.

API | Description
:--|:--:
enableExternalCapture | Enable/disable external video capture devices.

Parameter type | Description
:--|:--:
boolean | true means enabled; false means disabled.
boolean | true means that local rendering is enabled; false means disabled.
EnableExternalCaptureCompleteCallback | A class that calls a callback function defined by the App

```java
ILiveSDK.getInstance().getAvVideoCtrl().enableExternalCapture(false, true
      new AVVideoCtrl.EnableExternalCaptureCompleteCallback(){
@Override
protected void onComplete(boolean enable, int result) {
super.onComplete(enable, result);
}
});
```

2. Get raw video data and start processing.

3. Upload video data

API | Description
:--|:--:
fillExternalCaptureFrame | Pass the video data captured by external devices to the SDK

Parameter type | Description
:--|:--:
byte array | Image data
int | Length of the array
int | byteperRow of the image. Only used by RGB32 video. Normally it is 4 times the width of the video. Pay special attention if a special resolution is used.
int | Width of the video image
int | Height of the video image
int | Video image rendering orientation. Orientation could be 0, 1, 2, or 3, meaning that the video should be rotated by 0, 90, 180 or 270 degrees to be upright, respectively. |
int | Color format of the video image. For specific values, refer to EXTERNAL_FORMAT_I420, EXTERNAL_FORMAT_RGBA, etc.
int | Video source type. Only VIDEO_SRC_TYPE_CAMERA is supported.

```java
// The video image needs to be rotated by 90 degrees.
ILiveSDK.getInstance().getAvVideoCtrl().fillExternalCaptureFrame(data, data.length, 0,
    mCameraSize.width, mCameraSize.height, 3, AVVideoCtrl.COLOR_FORMAT_I420, AVView.VIDEO_SRC_TYPE_CAMERA);
```


### Customizing Pre-processing of Video Data

      
![](https://mc.qcloudimg.com/static/img/0baaafa05e5549ff30f584ac9424f756/11.png)


1. Intercepting AVSDK camera data

| API Name |  Description  |
|---------|---------|
| **setLocalVideoPreProcessCallback** | Set the pre-processing function for local camera video data |
##### Implementation:
<pre>

/*
Function description:
a. After pre-processing camera data, usually you only need to write the processed data back to VideoFrame.data, while keeping the data format and size of the video.
b. Usually, you don't need to modify other properties.

Return values: true: successful false: failed
*/
boolean bRet = ILiveSDK.getInstance().getAvVideoCtrl().setLocalVideoPreProcessCallback(new AVVideoCtrl.LocalVideoPreProcessCallback(){

                    @Override
                    public void onFrameReceive(AVVideoCtrl.VideoFrame var1) {
						Log.d("SdkJni", "base class SetLocalPreProcessCallback.onFrameReceive");
					}
}
</pre>

##### Parameter description for callback data type AVVideoCtrl.VideoFrame:

| Parameter | Description |
|---------|---------|
| **byte[] data** | Video data (a. Currently Android supports only I420 data output; b. After pre-processing the data, write them back to property data; as long as the video format doesn't change, AVSDK can properly generate previews and encode. |
| **int dataLen** | Length of the video data |
| **int width** | Width of the video |
| **int height** | Height of the video |
| **int rotate** | Orientation of the video image. Orientation could be 0, 1, 2, or 3, meaning that the video should be rotated by 0, 90, 180 or 270 degrees to be upright, respectively. |
| **int videoFormat** | Video format. Currently I420, NV21, NV12, RGB565, RGB24 and ARGB are supported. 0 is the default value. |
| **String identifier** | Identifier of room members |
| **int srcType** | Video capture source. NONE = 0 CAMERA = 1 SCREEN = 2 MEDIA = 3 |
| **long timeStamp** | Time-stamp of the video frame. This property is filled automatically by the SDK with UTC time. 0 is an invalid value. |

2. Pre-processing video data
Having obtained the camera video data from AVSDK, you can now pre-process them, such as applying whitening, beauty filters, or performing face recognition. After pre-proccesing, pass the data back to AVSDK by AVVideoCtrl.VideoFrame.data. AVSDK will then automatically render and encode the data.

3. Stop intercepting AVSDK camera data
##### Implementation:
<pre>
// true: successful  false: failed

boolean bRet = ILiveSDK.getInstance().getAvVideoCtrl().setLocalVideoPreProcessCallback(null);
</pre>

 ------
### iOS
Customizing video capture is mainly used to pre-process raw data, such as when you need to implement face recognition, beauty filter and dynamic effects. Below is an example of adding dynamic effects by customizing video capture:

![](http://mc.qcloudimg.com/static/img/f532b2ba735514ed2faff41cf805a817/image.png)

**Note: Dynamic effects are implemented by developers and are not related to this documentation. Besides dynamic effects, you can pre-process the raw data in any way you want.**

1. Process description
Note that in customizing video capture, the capture process is independent of iLiveSDK and is not related to the SDK in any way. During the process, iLiveSDK's role is to pass-through data and render remote data. The process introduced here is: ***Customizing video capture -> Video data is passed to iLiveSDK -> Remote end receives the video frames and starts rendering***
![](http://mc.qcloudimg.com/static/img/5311e0e74ef71db124c291be01f8b5da/image.png)


2. Preparation for capture
***After joining the room and before capture starts***

| API | Description |
|---|---|
| enableExternalCapture: | Enable (disable) external video capture devices. These devices need to be enabled in custom capture. The returned value of QAV_OK indicates a successful operation. After this method is called, camera APIs ***can't*** be enabled again by calling iLiveSDK; furthermore, whitening and beauty filter of iLiveSDK would stop functioning.

| Parameter Type | Parameter Name | Description |
|---|---|---|
| BOOL | isEnableExternalCapture | Whether to enable external video capture devices. Pass in YES in custom capture |
| BOOL | shouldRender | Whether SDK will render input stream video data.The value is "YES" or "NO" |

* Example:

```
    QAVContext *context = [[ILiveSDK getInstance] getAVContext];
    [context.videoCtrl enableExternalCapture:YES shouldRender:NO];
```

3. Custom capture
Custom capture uses system level APIs, which are unrelated to iLiveSDK. Here we only briefly introduce relevant system classes and methods.

| System Class or Method | Description |
|---|---|
| AVCaptureSession | Capture video |
| AVCaptureDeviceInput | Video input stream |
| AVCaptureVideoDataOutput | Video output stream |
| captureOutput: didOutputSampleBuffer: fromConnection: | Callback function for captured video. The captured video data are passed to this interface for you to pre-process. |

4. Processing after Capture
Having obtained the raw data (of type `CMSampleBufferRef`) from the system, you can now pre-process them, such as applying whitening, beauty filters, or performing face recognition. The video data after pre-process need to be rendered by the developers and are unrelated to iLiveSDK.

5. iLiveSDK Pass-through

| API | Description |
|---|---|
| fillExternalCaptureFrame: | Pass captured video frame to audio/video SDK. The returned value of QAV_OK indicates a successful operation |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| QAVVideoFrame | frame | A type of AVSDK vedio frame. Developers need to convert custom-captured video data to this type. |
*Example:

```
    QAVVideoCtrl *videoCtrl = [[ILiveSDK getInstance] getAvVideoCtrl].videoCtrl;
    QAVResult result = [videoCtrl fillExternalCaptureFrame:frame];
```

6. Remote Rendering

| API | Description |
|---|---|
| OnVideoPreview: | Callback for remote video data. It receives remote frame data, and renders them with iLiveSDK's rendering APIs. Developers only need to specify the rendering area. For more information about rendering, please see [the new version of FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos/tree/master) |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| QAVVideoFrame | frameData | A type of AVSDK video frame |

7. Notes
> *1 OpenGL and iLiveSDK should not be used together to render custom-captured video data. Otherwise, the App may crash. In other words, there should be two views on the interface: one to render custom-captured video data, and the other to render QAVVideoFrame objects.

> *2 When converting to QAVVideoFrame, color_format attribute should be AVCOLOR_FORMAT_NV12.
srcType attribute should be QAVVIDEO_SRC_TYPE_CAMERA.

