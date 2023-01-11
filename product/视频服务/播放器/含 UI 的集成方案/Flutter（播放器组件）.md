## SDK 下载

腾讯云视立方 Flutter 播放器 SDK 的地址是 [Player Flutter](https://github.com/LiteAVSDK/Player_Flutter/tree/main/Flutter)。

## 阅读对象

本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com/) 相关服务，未注册用户可注册账号 [免费试用](https://cloud.tencent.com/login)。

## 通过本文您可以学会

* 如何集成腾讯云视立方 Flutter播放器SDK
* 如何使用播放器组件进行点播播放

## 播放器组件简介

Flutter 播放器组件是基于 flutter 播放器 SDK 的扩展，播放器组件对于点播播放器，集成了更多的功能，包括全屏切换、清晰度切换、
进度条、播放控制、封面标题展示等常用功能，并且相对于点播播放器使用起来更加方便，如果想更加方便快捷的集成 flutter 视频播放能力，可以选择 flutter 播放器组件使用。
支持功能列表：

- 全屏播放
- 播放过程中屏幕旋转自适应
- 自定义视频封面
- 清晰度切换
- 声音和亮度调节
- 倍速播放
- 硬件加速开启\关闭
- 画中画（PIP）（支持 Android 和 iOS 平台）
- 雪碧图和关键帧打点信息

更多功能正在逐步开发中......

## 集成指引[](id:Guide)

1. 将项目中 `superplayer_widget` 目录复制到自己的 flutter 工程下
2. 在自己项目的配置文件 `pubspec.yaml` 下添加依赖
```yaml
superplayer_widget:
  # 该路径根据superplayer_widget存放路径改变
  path: ../superplayer_widget
```
3. 在需要使用到的页面，导入`superplayer_widget`的依赖包，如下所示：
```dart
import 'package:superplayer_widget/demo_superplayer_lib.dart';
```

## SDK 集成[](id:stepone)

### 步骤1：申请视频播放能力 License 和集成[](id:step1)

集成播放器前，需要 [注册腾讯云账户](https://cloud.tencent.com/login)，注册成功后申请视频播放能力 License， 然后通过下面方式集成，建议在应用启动时进行。
如果没有集成 license，播放过程中可能会出现异常。

```dart
String licenceURL = ""; // 获取到的 licence URL
String licenceKey = ""; // 获取到的 licence key
SuperPlayerPlugin.setGlobalLicense(licenceURL, licenceKey);
```

### 步骤2：创建 controller[](id:step2)

```dart
SuperPlayerController _controller = SuperPlayerController(context);
```

### 步骤3：配置播放器[](id:step3)

```dart
FTXVodPlayConfig config = FTXVodPlayConfig();
// 如果不配置preferredResolution，则在播放多码率视频的时候优先播放720 * 1280分辨率的码率
config.preferredResolution = 720 * 1280;
_controller.setPlayConfig(config);
```

FTXVodPlayConfig 中的详细配置可参考 flutter 点播播放器的配置播放器接口。

### 步骤4：设置监听事件[](id:step4)

```dart
_controller.onSimplePlayerEventBroadcast.listen((event) {
  String evtName = event["event"];
  if (evtName == SuperPlayerViewEvent.onStartFullScreenPlay) {
    setState(() {
      _isFullScreen = true;
    });
  } else if (evtName == SuperPlayerViewEvent.onStopFullScreenPlay) {
    setState(() {
      _isFullScreen = false;
    });
  } else {
    print(evtName);
  }
});
```

### 步骤5：添加布局[](id:step5)

```dart
Widget _getPlayArea() {
    return Container(
    height: 220,
    child: SuperPlayerView(_controller),
  );
}
```

### 步骤6：添加返回事件监听[](id:step6)

添加返回事件监听，确保用户在触发返回事件的时候，如果播放器处于全屏等状态，可以优先退出全屏，再次触发才会退出页面。
**如果全屏播放状态下需要直接退出页面，可以不实现该监听。**

```dart
  @override
Widget build(BuildContext context) {
  return WillPopScope(
      child: Container(
        decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage("images/ic_new_vod_bg.png"),
              fit: BoxFit.cover,
            )),
        child: Scaffold(
          backgroundColor: Colors.transparent,
          appBar: _isFullScreen
              ? null
              : AppBar(
            backgroundColor: Colors.transparent,
            title: const Text('SuperPlayer'),
          ),
          body: SafeArea(
            child: Builder(
              builder: (context) => getBody(),
            ),
          ),
        ),
      ),
      onWillPop: onWillPop);
}

Future<bool> onWillPop() async {
  return !_controller.onBackPress();
}
```

### 步骤7：启动播放[](id:step7)
<dx-tabs>
::: 通过 URL 方式
```dart
SuperPlayerModel model = SuperPlayerModel();
model.videoURL = "http://1400329073.vod2.myqcloud.com/d62d88a7vodtranscq1400329073/59c68fe75285890800381567412/adp.10.m3u8";
_controller.playWithModelNeedLicence(model);
```
:::
::: 通过 FileId 方式
```dart
SuperPlayerModel model = SuperPlayerModel();
model.appId = 1500005830;
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "8602268011437356984";
// psign 即播放器组件签名，签名介绍和生成方式参见链接：https://cloud.tencent.com/document/product/266/42436
model.videoId.pSign = "psignXXX" // 通过fileId播放必须填写
_controller.playWithModelNeedLicence(model);
```

在 [媒资管理](https://console.cloud.tencent.com/vod/media) 找到对应的视频文件。在文件名下方可以看到 FileId。

通过 FileId 方式播放，播放器会向后台请求真实的播放地址。如果此时网络异常或 FileId 不存在，则会收到 SuperPlayerViewEvent.onSuperPlayerError 事件。
:::
</dx-tabs>

### 步骤8：结束播放[](id:step8)

结束播放时**记得调用 controller 的销毁方法**，尤其是在下次 startVodPlay 之前，否则可能会产生大量的内存泄露以及闪屏问题。也确保在退出页面的时候，能够结束视频播放。
```dart
  @override
void dispose() {
  // must invoke when page exit.
  _controller.releasePlayer();
  super.dispose();
}
```

## 播放器组件接口列表[](id:sdkList)

### 1、视频播放

> ! 10.7版本开始，startPlay 变更为 startVodPlay，需要通过 {@link SuperPlayerPlugin#setGlobalLicense} 设置 Licence 后方可成功播放， 否则将播放失败（黑屏），全局仅设置一次即可。直播 Licence、短视频 Licence 和视频播放 Licence 均可使用，若您暂未获取上述 Licence ，可 [快速免费申请测试版 Licence](https://cloud.tencent.com/act/event/License) 以正常播放，正式版 License 需 [购买](https://cloud.tencent.com/document/product/881/74588#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license)。

- **说明**：开始播放视频.
- **接口**
```dart
_controller.playWithModelNeedLicence(model);
```
- **参数说明**
 - SuperPlayerModel
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>appId</td>
<td>int</td>
<td>应用 appId。FileId播放必填</td>
</tr>
<tr>
<td>videoURL</td>
<td>String</td>
<td>视频 URL，URL 播放必填</td>
</tr>
<tr>
<td>multiVideoURLs</td>
<td>List&lt;String&gt;</td>
<td>多码率 URL，多码率 URL 播放必填</td>
</tr>
<tr>
<td>defaultPlayIndex</td>
<td>int</td>
<td>默认播放码率序号，配合 multiVideoURLs 使用</td>
</tr>
<tr>
<td>videoId</td>
<td>SuperPlayerVideoId</td>
<td>fileId 存储对象，以下会有详细介绍</td>
</tr>
<tr>
<td>title</td>
<td>String</td>
<td>视频标题，用户可设置该字段来自定义标题，从而覆盖播放器内部从服务器请求的标题</td>
</tr>
<tr>
<td>coverUrl</td>
<td>String</td>
<td>从腾讯服务器拉取的封面图片,该值会在 SuperVodDataLoader 中被自动赋值</td>
</tr>
<tr>
<td>customeCoverUrl</td>
<td>String</td>
<td>自定义视频封面，该字段会被优先判断，可以通过定义该参数来实现自定义封面</td>
</tr>
<tr>
<td>duration</td>
<td>int</td>
<td>视频时长，单位 秒</td>
</tr>
<tr>
<td>videoDescription</td>
<td>String</td>
<td>视频描述</td>
</tr>
<tr>
<td>videoMoreDescription</td>
<td>String</td>
<td>视频详细描述</td>
</tr>
<tr>
<td>playAction</td>
<td>int</td>
<td>action 包括 PLAY_ACTION_AUTO_PLAY、PLAY_ACTION_MANUAL_PLAY 和 PLAY_ACTION_PRELOAD，以下对参数含义会有详细介绍</td>
</tr>
</tbody></table>

 - SuperPlayerVideoId
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>fileId</td>
<td>String</td>
<td>文件id。必填</td>
</tr>
<tr>
<td>psign</td>
<td>String</td>
<td>v4 开启防盗链必填</td>
</tr>
</tbody></table>
 - playAction
   - PLAY_ACTION_AUTO_PLAY：调用 playWithModel 之后，会自动开始播放视频。
   - PLAY_ACTION_MANUAL_PLAY：调用 playWithModel 之后，需要手动播放，并且播放器实质上并未加载视频，只会显示封面图，相对于 PLAY_ACTION_PRELOAD 没有任何视频播放资源消耗。
   - PLAY_ACTION_PRELOAD：调用 playWithModel 之后，会显示封面图，不会开始播放视频，不过播放器实质上已经加载了视频，相对于 PLAY_ACTION_MANUAL_PLAY，起播速度会更快。

### 2、暂停播放

- **说明**：暂停播放视频
- **接口**
```dart
_controller.pause();
```

### 3、继续播放

- **说明**：继续播放视频
- **接口**
```dart
_controller.resume();
```

### 4、重新开始播放

- **说明**：重新开始播放视频
- **接口**
```dart
_controller.reStart();
```

### 5、重置播放器

- **说明**：重置播放器状态，并停止播放视频
- **接口**
```dart
_controller.resetPlayer();
```

### 6、释放播放器

- **说明**：释放播放器资源，并停止播放，调用该方法之后，controller 将不可再复用
- **接口**
```dart
_controller.releasePlayer();
```

### 7、播放器返回事件

- **说明**：触发播放器返回事件，该方法主要用于全屏播放模式下的返回判断和处理，返回 true：执行了退出全屏等操作，消耗了返回事件，false：未消耗事件。
- **接口**
```dart
_controller.onBackPress();
```

### 8、切换清晰度

- **说明**：实时切换当前正在播放的视频的清晰度
- **接口**
```dart
_controller.switchStream(videoQuality);
```

- **参数说明**
videoQuality 在开始播放之后，一般可通过 _controller.currentQualiyList 和 _controller.currentQuality 来获取，前者为清晰度列表，后者为默认清晰度。**清晰度切换能力在播放器组件中已经集成，切换到全屏之后可点击右下角清晰度进行切换。**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>index</td>
<td>int</td>
<td>清晰度序号</td>
</tr>
<tr>
<td>bitrate</td>
<td>int</td>
<td>清晰度码率</td>
</tr>
<tr>
<td>width</td>
<td>int</td>
<td>该清晰度下视频的宽度</td>
</tr>
<tr>
<td>height</td>
<td>int</td>
<td>该清晰度下视频的高度</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>清晰度简称</td>
</tr>
<tr>
<td>title</td>
<td>String</td>
<td>用于显示的清晰度名称</td>
</tr>
<tr>
<td>URL</td>
<td>String</td>
<td>非必填，清晰度 URL，用于多码率下的清晰度 URL</td>
</tr>
</tbody></table>


### 9、调整进度（seek）

- **说明**：调整当前视频的播放进度
- **接口**
```dart
_controller.seek(progress);
```

- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>progress</td>
<td>double</td>
<td>需要调整到的时间，单位 秒</td>
</tr>
</tbody></table>

### 10、配置播放器组件

- **说明**：配置播放器组件
- **接口**
```dart
_controller.setPlayConfig(config);
```

- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>connectRetryCount</td>
<td>int</td>
<td>播放器重连次数，当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连，通过该值设置 SDK 重连次数</td>
</tr>
<tr>
<td>connectRetryInterval</td>
<td>int</td>
<td>播放器重连间隔，当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连，通过该值设置两次重连间隔时间</td>
</tr>
<tr>
<td>timeout</td>
<td>int</td>
<td>播放器连接超时时间</td>
</tr>
<tr>
<td>playerType</td>
<td>int</td>
<td>播放器类型 <br><li>0 点播 <br><li>1 直播 <br><li>2 直播回看</td>
</tr>
<tr>
<td>headers</td>
<td>Map</td>
<td>自定义 http headers</td>
</tr>
<tr>
<td>enableAccurateSeek</td>
<td>bool</td>
<td>是否精确 seek，默认 true</td>
</tr>
<tr>
<td>autoRotate</td>
<td>bool</td>
<td>播放 MP4 文件时，若设为 true 则根据文件中的旋转角度自动旋转。旋转角度可在 PLAY_EVT_CHANGE_ROTATION 事件中获得。默认 true</td>
</tr>
<tr>
<td>smoothSwitchBitrate</td>
<td>bool</td>
<td>平滑切换多码率 HLS，默认 false。<br><li>设为 false 时，可提高多码率地址打开速度; <br><li>设为 true，在 IDR 对齐时可平滑切换码率</td>
</tr>
<tr>
<td>cacheMp4ExtName</td>
<td>String</td>
<td>缓存 MP4 文件扩展名，默认 MP4</td>
</tr>
<tr>
<td>progressInterval</td>
<td>int</td>
<td>设置进度回调间隔,若不设置，SDK 默认间隔0.5秒回调一次，单位毫秒</td>
</tr>
<tr>
<td>maxBufferSize</td>
<td>int</td>
<td>最大播放缓冲大小，单位：MB。此设置会影响 playableDuration，设置越大，提前缓存的越多</td>
</tr>
<tr>
<td>maxPreloadSize</td>
<td>int</td>
<td>预加载最大缓冲大小，单位：MB</td>
</tr>
<tr>
<td>firstStartPlayBufferTime</td>
<td>int</td>
<td>首缓需要加载的数据时长，单位：ms，默认值为100ms</td>
</tr>
<tr>
<td>nextStartPlayBufferTime</td>
<td>int</td>
<td>缓冲时（缓冲数据不够引起的二次缓冲，或者 seek 引起的拖动缓冲）最少要缓存多长的数据才能结束缓冲，单位：ms，默认值为250ms</td>
</tr>
<tr>
<td>overlayKey</td>
<td>String</td>
<td>HLS 安全加固加解密 key</td>
</tr>
<tr>
<td>overlayIv</td>
<td>String</td>
<td>HLS 安全加固加解密 Iv</td>
</tr>
<tr>
<td>extInfoMap</td>
<td>Map</td>
<td>一些不必周知的特殊配置</td>
</tr>
<tr>
<td>enableRenderProcess</td>
<td>bool</td>
<td>是否允许加载后渲染后处理服务,默认开启，开启后超分插件如果存在，默认加载</td>
</tr>
<tr>
<td>preferredResolution</td>
<td>int</td>
<td>优先播放的分辨率，preferredResolution = width * height</td>
</tr>
</tbody></table>

### 11、开关硬解

- **说明**：开启或关闭硬解播放能力
- **接口**
```dart
_controller.enableHardwareDecode(enable);
```

### 12、获得播放状态

- **说明**：获得当前播放器的播放状态
- **接口**
```dart
SuperPlayerState superPlayerState = _controller.getPlayerState();
```

- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>INIT</td>
<td>SuperPlayerState</td>
<td>初始状态</td>
</tr>
<tr>
<td>PLAYING</td>
<td>SuperPlayerState</td>
<td>播放中</td>
</tr>
<tr>
<td>PAUSE</td>
<td>SuperPlayerState</td>
<td>暂停中</td>
</tr>
<tr>
<td>LOADING</td>
<td>SuperPlayerState</td>
<td>缓冲中</td>
</tr>
<tr>
<td>END</td>
<td>SuperPlayerState</td>
<td>播放结束</td>
</tr>
</tbody></table>

### 13、进入画中画模式

- **说明**：调动该方法之后，视频将会进入画中画模式，该模式只支持 Android 7.0以上，并且支持画中画模式的机型。
- **接口**
```dart
_controller.enterPictureInPictureMode(
backIcon: "images/ic_pip_play_replay.png",
playIcon: "images/ic_pip_play_normal.png",
pauseIcon: "images/ic_pip_play_pause.png",
forwardIcon: "images/ic_pip_play_forward.png");
```

- **参数说明**
该参数只适用于 Android 平台。
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>backIcon</td>
<td>String</td>
<td>回退按钮图标，由于 Android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标</td>
</tr>
<tr>
<td>playIcon</td>
<td>String</td>
<td>播放按钮图标，由于 Android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标</td>
</tr>
<tr>
<td>pauseIcon</td>
<td>String</td>
<td>暂停按钮图标，由于 Android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标</td>
</tr>
<tr>
<td>forwardIcon</td>
<td>String</td>
<td>快进按钮图标，由于 Android 平台限制，图标大小不得超过1M，可不传，不传则使用系统自带图标</td>
</tr>
</tbody></table>

## 事件通知

### 1、播放状态监听

- **说明**：监听视频播放的状态，封装后的状态变化。
- **代码**
```dart
_playController.onPlayStateBroadcast.listen((event) {
  SuperPlayerState state = event['event'];
});
```

- **事件说明**
事件通过枚举类 SuperPlayerState 来传递事件。
<table>
<thead>
<tr>
<th>状态</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>INIT</td>
<td>初始状态</td>
</tr>
<tr>
<td>PLAYING</td>
<td>播放中</td>
</tr>
<tr>
<td>PAUSE</td>
<td>暂停中</td>
</tr>
<tr>
<td>LOADING</td>
<td>缓冲中</td>
</tr>
<tr>
<td>END</td>
<td>播放结束</td>
</tr>
</tbody></table>

### 2、播放事件监听

- **说明**：监听播放器的操作事件。
- **代码**
```dart
_controller.onSimplePlayerEventBroadcast.listen((event) {
    String evtName = event["event"];
    if (evtName == SuperPlayerViewEvent.onStartFullScreenPlay) {
        setState(() {
        _ isFullScreen = true;
        });
    } else if (evtName == SuperPlayerViewEvent.onStopFullScreenPlay) {
        setState(() {
          _isFullScreen = false;
        });
    } else {
        print(evtName);
    }
});
```

- **事件说明**
<table>
<thead>
<tr>
<th>状态</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>onStartFullScreenPlay</td>
<td>进入全屏播放</td>
</tr>
<tr>
<td>onStopFullScreenPlay</td>
<td>退出全屏播放</td>
</tr>
<tr>
<td>onSuperPlayerDidStart</td>
<td>播放开始通知</td>
</tr>
<tr>
<td>onSuperPlayerDidEnd</td>
<td>播放结束通知</td>
</tr>
<tr>
<td>onSuperPlayerError</td>
<td>播放错误通知</td>
</tr>
<tr>
<td>onSuperPlayerBackAction</td>
<td>返回事件</td>
</tr>
</tbody></table>

## 高级功能

### 通过 fileId 提前请求视频数据

可通过 SuperVodDataLoader 提前将视频数据请求下来，提高起播速度。
**代码示例**

```dart
SuperPlayerModel model = SuperPlayerModel();
model.appId = 1500005830;
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "8602268011437356984";
model.title = "云点播";
SuperVodDataLoader loader = SuperVodDataLoader();
// model中的必要参数会在SuperVodDataLoader中直接赋值
loader.getVideoData(model, (resultModel) {
  _controller.playWithModelNeedLicence(resultModel);
})
```


### 画中画模式的使用
1. **平台配置**
	- **Android  平台配置**：在自己项目 android 包下，找到 build.gradle，确保 compileSdkVersion 和 targetSdkVersion 的版本为31或以上
	- **iOS 平台配置**：在自己项目的 target 下选择 Signing & Capabilities 添加 Background Modes，勾选 Audio、AirPlay、and Picture in Picture。
2. **复制 superPlayer 示例代码**
将 github 项目中 superplayer_widget 导入到自己的 lib 目录下，仿照示例代码中的 demo_superplayer.dart 集成播放器组件。
然后就可以在播放器组件的播放界面右边中间看到画中画模式按钮，单击即可进入画中画模式。
3. **监听画中画模式生命周期**
使用 SuperPlayerPlugin 中的 onExtraEventBroadcast 可监听到画中画模式的生命周期，示例代码如下：
```dart
SuperPlayerPlugin.instance.onExtraEventBroadcast.listen((event) {
  int eventCode = event["event"];
  if (eventCode == TXVodPlayEvent.EVENT_PIP_MODE_ALREADY_EXIT) {
    // exit pip mode
  } else if (eventCode == TXVodPlayEvent.EVENT_PIP_MODE_REQUEST_START) {
    // enter pip mode
  } else if (eventCode == TXVodPlayEvent.EVENT_PIP_MODE_ALREADY_ENTER) {
    // already enter pip mode
  } else if (eventCode == TXVodPlayEvent.EVENT_IOS_PIP_MODE_WILL_EXIT) {
    // will exit pip mode
  } else if (eventCode == TXVodPlayEvent.EVENT_IOS_PIP_MODE_RESTORE_UI) {
    // restore UI only support iOS
  } 
});
```
4. **画中画模式进入错误码**
进入画中画模式失败的时候，除了有 log 提示以外，还会有 toast 提示，可在 superplayer_widget.dart 的 \_onEnterPipMode 方法内修改错误情况处理。错误码含义如下：
<table>
<thead>
<tr>
<th>参数名</th>
<th>值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>NO_ERROR</td>
<td>0</td>
<td>启动成功，没有错误</td>
</tr>
<tr>
<td>ERROR_PIP_LOWER_VERSION</td>
<td>-101</td>
<td>android 版本过低，不支持画中画模式</td>
</tr>
<tr>
<td>ERROR_PIP_DENIED_PERMISSION</td>
<td>-102</td>
<td>画中画模式权限未打开，或者当前设备不支持画中画</td>
</tr>
<tr>
<td>ERROR_PIP_ACTIVITY_DESTROYED</td>
<td>-103</td>
<td>当前界面已经销毁</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_DEVICE_NOT_SUPPORT</td>
<td>-104</td>
<td>设备或系统版本不支持（iPad iOS9+ 才支持 PIP）</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_PLAYER_NOT_SUPPORT</td>
<td>-105</td>
<td>播放器不支持</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_VIDEO_NOT_SUPPORT</td>
<td>-106</td>
<td>视频不支持</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_IS_NOT_POSSIBLE</td>
<td>-107</td>
<td>PIP 控制器不可用</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_FROM_SYSTEM</td>
<td>-108</td>
<td>PIP 控制器报错</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_PLAYER_NOT_EXIST</td>
<td>-109</td>
<td>播放器对象不存在</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_IS_RUNNING</td>
<td>-110</td>
<td>PIP 功能已经运行</td>
</tr>
<tr>
<td>ERROR_IOS_PIP_NOT_RUNNING</td>
<td>-111</td>
<td>PIP 功能没有启动</td>
</tr>
</tbody></table>
5. **判断当前设备是否支持画中画**
使用 SuperPlayerPlugin 中的 isDeviceSupportPip 可判断当前是否能够开启画中画，代码示例如下：
```dart
int result = await SuperPlayerPlugin.isDeviceSupportPip();
if(result == TXVodPlayEvent.NO_ERROR) {
  // pip support
}
```
result 的返回结果的含义和画中画模式错误码一致。
6. **使用画中画控制器管理画中画**
画中画控制器 TXPipController 为 superplayer_widget 中封装的画中画工具，**必须与 SuperPlayerView 搭配起来使用**，进入画中画会自动关闭当前界面，并回调提前设置的监听方法，在回调的方法中可以保存播放器当前界面的必要参数。画中画还原之后，会重新将之前的界面 push 回来，并传递之前保存的参数。
使用该控制器的时候，画中画和播放器只能存在一个实例，当重新进入播放器界面的时候，画中画会自动关闭。
	1. 在自己的项目的入口处，如 main.dart，调用 TXPipController 设置画中画控制跳转，跳转的页面为用于进入画中画的播放器页面，
   可根据自身项目情况设置不同的界面，代码实例如下：
```dart
TXPipController.instance.setNavigatorHandle((params) {
  navigatorKey.currentState?.push(MaterialPageRoute(builder: (_) => DemoSuperPlayer(initParams: params)));
});
```
	2. 设置画中画的播放页面监听，需要实现`TXPipPlayerRestorePage`方法，设置之后，当即将进入画中画时，控制器会回调`void onNeedSavePipPageState(Map<String, dynamic> params)`方法，此时可以在 params 中存入当前页面需要的参数。
```dart
TXPipController.instance.setPipPlayerPage(this);
```
	3. 随后，当用户单击 SuperPlayerView 上的进入画中画按钮的时候，会调用`SuperPlayerView`的`_onEnterPipMode`内部方法进入画中画，也可以自行调用`SuperPlayerController`的`enterPictureInPictureMode`方法进入。
