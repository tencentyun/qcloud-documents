## 开发准备

### SDK 获取

实时流式语音识别的 iOS SDK 的下载地址：[iOS SDK](https://main.qcloudimg.com/raw/08dc7d8975ede33ecba181d38b1075ae/QCloudAAIClientSDK.zip)

更多示例可参考 Demo：[iOS Demo](https://main.qcloudimg.com/raw/522db7adc9be319ea591d15e5cbec49c/iOSDemo.zip)

### 开发准备

-  只支持 iOS 8.0 及以上版本，不支持 bitcode 版本；
-  实时流式语音识别，需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等）；
-  从控制台获取 APP ID、SecretID、SecretKey，详情参考 [基本概念](https://cloud.tencent.com/document/product/441/6194)。


### SDK 配置

#### SDK 导入

iOS SDK 压缩包名称为： QCloudSDK.zip。压缩包中包含了一个` .a` 静态库和QCloudSDK.framework。

#### 工程配置

在工程` info.plist` 文件中设置：

1. App Transport Security Settings 类型，然后在 App Transport Security Settings 下添加 Allow Arbitrary Loads 类型 Boolean，值设为 `YES`；
2. 在工程 `info.plist `文件中添加 Privacy - Microphone Usage Description，获取系统的麦克风的权限；
3. 在工程中添加依赖库，在build Phases Link Binary With Libraries中添加以下库：
    QCloudSDK.framework
    AVFoundation.framework
    AudioToolbox.framework
    libWXVoiceSpeex.a


### 说明

#### QCloudRealTimeRecognizer初始化说明
*QCloudRealTimeRecognizer*是实时语音识别类，提供两种初始化方法。
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

#### QCloudConfig初始化方法说明

```objective-c
/**
 * 初始化方法
 * @param appid     腾讯云appId     基本概念见https://cloud.tencent.com/document/product/441/6194
 * @param secretId  腾讯云secretId  基本概念见https://cloud.tencent.com/document/product/441/6194
 * @param secretKey 腾讯云secretKey 基本概念见https://cloud.tencent.com/document/product/441/6194
 * @param projectId 腾讯云projectId 基本概念见https://cloud.tencent.com/document/product/441/6194
 */
- (instancetype)initWithAppId:(NSString *)appid
                     secretId:(NSString *)secretId
                    secretKey:(NSString *)secretKey
                    projectId:(NSString *)projectId;
```

#### QCloudRealTimeRecognizerDelegate方法说明

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

## 示例
### 使用内置录音器采集语音识别示例
#### 1.引入上传 SDK 的头文件，将使用QCloudSDK的文件名后缀有*.m->.mm*
```objective-c
#import<QCloudSDK/QCloudSDK.h>
```
#### 2.创建QCloudConfig实例
```objective-c
 //1.创建QCloudConfig实例
 QCloudConfig *config = [[QCloudConfig alloc] initWithAppId:kQDAppId 
  						  secretId:kQDSecretId 
					         secretKey:kQDSecretKey 
					         projectId:kQDProjectId];
 config.sliceTime = 600;                             	           //语音分片时常600ms
 config.enableDetectVolume = _volumeDetectSwitch.on;                //是否检测音量
 config.endRecognizeWhenDetectSilence = _silenceDetectEndSwitch.on; //是否检测到静音停止识别
```
#### 3.创建QCloudRealTimeRecognizer实例
```objective-c
 QCloudRealTimeRecognizer *recognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config];;
```
#### 4.设置delegate，实现*QCloudRealTimeRecognizerDelegate*方法，QCloudRealTimeRecognizerDelegate定义详见上面说明
```objective-c
recognizer.delegate = self;
```
#### 5.开始识别
```objective-c
 [recognizer start];
```
#### 6.结束识别
```objective-c
 [recognizer stop];
```
