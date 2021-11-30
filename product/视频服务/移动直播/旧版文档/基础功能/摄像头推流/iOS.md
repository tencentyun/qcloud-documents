## 功能概述
摄像头推流，是指采集手机摄像头的画面以及麦克风的声音，进行编码之后再推送到直播云平台上。腾讯云 LiteAVSDK 通过 TXLivePusher 接口提供摄像头推流能力，如下是 LiteAVSDK 的简单版 Demo 中演示摄像头推流的相关操作界面：
![](https://main.qcloudimg.com/raw/39ee7f9e0e092d0adb9f1dff1077a482.png)

## 特别说明
- **不绑定腾讯云**
 SDK 不绑定腾讯云，如果要推流到非腾讯云地址，请在推流前设置 TXLivePushConfig 中的`enableNearestIP`为 false。但当您要推流的地址为腾讯云地址时，请务必在推流前将其设置为 YES，否则 SDK 针对腾讯云的协议优化将不能发挥作用。

- **x86 模拟器调试**
由于 SDK 大量使用 iOS 系统的音视频接口，这些接口在 Mac 上自带的 x86 仿真模拟器下往往不能工作。所以，如果条件允许，推荐您尽量使用真机调试。

## 示例代码

| 所属平台 | GitHub 地址 | 关键类 |
|:---------:|:--------:|:---------:|
| iOS | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/Demo/TXLiteAVDemo/LivePusherDemo/CameraPushDemo) | CameraPushViewController.m |
| Android | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo/livepusherdemo/src/main/java/com/tencent/liteav/demo/livepusher/camerapush) | CameraPushImpl.java |


## 功能对接

### 1. 下载 SDK 开发包
[下载](https://cloud.tencent.com/document/product/454/7873) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/454/7876) 将 SDK 嵌入您的 App 工程中。

[](id:step2)
### 2. 给 SDK 配置 License 授权
单击 [License 申请](https://console.cloud.tencent.com/live/license) 获取测试用的 License，您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。

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

### 3. 初始化 TXLivePush 组件
首先创建一个`TXLivePushConfig`对象。该对象可以指定一些高级配置参数，但一般情况下我们不建议您操作该对象，因为我们已经在其内部配置好了所有需要校调的参数。之后再创建一个`TXLivePush`对象，该对象负责完成推流的主要工作。

```objectivec   
 TXLivePushConfig *_config = [[TXLivePushConfig alloc] init];  // 一般情况下不需要修改默认 config   
 
 TXLivePush *_pusher = [[TXLivePush alloc] initWithConfig: _config]; // config 参数不能为空
```

[](id:step4)
### 4. 开启摄像头预览
调用 [TXLivePush](https://cloud.tencent.com/document/product/454/34755) 中的`startPreview`接口可以开启当前手机的摄像头预览。您需要为`startPreview` 接口提供一个用于显示视频画面的 view 对象。

```objectivec   
 //创建一个 view 对象，并将其嵌入到当前界面中
 UIView *_localView = [[UIView alloc] initWithFrame:self.view.bounds];
 [self.view insertSubview:_localView atIndex:0];
 _localView.center = self.view.center;
 
 //启动本地摄像头预览
 [_pusher startPreview:_localView];
```

> ! 如果要给 view 增加动画效果，需要修改 view 的 transform 属性而不是 frame 属性。
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _localView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
        }];
```

### 5. 启动和结束推流
如果已经通过`startPreview`接口启动了摄像头预览，就可以调用 TXLivePush 中的`startPush`接口开始推流。

```objectivec 
//启动推流
NSString* rtmpUrl = @"rtmp://test.com/live/xxxxxx";    //此处填写您的 rtmp 推流地址
[_pusher startPush:rtmpUrl];
```

推流结束后，可以调用 TXLivePush 中的`stopPush`接口结束推流。请注意，如果已经启动了摄像头预览，请在结束推流时将其关闭，否则会导致 SDK 的表现异常。
```objectivec
//结束推流
[_pusher stopPreview]; //如果已经启动了摄像头预览，请在结束推流时将其关闭。
[_pusher stopPush];
```

-  **获取可用的推流 URL**
开通直播服务后，可以使用【直播控制台】>【辅助工具】> [【地址生成器】](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 生成推流地址，详细信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
![](https://main.qcloudimg.com/raw/0ec9d83f340454c287d96f83eec3a3e4.png)
- **返回 -5 的原因**
如果 `startPush` 接口返回 -5，则代表您的 License 校验失败了，请检查 [第2步“给 SDK 配置   License 授权”](#step2) 中的工作是否有问题。


### 6. 纯音频推流
如果您的直播场景是纯音频直播，不需要视频画面，那么您可以不执行 [第4步](#step4) 中的操作，取而代之的是开启 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的`enablePureAudioPush`配置。

```objectivec
//通过修改 enablePureAudioPush 开关，开启纯音频推流
TXLivePushConfig *_config = [[TXLivePushConfig alloc] init];
_config.enablePureAudioPush = YES;   // YES 为启动纯音频推流，只有在调用 startPush 前设置才会生效。

TXLivePush *_pusher = [[TXLivePush alloc] initWithConfig: _config]; 
NSString* rtmpUrl = @"rtmp://test.com/live/xxxxxx";    
[_pusher startPush:rtmpUrl];
```
如果您启动纯音频推流，但是 rtmp、flv 、hls 格式的播放地址拉不到流，那是因为线路配置问题，请 [提工单](https://console.cloud.tencent.com/workorder/category) 联系我们帮忙修改配置。

### 7. 设定画面清晰度
调用 TXLivePush 中的`setVideoQuality`接口，可以设定观众端的画面清晰度。之所以说是观众端的画面清晰度，是因为主播看到的视频画面是未经编码压缩过的高清原画，不受设置的影响。而`setVideoQuality`通过设定视频编码器的编码质量，使观众端感受到画质的差异。详情请参考 [设定画面质量](https://cloud.tencent.com/document/product/454/9868#.E8.AE.BE.E5.AE.9A.E5.BB.BA.E8.AE.AE)。
![](https://main.qcloudimg.com/raw/8fc91a05e4e96c39a9fdcf45247fb988.png)

### 8. 美颜美白和红润特效
调用 TXLivePush 中的`setBeautyStyle`接口可以设置美颜效果，SDK 中提供了两种磨皮算法（beautyStyle）：

| 美颜风格 | 效果说明 | 
|---------|---------|
| BEAUTY_STYLE_SMOOTH | 光滑风格，算法更加注重皮肤的光滑程度，适合秀场直播类场景下使用。 |
| BEAUTY_STYLE_NATURE| 自然风格，算法更加注重保留皮肤细节，适合对真实性要求更高的主播。|

![](https://main.qcloudimg.com/raw/65a8ca85f71b41fa0cb3fa3f46eb8782.png)


```objectivec
//     beautyStyle     : 美颜算法，目前支持 自然 和 光滑 两种。
//     beautyLevel     : 磨皮级别，取值范围 0 - 9； 0 表示关闭 1 - 9值越大 效果越明显。
//     whitenessLevel  : 美白级别，取值范围 0 - 9； 0 表示关闭 1 - 9值越大 效果越明显。
//     ruddinessLevel  : 红润级别，取值范围 0 - 9； 0 表示关闭 1 - 9值越大 效果越明显。
(void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel 
          whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel;
```

### 9. 色彩滤镜效果
调用 TXLivePush 中的`setFilter`接口可以设置色彩滤镜效果。所谓色彩滤镜，是指一种将整个画面色调进行区域性调整的技术，例如将画面中的淡黄色区域淡化实现肤色亮白的效果，或者将整个画面的色彩调暖让视频的效果更加清新和温和。

调用 TXLivePush 中的`setSpecialRatio`接口可以设定滤镜的浓度，设置的浓度越高，滤镜效果也就越明显。

从手机 QQ 和 Now 直播的经验来看，单纯通过`setBeautyStyle`调整磨皮效果是不够的，只有将美颜效果和`setFilter`配合使用才能达到更加多变的美颜效果。所以，我们的设计师团队提供了17种默认的色彩滤镜，并将其默认打包在 [Demo](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/Demo) 中供您使用。
![](https://main.qcloudimg.com/raw/ef097190798fc104d8fec9cc40a13bf8.png)

<dx-codeblock>
::: objectivec objectivec
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:lookupFileName];

UIImage *image = [UIImage imageWithContentsOfFile:path];
[_pusher setFilter:image];
[_pusher setSpecialRatio:0.5f];
:::
</dx-codeblock>

### 10. 控制摄像头
TXLivePush 提供了一组 API 用户控制摄像头的行为：

| API 函数 | 功能说明 | 备注说明 |
|---------|---------|---------|
| switchCamera | 切换前后摄像头 | Mac 平台对应的函数为 `selectCamera`。 |
| toggleTorch | 打开或关闭闪光灯 | 仅在当前是后置摄像头时有效。|
| setZoom | 调整摄像头的焦距 | 焦距大小，取值范围：1 - 5，默认值建议设置为1即可。|
| setFocusPosition | 设置手动对焦位置 | 需要将 TXLivePushConfig 中的`touchFocus`选项设置为 YES 后才能使用。|

### 11. 观众端的镜像效果
调用 TXLivePush 中的`setMirror`接口可以设置观众端的镜像效果。之所以说是观众端的镜像效果，是因为当主播在使用前置摄像头直播时，自己看到的画面会被 SDK 默认反转，这时主播的体验跟自己照镜子时的体验是保持一致的。`setMirror`所影响的是观众端观看到的画面情况，如下图所示：
![](https://main.qcloudimg.com/raw/45ef7c9d0f1ecfc9bfab7735d92ec641.jpg)

### 12. 横屏推流
大多数情况下，主播习惯以“竖屏持握”手机进行直播拍摄，观众端看到的也是竖屏分辨率的画面（例如 540 × 960 这样的分辨率）；有时主播也会“横屏持握”手机，这时观众端期望能看到是横屏分辨率的画面（例如 960 × 540 这样的分辨率），如下图所示：
![](https://main.qcloudimg.com/raw/d42f32ad9deef5b3eba3ccb271fe05e8.png)

TXLivePush 默认推出的是竖屏分辨率的视频画面，如果希望推出横屏分辨率的画面，需要：
1. 设置 TXLivePushConfig 中的`homeOrientation`接口可以改变观众端看到的视频画面宽高比方向。
2. 调用 TXLivePush 中的`setRenderRotation`接口可以改变主播端的视频画面的渲染方向。

<dx-codeblock>
::: objectivec objectivec
// 如果希望竖屏推流（HOME 键在下），这是 SDK 的默认行为
_config.homeOrientation = HOME_ORIENTATION_DOWN;
[_pusher setConfig:_config];
[_pusher setRenderRotation:0];

// 如果希望横屏推流（HOME 键在右）
_config.homeOrientation = HOME_ORIENTATION_RIGHT;
[_pusher setConfig:_config];
[_pusher setRenderRotation:90];
:::
</dx-codeblock>

### 13. 隐私模式（垫片推流）

有时候主播的一些动作不希望被观众看到，但直播过程中又不能下播，那就可以考虑进入隐私模式。在隐私模式下，SDK 可以暂停采集主播手机的摄像头画面以及麦克风声音，并使用一张默认图片作为替代图像进行推流，也就是所谓的“垫片”。

该功能也常用于 App 被切到后台时：在 iOS 系统中，当 App 切到后台以后，操作系统不再允许该 App 继续采集摄像头画面。 此时就可以通过调用`pausePush`进入垫片状态。因为对于大多数直播 CDN 而言，如果超过一定时间（腾讯云目前为70s）不推视频数据，服务器就会断开当前的推流链接，所以在 App 切到后台后进入垫片模式是很有必要的。
![](https://main.qcloudimg.com/raw/bdc0e50690ff8d721d924d9570fc682f.jpg)
- **step1: 开启 XCode 中的 Background 模式**
![](https://main.qcloudimg.com/raw/8aeeee0ec6b5294cecf5dadd3e32f075.jpg)
- **step2: 设置 TXLivePushConfig 中的相关参数**
在开始推流前，使用 LivePushConfig 的`pauseImg`、`pauseFps`和`pauseTime`接口可以设置垫片推流的详细参数：
<dx-codeblock>
::: objectivec objectivec
    TXLivePushConfig *_config = [[TXLivePushConfig alloc] init];
    // 设置后台推流持续时长，单位秒，默认300秒。
    _config.pauseTime = 300;
    // 设置后台推流帧率，最小值为5，最大值为20，默认为10。
    _config.pauseFps = 10;
    // 设置后台推流的默认图片，默认为黑色背景, 图片最大尺寸不能超过1920*1920。
    _config.pauseImg = [UIImage imageNamed:@"pause_publish.jpg"];
        
    TXLivePush *_pusher = [[TXLivePush alloc] initWithConfig: _config]; 
:::
</dx-codeblock>
- **step3: 监听 App 的前后台切换事件**
如果 App 在切到后台后就被 iOS 系统彻底休眠掉，SDK 将无法继续推流，观众端就会看到主播画面进入黑屏或者冻屏状态。您可以使用下面的代码让 App 在切到后台后还可再跑几分钟。
<dx-codeblock>
::: objectivec objectivec
// 注册应用监听事件
 NSNotificationCenter *center = [NSNotificationCenter defaultCenter];
[center addObserver:self selector:@selector(willResignActive:) name:UIApplicationWillResignActiveNotification object:nil];
[center addObserver:self selector:@selector(didBecomeActive:) name:UIApplicationDidBecomeActiveNotification object:nil];


// 具体实现. _livePuser 为当前TXLivePush实例对象
#pragma mark - 前后台切换
- (void)willResignActive:(NSNotification *)notification {
    [_livePusher pausePush];
    _inBackground = YES;
}

- (void)didBecomeActive:(NSNotification *)notification {
    [_livePusher resumePush];
    _inBackground = NO;
    // 其他唤醒业务逻辑
}
:::
</dx-codeblock>

>! 请注意调用顺序：startPush => ( pausePush => resumePush ) => stopPush，错误的调用顺序会导致 SDK 表现异常，因此使用成员变量对执行顺序进行保护是很有必要的。

### 14. 背景混音
调用 TXLivePush 中的 BGM 相关接口可以实现背景混音功能。背景混音是指主播在直播时可以选取一首歌曲伴唱，歌曲会在主播的手机端播放出来，同时也会被混合到音视频流中被观众端听到，所以被称为“混音”。
![](https://main.qcloudimg.com/raw/0bbeb0cc7e6001a7c2fe68723b943540.png)

| 接口 | 说明 |
|-------|---------|
| playBGM | 通过 path 传入一首歌曲，[小直播 Demo](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.9B.B4.E6.92.AD-app) 中我们是从 iOS 的本地媒体库中获取音乐文件。 |
| stopBGM|停止播放背景音乐。|
| pauseBGM|暂停播放背景音乐。|
| resumeBGM|继续播放背景音乐。|
| setMicVolume|设置混音时麦克风的音量大小，推荐在 UI 上实现相应的一个滑动条，由主播自己设置。|
| setBGMVolume|设置混音时背景音乐的音量大小，推荐在 UI 上实现相应的一个滑动条，由主播自己设置。|
| setBgmPitch|调整背景音乐的音调高低。|

### 15. 耳返和混响
调用 TXLivePushConfig 中的`enableAudioPreview`选项可以开启耳返功能，“耳返”指的是当主播带上耳机来唱歌时，耳机中要能实时反馈主播的声音。
调用 TXLivePush 中的`setReverbType`接口可以设置混响效果，例如 KTV、会堂、磁性、金属等，这些效果也会作用到观众端。
调用 TXLivePush 中的`setVoiceChangerType`接口可以设置变调效果，例如“萝莉音”，“大叔音”等，用来增加直播和观众互动的趣味性，这些效果也会作用到观众端。
![](https://main.qcloudimg.com/raw/a90a110e2950568b9d7cd6bef8e0893b.png)

### 16. 设置 Logo 水印
设置 TXLivePushConfig 中的`watermark`可以让 SDK 在推出的视频流中增加一个水印，水印位置位是由`watermarkNormalization`选项决定。

- SDK 所要求的水印图片格式为 png 而不是 jpg，因为 png 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（将 jpg 图片在 Windows 下修改后缀名是不起作用的）。
- `watermarkNormalization`设置的是水印图片相对于推流分辨率的归一化坐标。假设推流分辨率为：540 × 960，该字段设置为：（0.1，0.1，0.1，0.0），那么水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。

```objectivec
//设置视频水印
_config.watermark = [UIImage imageNamed:@"watermark.png"];
_config.watermarkNormalization = CGRectMake(0.1f，0.1f，0.1f，0.0f);
```

### 17. 本地录制
调用 TXLivePush 中的`startRecord`接口可以启动本地录制，录制格式为 MP4，通过参数 `videoPath` 可以指定 MP4文件的存放路径。
调用 TXLivePush 中的`stopRecord`接口可以结束录制。如果您已经通过 `recordDelegate` 接口注册了监听器给 TXLivePusher，那么一旦录制结束，录制出来的文件会通过 `TXLiveRecordListener` （详见 TXLiveRecordTypeDef.h 头文件）回调通知出来。

```objectivec
-(int) startRecord:(NSString *)videoPath;
-(int) stopRecord;
```

>! 
>- 只有启动推流后才能开始录制，非推流状态下启动录制无效。
>- 出于安装包体积的考虑，仅专业版和企业版两个版本的 LiteAVSDK 支持该功能，直播精简版仅定义了接口但并未实现。
>- 录制过程中请勿动态切换分辨率和软硬编，会有很大概率导致生成的视频异常。
>- 使用 TXLivePusher 录制视频会一定程度地降低推流性能，云直播服务也提供了云端录制功能，具体使用方法请参考 [直播录制](https://cloud.tencent.com/document/product/267/32739)。

### 18. 主播端弱网提醒

手机连接 Wi-Fi 网络不一定就非常好，如果 Wi-Fi 信号差或者出口带宽很有限，可能网速不如4G，如果主播在推流时遇到网络很差的情况，需要有一个友好的提示，提示主播应当切换网络。
![](https://main.qcloudimg.com/raw/36b97591cedf5b80b3c85c7ac758f4f5.jpg)

通过 TXLivePushListener 里的 onPlayEvent 可以捕获 **PUSH_WARNING_NET_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。此时就可以像上图一样在 UI 上弹出一个“弱网提示”。

```objectiveC
- (void)onPushEvent:(int)evtID withParam:(NSDictionary *)param {
    dispatch_async(dispatch_get_main_queue(), ^{
        if (evtID == PUSH_ERR_NET_DISCONNECT || evtID == PUSH_ERR_INVALID_ADDRESS) {
            //...
        } else if (evtID == PUSH_WARNING_NET_BUSY) {
            [_notification displayNotificationWithMessage:
                @"您当前的网络环境不佳，请尽快更换网络保证正常直播" forDuration:5];
        }
        //...
    });
}
```

### 19. 发送 SEI 消息 
调用 TXLivePush 中的 `sendMessageEx`接口可以发送 SEI 消息。所谓 SEI，是视频编码数据中规定的一种附加增强信息，平时一般不被使用，但我们可以在其中加入一些自定义消息，这些消息会被直播 CDN 转发到观众端。使用场景有：

1. 答题直播：推流端将**题目**下发到观众端，可以做到“音-画-题”完美同步。
2. 秀场直播：推流端将**歌词**下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
3. 在线教育：推流端将**激光笔**和**涂鸦**操作下发到观众端，可以在播放端实时地划圈划线。

由于自定义消息是直接被塞入视频数据中的，所以不能太大（几个字节比较合适），一般常用于塞入自定义的时间戳等信息。

```objectiveC
NSString* msg = @"test";
[_pusher sendMessageEx:[msg dataUsingEncoding:NSUTF8StringEncoding]];
```

常规开源播放器或者网页播放器是不能解析 SEI 消息的，必须使用 LiteAVSDK 中自带的 TXLivePlayer 才能解析这些消息：
1. 设置 TXLivePlayConfig 中的`enableMessage`选项为 YES。
2. 当 TXLivePlayer 所播放的视频流中有 SEI 消息时，会通过 TXLivePlayListener 中的 onPlayEvent(PLAY_EVT_GET_MESSAGE) 通知给您。

## 事件处理
### 1. 事件监听
SDK 通过 [TXLivePushListener](https://cloud.tencent.com/document/product/454/34757) 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://cloud.tencent.com/document/product/454/17246) 。需要注意的是：**TXLivePushListener 只能监听得到 PUSH\_ 前缀的推流事件**。

### 2. 常规事件 
一次成功的推流都会通知的事件有（例如，收到1003就意味着摄像头的画面开始渲染）：

| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器。|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕，一切正常，准备开始推流。|
|PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | 推流器已成功打开摄像头（部分 Android 手机在此过程需要耗时1s - 2s）。| 

### 3. 错误通知 
SDK 发现部分严重问题，推流无法继续（例如，用户禁用了 App 的 Camera 权限导致摄像头打不开）：

| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败。|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败。|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败。|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败。|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率。|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率。|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连，且经三次重连无效，更多重试请自行重启推流。|

### 4. 警告事件 
SDK 发现部分警告问题，但 WARNING 级别的事件都会触发一些尝试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复。

- **WARNING_NET_BUSY**
主播网络差，如果您需要 UI 提示，这个 WARNING 相对比较有用。
- **WARNING_SERVER_DISCONNECT**
推流请求被后台拒绝，一般是由于推流地址里的 txSecret 计算错误，或者是推流地址被其他人占用（一个推流 URL 同时只能有一个端推流）。

| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻。|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连，已启动自动重连（自动重连连续失败超过三次会放弃）。|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码。|
|PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP - DNS 解析失败（会触发重试流程）。        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP 服务器连接失败（会触发重试流程）。  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP 服务器握手失败（会触发重试流程）。  |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP 服务器主动断开连接（会触发重试流程）。  |
