为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于开发的接口升级技术文档（GME 2.2 升级 GME 2.3）。

## SDK 变更
### 新增功能
- 支持实时语音过程中使用离线语音；
- 支持实时语音过滤，可识别暴恐、涉黄、涉政等信息；
- 支持 H5 实时语音，实现全平台实时语音互通；

### 优化能力
- 优化 SDK 的范围语音功能接口，降低接入门槛；
- 语音降噪效果优化；
- 大幅降低 SDK 内存消耗；

## 主要接口变更
### EnterRoom 
进房操作由同步改为异步调用，回值为 0 的时候代表异步投递成功，等待回调函数进行处理，否则为异步投递失败。

```
public abstract int EnterRoom();
```

### ExitRoom 
退房操作由同步改为异步调用，参照 RoomExitComplete 回调函数处理，回值为 AV_OK 的时候代表异步投递成功。

>!如果应用中有退房后立即进房的场景，在接口调用流程上，需要先等接口 ExitRoom 的回调 RoomExitComplete 通知后，再调用 EnterRoom 接口。

```
public abstract int ExitRoom();
```



## 其他接口变更
### PauseAudio/ResumeAudio 

```
public int PauseAudio()
public int ResumeAudio()
```

如果在早于 2.3 版本的 SDK 接口调用过程中，有调用到上面两个接口，即 ITMGAudioCtrl::PauseAudio/ResumeAudio，版本对比如下表所示：


|2.3 之前版本|升级 2.3 版本|
|---|---|
|使用目的为与其他模块互斥|将 PauseAudio 改为 Pause，将 ResumeAudio 改为 Resume|
|使用目的为在实时语音中使用离线语音|请将 PauseAudio 及 ResumeAudio 删除|


### SetLogLevel 接口参数变更

#### 原接口
```
ITMGContext virtual void SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```

#### 新接口
```
ITMGContext virtual void SetLogLevel(ITMG_LOG_LEVEL levelWrite, ITMG_LOG_LEVEL levelPrint)
```

#### 参数含义

|参数|类型|意义|
|---|---|---|
|levelWrite|ITMG_LOG_LEVEL|设置写入日志的等级，TMG_LOG_LEVEL_NONE 表示不写入|
|levelPrint|ITMG_LOG_LEVEL|设置打印日志的等级，TMG_LOG_LEVEL_NONE 表示不打印|

#### ITMG_LOG_LEVEL 类型

|ITMG_LOG_LEVEL|意义|
|-------------------------------|-------------|
|TMG_LOG_LEVEL_NONE=0		|不打印日志			|
|TMG_LOG_LEVEL_ERROR=1		|打印错误日志（默认）	|
|TMG_LOG_LEVEL_INFO=2			|打印提示日志		|
|TMG_LOG_LEVEL_DEBUG=3		|打印开发调试日志	|
|TMG_LOG_LEVEL_VERBOSE=4		|打印高频日志		|
