

本文主要介绍适用于开发的接口升级技术文档。方便您调试和接入腾讯云游戏多媒体引擎 API。
## GME 2.x 升级 GME 2.9

### SDK 更新动态
- 动态库拆分。
- 修改 Android 包名。

GME SDK 更新后，除了 libgmesdk 外，新增以下库文件。

### 库文件对应功能

新版本的GME拆解了动态库，尽可能降低包体大小。可以根据自己的需求只引入相应的库文件。例如只需要变声功能，则只需引入 libgmesoundtouch。

|库文件|对应功能|
|----|-----|
|libgmefdkaac|1. 用于进入标准、高清音质房间 2. 用于播放 acc 格式伴奏文件|
|libgmefaad2|用于播放 mp4 格式伴奏文件|
|libgmeogg|用于播放 ogg 格式伴奏文件|
|libgmelamemp3|用于播放 mp3 格式伴奏文件|
|libgmesoundtouch|用于变声、变调功能|

### 升级须知

iOS 端升级，需要参考 [iOS 工程升级指引](https://cloud.tencent.com/document/product/607/67303) 进行相关配置。
Android 端升级，需要修改包名，将 Tencent 改为 GME，混淆配置也需要修改，参考 [Android工程导出文档](https://cloud.tencent.com/document/product/607/56342)。
Unity 端升级，如果使用了标准音质或者高清音质，或者使用了伴奏，需要参考 [Unity使用高清音质文档](https://cloud.tencent.com/document/product/607/67297) 进行解决。


## GME 2.2 升级 GME 2.3.5 
### SDK 更新动态
**新增功能**
- 支持实时语音过程中使用离线语音。
- 支持实时语音过滤，可识别可能令人反感、不安全或不适宜内容。
- 支持 H5 实时语音，实现全平台实时语音互通。
- 新增 Android v8a 架构支持。
- Android 低延时采集播放适配。

**优化能力**
- 优化 SDK 的范围语音功能接口，降低接入门槛。
- 语音降噪效果优化。
- 大幅降低 SDK 内存消耗。

### 主要接口变更
#### EnterRoom 
进房操作由同步改为异步调用，返回值为0时的，表示异步投递成功，等待回调函数进行处理，若返回值不为0时，则表示异步投递失败。

```
public abstract int EnterRoom();
```

#### ExitRoom 
退房操作由同步改为异步调用，参照 RoomExitComplete 回调函数处理，返回值为 AV_OK 时，表示异步投递成功。

>!如果应用中有退房后立即进房的场景，在接口调用流程上，开发者无需要等待 ExitRoom 的回调 RoomExitComplete 通知，只需直接调用接口。

```
public abstract int ExitRoom();
```

### 错误码变更
- 如需对所有错误码统一处理，请使用 !AV_OK。 
- 如需单独处理每一类错误，请关注接口返回的错误类型。

>?错误码“1”没有明确含义，且2.3.5以后版本不再返回，故删除。


### 其他接口变更
#### PauseAudio/ResumeAudio 

```
public int PauseAudio()
public int ResumeAudio()
```

在2.3之前版本的 SDK 接口调用过程中，如有调用 ITMGAudioCtrl::PauseAudio/ResumeAudio 两个接口，可参照下表进行版本对比。


|2.3 之前版本|升级 2.3 版本|
|---|---|
|使用目的为与其他模块互斥|将 PauseAudio 改为 Pause，将 ResumeAudio 改为 Resume|
|使用目的为在实时语音中使用离线语音|请将 PauseAudio 及 ResumeAudio 删除|


#### SetLogLevel 接口参数变更

**原接口**
```
ITMGContext virtual void SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```

**新接口**
```
ITMGContext virtual void SetLogLevel(ITMG_LOG_LEVEL levelWrite, ITMG_LOG_LEVEL levelPrint)
```

**参数说明**

|参数|类型|说明|
|---|---|---|
|levelWrite|ITMG_LOG_LEVEL|设置写入日志的等级，TMG_LOG_LEVEL_NONE 表示不写入|
|levelPrint|ITMG_LOG_LEVEL|设置打印日志的等级，TMG_LOG_LEVEL_NONE 表示不打印|

**ITMG_LOG_LEVEL 类型**

|ITMG_LOG_LEVEL|说明|
|-------------------------------|-------------|
|TMG_LOG_LEVEL_NONE=0		|不打印日志			|
|TMG_LOG_LEVEL_ERROR=1		|打印错误日志（默认）	|
|TMG_LOG_LEVEL_INFO=2			|打印提示日志		|
|TMG_LOG_LEVEL_DEBUG=3		|打印开发调试日志	|
|TMG_LOG_LEVEL_VERBOSE=4		|打印高频日志		|

## GME 2.3.5 升级 GME 2.5.1 
### 增加接口
#### GetSendStreamLevel 
此接口用于获取音频上行实时音量，返回值为 int 类型，取值范围为0到100。

```
ITMGContextGetInstance()->GetAudioCtrl()->GetSendStreamLevel();
```

#### GetRecvStreamLevel 
此接口用于获取房间内其他成员下行实时音量，返回值为 int 类型，取值范围为0到100。

```
iter->second.level = ITMGContextGetInstance()->GetAudioCtrl()->GetRecvStreamLevel(iter->second.openid.c_str());
```

### 接口变更
#### 语音消息及转文字接口变更返回值

以下接口返回值修改为 int 类型。

```
StartRecording
UploadRecordedFile
DownloadRecordedFile
PlayRecordedFile
SpeechToText
```

## GME 2.5 升级 GME 2.7 
### 增加接口
#### PlayRecordedFile(const char* filePath, ITMG_VOICE_TYPE voiceType)
此接口用于播放带有变声效果的语音消息。

#### SetAccompanyKey(int nKey)
此接口用于设置实时语音伴奏升降调。

