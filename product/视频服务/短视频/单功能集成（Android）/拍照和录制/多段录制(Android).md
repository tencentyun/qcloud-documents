
视频多段录制基本使用流程如下： 

1. 启动画面预览。
2. 开始录制。
3. 开始播放 BGM。
4. 暂停录制。
5. 暂停播放 BGM。
6. 继续录制。
7. 继续播放 BGM。
8. 停止录制。
9. 停止 BGM。

```
// 开始录制
mTXCameraRecord.startRecord();

// pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取
mTXCameraRecord.pauseRecord();
mTXCameraRecord.pauseBGM();

// 继续录制视频
mTXCameraRecord.resumeRecord();
mTXCameraRecord.resumeBGM();

// 停止录制，将多段视频合成为一个视频输出
mTXCameraRecord.stopBGM();
mTXCameraRecord.stopRecord();

// 获取片段管理对象
mTXCameraRecord.getPartsManager();

// 获取当前所有视频片段的总时长
mTXUGCPartsManager.getDuration();

// 获取所有视频片段路径
mTXUGCPartsManager.getPartsPathList();

// 删除最后一段视频
mTXUGCPartsManager.deleteLastPart();

// 删除指定片段视频
mTXUGCPartsManager.deletePart(index);

// 删除所有片段视频
mTXUGCPartsManager.deleteAllParts();

// 您可以添加当前录制视频之外的视频
mTXUGCPartsManager.insertPart(videoPath, index) ;

```
