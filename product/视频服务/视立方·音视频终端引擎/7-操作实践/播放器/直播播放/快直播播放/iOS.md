本文主要介绍腾讯云视立方 SDK 的直播播放功能。
## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | &#10003;  | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 基础知识
### 直播和点播 
- **直播（LIVE）**的视频源是主播实时推送的。因此，主播停止推送后，播放端的画面也会随即停止，而且由于是实时直播，所以播放器在播直播 URL 的时候是没有进度条的。
- **点播（VOD）**的视频源是云端的一个视频文件，只要未被从云端移除，视频就可以随时播放， 播放中您可以通过进度条控制播放位置，腾讯视频和优酷土豆等视频网站上的视频观看就是典型的点播场景。

### 协议的支持
通常使用的直播协议如下，标准直播推荐使用 FLV 协议的直播地址（以 `http` 开头，以 `.flv` 结尾），快直播使用 WebRTC 协议，更多信息请参见 [快直播拉流](https://cloud.tencent.com/document/product/454/55880)：

|直播协议 |优点 |缺点 |播放延迟 |
|---------|---------|---------|---------|
|FLV |成熟度高、高并发无压力 |需集成 SDK 才能播放 |2s - 3s |
|RTMP |延迟较低 |高并发情况下表现不佳 |1s - 3s |
|HLS(m3u8) |手机浏览器支持度高 |延迟非常高 |10s - 30s |
|WebRTC |延迟最低 |需集成 SDK 才能播放 |< 1s |


>?标准直播与快直播计费价格不同，更多计费详情请参见 [标准直播计费](https://cloud.tencent.com/document/product/267/34175) 和 [快直播计费](https://cloud.tencent.com/document/product/267/39136)。


## 特别说明
腾讯云视立方 SDK **不会对播放地址的来源做限制**，即您可以用它来播放腾讯云或非腾讯云的播放地址。但腾讯云视立方 SDK 中的播放器只支持 FLV 、RTMP、HLS（m3u8）和 WebRTC 四种格式的直播地址，以及 MP4、 HLS（m3u8）和 FLV 三种格式的点播地址。

## 对接攻略
[](id:step1)
### 步骤1：创建 Player
腾讯云视立方 SDK 中的 V2TXLivePlayer 模块负责实现直播播放功能。
```objectivec
V2TXLivePlayer *_txLivePlayer = [[V2TXLivePlayer alloc] init];
```

[](id:step2)
### 步骤2：渲染 View
接下来我们要给播放器的视频画面找个地方来显示，iOS 系统中使用 view 作为基本的界面渲染单位，所以您只需要准备一个 view 并调整好布局就可以了。

```objectivec
//用 setRenderView 给播放器绑定决定渲染区域的view.
[_txLivePlayer setRenderView:_myView];
```

内部原理上，播放器并不是直接把画面渲染到您提供的 view （示例代码中的 `_myView`）上，而是在这个 view 之上创建一个用于 OpenGL 渲染的子视图（subView）。

如果您要调整渲染画面的大小，只需要调整您所常见的 view 的大小和位置即可，SDK 会让视频画面跟着您的 view 的大小和位置进行实时的调整。
 ![](https://main.qcloudimg.com/raw/39a02a8525a20fd861c69c42d2b3ab14.png)

**如何做动画？**
针对 view 做动画是比较自由的，不过请注意此处动画所修改的目标属性应该是 transform 属性而不是 frame 属性。
```objectivec
[UIView animateWithDuration:0.5 animations:^{
		_myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
}];
```

[](id:step3)
### 步骤3：启动播放
```objectivec
NSString* url = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:url];
```

[](id:step4)
### 步骤4：画面调整

- **setRenderFillMode：铺满 or 适应**
<table>
<tr><th>可选值</th><th>含义</th>
</tr><tr>
<td>V2TXLiveFillModeFill</td>
<td>将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全</td>
</tr><tr>
<td>V2TXLiveFillModeFit</td>
<td>将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边</td>
</tr></table>
- **setRenderRotation：视频画面顺时针旋转角度**
<table>
<tr><th>可选值</th><th>含义</th>
</tr><tr>
<td>V2TXLiveRotation0</td>
<td>不旋转</td>
</tr><tr>
<td>V2TXLiveRotation90</td>
<td>顺时针旋转90度</td>
</tr><tr>
<td>V2TXLiveRotation180</td>
<td>顺时针旋转180度</td>
</tr><tr>
<td>V2TXLiveRotation270</td>
<td>顺时针旋转270度</td>
</tr></table>

![](https://main.qcloudimg.com/raw/f3c65504a98c38857ff3e78bcb6c9ae9.jpg)

[](id:step5)
### 步骤5：暂停播放
对于直播播放而言，并没有真正意义上的暂停，所谓的直播暂停，只是**画面冻结**和**关闭声音**，而云端的视频源还在不断地更新着，所以当您调用 resume 的时候，会从最新的时间点开始播放，这是和点播对比的最大不同点（点播播放器的暂停和继续与播放本地视频文件时的表现相同）。

```objectivec
// 暂停
[_txLivePlayer pauseAudio];
[_txLivePlayer pauseVideo];
// 恢复
[_txLivePlayer resumeAudio];
[_txLivePlayer resumeVideo];
```

[](id:step6)
### 步骤6：结束播放

```objectivec
// 停止播放
[_txLivePlayer stopPlay];
```

[](id:step7)
### 步骤7：屏幕截图
通过调用 **snapshot** 您可以截取当前直播画面为一帧屏幕通过 V2TXLivePlayerObserver 的 [onSnapshotComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a5754eb816b91fd0d0ac1559dd7884dad) 回调截屏图片，此功能只会截取当前直播流的视频画面，如果您需要截取当前的整个 UI 界面，请调用 iOS 的系统 API 来实现。
![](https://main.qcloudimg.com/raw/d86e665e3fc709c07d170e2ab3e2a7ef.jpg)
```
...
[_txLivePlayer setObserver:self];
[_txLivePlayer snapshot];
...

- (void)onSnapshotComplete:(id<V2TXLivePlayer>)player image:(TXImage *)image {
    if (image != nil) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [self handle:image];
        });
    }
}
```

## 延时调节
腾讯云视立方 SDK 的直播播放功能，并非基于 ffmpeg 做二次开发， 而是采用了自研的播放引擎，所以相比于开源播放器，在直播的延迟控制方面有更好的表现，我们提供了三种延迟调节模式，分别适用于：秀场，游戏以及混合场景。

- **三种模式的特性对比**
<table>
<tr><th>控制模式</th><th>卡顿率</th><th>平均延迟</th><th>适用场景</th><th>原理简述</th>
</tr><tr>
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
```objectivec
//自动模式
[_txLivePlayer setCacheParams:1 maxTime:5];
//极速模式
[_txLivePlayer setCacheParams:1 maxTime:1];
//流畅模式
[_txLivePlayer setCacheParams:5 maxTime:5];

//设置完成之后再启动播放
```

>? 更多关于卡顿和延迟优化的技术知识，请参见 [优化视频卡顿](https://cloud.tencent.com/document/product/1449/58943)。

[](id:sdklisten)
## SDK 事件监听
您可以为 V2TXLivePlayer 对象绑定一个 [V2TXLivePlayerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html)，之后 SDK 的内部状态信息例如播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等会通过对应的回调通知给您。

### 定时触发的状态通知
- [onStatisticsUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusherObserver__ios.html#ae93683da9240a752e7b6d70d8e940cbc) 通知每2秒都会被触发一次，目的是实时反馈当前的播放器状态，它就像汽车的仪表盘，可以告知您目前 SDK 内部的一些具体情况，以便您能对当前网络状况和视频信息等有所了解。
<table>
<tr><th>评估参数</th><th>含义说明</th>
</tr><tr>
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
<td>视频码率（Kbps）</td>
</tr></table>
- [onPlayoutVolumeUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a5439ba0397be3943c6ebfb6083c27664) 播放器音量大小回调。这个回调仅当您调用 [enableVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#aeed74080dd72e52b15475a54ca5fd86b) 开启播放音量大小提示之后才会工作。回调的时间间隔也会与您在设置 `enableVolumeEvaluation` 的参数 `intervalMs` 保持一致。

### 非定时触发的状态通知
其余的回调仅在事件发生时才会抛出来。
