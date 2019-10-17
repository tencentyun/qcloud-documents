## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
TAISDK 是一款封装了腾讯云教育 AI 能力的 SDK，通过集成 SDK，用户可以快速接入相关产品功能，如数学作业批改、智聆口语评测等。本文档介绍智聆口语评测 iOS SDK 相关说明，如需其他产品的调用说明，可在对应产品的产品文档查看。
详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 使用前提
####  添加第三方库依赖
第三方库 lame.framework 的主要目的是为了实现文件类型转换。本 SDK 依赖第三方库为 lame.framework，您只需将 SDK 和 lame.framework 直接引入项目中即可。

#### 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在【[访问管理](https://console.cloud.tencent.com/cam/overview)】>【云 API 密钥】>【[API 密钥管理](https://console.cloud.tencent.com/cam/capi)】中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png)

## 集成 SDK 
### 1. 导入 SDK
从 [Demo 源码](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe) 中获取 SDK 并导入到工程。
![](http://dldir1.qq.com/hudongzhibo/taisdk/document/taisdk_ios_1.png)

### 2. 调用接口
声明并定义对象：
```objc
@property (strong, nonatomic) TAIOralEvaluation *oralEvaluation;
self.oralEvaluation = [[TAIOralEvaluation alloc] init];
self.oralEvaluation.delegate = self;
```
数据回调：
```objc
- (void)oralEvaluation:(TAIOralEvaluation *)oralEvaluation onEvaluateData:(TAIOralEvaluationData *)data result:(TAIOralEvaluationRet *)result error:(TAIError *)error
{
    //数据和结果回调（只有data.bEnd为YES，result有效）
}
```

### 3. 录制音频
* **内部录制**（SDK 内部录制音频并传输，推荐）
```objc
//1.初始化参数
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init];
param.sessionId = [[NSUUID UUID] UUIDString];
param.appId = @"";
param.workMode = TAIOralEvaluationWorkMode_Once;
param.evalMode = TAIOralEvaluationEvalMode_Sentence;
param.storageMode = TAIOralEvaluationStorageMode_Disable;
param.serverType = TAIOralEvaluationServerType_English;
param.scoreCoeff = 1.0;
param.fileType = TAIOralEvaluationFileType_Mp3;//只支持mp3
param.refText = @"";
param.secretId = @"";
param.secretKey = @"";
//2.开始录制
[self.oralEvaluation startRecordAndEvaluation:param callback:^(TAIError *error) 
    //结果返回
}];
//3.结束录制
[self.oralEvaluation stopRecordAndEvaluation:^(TAIError *error) {
    //结果返回
}];
```
* **外部录制**（SDK 外部录制音频数据作为 API 调用参数）
```objc
//1.初始化参数
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init];
param.sessionId = [[NSUUID UUID] UUIDString];
param.appId = @"";
param.workMode = TAIOralEvaluationWorkMode_Once;
param.evalMode = TAIOralEvaluationEvalMode_Sentence;
param.storageMode = TAIOralEvaluationStorageMode_Disable;
param.serverType = TAIOralEvaluationServerType_English;
param.scoreCoeff = 1.0;
param.fileType = TAIOralEvaluationFileType_Mp3;
param.refText = @"hello guagua";
param.secretId = @"";
param.secretKey = @"";
NSString *mp3Path = [[NSBundle mainBundle] pathForResource:@"hello_guagua" ofType:@"mp3"];
TAIOralEvaluationData *data = [[TAIOralEvaluationData alloc] init];
data.seqId = 1;
data.bEnd = YES;
data.audio = [NSData dataWithContentsOfFile:mp3Path];
__weak typeof(self) ws = self;
//2.传输数据
[self.oralEvaluation oralEvaluation:param data:data callback:^(TAIError *error) {
    //接口调用结果返回
}];
```
>!外部录制三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败。



### 4. 签名
SecretKey 属于安全敏感参数，线上版本一般由业务后台生成 [临时 SecretKey](https://cloud.tencent.com/document/api/598/13896) 或者 SDK 外部签名返回到客户端。
临时签名policy示例如下：
```json
{
    "version": "2.0",
    "statement": {
        "effect": "allow",
        "action": [
            "soe:InitOralProcess",
            "soe:ExtraOralProcess",
            "soe:TransmitOralProcess",
            "soe:TransmitOralProcessWithInit"
        ],
        "resource": "*"
    }
}
```

- 内部签名：SDK 内部通过用户提供的 SecretKey 和 SecretId 计算签名，用户无需关心签名细节
- 外部签名：SDK 外部调用 getStringToSign 获取签名字符串，然后根据 [签名规则-计算签名](https://cloud.tencent.com/document/product/884/30657#3.-.E8.AE.A1.E7.AE.97.E7.AD.BE.E5.90.8D) 进行签名。口语评测时需提供 SecretId、timestamp 和 signature 参数。

```objc
//获取签名所需字符串
- (NSString *)getStringToSign:(NSInteger)timestamp;
```
>!时间戳 timestamp 必须和 TAIEvaluationParam 参数的 timestamp 一致。

## 参数说明

### 公共参数
TAICommonParam 参数说明：

| 参数|类型|必填|说明 |
|---|---|---|---|
|appId|NSString|是|AppId|
|timeout|NSInteger|否|超时时间，默认30秒|
|secretId|NSString|是|密钥 ID|
|secretKey|NSString|内部签名：必填|密钥 Key|
|signature|NSString|外部签名：必填|签名|
|timestamp|NSInteger|外部签名：必填|秒级时间戳|

TAIError 参数说明：

| 参数|类型|说明 |
|---|---|---|
|code|TAIErrCode|错误码|
|desc|NSString|错误描述|
|requestId|NSString|请求 ID，定位错误信息|



### 智聆口语评测参数
TAIOralEvaluationParam 参数说明：

| 参数|类型|必填|说明 |
|---|---|---|---|
|sessionId|NSString|是|一次批改唯一标识|
|workMode|TAIOralEvaluationWorkMode|是|传输方式|
|evalMode|TAIOralEvaluationEvalMode|是|评测模式|
|fileType|TAIOralEvaluationFileType|是|数据格式（目前支持 MP3）|
|storageMode|TAIOralEvaluationStorageMode|式|是否存储音频文件|
|serverType|TAIOralEvaluationServerType|是|语言类型|
|scoreCoeff|Float|是|苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段|
|refText|NSString|是|被评估语音对应的文本|

TAIOralEvaluationData 参数说明：

| 参数|类型|说明 |
|---|---|---|
|seqId|NSInteger|分片序列号|
|bEnd|BOOL|是否最后一个分片|
|audio|NSData|音频数据|

TAIMathCorrectionRet 参数说明：

| 参数|类型|说明 |
|---|---|---|
|sessionId|NSString|一次批改唯一标识|
|pronAccuracy|Float|发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|Float|发音流利度，取值范围[0, 1]，当为词模式时，取值无意义|
|pronCompletion|Float|发音完整度，取值范围[0, 1]，当为词模式时，取值无意义|
|audioUrl|NSString|保存语音音频文件的下载地址（TAIOralEvaluationStorageMode_Enable 有效）|
|words|NSArray<TAIOralEvaluationWord *>|详细发音评估结果|


TAIOralEvaluationWord 参数说明：

| 参数|类型|说明 |
|---|---|---|
|beginTime|Int|当前单词语音起始时间点，单位为ms|
|endTime|Int|当前单词语音终止时间点，单位为ms|
|pronAccuracy|Float|单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|Float|单词发音流利度，取值范围[0, 1]|
|word|NSString|当前词|
|matchTag|Int|当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词|












