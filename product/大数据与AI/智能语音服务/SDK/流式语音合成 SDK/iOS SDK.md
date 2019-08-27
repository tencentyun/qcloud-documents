## 开发相关


### 开发准备
- 支持 iOS 8.0 及以上版本，不支持 bitcode 版本。
- 合成实时流式语音，需要手机能够连接网络（2/3/4G 或 Wi-Fi 网络等）。
- 语音合成 iOS SDK [下载地址](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/tts_sdk_ios_v2.zip)。
- 腾讯云控制台获取 AppID、SecretID、SecretKey，详情参考 [基本概念](https://cloud.tencent.com/document/product/441/6194)。
- 服务端 [API 文档](https://cloud.tencent.com/document/api/441/18086)。

### 导入 SDK
iOS SDK 文件夹名称为： QCloud_TTS。其中包含一个 .a 静态库和一个头文件夹 header。

 ### 配置工程
- 在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。
- 在工程中添加依赖库，在 build Phases Link Binary Whith Libraries 中添加以下库：libc++.tbd

### 初始化
引入上传 SDK 中的头文件 QCloudTTS.h，需要先实例化 QCloudTTS 对象。

### 参数说明

| 参数名称  | 类型      | 必填 | 说明|
| --------- | --------- | ---- | ---------- |
| appId     | NSInteger | 是   | 腾讯云 ID，即 AppID ，[获取地址](https://console.cloud.tencent.com/developer)   |
| secretId  | NSString  | 是   | 腾讯云安全凭证，[获取地址](https://console.cloud.tencent.com/cam/capi)            |
| secretKey | NSString  | 是   | 腾讯云安全凭证，获取地址同上  |
| sessionId | NSString  | 否   | 一次请求对应一个 SessionId，会原样返回 |
| projectId | NSString  | 否   | 项目 ID，用户自定义，默认为 0 ，[获取地址](https://console.cloud.tencent.com/project)                              |
| speed     | NSInteger | 否   | 语速，范围：[-2，2]，分别对应不同语速：0.6倍、0.8倍、1.0倍、1.2倍、1.5倍，默认为 0 |
| voiceType | NSInteger | 否   | tts音色，默认女声，亲和风格  |
| language  | NSInteger | 否   | 主语言类型，默认中文 |


## 快速入门

### 初始化 QCloudTTS 并注册 QCloudTTSDelegate

```
QCloudTTS * apiObj = [[QCloudTTS alloc] initWithAppId:appId secretId:secretId secretKey:secretKey]];
apiObj.ttsDelegate = self;
```

### 设置自定义参数 QCloudTTSConfig

**TTS音色类型**
```
typedef NS_ENUM(NSUInteger, VoiceType) {
VoiceTypeAffinityFemale   = 0,   // 0：亲和女声（默认）
VoiceTypeAffinityMale     = 1,   // 1：亲和男声
VoiceTypeMatureMale       = 2,   // 2：成熟男声
VoiceTypeVibrantMale      = 3,   // 3：活力男声
VoiceTypeWarmFemale       = 4,   // 4：温暖女声
VoiceTypeEmotionalFemale  = 5,   // 5：情感女声
VoiceTypeEmotionalMale    = 6,   // 6：情感男声
};
```

**TTS语速**
```
typedef NS_ENUM(NSInteger, SpeedType) {
SpeedTypeVerySlow     = -2,   // 0.6 倍
SpeedTypeSlowDown     = -1,   // 0.8 倍
SpeedTypeNormal       = 0,    // 1.0 倍（默认）
SpeedTypeAccelerate   = 1,    // 1.2 倍
SpeedTypeVeryFast     = 2,    // 1.5 倍
};
```
 
**TTS主语言类型**
```
typedef NS_ENUM(NSUInteger, PrimaryLanguage) {
PrimaryChinese    = 1,   // 1：中文（默认）
PrimaryEnglish    = 2,   // 2：英文
};
```
**示例**
```
QCloudTTSConfig *config = [QCloudTTSConfig getInstance];
config.projectId = 1234567;
config.volume = VolumeLevelOne;
config.speed = SpeedTypeNormal;
config.voiceType = VoiceTypeFemale;
config.language = PrimaryChinese;
```
### 监听 QCloudTTSDelegate 播放状态**

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
```
### 语音合成

```
(BOOL)startTTS:(NSString * )text fail:(TTSExceptionHandler)fail;
```

**示例**
在使用云API之前，请前往 腾讯云API密钥页面 申请安全凭证。 安全凭证包括 SecretId 和 SecretKey 。
```
SecretId 用于标识 API 调用者身份。
SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。
```

>!这里只是示例，请根据用户实际申请的 SecretId 和 SecretKey 进行后续操作。

```
NSInteger appId = 1257709062;                                   //腾讯云 appId
NSString *secretId = @“AKIDzlIbgVXMPC*****QaT6TZOwDF1WktQr4”;   //腾讯云 secretId
NSString *secretKey = @“6xYsxngLo45sT*****ORFuMZZLs9BzXt”;      //腾讯云 secretKey

QCloudTTS* _apiObj = [[QCloudTTS alloc] initWithAppId:appId secretId:secretId secretKey:secretKey];_

apiObj.ttsDelegate = self;
[apiObj startTTS:ttsText fail:^(NSString *code, NSString *errMsg) {
	//接口异常处理
	NSLog(@“error:%@”,errMsg);
}];
```
### 暂停、恢复或停止语音播放
```
[apiObj pauseTTS];

[apiObj resumeTTS];

[apiObj stopTTS];
```


### 错误码
请参考 [语音合成 API 文档](https://cloud.tencent.com/document/api/441/18086)。


