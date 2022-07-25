## 开发准备  
### SDK 获取
录音文件识别的 iOS SDK 以及 Demo 的下载地址：[接入 SDK 下载](https://console.cloud.tencent.com/asr/download)。

### 使用须知
- SDK 支持 **iOS 9.0** 及以上版本。
- 录音文件识别，需要手机能够连接网络（3G、4G 或 Wi-Fi 网络等）。
- 运行 Demo 必须设置 AppID、SecretID、SecretKey，可在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取。

### SDK 导入
1. 下载并解压 iOS SDK 压缩包，压缩包中包含 Demo 和 SDK, 其中QCloudFileRecognizer.framework为录音文件识别极速版framework包。
2. XcodeFile > Add Files to "Your Project"，在弹出 Panel 选中所下载SDK包QCloudFileRecognizer.framework > Add（选中“Copy items if needed”）。


### 工程配置
**在工程中添加依赖库，在 build Phases Link Binary With Libraries 中添加以下库：**
- QCloudFileRecognizer.framework
- libc++.tbd
- AVFoundation.framework
- AudioToolbox.framework

### 类说明
#### QCloudFlashFileRecognizer 初始化说明
**QCloudFlashFileRecognizer** 是录音文件极速版入口类。
```objective-c
/**
  通过 appId secretId secretKey 初始化
  @param appid     腾讯云 appId
  @param secretId  腾讯云 secretId
  @param secretKey 腾讯云 secretKey
 **/
- (instancetype)initWithAppId:(NSString *)appid secretId:(NSString *)secretId secretKey:(NSString *)secretKey;

/** 
  通过 appId 临时secretId 临时secretKey token 初始化 
  详见 https://cloud.tencent.com/document/product/598/33416
  @param appid     腾讯云 appId
  @param secretId  腾讯云 临时secretId
  @param secretKey 腾讯云 临时secretKey
  @param token 腾讯云 token
 **/
- (instancetype)initWithAppId:(NSString *)appid secretId:(NSString *)secretId secretKey:(NSString *)secretKey token:(NSString *)token;
```

[](id:QCloudFlashFileRecognizerDelegate)
#### QCloudFlashFileRecognizerDelegate 协议说明
此 delegate 为录音文件识别相关回调，调用者需要实现此 delegate 获取识别结果事件。
```objective-c
@protocol QCloudFlashFileRecognizerDelegate <NSObject>
@optional

/**
 录音文件识别获取服务器结果成功回调

@param recognizer 录音文件识别器
 @param status 非0时识别失败
 @param text 识别文本，status非0时，此为服务器端返回的错误信息
 @param resultData 原始数据
 */
- (void)FlashFileRecognizer:(QCloudFlashFileRecognizer *_Nullable)recognizer status:(nullable NSInteger *) status text:(nullable NSString *)text resultData:(nullable NSDictionary *)resultData;

/**
 录音文件识别失败回调
 @param recognizer 录音文件识别器
 @param error 识别错误，出现错误此字段有
 @param resultData 原始数据
 */
- (void)FlashFileRecognizer:(QCloudFlashFileRecognizer *_Nullable)recognizer error:(nullable NSError *)error resultData:(nullable NSDictionary *)resultData;

/**
 * 日志输出
 * @param log 日志
 */
- (void)FlashFileRecgnizerLogOutPutWithLog:(NSString *_Nullable)log;

@end
```

## 示例
1. **创建 QCloudFlashFileRecognizer 实例** 
```objective-c
  QCloudFlashFileRecognizer *recognizer = [[QCloudFlashFileRecognizer alloc] initWithAppId:appId 
  								        secretId:secretId secretKey:secretKey];
  //设置 delegate，相关回调方法见 QCloudFlashFileRecognizerDelegate 定义
 recognizer.delegate = self;
```
2. **实现此 [QCloudFlashFileRecognizerDelegate](#QCloudFlashFileRecognizerDelegate) 协议方法**
3. **调用方式示例**
```objective-c
 (void)recognizeWithAudioData {
    QCloudFlashFileRecognizeParams *params = [QCloudFlashFileRecognizeParams defaultRequestParams];
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"test" ofType:@"mp3"];
    NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
    params.audioData = audioData;
    //音频格式。支持 wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac。
    params.voiceFormat = @"mp3";
    
    //以下参数不设置将使用默认值
    params.engineModelType = @"16k_zh";//引擎模型类型,默认16k_zh。8k_zh：8k 中文普通话通用；16k_zh：16k 中文普通话通用；16k_zh_video：16k 音视频领域。
    params.filterDirty = 0;;// 0 ：默认状态 不过滤脏话 1：过滤脏话
    params.filterModal = 0;// 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
    params.filterPunc = 0;// 0 ：默认状态 不过滤句末的句号 1：滤句末的句号
    params.convertNumMode = 1;;//1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
    params.speakerDiarization = 0; //是否开启说话人分离（目前支持中文普通话引擎），默认为0，0：不开启，1：开启。
    params.firstChannelOnly = 1; //是否只识别首个声道，默认为1。0：识别所有声道；1：识别首个声道。
    params.wordInfo = 0; //是否显示词级别时间戳，默认为0。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。
    
    
    [_recognizer recognize:params];
}
```
