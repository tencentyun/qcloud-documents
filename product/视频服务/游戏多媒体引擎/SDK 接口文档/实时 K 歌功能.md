
为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍游戏多媒体引擎实时语音 K 歌功能的接入技术文档。


## 使用前提
- 如需使用实时语音 K 歌功能，需要在接入 GME SDK 且能在进行实时语音通话的情况下，才可以使用此功能。
- 进房时候需要填入房间类型参数，推荐使用 RoomType = 2 进入房间（请使用2或者3）。
- 使用中如果有错误码提示，可参考 [错误码文档](https://cloud.tencent.com/document/product/607/15173) 进行解决。
- 技术方案及相关实践可以观看 [零基础快速搭建 K 歌应用](https://cloud.tencent.com/edu/learning/live-1672)。


#### 流程图
进房流程参考图如下：
![](https://main.qcloudimg.com/raw/02785c646096bc435fe91003fe3169e7.png)


实时语音进房接口：
```
ITMGContext.GetInstance(this).Init(String.valueOf(mAppId), mUserId);//初始化sdk
ITMGContext.GetInstance(this).SetTMGDelegate(new MyDelegate());//设置代理类，用来接受各种回调和事件
EnginePollHelper.createEnginePollHelper();//周期性调用Poll函数，触发回调

byte[] authbuff = AuthBuffer.getInstance().genAuthBuffer(mAppId, mRoomId, mUserId,mAppKey);//获得鉴权信息
ITMGContext.GetInstance(this).EnterRoom(mRoomId, 2, authbuff);//进入房间
```

>?详细调用流程和接口详情请参考 [各端 SDK 接口文档](https://cloud.tencent.com/document/product/607)。



## K 歌接口获取
1. 您需要在 [下载指引](https://cloud.tencent.com/document/product/607/18521) 中下载标准 SDK 文件。
2. 根据不同的平台，下载 [K 歌功能接口](https://picture-1256313114.cos.ap-beijing.myqcloud.com/ktv_header.zip)并导入相应接口文件。

>?此功能支持 mp3、ogg 一共两种格式。
- 如果音乐文件为 ogg 格式，请 [单击下载ogg动态库](https://picture-1256313114.cos.ap-beijing.myqcloud.com/ogg_codec.zip)（iOS 端已包含 ogg 动态库，无需额外导入）。
- 如果音乐文件为 mp3 格式，请 [单击下载mp3动态库](https://picture-1256313114.cos.ap-beijing.myqcloud.com/mp3_codec.zip)（只有 iOS 平台才需导入此动态库，其他平台无需额外导入）。

### Android 端配置
Android 对应的接口，已经包含在标准 jar 包内，不需要下载额外的接口文件。

### iOS 端配置
1. 在 iOS 端使用 K 歌功能，需要将相关动态库引入工程中，[单击下载 mp3 动态库](https://picture-1256313114.cos.ap-beijing.myqcloud.com/mp3_codec.zip)。
2. 将下载好的文件引入到工程文件中。并在 Link Binary With Libraries 中添加此动态库。
3. 将头文件 TMGEngine_adv.h 加入工程中，与其他 SDK 头文件同目录下。

### Windows 端配置
Windows 端使用 K 歌功能，需要下载头文件后，将头文件 tmg_sdk_adv.h、tmg_type_adv.h 导入工程中。

### Unity 引擎配置
在 Unity 引擎中使用 K 歌功能，需要下载头文件，将 Unity 文件夹下的代码文件 TMGEngine_Adv.cs、ITMGEngine_Adv.cs 拷贝后导入工程中。

如需导出 iOS 平台，请参考上文进行 mp3 动态库导入。


## 录制相关接口

### 开始录制
调用 StartRecord 接口开始录制。录制完成会有回调函数，需要监听  ITMG_MAIN_EVENT_TYPE_RECORD_COMPLETED。

录制时候请保证麦克风已经打开（设备及上行都需要打开），另外保证文件路径是可访问的，SDK 不会主动创建文件夹。

#### 函数原型  
```
int StartRecord(int type, String dstFile, String accMixFile, String accPlayFile)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| type    		|int		|K歌场景下，此参数传 ITMG_AUDIO_RECORDING_KTV。如果是纯录制 MP3 文件，请使用 ITMG_AUDIO_RECORDING_SELF|
| dstFile  		|String	|目标文件路径，用于保存录制完成的音乐。|
| accMixFile	|String 	|一般为没有原声的伴奏，用于和人声合成音乐文件。|
| accPlayFile	|String 	|用于播放的音乐文件，正常情况下与 accMixFile 为同一个文件。但在用户不熟悉歌曲时，可以填入带原唱的音乐文件路径，此时播放内容为带原唱的音乐，而合成为不带原声的伴奏。|

#### 示例代码

```
//Android
ITMGAudioRecordCtrl.GetInstance().StartRecord(ITMGAudioRecordCtrl.ITMG_AUDIO_RECORDING_KTV, dstFile, accMixFile, accPlayFile);
//iOS
#import "GMESDK/TMGEngine_adv.h"
[[ITMGAudioRecordCtrl GetInstance]StartPreview]
```



### 停止录制
调用 StopRecord 接口停止录制。
#### 函数原型  
```
int StopRecord()
```

### 暂停录制
调用 PauseRecord 接口暂停录制。
#### 函数原型  
```
int PauseRecord()
```

### 恢复录制
调用 ResumeRecord 接口恢复录制。
#### 函数原型  
```
int ResumeRecord()
```

### 录制回调
ITMG_MAIN_EVENT_TYPE_RECORD_COMPLETED 录制完成的回调。伴奏播放结束或者调用 StopRecord 触发此回调。

#### 回调参数
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| result    		|int		|录制结果，0为成功。如果有其他错误码，可参考 [ 错误码文档](https://cloud.tencent.com/document/product/607/15173) 进行解决。|
| filepath  		|String	|目标文件的路径，StartRecord 传入的参数 dstFile。|
| duration	|String 	|录制文件的长度，单位为毫秒。|



### 设置播放文件
在调用 StartRecord 接口进行录制的时候，会设置播放的音乐文件。如果想要重新设置，可调用此接口重新设置播放文件。一般用于在原唱和纯音伴奏之间切换。

#### 函数原型  
```
int SetAccompanyFile(String accPlayFile)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| accPlayFile    		|String |用于播放的音乐文件。|



### 获取伴奏时长
调用此参数获取伴奏文件 accMixFile 的时长，返回的时长单位为毫秒。

#### 函数原型  
```
int GetAccompanyTotalTimeByMs()
```

### 获取当前录制时长

调用此参数获取获取当前录制时长，返回的时长单位为毫秒。

#### 函数原型  
```
int GetRecordTimeByMs()
```

### 录制跳转
将录制时间跳转到指定时刻。如果参数比当前时间靠前，则重复的地方重新录制；相比当前时间靠后，则用静音数据填充没有录制的部分。

#### 函数原型  
```
int SetRecordTimeByMs(int timeMs)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| timeMs    		|int |跳转的时刻，单位为毫秒。|



## K 歌文件预览
### 获取录制文件的时长
调用此参数获取录制文件的时长。

#### 函数原型  
```
int GetRecordFileDurationByMs()
```

### 开始预览录制文件
调用此参数开始预览录制文件。

#### 函数原型  
```
int StartPreview()
```

### 停止预览录制文件
调用此参数停止预览录制文件。

#### 函数原型  
```
int StopPreview()
```

### 暂停预览录制文件
调用此参数暂停预览录制文件。

#### 函数原型  
```
int PausePreview()
```

### 恢复预览录制文件
调用此参数恢复预览录制文件。

#### 函数原型  
```
int ResumePreview()
```

### 设置当前预览的时间点
调用此参数设置当前预览的时间点。
   
#### 函数原型  
```
int SetPreviewTimeByMs(int time)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| time    		|int |预览文件的时间点，单位毫秒。|

### 获取当前预览的时间点
调用此参数获取当前预览的时间点。

#### 函数原型  
```
int GetPreviewTimeByMs()
```

### 播放预览回调
ITMG_MAIN_EVENT_TYPE_RECORD_PREVIEW_COMPLETED 预览完成的回调。预览文件播放结束或者调用 StopPreview 接口触发

#### 回调参数
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| result    		|int		|播放结果，0为成功。|


## 文件合成接口

### 合并文件
调用此参数将录制好的人声和伴奏合并成一个文件。
   
#### 函数原型  
```
int MixRecordFile();
```

### 取消合并
调用此参数将取消合并操作。
   
#### 函数原型  
```
int CancelMixRecordFile();
```


### 合并文件回调
ITMG_MAIN_EVENT_TYPE_RECORD_MIX_COMPLETED 预览完成的回调。预览文件播放结束或者调用 StopPreview 接口触发。

#### 回调参数
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| result    		|int		|合成结果，0为成功。|
| filepath    		|String		|目标文件的路径，由 StartRecord 接口中传入的 dstFile。|
| duration    		|String		|录制文件的长度，单位为毫秒。|

## 高级设置

### 设置伴奏缩放
调用此接口设置人声和伴奏的缩放比例。录制完成后可进行调整。

####  函数原型  
```
int SetMixWieghts(float mic, float acc)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| mic    		|float |人声的缩放比例，1.0为原来音量，小于1.0为缩小，大于1.0为放大，范围为0到2。|
| acc    		|float |伴奏的缩放比例，1.0为原来音量，小于1.0为缩小，大于1.0为放大，范围为0到2。|

### 设置偏移量
调用此接口设置人声相对于伴奏的偏移，一般用于调整声音跟不上节拍的问题。录制完成后可进行调整。

####  函数原型  
```
int AdjustAudioTimeByMs(int time)
```
|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| time    		|int |人声相对于伴奏的偏移时间，单位ms。大于0为向后移动，小于0为向前移动。|

### 设置音效
设置音效类型，K 歌音效可参考 [实时语音音效文档](https://cloud.tencent.com/document/product/607/34378)。录制完成后可进行调整，录制时也可使用。

####  函数原型  
```
int SetRecordKaraokeType(int type)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| type    		|int |此类型同等于实时语音音效中的K歌音效特效类型，具体可参考 [K 歌音效特效](https://cloud.tencent.com/document/product/607/34378#k-.E6.AD.8C.E9.9F.B3.E6.95.88.E7.89.B9.E6.95.88)。|



