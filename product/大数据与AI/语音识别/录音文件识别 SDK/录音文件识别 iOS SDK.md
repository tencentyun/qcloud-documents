iOS SDK 接入请观看视频： 

<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-12774?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 开发准备  

### SDK 获取

录音文件识别的 iOS SDK 以及 Demo 的下载地址：[QCloud SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_IOS_v2.6.4.zip)。

### 使用须知

- QCloudSDK 支持 **iOS 9.0** 及以上版本。
- 录音文件识别，需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等）。
- 运行 Demo 必须设置 AppID、SecretID、SecretKey、ProjectId，可在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取。

### SDK 导入

下载并解压 iOS SDK 压缩包，压缩包中包含 Sample Code 和 QCloudSDK。

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
   <string>需要使用您的麦克风采集音频</string>
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

#### QCloudFileRecognizer 初始化说明

**QCloudFileRecognizer** 是录音文件识别入口类，提供两种初始化方法。

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

[](id:QCloudFileRecognizerDelegate)

#### QCloudFileRecognizerDelegate 协议说明

此 delegate 为录音文件识别相关回调，调用者需要实现此 delegate 获取识别结果、开始录音、结束录音事件。

```objective-c
@protocol QCloudFileRecognizerDelegate <NSObject>
@optional

/**
 录音文件识别成功回调

 @param recognizer 录音文件识别器
 @param requestId 请求唯一标识 requestId，recognize：接口返回
 @param text 识别文本
 @param resultData 原始数据
 */
- (void)fileRecognizer:(QCloudFileRecognizer *_Nullable)recognizer requestId:(NSInteger)requestId text:(nullable NSString *)text resultData:(nullable NSDictionary *)resultData;
/**
 录音文件识别失败回调
 
 @param recognizer 录音文件识别器
 @param requestId 请求唯一标识 requestId，recognize：接口返回
 @param error 识别错误，出现错误此字段有
 @param resultData 原始数据
 */
- (void)fileRecognizer:(QCloudFileRecognizer *_Nullable)recognizer requestId:(NSInteger)requestId error:(nullable NSError *)error resultData:(nullable NSDictionary *)resultData;
@end
```

## 示例

### 1. 创建 QCloudFileRecognizer 实例 

```objective-c
  QCloudFileRecognizer *recognizer = [[QCloudFileRecognizer alloc] initWithAppId:appId 
  								        secretId:secretId 
								       secretKey:secretKey];
  //设置 delegate，相关回调方法见 QCloudFileRecognizerDelegate 定义
 recognizer.delegate = self;
```

### 2. 实现此 [QCloudFileRecognizerDelegate](#QCloudFileRecognizerDelegate) 协议方法

### 3. 调用方式示例

+ #### 通过语音 url 调用

```objective-c
 (void)recognizeWithUrl {
    QCloudFileRecognizeParams *params = [QCloudFileRecognizeParams defaultRequestParams];
    params.audioUrl = @"https://asr-audio-1256237915.cos.ap-shanghai.myqcloud.com/30s.wav";
    [_recognizer recognize:params];
}
```

+ #### 通过语音数据调用

```objective-c
 (void)recognizeWithAudioData {
    QCloudFileRecognizeParams *params = [QCloudFileRecognizeParams defaultRequestParams];
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"recordedFile" ofType:@"wav"];
    NSData *audioData = [[NSData alloc] initWithContentsOfFile:filePath];
    params.audioData = audioData;
    params.sourceType = QCloudAudioSourceTypeAudioData;
    [_recognizer recognize:params];
}
```
