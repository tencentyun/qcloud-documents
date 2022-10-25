>? 当前文档适用于 V1.5.1版本及以下 SDK。建议正在使用旧版 SDK 的客户及时升级到 [新版 SDK](https://cloud.tencent.com/document/product/1073/80488)，以获取更好的使用体验。
## 开发相关
### 开发准备
- 支持 iOS 8.0 及以上版本，不支持 bitcode 版本。
- 合成实时流式语音，需要手机能够连接网络（3/4/5G 或 Wi-Fi 网络等）。
- 语音合成 [iOS SDK ](https://console.cloud.tencent.com/tts/download)。
- 服务端 [API 文档](https://cloud.tencent.com/document/product/1073/37995)。

### 导入 SDK
Frameworks 文件夹内的 QCloudTTS_SDK.framework 即为 SDK，引入 `<QCloudTTS_SDK/QCloudTTS.h>` 即可调用 SDK 相关接口。

### 参数说明

| 参数名称  | 类型      | 必填 | 说明                                                         |
| --------- | --------- | ---- | ------------------------------------------------------------ |
| appId     | NSInteger | 是   | 腾讯云 ID，即 AppID，[获取地址](https://console.cloud.tencent.com/developer) |
| secretId  | NSString  | 是   | 腾讯云安全凭证，[获取地址](https://console.cloud.tencent.com/cam/capi) |
| secretKey | NSString  | 是   | 腾讯云安全凭证，获取地址同上                                 |
| sessionId | NSString  | 否   | 一次请求对应一个 SessionId，会原样返回                       |
| projectId | NSString  | 否   | 项目 ID，用户自定义，默认为0，[获取地址](https://console.cloud.tencent.com/project) |
| speed     | NSInteger | 否   | 语速，范围：[-2，2]，分别对应不同语速：0.6倍、0.8倍、1.0倍、1.2倍、1.5倍，默认为0 |
| voiceType | NSInteger | 否   | tts 音色                                                     |
| language  | NSInteger | 否   | 主语言类型，默认中文                                         |


## 快速入门
### 初始化 QCloudTTS 并注册 QCloudTTSDelegate
```
QCloudTTS * apiObj = [[QCloudTTS alloc] initWithAppId:appId secretId:secretId secretKey:secretKey];
apiObj.ttsDelegate = self;
```

### 设置自定义参数 QCloudTTSConfig
#### TTS 音色类型
```
// 更多音色id可查看官网文档https://cloud.tencent.com/document/product/1073/37995
typedef NS_ENUM(NSUInteger, VoiceType) {
    VoiceTypeZhiYu            = 1001,   // 1001：智瑜，情感女声
    VoiceTypeZhiYun           = 1004,   // 1004：智云，通用男声
    VoiceTypeZhiLing          = 1002,   // 1002：智聆，通用女声
    VoiceTypeZhiMei           = 1003,   // 1003：智美，客服女声
    VoiceTypeWeJack           = 1050,   // 1050：WeJack，英文男声
    VoiceTypeWeRose           = 1051,   // 1051：WeRose，英文女声
    VoiceTypeXiaoYao          = 10510000,//智逍遥，阅读男声
};
```

#### TTS 语速
```
typedef NS_ENUM(NSInteger, SpeedType) {
SpeedTypeVerySlow     = -2,   // 0.6 倍
SpeedTypeSlowDown     = -1,   // 0.8 倍
SpeedTypeNormal       = 0,    // 1.0 倍（默认）
SpeedTypeAccelerate   = 1,    // 1.2 倍
SpeedTypeVeryFast     = 2,    // 1.5 倍
};
```

#### TTS 主语言类型

```
typedef NS_ENUM(NSUInteger, PrimaryLanguage) {
PrimaryChinese    = 1,   // 1：中文（默认）
PrimaryEnglish    = 2,   // 2：英文
};
```

#### 示例

```
QCloudTTSConfig *config = [QCloudTTSConfig getInstance];
config.projectId = 1234567;
config.volume = VolumeLevelOne;
config.speed = SpeedTypeNormal;
config.voiceType = VoiceTypeZhiYu;
config.language = PrimaryChinese;
```

### 监听 QCloudTTSDelegate 播放状态

```
//开始播放
- (void) onTTSPlayStart{
		NSLog(@"onTTSPlayStart");
}

//音频缓冲中
- (void) onTTSPlayWait{
		NSLog(@"onTTSPlayWait");
}

//缓冲完成，继续播放
- (void) onTTSPlayContinue{
		NSLog(@"onTTSPlayContinue");
}

//播放中止
- (void) onTTSPlayStop{
		 NSLog(@"onTTSPlayStop");
}

//播放结束
- (void) onTTSPlayEnd{
		NSLog(@"onTTSPlayEnd");
}

//返回当前播放的音频文件
- (void) onTTSAudioData:(NSData *_Nonnull)data;


// @param sentence 当前播放的句子
// @param seq 当前播放的句子在句子集合中的序号
- (void) onTTSPlayProgressWithCurrentSentence:(NSString *_Nonnull)sentence Seq:(NSInteger )seq;

```

### 语音合成

语音合成有两个接口，基于基础语音合成接口封装，支持不限字数长文本入参，SDK内部会将文本切分为短句多次请求合成，也支持入参切分好的句子集合  ，支持播放暂停与恢复，适合实时播放场景。

合成接口1：直接入参文本段落，使用 SDK 内部的规则切分文本，如果 sdk 的切分规则不符合您的业务需求，您可以选用合成接口2。

合成接口2：入参切分好的句子集合，您需要确保列表内每句话长度不超过后端接口最大字符限制，建议文本中第一句话不要设的太长， demo 工程内附带了一份文本切分示例代码。长度限制详见 [语音合成 API 文档](https://cloud.tencent.com/document/product/1073/37995)。

>! 如果要使用 SSML 标记语言，请选择使用合成接口2，并确保入参列表中每一个元素不能超过150中文字符（不包括 SSML 标签）。如果选择合成接口1，入参 SSML 标签会被切分导致 SSML 标签无效，具体使用可以参考 demo，SSML 语法详见 [SSML 标记语言](https://cloud.tencent.com/document/product/1073/49575)。
>
```
合成接口1：直接入参文本段落:
(BOOL)startTTS:(NSString * )text fail:(TTSExceptionHandler)fail;
//可以通过这个接口获取内部切分好的句子集合
//NSArray<NSString *> * SentencesArray = [_qcloudTTSObj getSentencesArray];

合成接口2：入参切分好的句子集合:
- (BOOL)startTTSArray:(NSArray<NSString *>*)sentencesArray fail:(TTSExceptionHandler)fail;
```

#### 示例
在使用云 API 之前，请前往 [腾讯云 API 密钥](https://console.cloud.tencent.com/cam/capi) 申请安全凭证。安全凭证包括 SecretId 和 SecretKey。
```
SecretId 用于标识 API 调用者身份。
SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。
```
>!这里只是示例，请根据用户实际申请的 SecretId 和 SecretKey 进行后续操作。

```
NSInteger appId = 1257709062;                                   //腾讯云 AppId
NSString *secretId = @“AKIDzlIbgVXMPC*****QaT6TZOwDF1WktQr4”;   //腾讯云 secretId
NSString *secretKey = @“6xYsxngLo45sT*****ORFuMZZLs9BzXt”;      //腾讯云 secretKey

 //直接鉴权
QCloudTTS* _apiObj = [[QCloudTTS alloc] initWithAppId:appId secretId:secretId secretKey:secretKey];

 //也可以使用临时密钥鉴权
  /* 1.通过sts 获取到临时证书 ,此步骤应在您的服务器端实现，见https://cloud.tencent.com/document/product/598/33416
    2.通过临时密钥调用接口
     QCloudTTS* _apiObj = [[QCloudTTS alloc] initWithAppId:appId secretId:@"填入临时SecretId" secretKey:@"填入临时SecretKey" token:@"对应的token"];
 */

_apiObj.ttsDelegate = self;
[apiObj startTTS:ttsText fail:^(NSString *code, NSString *errMsg) {
//接口异常处理NSLog(@“error:%@”,errMsg);
}];
```

### 暂停、恢复或停止语音播放
```
[apiObj pauseTTS];
[apiObj resumeTTS];
[apiObj stopTTS];
```

### 错误码
请参考 [语音合成 API 文档](https://cloud.tencent.com/document/product/1073/37995)。
