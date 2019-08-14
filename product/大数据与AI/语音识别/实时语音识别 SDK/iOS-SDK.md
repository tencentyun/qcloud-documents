## 1. 接入准备

### 1.1 SDK 获取

实时语音识别的 iOS SDK 以及 Demo 的下载地址：[iOS SDK](https://client-sdk-1255628450.cos.ap-shanghai.myqcloud.com/asr%20sdk/QCloudSDK_iOS.zip)。


### 1.2 接入须知

+ 开发者在调用前请先查看实时语音识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/35721) ，了解接口的**使用要求**和**使用步骤**。
+ 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等），且系统为**iOS 9.0**及以上版本。

### 1.3 开发环境

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
   <string>需要使用了的麦克风采集音频</string>
```

+ **在工程中添加依赖库，在 build Phases Link Binary With Libraries 中添加以下库：**
   + AVFoundation.framework
   + AudioToolbox.framework
   + QCloudSDK.framework
   + CoreTelephony.framework
   + libWXVoiceSpeex.a
   
添加完后如下图所示：

![](https://main.qcloudimg.com/raw/17ff6f4f4a27e0843de528eb070c2f32.png)

## 2. 快速接入

### 2.1 开发流程及接入示例

下面分别介绍**使用内置录音器采集语音识别**和**调用者提供语音数据**接入流程和示例。

#### 使用内置录音器采集语音识别示例

1.**引入 QCloudSDK 的头文件，将使用 QCloudSDK 的文件名后缀由 .m->.mm**

```objective-c
#import<QCloudSDK/QCloudSDK.h>
```

2.**创建 QCloudConfig 实例**

```objective-c
 //1.创建QCloudConfig实例
 QCloudConfig *config = [[QCloudConfig alloc] initWithAppId:kQDAppId 
  						   secretId:kQDSecretId 
					          secretKey:kQDSecretKey 
					          projectId:kQDProjectId];
 config.sliceTime = 600;                        //语音分片时常600ms
 config.enableDetectVolume = YES;               //是否检测音量
 config.endRecognizeWhenDetectSilence = YES;    //是否检测到静音停止识别
```

3.**创建 QCloudRealTimeRecognizer 实例** 

```objective-c
 QCloudRealTimeRecognizer *recognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config];
```

4.**设置 delegate，实现 [QCloudRealTimeRecognizerDelegate](#QCloudRealTimeRecognizerDelegate) 方法**

```objective-c
recognizer.delegate = self;
```

5.**开始识别**

```objective-c
 [recognizer start];
```

6.**结束识别**

```objective-c
 [recognizer stop];
```


#### 调用者提供语音数据示例
1.**引入  QCloudSDK 的头文件，将使用 QCloudSDK 的文件名后缀由 .m->.mm**

```objective-c
#import<QCloudSDK/QCloudSDK.h>
```

2.**创建 QCloudConfig 实例** 

```objective-c
 //1.创建QCloudConfig实例
 QCloudConfig *config = [[QCloudConfig alloc] initWithAppId:kQDAppId 
  						  secretId:kQDSecretId 
					         secretKey:kQDSecretKey 
					         projectId:kQDProjectId];
 config.sliceTime = 600;                        //语音分片时常600ms
 config.enableDetectVolume = YES;               //是否检测音量
 config.endRecognizeWhenDetectSilence = YES;    //是否检测到静音停止识别
```

3.**自定义 QCloudDemoAudioDataSource，QCloudDemoAudioDataSource 实现 [QCloudAudioDataSource](#QCloudAudioDataSource) 协议**

```objective-c
 QCloudDemoAudioDataSource *dataSource = [[QCloudDemoAudioDataSource alloc] init];
```

4.**创建 QCloudRealTimeRecognizer 实例**

```objective-c
 QCloudRealTimeRecognizer *recognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config dataSource:dataSource];
```

5.**设置 delegate，实现 [QCloudRealTimeRecognizerDelegate](#QCloudRealTimeRecognizerDelegate) 方法**

```objective-c
 recognizer.delegate = self;
```

6.**开始识别** 

```objective-c
 [recognizer start];
```

7.**结束识别**

```objective-c
 [recognizer stop];
```

### 2.2 主要接口类说明

**QCloudRealTimeRecognizer 初始化说明**

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

**QCloudConfig 初始化方法说明**

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




**<div id="QCloudRealTimeRecognizerDelegate">QCloudRealTimeRecognizerDelegate方法说明</div>**

```objective-c
/**
 * 一次实时录音识别，分为多个flow，每个flow可形象的理解为一句话，一次识别中可以包括多句话。
  * 每个flow包含多个seq语音数据包，每个flow的seq从0开始
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
 */
- (void)realTimeRecognizerDidError:(QCloudRealTimeRecognizer *)recognizer error:(NSError *)error;


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
 * @param volume 声音音量，取值范围（-40-0)
 */
- (void)realTimeRecognizerDidUpdateVolume:(QCloudRealTimeRecognizer *)recognizer volume:(float)volume;


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/**
 * 语音流的开始识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的voiceId，唯一标识
 * @param seq flow的序列号
 */
- (void)realTimeRecognizerOnFlowRecognizeStart:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;
/**
 * 语音流的结束识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的voiceId，唯一标识
 * @param seq flow的序列号
 */
- (void)realTimeRecognizerOnFlowRecognizeEnd:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/**
 * 语音流开始识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的voiceId，唯一标识
 * @param seq flow的序列号
 */
- (void)realTimeRecognizerOnFlowStart:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;
/**
 * 语音流结束识别
 * @param recognizer 实时语音识别实例
 * @param voiceId 语音流对应的voiceId，唯一标识
 * @param seq flow的序列号
 */
- (void)realTimeRecognizerOnFlowEnd:(QCloudRealTimeRecognizer *)recognizer voiceId:(NSString *)voiceId seq:(NSInteger)seq;

@end
```

**<div id="QCloudAudioDataSource">QCloudAudioDataSource协议说明</div>**
调用者不适用 SDK 内置录音器进行语音数据采集，自己提供语音数据需要实现此协议所有方法，可见 Demo 工程里的 QDAudioDataSource 实现

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
 * 标识data source是否开始工作，执行完start后需要设置成YES， 执行完stop后需要设置成NO
 */
@property (nonatomic, assign) BOOL running;

/**
 * SDK会调用start方法，实现此协议的类需要初始化数据源。
 */
- (void)start:(void(^)(BOOL didStart, NSError *error))completion;
/**
 * SDK会调用stop方法，实现此协议的类需要停止提供数据
 */
- (void)stop;
/**
 * SDK会调用实现此协议的对象的此方法读取语音数据, 如果语音数据不足expectLength，则直接返回nil。
 * @param expectLength 期望读取的字节数，如果返回的NSData不足expectLength个字节，SDK会抛出异常。
 */
- (nullable NSData *)readData:(NSInteger)expectLength;

@end

```
