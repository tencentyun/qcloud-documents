## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 录制添加 BGM 

<dx-codeblock>
::: android 
// 设置 BGM 路径
mTXCameraRecord.setBGM(path);

// 设置 BGM 播放回调 TXRecordCommon.ITXBGMNotify
mTXCameraRecord.setBGMNofify(notify);

// 播放 BGM
mTXCameraRecord.playBGMFromTime(startTime, endTime)

// 停止播放 BGM
mTXCameraRecord.stopBGM();

// 暂停播放 BGM
mTXCameraRecord.pauseBGM();

// 继续播放 BGM
mTXCameraRecord.resumeBGM();

// 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小
// 音量大小,1为正常音量,建议值为0~2,如果需要调大背景音量可以设置更大的值
mTXCameraRecord.setBGMVolume(x);

// 设置背景音乐播放的开始位置和结束位置
mTXCameraRecord.seekBGM(startTime, endTime);
:::
</dx-codeblock>

## 编辑添加 BGM
<dx-codeblock>
::: android 
// 设置 BGM 路径，返回值为0表示设置成功； 其他表示失败，如：不支持的音频格式。
public int setBGM(String path);

// 设置 BGM 开始和结束时间，单位毫秒
public void setBGMStartTime(long startTime, long endTime);

// 设置背景音乐是否循环播放：true：循环播放，false：不循环播放
public void setBGMLoop(boolean looping);

// 设置 BGM 在视频添加的起始位置
public void setBGMAtVideoTime(long videoStartTime);

// 设置视频声音大小， volume 表示声音的大小， 取值范围0 - 1 ， 0 表示静音， 1 表示原声大小。
public void setVideoVolume(float volume);

// 设置BGM声音大小，volume 表示声音的大小， 取值范围0 - 1 ， 0 表示静音， 1 表示原声大小。
public void setBGMVolume(float volume);
:::
</dx-codeblock>

>?BGM 设置完之后，当启动编辑器预览，BGM 就会根据设置的参数播放，当启动编辑器生成，BGM 也会按照设置的参数合成到生成的视频中。
