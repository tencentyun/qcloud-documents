iOS SDK 接入请观看视频：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-20714?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 接入准备
### SDK 获取
一句话识别的 iOS SDK 以及 Demo 的下载地址：[iOS SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_IOS_v2.6.4.zip)。

### 接入须知
- 开发者在调用前请先查看实时语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的**使用要求**和**使用步骤**。
- 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等），且系统为 **iOS 9.0**及以上版本。

### 开发环境
在工程` info.plist` 添加以下设置：
+ **设置 NSAppTransportSecurity 策略，添加如下内容：**
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
+ **申请系统麦克风权限，添加如下内容：**
```objective-c
   <key>NSMicrophoneUsageDescription</key>
   <string>需要使用您的麦克风采集音频</string>
```
+ **在工程中添加依赖库，在建阶段链接二进制与库中添加以下库：**
  + AVFoundation.framework
  + AudioToolbox.framework
  + QCloudSDK.framework
  + CoreTelephony.framework
  + libWXVoiceSpeex.a

添加完如下图所示：
![](https://main.qcloudimg.com/raw/17ff6f4f4a27e0843de528eb070c2f32.png)

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
 + **通过语音 URL 调用**
```objective-c
- (void)recognizeWithUrl {
//语音数据url
NSString *url = @"https://asr-audio-1256237915.cos.ap-shanghai.myqcloud.com/30s.wav";
  //指定语音数据url 语音数据格式 采样率
  [_recognizer recoginizeWithUrl:url voiceFormat:kQCloudVoiceFormatWAV frequence:kQCloudEngSerViceType16k];
}
```
 + **通过语音数据调用**
```objective-c
- (void)recognizeWithAudioData {
   //语音数据
   NSString *filePath = [[NSBundle mainBundle] pathForResource:@"recordedFile" ofType:@"wav"];
   NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
   //指定语音数据 语音数据格式 采样率
   [_recognizer recoginizeWithData:audioData voiceFormat:kQCloudVoiceFormatWAV frequence:kQCloudEngSerViceType16k];
}
```
 + **通过指定参数调用**
```objective-c
- (void)recognizeWithParams {
   NSString *url = @"https://asr-audio-1256237915.cos.ap-shanghai.myqcloud.com/30s.wav";
   //获取一个已设置默认参数params
   QCloudOneSentenceRecognitionParams *params = [_recognizer defaultRecognitionParams];    
   //通过语音 url 请求, 此4个参数必须设置
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
 - **通过 SDK 内置录音器调用**
```objective-c
- (void)recognizeWithRecorder {
   [_recognizer startRecognizeWithRecorder];
}
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
@end
```

