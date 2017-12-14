#### [iOS] Solution to the occasional crash while switching between foreground and background and closing OpenGL

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

#### How to switch from background to foreground on mobile App

Android

For Android, switching between foreground and background is achieved by disabling and enabling camera.

```Java
QavsdkControl qavsdk = ((QavsdkApplication) mContext).getQavsdkControl();
AVVideoCtrl avVideoCtrl = qavsdk.getAVContext().getVideoCtrl();
result = avVideoCtrl.enableCamera(FRONT_CAMERA, isEnable, mEnableCameraCompleteCallback);
```

iOS

For iOS, switching to background requires disabling the opengl rendering at higher layer. To switch to foreground, VJ is recommended to disable the camera, if it is enabled. The modified sample code is as follows:

![iOS Sample Code](//mccdn.qcloud.com/static/img/b2401839764de55d9a3f8f5a67a4e49b/image.png)

#### How to use the "roles" configured in console SPEAR engine in the code?

For the ILVB featuring Beauty VJs, two roles are configured in SPEAR engine of Tencent Cloud console: VJ and Viewer. The main difference between the two roles lies in the fact that the viewer just watches/listens to the broadcasting and does not need audio recording and other permissions. Therefore, in many businesses, viewers are recommended not to trigger the permission pop-up "Do you want to allow the access to XX device?" from operating system.

Then, how to use the "roles" configured on the page in the code? Please see the following code snippet
![Figure 1](//mccdn.qcloud.com/static/img/e4e8a61adf1d250630f101bbd9160285/image.png)
![Figure 2](//mccdn.qcloud.com/static/img/e9e0e5041a81d75a2d3a9c54257a4d1d/image.png)

#### Can the video streams be sent directly to AVSDK for encoding and transmission?

Currently, avsdk only supports inputting video data in I420 format. Direct input of video data in other formats or based on other protocols is not supported.

The Android API:
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
	 * @return Returned value of AV_OK indicates a success; any other value indicates a failure.
	 *The resolution aspect ratio can only be 4:3, and the maximum width is 640
	 */
	public native int fillExternalCaptureFrame(byte[] data, int dataLen, int width, int height, int cameraAngle, int colorFormat, int srcType);

The API for Android is at com.tencent.av.sdk.AVVideoCtr
```

#### How to deal with the problem that the number of methods for Android exceeds the limit of 65535?
Please refer to the related articles by clicking [here](http://tech.meituan.com/mt-android-auto-split-dex.html)

#### Java signature generation error getlicense code:-1 
sig expired. Please re-generate it. If it expires immediately after its generation, please check if you've entered a short validity period or 0.

#### How to listen at viewer end for the fact that no upstream video data is transmitted from VJ ?
In a VJ-viewer scenario, the logic needs to be implemented at business side.  
We provide a solution that:  
1. Adds a timer onVideoPreview to the rendered callback   
2. Monitors onEndpointsUpdateInfo

#### Can the logs in logcat be disabled?
setLogPrintEnable (false)

#### FreeShow is unavailable for Android 6.0 users after being integrated.
For Android 6.0, you need to apply for dynamic permission. Please refer to the latest sample of FreeShow.

#### Error message "android-support-v4.jar is missing" appears.
You can add the android-support-v4.jar provided by Google (com.android.support:support-v4:23.3.0). 
