## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | &#10003;  | &#10003;  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 录制变声混响

<dx-codeblock>
::: ios 
//获取 recorder 对象
recorder = [TXUGCRecord shareInstance];

// 设置混响
// TXRecordCommon.VIDOE_REVERB_TYPE_0 关闭混响
// TXRecordCommon.VIDOE_REVERB_TYPE_1 KTV
// TXRecordCommon.VIDOE_REVERB_TYPE_2 小房间
// TXRecordCommon.VIDOE_REVERB_TYPE_3 大会堂
// TXRecordCommon.VIDOE_REVERB_TYPE_4 低沉
// TXRecordCommon.VIDOE_REVERB_TYPE_5 洪亮
// TXRecordCommon.VIDOE_REVERB_TYPE_6 金属声
// TXRecordCommon.VIDOE_REVERB_TYPE_7 磁性
[recorder setReverbType:VIDOE_REVERB_TYPE_1];

// 设置变声
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_0  关闭变声
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_1  熊孩子
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_2  萝莉
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_3  大叔
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_4  重金属
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_6  外国人
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_7  困兽
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_8  死肥仔
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_9  强电流
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_10 重机械
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_11 空灵
[record setVoiceChangerType:VIDOE_VOICECHANGER_TYPE_1];
:::
</dx-codeblock>

>?变声混响只针对录制人声有效，针对 BGM 无效。
