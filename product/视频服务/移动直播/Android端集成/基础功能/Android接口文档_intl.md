The following are lists of main APIs from the Tencent Video Cloud Android SDK, which are organized under TXLivePusher and TXLivePlayer classes, event callbacks and constant definition. For a specific API, please see [API Documentation](http://imgcache.qq.com/open/qcloud/video/act/liteav_android_doc/index.html).


## TXLivePusher

##### APIs

| Name | Description |
| ---------------------------------------- | --------------------------------- |
| setConfig(TXLivePushConfig config) | Sets push configuration |
| getConfig() | Gets push configuration |
| setPushListener(ITXLivePushListener listener) | Sets status callback on push events |
| setVideoProcessListener(VideoCustomProcessListener listener) | Sets callback for custom video processing |
| startCameraPreview(TXCloudVideoView view) | Enables camera preview |
| stopCameraPreview(isNeedClearLastImg) | Disables camera preview |
| startPusher(String url) | Starts push |
| stopPusher() | Stops push |
| pausePusher() | Pauses push |
| resumePusher() | Resumes push |
| startScreenCapture() | Starts screencap |
| stopScreenCapture() | Stops screencap |
| setVideoQuality(quality, adjustBitrate, adjustResolution) | Sets video quality and whether Qos traffic control or dynamic resolution is allowed |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel) | Sets beauty filter style, dermabrasion level, whitening level, and blushing level. |
| switchCamera() | Switches between front and rear cameras. Dynamic switching is supported during push |
| setMute(bool mute) | Enables Mute |
| setRenderRotation(rotation) | Sets the clockwise rotation of image |
| setMirror(enable) |  Sets horizonal mirrioring at the viewer end |
| playBGM(path)| Plays background music for mixing processing |
| stopBGM() | Stops background music |
| pauseBGM() | Pauses background music |
| resumeBGM() | Resumes background music |
| getMusicDuration(path) | Gets the duration of a music file |
| setMicVolume() | Sets microphone volume for audio mixing |
| setBGMVolume() | Sets background music volume for audio mixing |
| startRecord(videoFilePath) | Starts video recording |
| stopRecord() | Stops video recording |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | Sets video recording callback |
| snapshot(ITXSnapshotListener) | Captures video screen |
| setVideoProcessListener(VideoCustomProcessListener listener) | Set callback for custom video processing |
| sendCustomVideoData(buffer, bufferType, w, h) | Pushes custom video data |
| sendCustomPCMData(pcmBuffer) | Pushes custom audio data |


## TXLivePushConfig

##### APIs

| Name | Description |
| ------------------------------------- | ------------------- |
| enableAEC(enable) | Enables AEC (for joint broadcasting only) |
| enableNearestIP(enable) | Enables nearest route first |
| enablePureAudioPush(enable) | Enables audio-only push |
| enableScreenCaptureAutoRotate(enable) | Sets whether to enable adaptive rotation during screencap |
| setConnectRetryCount(count) | Sets the number of reconnection attempts at the pusher end |
| setConnectRetryInterval(interval) | Sets the interval between reconnection attempts at the pusher end |
| setEyeScaleLevel(level) | Sets eye enlarging effect |
| setFaceSlimLevel(level) | Sets face slimming effect |
| setFrontCamera(front) | Sets whether to use the front camera |
| setHomeOrientation(homeOrientation) | Sets rotation for captured videos |
| setPauseFlag(flag) | Sets push options for a pause of backend push |
| setPauseImg(img) | Sets the image played at the pause of backend push |
| setPauseImg(time, fps) | Sets how the backend plays the image for pause during the pause of backend push |
| setVideoEncodeGop(gop) | Sets GOP for video coding |
| setVideoResolution(resolution) | Sets video frame rate |
| setWatermark(watermark, x, y, width) | Sets watermark image attributes |
| setWatermark(watermark, x,y) | Sets watermark image attributes |


## TXLivePlayer

##### APIs

| Name | Description |
| ---------------------------------------- | ------------------- |
| setConfig(TXLivePlayConfig config) | Sets playback configuration |
| getConfig() | Gets playback configuration |
| setPlayerView(TXCloudVideoView view) | Binds the rendering view to your player |
| setPlayListener(ITXLivePlayListener listener) | Sets a callback of TXLivePlayer |
| startPlay(url, type) | Starts playback |
| stopPlay(isNeedClearLastImg) | Stops playback |
| pause() | Pauses playback |
| resume() | Resumes playback |
| enableHardwareDecode(enable) | Enables or disables hard decoding of video playback |
| isPlaying() | Indicates whether the playback is in progress. |
| setRenderMode(mode) | Sets the rendering (filling) mode of image |
| setRenderRotation(rotation) | Sets the clockwise rotation of image |
| startRecord(recordType) | Starts video recording |
| stopRecord() | Stops video recording |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | Sets video recording callback |
| setMute(mute) | Sets whether to enable Mute |
| snapshot(TXLivePlayer.ITXSnapshotListener listener) | Captures video images |
| setSurface(Surface surface) | Sets rendering surfaces |
| addVideoRawData(byte[] yuvBuffer)  | Sets a receiving buffer for the playback of YUV data |
| setVideoRawDataListener(ITXVideoRawDataListener listener) | Sets a callback for video YUV data |
| setAudioRawDataListener(ITXAudioRawDataListener listener) | Sets a callback for audio PCM data |


## TXLivePlayConfig

##### APIs

| Name | Description |
| --------------------------------- | --------------------- |
| enableAEC(enable) | Enables AEC (for joint broadcasting only) |
| setConnectRetryCount(count) | Sets the number of reconnection attempts at the player |
| setConnectRetryInterval(interval) | Sets the interval between reconnection attempts at the the player |
| setEnableMessage(enable) | Sets whether to enable message channel |
| setAutoAdjustCacheTime(bAuto) | Sets whether to automatically adjust the player caching time according to network conditions |
| setCacheTime(time) | Sets player caching time |
| setMaxAutoAdjustCacheTime(time) | Sets the maximum player caching time for automatic adjustment |
| setMinAutoAdjustCacheTime(time) | Sets the minimum player caching time for automatic adjustment |



## Details of TXLivePusher APIs

#### 1.setConfig(TXLivePushConfig config)

API details: void setConfig(TXLivePushConfig config)

Sets pusher configuration.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ------------------ | ------- |
| config | TXLivePushConfig * | Pusher configuration |


- **Sample code**: 

```
TXLivePushConfig mLivePushConfig = new TXLivePushConfig();
mLivePushConfig.setBeautyFilter(...);
......
mLivePusher.setConfig(mLivePushConfig);
```



#### 2.getConfig() 

API details: TXLivePushConfig getConfig() 

Gets pusher configuration. 


- **Sample code**: 

```
mLivePusher.getConfig() 
```



#### 3.setPushListener(ITXLivePushListener listener) 

API details: void setPushListener(ITXLivePushListener listener)

Sets status callback on push events. For specific event and its status, please see descriptions on push events.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| listener | ITXLivePushListener | Callback API for push event |

- **Sample code**: 

```
mLivePusher.setPushListener(new ITXLivePushListener() {
    @Override
    public void onPushEvent(int i, Bundle bundle) {
        // ...
    }

    @Override
    public void onNetStatus(Bundle bundle) {
        // ...
    }
});
```



#### 4.setVideoProcessListener(VideoCustomProcessListener listener)

API details: void setVideoProcessListener(VideoCustomProcessListener listener)

Sets callbacks for custom video processing, which are implemented before VJ's preview and encoding so that you can customize beauty filters or add video effects. 

- **Parameter description**

| Parameter | Type | Description |
| -------- | -------------------------- | --------- |
| listener | VideoCustomProcessListener | Callback for custom video processing |

- **Sample code**: 

```
public interface VideoCustomProcessListener {

    /**
    * Value-added callback for face coordinates
    * @param points   Normalizing face coordinates, of which every two values represent x and y values of a point P. Value range[0.f, 1.f]
    */
    void onDetectFacePoints(float[] points);
    
    /**
    * Perform a callback in the OpenGL thread, where you can conduct the secondary processing of captured images.
    * @param textureId  Texture ID
    * @param width      Width of texture
    * @param height     Height of texture
    * @return           Texture returned to SDK
    * Note: The texture type called back from the SDK is GLES20.GL_TEXTURE_2D, and the one returned by the API to the SDK must also be GLES20.GL_TEXTURE_2D.
    */
    int onTextureCustomProcess(int textureId, int width, int height);

    /**
    * Perform a callback in the OpenGL thread, where you can release the OpenGL resources created.
    */
    void onTextureDestoryed();
}
```



#### 5. startCameraPreview(TXCloudVideoView view) 

API details: void startCameraPreview(TXCloudVideoView view) 

Enables camera preview. The front camera is used by default, which can be set through TXLivePushConfig.setFrontCamera(). The API supports switching between different TXCloudVideoView during push. You should call stopCameraPreview() first before startCameraPreview().

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---------------- | ----------- |
| view | TXCloudVideoView | Rendering view of video preview |


- **Sample code**: 

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```



#### 6. stopCameraPreview(isNeedClearLastImg)                                

API details: void stopCameraPreview(boolean isNeedClearLastImg)

Disables camera preview. You can keep or clear the last frame of the screen. It is recommended to keep it if you stay on the push page after stopping preview; otherwise, please clear it.

Note: Disabling camera is a synchronous operation, which normally takes 100 ~ 200 ms, or more time on some handsets. You can call this API in an asynchronous thread to lessen the time impact.

- **Parameter description**

| Parameter | Type | Description |
| ------------------ | ------- | ---------------------------------------- |
| isNeedClearLastImg | boolean | Indicates whether to clear the last frame. "true": Yes; "false": No. |


- **Sample code**: 

```
mLivePusher.stopCameraPreview(true);
```



#### 7.startPusher(url)

API details: void startPusher(String url)

Starts push. You need to call startCameraPreview to enable camera preview before calling startPush. Otherwise, your data cannot be pushed.

Note: A push URL is exclusive, that is, a push URL can only be used by one pusher for pushing streams at a time.


- **Parameter description**

| Parameter | Type | Description |
| ---- | ------------ | ---------------------------------------- |
| url | const String | A valid push URL that supports RTMP protocol. The URL starts with "rtmp://". For more information on how to obtain Tencent Cloud push URL, please see [DOC](https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc"). |

- **Sample code**: 

```
mLivePusher.startPusher(rtmpUrl.trim());
```



#### 8.stopPusher()

API details: void stopPusher()

Stops push.

- **Sample code**: 

```
mLivePusher.stopPusher();
```



#### 9.pausePusher()

API details: void pausePusher()

Pauses pushing data from camera. If the App is switched to background during push, you can call pausePusherto enable the SDK stop capturing images from your camera while pushing a pause image plus mute data. You can set the pause image via TXLivePushConfig.setPauseImg(). When no pause image is set, a solid black image is used.

- **Sample code**: 

```
mLivePusher.pausePusher();
```



#### 10.resumePusher()

API details: void resumePusher()

Resumes pushing data from camera. If you call resumePusher after the App is switched back to foreground, the SDK stops pushing the pause image and resumes capturing images from camera and audio from microphone to push streams.

- **Sample code**: 

```
mLivePusher.resumePusher();
```



#### 11.startScreenCapture()

API details: void startScreenCapture()

Enables screen capturing. Since screencap is implemented based on the native capabilities of the Android system, for security reasons, Android will warn the user before the screencap is initiated by displaying a prompt: "an App will capture all the contents on your screen".

Note: This API takes effect just on Android API 21. Screencap and camera preview are mutually exclusive, which means only one of them can be effective at a time.

- **Sample code**: 

```
mLivePusher.startScreenCapture();
```



#### 12.stopScreenCapture()

API details: void stopScreenCapture()

Stops screen capturing.

- **Sample code**: 

```
mLivePusher.stopScreenCapture();
```



#### 13.setVideoQuality(quality, adjustBitrate, adjustResolution) 

API details: void setVideoQuality(int quality,  boolean adjustBitrate,  boolean adjustResolution)

Sets the pushed image clarity. The SDK provides 6 basic options for you to choose based on VJ scenarios. Each option corresponds to a different resolution and bitrate. Based on our rich experience with our huge customer base, We can help you find the most suitable resolution and bitrate and gain very good video quality. Among them, STANDARD, HIGH, and SUPER are intended for LVB mode, MAIN_PUBLISHER and SUB_PUBLISHER are intended for primary and secondary screens of joint broadcasting, and VIDEOCHAT is used for real-time audio/video.

The specific values are as follows:

- **Parameter description**

| Parameter | Type | Description |
| ---------------- | ------- | -------- |
| quality | int | video quality option |
| adjustBitrate | boolean | Dynamic bitrate switch |
| adjustResolution | boolean | Dynamic resolution switch |

- **Description on video quality options**

| Option | Constant Value | Resolution | Bitrate |
| -------- | ---------------------------------------- | -------- | -------- |
| STANDARD | TXLiveConstants.VIDEO_QUALITY_STANDARD_DEFINITION | 360*640  | 300~800  |
| HIGH     | TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION | 540*960  | 600~1500 |
| SUPER    | TXLiveConstants.VIDEO_QUALITY_SUPER_DEFINITION | 720*1280 | 600~1800 |

- **Sample code**: 

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION, true, true);;
```



#### 14. setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel)

API details: boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel)

Sets beauty filter style, dermabrasion level, whitening level, and blushing level.

- **Parameter description**

| Parameter | Type | Description |
| -------------- | ---- | ---------------------------------------- |
| style | int | Dermabrasion style: 0: Smooth 1: Natural 2: Hazy |
| beautyLevel | int | Dermabrasion level: Value range: 0-9. 0 means disabling beauty filter. Default is 0, i.e., disabling beauty filter |
| whiteningLevel | int | Whitening level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing |
| ruddyLevel | int | Blushing level: Value range: 0-9. 0 means disabling blushing. Default is 0, i.e., disabling blushing |


- **Sample code**: 

```
mLivePusher.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```



#### 15.switchCamera()

API details: void switchCamera()

Switches between cameras. When the front camera is in use, calling this API enables a switch from the front camera to the rear camera, and vice versa. This API takes effect only if it is called after camera preview (startCameraPreview(TXCloudVideoView)) is enabled. The front camera is used by default when the SDK enables camera preview.

- **Sample code**: 

```
mLivePusher.switchCamera();
```



#### 16.setMute(mute)

API details: void setMute(mute)

Enables Mute. Once Mute is enabled, the SDK shifts from pushing microphone-collected sounds to pushing mute.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------- | ---- |
| mute | boolean | Whether to enable mute |

- **Sample code**: 

```
mLivePusher.setMute(true);
```



#### 17.setRenderRotation(rotation)   

API details: void setRenderRotation(int rotation)   

Sets the clockwise rotation for local image previews. This API is often used with LivePushConfig.setHomeOrientation() for pushing with your device in landscape mode.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---- | ----------- |
| rotation | int | Its value is normally 0 or 90. |

- **Sample code**: 

```
// When your device is in portrait mode, pushing is done with portrait orientation and local rendering is done with 0 degree offset to the vertical line.
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN);
mLivePusher.setRenderRotation(0);

// When your device is in landscape mode, pushing is done with landscape orientation and local rendering is done with 90 degree offset to the vertical line.
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT);
mLivePusher.setRenderRotation(90);
```



#### 18.setMirror(enable)  

API details: void setMirror(boolean enable)

Sets horizontal mirroring at the viewer end. Note that this API only works on the viewer end, not the VJ (pusher) end. The mirroring effect is always seen from the pusher end. The image is seen as mirrored from the pusher end when the front camera is in use, and non-mirrored when the rear camera is in use.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ------- | -------------------------------------- |
| enable | boolean | "true" indicates the image is seen as mirrored, and "false" indicates the image is seen as non-mirrored. |

- **Sample code**: 

```
//The image is seen as mirrored at the viewer end
mLivePusher.setMirror(true);
```



#### 19.playBGM(path)

API details: boolean playBGM(String path)

Plays background music. This API is used for audio mixing, for example, mixing background music with sounds collected from the microphone for playback. If the playback is successful, a value of "true" is returned. If the playback fails, a value of "false" is returned.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---------------- |
| path | String | The background music file is located in the absolute path in the phone |

- **Sample code**: 

```
mLivePusher.playBGM(musicFilePath);
```



#### 20.stopBGM()

API details: boolean stopBGM()

Stops background music. If the playback ends successfully, a value of "true" is returned. If the playback fails to end, a value of "false" is returned.


- **Sample code**: 

```
mLivePusher.stopBGM();
```



#### 21.pauseBGM()

API details: boolean pauseBGM()

Pauses background music. If the playback pauses successfully, a value of "true" is returned. If the playback fails to pause, a value of "false" is returned.


- **Sample code**: 

```
mLivePusher.pauseBGM();
```



#### 22.resumeBGM()

API details: boolean resumeBGM()

Resumes background music. If the playback resumes successfully, a value of "true" is returned. If the playback fails to resume, a value of "false" is returned.


- **Sample code**: 

```
mLivePusher.resumeBGM();
```

#### 23.getMusicDuration(path)

API details: int getMusicDuration(java.lang.String path)

Gets the duration (in ms) of a music file.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| path | Path to the music file | If path == null, get the duration of the current music. If path != null, get the duration of the music under the path. |

- **Sample code**: 
```
mLivePusher.getMusicDuration(path);
```


#### 24.setMicVolume()

API details: boolean setMicVolume(float x)

Sets microphone volume for audio mixing. If the microphone volume is set successfully, a value of "true" is returned. If the microphone volume fails to be set, a value of "false" is returned.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |


- **Sample code**: 

```
mLivePusher.setMicVolume(2f);
```



#### 25.setBGMVolume()

API details: boolean setBGMVolume(float x)

Sets background music volume for audio mixing. If the background music volume is set successfully, a value of "true" is returned. If the background music volume fails to be set, a value of "false" is returned.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ----- | ---------------------------------------- |
| x | float | Volume: Normal volume is 1. The recommended value is 0-2. If you need to turn up the volume, you can set it to a larger value. It is recommended to add a slider in the UI to allow VJs to set volume on their own |


- **Sample code**: 

```
mLivePusher.setBGMVolume(2f);
```



#### 26.startRecord(videoFilePath)

API details: int startRecord(final String videoFilePath)

Starts recording video. This API is used at the VJ end to save the pushed preview as a local file in real time.

Note: This API can be called only after the startpusher operation is successful. Additionally, the generated video files are managed by your applications, and the SDK does not clean them.

If the recording starts successfully, "0" is returned. If the recording is in progress, "-1" is returned. If the pushing has not started and the recording fails to start, "-2" is returned.

- **Parameter description**

| Parameter | Type | Description |
| ------------- | ------ | -------------------------------- |
| videoFilePath | String | The recorded videos are located in the absolute path in the phone. The caller should guarantee that the App has access to the path. |

- **Sample code**: 

```
String videoFile = Environment.getExternalStorageDirectory() + File.separator + "TXUGC/test.mp4";
mLivePusher.startRecord(videoFile);
```


#### 27.stopRecord()

API details: void stopRecord()

Stops recording video. The recording result is asynchronously notified by means of recording callback.

- **Sample code**: 

```
mLivePusher.stopRecord();
```



#### 28.setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

API details: void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

Sets video recording callback to receive the video recording progress and result.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | Video recording callback |

- **Sample code**: 

```
mLivePusher.setVideoRecordListener(new TXRecordCommon.ITXVideoRecordListener(){
    @Override
    public void onRecordEvent(int event, Bundle param) {
    }

    @Override
    public void onRecordProgress(long milliSecond) {
        Log.d(TAG, "record progress:" + milliSecond);
    }

    @Override
    public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
        if (result.retCode == TXRecordCommon.RECORD_RESULT_OK) {
            String videoFile        = result.videoPath;
            String videoCoverPic    = result.coverPath;
        } else {
            Log.d(TAG, "record error:" + result.retCode + ", error msg:" + result.descMsg);
        }
    }
});
```



#### 29.snapshot(ITXSnapshotListener)

API details: void snapshot(final ITXSnapshotListener listener)

Captures video images. This API is used to capture a frame of video in real time on VJ side.

Note: The screencap result will be notified to you through an asynchronous callback by the main thread.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------------- | -------- |
| listener | ITXSnapshotListener | Video image callback API |

- **Sample code**: 

```
mLivePusher.snapshot(new TXLivePusher.ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        //bmp A video frame
    }
});
```

#### 30.setAudioProcessListener(listener)

API details: void setAudioProcessListener(TXLivePusher.AudioCustomProcessListener listener)

Sets a callback for custom audio processing. The callback is executed before the audio data is sent to the encoder for encoding.

- **Sample code**: 
```
mLivePusher.setAudioProcessListener(new TXLivePusher.AudioCustomProcessListener() {
    @Override
    public void onRecordPcmData(byte[] data, long ts, int sampleRate, int channels, int bits) {
       // data - pcm data
        // ts - pcm timestamp
        // sampleRate - audio sample rate
        // channels - audio channels
        // bits - audio bits
    }
});
```


#### 31.sendCustomVideoData(buffer, bufferType, w, h)

API details: int sendCustomVideoData(byte[] buffer, int bufferType, int w, int h)

This API is used to populate the SDK with the video data you captured and processed. Only i420 format is supported. It's suitable for scenarios where you only want to use our SDK to encode and push stream. Before calling this API, do not call TXLivePusher's startCameraPreview.

Description of the returned results:

| Result | Description |
| ----- | ---------------------------------------- |
| >0 | Indicates a successful sending but with a high frame rate, which is higher than the rate set in TXLivePushConfig. Too high a rate will cause the bitrate of your video encoder exceeding the bitrate set in TXLivePushConfig. The returned value represents the time that the current YUV video frame is ahead of the set video frame. |
| 0 | Sent successfully |
| -1 | Invalid video resolution |
| -2 | The length of YUV data does not match that required for the set video resolution. |
| -3 | Invalid video format |
| -4 | Invalid length and width of video images, which are smaller than the required size |
| -1000 | Internal error with SDK |

- **Parameter description**

| Parameter | Type | Description |
| ---------- | ------ | ---------------------------------------- |
| buffer | byte[] | Video data |
| bufferType | int | Video format. Only TXLivePusher.YUV_420P and TXLivePusher.RGB_RGBA are supported. |
| w | int | Width of a video image |
| h | int | Height of a video image |

- **Sample code**: 

```
//The following is a simple example to get and push the video data called back from camera preview.
@Override
public void onPreviewFrame(byte[] data, Camera camera) {
    // Assume the video captured by the camera is in NV21 and the preview screen size is 1280X720.
    if (!isPush) {
    } else {
        // Start custom push.
        // Transcode the video to I420
        byte[] buffer = new byte[data.length];
        buffer = nv21ToI420(data, mPreviewWidth, mPreviewHeight);

        int customModeType = 0;
        customModeType |= TXLiveConstants.CUSTOM_MODE_VIDEO_CAPTURE;
        // The width and height of the resolution must be less than or equal to those of the preview screen. 
        // You can also select 480x640, but can't select 540x960, because the encoder cannot trim off the image if the height of the resolution (960) is greater than that of the preview screen (720).
        mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_TYPE_1280_720);
        mLivePushConfig.setAutoAdjustBitrate(false);
        mLivePushConfig.setVideoBitrate(1200);
        mLivePushConfig.setVideoEncodeGop(3);
        mLivePushConfig.setVideoFPS(15);
        mLivePushConfig.setCustomModeType(customModeType);
        mLivePusher.setConfig(mLivePushConfig);

        int result= mLivePusher.sendCustomVideoData(buffer, TXLivePusher.YUV_420P, mPreviewWidth, mPreviewHeight);
    }
}

/**
Transcode  * nv21 to I420
 * @param data
 * @param width
 * @param height
 * @return
 */
public static byte[] nv21ToI420(byte[] data, int width, int height) {
    byte[] ret = new byte[data.length];
    int total = width * height;

    ByteBuffer bufferY = ByteBuffer.wrap(ret, 0, total);
    ByteBuffer bufferU = ByteBuffer.wrap(ret, total, total / 4);
    ByteBuffer bufferV = ByteBuffer.wrap(ret, total + total / 4, total / 4);

    bufferY.put(data, 0, total);
    for (int i=total; i<data.length; i+=2) {
        bufferV.put(data[i]);
        bufferU.put(data[i+1]);
    }
    return ret;
}
```



#### 32.void sendCustomPCMData(pcmBuffer)

API details: void sendCustomPCMData(byte[] pcmBuffer)

This API is used to populate the SDK with the  audio data you captured and processed. Please use mono or dual channel PCM audio data in16-bit wide and at 48,000Hz. For audio in mono or dual channel, ensure that the length of the incoming PCM is 2048 or 4069 bytes respectively. This API is often used with sendCustomVideoData(buffer, bufferType, w, h).


- **Parameter description**

| Parameter | Type | Description |
| --------- | ------ | -------- |
| pcmBuffer | byte[] | pcm audio data |

- **Sample code**: 

```
//The following is a simple example to get the audio data captured through microphones.
AudioRecord mAudioRecord = null;
int mMinBufferSize = 0; // Minimum buffer size

private static final int DEFAULT_SOURCE = MediaRecorder.AudioSource.MIC;
// Sets the sampling rate to 48,000.
private static final int DEFAULT_SAMPLE_RATE = 48000;
// Supports mono-channel (CHANNEL_IN_MONO) and dual-channel (CHANNEL_IN_STEREO).
private static final int DEFAULT_CHANNEL_CONFIG = AudioFormat.CHANNEL_IN_STEREO;  
// Sets bit width.
private static final int DEFAULT_AUDIO_FORMAT = AudioFormat.ENCODING_PCM_16BIT;    

private boolean mIsCaptureStarted = false;
private volatile boolean mIsLoopExit = true;

private Thread mCaptureThread;
private OnAudioFrameCapturedListener mAudioFrameCapturedListener;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    // Enables audio capture.
    startCapture();
}

public interface OnAudioFrameCapturedListener {
    public void onAudioFrameCaptured(byte[] audioData);
}

public boolean isCaptureStarted() {
    return mIsCaptureStarted;
}

public void setOnAudioFrameCapturedListener(OnAudioFrameCapturedListener listener) {
    mAudioFrameCapturedListener = listener;
}

public boolean startCapture() {
    return startCapture(DEFAULT_SOURCE, DEFAULT_SAMPLE_RATE, DEFAULT_CHANNEL_CONFIG,
            DEFAULT_AUDIO_FORMAT);
}

public boolean startCapture(int audioSource, int sampleRateInHz, int channelConfig, int audioFormat) {

    if (mIsCaptureStarted) {
        Log.e(TAG, "audio Capture already started !");
        return false;
    }

    // SDK requires 4096 for dual channel and 2048 for mono.
    mMinBufferSize = 4096;
    if (mMinBufferSize == AudioRecord.ERROR_BAD_VALUE) {
        Log.e(TAG, "Invalid AudioRecord parameter !");
        return false;
    }
    Log.d(TAG , "getMinBufferSize = "+mMinBufferSize+" bytes !");

    mAudioRecord = new AudioRecord(audioSource,sampleRateInHz,channelConfig,audioFormat,mMinBufferSize);
    if (mAudioRecord.getState() == AudioRecord.STATE_UNINITIALIZED) {
        Log.e(TAG, "AudioRecord initialize fail !");
        return false;
    }

    mAudioRecord.startRecording();

    mIsLoopExit = false;
    mCaptureThread = new Thread(new AudioCaptureRunnable());
    mCaptureThread.start();

    mIsCaptureStarted = true;
    Log.d(TAG, "Start audio capture success !");

    return true;
}

public void stopCapture() {
    if (!mIsCaptureStarted) {
        return;
    }

    mIsLoopExit = true;
    try {
        mCaptureThread.interrupt();
        mCaptureThread.join(1000);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }

    if (mAudioRecord.getRecordingState() == AudioRecord.RECORDSTATE_RECORDING) {
        mAudioRecord.stop();
    }

    mAudioRecord.release();

    mIsCaptureStarted = false;
    mAudioFrameCapturedListener = null;

    Log.d(TAG, "Stop audio capture success !");
}

private class AudioCaptureRunnable implements Runnable {
    @Override
    public void run() {
        while (!mIsLoopExit) {
                
            byte[] buffer = new byte[mMinBufferSize];

            int ret = mAudioRecord.read(buffer, 0, mMinBufferSize);
            if (ret == AudioRecord.ERROR_INVALID_OPERATION) {
                Log.e(TAG , "AudioRecord Error ERROR_INVALID_OPERATION");
            } else if (ret == AudioRecord.ERROR_BAD_VALUE) {
                Log.e(TAG , "AudioRecord Error ERROR_BAD_VALUE");
            } else {
                if (mAudioFrameCapturedListener != null) {
                    mAudioFrameCapturedListener.onAudioFrameCaptured(buffer);
                }
                if (isPush) {
                    mLivePusher.sendCustomPCMData(buffer);
                }
            }
            SystemClock.sleep(10);
        }
    }
}
```



## Details of TXLivePushConfig APIs

#### 1. enableAEC(enable)

API details: void enableAEC(boolean enable)

Enables AEC. Enabling AEC is required for joint broadcasting, and is not recommended for other scenarios. This feature is disabled by default.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | -------------------------------- |
| enable | boolean | "true" indicates AEC is enabled; and "false" indicates AEC is disabled. Default is "false". |


- **Sample code**: 

```
mLivePushConfig.enableAEC(true);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 2. enableNearestIP(enable)

API details: void enableNearestIP(boolean enable)

Enables the nearest route first. Our SDK is not bound with Tencent Cloud. If you want to push to non-Tencent Cloud or overseas IPs, please set enableNearestIP of TXLivePushConfig to false first. However, this is not necessary for Tencent Cloud IPs.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | ------------------------------- |
| enable | boolean | "true" indicates AEC is enabled; and "false" indicates AEC is disabled. Default is "true". |


- **Sample code**: 

```
mLivePushConfig.enableNearestIP(true);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 3. enablePureAudioPush(enable)

API details: void enablePureAudioPush(boolean enable)

Enables pushing audio only. The API only takes effect if it is called before push starts.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | -------------------------------- |
| enable | boolean | "true" indicates AEC is enabled; and "false" indicates AEC is disabled. Default is "false". |


- **Sample code**: 

```
mLivePushConfig.enablePureAudioPush(true);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 4. enableScreenCaptureAutoRotate(enable)

API details: void enableScreenCaptureAutoRotate(boolean enable)

Sets whether to enable adaptive rotation during screencap. This API only applies to screencap.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | ---------------------------------------- |
| enable | boolean | "true" indicates adaptive rotation is enabled and the video is displayed in the maximum allowed size after rotation. "false" indicates adaptive rotation is disabled and the video is zoomed out and centrally displayed. Default is "true". |


- **Sample code**: 

```
mLivePushConfig.enableScreenCaptureAutoRotate(true);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 5. setConnectRetryCount(count)

API details: void setConnectRetryCount(int count)

Sets the number of reconnection attempts at the pusher end. SDK attempts to reconnect to the server after it is disconnected unexpectedly. This function is used to set the number of SDK reconnection attempts. It's often used with setConnectRetryInterval.

- **Parameter description**

| Parameter | Type | Description |
| ----- | :--: | ------------------------------ |
| count | int | Number of SDK reconnection attempts: 0-10. Default is 3. |


- **Sample code**: 

```
mLivePushConfig.setConnectRetryCount(5);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 6. setConnectRetryInterval(interval)

API details: void setConnectRetryInterval(int  interval)

Sets the interval between reconnection attempts at the pusher end. SDK attempts to reconnect to the server after it is disconnected unexpectedly. This function is used to set the interval between two successive reconnection attempts. It's often used with setConnectRetryCount.

- **Parameter description**

| Parameter | Type | Description |
| -------- | :--: | ---------------------------------- |
| interval | int | Reconnection interval of SDK in seconds. Value: 3-30. Default is 3. |


- **Sample code**: 

```
mLivePushConfig.setConnectRetryInterval(10);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 7. setEyeScaleLevel(level)

API details: void setEyeScaleLevel(int level)

Sets eye enlarging effect. This API takes effect only when it is called by the [Commercial Enterprise Edition](https://cloud.tencent.com/document/product/454/7873#Android).

- **Parameter description**

| Parameter | Type | Description |
| ----- | :--: | ------------------------------- |
| level | int | Eye enlarging level ranges from 1 to 9. Default is 0, which means disabling eye enlarging.  |


- **Sample code**: 

```
mLivePushConfig.setEyeScaleLevel(1);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 8. setFaceSlimLevel(level)

API details: void setFaceSlimLevel(int level)

Sets face slimming effect. This API takes effect only when it is called by the [Commercial Enterprise Edition](https://cloud.tencent.com/document/product/454/7873#Android).

- **Parameter description**

| Parameter | Type | Description |
| ----- | :--: | ------------------------------ |
| level | int | Face slimming level ranges from 1 to 9. Default is 0, which means disabling face slimming.  |


- **Sample code**: 

```
mLivePushConfig.setFaceSlimLevel(1);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 9. setFrontCamera(front)

API details: void setFrontCamera(boolean front)

Sets whether to use the front camera. The front camera is used by default.

- **Parameter description**

| Parameter | Type | Description |
| ----- | :-----: | ---------------------------------------- |
| front | boolean | "true" indicates the front camera is used, and "false" indicates the rear camera is used. Default is "false". |


- **Sample code**: 

```
mLivePushConfig.setFrontCamera(true);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 10. setHomeOrientation(homeOrientation)

API details: void setHomeOrientation(int homeOrientation)

Sets rotation for captured videos. This API is mainly used for pushing in landscape mode. It's often used with TXLivePusher.setRenderRotation(rotation).

- **Parameter description**

| Parameter | Type | Description |
| --------------- | :--: | ---------------------------------------- |
| homeOrientation | int | Rotation angle of captured video. For specific angle values, see **Rotation Angle** as defined in TXLiveConstants. |

- **Sample code**: 

```
// Your phone is in portrait mode and its Home button is at the bottom. Rotate 0 degrees.
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN); 
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
//  Your phone is in portrait mode, and local rendering is done with 0 degree offset to the vertical line.
mLivePusher.setRenderRotation(0);


// Your phone is in landscape mode and its Home button is to the right. Rotate 270 degrees.
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
//  Your phone is in landscape mode, and local rendering is done with 90 degree offset to the vertical line.
mLivePusher.setRenderRotation(90);
```



#### 11. setPauseFlag(flag)

API details: void setPauseFlag(int flag)

Sets whether to stop video or audio capture when pushing is held. This API is often used for backend push. It's recommended to use with setPauseImg().

- **Parameter description**

| Parameter | Type | Description |
| ---- | :--: | ---------------------------------------- |
| flag | int | Continue with flag option when pushing is held. For specific values, see **Backend Pushing Options** as defined in TXLiveConstants. |

- **Sample code**: 

```
mLivePushConfig.setPauseFlag(TXLiveConstants.PAUSE_FLAG_PAUSE_VIDEO | TXLiveConstants.PAUSE_FLAG_PAUSE_AUDIO);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 12. setPauseImg(img)

API details: void setPauseImg(Bitmap img)

Sets the image played at the pause of backend push. This API is often used for backend push. It's recommended to use with setPauseFlag().

- **Parameter description**

| Parameter | Type | Description |
| ---- | :----: | ----------------------------- |
| img | Bitmap | The image played at the pause of backend push, which cannot exceed 1920*1920. |

- **Sample code**: 

```
Bitmap bitmap = decodeResource(getResources(),R.drawable.pause_publish);
mLivePushConfig.setPauseImg(bitmap);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 13.setPauseImg(time, fps)

API details: void setPauseImg(int time, int fps)

Sets the duration and frame rate of the image played at the pause of backend push. This API is often used for backend push. It's recommended to use with setPauseFlag().

- **Parameter description**

| Parameter | Type | Description |
| ---- | :--: | ------------------------ |
| time | int | The maximum duration of the image played at the pause of backend push (in seconds). Default is 300. |
| fps | int | The frame rate of the image played at the pause of backend push, which ranges from 3 to 8. Default is 5. |

- **Sample code**: 

```
mLivePushConfig.setPauseImg(300,5);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 14.setVideoEncodeGop(gop)

API details: void setVideoEncodeGop(int gop)

Sets video encoding GOP.

Note: Too much GOP will increase delay, so it's recommended to use TXLivePusher.setVideoQuality to enable the SDK to adjust the value as needed.

- **Parameter description**

| Parameter | Type | Description |
| ---- | :--: | ------------------ |
| gop | int | GOP for video encoding (in seconds). Default is 3. |

- **Sample code**: 

```
mLivePushConfig.setVideoEncodeGop(1);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 15.setVideoResolution(resolution)

API details: void setVideoResolution(int resolution)

Sets video encoding resolution. See **Resolution of Pushed Video** for available values.

Note: It's recommended to use TXLivePusher.setVideoQuality to enable the SDK to adjust the value as needed.

- **Parameter description**

| Parameter | Type | Description |
| ---------- | :--: | ---------------------------------------- |
| resolution | int | Video encoding resolution. Default is VIDEO_RESOLUTION_TYPE_540_960. |

- **Sample code**: 

```
mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_TYPE_540_960);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 16.setWatermark(watermark, x, y,) 

API details: void setWatermark(Bitmap watermark, int x, int y)

Sets a watermark image. The SDK requires png watermark images, because they have transparency information, which helps better solve issues like jagged screens. If you need to adjust the position of the watermark image, it is recommended that you use the API setWatermark(watermark, x, y, width).

- **Parameter description**

| Parameter | Type | Description |
| --------- | :----: | ----------- |
| watermark | Bitmap | Watermark image |
| x         |  int   | X coordinate of watermark position |
| y         |  int   | Y coordinate of watermark position |

- **Sample code**: 

```
//Set a video watermark.
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
//The latter two parameters are the X and Y coordinates of the watermark position.
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



#### 17.setWatermark(watermark, x, y, width) 

API details: void setWatermark(Bitmap watermark, float x, float y, float width)

Sets a watermark image. The SDK requires png watermark images, because they have transparency information, which helps better solve issues like jagged screens.
It's recommended to use this API if you need to adjust the position of the watermark image.

- **Parameter description**

| Parameter | Type | Description |
| --------- | :----: | -------------------- |
| watermark | Bitmap | Watermark image |
| x         |  int   | Normalized X coordinate of watermark position, with value range [0,1] |
| y         |  int   | Normalized Y coordinate of watermark position, with value range [0,1] |
| w         |  int   | Normalized watermark width, with value range [0,1] |

- **Sample code**: 

```
//Set a video watermark.
//The parameters are the Bitmap of the watermark image, the X and Y coordinates of the watermark position, and the watermark width. The available value range for the last three parameters is [0, 1].
//The latter two parameters are the X and Y coordinates of the watermark position.
mLivePushConfig.setWatermark(mBitmap, 0.02f, 0.05f, 0.2f);
mLivePusher.setConfig(mLivePushConfig);    // Reset config.
```



## Details of TXLivePlayer APIs

#### 1.setConfig(TXLivePlayConfig config)

API details: void setConfig(TXLivePlayConfig config)

Sets to get player configuration.

Note: Please set config before calling startPlay as this is not allowed during playback.

- **Parameter description**

| Parameter | Type | Description |
| ------ | ---------------- | -------- |
| config | TXLivePlayConfig | Player configuration |


- **Sample code**: 

```
TXLivePlayConfig mPlayConfig = new TXLivePlayConfig();
mPlayConfig.setConnectRetryCount(3);
......
mLivePlayer.setConfig(mPlayConfig);
......
mLivePlayer.startPlay(...);
```



#### 2. setPlayerView(TXCloudVideoView view) 

API details: void setPlayerView(TXCloudVideoView view) 

Binds the rendering view to TXLivePlayer. The API supports binding the same player to different TXCloudVideoView during playback.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---------------- | ------------ |
| view | TXCloudVideoView | Views rendered by player screen |

- **Sample code**: 

```
// Initialization
TXCloudVideoView playerView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//Associate player object with interface view.
mLivePlayer.setPlayerView(playerView);
```



#### 3. setPlayListener(ITXLivePlayListener listener)

API details: void setPlayListener(ITXLivePlayListener listener)

Sets the callback of TXLivePlayer for receiving playback events and player status.

```
// Initialization  
mLivePlayer.setPlayListener(new ITXLivePlayListener() {
    @Override
    public void onPlayEvent(int i, Bundle bundle) {
        // A player event is received. Please see TXLiveConstants.PLAY_EVT_xxx for specific event definition.
    }

    @Override
    public void onNetStatus(Bundle bundle) {
        // The player's current status is received, which is refreshed every 2 seconds. For specific status, please see TXLiveConstants.NET_STATUS_xxx.
    }
});
```



#### 4.startPlay(url, type)

API details: int startPlay(String url,int type)

Starts playback. If the playback starts successfully, "0" is returned. If the playback fails to start due to empty playUrl, "-1" is returned. If the playback fails to start due to invalid playUrl, "-2" is returned. If the playback fails to start due to invalid playType, "-3" is returned.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------ | ---------------------------------------- |
| url | String | A valid pull URL, which is the video playback URL. The URL starts with "rtmp://". For more information on how to obtain Tencent Cloud pull URL, please see [DOC](https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc"). We recommend using FLV format. |
| type | int    | Playback type. See enumerated values of play type defined in TXLivePlayer. |

- **Sample code**: 

```
int result = mLivePlayer.startPlay(playUrl,TXLivePlayer.PLAY_TYPE_LIVE_FLV); 
```



#### 5.stopPlay(isNeedClearLastImg)

API details: int stopPlay(boolean isNeedClearLastImg)

Stops playback. If the playback stops successfully, "0" is returned. If the playback fails to stop, one of other integers is returned.

- **Parameter description**

| Parameter | Type | Description |
| ------------------ | ---- | ---------------------------------------- |
| isNeedClearLastImg | int  | Indicates whether to clear the last frame. "true" means clearing the last frame. This is recommended when playback stops normally. "false" means retaining the last frame. This is recommended when playback stops exceptionally (for example, the playback is forced to stop due to exceptional network status) and the SDK users want to reconnect to the server. |

- **Sample code**: 

```
mLivePlayer.stopPlay(true);
```



#### 6.pause()

API details: void pause()

Pauses playback in VOD scenarios. Pausing playback is not applicable to LVB scenarios. If this API is called during LVB, the pull stops.

- **Sample code**: 

```
mLivePlayer.pause();
```



#### 7.resume()

API details: void resume()

Resumes playback from the pause position in VOD scenarios. If this API is called during LVB, the stream is pulled again.

- **Sample code**: 

```
mLivePlayer.resume();
```



#### 8.enableHardwareDecode(enable)

API details: void enableHardwareDecode(enable)

Enable or Disable video hardware decoding. Video software decoding is used in the SDK by default.

Note: Hardware decoding is only supported on phones with Android 4.2 or later (the minimum API level is 16). If hardware encoding fails, the SDK will automatically switch to software encoding. This API takes effect only after it is configured before startPlay.


- **Sample code**: 

```
mLivePlayer.enableHardwareDecode(true);
......
mLivePlayer.startPlay(...)
```



#### 9.isPlaying()

API details: boolean isPlaying()

Indicates whether the playback is in progress.

If the playback is in progress, a value of "true" is returned. Otherwise, a value of "false" is returned.

- **Sample code**: 

```
boolean isPlaying = mLivePlayer.isPlaying();
```



#### 10.setRenderMode(mode)

API details: void setRenderMode(int mode)

Sets the rendering (fill) mode of image.

Note: This API supports only the following two modes.

TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN (full screen): The image spread across the entire screen proportionally, with the excess parts trimed off. No black edges are left in this mode, but the image may not be displayed completely because of incorrect aspect ratio or view.

TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION (adaptation): The image is scaled proportionally. Both the width and the height of the scaled image do not extend beyond the display area and the image is centered. In this mode, black edges may appear in the screen.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ---- | ---------------------------------------- |
| mode | int  | TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN or TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION. The default mode is FULL_FILL_SCREEN. |

- **Sample code**: 

```
// Set the filling mode to adaptation.
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION);
// Set the filling mode to full screen.
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN);
```



#### 11.setRenderRotation(rotation)

API details: void setRenderRotation(int rotation)

Set the clockwise rotation of image, that is, set the image display orientation to portrait or landscape.

Available values are TXLiveConstants.RENDER_ROTATION_PORTRAIT (portrait) and TXLiveConstants.RENDER_ROTATION_LANDSCAPE (landscape).

- **Parameter description**

| Parameter | Type | Description |
| -------- | ---- | -------------- |
| rotation | int  | Indicates rendering in the orientation of portrait or landscape. Default is portrait. |

- **Sample code**: 

```
// Set image rendering orientation to landscape.
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_LANDSCAPE);
// Set image rendering orientation to portrait.
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_PORTRAIT);
```



#### 12.startRecord()

API details: int startRecord(int recordType)

Starts recording captured streams. As an extension in LVB playback scenarios, Recording Captured Stream means that during the LVB, the viewer can capture and record a segment of video by clicking the "Record" button and publish the recorded content via the video delivery platform (e.g. Tencent Cloud's VOD system) so that the content can be shared through UGC message on social platforms such as the "Moment" of WeChat.

Note: This API is being used on Android 4.4 (API 18 above), and can only be called after playback.

- **Parameter description**

| Parameter | Type | Description |
| ---------- | ---- | ---------------- |
| recordType | int  | This parameter has been deprecated. Only video-only recording is supported. |

- **Sample code**: 

```
int recordType = TXRecordCommon.RECORD_TYPE_STREAM_SOURCE;
mLivePlayer.startRecord(recordType);
```



#### 13.stopRecord()()

API details: int stopRecord()

Stops recording captured streams. 0: Successful. Other values: Failed. The recording result is notified by means of recording callback.

- **Sample code**: 

```
mLivePlayer.stopRecord();
```



#### 14.setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

API details: void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

Sets video recording callback to receive the video recording progress and result.

- **Parameter description**

| Parameter | Type | Description |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | Video recording callback |

- **Sample code**: 

```
mLivePusher.setVideoRecordListener(new TXRecordCommon.ITXVideoRecordListener(){
    @Override
    public void onRecordEvent(int event, Bundle param) {
    }

    @Override
    public void onRecordProgress(long milliSecond) {
        Log.d(TAG, "record progress:" + milliSecond);
    }

    @Override
    public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
        if (result.retCode == TXRecordCommon.RECORD_RESULT_OK) {
            String videoFile        = result.videoPath;
            String videoCoverPic    = result.coverPath;
        } else {
            Log.d(TAG, "record error:" + result.retCode + ", error msg:" + result.descMsg);
        }
    }
});
```



#### 15.setMute(mute)

API details: void setMute(boolean mute)

Indicates whether to enable Mute. This API takes after only when it is configured before or during playback.

- **Parameter description**

| Parameter | Type | Description |
| ---- | ------- | ---------- |
| mute | boolean |  Indicates whether to enable Mute. Default is no. |

- **Sample code**: 

```
mLivePlayer.setMute(true);
```



#### 16. snapshot(TXLivePlayer.ITXSnapshotListener listener)

API details: void snapshot(TXLivePlayer.ITXSnapshotListener listener)

Takes a screenshot of a video. This API is used to take a screenshot to a video frame in the current LVB stream. If you want to capture the entire current UI, call the system API. The callback for the screenshot capture result is implemented asynchronously in the main thread.

- **Sample code**: 

```
mLivePlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //Acquire screenshot bitmap
        }
    }
});
```



#### 17. setSurface(Surface surface)

API details: void  setSurface(Surface surface)

Sets a rendering surface. It can be used to take over rendering from the SDK.
Note: This API is only suitable for hardware decoding when setPlayView is not set.

- **Sample code**: 

```
TextureView videoView = (TextureView) findViewById(R.id.video_view);
videoView.setSurfaceTextureListener(new TextureView.SurfaceTextureListener() {
    @Override
    public void onSurfaceTextureAvailable(SurfaceTexture surface, int width, int height) {
        mLivePlayer.setSurface(new Surface(surface));
    }

    @Override
    public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {

    }

    @Override
    public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) {
        if (mLivePlayer != null) {
            mLivePlayer.setSurface(null);
        }
        return false;
    }

    @Override
    public void onSurfaceTextureUpdated(SurfaceTexture surface) {

    }
});
```



#### 18. addVideoRawData(byte[] yuvBuffer)

API details: void  addVideoRawData(byte[] yuvBuffer)

Sets a receiving buffer for the playback of YUV data. It's used with setVideoRawDataListener to take over rendering from the SDK.
Note: This API is only suitable for software decoding when setPlayView is not set. The size of the buffer is calculated using the actual resolution of the video.



#### 19. setVideoRawDataListener(ITXVideoRawDataListener listener)

API details: void setVideoRawDataListener(ITXVideoRawDataListener listener)

Sets a callback for video YUV data. It's used with addVideoRawData to take over rendering from the SDK.
Note: This API is only suitable for software decoding when setPlayView is not set.

 **Sample code**: 

```
public void onPlayEvent(int event, Bundle param) {
    ......
    if (event == TXLiveConstants.PLAY_EVT_CHANGE_RESOLUTION) {
        videoWidth = param.getInt(TXLiveConstants.EVT_PARAM1,0);
        videoHeight = param.getInt(TXLiveConstants.EVT_PARAM2,0);
        mLivePlayer.addVideoRawData(new byte[videoWidth*videoHeight*3/2]);
    } 
    ......
}
    
    
mLivePlayer.setVideoRawDataListener(new TXLivePlayer.ITXVideoRawDataListener() {
    @Override
    public void onVideoRawDataAvailable(byte[] buf, int width, int height, int timestamp) {
        mLivePlayer.addVideoRawData(new byte[videoWidth*videoHeight*3/2]);
    }
});

```



#### 20. setAudioRawDataListener(ITXAudioRawDataListener listener)

API details: void setAudioRawDataListener(ITXAudioRawDataListener listener)

Sets a callback for audio PCM data.

 **Sample code**: 

```
mLivePlayer.setAudioRawDataListener(new TXLivePlayer.ITXAudioRawDataListener() {
    @Override
    public void onPcmDataAvailable(byte[] buf, long timestamp) {
        // Audio PCM data
    }

    @Override
    public void onAudioInfoChanged(int sampleRate, int channels, int bits) {
        //Audio sampling rate, number of channels
    }
});
```



## Details of TXLivePlayConfig APIs

#### 1. enableAEC(enable)

API details: void enableAEC(boolean enable)

Enables AEC. Enabling AEC is required for joint broadcasting, and is not recommended for other scenarios.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | -------------------------------- |
| enable | boolean | "true" indicates AEC is enabled; and "false" indicates AEC is disabled. Default is "false". |


- **Sample code**: 

```
mPlayConfig.enableAEC(true);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 2. setConnectRetryCount(count)

API details: void setConnectRetryCount(int count)

Sets the number of reconnection attempts at the player. SDK attempts to reconnect to the server after it is disconnected unexpectedly. This function is used to set the number of SDK reconnection attempts. It's often used with setConnectRetryInterval.

- **Parameter description**

| Parameter | Type | Description |
| ----- | :--: | ------------------------------ |
| count | int | Number of SDK reconnection attempts: 0-10. Default is 3. |


- **Sample code**: 

```
mPlayConfig.setConnectRetryCount(5);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 3. setConnectRetryInterval(interval)

API details: void setConnectRetryInterval(int  interval)

Sets the interval between reconnection attempts at the the player. SDK attempts to reconnect to the server after it is disconnected unexpectedly. This function is used to set the interval between two successive reconnection attempts. It's often used with setConnectRetryCount.

- **Parameter description**

| Parameter | Type | Description |
| -------- | :--: | ---------------------------------- |
| interval | int | Reconnection interval of SDK in seconds. Value: 3-30. Default is 3. |


- **Sample code**: 

```
mPlayConfig.setConnectRetryInterval(10);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 4. setEnableMessage(enable)

API details: void setEnableMessage(boolean enable)

Enables a message channel.

- **Parameter description**

| Parameter | Type | Description |
| ------ | :-----: | ---------------------------------------- |
| enable | boolean | A value of "true" means a message channel is enabled, and "false" means a message channel is disabled. Default is "false". |


- **Sample code**: 

```
mPlayConfig.setEnableMessage(true);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 5. setAutoAdjustCacheTime(bAuto) 

API details: void setAutoAdjustCacheTime(boolean bAuto)

Sets whether to automatically adjust the player caching time according to network conditions. It's often used with setMinAutoAdjustCacheTime(time) and setMaxAutoAdjustCacheTime(time).

Once automatic adjustment is enabled, the SDK adjusts the caching time automatically by using MaxAutoAdjustCacheTime and MinAutoAdjustCacheTime based on network conditions.

Once automatic adjustment is disabled, the SDK uses a fixed caching time which can be adjusted by modifying cacheTime.

- **Parameter description**

| Parameter | Type | Description |
| ----- | :-----: | -------------------------------------- |
| bAuto | boolean | "true" means automatic adjustment is enabled, and "false" means automatic adjustment is disabled. Default is "true". |


- **Sample code**: 

```
//Auto mode
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(5);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 6. setCacheTime(time)

API details: void setCacheTime(float time)

Sets player caching time. setAutoAdjustCacheTime(false) is used to set fixed player caching time.

- **Parameter description**

| Parameter | Type | Description |
| ---- | :---: | -------------------------- |
| time | float | Player caching time in seconds. It should be greater than 0 and is 5 by default. |


- **Sample code**: 

```
//Smooth mode
mPlayConfig.setAutoAdjustCacheTime(false);
mPlayConfig.setCacheTime(5);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 7. setMaxAutoAdjustCacheTime(time)

API details: void setMinAutoAdjustCacheTime(float time)

Sets the maximum player caching time for automatic adjustment. It's used with setAutoAdjustCacheTime(bAuto) and setMinAutoAdjustCacheTime(time).

- **Parameter description**

| Parameter | Type | Description |
| ---- | :---: | ---------------------------- |
| time | float | The maximum player caching time in seconds. It should be greater than 0 and is 5 by default. |


- **Sample code**: 

```
//Speedy mode
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



#### 8. setMinAutoAdjustCacheTime(time) 

API details: void setMinAutoAdjustCacheTime(float time)

Sets the minimum player caching time for automatic adjustment. It's used with setAutoAdjustCacheTime(bAuto) and setMaxAutoAdjustCacheTime(time).

- **Parameter description**

| Parameter | Type | Description |
| ---- | :---: | ---------------------------- |
| time | float | The minimum player caching time in seconds. It should be greater than 0 and is 1 by default. |


- **Sample code**: 

```
//Speedy mode
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);
mLivePlayer.setConfig(mPlayConfig);    // Reset config.
```



## Enumeration Type Definition

#### 1.Resolution of pushed video

The following parameters are generally not used if you use the camera to push. When you use screencap push feature and need to switch between landscape and portrait modes, these parameters are required to change resolutions of pushed images.

```
VIDEO_RESOLUTION_TYPE_360_640         =  0;    // 360 * 640
VIDEO_RESOLUTION_TYPE_540_960         =  1;    // 540 * 640
VIDEO_RESOLUTION_TYPE_720_1280        =  2;    // 720 * 1280
VIDEO_RESOLUTION_TYPE_640_360         =  3;    // 640 * 360
VIDEO_RESOLUTION_TYPE_960_540         =  4;    // 960 * 440
VIDEO_RESOLUTION_TYPE_1280_720        =  5;    // 1280 * 720
VIDEO_RESOLUTION_TYPE_320_480         =  6;    // 320 * 480
VIDEO_RESOLUTION_TYPE_180_320         =  7;    // 180 * 320
VIDEO_RESOLUTION_TYPE_270_480         =  8;    // 270 * 480
VIDEO_RESOLUTION_TYPE_320_180         =  9;    // 320 * 180
VIDEO_RESOLUTION_TYPE_480_270         =  10;   // 480 * 270
```

#### 2. Software and hardware encoding options

Choose an encoding option to push streams. It's recommended to use ENCODE_VIDEO_AUTO if you don't know when to enable hardware acceleration. Software encoding is enabled by default. However, the SDK will switch to hardware encoding automatically when the CPU utilization of your phone > 80% or frame rate <= 10.

```
ENCODE_VIDEO_SOFTWARE               = 0; // Software encoding
ENCODE_VIDEO_HARDWARE               = 1; // Hardware encoding
ENCODE_VIDEO_AUTO                   = 2; // Automatically decided
```


#### 3. Image Tiling Mode

Sets the filling mode of image rendering at the player to full screen or adaptation.

```
RENDER_MODE_FULL_FILL_SCREEN     =  0; //Full screen: The image spread across the entire screen proportionally, with the excess parts trimmed off. No black edges are left in this mode.
RENDER_MODE_ADJUST_RESOLUTION    =  1; //Adaptation: The image is scaled proportionally. Both the width and the height of the scaled image do not extend beyond the display area and the image is centered. In this mode, black edges may appear in the screen.

```

#### 4. Video Image Rendering Orientation

Sets the rotation angle of image rendering at the player to portrait or landscape.

```
RENDER_ROTATION_PORTRAIT         =  0;      // Portrait
RENDER_ROTATION_LANDSCAPE        =  270;    // Landscape (90° clockwise rotated)
```

#### 5. Video rotation angle

For pushing in landscape mode, the pusher sets a video rotation angle for the viewer side.

```
VIDEO_ANGLE_HOME_RIGHT           =  0;      // Home button on the right
VIDEO_ANGLE_HOME_DOWN            =  1;      // Home button at the bottom
VIDEO_ANGLE_HOME_LEFT            =  2;      // Home button on the left
VIDEO_ANGLE_HOME_UP              =  3;      // Home button at the top
```

#### 6. Backend push options

Options available for setPauseFlag.

```
PAUSE_FLAG_PAUSE_VIDEO = 1;     // When pausePusher is used, set this flag bit to pause the image previously captured by camera or screencap and use pauseImg as the pushing image. If this flag bit is not set, the images are still captured (by camera or screencap) and pushed.
PAUSE_FLAG_PAUSE_AUDIO = 2;     // When pausePusher is used, set this flag bit to pause audio capture and push mute data. If this flag bit is not set, the audio is still captured by the microphone and pushed.

```



#### 7.Playback type

Playback types supported by your player. It is recommended that you play back videos in your App in the format of FLV under LVB scenarios.

```
PLAY_TYPE_LIVE_RTMP = 0       // The input URL is an RTMP-based LVB URL. 
PLAY_TYPE_LIVE_FLV =  1       // The input URL is an FLV-based LVB URL. 
PLAY_TYPE_LIVE_RTMP_ACC =  5  // Low-latency URL (only for joint broadcasting scenarios). 
PLAY_TYPE_VOD_HLS =  3        // The input URL is an HLS(m3u8)-based playback URL. 
```

## ITXLivePushListener Event Callback

#### APIs for push events

| API Definition | Description |
| ------------------------------------ | ------------------- |
| onPushEvent(int event, Bundle param) |  Push event notification API |
| onNetStatus(Bundle param)            | Push status notification API |

#### Push events

```
PUSH_EVT_CONNECT_SUCC = 1001,                      // Connected to the push server
PUSH_EVT_PUSH_BEGIN = 1002,                        // Handshake with the server completed. Push starts.
PUSH_EVT_OPEN_CAMERA_SUCC = 1003,                  // Camera enabled successfully
PUSH_EVT_SCREEN_CAPTURE_SUCC = 1004;               // Screencap enabled successfully
PUSH_EVT_CHANGE_RESOLUTION = 1005,                 // Resolution is adjusted dynamically during push
PUSH_EVT_CHANGE_BITRATE = 1006,                    // Bitrate is adjusted dynamically during push
PUSH_EVT_FIRST_FRAME_AVAILABLE = 1007,             // The first frame is captured
PUSH_EVT_START_VIDEO_ENCODER = 1008,               // Encoder started

PUSH_ERR_OPEN_CAMERA_FAIL = -1301,                 // Failed to enable camera
PUSH_ERR_OPEN_MIC_FAIL = -1302,                    // Failed to enable microphone
PUSH_ERR_VIDEO_ENCODE_FAIL = -1303,                // Video encoding failed
PUSH_ERR_AUDIO_ENCODE_FAIL = -1304,                // Audio encoding failed
PUSH_ERR_UNSUPPORTED_RESOLUTION = -1305,           // Unsupported video resolution
PUSH_ERR_UNSUPPORTED_SAMPLERATE = -1306,           // Unsupported audio sampling rate
PUSH_ERR_NET_DISCONNECT = -1307,                   // Network disconnected. Too many failed reconnection attempts. Restart the push for more retries.
PUSH_ERR_SCREEN_CAPTURE_START_FAILED  = -1308;     // Failed to start screencap, which is possibly rejected by the user.
PUSH_ERR_SCREEN_CAPTURE_UNSURPORT = -1309;         // Screencap failed due to unsupported Android OS version; 5.0 or above is required.
PUSH_ERR_SCREEN_CAPTURE_DISTURBED = -1310;         // Screencap was interrupted by other applications. The application that opened MediaProjection first was stopped by the application that opens MediaProjection later. The SDK throws this error.
PUSH_ERR_MIC_RECORD_FAIL = -1311;                  // Android Mic was activated successfully, but could not record audio for 6 consecutive times. The thread for audio recording will exit.
PUSH_ERR_SCREEN_CAPTURE_SWITCH_DISPLAY_FAILED  = -1312;   // Failed to dynamically switch between landscape and portrait modes during screencap.

PUSH_WARNING_NET_BUSY = 1101,                      // Bad network condition: data upload is blocked because upstream bandwidth is too small
PUSH_WARNING_RECONNECT = 1102,                     // Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts)
PUSH_WARNING_HW_ACCELERATION_FAIL = 1103,          // Failed to start hard-encoding. Soft-encoding is used instead.
PUSH_WARNING_VIDEO_ENCODE_FAIL = 1104,             // Video encoding failed. Non-fatal error. Encoder will be restarted internally.
PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL = 1105,  // Video encoding bitrate exception
PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW = 1106, // Video encoding bitrate exception
PUSH_WARNING_DNS_FAIL = 3001,                      // RTMP - DNS resolution failed
PUSH_WARNING_SEVER_CONN_FAIL = 3002,               // RTMP server connection failed
PUSH_WARNING_SHAKE_FAIL = 3003,                    // RTMP server handshake failed
PUSH_WARNING_SERVER_DISCONNECT = 3004,             // RTMP server disconnected automatically. Check the validity of push URL or the validity period of the hotlink protection.
PUSH_WARNING_SERVER_NO_DATA = 3005,                // No data was sent within 30 seconds. Server disconnected automatically.
```

#### Status information about push and pull

Status information about push and pull is called back to monitor SDK's indicators.

| Push Status | Type | Description |
| :--------------------------- | :----: | :--------------------------------------- |
| NET_STATUS_CPU_USAGE         | String | CPU utilization of current process and overall CPU utilization of the machine |
| **NET_STATUS_VIDEO_WIDTH**  |  int   | **Width of the current video (in pixels)** |
| **NET_STATUS_VIDEO_HEIGHT** |  int   | **Height of the current video (in pixels)** |
| NET_STATUS_NET_SPEED         |  int   | Current transmission speed (in Kbps) |
| NET_STATUS_VIDEO_BITRATE     |  int   | The output bitrate of the current video encoder, i.e., the number of video data bits produced by the encoder per second (in Kbps) |
| NET_STATUS_AUDIO_BITRATE     |  int   | The output bitrate of the current audio encoder, i.e., the number of audio data bits produced by the encoder per second (in Kbps) |
| NET_STATUS_VIDEO_FPS         |  int   | Current video frame rate, that is, the number of frames produced by video encoder per second |
| NET_STATUS_CACHE_SIZE        |  int   | Accumulated audio/video data size. A value ≥ 10 indicates the current upstream bandwidth is not enough to consume the audio/video data produced |
| NET_STATUS_CODEC_DROP_CNT    |  int   | The number of global packet drops. To avoid a vicious accumulation of delays, the SDK actively drops packets when the accumulated data exceeds the threshold. A higher number of packet drops means a more severe network problem. |
| NET_STATUS_SERVER_IP         | String | IP of the connected push server |


## ITXLivePlayListener Event Callback

#### APIs for playback events

| API Definition | Description |
| ------------------------------------ | -------------------- |
| onPlayEvent(int event, Bundle param) | Playback event notification of TXLivePlayer |
| onNetStatus(Bundle param)            | Playback status notification of TXLivePlayer |

#### Playback events

```
PLAY_EVT_CONNECT_SUCC = 2001,                   // Connected to the server
PLAY_EVT_RTMP_STREAM_BEGIN = 2002,              // Connected to the server. Pull started.
PLAY_EVT_RCV_FIRST_I_FRAME = 2003,              // The first video data packet (IDR) is rendered
PLAY_EVT_PLAY_BEGIN = 2004,                     // Video playback started
PLAY_EVT_PLAY_PROGRESS = 2005,                  // Video playback progress
PLAY_EVT_PLAY_END = 2006,                       // Video playback ended
PLAY_EVT_PLAY_LOADING = 2007,                   // Video playback loading
PLAY_EVT_START_VIDEO_DECODER = 2008,            // Decoder started
PLAY_EVT_CHANGE_RESOLUTION = 2009,              // Video resolution changed

PLAY_ERR_NET_DISCONNECT = -2301,                // Network disconnected. Too many failed reconnection attempts. Restart the playback for more retries.
PLAY_ERR_GET_RTMP_ACC_URL_FAIL = -2302,         // Failed to get the accelerated pull address

PLAY_WARNING_VIDEO_DECODE_FAIL = 2101,          // Failed to decode the current video frame
PLAY_WARNING_AUDIO_DECODE_FAIL = 2102,          // Failed to decode the current audio frame
PLAY_WARNING_RECONNECT = 2103,                  // Network disconnected. Auto reconnection has been initiated (no more attempts will be made after three failed attempts)
PLAY_WARNING_RECV_DATA_LAG = 2104,              // Unstable inbound packet: This may be caused by insufficient downstream bandwidth, or inconsistent outbound stream from the VJ end.
PLAY_WARNING_VIDEO_PLAY_LAG = 2105,             // Stutter occurred during the video playback (user experience)
PLAY_WARNING_HW_ACCELERATION_FAIL = 2106,       // Failed to start hard decoding. Soft decoding is used instead.
PLAY_WARNING_VIDEO_DISCONTINUITY = 2107,        // Discontinuous sequence of video frames. Some frames may be dropped.
PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL = 2108,   // Hard decoding of the first I-frame of current stream failed. Switched to soft decoding automatically.
PLAY_WARNING_DNS_FAIL = 3001,                   // RTMP - DNS resolution failed
PLAY_WARNING_SEVER_CONN_FAIL=: 3002,            // RTMP server connection failed
PLAY_WARNING_SHAKE_FAIL = 3003,                 // RTMP server handshake failed
PLAY_WARNING_SERVER_DISCONNECT = 3004,          // RTMP server disconnected automatically
```

