## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 草稿箱实现步骤

### 第一次录制
1. 开始录制。
2. 暂停/结束第一次录制。
3. 缓存视频分片到本地（草稿箱）。

### 第二次录制
1. 预加载本地缓存视频分片。
2. 继续录制。
3. 结束录制。

## 示例代码

<dx-codeblock>
::: android 
// 获取第一次视频录制对象
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());

// 开始录制
mTXCameraRecord.startRecord();

// 暂停录制
mTXCameraRecord.pauseRecord();

// 获取缓存的录制分片，记录到本地
List<String> pathList = mTXCameraRecord.getPartsManager().getPartsPathList(); // pathList 写本地

// 第二次打开 app，获取录制对象
mTXCameraRecord2 = TXUGCRecord.getInstance(this.getApplicationContext());

// 预加载本地缓存片段
mTXCameraRecord2.getPartsManager().insertPart(videoPath, 0);

// 开始录制
mTXCameraRecord2.startRecord();

// 结束录制,SDK 会把缓存视频片段和当前录制视频片段合成
mTXCameraRecord2.stopRecord();
:::
</dx-codeblock>

>?具体实现方法请参见 [小视频源码](https://cloud.tencent.com/document/product/1449/56977#video_app) 中录制中的 RecordDraftMgr 类的使用。
