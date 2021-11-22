## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 功能概述
摄像头推流，是指采集手机摄像头的画面以及麦克风的声音，进行编码之后再推送到直播云平台上。腾讯云视立方 LiteAVSDK 通过 V2TXLivePusher 接口提供摄像头推流能力，如下是 LiteAVSDK 的简单版 Demo 中演示摄像头推流的相关操作界面：
![](https://main.qcloudimg.com/raw/39ee7f9e0e092d0adb9f1dff1077a482.png)

## 特别说明
**x86 模拟器调试：**由于 SDK 大量使用 iOS 系统的音视频接口，这些接口在 Mac 上自带的 x86 仿真模拟器下往往不能工作。所以，如果条件允许，推荐您尽量使用真机调试。

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
[下载](https://cloud.tencent.com/document/product/1449/56978) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/1449/56986) 将 SDK 嵌入您的 App 工程中。

[](id:step2)
### 2. 给 SDK 配置 License 授权
单击 [License 申请](https://cloud.tencent.com/document/product/1449/56981) 获取测试用的 License，您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。
在您的 App 调用 LiteAVSDK 的相关功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置：
```objc
@import TXLiteAVSDK_Professional;
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";
        
    //TXLiveBase 位于 "TXLiveBase.h" 头文件中
    [TXLiveBase setLicenceURL:licenceURL key:licenceKey]; 
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

[](id:step3)
### 3. 初始化 V2TXLivePusher 组件
创建一个`V2TXLivePusher`对象，需要指定对应的 `V2TXLiveMode`。

```objectivec   
 V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTMP]; // 指定对应的直播协议为 RTMP 
```

[](id:step4)
### 4. 开启摄像头预览
想要开启摄像头预览，首先需要调用 [V2TXLivePusher](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html) 中的`setRenderView`接口，改接口需要设置一个用于显示视频画面的 view 对象，然后调用`startCamera`接口开启当前手机摄像头的预览。

<dx-codeblock>
::: objectivec objectivec
 //创建一个 view 对象，并将其嵌入到当前界面中
 UIView *_localView = [[UIView alloc] initWithFrame:self.view.bounds];
 [self.view insertSubview:_localView atIndex:0];
 _localView.center = self.view.center;

 //启动本地摄像头预览
 [_pusher setRenderView:_localView];
 [_pusher startCamera:YES];
:::
</dx-codeblock>

> ! 如果要给 view 增加动画效果，需要修改 view 的 transform 属性而不是 frame 属性。
>```objectivec
[UIView animateWithDuration:0.5 animations:^{
	_localView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
}];
```

[](id:step5)
### 5. 启动和结束推流
如果已经通过`startCamera`接口启动了摄像头预览，就可以调用 V2TXLivePusher 中的 [startPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a33b38f236a439e7d848606acb68cc087) 接口开始推流。推流地址可以使用 [TRTC 地址](https://cloud.tencent.com/document/product/454/7915#.E8.87.AA.E4.B8.BB.E6.8B.BC.E8.A3.85-rtc-.E8.BF.9E.E9.BA.A6.2Fpk-url) ，或者使用 [RTMP 地址](https://cloud.tencent.com/document/product/454/7915#.E8.87.AA.E4.B8.BB.E6.8B.BC.E8.A3.85.E6.8E.A8.E6.B5.81-url) ，前者使用 UDP 协议，推流质量更高，并支持连麦互动。
```objectivec 
//启动推流， URL 可以使用 trtc:// 或者 rtmp:// 两种协议，前者支持连麦功能
NSString* url = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx";  //支持连麦
NSString* url = @"rtmp://test.com/live/streamid?txSecret=xxxxx&txTime=xxxxxxxx";    //不支持连麦，直接推流到直播 CDN
[_pusher startPush:url];
```

推流结束后，可以调用 V2TXLivePusher 中的 [stopPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a7332411d6264bc743b0b2bae0b8a73ae) 接口结束推流。
```objectivec
//结束推流
[_pusher stopPush];
```
>! 如果已经启动了摄像头预览，请在结束推流时将其关闭。 

-  **获取可用的推流 URL**
开通直播服务后，可以使用【直播控制台】>【辅助工具】> [【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 生成推流地址，详细信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
![](https://main.qcloudimg.com/raw/0ec9d83f340454c287d96f83eec3a3e4.png)
- **返回 V2TXLIVE_ERROR_INVALID_LICENSE 的原因**    
如果 `startPush` 接口返回 `V2TXLIVE_ERROR_INVALID_LICENSE`，则代表您的 License 校验失败了，请检查 [第2步：给 SDK 配置   License 授权](#step2) 中的工作是否有问题。

[](id:step6)
### 6. 纯音频推流
如果您的直播场景是纯音频直播，不需要视频画面，那么您可以不执行 [第4步](#step4) 中的操作，或者在调用 `startPush` 之前不调用 `startCamera` 接口即可。
```objectivec
V2TXLivePusher *_pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTMP]; 
//启动推流， URL 可以使用 trtc:// 或者 rtmp:// 两种协议，前者支持连麦功能
NSString* url = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx";  //支持连麦
NSString* url = @"rtmp://test.com/live/streamid?txSecret=xxxxx&txTime=xxxxxxxx";    //不支持连麦，直接推流到直播 CDN
[_pusher startPush:url];
[_pusher startMicrophone];
```
>? 如果您启动纯音频推流，但是 RTMP、FLV 、HLS 格式的播放地址拉不到流，那是因为线路配置问题，请 [提工单](https://console.cloud.tencent.com/workorder/category) 联系我们帮忙修改配置。

[](id:step7)
### 7. 设定画面清晰度
调用 V2TXLivePusher 中的 [setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a0b08436c1e14a8d7d9875fae59ac6d84) 接口，可以设定观众端的画面清晰度。之所以说是观众端的画面清晰度，是因为主播看到的视频画面是未经编码压缩过的高清原画，不受设置的影响。而 `setVideoQuality` 设定的视频编码器的编码质量，观众端可以感受到画质的差异。详情请参见 [设定画面质量](https://cloud.tencent.com/document/product/1449/57016)。

[](id:step8)
### 8. 美颜美白和红润特效
调用 V2TXLivePusher 中的 [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a4fb05ae6b5face276ace62558731280a) 接口可以获取 TXBeautyManager 实例进一步设置美颜效果。

#### 美颜风格
SDK 内置三种不同的磨皮算法，每种磨皮算法即对应一种美颜风格，您可以选择最适合您产品定位的方案。详情请参见 [TXBeautyManager.h](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#gafbbe0e87ec0168eacfc10e57c43abad8)  文件：

| 美颜风格 | 效果说明 |
|---------|---------|
| TXBeautyStyleSmooth | 光滑，适用于美女秀场，效果比较明显  |
| TXBeautyStyleNature | 自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然  |
| TXBeautyStylePitu | 由上海优图实验室提供的美颜算法，磨皮效果介于光滑和自然之间，比光滑保留更多皮肤细节，比自然磨皮程度更高  |

美颜风格可以通过 TXBeautyManager 的 [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#a8f2378a87c2e79fa3b978078e534ef4a) 接口设置：

<table>
<tr><th>美颜风格</th><th width=51%>设置方式</th><th>接口说明</th></tr>
<tr>
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
- 调用 V2TXLivePusher 中的 [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a4fb05ae6b5face276ace62558731280a) 接口可以获取 TXBeautyManager 实例进一步设置美色彩滤镜效果。
- 调用 TXBeautyManager 的 `setFilter` 接口可以设置色彩滤镜效果。所谓色彩滤镜，是指一种将整个画面色调进行区域性调整的技术，例如将画面中的淡黄色区域淡化实现肤色亮白的效果，或者将整个画面的色彩调暖让视频的效果更加清新和温和。   
- 调用 TXBeautyManager 的 `setFilterStrength` 接口可以设定滤镜的浓度，设置的浓度越高，滤镜效果也就越明显。 

从手机 QQ 和 Now 直播的经验来看，单纯通过 TXBeautyManager 的 `setBeautyStyle` 调整美颜风格是不够的，只有将美颜风格和`setFilter`配合使用才能达到更加丰富的美颜效果。所以，我们的设计师团队提供了17种默认的色彩滤镜，并将其默认打包在了 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/XiaoZhiBoApp/XiaoZhiBoApp/FilterResource.bundle) 中供您使用。
```objectivec
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:lookupFileName];

UIImage *image = [UIImage imageWithContentsOfFile:path];
[[_pusher getBeautyManager] setFilter:image];
[[_pusher getBeautyManager] setFilterStrength:0.5f];
```

[](id:step10)
### 10. 设备管理
V2TXLivePusher 提供了一组 API 用户控制设备的行为，您可通过 `getDeviceManager` 获取 TXDeviceManager 实例进一步进行设备管理，详细用法请参见 [TXDeviceManager API](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXDeviceManager__ios.html#interfaceTXDeviceManager)。
![](https://main.qcloudimg.com/raw/c4d8e442558891c66f315d4c0799fce3.jpg)

[](id:step11)
### 11. 观众端的镜像效果
通过调用 V2TXLivePusher 的 [setRenderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#adf4cd57c705a1022d6730fd722f8dab5) 可以改变摄像头的镜像方式，继而影响观众端观看到的镜像效果。之所以说是观众端的镜像效果，是因为当主播在使用前置摄像头直播时，默认情况下自己看到的画面会被 SDK 反转。
![](https://main.qcloudimg.com/raw/48cb3e6a39e968f3707fc956c062632a.png)

[](id:step12)
### 12. 横屏推流
大多数情况下，主播习惯以“竖屏持握”手机进行直播拍摄，观众端看到的也是竖屏分辨率的画面（例如 540 × 960 这样的分辨率）；有时主播也会“横屏持握”手机，这时观众端期望能看到是横屏分辨率的画面（例如 960 × 540 这样的分辨率），如下图所示： 
![](https://main.qcloudimg.com/raw/d42f32ad9deef5b3eba3ccb271fe05e8.png)

V2TXLivePusher 默认推出的是竖屏分辨率的视频画面，如果希望推出横屏分辨率的画面，可以修改 [setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a0b08436c1e14a8d7d9875fae59ac6d84) 接口的参数来设定观众端的画面横竖屏模式。
```objectivec
[_pusher setVideoQuality:videoQuality
             resolutionMode:isLandscape ? V2TXLiveVideoResolutionModeLandscape : V2TXLiveVideoResolutionModePortrait];
```

[](id:step13)
### 13. 音效设置
调用 V2TXLivePusher 中的 [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__ios.html) 获取 TXAudioEffectManager 实例可以实现背景混音、耳返、混响等音效功能。背景混音是指主播在直播时可以选取一首歌曲伴唱，歌曲会在主播的手机端播放出来，同时也会被混合到音视频流中被观众端听到，所以被称为“混音”。
![](https://main.qcloudimg.com/raw/269e653bc68c73c69feeb6418c513c25.jpg)

- 调用 TXAudioEffectManager 中的 `enableVoiceEarMonitor` 选项可以开启耳返功能，“耳返”指的是当主播带上耳机来唱歌时，耳机中要能实时反馈主播的声音。
- 调用 TXAudioEffectManager 中的 `setVoiceReverbType` 接口可以设置混响效果，例如 KTV、会堂、磁性、金属等，这些效果也会作用到观众端。
- 调用 TXAudioEffectManager 中的 `setVoiceChangerType` 接口可以设置变调效果，例如“萝莉音”，“大叔音”等，用来增加直播和观众互动的趣味性，这些效果也会作用到观众端。
![](https://main.qcloudimg.com/raw/a90a110e2950568b9d7cd6bef8e0893b.png)

>? 详细用法请参见 [TXAudioEffectManager API](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__ios.html)。

[](id:step14)
### 14. 设置 Logo 水印

设置 V2TXLivePusher 中的 [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#ad48aacbfad38b8f5389c159283fae859) 可以让 SDK 在推出的视频流中增加一个水印，水印位置位是由传入参数 `(x, y, scale)` 所决定。

- SDK 所要求的水印图片格式为 PNG 而不是 JPG，因为 PNG 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（将 JPG 图片修改后缀名是不起作用的）。
- `(x, y, scale)` 参数设置的是水印图片相对于推流分辨率的归一化坐标。假设推流分辨率为：540 × 960，该字段设置为：`（0.1，0.1，0.1）`，那么水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。

```objectivec
//设置视频水印
[_pusher setWatermark:[UIImage imageNamed:@"watermark"] x:0.03 y:0.015 scale:1];
```

[](id:step15)
### 15. 主播端弱网提醒
手机连接 Wi-Fi 网络不一定就非常好，如果 Wi-Fi 信号差或者出口带宽很有限，可能网速不如4G，如果主播在推流时遇到网络很差的情况，需要有一个友好的提示，提示主播应当切换网络。    
![](https://main.qcloudimg.com/raw/66441cb1356f87caeffb4a3102b938ea.png)  

通过 V2TXLivePusherObserver 里的 [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html#ga5506c2171438841ab3e99c80786c7ba0) 可以捕获 **V2TXLIVE_WARNING_NETWORK_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。此时就可以像上图一样在 UI 上弹出一个“弱网提示”。


<dx-codeblock>
::: objectiveC objectiveC
- (void)onWarning:(V2TXLiveCode)code
          message:(NSString *)msg
        extraInfo:(NSDictionary *)extraInfo {
    dispatch_async(dispatch_get_main_queue(), ^{
        if (code == V2TXLIVE_WARNING_NETWORK_BUSY) {
            [_notification displayNotificationWithMessage:
                @"您当前的网络环境不佳，请尽快更换网络保证正常直播" forDuration:5];
        }
    });
}
:::
</dx-codeblock>

[](id:step16)
### 16. 发送 SEI 消息
调用 V2TXLivePusher 中的 [sendSeiMessage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a106dc65c2616b80e193aad95876f7fe6) 接口可以发送 SEI 消息。所谓 SEI，是视频编码数据中规定的一种附加增强信息，平时一般不被使用，但我们可以在其中加入一些自定义消息，这些消息会被直播 CDN 转发到观众端。使用场景有：
- 答题直播：推流端将题目下发到观众端，可以做到“音-画-题”完美同步。
- 秀场直播：推流端将歌词下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
- 在线教育：推流端将激光笔和涂鸦操作下发到观众端，可以在播放端实时地划圈划线。

由于自定义消息是直接被塞入视频数据中的，所以不能太大（几个字节比较合适），一般常用于塞入自定义的时间戳等信息。
``` objectiveC
int payloadType = 5;
NSString* msg = @"test";
[_pusher sendSeiMessage:payloadType data:[msg dataUsingEncoding:NSUTF8StringEncoding]];
```
常规开源播放器或者网页播放器是不能解析 SEI 消息的，必须使用 LiteAVSDK 中自带的 V2TXLivePlayer 才能解析这些消息：
1. 设置：
```objectiveC
int payloadType = 5;
[_player enableReceiveSeiMessage:YES payloadType:payloadType];
```
2. 当 V2TXLivePlayer 所播放的视频流中有 SEI 消息时，会通过 V2TXLivePlayerObserver 中的 onReceiveSeiMessage 回调来接收该消息。


## 事件处理
### 事件监听
SDK 通过 [V2TXLivePusherObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusherObserver__ios.html) 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)。

### 错误通知 
SDK 发现部分严重问题，推流无法继续。

| 事件 ID                 |    数值  |  含义说明                    |
| :-------------------  |:-------- |  :------------------------ |
|V2TXLIVE_ERROR_FAILED                  | -1 | 暂未归类的通用错误  |
|V2TXLIVE_ERROR_INVALID_PARAMETER       | -2 | 调用 API 时，传入的参数不合法  |
|V2TXLIVE_ERROR_REFUSED                 | -3 | API 调用被拒绝  |
|V2TXLIVE_ERROR_NOT_SUPPORTED           | -4 | 当前 API 不支持调用  |
|V2TXLIVE_ERROR_INVALID_LICENSE         | -5 | license 不合法，调用失败  |
|V2TXLIVE_ERROR_REQUEST_TIMEOUT         | -6 | 请求服务器超时  |
|V2TXLIVE_ERROR_SERVER_PROCESS_FAILED   | -7 | 服务器无法处理您的请求  |

### 警告事件 
SDK 发现部分警告问题，但 WARNING 级别的事件都会触发一些尝试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复。

| 事件 ID                                       | 数值  | 含义说明                                                     |
| :-------------------------------------------- | :---- | :----------------------------------------------------------- |
| V2TXLIVE_WARNING_NETWORK_BUSY                 | 1101  | 网络状况不佳：上行带宽太小，上传数据受阻                     |
| V2TXLIVE_WARNING_VIDEO_BLOCK                  | 2105  | 视频回放期间出现滞后                                         |
| V2TXLIVE_WARNING_CAMERA_START_FAILED          | -1301 | 摄像头打开失败                                               |
| V2TXLIVE_WARNING_CAMERA_OCCUPIED              | -1316 | 摄像头正在被占用中，可尝试打开其他摄像头                     |
| V2TXLIVE_WARNING_CAMERA_NO_PERMISSION         | -1314 | 摄像头设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_MICROPHONE_START_FAILED      | -1302 | 麦克风打开失败                                               |
| V2TXLIVE_WARNING_MICROPHONE_OCCUPIED          | -1319 | 麦克风正在被占用中，例如移动设备正在通话时，打开麦克风会失败 |
| V2TXLIVE_WARNING_MICROPHONE_NO_PERMISSION     | -1317 | 麦克风设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_NOT_SUPPORTED | -1309 | 当前系统不支持屏幕分享                                       |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_START_FAILED  | -1308 | 开始录屏失败，如果在移动设备出现，可能是权限被用户拒绝了     |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_INTERRUPTED   | -7001 | 录屏被系统中断                                               |

