>? 
>- 当前页面为新版（V2.0.0及以上）SDK 开发文档。新客户可直接按当前文档接入新版 SDK。
>- 旧版（V1.5.1版本及以下）开发文档已于2022年9月5日下线。正在使用旧版 SDK 的客户，可前往 [控制台](https://console.cloud.tencent.com/tts/download)  查看开发文档。
>- 新版 SDK 在稳定性、功能健全性、接口自由度等方面都有所优化。我们将继续支持旧版（V1.5.1版本及以下）SDK，但建议正在使用旧版 SDK 的客户及时升级到新版，以获取更好的使用体验。

## 开发相关
### 开发准备
- 支持 iOS 9.0 及以上版本，不支持 bitcode 版本。
- 合成实时流式语音，需要手机能够连接网络（3/4/5G 或 Wi-Fi 网络等）。
- 语音合成 [iOS SDK ](https://console.cloud.tencent.com/tts/download)。
- 服务端 [API 文档](https://cloud.tencent.com/document/product/1073/37995)。

### 导入 SDK
SDK 文件夹内的 QCloudTTS.framework 即为 SDK，引入 `<QCloudTTS/QCloudTTSEngine.h>` 及 `<QCloudTTS/QCloudMediaPlayer.h>` 即可调用 SDK 相关接口。

### 接口说明
#### 获得 TTS 合成器实例
```java
//获得实例
QCloudTTSEngine *ttsEngine = [QCloudTTSEngine getShareInstance];

//销毁实例
[QCloudTTSEngine instanceRelease];
```

#### 初始化引擎
```java
-(void) engineInit:(TtsMode)mode Delegate:(id<QCloudTTSEngineDelegate> _Nonnull) delegate; 
//TtsMode: 固定填入 TTS_MODE_ONLINE
//QCloudTTSEngineDelegate: TTS合成器代理，用于获取合成结果
```

#### **QCloudTTSEngineDelegate**: TTS合成器代理，用于获取合成结果
**onSynthesizeData 方法签名说明**

| 参数               | 说明                                                  |
| ------------------ | ----------------------------------------------------- |
| NSData   data      | 语音数据                                              |
| String utteranceId | 语句 ID                                                |
| String text        | 文本                                                  |
| int engineType     | 引擎类型，0：在线， 1：离线；当前是纯在线 SDK，请忽略此参数 |

**onError方法签名说明**

| 参数               | 说明                     |
| ------------------ | ------------------------ |
| TtsError error     | 错误信息，无错误返回 null |
| String utteranceId | 语句 ID（如果有则返回）    |
| String text        | 文本（如果有则返回）       |

**示例**
```java
-(void) onSynthesizeData:(NSData *_Nullable)data UtteranceId:(NSString *_Nullable)utteranceId Text:(NSString *_Nullable)text EngineType:(NSInteger)type{
	// 您可以在这里将音频保存或者送入播放接口播放，可调用播放器入参接口入参
}

-(void) onError:(TtsError *_Nullable)error UtteranceId:(NSString *_Nullable)utteranceId Text:(NSString *_Nullable)text{
	// 您可以在这里添加错误后处理
}


- (void)onOfflineAuthInfo:(QCloudOfflineAuthInfo * _Nonnull)OfflineAuthInfo {
    //离在线SDK保留接口，请忽略，如果您后续升级为离线SDK或者离在线SDK，此接口将用于返回授权信息
}
```

#### 合成文本入参接口

| 接口                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| -(TtsError *_Nullable) synthesize:(NSString *_Nonnull)text UtteranceId:(NSString *_Nullable)utteranceId; | text 为需要合成的文本；utteranceId 为标记该文本的 ID，将随合成结果返回宿主层，业务不需要可传 nil |

**示例**

```java
//内部有维护队列，可持续添加语句，SDK内将依次合成
TtsError error = nil;
error = [ttsEngine synthesize:@"今天天气不错".text UtteranceId:@"第1句"];
error = [ttsEngine synthesize:@"腾讯云语音合成".text UtteranceId:@"第2句"];
error = [ttsEngine synthesize:@"腾讯云AI".text UtteranceId:@"第3句"];
error = [ttsEngine synthesize:@"腾讯云".text UtteranceId:nil];

//取消未合成的任务并清空内部队列
[ttsEngine cancel];
```

#### QCloudTTSEngine配置参数方法

| 接口                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| setOnlineAuthParam:(NSInteger)appId SecretId:(NSString* _Nonnull)secretId SecretKey:(NSString* _Nonnull)secretKey Token:(NSString* _Nullable)token | appid：配置腾讯云 appid、SecretId、SecretKey、Token（ token，可为空，如果使用 [STS 临时证书](https://cloud.tencent.com/document/product/598/33416) 鉴权，secretId 和 secretKey 均入参临时的，同时需要入参对应的 token ） |
| setOnlineVoiceSpeed:(float)voiceSpeed;                       | 设置在线所合成音频的语速，语速范围：[-2，2]，分别对应不同语速：0.6倍、0.8倍、1.0倍、1.2倍、1.5倍，默认为0<br>如果需要更细化的语速，可以保留小数点后一位，例如0.5、1.1、1.8等。  |
| setOnlineVoiceVolume:(float)voiceVolume;                     | 设置在线所合成音频的音量，默认0                              |
| setOnlineVoiceLanguage:(int)primaryLanguage;                 | 主语言类型：1-中文（默认）2-英文                             |
| setOnlineCodec:(NSString* _Nonnull) code;                    | 在线模式编码格式，**非业务必要不建议更改：默认 mp3**，目前支持 mp3、wav、pcm，如更改为 pcm 不支持播放 |
| setOnlineVoiceType:(int)voiceType;                           | 设置在线所合成音频的音色 ID，完整的音色 ID 列表参见 [基础语音合成](https://cloud.tencent.com/document/product/1073/37995) |
| setTimeoutIntervalForRequest:(int)timeout;                   | 连接超时，范围：[500,30000]，单位ms，默认15000ms              |
| setTimeoutIntervalForResource:(int) timeout;                 | 读取超时，范围：[2200,60000]，单位ms ，默认30000ms      |

**示例**
```java
  [ttsEngine setOnlineAuthParam:123 SecretId:@"AK****Hp7" SecretKey:@"D9***c2" Token:nil];
  [ttsEngine setOnlineVoiceSpeed:0.0];//配置语速
  [ttsEngine setOnlineVoiceType:1001];//配置音色id 
  [ttsEngine setOnlineVoiceLanguage:1];//配置主语言
  [ttsEngine setOnlineVoiceVolume:0];//配置音量
  [ttsEngine setTimeoutIntervalForRequest:15 *1000];
  [ttsEngine setTimeoutIntervalForResource:30 *1000];
```



### 播放接口
#### 初始化播放器
如果 SDK 的内置播放器无法满足您的需求，您也可以使用自己实现的播放器替换。demo 中也额外提供了一份播放器源码，您可以修改播放器逻辑，源代码位于 MediaPlayerDemo.m，与 SDK 内置播放器一致。
```java
//使用SDK中提供的播放器

 QCloudMediaPlayer player = [[QCloudMediaPlayer alloc]init];

//---------QCloudPlayerDelegate---------
//播放开始
-(void) onTTSPlayStart{
    NSLog(@"onTTSPlayStart");
}

//队列所有音频播放完成，音频等待中
-(void) onTTSPlayWait{
    NSLog(@"onTTSPlayWait");
}

//恢复播放
-(void) onTTSPlayResume{
    NSLog(@"onTTSPlayResume");
}

//暂停播放
-(void) onTTSPlayPause{

    NSLog(@"onTTSPlayPause");
}
//播放中止
-(void)onTTSPlayStop{
    NSLog(@"onTTSPlayStop");
    
}
//播放器异常
-(void)onTTSPlayError:(QCPlayerError* _Nullable)playError{
    NSLog(@"playError.code==%@,playError.massage==%@",@(playError.mCode),playError.message);
}

//即将播放播放下一句，即将播放音频对应的句子，以及这句话utteranceId
-(void) onTTSPlayNextWithText:(NSString* _Nullable)text UtteranceId:(NSString* _Nullable)utteranceId{
    NSLog(@"text==%@,utteranceId==%@",text,utteranceId);
}

// 当前播放的字符,当前播放的字符在所在的句子中的下标.
// currentWord 当前读到的单个字，是一个估算值不一定准确
// currentIdex 当前播放句子中读到文字的下标
-(void)onTTSPlayProgressWithCurrentWord:(NSString*_Nullable)currentWord CurrentIndex:(NSInteger)currentIdex{
    NSLog(@"CurrentWord==%@,currentIdex==%@",currentWord,@(currentIdex));
}


```

#### 播放器入参

| 参数               | 说明                             |
| ------------------ | -------------------------------- |
| data               | 入参音频流，通过传入字节数组播放 |
| url                | 入参音频文件，通过传入文件播放   |
| String text        | 音频对应的文本                   |
| String utteranceId | 文本 ID                            |

**示例**

```java
//通过音频数据入参
QCPlayerError err = [_player enqueueWithData:data Text:text UtteranceId:utteranceId];

//通过音频文件入参
 NSString *str = [self filePathWithName:@"tmp.mp3"];
 NSURL * url = [NSURL URLWithString:str];
QCPlayerError err = [_player enqueueWithFile:url Text:text UtteranceId:utteranceId];
```

### 客户端错误码

| ID   | 错误码                                | 说明                                             |
| ---- | ------------------------------------- | ------------------------------------------------ |
| -100 | TTS_ERROR_CODE_UNINITIALIZED          | SDK 未初始化                                      |
| -101 | TTS_ERROR_CODE_GENERATE_SIGN_FAIL     | 签名失败                                         |
| -102 | TTS_ERROR_CODE_NETWORK_CONNECT_FAILED | 网络异常                                         |
| -103 | TTS_ERROR_CODE_DECODE_FAIL            | Response 解析失败                                 |
| -104 | TTS_ERROR_CODE_SERVER_RESPONSE_ERROR  | 后端返回失败错误码，详细错误信息请查看后端错误码 |
| -105 | TTS_ERROR_CODE_QUEUE_IS_FULL          | 合成队列已满                                     |
| -106 | TTS_ERROR_CODE_CANCEL_FAILURE         | 取消失败，请稍后重试                             |
| -900 | TTS_ERROR_CODE_OFFLINE_NOSUPPORT      | 当前 SDK 不支持离线合成能力，请使用 TtsMode.ONLINE  |


### 服务端错误码
请参考 [语音合成 API 文档](https://cloud.tencent.com/document/product/1073/37995)。

 
