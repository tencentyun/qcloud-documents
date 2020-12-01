

视频多段录制基本使用流程如下：

1. 启动画面预览。 
2. 开始录制。
3. 开始播放 BGM。
4. 暂停录制。
5. 暂停播放 BGM。
6. 继续播放 BGM。
7. 继续录制。
8. 停止录制。
9. 停止播放 BGM。

```objc
//开启画面预览
recorder = [TXUGCRecord shareInstance];
[recorder startCameraCustom:param preview:preview];

// 开始录制
[recorder startRecord];

//设置BGM
[recorder setBGM:BGMPath];

//开始播放BGM
[recorder playBGMFromTime:beginTime toTime:_BGMDuration withBeginNotify:^(NSInteger errCode) {
//开始播放
} withProgressNotify:^(NSInteger progressMS, NSInteger durationMS) {
//播放进度
} andCompleteNotify:^(NSInteger errCode) {
 //播放结束
}];

// 调用 pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取管理
[recorder pauseRecord];

//暂停播放BGM
[recorder pauseBGM];

//继续播放BGM
 [recorder resumeBGM];

// 继续录制视频
[recorder resumeRecord];

// 停止录制，将多段视频合成为一个视频输出
[recorder stopRecord];

// 停止播放BGM
[recorder stopBGM];

//获取视频分片管理对象
TXUGCPartsManager *partsManager = recorder.partsManager;

//获取当前所有视频片段的总时长
[partsManager getDuration];

//获取所有视频片段路径
[partsManager getVideoPathList];

// 删除最后一段视频
[partsManager deleteLastPart];

// 删除指定片段视频
[partsManager deletePart:1];

// 删除所有片段视频
[partsManager deleteAllParts];

 //您可以添加当前录制视频之外的视频
[partsManager insertPart:videoPath atIndex:0];

//合成所有片段视频
[partsManager joinAllParts: videoOutputPath complete:complete];
```
