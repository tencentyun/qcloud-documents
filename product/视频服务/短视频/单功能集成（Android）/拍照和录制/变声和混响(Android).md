#### 录制变声混响：

<dx-codeblock>
::: android
// 设置混响
// TXRecordCommon.VIDOE_REVERB_TYPE_0 关闭混响
// TXRecordCommon.VIDOE_REVERB_TYPE_1 KTV
// TXRecordCommon.VIDOE_REVERB_TYPE_2 小房间
// TXRecordCommon.VIDOE_REVERB_TYPE_3 大会堂
// TXRecordCommon.VIDOE_REVERB_TYPE_4 低沉
// TXRecordCommon.VIDOE_REVERB_TYPE_5 洪亮
// TXRecordCommon.VIDOE_REVERB_TYPE_6 金属声
// TXRecordCommon.VIDOE_REVERB_TYPE_7 磁性
mTXCameraRecord.setReverb(TXRecordCommon.VIDOE_REVERB_TYPE_1);

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
mTXCameraRecord.setVoiceChangerType(TXRecordCommon.VIDOE_VOICECHANGER_TYPE_1);
:::
</dx-codeblock>

>?变声混响只针对录制人声有效，针对 BGM 无效。
