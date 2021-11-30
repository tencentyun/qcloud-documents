## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。    
TAISDK 是一款封装了腾讯云教育 AI 能力的 SDK，通过集成 SDK，用户可以快速接入相关产品功能，如数学作业批改、智聆口语评测等。本文档介绍智聆口语评测 iOS SDK 相关说明，如需其他产品的调用说明，可在对应产品的产品文档查看。
详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。
单击 [示例链接](https://tec.qq.com/ai/soe#demos) 在线体验智聆口语评测 demo。

## 总体流程
### 1. 流程图
![](https://main.qcloudimg.com/raw/adc1d339f5892577db7ab2c701ab8b06.jpg)

### 2. 集成 demo 示例
[下载 SDK](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe) 地址。
获取密钥（ 密钥获取⽅式⻅下⽂） 后到 TAIDemo/TAIDemo/PrivateInfo.m 根据需要填写 appId、secretId、secretKey、soeAppId 和hcmAppId（token 无需填写）。
![](https://main.qcloudimg.com/raw/c9d27bfaa226bc2e513666c635b21d94.png)

## SDK 集成准备
###  1. 添加第三方库依赖
第三方库 lame.framework 的主要目的是为了实现文件类型转换。本 SDK 依赖第三方库为 lame.framework，您只需将 SDK 和 lame.framework 直接引入项目中即可。

### 2. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在**[访问管理](https://console.cloud.tencent.com/cam/overview)**>**访问密钥**>**[API 密钥管理](https://console.cloud.tencent.com/cam/capi)**中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png)

## SDK 集成步骤  
### 1. 导入 SDK
从 [Demo 源码](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe) 中获取 SDK 并导入到工程。
![](https://main.qcloudimg.com/raw/ba3691482e485a775bf4858cbfa7c327/20191231001.png)

### 2. 调用接口
#### 2.1 声明并定义对象：
```objc
@property (strong, nonatomic) TAIOralEvaluation *oralEvaluation;
self.oralEvaluation = [[TAIOralEvaluation alloc] init];
self.oralEvaluation.delegate = self;
```

#### 2.2 数据回调：
```objc
- (void)oralEvaluation:(TAIOralEvaluation *)oralEvaluation onEvaluateData:(TAIOralEvaluationData *)data result:(TAIOralEvaluationRet *)result error:(TAIError *)error
{
    //数据和结果回调（只有data.bEnd为YES，result有效）
}
```

>!请在开始录制音频前设置回调函数，您将通过回调函数获取语音评测结果和错误信息。

### 3. 静音设置
#### 3.1 初始化 TAIRecorderParam 对象，并设置相应参数
请在开始调用 startRecordAndEvaluation（）函数前设置 TAIRecorderParam 参数，静音检测您可以通过 vadEnable 参数打开，并通过 vadInterval 参数设置静音检测时间间隔。
```
TAIRecorderParam *recordParam = [[TAIRecorderParam alloc] init]; 
recordParam.fragEnable = YES; 
recordParam.fragSize = 1024; 
recordParam.vadEnable = YES; 
recordParam.vadInterval = 5000; 
[self.oralEvaluation setRecorderParam:recordParam];
```

#### 3.2 上层通知
当检测到静⾳或者录⾳分⻉变化时，通过 TAIOralEvaluationListener 通知上层。
```
//检测到静音 
- (void)onEndOfSpeechInOralEvaluation:(TAIOralEvaluation *)oralEvaluation 
{     
//这里可以根据业务逻辑处理，如停止录音或提示用户 
} 
//音量发生变化 
- (void)oralEvaluation:(TAIOralEvaluation *)oralEvaluation onVolumeChanged:(NSInteger)volume 
{     
//回调录音分贝大小[0-120] 
}
```


### 4. 录制音频
#### 4.1 内部录制（SDK 内部录制音频并传输，推荐）
**4.1.1 初始化并设置相应参数**
初始化 TAIOraEvaluation 对象，并通过实例化对象 param 设置评测文本、客户 ID、密码等信息，详细参数信息请查看下文参数说明。
```
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init]; 
param.sessionId = [[NSUUIDUUID] UUIDString]; 
param.appId = @""; 
param.workMode = TAIOralEvaluationWorkMode_Once; 
param.evalMode = TAIOralEvaluationEvalMode_Sentence; 
param.storageMode = TAIOralEvaluationStorageMode_Disable; 
param.serverType = TAIOralEvaluationServerType_English; 
param.scoreCoeff = 1.0; 
param.fileType = TAIOralEvaluationFileType_Mp3; 
param.refText = @""; 
param.secretId = @""; 
param.secretKey = @"";
```

**4.1.2 开始录制**
调⽤ startRecordAndEvaluation（）⽅法传⼊步骤3.1.1中设置的 param 参数，并设置回调函数，即可开始录制。
```
[self.oralEvaluation startRecordAndEvaluation:param callback:^(TAIError *error)      
//结果返回 
}];
```

**4.1.3 结束录制**
```
[self.oralEvaluation stopRecordAndEvaluation:^(TAIError *error) {    
//结果返回 
}];
```

#### 4.2 外部录制（SDK 外部录制音频数据作为 API 调用参数）
上传外部录制音频数据时，调用 oralEvaluation 方法，传入实例化后的 TAIOralEvaluationParam 对象及 TAIoralEvationData 对象，并设置回调函数获取错误信息。
```objc
//初始化参数
TAIOralEvaluationParam *param = [[TAIOralEvaluationParam alloc] init]; 
param.sessionId = [[NSUUIDUUID] UUIDString]; 
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


NSString *mp3Path = [[NSBundlemainBundle] pathForResource:@"hello_guagua"ofType:@"mp3"]; 
TAIOralEvaluationData *data = [[TAIOralEvaluationData alloc] init]; 
data.seqId = 1; 
data.bEnd = YES; 
data.audio = [NSDatadataWithContentsOfFile:mp3Path]; 
__weak typeof(self) ws = self;    


//评测结束后是否重置AVAudioSession  true:重置  false:否 
[self.oralEvaluation resetAvAudioSession:true];    

//传输数据 
[self.oralEvaluation oralEvaluation:param data:data callback:^(TAIError *error) {     
    //接口调用结果返回 
}];

```
>!外部录制三种格式（mp3，wav/pcm，raw）目前仅支持16k采样率16bit编码单声道，如果有不一致可能会导致评估不准确或失败。



### 5. 签名
SecretKey 属于安全敏感参数，线上版本一般由业务后台生成 [临时 SecretKey](https://cloud.tencent.com/document/api/598/13896) 或者 SDK 外部签名返回到客户端。
临时签名 policy 示例如下：
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

### 输入参数
**TAIOralEvaluationParam 参数说明：**
相应参数详细说明见 [发音数据传输接口附带初始化过程（常用实践）](https://cloud.tencent.com/document/product/884/32605) 文档。

| 参数               | 类型                         | 必填           | 说明                                                         |
| :----------------- | :--------------------------- | :------------- | :----------------------------------------------------------- |
| appid              | NSString                     | 是             | 账号应用 ID                                                   |
| timeout            | NSInteger                    | 否             | 超时时间，默认30秒                                           |
| secretId           | NSString                     | 是             | 您在控制台获取的密钥 ID                                       |
| secretKey          | NSString                     | 内部签名：必填 | 您在控制台获取的密钥 Key，在使用内部签名时必须设置此参数      |
| signature          | NSString                     | 外部签名：必填 | 仅在使用外部签名时需要设置此参数，详细获取方式请查看上述5.签名 |
| timestamp          | NSInteger                    | 外部签名：必填 | 秒级时间戳                                                   |
| soeAppId           | NSString                     | 否             | 业务应用 ID                                                   |
| sessionId          | NSString                     | 是             | 一次评测唯一标识                                             |
| workMode           | TAIOralEvaluationWorkMode    | 是             | 传输方式                                                     |
| evalMode           | TAIOralEvaluationEvalMode    | 是             | 评测模式                                                     |
| isFixOn            | Bool                         | 是             | 用于设置是否开启单词映射                                     |
| fileType           | TAIOralEvaluationFileType    | 是             | 用于设置输入的语音文件类型                                   |
| storageMode        | TAIOralEvaluationStorageMode | 是             | 是否存储音频文件，用于设置是否存储及如何存储评测音频文件     |
| serverType         | TAIOralEvaluationServerType  | 是             | 评测语言类型，可选为中文或英文                               |
| scoreCoeff         | Float                        | 是             | 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数 |
| refText            | NSString                     | 是             | 被评估语音对应的文本                                         |
| sentenceInfoEnable | Bool                         | 是             | 输出断句中间结果标识                                         |
| audioPath          | NSString                     | 是             | 本地音频保存路径                                             |


**TAIORecorderParam 参数说明：**

| 参数        | 类型     | 必填 | 说明                                                     |
| :---------- | :------- | :--- | :------------------------------------------------------- |
| fragEnable  | Bool     | 否   | 是否开启分片，默认 YES                                    |
| fragSize    | NSString | 否   | 语音分片大小，默认1024，建议为1024的整数倍，范围[1k,10k] |
| vadEnable   | Bool     | 否   | 是否开启静音检测，默认 NO                                 |
| vadInterval | NSString | 否   | 静音检测时间间隔，单位为 ms                               |

**TAIOralEvaluationData 参数说明：**

| 参数|类型|说明 |
|---|---|---|
|seqId|NSInteger|分片序列号|
|bEnd|BOOL|是否最后一个分片|
|audio|NSData|音频数据|

### 返回结果参数


#### TAIOralEvaluationRet 参数说明：

| 参数            | 类型                                    | 说明                                                         |
| :-------------- | :-------------------------------------- | :-------------------------------- |
| sessionId       | NSString                                |    语音段唯一标识                                    |
| requestId      	| NSString	|   唯一请求 ID，每次请求都会返回  |
| pronAccuracy    | Float                                   | 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配          |
| pronFluency     | Float                                   | 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义         |
| pronCompletion  | Float                                   | 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义         |
| audioUrl        | NSString                                | 保存语音音频文件的下载地址（TAIOralEvaluationStorageMode.Enable 有效） |
| words           | NSArray<taioralevaluationword/*>        | 单词详细发音评估结果                                             |
| SuggestedScore  | Float                                   | 建议评分，取值范围[0,100]                                    |
| sentenceInfoSet | NSArray<TAIOralEvaluationSentenceInfo/*> | 断句中间结果，待用户发音完全结束后，系统会给出一个综合所有句子的整体结果  |


#### AIOralEvaluationWord 参数说明：

| 参数|类型|说明 |
|---|---|---|
| beginTime|Int | 当前单词语音起始时间点，单位为 ms |
| endTime|Int | 当前单词语音终止时间点，单位为 ms |
| pronAccuracy | Float | 单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配 |
| pronFluency | Float | 单词发音流利度，取值范围[0, 1] |
| word|NSString | 当前词 |
| matchTag | Int | 当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词 |
| phoneInfos	|	NSArray<TAIOralEvaluationPhoneInfo/*> | 音节评估详情<br> 注：在 EvalMode 为2，3，5时此参数为空 |
| referenceWord | NSString | 读音评估对应的单词 |

#### SentenceInfoSet 参数说明：

| 参数           | 类型                             | 说明                                                      |
| -------------- | -------------------------------- | --------------------------------------------------------- |
| sentenceId     | Int                              | 句子序号                                                  |
| words          | NSArray<taioralevaluationword *> | 单词粒度详细发音评估结果                                  |
| pronAccuracy   | Float                            | 音素发音准确度，取值范围[-1,   100]，当取-1时指完全不匹配 |
| pronFluency    | Float                            | 单词发音流利度，取值范围[0,   1]                          |
| pronCompletion | BOOL                             | 发音完整度，取值范围[0,   1]，当为词模式时，取值无意义    |
| suggestScore   | Float                            | 建议评分，取值范围[0,100]                                 |


#### TAIOralEvaluationPhoneInfo 参数说明：

| 参数           | 类型     | 说明                                                    |
| :------------- | :------- | :------------------------------------------------------ |
| beginTime      | Int      | 当前音素语音起始时间点，单位为 ms                        |
| endTime        | Int      | 当前音素语音终止时间点，单位为 ms                        |
| pronAccuracy   | Float    | 音素发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配 |
| detectedStress | BOOL     | 当前音素是否检测为重音                                  |
| phone          | NSString | 用户实际发音音素                                        |
| stress         | BOOL     | 用户实际发音音素是否应为重音                            |
| rLetter        | NSString | 音素对应的字母                                          |
| referencePhone | NSString | 参考音素，在单词诊断模式下，代表标准音素                |


#### TAIError 参数说明：

| 参数      | 类型       | 说明                                                         |
| :-------- | :--------- | :----------------------------------------------------------- |
| Code      | TAIErrCode | 返回错误码<br>0：成功<br>1：参数错误<br>2：json 解析错误<br>3：http 请求错误<br>4：服务器错误详细错误信息请查看 desc 参数 |
| desc      | NSString   | 详细错误描述                                                 |
| requestId | NSString   | 请求 ID，用于订单唯一标识                                   |












