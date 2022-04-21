
草稿箱实现步骤： 
#### 第一次录制
1. 开始录制。
2. 暂停/结束第一次录制。
3. 缓存视频分片到本地（草稿箱）。

#### 第二次录制
1. 预加载本地缓存视频分片。
2. 继续录制。
3. 结束录制。



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

>?具体实现方法请参考 [小视频源码](https://cloud.tencent.com/document/product/584/9366) 中录制中的 RecordDraftManager 类的使用。
