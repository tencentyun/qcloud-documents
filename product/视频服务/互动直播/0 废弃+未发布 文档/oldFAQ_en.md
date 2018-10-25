## How to set up an image (SetMirror)

### Android

![mirrorAndroid](//mccdn.qcloud.com/static/img/9148c0611d28be304e4bd96dd20341ba/image.png)

### iOS

Please see the content in the bold red box.

![mirrorIOS](//mccdn.qcloud.com/static/img/484da1414d62848bf0d77845586b7f02/image.png)

## [iOS] How to deal with the blurred screen at viewer or VJ ends?

![Blurred Screen](//mccdn.qcloud.com/static/img/1545ecd928d6cd59c2944b5699a2c02b/image.png)

## How to deal with the Error 1002 returned while enabling microphone in the callback for joining a room?

`1002`: A conflict occurred between the two operations

### Android

Solution: Set enableMic to true before joining the room. For Android, user can enable the microphone before joining the room, so no conflict will occur.

### iOS

For iOS, the microphone is being disabled by default when user joins a room, so a conflict may occur between enabling the microphone and joining a room. You can solve this problem by applying a delay of 1s before enabling the microphone.

## How to deal with the black screen at viewer end when VJ returns to the foreground after switching to the background for a while (15s)?

Solution: VJ needs to disable the camera before switching to the background, and enable the camera again when switching back to the foreground.

## [iOS] How to deal with the occasional crash while switching between foreground and background and closing OpenGL?

```ObjectiveC
-(void)didEnterBackground:(NSNotification*)notification{
    if (_imageView)
    {
        [_imageView stopDisplay];
        [NSObject cancelPreviousPerformRequestsWithTarget:_imageView selector:@selector(startDisplay) object:nil];//vigoss
    }
}

-(void)WillEnterForeground:(NSNotification*)notification{
    if (_imageView)
        [_imageView performSelector:@selector(startDisplay) withObject:nil afterDelay:0.5];//vigoss
}
```

When you exit ILVB:

```ObjectiveC
        [_imageView stopDisplay];
        [NSObject cancelPreviousPerformRequestsWithTarget:_imageView selector:@selector(startDisplay) object:nil];
```
## Solution to the problem of being unable to set volume to 0
### Android

By simply setting enableSpeaker to false, you can go into a mute mode.

### iOS

At VJ end, the volume of VJ cannot be set to 0; at viewer end, you can go into a mute mode by setting the `Audio Scenario` to `Watch` in audio parameter settings of console Spear engine, or by referring to the usage of **Mute** button in sample 2.

## The option to automatically create a room while joining a room that does not exist.

![Automatically Create a Room](//mccdn.qcloud.com/static/img/f8f70026eae76d3b6415a8ea3c051932/image.jpg)

## Rendering VJ's local view with beauty filter in SDK1.7 version or above

![Local Rendering with Beauty Filter](//mccdn.qcloud.com/static/img/c0ff897cac4a9a42ef452626e7404a61/image.png)

## What should be done when switching from background to foreground on mobile App?

### Android

For Android, switching between foreground and background only requires disabling and enabling camera.

```Java
QavsdkControl qavsdk = ((QavsdkApplication) mContext).getQavsdkControl();
AVVideoCtrl avVideoCtrl = qavsdk.getAVContext().getVideoCtrl();
result = avVideoCtrl.enableCamera(FRONT_CAMERA, isEnable, mEnableCameraCompleteCallback);
```

### iOS
For iOS, switching to background requires the opengl rendering at higher layer to be disabled. To switch back to foreground, VJ is recommended to disable the camera, if it is enabled. The sample code for modification is as follows:

![iOS Sample Code](//mccdn.qcloud.com/static/img/b2401839764de55d9a3f8f5a67a4e49b/image.png)

## How to use the "roles" configured in console SPEAR engine in the code?

For the ILVB featuring Beauty VJs, two roles are configured in SPEAR engine of Tencent Cloud console: VJ and Viewer. The main difference between the two roles is that a viewer just watches/listens to the broadcasting and does not need audio recording and other permissions. Therefore, for a lot of business, viewers are recommended not to trigger the permission pop-up "Accessing XX device is allowed or not?" from operating system.

How to use the "roles" configured on the page in the code? Please see the following code snippet
![Figure 1](//mccdn.qcloud.com/static/img/e4e8a61adf1d250630f101bbd9160285/image.png)
![Figure 2](//mccdn.qcloud.com/static/img/e9e0e5041a81d75a2d3a9c54257a4d1d/image.png)
## Default directory for OpenSDK logs

### Android

By default, the logs are placed under tencent/imsdklogs/com/tencent/avsdk in built-in SD.         

### iOS

The logs are placed under subdirectory /Library/Caches in the installation directory of DEMO App, as shown below:

![iOSLog Directory](//mccdn.qcloud.com/static/img/0837b7ff0ec0d611b0f2c7ddaef0c0a2/image.png)

### Windows

Current directory If DEMO executable is run directly, the current directory is the one where the executable is located; if DEMO executable is compiled and run from VS2010, the current directory is the one where VS2010 DEMO project is located, that is, OpenSDK\Demo\PC\src\.

### Note

For open SDK, API for setting log storage directory is provided by IMSDK. Audio/video SDK is only responsible for obtaining the directory set by the API to store the logs, which are then reported by IMSDK.

## Solution to reverse of camera in versions earlier than Android 1.7

### Modification to AvActivity class

Add the code in the yellow box below to the corresponding location in AvActivity class.

![AvActivity](//mccdn.qcloud.com/img56cde3ee57ed1.png)

```c++
Log.d("shixu", "isfront: " + isFront);
				
if (isFront) {
	mQavsdkControl.setMirror(true, mSelfIdentifier);
} else {
	mQavsdkControl.setMirror(false, mSelfIdentifier);
}
```

### Modification to AVUIControl class

Add the code in the yellow box below to the corresponding location in AVUIControl class.

![AVUIControl](//mccdn.qcloud.com/img56cde50e6c1dc.png)

```c++
if (isFrontCamera()) {
	view.setMirror(true);
} else {
 view.setMirror(false);
}
```

```c++
private boolean isFrontCamera() {
    QavsdkControl mQavsdkControl = ((QavsdkApplication)(mContext.getApplicationContext())).getQavsdkControl();
		
    Log.d("shixu", "is front camera: " + mQavsdkControl.getIsFrontCamera());
    return mQavsdkControl.getIsFrontCamera();
}
	
public void setMirror(boolean isMirror, String identifier) {
    GLVideoView view = null;
    int index = getViewIndexById(identifier, AVConstants.VIDEO_SRC_CAMERA);		
    if (index >= 0) {
        view = mGlVideoView[index];
        view.setMirror(isMirror);
    }
}
```

### Modification to QavsdkControl class

Add the code in the yellow box below to the corresponding location in QavsdkControl class.

![](//mccdn.qcloud.com/img56cde60fd1e7c.png)

```c++
public void setMirror(boolean isMirror, String identifier) {
    if (null != mAVUIControl) {
        mAVUIControl.setMirror(isMirror, identifier);
    }
}
```

## Can the video streams be sent directly to AVSDK for encoding and transmission?

Currently, avsdk only supports inputting video data in I420 format. Direct input of video data in other formats or based on other protocols is not supported.

Android API:
```
	/**
	 * Input the video images obtained from the external video capturing device to the SDK. <br/>
	 * @param data Image data.
	 * @param data Image data length.
	 * @param width Image width.
	 * @param height Image height.
	 * @param cameraAngle Image rendering angle. The angle can be 0, 90, 180, or 270.
	 * @param colorFormat Image color format. Currently, only COLOR_FORMAT_I420 is supported.
	 * @param srcType Video source type. Currently, only VIDEO_SRC_TYPE_CAMERA is supported.
	 * @return Returned value of AV_OK indicates a success; other values indicate a failure.
	 *The resolution aspect ratio can only be 4:3, and the maximum width is 640
	 */
	public native int fillExternalCaptureFrame(byte[] data, int dataLen, int width, int height, int cameraAngle, int colorFormat, int srcType);

The API for Android is at com.tencent.av.sdk.AVVideoCtr
```

## How to deal with the problem that the number of methods for Android exceeds the limit of 65535?
Please refer to the related articles by clicking [here](http://tech.meituan.com/mt-android-auto-split-dex.html)

