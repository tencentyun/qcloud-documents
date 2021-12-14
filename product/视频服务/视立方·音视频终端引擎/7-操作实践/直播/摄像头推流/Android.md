## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 功能概述

摄像头推流，是指采集手机摄像头的画面以及麦克风的声音，进行编码之后再推送到直播云平台上。腾讯云视立方 LiteAVSDK 通过 V2TXLivePusher 接口提供摄像头推流能力，如下是 LiteAVSDK 腾讯云工具包 App 中演示摄像头推流的相关操作界面：
![#800px](https://main.qcloudimg.com/raw/52ee09ae4039d24f39e3cf8110e632c7.jpg)

## 特别说明
**真机调试：**  由于 SDK 大量使用 Android 系统的音视频接口，这些接口在仿真模拟器下往往不能工作，推荐您尽量使用真机调试。

## 示例代码
| 所属平台 |                         GitHub 地址                          |           关键类            |
| :------: | :----------------------------------------------------------: | :-------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/LiteAVProfessional_iOS/blob/master/Demo/TXLiteAVDemo/LivePusherDemo/CameraPushDemo/CameraPushViewController.m) | CameraPushViewController.m  |
| Android  | [Github](https://github.com/tencentyun/LiteAVProfessional_Android/blob/master/Demo/livepusherdemo/src/main/java/com/tencent/liteav/demo/livepusher/camerapush/ui/CameraPushMainActivity.java) | CameraPushMainActivity.java |
>?除上述示例外，针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。
>- iOS：[MLVB-API-Example](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example-OC)
>- Android：[MLVB-API-Example](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example)

## 功能对接

[](id:step1)
### 1. 下载 SDK 开发包

[下载](https://cloud.tencent.com/document/product/1449/56978) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/1449/56987) 将 SDK 嵌入您的 App 工程中。

[](id:step2)
### 2. 给 SDK 配置 License 授权
单击 [License 申请](https://cloud.tencent.com/document/product/1449/56981) 获取测试用 License，您会获得两个字符串：其中一个字符串是 licenceURL ，另一个字符串是解密 licenceKey。
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

[](id:step3)
### 3. 初始化 V2TXLivePusher 组件

创建一个 `V2TXLivePusher` 对象，该对象负责完成推流的主要工作。

```java   
V2TXLivePusher mLivePusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTMP); //指定对应的直播协议为 RTMP
```

[](id:step4)
### 4. 开启摄像头预览  

想要开启摄像头的预览画面，您需要先给 SDK 提供一个用于显示视频画面的 `TXCloudVideoView` 对象，由于 `TXCloudVideoView` 是继承自 Android 中的 `FrameLayout`，所以您可以：
1. 直接在 xml 文件中添加一个视频渲染控件：    
```xml  
<com.tencent.rtmp.ui.TXCloudVideoView   
              android:id="@+id/pusher_tx_cloud_view"  
              android:layout_width="match_parent" 
              android:layout_height="match_parent" /> 
```
2. 通过调用 V2TXLivePusher 中的`startCamera`接口开启当前手机摄像头的预览画面。 
```java     
//启动本地摄像头预览    
TXCloudVideoView mPusherView = (TXCloudVideoView) findViewById(R.id.pusher_tx_cloud_view); 
mLivePusher.setRenderView(mPusherView);
mLivePusher.startCamera(true);
```

[](id:step5)
### 5. 启动和结束推流
如果已经通过`startCamera`接口启动了摄像头预览，就可以调用 V2TXLivePusher 中的 [startPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#ab4f8adaa0616d54d6ed920e49377a08a) 接口开始推流。推流地址可以使用 [TRTC 地址](https://cloud.tencent.com/document/product/454/7915#.E8.87.AA.E4.B8.BB.E6.8B.BC.E8.A3.85-rtc-.E8.BF.9E.E9.BA.A6.2Fpk-url) ，或者使用 [RTMP 地址](https://cloud.tencent.com/document/product/454/7915#.E8.87.AA.E4.B8.BB.E6.8B.BC.E8.A3.85.E6.8E.A8.E6.B5.81-url) ，前者使用 UDP 协议，推流质量更高，并支持连麦互动。
```objectivec 
//启动推流， URL 可以使用 trtc:// 或者 rtmp:// 两种协议，前者支持连麦功能
String rtmpURL = "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx";  //支持连麦
String rtmpURL = "rtmp://test.com/live/streamid?txSecret=xxxxx&txTime=xxxxxxxx";    //不支持连麦，直接推流到直播 CDN
int ret = mLivePusher.startPush(rtmpURL.trim());  
if (ret == V2TXLIVE_ERROR_INVALID_LICENSE) {    
    Log.i(TAG, "startRTMPPush: license 校验失败");  
}       
```

推流结束后，可以调用 V2TXLivePusher 中的 [stopPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#af07c1dcff91b43a2309665b8663ed530) 接口结束推流。
```objectivec
//结束推流
mLivePusher.stopPush();
```
>! 如果已经启动了摄像头预览，请在结束推流时将其关闭。 

- **如何获取可用的推流 URL** 
开通直播服务后，可以使用 [【直播控制台】>【直播工具箱】>【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 生成推流地址，详细信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。 
![](https://main.qcloudimg.com/raw/7110d39cdb464b789bd68301f4de7ebe.png)   
- **返回 V2TXLIVE_ERROR_INVALID_LICENSE 的原因？**    
如果 `startPush` 接口返回 `V2TXLIVE_ERROR_INVALID_LICENSE`，则代表您的 License 校验失败了，请检查 [第2步：给 SDK 配置 License 授权](#step2) 中的工作是否有问题。   

[](id:step6)
### 6. 纯音频推流    
如果您的直播场景是纯音频直播，不需要视频画面，那么您可以不执行 [第4步](#step4) 中的操作，或者在调用 `startPush` 之前调用 `stopCamera` 接口即可。
```java     
V2TXLivePusher mLivePusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTMP); //指定对应的直播协议为 RTMP
mLivePusher.startMicrophone();
//启动推流， URL 可以使用 trtc:// 或者 rtmp:// 两种协议，前者支持连麦功能
String rtmpURL = "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx";  //支持连麦
String rtmpURL = "rtmp://test.com/live/streamid?txSecret=xxxxx&txTime=xxxxxxxx";    //不支持连麦，直接推流到直播 CDN
int ret = mLivePusher.startPush(rtmpURL.trim());  
```
>? 如果您启动纯音频推流，但是 RTMP、FLV 、HLS 格式的播放地址拉不到流，那是因为线路配置问题，请 [提工单](https://console.cloud.tencent.com/workorder/category) 联系我们帮忙修改配置。  

[](id:step7)
### 7. 设定画面清晰度  
调用 V2TXLivePusher 中的 [setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a2695806cb6c74ccce4b378d306ef0a02) 接口，可以设定观众端的画面清晰度。之所以说是观众端的画面清晰度，是因为主播看到的视频画面是未经编码压缩过的高清原画，不受设置的影响。而 `setVideoQuality` 设定的视频编码器的编码质量，观众端可以感受到画质的差异。详情请参见 [设定画面质量](https://cloud.tencent.com/document/product/1449/57016)。

[](id:step8)
### 8. 美颜美白和红润特效    
![](https://main.qcloudimg.com/raw/b0ddfe1f97d73c9fc8e42caf994211b7.jpg)
调用 V2TXLivePusher 中的 [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a3fdfeb3204581c27bbf1c8b5598714fb) 接口可以获取 TXBeautyManager 实例进一步设置美颜效果。

#### 美颜风格
SDK 内置三种不同的磨皮算法，每种磨皮算法即对应一种美颜风格，您可以选择最适合您产品定位的方案。定义见  `TXLiveConstants.java`  文件：
<table><tr>
<th>美颜风格</th><th>效果说明</th>
</tr><tr>
<td>BEAUTY_STYLE_SMOOTH</td>
<td>光滑，适用于美女秀场，效果比较明显</td>
</tr><tr>
<td>BEAUTY_STYLE_NATURE</td>
<td>自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然</td>
</tr><tr>
<td>BEAUTY_STYLE_PITU</td>
<td>由上海优图实验室提供的美颜算法，磨皮效果介于光滑和自然之间，比光滑保留更多皮肤细节，比自然磨皮程度更高</td>
</tr></table>

美颜风格可以通过 TXBeautyManager 的 `setBeautyStyle` 接口设置：
<table>
<tr><th>美颜风格</th><th width=51%>设置方式</th><th>接口说明</th>
</tr><tr>
<td>美颜级别</td>
<td>通过 TXBeautyManager 的 <code>setBeautyLevel</code> 设置</td>
<td>取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显</td>
</tr><tr>
<td>美白级别</td>
<td>通过 TXBeautyManager 的 <code>setWhitenessLevel</code> 设置</td>
<td>取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显</td>
</tr><tr>
<td>红润级别</td>
<td>通过 TXBeautyManager 的 <code>setRuddyLevel</code> 设置</td>
<td>取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显</td>
</tr></table>

[](id:step9)
### 9. 色彩滤镜效果   
![](https://main.qcloudimg.com/raw/eb06687c79243fa3a6befb30ff62e09e.jpg)
- 调用 V2TXLivePusher 中的 [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a3fdfeb3204581c27bbf1c8b5598714fb) 接口可以获取 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html) 实例进一步设置美色彩滤镜效果。
- 调用 TXBeautyManager 的 `setFilter` 接口可以设置色彩滤镜效果。所谓色彩滤镜，是指一种将整个画面色调进行区域性调整的技术，例如将画面中的淡黄色区域淡化实现肤色亮白的效果，或者将整个画面的色彩调暖让视频的效果更加清新和温和。   
- 调用 TXBeautyManager 的 `setFilterStrength` 接口可以设定滤镜的浓度，设置的浓度越高，滤镜效果也就越明显。 

从手机 QQ 和 Now 直播的经验来看，单纯通过 TXBeautyManager 的 `setBeautyStyle` 调整美颜风格是不够的，只有将美颜风格和`setFilter`配合使用才能达到更加丰富的美颜效果。所以，我们的设计师团队提供了17种默认的色彩滤镜，并将其默认打包在了 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo) 中供您使用。 

```java 
//选择期望的色彩滤镜文件   
Bitmap filterBmp = decodeResource(getResources(), R.drawable.filter_biaozhun);  
mLivePusher.getBeautyManager().setFilter(filterBmp);   
mLivePusher.getBeautyManager().setFilterStrength(0.5f);  
```

[](id:step10)
### 10. 设备管理

V2TXLivePusher 提供了一组 API 用户控制设备的行为。您通过 `getDeviceManager` 获取 TXDeviceManager 实例进一步进行设备管理，详细用法请参见 [TXDeviceManager API](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXDeviceManager__android.html)。
![](https://main.qcloudimg.com/raw/c4d8e442558891c66f315d4c0799fce3.jpg)

[](id:step11)
### 11. 观众端的镜像效果    

通过调用 V2TXLivePusher 的 [setRenderMirror](http://doc.qcloudtrtc.com/group__V2TXLivePusher__android.html#afd909d85fd0dda0db4078692b319681f) 可以改变摄像头的镜像方式，继而影响观众端观看到的镜像效果。之所以说是观众端的镜像效果，是因为当主播在使用前置摄像头直播时，默认情况下自己看到的画面会被 SDK 反转，这时主播就像照镜子一样，观众看到的效果和主播看到的是一致的。如下图所示：
![](https://main.qcloudimg.com/raw/e9841250668a9057d638ee67d0b0afee.png)   

[](id:step12)
### 12. 横屏推流    

大多数情况下，主播习惯以“竖屏持握”手机进行直播拍摄，观众端看到的也是竖屏分辨率的画面（例如 540 × 960 这样的分辨率）；有时主播也会“横屏持握”手机，这时观众端期望能看到是横屏分辨率的画面（例如 960 × 540 这样的分辨率），如下图所示： 
![](https://main.qcloudimg.com/raw/b1e58275542aac52fb861745d95246cc.png)    
V2TXLivePusher 默认推出的是竖屏分辨率的视频画面，如果希望推出横屏分辨率的画面，可以修改`setVideoQuality`接口的参数来设定观众端的画面横竖屏模式。
```java 
mLivePusher.setVideoQuality(mVideoResolution, isLandscape ? V2TXLiveVideoResolutionModeLandscape : V2TXLiveVideoResolutionModePortrait);   
```

[](id:step13)
### 13. 音效设置

调用 V2TXLivePusher 中的 `getAudioEffectManager` 获取 TXAudioEffectManager 实例可以实现背景混音、耳返、混响等音效功能。背景混音是指主播在直播时可以选取一首歌曲伴唱，歌曲会在主播的手机端播放出来，同时也会被混合到音视频流中被观众端听到，所以被称为“混音”。
![](https://main.qcloudimg.com/raw/269e653bc68c73c69feeb6418c513c25.jpg)
- 调用 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__android.html) 中的 `enableVoiceEarMonitor` 选项可以开启耳返功能，“耳返”指的是当主播带上耳机来唱歌时，耳机中要能实时反馈主播的声音。
- 调用 TXAudioEffectManager 中的 `setVoiceReverbType` 接口可以设置混响效果，例如 KTV、会堂、磁性、金属等，这些效果也会作用到观众端。
- 调用 TXAudioEffectManager 中的 `setVoiceChangerType` 接口可以设置变调效果，例如“萝莉音”，“大叔音”等，用来增加直播和观众互动的趣味性，这些效果也会作用到观众端。

![](https://main.qcloudimg.com/raw/a90a110e2950568b9d7cd6bef8e0893b.png)
>? 详细用法请参见 [TXAudioEffectManager API](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXDeviceManager__android.html)。

[](id:step14)
### 14. 设置 Logo 水印  

设置 V2TXLivePusher 中的 [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a4f56a5a937d87e5b1ae6f77c5bab2335) 可以让 SDK 在推出的视频流中增加一个水印，水印位置位是由传入参数 `(x, y, scale)` 所决定。

- SDK 所要求的水印图片格式为 PNG 而不是 JPG，因为 PNG 图片格式有透明度信息，因而能够更好地处理锯齿等问题（将 JPG 图片修改后缀名是不起作用的）。
- `(x, y, scale)` 参数设置的是水印图片相对于推流分辨率的归一化坐标。假设推流分辨率为：540 × 960，该字段设置为：`（0.1，0.1，0.1）`，则水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。

```java 
//设置视频水印
mLivePusher.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 0.03f, 0.015f, 1f);
```

[](id:step15)
### 15. 主播端弱网提醒 
如果主播在推流时遇到网络很差的情况，需要有一个友好的提示，提示主播应当检查网络。    
通过 V2TXLivePusherObserver 里的 [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusherObserver__android.html#abd54414cbd5d52c096f9cc090cfe1fec) 可以捕获 **V2TXLIVE_WARNING_NETWORK_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。此时可以在 UI 上弹出一个“弱网提示”来强提醒主播检查网络。
<dx-codeblock>
:::java java 
@Override
public void onWarning(int code, String msg, Bundle extraInfo) {
    if (code == V2TXLiveCode.V2TXLIVE_WARNING_NETWORK_BUSY) {
        showNetBusyTips(); // 显示网络繁忙的提示
    }
} 
:::
</dx-codeblock>

[](id:step16)
### 16. 发送 SEI 消息 
调用 V2TXLivePusher 中的 [sendSeiMessage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a5ba3762815f11bf5005f151e06ae0b38) 接口可以发送 SEI 消息。所谓 SEI，是视频编码数据中规定的一种附加增强信息，平时一般不被使用，但我们可以在其中加入一些自定义消息，这些消息会被直播 CDN 转发到观众端。使用场景有：
- 答题直播：推流端将题目下发到观众端，可以做到“音-画-题”完美同步。
- 秀场直播：推流端将歌词下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
- 在线教育：推流端将激光笔和涂鸦操作下发到观众端，可以在播放端实时地划圈划线。

由于自定义消息是直接被塞入视频数据中的，所以不能太大（几个字节比较合适），一般常用于塞入自定义的时间戳等信息。
```java
//Android 示例代码
int payloadType = 5;
String msg = "test";
mTXLivePusher.sendSeiMessage(payloadType, msg.getBytes("UTF-8"));
```
常规开源播放器或者网页播放器是不能解析 SEI 消息的，必须使用 LiteAVSDK 中自带的 V2TXLivePlayer 才能解析这些消息：
1. 设置：
```java
int payloadType = 5;
mTXLivePlayer.enableReceiveSeiMessage(true, payloadType)
```
2. 当 V2TXLivePlayer 所播放的视频流中有 SEI 消息时，会通过 V2TXLivePlayerObserver 中的 onReceiveSeiMessage 回调来接收该消息。



## 事件处理

### 事件监听
SDK 通过 [V2TXLivePusherObserver](http://doc.qcloudtrtc.com/group__V2TXLivePusherObserver__android.html) 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__android.html)。

### 错误通知
SDK 发现部分严重问题，推流无法继续。

| 事件 ID                              | 数值 | 含义说明                        |
| :------------------------------------ | :---- | :------------------------------- |
| V2TXLIVE_ERROR_FAILED                | -1   | 暂未归类的通用错误            |
| V2TXLIVE_ERROR_INVALID_PARAMETER     | -2   | 调用 API 时，传入的参数不合法 |
| V2TXLIVE_ERROR_REFUSED               | -3   | API 调用被拒绝                |
| V2TXLIVE_ERROR_NOT_SUPPORTED         | -4   | 当前 API 不支持调用           |
| V2TXLIVE_ERROR_INVALID_LICENSE       | -5   | license 不合法，调用失败      |
| V2TXLIVE_ERROR_REQUEST_TIMEOUT       | -6   | 请求服务器超时                |
| V2TXLIVE_ERROR_SERVER_PROCESS_FAILED | -7   | 服务器无法处理您的请求        |

### 警告事件
SDK 发现部分警告问题，但 WARNING 级别的事件都会触发一些尝试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复。

| 事件 ID                                       | 数值  | 含义说明                                                     |
| :-------------------------------------------- | :---- | :----------------------------------------------------------- |
| V2TXLIVE_WARNING_NETWORK_BUSY                 | 1101  | 网络状况不佳：上行带宽太小，上传数据受阻                     |
| V2TXLIVE_WARNING_VIDEO_BLOCK                  | 2105  | 当前视频播放出现卡顿                                         |
| V2TXLIVE_WARNING_CAMERA_START_FAILED          | -1301 | 摄像头打开失败                                               |
| V2TXLIVE_WARNING_CAMERA_OCCUPIED              | -1316 | 摄像头正在被占用中，可尝试打开其他摄像头                     |
| V2TXLIVE_WARNING_CAMERA_NO_PERMISSION         | -1314 | 摄像头设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_MICROPHONE_START_FAILED      | -1302 | 麦克风打开失败                                               |
| V2TXLIVE_WARNING_MICROPHONE_OCCUPIED          | -1319 | 麦克风正在被占用中，例如移动设备正在通话时，打开麦克风会失败 |
| V2TXLIVE_WARNING_MICROPHONE_NO_PERMISSION     | -1317 | 麦克风设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_NOT_SUPPORTED | -1309 | 当前系统不支持屏幕分享                                       |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_START_FAILED  | -1308 | 开始录屏失败，如果在移动设备出现，可能是权限被用户拒绝了     |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_INTERRUPTED   | -7001 | 录屏被系统中断                                               |


