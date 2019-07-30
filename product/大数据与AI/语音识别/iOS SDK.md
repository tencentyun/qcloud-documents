
## 开发准备

### SDK 获取

一句话识别的 iOS SDK 以及 Demo 的下载地址：[QCloud SDK](https://main.qcloudimg.com/raw/777564552ff9e038b613f8cb96570a2d/QCloudSDK_v2.0.3.zip)。


### 使用须知

+ QCloudSDK 支持 **iOS 9.0** 及以上版本。
+ 一句话识别，需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等）。
+ 从控制台获取 AppID、SecretID、SecretKey、ProjectId 详情参考 [基本概念](https://cloud.tencent.com/document/product/441/6194)。
+ 运行 Demo 必须设置 AppID、SecretID、SecretKey、ProjectId.
+ 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。

### SDK 导入

iOS SDK 压缩包名称为： QCloudSDK_v2.0.3.zip，压缩包中包含 Sample Code 和 QCloudSDK。

### 工程配置

在工程` info.plist` 添加以下设置：
1. **设置 NSAppTransportSecurity 策略，添加如下内容：**
```objective-c
  <key>NSAppTransportSecurity</key>
  <dict>
	<key>NSExceptionDomains</key>
	<dict>
		<key>qcloud.com</key>
		<dict>
			<key>NSExceptionAllowsInsecureHTTPLoads</key>
			<true/>
			<key>NSExceptionMinimumTLSVersion</key>
			<string>TLSv1.2</string>
			<key>NSIncludesSubdomains</key>
			<true/>
			<key>NSRequiresCertificateTransparency</key>
			<false/>
		</dict>
	</dict>
    </dict>
```
2. **申请系统麦克风权限，添加如下内容：**
```objective-c
   <key>NSMicrophoneUsageDescription</key>
   <string>需要使用了的麦克风采集音频</string>
```
3. **在工程中添加依赖库，在 build Phases Link Binary With Libraries 中添加以下库：**
   + AVFoundation.framework
   + AudioToolbox.framework
   + QCloudSDK.framework
   + CoreTelephony.framework
   + libWXVoiceSpeex.a

添加完如图所示。
![](https://main.qcloudimg.com/raw/17ff6f4f4a27e0843de528eb070c2f32.png)

### 类说明
**QCloudSentenceRecognizer 初始化说明**
**QCloudSentenceRecognizer** 是一句话识别入口类，提供两种初始化方法。
```objective-c
/**
 * 初始化方法，调用者使用内置录音器采集音频
 * @param config 配置参数，详见QCloudConfig定义
 */
- (instancetype)initWithConfig:(QCloudConfig *)config;
/**
 * 通过appId secretId secretKey初始化
 * @param appid     腾讯云appId        基本概念见https://cloud.tencent.com/document/product/441/6194
 * @param secretId  腾讯云secretId     基本概念见https://cloud.tencent.com/document/product/441/6194
 * @param secretKey 腾讯云secretKey    基本概念见https://cloud.tencent.com/document/product/441/6194
 */
- (instancetype)initWithAppId:(NSString *)appid secretId:(NSString *)secretId secretKey:(NSString *)secretKey;
```
**QCloudConfig 初始化方法说明**
腾讯云 AppId，腾讯云 secretId，腾讯云 secretKey，腾讯云 projectId 从控制台获取，[基本概念](https://cloud.tencent.com/document/product/441/6194) 。
```objective-c
/**
 * 初始化方法
 * @param appid     腾讯云appId 
 * @param secretId  腾讯云secretId
 * @param secretKey 腾讯云secretKey
 * @param projectId 腾讯云projectId
 */
- (instancetype)initWithAppId:(NSString *)appid
                     secretId:(NSString *)secretId
                    secretKey:(NSString *)secretKey
                    projectId:(NSString *)projectId;
```
**QCloudSentenceRecognizerDelegate 说明**
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
 * @param volume 声音音量，取值范围（-40-0)
 */
- (void)oneSentenceRecognizerDidUpdateVolume:(QCloudSentenceRecognizer *)recognizer volume:(float)volume;
@end
```
### 示例
1）**创建 QCloudSentenceRecognizer 实例** 

```objective-c
  QCloudSentenceRecognizer *recognizer = [[QCloudSentenceRecognizer alloc] initWithAppId:appId 
  									        secretId:secretId 
									       secretKey:secretKey];
  //设置delegate，相关回调方法见QCloudOneSentenceRecognizerDelegate定义
 recognizer.delegate = self;
```
2）**实现此 QCloudSentenceRecognizerDelegate 协议方法**
3）**调用示例**
**a. 通过语音 URL 调用**
```objective-c
- (void)recognizeWithUrl {
//语音数据url
NSString *url = @"http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav";
  //指定语音数据url 语音数据格式 采样率
  [_recognizer recoginizeWithUrl:url voiceFormat:kQCloudVoiceFormatWAV frequence:kQCloudEngSerViceType16k];
}
```
**b. 通过语音数据调用**
```objective-c
- (void)recognizeWithAudioData {
   //语音数据
   NSString *filePath = [[NSBundle mainBundle] pathForResource:@"recordedFile" ofType:@"wav"];
   NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
   //指定语音数据 语音数据格式 采样率
   [_recognizer recoginizeWithData:audioData voiceFormat:kQCloudVoiceFormatWAV frequence:kQCloudEngSerViceType16k];
}
```
**c. 通过指定参数调用**
```objective-c
- (void)recognizeWithParams {
   NSString *url = @"http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav";
   //获取一个已设置默认参数params
   QCloudOneSentenceRecognitionParams *params = [_recognizer defaultRecognitionParams];    
   //通过语音url请求, 此4个参数必须设置
   params.url = url;                           
   //设置语音频数据格式，见kQCloudVoiceFormat定义
   params.voiceFormat = kQCloudVoiceFormatWAV;
   //设置语音数据来源，见QCloudAudioSourceType定义
   params.sourceType = QCloudAudioSourceTypeUrl;
   //设置采样率，见kQCloudEngSerViceType定义
   params.engSerViceType = kQCloudEngSerViceType16k; 
   [_recognizer recognizeWithParams:params];
}
```
**d. 通过 SDK 内置录音器调用**
```objective-c
- (void)recognizeWithRecorder {
   [_recognizer startRecognizeWithRecorder];
}
```
