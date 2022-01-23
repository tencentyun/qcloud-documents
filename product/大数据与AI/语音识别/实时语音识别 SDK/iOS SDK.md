iOS SDK 接入请观看视频：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-12773?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

##  接入准备
###  SDK 获取
实时语音识别的 iOS SDK 以及 Demo 的下载地址：[iOS SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_IOS_v2.6.4.zip)。

###  接入须知
- 开发者在调用前请先查看实时语音识别的[ 接口说明](https://cloud.tencent.com/document/product/1093/37138)，了解接口的**使用要求**和**使用步骤**。   
- 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等），且系统为 **iOS 9.0** 及以上版本。

###  开发环境
在工程` info.plist`添加以下设置：
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
+ **在工程中添加依赖库，在 build Phases Link Binary With Libraries 中添加以下库：**
  + AVFoundation.framework
  + AudioToolbox.framework
  + QCloudSDK.framework
  + CoreTelephony.framework
  + libWXVoiceSpeex.a

添加完后如下图所示：
![](https://main.qcloudimg.com/raw/17ff6f4f4a27e0843de528eb070c2f32.png)

##  快速接入
### 开发流程及接入示例
下面分别介绍**使用内置录音器采集语音识别**和**调用者提供语音数据**接入流程和示例。

#### 使用内置录音器采集语音识别示例
1. **引入 QCloudSDK 的头文件，将使用 QCloudSDK 的文件名后缀由 .m->.mm**
```objective-c
#import<QCloudSDK/QCloudSDK.h>
```
2. **创建 QCloudConfig 实例**
```objective-c
 //1.创建 QCloudConfig 实例
 QCloudConfig *config = [[QCloudConfig alloc] initWithAppId:kQDAppId 
  						   secretId:kQDSecretId 
					          secretKey:kQDSecretKey 
					          projectId:kQDProjectId];
 config.sliceTime = 600;                        //语音分片时长600ms
 config.enableDetectVolume = YES;               //是否检测音量
 config.endRecognizeWhenDetectSilence = YES;    //是否检测到静音停止识别
```
3. **创建 QCloudRealTimeRecognizer 实例** 
```objective-c
 QCloudRealTimeRecognizer *recognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config];
```
4. **设置 delegate，实现 [QCloudRealTimeRecognizerDelegate](#QCloudRealTimeRecognizerDelegate) 方法**
```objective-c
recognizer.delegate = self;
```
5. **开始识别**
```objective-c
 [recognizer start];
```
6. **结束识别**
```objective-c
 [recognizer stop];
```

#### 调用者提供语音数据示例
1. **引入  QCloudSDK 的头文件，将使用 QCloudSDK 的文件名后缀由 .m->.mm**
```objective-c
#import<QCloudSDK/QCloudSDK.h>
```
2. **创建 QCloudConfig 实例** 
```objective-c
 //1.创建 QCloudConfig 实例
 QCloudConfig *config = [[QCloudConfig alloc] initWithAppId:kQDAppId 
  						  secretId:kQDSecretId 
					         secretKey:kQDSecretKey 
					         projectId:kQDProjectId];
 config.sliceTime = 600;                        //语音分片时长600ms
 config.enableDetectVolume = YES;               //是否检测音量
 config.endRecognizeWhenDetectSilence = YES;    //是否检测到静音停止识别
```
3. **自定义 QCloudDemoAudioDataSource，QCloudDemoAudioDataSource 实现 [QCloudAudioDataSource](#QCloudAudioDataSource) 协议**
```objective-c
 QCloudDemoAudioDataSource *dataSource = [[QCloudDemoAudioDataSource alloc] init];
```
4. **创建 QCloudRealTimeRecognizer 实例**
```objective-c
 QCloudRealTimeRecognizer *recognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config dataSource:dataSource];
```
5. **设置 delegate，实现 [QCloudRealTimeRecognizerDelegate](#QCloudRealTimeRecognizerDelegate) 方法**
```objective-c
 recognizer.delegate = self;
```
6. **开始识别** 
```objective-c
 [recognizer start];
```
7. **结束识别**
```objective-c
 [recognizer stop];
```

### 主要接口类说明
#### QCloudRealTimeRecognizer 初始化说明
QCloudRealTimeRecognizer 是实时语音识别类，提供两种初始化方法。
```objective-c
/**
 * 初始化方法，调用者使用内置录音器采集音频
 * @param config 配置参数，详见QCloudConfig定义
 */
- (instancetype)initWithConfig:(QCloudConfig *)config;

/**
 * 初始化方法，调用者传递语音数据调用此初始化方法
 * @param config 配置参数，详见QCloudConfig定义
 * @param dataSource 语音数据数据源，必须实现QCloudAudioDataSource协议
 */
- (instancetype)initWithConfig:(QCloudConfig *)config dataSource:(id<QCloudAudioDataSource>)dataSource;
```

#### QCloudConfig 初始化方法说明
```objective-c
/**
 * 初始化方法-直接鉴权
 * @param appid     腾讯云 appId 
 * @param secretId  腾讯云 secretId
 * @param secretKey 腾讯云 secretKey
 * @param projectId 腾讯云 projectId
 */
- (instancetype)initWithAppId:(NSString *)appid
                     secretId:(NSString *)secretId
                    secretKey:(NSString *)secretKey
                    projectId:(NSString *)projectId;

/**
 * 初始化方法-通过STS临时证书鉴权，详见https://cloud.tencent.com/document/product/598/33416
 * @param appid     腾讯云appId 
 * @param secretId  腾讯云临时secretId  
 * @param secretKey 腾讯云临时secretKey
 * @param token     对应的token
 */
- (instancetype)initWithAppId:(NSString *)appid
    				    secretId:(NSString *)secretId
       					secretKey:(NSString *)secretKey
            			token:(NSString *)token;
```

[](id:QCloudRealTimeRecognizerDelegate)
#### QCloudRealTimeRecognizerDelegate 方法说明
```objective-c
/**
 * 一次实时录音识别，分为多个flow，每个 flow 可形象的理解为一句话，一次识别中可以包括多句话。
  * 每个 flow 包含多个 seq 语音数据包，每个 flow 的 seq 从0开始
 */
@protocol QCloudRealTimeRecognizerDelegate <NSObject>

@required
/**
 * 每个语音包分片识别结果
 * @param response 语音分片的识别结果
 */
- (void)realTimeRecognizerOnSliceRecognize:(QCloudRealTimeRecognizer *)recognizer response:(QCloudRealTimeResponse *)response;

@optional
/**
 * 一次识别成功回调
 @param recognizer 实时语音识别实例
 @param result 一次识别出的总文本
 */
- (void)realTimeRecognizerDidFinish:(QCloudRealTimeRecognizer *)recognizer result:(NSString *)result;
/**
 * 一次识别失败回调
 * @param recognizer 实时语音识别实例
 * @param error 错误信息
 * @param voiceId  如果错误是后端返回的，附带voiceId
 */

- (void)realTimeRecognizerDidError:(QCloudRealTimeRecognizer *)recognizer error:(NSError *)error  voiceId:(NSString * _Nullable) voiceId;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/**
 * 开始录音回调
 * @param recognizer 实时语音识别实例
 * @param error 开启录音失败，错误信息
 */
- (void)realTimeRecognizerDidStartRecord:(QCloudRealTimeRecognizer *)recognizer error:(NSError *)error;
/**
 * 结束录音回调
 * @param recognizer 实时语音识别实例
 */
- (void)realTimeRecognizerDidStopRecord:(QCloudRealTimeRecognizer *)recognizer;
/**
 * 录音音量实时回调用
 * @param recognizer 实时语音识别实例
 * @param volume 声音音量，取值范围（-40-0）
 */
- (void)realTimeRecognizerDidUpdateVolume:(QCloudRealTimeRecognizer *)recognizer volume:(float)volume;


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/**
 * 语音流的开始识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的 voiceId，唯一标识
 * @param seq flow 的序列号
 */
- (void)realTimeRecognizerOnFlowRecognizeStart:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;
/**
 * 语音流的结束识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的 voiceId，唯一标识
 * @param seq flow的序列号
 */
- (void)realTimeRecognizerOnFlowRecognizeEnd:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/**
 * 语音流开始识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的 voiceId，唯一标识
 * @param seq flow 的序列号
 */
- (void)realTimeRecognizerOnFlowStart:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;
/**
 * 语音流结束识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的 voiceId，唯一标识
 * @param seq flow 的序列号
 */
- (void)realTimeRecognizerOnFlowEnd:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;

@end
```

[](id:QCloudAudioDataSource)
#### QCloudAudioDataSource 协议说明
调用者不适用 SDK 内置录音器进行语音数据采集，自己提供语音数据需要实现此协议所有方法，可见 Demo 工程中的 QDAudioDataSource 实现。
```objective-c
/**
 * 语音数据数据源，如果调用者需要自己提供语音数据, 调用者实现此协议中所有方法
 * 提供符合以下要求的语音数据:
 * 采样率：16k
 * 音频格式：pcm
 * 编码：16bit位深的单声道
 */
@protocol QCloudAudioDataSource <NSObject>

@required

/**
 * 标识 data source是否开始工作，执行完 start 后需要设置成 YES， 执行完 stop 后需要设置成 NO
 */
@property (nonatomic, assign) BOOL running;

/**
 * SDK 会调用 start 方法，实现此协议的类需要初始化数据源。
 */
- (void)start:(void(^)(BOOL didStart, NSError *error))completion;
/**
 * SDK 会调用 stop 方法，实现此协议的类需要停止提供数据
 */
- (void)stop;
/**
 * SDK 会调用实现此协议的对象的此方法读取语音数据, 如果语音数据不足 expectLength，则直接返回 nil。
 * @param expectLength 期望读取的字节数，如果返回的 NSData 不足 expectLength个字节，SDK 会抛出异常。
 */
- (nullable NSData *)readData:(NSInteger)expectLength;

@end
```

