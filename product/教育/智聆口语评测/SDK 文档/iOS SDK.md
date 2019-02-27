## 概述
腾讯云智聆口语评测（英文版）（Smart Oral Evaluation-English，SOE-E）是腾讯云推出的语音评测产品，是基于英语口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的英语口语发音评测。支持单词和句子模式的评测，多维度反馈口语表现。支持单词和句子评测模式，可广泛应用于英语口语类教学应用中。

TAISDK是一款封装了腾讯云教育AI能力的SDK，通过集成SDK，用户可以快速接入相关产品功能，如数学作业批改、智聆口语评测等。本文档介绍智聆口语评测iOS SDK相关说明，如需其他产品的调用说明，可到对应产品的产品文档查看。
详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 使用说明
####  第三方库依赖
第三方库 lame.framework 的主要目的是为了实现文件类型转换。本 SDK 依赖第三方库：lame.framework，将 SDK 和 lame.framework 直接引入项目中即可。

### 一、获取密钥

secretId和secretKey是使用SDK的安全凭证，通过以下方式获取

![](http://dldir1.qq.com/hudongzhibo/taisdk/document/taisdk_cloud_1.png)

### 二、SDK集成

#### 1、导入SDK

[Demo源码下载](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe)

从Demo获取SDK并导入到工程
![](http://dldir1.qq.com/hudongzhibo/taisdk/document/taisdk_ios_1.png)


#### 2、接口调用

##### 智聆口语评测


```objc
//一、声明并定义对象
@property (strong, nonatomic) TAIOralEvaluation *oralEvaluation;
self.oralEvaluation = [[TAIOralEvaluation alloc] init];
self.oralEvaluation.delegate = self;
```

```objc
//二、数据回调
- (void)oralEvaluation:(TAIOralEvaluation *)oralEvaluation onEvaluateData:(TAIOralEvaluationData *)data result:(TAIOralEvaluationRet *)result error:(TAIError *)error
{
    //数据和结果回调（只有data.bEnd为YES，result有效）
}
```

* 内部录制（SDK内部录制音频并传输，推荐）

```objc
//三、初始化参数
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init];
param.sessionId = [NSString stringWithFormat:@"%ld", (long)[[NSDate date] timeIntervalSince1970]];
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
//四、开始录制
[self.oralEvaluation startRecordAndEvaluation:param callback:^(TAIError *error) 
    //结果返回
}];
```

```objc
//五、结束录制
[self.oralEvaluation stopRecordAndEvaluation:^(TAIError *error) {
    //结果返回
}];
```

* 外部录制（SDK外部录制音频数据作为Api调用参数）

```objc
//三、初始化参数
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init];
param.sessionId = [NSString stringWithFormat:@"%ld", (long)[[NSDate date] timeIntervalSince1970]];
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
//四、传输数据
[self.oralEvaluation oralEvaluation:param data:data callback:^(TAIError *error) {
    //接口调用结果返回
}];
```


注意事项
> 外部录制三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败



#### 3、签名

secretKey属于安全敏感参数，线上版本一般由业务后台生成[临时secretKey](https://cloud.tencent.com/document/api/598/13895)或者SDK外部签名返回到客户端。

>（1）内部签名：sdk内部通过用户提供的secretKey和secretId计算签名，用户无需关心签名细节
>（2）外部签名：sdk外部调用getStringToSign获取签名字符串，然后根据[签名规则（参考步骤三）](https://cloud.tencent.com/document/product/884/30657) 进行签名。口语评测时需提供secretId、timestamp和signature参数


```objc
//获取签名所需字符串
- (NSString *)getStringToSign:(NSInteger)timestamp;
```

注意事项
>时间戳timestamp必须和TAIEvaluationParam参数的timestamp一致

#### 4、参数说明

##### 公共参数
* TAICommonParam参数说明

| 参数|类型|必填|说明 |
|---|---|---|---|
|appId|NSString|是|appId|
|timeout|NSInteger|否|超时时间，默认30秒|
|secretId|NSString|是|密钥Id|
|secretKey|NSString|内部签名：必填|密钥Key|
|signature|NSString|外部签名：必填|签名|
|timestamp|NSInteger|外部签名：必填|秒级时间戳|

* TAIError参数说明

| 参数|类型|说明 |
|---|---|---|
|code|TAIErrCode|错误码|
|desc|NSString|错误描述|
|requestId|NSString|请求id，定位错误信息|



##### 智聆口语评测

* TAIOralEvaluationParam参数说明

| 参数|类型|必填|说明 |
|---|---|---|---|
|sessionId|NSString|是|一次批改唯一标识|
|workMode|TAIOralEvaluationWorkMode|是|传输方式|
|evalMode|TAIOralEvaluationEvalMode|是|评测模式|
|fileType|TAIOralEvaluationFileType|是|数据格式（目前支持mp3）|
|storageMode|TAIOralEvaluationStorageMode|式|是否存储音频文件|
|serverType|TAIOralEvaluationServerType|是|语言类型|
|scoreCoeff|float|是|苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段|
|refText|NSString|是|被评估语音对应的文本|

* TAIOralEvaluationData参数说明

| 参数|类型|说明 |
|---|---|---|
|seqId|NSInteger|分片序列号|
|bEnd|BOOL|是否最后一个分片|
|audio|NSData|音频数据|

* TAIMathCorrectionRet参数说明

| 参数|类型|说明 |
|---|---|---|
|sessionId|NSString|一次批改唯一标识|
|pronAccuracy|float|发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|float|发音流利度，取值范围[0, 1]，当为词模式时，取值无意义|
|pronCompletion|float|发音完整度，取值范围[0, 1]，当为词模式时，取值无意义|
|audioUrl|NSString|保存语音音频文件的下载地址（TAIOralEvaluationStorageMode_Enable有效）|
|words|NSArray<TAIOralEvaluationWord *>|详细发音评估结果|


* TAIOralEvaluationWord参数说明

| 参数|类型|说明 |
|---|---|---|
|beginTime|int|当前单词语音起始时间点，单位为ms|
|endTime|int|当前单词语音终止时间点，单位为ms|
|pronAccuracy|float|单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|float|单词发音流利度，取值范围[0, 1]|
|word|NSString|当前词|
|matchTag|int|当前词与输入语句的匹配情况，0:匹配单词、1：新增单词、2：缺少单词|












