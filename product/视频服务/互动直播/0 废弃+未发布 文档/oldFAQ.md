## 如何设置镜像（SetMirror）

### 安卓

![mirrorAndroid](//mccdn.qcloud.com/static/img/9148c0611d28be304e4bd96dd20341ba/image.png)

### iOS

请参考粗红框里的内容

![mirrorIOS](//mccdn.qcloud.com/static/img/484da1414d62848bf0d77845586b7f02/image.png)

## 【iOS】观众或者主播端出现花屏的解决方案

![花屏](//mccdn.qcloud.com/static/img/1545ecd928d6cd59c2944b5699a2c02b/image.png)

## 进房间回调里面打开麦克风报1002错误的解决办法

`1002`：互斥操作。

### 安卓

解决办法：在进房间之前调用enableMic为true。因为安卓可以在进房之前打开麦克风，所以如此操作之后不会引发互斥

### iOS

由于iOS进房间时默认正在关闭麦克风，所以打开麦克风操作与进房间（正在关闭麦克风）的动作可能造成互斥。目前的解决办法是：在打开麦克风之前加下1S的延时。

## 主播切后台一段时间（15s）后回前台，观众黑屏的问题

解决办法是：主播退到后台前先把摄像头关闭了，回到前台再次打开。

## 【iOS】前后台切换/关闭OpenGL偶现crash的解决方法

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

退出直播的时候：

```ObjectiveC
        [_imageView stopDisplay];
        [NSObject cancelPreviousPerformRequestsWithTarget:_imageView selector:@selector(startDisplay) object:nil];
```
## 关于音量不能调低到0的问题
### 安卓

如果想要静音的话，直接将enableSpeaker设置为false即可

### iOS

如果是主播模式，主播音量不能调节到0；观众端可以在控制台Spear引擎的音频参数设置里的`音频场景`设置为`观看`，或参考sample2里面静音按钮的方法实现静音

## 进入房间时，如果房间不存在则自动创建房间选项

![自动创建房间](//mccdn.qcloud.com/static/img/f8f70026eae76d3b6415a8ea3c051932/image.jpg)

## SDK1.7(+) 版本美颜渲染主播本地画面

![美颜本地渲染](//mccdn.qcloud.com/static/img/c0ff897cac4a9a42ef452626e7404a61/image.png)

## 终端App退后台/回前台的处理

### Android

安卓退后台/回前台仅需要关闭和开启摄像头即可

```Java
QavsdkControl qavsdk = ((QavsdkApplication) mContext).getQavsdkControl();
AVVideoCtrl avVideoCtrl = qavsdk.getAVContext().getVideoCtrl();
result = avVideoCtrl.enableCamera(FRONT_CAMERA, isEnable, mEnableCameraCompleteCallback);
```

### iOS
iOS退后台时需要关掉上层的opengl渲染。回前台时，如果主播开启了摄像头的话，建议关闭摄像头。相关修改的示例代码如下：

![iOS示例代码](//mccdn.qcloud.com/static/img/b2401839764de55d9a3f8f5a67a4e49b/image.png)

## 如何在代码中使用控制台SPEAR引擎配置中的“角色”

对于美女主播类业务，通常会在腾讯云控制台的SPEAR引擎中配置两种“角色”：主播角色和观众角色。二者的主要区别是观众角色通常只是收看/收听，不需要录音等音频权限，所以很多业务也希望观众端最好不要触发操作系统弹出“是否允许访问XX设备”的权限提示。

那么如何在代码中使用网页上配置的“角色”呢？请参考下面的代码片段
![图1](//mccdn.qcloud.com/static/img/e4e8a61adf1d250630f101bbd9160285/image.png)
![图2](//mccdn.qcloud.com/static/img/e9e0e5041a81d75a2d3a9c54257a4d1d/image.png)
## OpenSDK默认日志存放目录

### Android

默认放在内置SD下的tencent/imsdklogs/com/tencent/avsdk子目录。         

### iOS

DEMO APP安装目录下的/Library/Caches子目录。如下图：

![iOSLog目录](//mccdn.qcloud.com/static/img/0837b7ff0ec0d611b0f2c7ddaef0c0a2/image.png)

### Windows

当前目录。对于直接运行DEMO可执行文件，当前目录就是DEMO可执行文件所在目录；对于从VS2010编译并运行DEMO可执行文件时，当前目录是VS2010 DEMO工程所在目录，也就是OpenSDK\Demo\PC\src\目录下。

### 注意事项

开放SDK统一由IMSDK提供对外设置日志存放目录的接口，音视频SDK只是获取它所设置的目录来存放日志，并由IMSDK来负责上报日志。

## 安卓1.7之前版本摄像头反转问题解决方法

### AvActivity类的修改

将下图中黄色框里的代码添加到AvActivity类的相应位置

![AvActivity](//mccdn.qcloud.com/img56cde3ee57ed1.png)

```c++
Log.d("shixu", "isfront: " + isFront);
				
if (isFront) {
	mQavsdkControl.setMirror(true, mSelfIdentifier);
} else {
	mQavsdkControl.setMirror(false, mSelfIdentifier);
}
```

### AVUIControl类的修改

将下图中黄色框里的代码添加到AVUIControl类的相应位置

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

### QavsdkControl类的修改

将下图中黄色框里的代码添加到QavsdkControl类的相应位置

![](//mccdn.qcloud.com/img56cde60fd1e7c.png)

```c++
public void setMirror(boolean isMirror, String identifier) {
    if (null != mAVUIControl) {
        mAVUIControl.setMirror(isMirror, identifier);
    }
}
```

## 是否可以把视频流直接送给AVSDK进行编码传输？

avsdk目前只支持外部输入I420格式视频数据，不支持其他格式或其他协议视频数据的直接输入

安卓接口为：
```
	/**
	 * 输入从外部视频捕获设备获取的视频图像到SDK。<br/>
	 * @param data 图像数据。
	 * @param dataLen 图像数据长度。
	 * @param width 图像宽度。
	 * @param height 图像高度。
	 * @param cameraAngle 图像渲染角度。角度可以是0，90，180，270。
	 * @param colorFormat 图像颜色格式。当前仅支持COLOR_FORMAT_I420。
	 * @param srcType 视频源类型。当前仅支持VIDEO_SRC_TYPE_CAMERA。
	 * @return 返回值为AV_OK时表示成功，否则表示失败。
	 * 分辨率宽高比例限定只能为4：3，且最大宽度为640
	 */
	public native int fillExternalCaptureFrame(byte[] data, int dataLen, int width, int height, int cameraAngle, int colorFormat, int srcType);

android的接口位于com.tencent.av.sdk.AVVideoCtr
```

### 如何解决Android方法数超过65535的限制？
请看相关文章介绍，点[这里](http://tech.meituan.com/mt-android-auto-split-dex.html)
