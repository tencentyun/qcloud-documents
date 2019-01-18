## 概述
腾讯云智聆口语评测（英文版）（Smart Oral Evaluation-English，SOE-E）是腾讯云推出的语音评测产品，是基于英语口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的英语口语发音评测。支持单词和句子模式的评测，多维度反馈口语表现。支持单词和句子评测模式，可广泛应用于英语口语类教学应用中。
本 SDK 为智聆口语测评（英文版）的 iOS 版本，封装了对智聆口语测评网络API的调用及本地音频文件处理，并提供简单的录音功能，使用者可以专注于从业务切入，方便简洁地进行二次开发。
详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 使用说明
#### 工程及 Demo 源码
[工程及 Demo 源码的 GitHub 地址>>](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe)
本 SDK 的主文件为 TencentSOE.framework，直接引入项目中即可。
![](https://main.qcloudimg.com/raw/f79f9171a7c93d14dd51c4c10a5d070e.png)
####  第三方库依赖
第三方库 lame.framework 的主要目的是为了实现文件类型转换。本 SDK 依赖第三方库：lame.framework，将 SDK 和 lame.framework 直接引入项目中即可。

####  获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在【[访问管理](https://console.cloud.tencent.com/cam/overview)】>【云 API 密钥】>【[API 密钥管理](https://console.cloud.tencent.com/cam/capi)】中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png)



## 使用示例
SDK 详细使用流程请参见 [TSOEDemo 工程](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe/tree/master/demo/TSOEDemo)。
#### 初始化 SDK
```
[TXTencentSOE shareTencentSOE].VoiceSecretID = @"";
[TXTencentSOE shareTencentSOE].VoiceSecretKey = @"";
[TXTencentSOE shareTencentSOE].Region = @"";
[TXTencentSOE shareTencentSOE].SoeAppId = @"";
[TXTencentSOE shareTencentSOE].isLongLifesession = @"1";
[TXTencentSOE shareTencentSOE].requestDomain = @"soe.tencentcloudapi.com";
```
详细说明请参见 Demo 中的 initSdk。

####  开始分片录制
```
[TXTencentSOE shareTencentSOE].seqID = 0;
[TXTencentSOE shareTencentSOE].isVoiceVerifyInit= 0;
[_recorder startRecording];
```
详细说明请参见 Demo 中的 startRecord。

####  同时处理分片回调的数据并进行口语评测
```
_verification = [[TXVoiceVerification alloc] init];
NSString *dataStr = [TXBase64File getBase64StringWithFileData:mp3Data];
if(![TXTencentSOE shareTencentSOE].isVoiceVerifyInit){
    [TXTencentSOE shareTencentSOE].isVoiceVerifyInit = 1;
    [self initVoice:dataStr isEnd:isEnd];
}
else{
    [self vertifyVoice:dataStr isEnd:isEnd];
}
```
详细说明请参见 Demo 中的 AudioQueueRecorder 回调。

####  处理口语评测的结果
最后一个分片完成后，即可处理口语评测的结果。
```
TXVoiceVerificationFileType type = [self getFileType];
__weak typeof(self) ws = self;
[_verification oralProcessTransmitWithVoiceFileType:type userVoiceData:@[date] sessionID:_sessionId isEnd:isEnd result:^(TXVoiceVerification *voiceVerification, NSDictionary * _Nullable result, NSURLResponse * _Nullable response, NSError * _Nullable error) {
    [ws setResponse:[NSString stringWithFormat:@"%@", result]];
}];
```
详细说明请参见 Demo 中的 vertifyVoice 返回。

## 接口设计说明
TencentSOE.fremework 有四大模块：配置信息、录音、对文件进行 base64加密、校验语音。
#### 配置信息（TXTencentSOE）
TXTencentSOE 是一个单例，需要配置申请的 SecretID 和 SecretKey，代码如下。
```
// 初始化语音评测单例
[TXTencentSOE shareTencentSOE].VoiceSecretID = @"";//填写在官网申请的secretid
[TXTencentSOE shareTencentSOE].VoiceSecretKey = @"";//填写在官网申请的secretkey
[TXTencentSOE shareTencentSOE].Region = @"";
[TXTencentSOE shareTencentSOE].SoeAppId = @"";//填写soeappid
[TXTencentSOE shareTencentSOE].isLongLifesession = @"1";
[TXTencentSOE shareTencentSOE].requestDomain = @"soe.tencentcloudapi.com";//可根据实际选择就近的请求域名
```
#### 录音(TXRecorder)
TXRecorder 是对录音功能的封装，这里依赖了系统库 AudioToolbox 和第三方库 lame，包括以下三个对象方法。
```
@selector(startRecording:)//开始录音
@selector(stopRecording)//停止录音
@selector(AudioQueueRecorder:(TXRecorder *)recorder mp3Data:(NSData *)mp3Data isEnd:(int)isEnd)//回调录制数据到上层 App
```
#### 对文件进行 base64加密（TXBase64File）
TXBase64File 需要关注以下方法。
```
@selector(getBase64StringWithFileData:)//对一段 data 做 base64编码
```
#### 校验语音(TXVoiceVerification)
`TXVoiceVerification`用来校验语音，并进行口语评测，分为两部分：初始化接口和发音数据传输接口。
- 初始化接口
```
@selector(oralProcessInitWithSessionID:RefText:workMode:evaluationMode:ScoreCoeff:result:)
```
 * sessionID：语音段唯一标识，一个完整语音一个 SessionId。
 * RefText：被评估语音对应的文本。
 * workMode：语音输入模式，0表示流式分片，1表示非流式一次性评估，分别与枚举值相对应。
 * evaluationMode：评估模式，0表示词模式， 1表示句子模式。当为词模式评估时，能够提供每个音节的评估信息；当为句子模式时，能够提供完整度和流利度信息。
 * ScoreCoeff：评价苛刻指数，取值为[1.0，4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段。
 * block：接口运行结果返回的 block，block 中的 result 对应结果，error 对应错误信息。

- 发音数据传输接口
```
@selector(oralProcessTransmitWithVoiceFileType:userVoiceData:sessionID:result:)
```
 * voiceFileType：文件类型，有 Raw、Wav、MP3三种类型。
 * userVoiceDataArray：要校验的语音数组，采用分片传输，只需要传入只有一个元素的数组就可以了，这个参数的传输依赖于 TXBase64File 生成的字符串与数组。
 * sessionID：同初始化接口的 sessionID。
 * block：同初始化接口的 block。





