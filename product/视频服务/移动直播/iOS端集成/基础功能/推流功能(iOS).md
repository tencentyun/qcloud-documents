## 基础知识
**推流** 是指将音视频数据采集编码之后，推送到您指定的视频云平台上，这里涉及大量的音视频基础知识，而且需要长时间的打磨和优化才能达到符合预期的效果。

腾讯视频云 SDK 主要帮您解决在智能手机上的推流问题，它的接口非常简单易用，只需要一个推流URL就能驱动：
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## 特别说明
- **<font color='red'>不绑定腾讯云</font>**
> SDK 不绑定腾讯云，如果要推流到非腾讯云地址，请在推流前设置 TXLivePushConfig 中的 enableNearestIP 设置为 NO。但如果您要推流的地址为腾讯云地址，请务必在推流前将其设置为 YES，否则推流质量可能会因为运营商 DNS 不准确而受到影响。

- **x86 模拟器调试**
> 由于 SDK 大量使用iOS系统的高级特性，我们不能保证所有特性在x86环境的模拟器下都能正常运行，而且音视频是性能敏感的功能，模拟器下的表现跟真机会有很大的不同。所以，如果条件允许，推荐您尽量使用真机调试。

## 准备工作

- **获取开发包**
[下载](https://cloud.tencent.com/document/product/454/7873) SDK 开发包，并按照[工程配置](https://cloud.tencent.com/document/product/454/7876)指引将 SDK 嵌入您的 APP 开发工程。

- **获取测试URL**
[开通](https://console.cloud.tencent.com/live)直播服务后，可以使用 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 生成推流地址，详细信息可以参考 [获得推流播放URL](https://cloud.tencent.com/document/product/454/7915)。
![](https://mc.qcloudimg.com/static/img/64342b926e05da462a54b8ce4f8c526f/image.png)

## 代码对接
>本篇攻略主要是面向**摄像头直播**的解决方案，该方案主要用于美女秀场直播、活动直播等场景，游戏直播请参考本目录下的同级文档。

### step 1: 创建Pusher对象
先创建一个 **LivePush** 对象，我们后面主要用它来完成推流工作。

不过在创建 LivePush 对象之前，还需要您指定一个**LivePushConfig**对象，该对象的用途是决定 LivePush 推流时各个环节的配置参数，比如推流用多大的分辨率、每秒钟要多少帧画面（FPS）以及Gop（表示多少秒一个I帧）等等。

LivePushConfig 在alloc之后便已经装配了一些我们反复调过的参数，如果您不需要自己定制这些配置，简单的alloc出来并塞给LivePush对象就可以了。如果您有相关领域的经验基础，需要对这些默认配置进行调整，可以阅读**进阶篇**中的内容。

```objectivec   
// 创建 LivePushConfig 对象，该对象默认初始化为基础配置
 TXLivePushConfig* _config = [[TXLivePushConfig alloc] init];    
 //在 _config中您可以对推流的参数（如：美白，硬件加速，前后置摄像头等）做一些初始化操作，需要注意 _config不能为nil  
 _txLivePush = [[TXLivePush alloc] initWithConfig: _config];
```

### step 2: 渲染View
接下来我们要给摄像头的影像画面找个地方来显示，iOS系统中使用view作为基本的界面渲染单位，所以您只需要准备一个view传给 LivePush 对象的 **startPreview** 接口函数就可以了。

- **推荐的布局！**
> 实际上，SDK 的内部并不是直接把画面渲染在您提供的view上，而是在这个view之上创建一个用于OpenGL渲染的子视图（subView），但是，这个渲染用的subView的大小会跟随您提供的view大小变化而自动调整。
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> 不过即如此，如果您想要在渲染画面之上实现弹幕、献花之类的UI控件，我们也推荐您”另起炉灶“（再创建一个平级的view），这样可以避免很多前后画面覆盖的问题。

- **如何做动画？**
> 针对view做动画是比较自由的，不过请注意此处动画所修改的目标属性应该是<font color='red'>transform</font>属性而不是frame属性。
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
        }];
```

### step 3: 启动推流
经过 step1 和 step2 的准备之后，用下面这段代码就可以启动推流了： 

```objectivec 
NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";    
[_txLivePush startPreview:_myView];  //_myView 就是step2中需要您指定的view    
[_txLivePush startPush:rtmpUrl];
```

- **startPush** 的作用是告诉 SDK 音视频流要推到哪个推流URL上去。
- **startPreview** 的参数就是step2中需要您指定的view，startPreview 的作用就是将界面view控件和LivePush对象关联起来，从而能够将手机摄像头采集到的画面渲染到屏幕上。

### step 3+: 纯音频推流
如果你的直播场景是声音直播，那么需要更新下推流的配置信息。前面 step1 和 step2 准备步骤不变，使用以下代码设置纯音频推流并启动推流。

```objectivec
// 只有在推流启动前设置启动纯音频推流才会生效，推流过程中设置不会生效。
txLivePush.config.enablePureAudioPush = YES;   // YES 为启动纯音频推流，而默认值是 NO；
[_txLivePublisher setConfig:_config];          // 重新设置 config

NSString* rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";      
[_txLivePush startPush:rtmpUrl];
```
如果你启动纯音频推流，但是 rtmp、flv 、hls 格式的播放地址拉不到流，那是因为线路配置问题，请提工单联系我们帮忙修改配置。

### step 4: 设定清晰度

如果您是第一次接触音视频，<font color='red'>**不推荐**</font> 您自行设置分辨率、码率等视频参数，参数配置不当可能影响最终的画质表现，推荐您使用 TXLivePusher::setVideoQuality 接口的可以设定推流的画面清晰度：

![](https://main.qcloudimg.com/raw/6e66be90ff14bb8f0603c70668a27ec8.png)

- **推荐参数设置**

| 应用场景 | quality |  adjustBitrate | adjustResolution |
|:-------:|:-------:|:-------:|
| 秀场直播 | VIDEO_QUALITY_HIGH_DEFINITION 或 <br> VIDEO_QUALITY_SUPER_DEFINITION  | NO | NO |
| 手游直播 | VIDEO_QUALITY_SUPER_DEFINITION  | YES | YES |
| 连麦（主画面） | VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER | YES | YES | 
| 连麦（小画面） | VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER  | NO | NO |
| 视频通话| VIDEO_QUALITY_REALTIEM_VIDEOCHAT | YES | YES | 

- **内部数据指标**

| quality | adjustBitrate | adjustResolution | 码率范围 | 分辨率范围 | 
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| STANDARD | YES | YES | 300~800kbps| 270x480 ~ 360x640| 
| STANDARD | YES | NO |300~800kbps|360x640| 
| STANDARD | NO | NO | 800kbps | 360x640| 
| HIGH | YES | YES |600~1500kbps| 360x640~540x960| 
| HIGH | YES | NO |600~1500kbps| 540x960| 
| HIGH | NO | NO |1200kbps| 540x960| 
| SUPER | YES | YES | 600~1800kbps|360x640~720x1280|
| SUPER | YES | NO |600~1800kbps|720x1280|
| SUPER | NO | NO |1800kbps|720x1280|
| MAIN_PUBLISHER | YES | YES |600~1500kbps| 360x640~540x960| 
| SUB_PUBLISHER | NO | NO |350kbps| 320x480| 
| VIDEOCHAT | YES | YES | 200~800kbps| 190x320~360x640| 

### step 5: 美颜滤镜

![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
- **美颜**
setBeautyStyle 接口可以设置美颜风格、磨皮程度、美白级别和红润级别，配合 540 * 960 分辨率（setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION），可以达到最佳的画质效果：
```objectivec
//     beautyStyle     : 磨皮风格，目前支持 自然 和 光滑 两种。
//     beautyLevel     : 磨皮级别，取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
//     whitenessLevel  : 美白级别，取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
//     ruddinessLevel  : 红润级别，取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
(void)setBeautyStyle:(int)beautyStyle beautyLevel:(float)beautyLevel 
          whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel;
```

- **滤镜**
setFilter 接口可以设置滤镜效果，滤镜本身是一张直方图文件，我们设计师团队提供了八种素材，默认打包在了Demo中，您可以随意使用，不用担心版权问题。

 setSpecialRatio 接口则可以设置滤镜的程度，从0到1，越大滤镜效果越明显，默认取值0.5。
```objectivec
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
if (path != nil && index != FilterType_None && _txLivePublisher != nil) {
        path = [path stringByAppendingPathComponent:lookupFileName];
        UIImage *image = [UIImage imageWithContentsOfFile:path];
        [_txLivePublisher setFilter:image];
} 
```
> 如果要自定义滤镜，一定要用 PNG 格式的图片，<font color='red'>不要用 JPG，不要用 JPG，不要用 JPG...</font>


### step 6: 控制摄像头
- **切换前置或后置摄像头** 
默认是使用**前置**摄像头（可以通过修改 LivePushConfig 的配置项 frontCamera 来修改这个默认值），调用一次switchCamera 切换一次，注意切换摄像头前必须保证 LivePushConfig 和 LivePush 对象都已经初始化。  
  
```objectivec
// 默认是前置摄像头，可以通过修改 LivePushConfig 的配置项 frontCamera 来修改这个默认值   
[_txLivePush switchCamera];
```

- **打开或关闭闪光灯** 
只有后置摄像头才可以打开闪光灯（您可以通过"TXLivePush.h"里面的frontCamera成员来确认当前摄像头是前置还是后置）

```objectivec
if(!frontCamera) {
    BOOL bEnable = YES;
    //bEnable为YES，打开闪光灯; bEnable为NO，关闭闪光灯
    BOOL result = [_txLivePush toggleTorch: bEnable];
    //result为YES，打开成功;result为NO，打开失败
}
```

- **自定义手动对焦**
SDK 的iOS版本内部有默认的手动对焦逻辑，虽然功能没什么问题，但是经常由于屏幕的触控事件被抢占而无法发挥作用。同时，界面排布的自由我们原则上绝不能干预。
我们在新版本的 TXLivePush 里增加了一个 setFocusPosition 函数接口，您可以自己根据手指触控位置进行手动对焦。

```objectivec
// 如果客户调用这个接口，SDK内部触发对焦的逻辑将会停止，避免重复触发对焦逻辑
- (void)setFocusPosition:(CGPoint)touchPoint;
```

### step 7: 设置Logo水印
最近相关政策规定，直播的视频必须要打上水印，所以这个之前看起来并不是特别起眼的功能现在要重点说一下：
腾讯视频云目前支持两种水印设置方式：一种是在推流SDK进行设置，原理是在SDK内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印Logo。

这里我们特别建议您使用<font color='red'>SDK添加水印</font>，因为在云端打水印有三个明显的问题：
 （1）这是一种很耗云端机器的服务，而且不是免费的，会拉高您的费用成本；
 （2）在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 （3）在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

SDK所要求的水印图片格式为png，因为png这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。（您可千万别把jpg图片在windows下改个后缀名就塞进去了，专业的png图标都是需要由专业的美工设计师处理的）

```objectivec
//设置视频水印
_config.watermark = [UIImage imageNamed:@"watermark.png"];
_config.watermarkPos = (CGPoint){10, 10};
```

### step 8: 本地录制
使用 startRecord 接口可以启动本地录制，录制格式为 MP4，通过 videoPath 可以指定 MP4 文件的存放路径。
- 录制过程中请勿动态切换分辨率和软硬编，可能导致生成的视频异常
- 如果是云端录制，只需要在推流 URL 后面拼接 &record=mp4 即可，详情请参考[云端录制](https://cloud.tencent.com/document/product/454/7917)。
- stopRecord 调用之后，录制出来的文件会通过 TXLiveRecordListener 通知出来。

```objectivec
-(int) startRecord:(NSString *)videoPath;
-(int) stopRecord;
```

### step 9: 后台推流
常规模式下，App一旦切到后台，摄像头的采集能力就会被 iOS 暂时停止掉，这就意味着 SDK 不能再继续采集并编码出音视频数据。如果我们什么都不做，那么故事将按照如下的剧本发展下去：
+ 阶段一（切后台开始 -> 之后的10秒内）- CDN因为没有数据所以无法向观众提供视频流，观众看到画面卡主。
+ 阶段二（10秒 -> 70秒内）- 观众端的播放器因为持续收不到直播流而直接推出，直播间已经人去楼空。
+ 阶段三（70秒以后）- 推流的 RTMP 链路被服务器直接断掉，主播需要重新开启直播才能继续。

主播可能只是短暂接个紧急电话而已，但上述的交互体验显然会让观众全部离开直播间，怎么优化呢？
从 **SDK 1.6.1** 开始，我们引入了一种解决方案，如下是从观众端的视角看去，该方案可以达到的效果： 
![](https://mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

- **9.1) 调整XCode设置**
![](https://main.qcloudimg.com/raw/64e1d95634ebed1de71ad3b84492f37e.jpg)

- **9.2) 设置pauseImg**
在开始推流前，使用 LivePushConfig 的 pauseImg 接口设置一张等待图片，图片含义推荐为“主播暂时离开一下下，稍后回来”。

```objectivec
    // 300 为后台播放暂停图片的最长持续时间,单位是秒
    _config.pauseTime = 300;
    // 10 为后台播放暂停图片的帧率,最小值为5,最大值为20
    _config.pauseFps = 10;
    // 设置推流暂停时,后台播放的暂停图片, 图片最大尺寸不能超过1920*1920.
    _config.pauseImg = [UIImage imageNamed:@"pause_publish.jpg"];
    [_txLivePublisher setConfig:_config];
```

- **9.3) 设置App后台（短暂）运行**
App 如果切后台后就彻底被休眠掉，那么 SDK 也就无法继续推流了，观众端就会看到直播间进入黑屏或者冻屏状态。我们可以使用下面的代码让 App 在切到后台后还可再跑几分钟，至少足够主播接听一个短暂的私人电话。

```objectivec
//先注册后退消息通知
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleEnterBackground:) 
    name:UIApplicationDidEnterBackgroundNotification object:nil];

//收到通知后，调用beginBackgroundTaskWithExpirationHandler
-(void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
}
```
- **9.4) 切后台处理**
在上一步的 handleEnterBackground 里，调用 TXLivePush 的 pausePush 接口函数，之后 SDK 虽然采集不到摄像头的画面了，但可以用您刚才设置的 pauseImg 持续推流。

```
//切后台处理： 在上一步的基础上补一句
- (void)handleEnterBackground:(NSNotification *)notification
{
    [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
    }];
    [_txLivePush pausePush];
}
```

- **9.5) 切前台处理**
 等待 App 切回前台之后 （在 handleEnterForeground 里），调用 TXLivePush 的 resumePush 接口函数，SDK 会恢复对摄像头画面的采集。要注意的是：由于 pausePush 和 resumePush 跟 SDK 内部状态息息相关，必须要 <font color='red'> 配对使用 </font>，否则会引入很多不必要的 BUG。
 
```objectivec
//切前台处理
- (void)handleEnterForeground:(NSNotification *)notification
{
    [_txLivePush resumePush];
}
```

### step 10: 卡顿预警提示

- 如果主播网络质量不好，我们应该怎么做？ 
- 主动降低清晰度来确保流畅性？ 这样观众端的感受就是模糊和马赛克。
- 主动丢掉一部分视频帧，以确保画面还能持续有一定的清晰度？这样观众端的感受就是持续卡顿。
- 以上都是我们不想要的？那怎么办？
- “既然马儿跑得快，又让马儿不吃草。”  我们都知道，这是不可能的事情。

通过 TXLivePushListener 里的 onPlayEvent 可以捕获 **PUSH_WARNING_NET_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。

此时可以提示主播 **“您当前的网络状况不佳，推荐您离 WiFi 近一点，尽量不要让 WiFi 穿墙”**。

### step 11: 横屏推流
大多数情况下，用户习惯以“竖屏持握”进行直播拍摄，观看端看到的也是竖屏样式；有时候用户在直播的时候需要更广的视角，则拍摄的时候需要“横屏持握”，这个时候其实是期望观看端能看到横屏画面，就需要做横屏推流，下面两幅示意图分别描述了横竖屏持握进行横竖屏推流在观众端看到的效果。
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
> <font color='red'>**注意：**</font> 横屏推流和竖屏推流，观众端看到的图像的宽高比是不同的，竖屏9:16，横屏16：9。

要实现横屏推流，需要在两处进行设置：
- **调整观众端表现**
通过对 LivePushConfig 中的 **homeOrientation** 设置项进行配置，它控制的是观众端看到的视频宽高比是 **16:9** 还是 **6:19**，调整后的结果可以用播放器查看以确认是否符合预期。

- **调整主播端表现**
接下来就看主播本地渲染是否正常，这里可以通过 TXLivePush 中的 setRenderRotation 接口来设置主播看到的画面的旋转方向。此接口提供了** 0，90，180，270** 四个参数供设置旋转角度。

### step 12: 背景混音
SDK 1.6.1 开始支持背景混音，支持主播带耳机和不带耳机两种场景，您可以通过 TXLivePush 中的如下这组接口实现背景混音功能：

| 接口 | 说明 |
|:-------:|---------|
| playBGM | 通过path传入一首歌曲，[小直播Demo](https://cloud.tencent.com/doc/api/258/6164)中我们是从iOS的本地媒体库中获取音乐文件 |
| stopBGM|停止播放背景音乐|
| pauseBGM|暂停播放背景音乐|
| resumeBGM|继续播放背景音乐|
| setMicVolume|设置混音时麦克风的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|
| setBGMVolume|设置混音时背景音乐的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|

### step 13: 耳返&混响
- **耳返**
指的是当主播带上耳机来唱歌时，耳机中要能实时反馈主播的声音，这是由于主播自己的声音是通过头部骨骼（固体）传入耳朵，而观众听到声音最终是通过空气介质传入耳朵，这两种方式听的声音是有很大差异的，因此主播有需求直接听到观众端的效果。
![](//mc.qcloudimg.com/static/img/fca1094c93126ad5b61d962ec22ad0d5/image.png)

 在 TXLivePushConfig中 enableAudioPreview 接口可以打开耳返（如果是连麦，推荐大主播开，小主播就不要开了，实时音视频通话时开耳返会很奇怪。）

- **混响**
指的是耳返的时候，声音要加入一些特效，比如KTV、会堂、磁性、金属 等等，这个效果最终也会作用到观众端，让主播的歌声更加有味道。通过 TXLivePush 的成员函数 setReverbType (1.9.2 开始支持) 可以设置混响特效。

 目前可以支持的混响特效有：KTV、小房间、大会堂、低沉、洪亮、金属声 以及 磁性 等 6 种。

### step 14: 结束推流
结束推流很简单，不过要做好清理工作，因为用于推流的 TXLivePush 对象同一时刻只能有一个在运行，所以清理工作不当会导致下次直播遭受不良的影响。
```objectivec
//结束推流，注意做好清理工作
- (void)stopRtmpPublish {
    [_txLivePush stopPreview];
    [_txLivePush stopPush];
    _txLivePush.delegate = nil;
}
```

<h2 id="Message"> 发送消息 </h2>
此功能可以在推流端将一些自定义 message 随着音视频线路直接下发到观众端，适用场景例如：
（1）冲顶大会：推流端将**题目**下发到观众端，可以做到“音-画-题”完美同步。
（2）秀场直播：推流端将**歌词**下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
（3）在线教育：推流端将**激光笔**和**涂鸦**操作下发到观众端，可以在播放端实时地划圈划线。

```objectiveC
[_answerPusher sendMessage:[mesg dataUsingEncoding:NSUTF8StringEncoding]];
```

> 使用 TXLivePlayer 的 onPlayEvent （PLAY_EVT_GET_MESSAGE） 可以用来接收消息。

## 事件处理
### 1. 事件监听
SDK 通过 TXLive<font color='red'>Push</font>Listener 代理来监听推流相关的事件，注意 TXLive<font color='red'>Push</font>Listener 只能监听得到 <font color='red'>PUSH_</font> 前缀的推流事件。

### 2. 常规事件 
一次成功的推流都会通知的事件，比如收到1003就意味着摄像头的画面会开始渲染了

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕,一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | 推流器已成功打开摄像头（Android部分手机这个过程需要1-2秒）| 

### 3. 错误通知 
SDK发现了一些严重问题，推流无法继续了，比如用户禁用了APP的Camera权限导致摄像头打不开。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流|

### 4. 警告事件 
SDK发现了一些问题，但这并不意味着无可救药，很多 WARNING 都会触发一些重试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复，所以，千万不要“小题大做”哦。

- **WARNING_NET_BUSY**
主播网络不给力，如果您需要UI提示，这个 warning 相对比较有用（step10）。

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
推流请求被后台拒绝了，出现这个问题一般是由于推流地址里的 txSecret 计算错了，或者是推流地址被其他人占用了（一个推流URL同时只能有一个端推流）。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码|
|PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP -DNS解析失败（会触发重试流程）        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP服务器连接失败（会触发重试流程）  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP服务器握手失败（会触发重试流程）  |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP服务器主动断开连接（会触发重试流程）  |
