本文主要介绍腾讯云视立方 SDK 的直播播放功能。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | &#10003;  | &#10003;                                                            |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 示例代码
针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example) |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) |

## 对接攻略
[](id:step1)
### 步骤1：下载 SDK 开发包
[下载](https://cloud.tencent.com/document/product/1449/56978) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/1449/56987) 将 SDK 嵌入您的 App 工程中。

[](id:step2)
### 步骤2：添加渲染 View
为了能够展示播放器的视频画面，我们第一步要做的就是在布局 xml 文件里加入渲染 View：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="visible"/>
```

[](id:step3)
### 步骤3：创建 Player
腾讯云视立方 SDK 中的 **V2TXLivePlayer** 模块负责实现直播播放功能，并使用 **setRenderView** 接口将它与我们刚刚添加到界面上的 **video_view** 渲染控件进行关联。
```java
//mPlayerView 即 step1 中添加的界面 view
TXCloudVideoView mView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//创建 player 对象
V2TXLivePlayer mLivePlayer = new V2TXLivePlayerImpl(mContext);
//关键 player 对象与界面 view
mLivePlayer.setRenderView(mView);
```

[](id:step4)
### 步骤4：启动播放
```java
String flvUrl = "http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
mLivePlayer.startPlay(flvUrl); 
```

[](id:step5)
### 步骤5：画面调整
- **view：大小和位置**
如需修改画面的大小及位置，直接调整 [步骤2](#step2) 中添加的 `video_view` 控件的大小和位置即可。
- **setRenderFillMode：铺满 or 适应**
<table><tr><th>可选值</th><th>含义</th>
</tr><tr>
<td>V2TXLiveFillModeFill</td>
<td>将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全</td>
</tr><tr>
<td>V2TXLiveFillModeFit</td>
<td>将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边</td>
</tr></table>
- **setRenderRotation：视频画面顺时针旋转角度**
<table>
<tr><th>可选值</th><th>含义</th></tr><tr>
<td>V2TXLiveRotation0</td><td>不旋转</td>
</tr><tr>
<td>V2TXLiveRotation90</td><td>顺时针旋转90度</td>
</tr><tr>
<td>V2TXLiveRotation180</td><td>顺时针旋转180度</td>
</tr><tr>
<td>V2TXLiveRotation270</td><td>顺时针旋转270度</td>
</tr></table>

<dx-codeblock>
::: Java Java
// 设置填充模式
mLivePlayer.setRenderFillMode(V2TXLiveFillModeFit);
// 设置画面渲染方向
mLivePlayer.setRenderRotation(V2TXLiveRotation0);
:::
</dx-codeblock>

![](https://main.qcloudimg.com/raw/89e7b5b2b6b944fe8377cf9f2bcff573.jpg)

[](id:step6)
### 步骤5：暂停播放
对于直播播放而言，并没有真正意义上的暂停，所谓的直播暂停，只是**画面冻结**和**关闭声音**，而云端的视频源还在不断地更新着，所以当您调用 resume 的时候，会从最新的时间点开始播放，这是和点播对比的最大不同点（点播播放器的暂停和继续与播放本地视频文件时的表现相同）。

```java
// 暂停
mLivePlayer.pauseAudio();
mLivePlayer.pauseVideo();
// 继续
mLivePlayer.resumeAudio();
mLivePlayer.resumeVideo();
```

[](id:step7)
### 步骤7：结束播放
结束播放非常简单，直接调用 `stopPlay` 即可。
```java
mLivePlayer.stopPlay();  
```

[](id:step8)
### 步骤8：屏幕截图
通过调用 **snapshot** 您可以截取当前直播画面为一帧屏幕，此功能只会截取当前直播流的视频画面，如果您需要截取当前的整个 UI 界面，请调用 Android 的系统 API 来实现。
![](https://main.qcloudimg.com/raw/1439eff8e2b9629abf92960e1b784f56.jpg)

```java
mLivePlayer.setObserver(new MyPlayerObserver());
mLivePlayer.snapshot();
// 在MyPlayerObserver的回调接口onSnapshotComplete中获取屏幕截图
private class MyPlayerObserver extends V2TXLivePlayerObserver  {
    ...
    @Override
    public void onSnapshotComplete(V2TXLivePlayer v2TXLivePlayer, Bitmap bitmap) {
    }
    ...
}
```

[](id:Delay)
## 延时调节
腾讯云视立方 SDK 的直播播放功能，并非基于 ffmpeg 做二次开发， 而是采用了自研的播放引擎，所以相比于开源播放器，在直播的延迟控制方面有更好的表现，我们提供了三种延迟调节模式，分别适用于：秀场、游戏以及混合场景。

- **三种模式的特性对比**
<table>
<tr><th>控制模式</th><th>卡顿率</th><th>平均延迟</th><th>适用场景</th><th>原理简述</th></tr>
<tr>
<td>极速模式</td>
<td>较流畅偏高</td>
<td>2s- 3s</td>
<td>美女秀场（冲顶大会）</td>
<td>在延迟控制上有优势，适用于对延迟大小比较敏感的场景</td>
</tr><tr>
<td>流畅模式</td>
<td>卡顿率最低</td>
<td>&gt;= 5s</td>
<td>游戏直播（企鹅电竞）</td>
<td>对于超大码率的游戏直播（例如绝地求生）非常适合，卡顿率最低</td>
</tr><tr>
<td>自动模式</td>
<td>网络自适应</td>
<td>2s-8s</td>
<td>混合场景</td>
<td>观众端的网络越好，延迟就越低；观众端网络越差，延迟就越高</td>
</tr></table>
- **三种模式的对接代码**
```java
//自动模式
mLivePlayer.setCacheParams(1.0f, 5.0f);
//极速模式
mLivePlayer.setCacheParams(1.0f, 1.0f);
//流畅模式
mLivePlayer.setCacheParams(5.0f, 5.0f);
//设置完成之后再启动播放
```

>? 更多关于卡顿和延迟优化的技术知识，请参见 [优化视频卡顿](https://cloud.tencent.com/document/product/1449/58943)。

[](id:sdklisten)
## SDK 事件监听
您可以为 V2TXLivePlayer 对象绑定一个 [V2TXLivePlayerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__android.html)，之后 SDK 的内部状态信息例如播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等会通过对应的回调通知给您。

### 定时触发的状态通知

- [onStatisticsUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__android.html#ab10e1f4e22e9bb73e3cea4ae15c36465) 通知每2秒都会被触发一次，目的是实时反馈当前的播放器状态，它就像汽车的仪表盘，可以告知您目前 SDK 内部的一些具体情况，以便您能对当前网络状况和视频信息等有所了解。
<table>
<tr><th>评估参数</th><th>含义说明</th></tr>
<tr>
<td>appCpu</td>
<td>当前 App 的 CPU 使用率（％）</td>
</tr><tr>
<td>systemCpu</td>
<td>当前系统的 CPU 使用率（％）</td>
</tr><tr>
<td>width</td>
<td>视频宽度</td>
</tr><tr>
<td>height</td>
<td>视频高度</td>
</tr><tr>
<td>fps</td>
<td>帧率（fps）</td>
</tr><tr>
<td>audioBitrate</td>
<td>音频码率（Kbps）</td>
</tr><tr>
<td>videoBitrate</td>
<td> 视频码率（Kbps）</td>
</tr></table>
- [onPlayoutVolumeUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__android.html#a57fc000bf5e935f7253fa94e1750359e) 播放器音量大小回调。这个回调仅当您调用 [enableVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#aaa893a96eff34a7ba660441f7597d6d8) 开启播放音量大小提示之后才会工作。回调的时间间隔也会与您在设置 `enableVolumeEvaluation` 的参数 `intervalMs` 保持一致。

### 非定时触发的状态通知
其余的回调仅在事件发生时才会抛出来。
