## 功能介绍

超级播放器是基于`TXVodPlayer`和`TXLivePlayer`实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕、直播时移等功能于一体的解决方案，**且完全开源**。帮助您在短时间内，打造一个媲美市面上各种流行视频App的播放体验。

![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## 接入准备

1. 下载 SDK + Demo 开发包，下载地址为([Android](https://cloud.tencent.com/document/product/454/7873#Android)).

2. 播放器的 UI 部分代码开源，开源代码位于 `app/src/main/java/com/tencent/liteav/demo/play/`文件夹中，图片资源位于`app/src/main/res/drawable-xxhdpi/`文件夹中，您需要先将这两部分拷贝的您的App工程中。

3. Demo 的弹幕集成了第三方开源库`DanmakuFlameMaster`，可以自行在 github 获取，也可如 Demo 在 build.gradle示例配置 
```
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
```

## 创建播放器

超级播放器主类为`SuperPlayerView`，您需求先创建它。

```java
mSuperPlayerView = (SuperPlayerView) findViewById(R.id.superVodPlayerView);

// 设置Activity回调方法
mSuperPlayerView.setPlayerViewCallback(this);

// 开始播放
mSuperPlayerView.playWithMode(superPlayerModel);


/**
 * SuperVodPlayerActivity的回调接口，在SuperPlayerView中
 */
public interface PlayerViewCallback {
    void hideViews();
    void showViews();
    void onQuit(int playMode);
}
```

## 直播播放

### 如何播放
直播播放需要传入直播地址，常见的直播协议有一下几种：
![格式](https://mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

推荐使用 FLV 协议(以 .flv 结尾的播放地址)。在超级播放使用方法如下：

``` java
SuperPlayerModel superPlayerModel = new SuperPlayerModel();
superPlayerModel.videoURL = "http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv";
mSuperPlayerView.playWithMode(superPlayerModel); // 开始播放
```

### 清晰度无缝切换
在网络较差的情况下，可以适度降低画质，以减少卡顿；反之，网速变好的情况下可以切到更好的画质。
传统切流方式需要重新播放，会导致切换前后画面衔接不上。 超级播放器引入了无缝切换方案，在不中断直播的情况下切到另条流上。

无缝切换前，需要在播放前提供不同清晰度的流地址。

``` java
SuperPlayerModel superPlayerModel = new SuperPlayerModel();
superPlayerModel.videoURL = "http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv";
superPlayerModel.multiVideoURLs = new ArrayList<>(3);
superPlayerModel.multiVideoURLs.add(new SuperPlayerUrl("超清","http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv"));
superPlayerModel.multiVideoURLs.add(new SuperPlayerUrl("高清","http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_900.flv"));
superPlayerModel.multiVideoURLs.add(new SuperPlayerUrl("标清","http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_550.flv"));
```
在播放器中即可看到这几个清晰度，单击即可立即切换。

![直播清晰度](https://main.qcloudimg.com/raw/8cb10273fe2b6df81b36ddb79d0f4890.jpeg)

### 直播时移回看

时移功能是腾讯云推出的特色能力，可以在直播过程中，随时观看回退到任意直播历史时间点，并能在此时间点一直观看直播。非常适合游戏、球赛等互动性不高，但观看连续性较强的场景。

时移的原来是在直播的过程中，后台也在录制，当用户返回观看历史时间点时，等同于观看录制文件。具体原理可参考 [直播时移文档](https://cloud.tencent.com/document/product/267/18472)。


#### 接入准备

接入时移需要在后台打开2处配置：

1. 录制：配置时移时长、时移储存时长
2. 播放：时移获取元数据

时移功能处于公测申请阶段，如您需要可提交工单申请使用。


#### 开启时移

超级播放器开启时移非常简单，您只需要在播放前配置好appId

```java
superPlayerModel.appid = 1252463788;
```

appId在 腾讯云控制台 -> 账号信息 中可以查到。



配置好appId，播放直播流就能在下面看到进度条。往后拖动即可回到指定位置，单击“返回直播”可观看最新直播流。

![](https://main.qcloudimg.com/raw/a3a4a18819aed49b919384b782a13957.jpeg)



## 点播播放

### 如何播放

超级播放器支持两种点播方式，url和fileId。url方式播放与直播播放相同，只需要把直播流url换成点播url。

点播支持mp4、HLS、FLV格式，推荐使用mp4或hls格式。

| 视频格式 | 优点                           | 缺点                              |
| -------- | ------------------------------ | --------------------------------- |
| MP4      | 在PC和手机上兼容性好，存储简单 | 长视频加载较慢                    |
| HLS      | 苹果主推，加载快，支持多码率   | /                                 |
| FLV      | /                              | 由Adobe Flash延伸出的格式，不推荐 |

fileId播放需要填写 appId 和 fileId两个变量

```java
superPlayerModel.appid = 1252463788;
superPlayerModel.fileid = "4564972819219071679";
mSuperPlayerView.playWithMode(superPlayerModel); // 开始播放
```
通过fileId方式播放，播放器界面会显示后台已转码的各个清晰度，并能实现自由切换。

#### fileId获取

fileId在一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回[fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C)到客户端
2. 服务端视频上传，在[确认上传](https://cloud.tencent.com/document/product/266/9757)的通知中包含对应的fileId

如果文件已存在腾讯云，则可以进入 [点播视频管理](https://console.cloud.tencent.com/video/videolist) ，找到对应的文件。点开后在右侧视频详情中，可以看到appId和fileId。

![视频管理](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

### 清晰度无缝切换

通过fileId播放，如果视频有转码，播放器界面已经可以显示多个清晰度。无缝切换作为更好体验方式，在切换时不会明显感觉到重新加载的卡顿。

无缝切换需要转码时指定生成masterPlaylist和IDR对齐，配置后超级播放在播fileId时，就能取到多码率masterPlaylist的视频源地址。使用上和播普通fileId没有区别，超级播放器内部会自动处理多码率流，只需要在后台修改转码参数，修改方法请参考文档 [对视频文件进行处理](https://cloud.tencent.com/document/product/266/9642#.E8.AF.B7.E6.B1.82.E5.8F.82.E6.95.B0.E8.AF.B4.E6.98.8E)。


## 切换视频

播放器播放另一个视频，调用`playWithMode`即可
```java
mSuperPlayerView.playWithMode(superPlayerModel);
```

## 移除播放器

当不需要播放器时，调用onDestroy清理播放器内部状态，防止干扰下次播放。

```java
if (mSuperPlayerView != null) {
    mSuperPlayerView.resetPlayer();
}
```

