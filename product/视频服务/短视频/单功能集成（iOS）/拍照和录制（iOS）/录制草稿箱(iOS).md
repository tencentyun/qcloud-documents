草稿箱实现步骤：
#### 第一次录制
1. 开始录制。
2. 暂停/结束第一次录制。 
3. 缓存视频分片到本地（草稿箱）。

#### 第二次录制
1. 预加载本地缓存视频分片。
- 继续录制。
- 结束录制。

<dx-codeblock>
::: objc objc
//获取第一次视频录制对象
record = [TXUGCRecord shareInstance]；

//开始录制
[record startRecord];

//暂停录制，缓存视频分片
[record pauseRecord:^{
NSArray *videoPathList = record.partsManager.getVideoPathList;
//videoPathList 写本地
}];

//获取第二次视频录制对象
record2 = [TXUGCRecord shareInstance]；

//预加载本地缓存分片
[record2.partsManager insertPart:videoPath atIndex:0];

//开始录制
[record2 startRecord];

//结束录制,SDK会合成缓存视频片段和当前录制视频片段
[record2 stopRecord];
:::
</dx-codeblock>


>! 具体实现方法请参考 [小视频源码](https://cloud.tencent.com/document/product/584/9366) 中的 UGCKitRecordViewController 类。
