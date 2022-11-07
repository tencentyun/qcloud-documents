## 接入准备
### SDK 获取
一句话识别的 iOS SDK 以及 Demo 的下载地址：[接入 SDK 下载](https://console.cloud.tencent.com/asr/download)。

### 接入须知
- 开发者在调用前请先查看实时语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的**使用要求**和**使用步骤**。
- 该接口需要手机能够连接网络（3G、4G 或 Wi-Fi 网络等），且系统为 **iOS 9.0**及以上版本。

### SDK 导入
1. 下载并解压 iOS SDK 压缩包，压缩包中包含 Demo 和 SDK,其中QCloudOneSentence.framework为一句话识别framework包。
2. XcodeFile > Add Files to "Your Project"，在弹出 Panel 选中所下载SDK包 QCloudOneSentence.framework > Add（选中“Copy items if needed”）。

### 工程配置
**在工程` info.plist`申请系统麦克风权限，添加如下内容：**

```objective-c
   <key>NSMicrophoneUsageDescription</key>
   <string>需要使用您的麦克风采集音频</string>
```
**在工程中添加依赖库，在建阶段链接二进制与库中添加以下库：**
- QCloudOneSentence.framework
- libc++.tbd
- AVFoundation.framework
- AudioToolbox.framework
    
## 快速接入
### 开发流程及接入示例
1. **创建 QCloudSentenceRecognizer 实例** 
```objective-c
  QCloudSentenceRecognizer *recognizer = [[QCloudSentenceRecognizer alloc] initWithAppId:appId 
  									        secretId:secretId 
									          secretKey:secretKey];
  //设置delegate，相关回调方法见QCloudOneSentenceRecognizerDelegate定义
 recognizer.delegate = self;
```
2. **实现此 [QCloudSentenceRecognizerDelegate](#QCloudSentenceRecognizerDelegate) 协议方法**
3. **调用示例**
	- **通过语音 URL 调用**
>? 支持8K 和16K 的引擎类型，引擎模型类型请参见 [EngSerViceType](https://cloud.tencent.com/document/product/1093/35646#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)。
>
```objective-c
//快捷接口
- (void)recognizeWithUrl {
//语音数据url
NSString *url = @"https://asr-audio-1256237915.cos.ap-shanghai.myqcloud.com/30s.wav";
  //指定语音数据url 语音数据格式 识别引擎
  //支持的格式及引擎名称以API文档为准，见https://cloud.tencent.com/document/product/1093/35646
  [_recognizer recoginizeWithUrl:url voiceFormat:@"wav" EngSerViceType:@"16k_zh"];
}

//完整接口，可设置更多参数
- (void)recognizeWithParams {
   NSString *url = @"https://asr-audio-1256237915.cos.ap-shanghai.myqcloud.com/30s.wav";
   //获取一个已设置默认参数params
   QCloudOneSentenceRecognitionParams *params = [_recognizer defaultRecognitionParams];    
   //通过语音 url 请求, 此4个参数必须设置
   params.url = url;                           
   //设置语音频数据格式，支持的格式以API文档为准，见https://cloud.tencent.com/document/product/1093/35646
   params.voiceFormat = @"wav";
   //设置语音数据来源，见QCloudAudioSourceType定义
   params.sourceType = QCloudAudioSourceTypeUrl;
   //设置识别引擎,支持的识别引擎以API文档为准，见https://cloud.tencent.com/document/product/1093/35646
   params.engSerViceType = @"16k_zh"; 
  
   //以下为可选项
    //是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。
    params.filterDirty = 0;
    //是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
    params.filterModal = 0;
    //是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
    params.filterPunc = 0;
    //是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。
    params.convertNumMode = 1;
    //是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认值为 0。
    params.wordInfo = 1;
    //params.hotwordId = @"" //热词id
  
   [_recognizer recognizeWithParams:params];
}
```
	- **通过语音数据调用**
>? 支持8K 和16K 的引擎类型，引擎模型类型请参见 [EngSerViceType](https://cloud.tencent.com/document/product/1093/35646#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)。
>
```objective-c
//快捷接口
- (void)recognizeWithAudioData {
   //语音数据
   NSString *filePath = [[NSBundle mainBundle] pathForResource:@"recordedFile" ofType:@"wav"];
   NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
   //指定语音数据 语音数据格式 识别引擎
   //支持的格式以API文档为准，见https://cloud.tencent.com/document/product/1093/48982
   [_recognizer recoginizeWithData:audioData voiceFormat:@"wav" frequence:@"16k_zh"];
}

//完整接口，可设置更多参数
- (void)recognizeWithParams {

    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"test2" ofType:@"mp3"];
    NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
  
    //获取一个已设置默认参数params
    QCloudOneSentenceRecognitionParams *params = [_recognizer defaultRecognitionParams];    
    //通过语音数据发起请求, 此4个参数必须设置
    params.data = audioData;
    //设置语音频数据格式，支持的格式以API文档为准，见https://cloud.tencent.com/document/product/1093/35646
    params.voiceFormat = @"mp3";
    //设置语音数据来源，QCloudAudioSourceTypeUrl 或 QCloudAudioSourceTypeAudioData
    params.sourceType = QCloudAudioSourceTypeAudioData; 
    //设置识别引擎,支持的识别引擎以API文档为准，见https://cloud.tencent.com/document/product/1093/35646
    params.engSerViceType = @"16k_zh"; 
  
   //以下为可选项
    //是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。
    params.filterDirty = 0;
    //是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。
    params.filterModal = 0;
    //是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认值为 0。
    params.filterPunc = 0;
    //是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。
    params.convertNumMode = 1;
    //是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。默认值为 0。
    params.wordInfo = 1;
    //params.hotwordId = @"" //热词id
  
   [_recognizer recognizeWithParams:params];
}
```
 - **通过 SDK 内置录音器调用**
>? 支持16K 的引擎类型，引擎模型类型请参见 [EngSerViceType](https://cloud.tencent.com/document/product/1093/35646#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)。
>
```objective-c
//启动录音
  [_recognizer startRecognizeWithRecorder:@"16k_zh"];  //16k_zh > 识别引擎,传nil将默认使用16k_zh,支持的识别引擎以API文档为准，见https://cloud.tencent.com/document/product/1093/35646

//停止录音并上传录音数据开始识别
  [_recognizer stopRecognizeWithRecorder];
```

### 主要接口类说明
#### QCloudSentenceRecognizer 初始化说明
QCloudSentenceRecognizer 是一句话识别入口类，提供两种初始化方法。
```objective-c
/**
 * 初始化方法，调用者使用内置录音器采集音频
 * @param config 配置参数，详见 QCloudConfig 定义
 */
- (instancetype)initWithConfig:(QCloudConfig *)config;

/**
 * 直接鉴权
 * 通过 appId secretId secretKey 初始化
 * @param appid     腾讯云 appId        
 * @param secretId  腾讯云 secretId     
 * @param secretKey 腾讯云 secretKey    
 */
- (instancetype)initWithAppId:(NSString *)appid secretId:(NSString *)secretId secretKey:(NSString *)secretKey;

/**
 * 通过STS临时密钥鉴权，详见https://cloud.tencent.com/document/product/598/33416
 * @param appid     腾讯云appId 
 * @param secretId  腾讯云临时secretId  
 * @param secretKey 腾讯云临时secretKey
 * @param token     对应的token
 */
- (instancetype)initWithAppId:(NSString *)appid secretId:(NSString *)secretId secretKey:(NSString *)secretKey token:(NSString *)token;
```

[](id:QCloudSentenceRecognizerDelegate)
#### QCloudSentenceRecognizerDelegate 协议说明
此 delegate 为一句话识别相关回调，调用者需要实现此 delegate 获取识别结果、开始录音、结束录音事件。
```objective-c
@protocol QCloudSentenceRecognizerDelegate <NSObject>
@required
/**
 * 一句话识别回调delegate
 * @param result 识别结果文本，error=nil此字段才存在值
 * @param error 错误信息，详细错误信息见error.domain和error.userInfo字段
 * @param rawData 识别原始数据
 */
- (void)oneSentenceRecognizerDidRecognize:(QCloudSentenceRecognizer *)recognizer text:(nullable NSString *)text error:(nullable NSError *)error resultData:(nullable NSDictionary *)resultData;
@optional
/**
 * 开始录音回调
 */
- (void)oneSentenceRecognizerDidStartRecord:(QCloudSentenceRecognizer *)recognizer error:(nullable NSError *)error;
/**
 * 结束录音回调, SDK通过此方法回调后内部开始上报语音数据进行识别
 */
- (void)oneSentenceRecognizerDidEndRecord:(QCloudSentenceRecognizer *)recognizer;
/**
 * 录音音量实时回调用
 * @param recognizer 识别器实例
 * @param volume 声音音量，取值范围（-40-0）
 */
- (void)oneSentenceRecognizerDidUpdateVolume:(QCloudSentenceRecognizer *)recognizer volume:(float)volume;
/**
 * 日志输出
 * @param log 日志
 */
- (void)SentenceRecgnizerLogOutPutWithLog:(NSString *_Nullable)log;

@end
```
