## 功能概述

摄像头推流，是指采集手机摄像头的画面以及麦克风的声音，进行编码之后再推送到直播云平台上。腾讯云 LiteAVSDK 通过 TXLivePusher 接口提供摄像头推流能力，如下是 LiteAVSDK 的简单版 Demo 中演示摄像头推流的相关操作界面：
![](https://main.qcloudimg.com/raw/52ee09ae4039d24f39e3cf8110e632c7.jpg)

## 特别说明

- **不绑定腾讯云**
  SDK 不绑定腾讯云，如果要推流到非腾讯云地址，请在推流前设置 TXLivePushConfig 中的 `enableNearestIP`为 false。但当您要推流的地址为腾讯云地址时，请务必在推流前将其设置为 YES，否则 SDK 针对腾讯云的协议优化将不能发挥作用。

- **真机调试**
  由于 SDK 大量使用 Android 系统的音视频接口，这些接口在仿真模拟器下往往不能工作，推荐您尽量使用真机调试。

## 示例代码

| 所属平台 |                         GitHub 地址                          |           关键类            |
| :------: | :----------------------------------------------------------: | :-------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/Demo/TXLiteAVDemo/LivePusherDemo/CameraPushDemo/CameraPushViewController.m) | CameraPushViewController.m  |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/XiaoZhiBo/app/src/main/java/com/tencent/qcloud/xiaozhibo/anchor/screen/TCScreenAnchorActivity.java ) | TCScreenAnchorActivity.java |


## 功能对接

### 1. 下载 SDK 开发包

[下载](https://cloud.tencent.com/document/product/454/7873) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/454/7877) 将 SDK 嵌入您的 App 工程中。


### 2. 给 SDK 配置 License 授权

单击 [License 申请](https://console.cloud.tencent.com/live/license) 获取测试用 License，您会获得两个字符串：其中一个字符串是 licenseURL，另一个字符串是解密 key。

在您的 App 调用企业版 SDK 相关功能之前（建议在 Application类中）进行如下设置：

```java
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licence url
        String licenceKey = ""; // 获取到的 licence key
        TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);
    }
}
```

### 3. 初始化 TXLivePusher 组件

首先创建一个`TXLivePushConfig`对象。该对象可以指定一些高级配置参数，但一般情况下我们不建议您操作该对象，因为我们已经在其内部配置好了所有需要校调的参数。之后再创建一个 `TXLivePusher` 对象，该对象负责完成推流的主要工作。

```java   
 TXLivePushConfig mLivePushConfig  = new TXLivePushConfig();     
 TXLivePusher mLivePusher = new TXLivePusher(this); 
 
// 一般情况下不需要修改 config 的默认配置   
 mLivePusher.setConfig(mLivePushConfig);    
```
[](id:step4)
### 4. 开启摄像头预览  

欲展示摄像头的预览画面，您需要先给 SDK 提供一个用于显示视频画面的`TXCloudVideoView`对象，由于`TXCloudVideoView`是继承自 Android 中的`FrameLayout`，所以您可以直接在 xml 文件中添加一个视频渲染控件：    

```xml  
<com.tencent.rtmp.ui.TXCloudVideoView   
        android:id="@+id/pusher_tx_cloud_view"  
        android:layout_width="match_parent" 
        android:layout_height="match_parent" /> 
```

之后，就可以通过调用 TXLivePusher 中的`startCameraPreview`接口开启当前手机摄像头的预览画面。 

```java     
 //启动本地摄像头预览    
 TXCloudVideoView mPusherView = (TXCloudVideoView) findViewById(R.id.pusher_tx_cloud_view); 
 mLivePusher.startCameraPreview(mPusherView);   
```

### 5. 启动和结束推流  

如果已经启动了摄像头预览，就可以调用 TXLivePusher 中的`startPusher`接口开始推流。  

```java 
String rtmpURL = "rtmp://test.com/live/xxxxxx"; //此处填写您的 rtmp 推流地址  
int ret = mLivePusher.startPusher(rtmpURL.trim());  
if (ret == -5) {    
    Log.i(TAG, "startRTMPPush: license 校验失败");  
}       
```

推流结束后，可以调用 TXLivePusher 中的`stopPusher`接口结束推流。请注意，如果已经启动了摄像头预览，请在结束推流时将其关闭，否则会导致 SDK 的表现异常。  

```java 
mLivePusher.stopPusher();   
mLivePusher.stopCameraPreview(true); //如果已经启动了摄像头预览，请在结束推流时将其关闭。    
```

- **获取可用的推流 URL** 
开通直播服务后，可以使用 [【直播控制台】>【直播工具箱】>【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 生成推流地址，详细信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。 
![](https://main.qcloudimg.com/raw/7110d39cdb464b789bd68301f4de7ebe.png)   
- **返回 -5 的原因**    
如果 `startPusher` 接口返回 -5，则代表您的 License 校验失败了，请检查第2步“给 SDK 配置 License 授权”中的工作是否有问题。   

### 6. 纯音频推流    

如果您的直播场景是纯音频直播，不需要视频画面，那么您可以不执行 [第 4 步](#step4) 中的操作，取而代之的是开启 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的`enablePureAudioPush`配置。   

```java     
TXLivePushConfig mLivePushConfig  = new TXLivePushConfig();         
TXLivePusher mLivePusher = new TXLivePusher(this);  
    
//开启纯音频推流，只有在调用 startPusher 前设置才会生效。    
mLivePushConfig.enablePureAudioPush(true);  
mLivePusher.setConfig(mLivePushConfig); 
String rtmpURL = "rtmp://test.com/live/xxxxxx";     
mLivePusher.startPusher(rtmpURL.trim());    
```

如果您启动纯音频推流，但是 rtmp、flv 、hls 格式的播放地址拉不到流，那是因为线路配置问题，请提工单联系我们帮忙修改配置。  

### 7. 设定画面清晰度  

调用 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772) 中的`setVideoQuality`接口，可以设定观众端的画面清晰度。之所以说是观众端的画面清晰度，是因为主播看到的视频画面是未经编码压缩过的高清原画，不受设置的影响。而`setVideoQuality`设定的视频编码器的编码质量，观众端可以感受到画质的差异。详情请参见 [设定画面质量](https://cloud.tencent.com/document/product/454/9868#.E8.AE.BE.E5.AE.9A.E5.BB.BA.E8.AE.AE)。    
![](https://main.qcloudimg.com/raw/0c058cb8c8aa1033c99e6d551f3df1aa.png)    

### 8. 美颜美白和红润特效    

调用 TXLivePush 中的`setBeautyFilter`接口可以设置美颜效果，SDK 中提供了三种磨皮算法（style），定义见 `TXLiveConstants.java` 文件：    

| 美颜风格 | 效果说明 |     
|---------|---------|   
| TXLiveConstants.BEAUTY_STYLE_SMOOTH | 光滑风格，算法更加注重皮肤的光滑程度，适合秀场直播类场景下使用。 |  
| TXLiveConstants.BEAUTY_STYLE_NATURE| 自然风格，算法更加注重保留皮肤细节，适合对真实性要求更高的主播。|    
| TXLiveConstants.BEAUTY_STYLE_HAZY| 朦胧风格，算法会更加侧重画面去噪，使整体画面风格偏柔和。|  

![](https://main.qcloudimg.com/raw/a56fe175cd1f4fc7327865ba3e6d5786.jpg)    

```java 
 //style             美颜算法：  0：光滑  1：自然  2：朦胧    
 //beautyLevel       磨皮等级： 取值为 0-9.取值为 0 时代表关闭美颜效果.默认值: 0,即关闭美颜效果.  
 //whiteningLevel    美白等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果.  
 //ruddyLevel        红润等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果.  
 // 
 public boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel);    
```


### 9. 色彩滤镜效果   

调用 TXLivePusher 中的`setFilter`接口可以设置色彩滤镜效果。所谓色彩滤镜，是指一种将整个画面色调进行区域性调整的技术，例如将画面中的淡黄色区域淡化实现肤色亮白的效果，或者将整个画面的色彩调暖让视频的效果更加清新和温和。   

调用 TXLivePush 中的`setSpecialRatio`接口可以设定滤镜的浓度，设置的浓度越高，滤镜效果也就越明显。 

从手机 QQ 和 Now 直播的经验来看，单纯通过 `setBeautyStyle` 调整磨皮效果是不够的，只有将美颜效果和`setFilter`配合使用才能达到更加多变的美颜效果。所以，我们的设计师团队提供了17种默认的色彩滤镜，并将其默认打包在了 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo) 中供您使用。 
![](https://main.qcloudimg.com/raw/5850b01bd4cac9c166f7a74a87538bda.jpg)    

```java 
//选择期望的色彩滤镜文件   
Bitmap filterBmp = decodeResource(getResources(), R.drawable.filter_biaozhun);  
mLivePusher.setFilter(filterBmp);   
mLivePusher.setSpecialRatio(0.5f);  
```

### 10. 控制摄像头   

TXLivePusher 提供了一组 API 用户控制摄像头的行为：  

| API 函数 | 功能说明 | 备注说明 |    
|---------|---------|---------| 
| switchCamera | 切换前后摄像头 | - |  
| turnOnFlashLight | 打开或关闭闪光灯 | 仅在当前是后置摄像头时有效。| 
| setZoom | 调整摄像头的焦距 | 可以通过 TXLivePusher 的`getMaxZoom()`函数获取最大焦距，`setZoom`的取值范围即为 1 - 最大焦距。|    
| setExposureCompensation | 设置曝光比例，取值范围从-1到1 | 负数表示调低曝光，-1是最小值，对应`getMinExposureCompensation`。正数表示调高曝光，1是最大值，对`getMaxExposureCompensation`。0表示不调整曝光，默认值为0。| 

除了 TXLivePusher，TXLivePushConfig 中也提供了一个叫做`setTouchFocus`的设置项，用于控制是手动对焦还是自动对焦。  
![](https://main.qcloudimg.com/raw/b84df5af90a04977987712e4107e4c48.jpg)    

```java     
 TXLivePushConfig mLivePushConfig  = new TXLivePushConfig();        
 TXLivePusher mLivePusher = new TXLivePusher(this);     
    
 //开启手动曝光（需要 API 14 以上的 Android 系统才能支持） 
 mLivePushConfig.setTouchFocus(true);   
 mLivePusher.setConfig(mLivePushConfig);    
```

### 11. 观众端的镜像效果    

调用 TXLivePusher 中的`setMirror`接口可以设置观众端的镜像效果。之所以说是观众端的镜像效果，是因为当主播在使用前置摄像头直播时，自己看到的画面会被 SDK 默认反转，这时主播的体验跟自己照镜子时的体验是保持一致的。`setMirror`所影响的是观众端观看到的画面情况，如下图所示：   
![](https://main.qcloudimg.com/raw/29e793c537604e9093cf7544446e154b.jpg)    

### 12. 横屏推流    

大多数情况下，主播习惯以“竖屏持握”手机进行直播拍摄，观众端看到的也是竖屏分辨率的画面（例如 540 × 960 这样的分辨率）；有时主播也会“横屏持握”手机，这时观众端期望能看到是横屏分辨率的画面（例如 960 × 540 这样的分辨率），如下图所示： 
![](https://main.qcloudimg.com/raw/b1e58275542aac52fb861745d95246cc.png)    

TXLivePusher 默认推出的是竖屏分辨率的视频画面，如果希望推出横屏分辨率的画面，需要：    

1. 设置 TXLivePushConfig 中的`setHomeOrientation`改变观众端看到的视频画面的宽高比方向。    
2. 调用 TXLivePusher 中的`setRenderRotation`接口改变主播端的视频画面的渲染方向。  

```java 
public void onOrientationChange(boolean isPortrait) {   
    if (isPortrait) {   
        mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN);  
        mLivePusher.setConfig(mLivePushConfig); 
        mLivePusher.setRenderRotation(0);   
    } else {    
        mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT); 
        mLivePusher.setConfig(mLivePushConfig); 
        // 因为采集旋转了，为了保证本地渲染是正的，则设置渲染角度为90度。 
        mLivePusher.setRenderRotation(90);  
    }   
}   
```

>! Android 中的 Activity 支持跟随手机的重力感应自动渲染，如果您开启了 Activity 的自动重力感应旋转，请参见 [CameraPushMainActivity.java](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo/livepusherdemo/src/main/java/com/tencent/liteav/demo/livepusher/camerapush/ui/CameraPushMainActivity.java)  中的`setRotationForActivity`以及相关示例代码。    
>![](https://main.qcloudimg.com/raw/f72f665590b6676989dfa4187ef8e15d.png)   

### 13. 隐私模式（垫片推流）  

有时候主播的一些动作不希望被观众看到，但直播过程中又不能下播，那就可以考虑进入隐私模式。在隐私模式下，SDK 可以暂停采集主播手机的摄像头画面以及麦克风声音，并使用一张默认图片作为替代图像进行推流，也就是所谓的“垫片”。  
![](https://main.qcloudimg.com/raw/d0fc9968c5d22f632f8f318b1d35406b.jpg)    

通过 TXLivePushConfig 中的`setPauseImg`接口可以设置垫片用的背景图片、垫片的最大时长以及视频帧率。    
通过 TXLivePushConfig 中的`setPauseFlag`接口可以设置是暂停视频采集、还是暂停声音采集，还是两者都暂停。 

```java 
TXLivePushConfig mLivePushConfig  = new TXLivePushConfig();         
TXLivePusher mLivePusher = new TXLivePusher(this);  
            
// bitmap: 用于指定垫片图片，最大尺寸不能超过 1920*1920  
// time：垫片最长持续时间，单位是秒，300即代表最长持续300秒    
// fps：垫片帧率，最小值为 5fps，最大值为 20fps。   
Bitmap bitmap = decodeResource(getResources(), R.drawable.pause_publish);   
mLivePushConfig.setPauseImg(bitmap);    
mLivePushConfig.setPauseImg(300, 5);    
//表示仅暂停视频采集，不暂停音频采集 
//mLivePushConfig.setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO); 
//表示同时暂停视频和音频采集 
mLivePushConfig.setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO|PAUSE_FLAG_PAUSE_AUDIO);    
mLivePusher.setConfig(mLivePushConfig);     
```

设置完成之后，就可以调用 TXLivePusher 中的`pausePusher`进入隐私模式，也可以调用`resumePusher`退出隐私模式，但请注意保持正确的调用顺序：startPush=> ( pausePush => resumePush ) => stopPush，错误的调用顺序会导致 SDK 表现异常，因此使用成员变量对执行顺序进行保护是很有必要的。    

```java 
// 进入隐私模式   
mLivePusher.pausePusher();  
... 
// 退出隐私模式   
mLivePusher.resumePusher(); 
```

>! 
>- SDK 支持在 App 切后台之后继续采集画面和声音，您只需不调用`pausePusher()`就可以达到这个效果，但这不利于保护主播的隐私。  
>- 隐私模式可以通过在 App 界面上加一个切换按钮来让主播自主进入，也可以编写代码，让 App 在切后台时自动进入，目前 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo) 就采用了 App 切后台时自动进入隐私模式的交互方案，注释掉源码中对`pausePusher()`和`resumePusher()`的调用就可以关闭这个特性。 


### 14. 背景混音和混响    
![](https://main.qcloudimg.com/raw/e5c1b903cf5176f996a0b30dbb804032.jpg)   

调用 TXLivePush 中的 BGM 相关接口可以实现背景混音功能。背景混音是指主播在直播时可以选取一首歌曲伴唱，歌曲会在主播的手机端播放出来，同时也会被混合到音视频流中被观众端听到，所以被称为“混音”。    

| 接口 | 说明 | 
|-------|---------| 
| playBGM | 通过 path 传入一首歌曲，[小直播 Demo](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.9B.B4.E6.92.AD-app) 中我们是从 iOS 的本地媒体库中获取音乐文件。 |   
| stopBGM|停止播放背景音乐。|    
| pauseBGM|暂停播放背景音乐。|   
| resumeBGM|继续播放背景音乐。|  
| setMicVolumeOnMixing|设置混音时麦克风的音量大小，推荐在 UI 上实现相应的一个滑动条，由主播自己设置。 |  
| setBGMVolume|设置混音时背景音乐的音量大小，推荐在 UI 上实现相应的一个滑动条，由主播自己设置。|  
| setBgmPitch|调整背景音乐的音调高低。| 

调用 TXLivePush 中的`setReverbType`接口可以设置混响效果，例如 KTV、会堂、磁性、金属等，这些效果也会作用到观众端。    
调用 TXLivePush 中的`setVoiceChangerType`接口可以设置变调效果，例如“萝莉音”，“大叔音”等，用来增加直播和观众互动的趣味性，这些效果也会作用到观众端。    

### 15. 设置 Logo 水印  

通过 TXLivePushConfig 中的`setWatermark`接口可以让 SDK 在推出的视频流中增加一个水印，水印的位置位由该接口函数的后三个参数决定。  

- SDK 所要求的水印图片格式为 png 而不是 jpg，因为 png 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（将 jpg 图片在 Windows 下修改后缀名是不起作用的）。   
- `setWatermark`中后三个参数设置的是水印图片相对于推流分辨率的归一化坐标。假设推流分辨率为：540 x 960，后三个参数 x、y 和 width 被分别设置为：（0.1，0.1，0.1），那么水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。    

```java 
//设置视频水印    
TXLivePushConfig mLivePushConfig  = new TXLivePushConfig(); 
//四个参数依次是水印图片的 Bitmap、水印位置的 X 轴坐标，水印位置的 Y 轴坐标，水印宽度。后面三个参数取值范围是[0, 1]    
Bitmap waterBmp = decodeResource(getResources(), R.drawable.filter_water);  
mLivePushConfig.setWatermark(waterBmp, 0.1f, 0.1f, 0.1f);   
mLivePusher.setConfig(mLivePushConfig); 
```

### 16. 本地录制    

调用 TXLivePusher 中的`startRecord`接口可以启动本地录制，录制格式为 MP4，通过参数`videoPath`可以指定 MP4 文件的存放路径。    
调用 TXLivePusher 中的`stopRecord`接口可以结束录制。如果您已经通过`setVideoRecordListener`接口注册监听器给 TXLivePusher，那么一旦录制结束，录制出来的文件会通过`TXRecordCommon.ITXVideoRecordListener`回调通知出来。   

```java 
// 启动录制：返回 0 开始录制成功；-1 表示正在录制，这次启动录制忽略；-2 表示还未开始推流，这次启动录制失败 
public int startRecord(final String videoFilePath)  
// 结束录制 
public void stopRecord()    
// 视频录制回调   
public interface ITXVideoRecordListener {   
        void onRecordEvent(final int event, final Bundle param);    
        void onRecordProgress(long milliSecond);    
        void onRecordComplete(TXRecordResult result);   
}   
```

>!  
>1. 只有启动推流后才能开始录制，非推流状态下启动录制无效。 
>2. 出于安装包体积的考虑，仅专业版和企业版两个版本的 LiteAVSDK 支持该功能，直播精简版仅定义了接口但并未实现。  
>3. 录制过程中请勿动态切换分辨率和软硬编，会有很大概率导致生成的视频异常。 
>4. 使用 TXLivePusher 录制视频会一定程度地降低推流性能，云直播服务也提供了云端录制功能，具体使用方法请参考 [直播录制](https://cloud.tencent.com/document/product/267/32739)。    

### 17. 主播端弱网提醒 
手机连接 Wi-Fi 网络不一定就非常好，如果 Wi-Fi 信号差或者出口带宽很有限，可能网速不如4G，如果主播在推流时遇到网络很差的情况，需要有一个友好的提示，提示主播应当切换网络。    
![](https://main.qcloudimg.com/raw/0d0ccb1fca6cc847d51499a4f9e37e18.jpg)    
通过 TXLivePushListener 里的 onPlayEvent 可以捕获 **PUSH_WARNING_NET_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。此时就可以像上图一样在 UI 上弹出一个“弱网提示”。    

```objectiveC   
@Override   
    public void onPushEvent(int event, Bundle param) {  
        if (event == TXLiveConstants.PUSH_ERR_NET_DISCONNECT    
                || event == TXLiveConstants.PUSH_ERR_INVALID_ADDRESS    
                || event == TXLiveConstants.PUSH_ERR_OPEN_CAMERA_FAIL   
                || event == TXLiveConstants.PUSH_ERR_OPEN_MIC_FAIL) {   
            // 遇到以上错误，则停止推流 
            //...   
        } else if (event == TXLiveConstants.PUSH_WARNING_NET_BUSY) {    
            //您当前的网络环境不佳，请尽快更换网络保证正常直播  
            showNetBusyTips();  
        }   
    }   
```

### 18. 发送 SEI 消息

调用 TXLivePush 中的`sendMessageEx`接口可以发送 SEI 消息。所谓 SEI，是视频编码数据中规定的一种附加增强信息，平时一般不被使用，但我们可以在其中加入一些自定义消息，这些消息会被直播 CDN 转发到观众端。使用场景有：

1. 答题直播：推流端将**题目**下发到观众端，可以做到“音-画-题”完美同步。
2. 秀场直播：推流端将**歌词**下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
3. 在线教育：推流端将**激光笔**和**涂鸦**操作下发到观众端，可以在播放端实时地划圈划线。

由于自定义消息是直接被塞入视频数据中的，所以不能太大（几个字节比较合适），一般常用于塞入自定义的时间戳等信息。

```
//Android 示例代码
String msg = "test";
mTXLivePusher.sendMessageEx(msg.getBytes("UTF-8"));
```

常规开源播放器或者网页播放器是不能解析 SEI 消息的，必须使用 LiteAVSDK 中自带的 TXLivePlayer 才能解析这些消息：

1. 设置 TXLivePlayConfig 中的`enableMessage`选项为 YES。
2. 当 TXLivePlayer 所播放的视频流中由 SEI 消息时，会通过 TXLivePlayListener 中的 `onPlayEvent(PLAY_EVT_GET_MESSAGE) `通知给您。

## 事件处理

### 1. 事件监听

SDK 通过 ITXLivePushListener 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://cloud.tencent.com/document/product/454/17246) ，也可以查阅`TXLiveConstants.java`代码文件。需要注意的是：**ITXLivePushListener 只能监听得到 PUSH_ 前缀的推流事件**。

### 2. 常规事件

一次成功的推流都会通知的事件有（例如，收到1003就意味着摄像头的画面开始渲染）：

| 事件 ID                   | 数值 | 含义说明                                                     |
| ------------------------- | ---- | ------------------------------------------------------------ |
| PUSH_EVT_CONNECT_SUCC     | 1001 | 已经成功连接到腾讯云推流服务器。                             |
| PUSH_EVT_PUSH_BEGIN       | 1002 | 与服务器握手完毕,一切正常，准备开始推流。                    |
| PUSH_EVT_OPEN_CAMERA_SUCC | 1003 | 推流器已成功打开摄像头（部分 Android 手机这个过程需要1秒 - 2秒）。 |

### 3. 错误通知

SDK 发现部分严重问题，推流无法继续（例如，用户禁用了 App 的 Camera 权限导致摄像头打不开）：

| 事件 ID                         | 数值  | 含义说明                                             |
| ------------------------------- | ----- | ---------------------------------------------------- |
| PUSH_ERR_OPEN_CAMERA_FAIL       | -1301 | 打开摄像头失败。                                     |
| PUSH_ERR_OPEN_MIC_FAIL          | -1302 | 打开麦克风失败。                                     |
| PUSH_ERR_VIDEO_ENCODE_FAIL      | -1303 | 视频编码失败。                                       |
| PUSH_ERR_AUDIO_ENCODE_FAIL      | -1304 | 音频编码失败。                                       |
| PUSH_ERR_UNSUPPORTED_RESOLUTION | -1305 | 不支持的视频分辨率。                                 |
| PUSH_ERR_UNSUPPORTED_SAMPLERATE | -1306 | 不支持的音频采样率。                                 |
| PUSH_ERR_NET_DISCONNECT         | -1307 | 网络断连，且经三次重连无效，更多重试请自行重启推流。 |

### 4. 警告事件

SDK 发现了一些问题，但这并不意味着推流无法继续，SDK 会在警告事件发生后，尽可能地启动一些重试性的保护逻辑或者恢复措施，例如：

- **WARNING_NET_BUSY** 主播网络差，如果您需要 UI 提示，这个 WARNING 相对比较有用。
- **WARNING_SERVER_DISCONNECT** 推流请求被后台拒绝了，出现这个问题一般是由于推流地址里的 txSecret 计算错了，或者是推流地址被其他人占用了（一个推流 URL 同时只能有一个端推流）。

| 事件 ID                           | 数值 | 含义说明                                                     |
| --------------------------------- | ---- | ------------------------------------------------------------ |
| PUSH_WARNING_NET_BUSY             | 1101 | 网络状况不佳：上行带宽太小，上传数据受阻。                   |
| PUSH_WARNING_RECONNECT            | 1102 | 网络断连，已启动自动重连（自动重连连续失败超过三次会放弃）。 |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 1103 | 硬编码启动失败，采用软编码。                                 |
| PUSH_WARNING_DNS_FAIL             | 3001 | RTMP-DNS 解析失败（会触发重试流程）。                        |
| PUSH_WARNING_SEVER_CONN_FAIL      | 3002 | RTMP 服务器连接失败（会触发重试流程）。                      |
| PUSH_WARNING_SHAKE_FAIL           | 3003 | RTMP 服务器握手失败（会触发重试流程）。                      |
| PUSH_WARNING_SERVER_DISCONNECT    | 3004 | RTMP 服务器主动断开连接（会触发重试流程）。                  |

