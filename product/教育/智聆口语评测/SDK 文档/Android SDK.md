
##  概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。腾讯云智聆口语评测支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
TAISDK 是一款封装了腾讯云教育 AI 能力的 SDK，通过集成 SDK，用户可以快速接入相关产品功能，如智聆口语评测、数学作业批改等。本文档介绍智聆口语评测 Android SDK 相关说明，如需其他产品的调用说明，可在对应产品的产品文档查看。
本文档只对 Android SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。
单击 [示例链接](https://tec.qq.com/ai/soe#demos) 在线体验智聆口语评测 demo。

## 总体流程
### 1. 流程图
![](https://main.qcloudimg.com/raw/adc1d339f5892577db7ab2c701ab8b06.jpg)

### 2. 集成 demo 示例
[下载 SDK](https://github.com/TencentCloud/tencentcloud-sdk-android-soe) 地址。
获取密钥（ 密钥获取⽅式⻅下⽂） 后到
`tencentcloud-sdk-androidsoe/TAIDemo/app/src/main/java/com/tencent/taidemo/PrivateInfo.java` 
根据需要填写 AppId、secretId、secretKey、soeAppId 和 hcmAppId（token 不需要填写）。
![](https://main.qcloudimg.com/raw/ce5b479bbcb7497b46d630f266c6a28c.jpg)



## SDK 集成准备

### 1. 添加使用权限
本 SDK 需要以下权限：
```xml
android.permission.INTERNET
android.permission.RECORD_AUDIO
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
```

### 2. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在**[访问管理](https://console.cloud.tencent.com/cam/overview)**>**访问密钥**>**[API 密钥管理](https://console.cloud.tencent.com/cam/capi)**中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png)


## SDK 集成步骤

### 1. 导入 SDK
下载 [Demo 源码](https://github.com/TencentCloud/tencentcloud-sdk-android-soe)，并在 build.gradle 引入依赖包。
```java
implementation 'com.tencent.edu:TAISDK:1.2.3.58'
```

### 2. 接口调用
#### 2.1 声明并定义对象：
```java
private TAIOralEvaluation oral = new TAIOralEvaluation();
```

#### 2.2 设置数据回调：
```java
this.oral.setListener(new TAIOralEvaluationListener() {
    @Override
    public void onEvaluationData(final TAIOralEvaluationData data, final TAIOralEvaluationRet result, final TAIError error) {
        //数据和结果回调（只有data.bEnd为true，result有效）
    }
});
```

>!请在开始录制音频前设置回调函数，您将通过 TAIOralEvaluationListener 接口中的 onEvaluationData 函数获取语音评测结果和错误信息。

<dx-codeblock>
::: java java
public interface TAIOralEvaluationListener{
    void onEvaluationData(TAIOralEvaluationData data, TAIOralEvaluationRet result, TAIError error);
    void onFinalEvaluationData(TAIOralEvaluationData data, TAIOralEvaluationRet result, TAIError error);
    void onEndOfSpeech();
    void onVolumeChanged(int volume);
}
:::
</dx-codeblock>



### 3. 静音设置
#### 3.1 初始化 TAIRecorderParam 对象，并配置相关参数
请在开始调用 startRecordAndEvaluation() 函数前设置 TAIRecorderParam 参数，静音检测您可以通过 vadEnable 参数打开，并通过 vadInterval 参数设置静音检测时间间隔。
```
//在开始调用`startRecordAndEvaluation`前设置录制参数
recordParam = new TAIRecorderParam(); 
recordParam.fragSize =1024; 
recordParam.fragEnable =true; 
recordParam.vadEnable =true; 
recordParam.vadInterval =5000; 
this.oral.setRecorderParam(recordParam);
```


#### 3.2 上层通知
当检测到静音或者录音分贝变化时，通过 TAIOralEvaluationListenner 通知上层。
```
//检测到静音
@Override public void onEndOfSpeech() {     
    //这里可以根据业务逻辑处理，如停止录音或提示用户 
}  
    //音量发生变化
public void onVolumeChanged(finalint volume) {     
    //回调录音分贝大小[0-120] 
}
```

###  4. 录制音频
#### 4.1 内部录制（SDK 内部录制音频并传输，推荐）
**4.1.1 初始化并设置相应参数**
初始化 TAIOraEvaluation 对象，并通过实例化对象 param 设置评测文本、客户 ID、密码等信息，详细参数信息请查看下文参数说明。
```java
//初始化参数
TAIOralEvaluationParam param = new TAIOralEvaluationParam();
param.context = this;
param.appId = "";
param.sessionId = UUID.randomUUID().toString();
param.workMode = TAIOralEvaluationWorkMode.ONCE;
param.evalMode = TAIOralEvaluationEvalMode.SENTENCE;
param.storageMode = TAIOralEvaluationStorageMode.DISABLE;
param.serverType = TAIOralEvaluationServerType.ENGLISH;
param.fileType = TAIOralEvaluationFileType.MP3;
param.scoreCoeff = 1.0;
param.refText = "";
param.secretId = "";
param.secretKey = "";
```

**4.1.2 开始录制**
调用 startRecordAndEvaluation（）方法传入步骤4.1.1中设置的 param 参数，并设置回调函数，即可开始录制。
```
//开始录制
this.oral.startRecordAndEvaluation(param, new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});
```

**4.1.3 结束录制**
```
//结束录制
this.oral.stopRecordAndEvaluation(new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});
```

#### 4.2 外部录制（SDK 外部录制音频数据作为 API 调用参数）
上传外部录制音频数据时，调用 oralEvaluation() 方法，传入实例化后的 TAIOralEvaluationParam 对象及 TAIoralEvationData 对象，并设置回调函数获取错误信息。
```java
//初始化参数
TAIOralEvaluationParam param = new TAIOralEvaluationParam();
param.context = this;
param.appId = "";
param.sessionId = UUID.randomUUID().toString();
param.workMode = TAIOralEvaluationWorkMode.ONCE;
param.evalMode = TAIOralEvaluationEvalMode.SENTENCE;
param.storageMode = TAIOralEvaluationStorageMode.DISABLE;
param.serverType = TAIOralEvaluationServerType.ENGLISH;
param.fileType = TAIOralEvaluationFileType.MP3;
param.scoreCoeff = 1.0;
param.refText = "hello guagua";
param.secretId = "";
param.secretKey = "";
//传输数据
try{
    InputStream is = getAssets().open("hello_guagua.mp3");
    byte[] buffer = new byte[is.available()];
    is.read(buffer);
    is.close();
    TAIOralEvaluationData data = new TAIOralEvaluationData();
    data.seqId = 1;
    data.bEnd = true;
    data.audio = buffer;
    this.oral.oralEvaluation(param, data, new TAIOralEvaluationCallback() {
        @Override
        public void onResult(final TAIError error) {
            //接口调用结果返回
        }
    });
}
catch (Exception e){
}
```
>!外部录制三种格式（mp3、wav/pcm、raw）目前仅支持16k采样率16bit编码单声道，如果有不一致可能会导致评估不准确或失败。


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

```java
//获取签名所需字符串
public String getStringToSign(long timestamp);
```
>!时间戳 timestamp 必须和 TAIEvaluationParam 参数的 timestamp 一致。



## 参数说明



### 输入参数
#### TAIOralEvaluationParam 参数说明：
相应参数详细说明见 [发音数据传输接口附带初始化过程（常用实践）](https://cloud.tencent.com/document/product/884/32605) 文档。

| 参数               | 类型                         | 必填           | 说明                                                         |
| :----------------- | :--------------------------- | :------------- | :----------------------------------------------------------- |
| context            | Context                      | 是             | 上下文                                                       |
| AppID              | String                       | 是             | 账号应用 ID                                                   |
| timeout            | Int                          | 否             | 超时时间，默认30秒                                           |
| secretId           | String                       | 是             | 您在控制台获取的密钥 ID                                       |
| secretKey          | String                       | 内部签名：必填 | 您在控制台获取的密钥 Key，在使用内部签名时必须设置此参数      |
| signature          | String                       | 外部签名：必填 | 仅在使用外部签名时需要设置此参数，详细获取方式请查看上述5.签名 |
| timestamp          | Long                         | 外部签名：必填 | 秒级时间戳                                                   |
| soeAppId           | String                       | 否             | 业务应用 ID，与账号应用 AppID 无关，是用来方便客户管理服务的参数 |
| sessionId          | String                       | 是             | 一次评测唯一标识                                             |
| workMode           | TAIOralEvaluationWorkMode    | 是             | 语音输入模式，用于设置是否流式分片传输，推荐使用流式分片传输 |
| evalMode           | TAIOralEvaluationEvalMode    | 是             | 评测模式                                                     |
| isFixOn            | Boolean                      | 是             | 用于设置是否开启单词映射                                     |
| fileType           | TAIOralEvaluationFileType    | 是             | 用于设置输入的语音文件类型                                   |
| storageMode        | TAIOralEvaluationStorageMode | 是             | 是否存储音频文件，用于设置是否存储及如何存储评测音频文件     |
| serverType         | TAIOralEvaluationServerType  | 是             | 评测语言类型，可选为中文或英文                               |
| scoreCoeff         | Double                       | 是             | 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数 |
| refText            | String                       | 是             | 被评估语音对应的文本                                         |
| sentenceInfoEnable | Boolean                      | 是             | 输出断句中间结果标识                                         |
| audioPath          | String                       | 是             | Android 本地音频保存路径                                      |

#### TAIORecorderParam 参数说明：

| 参数        | 类型    | 必填 | 说明                                                     |
| :---------- | :------ | :--- | :------------------------------------------------------- |
| fragEnable  | Boolean | 否   | 是否开启分片，默认 YES                                    |
| fragSize    | Int     | 否   | 语音分片大小，默认1024，建议为1024的整数倍，范围[1k,10k] |
| vadEnable   | Boolean | 否   | 是否开启静音检测，默认 NO                                 |
| vadInterval | Int     | 否   | 静音检测时间间隔，单位为 ms                               |



#### TAIOralEvaluationData 参数说明：

| 参数   | 类型    | 说明             |
| :----- | :------ | :--------------- |
| seqId  | Int     | 分片序列号       |
| bEnd   | Boolean | 是否最后一个分片 |
| audio  | byte[]  | 音频数据         |
| length | Long    | 音频数据长度     |

### 返回结果参数
#### TAIOralEvaluationRet 参数说明：

| 参数|类型|说明 |
|---|---|---|
|sessionId|String|语音段唯一标识|
|   requestId	 |  String	  | 唯一请求 ID，每次请求都会返回|
|pronAccuracy|Double|发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|Double|发音流利度，取值范围[0, 1]，当为词模式时，取值无意义|
|pronCompletion|Double|发音完整度，取值范围[0, 1]，当为词模式时，取值无意义|
|audioUrl|String|保存语音音频文件的下载地址（TAIOralEvaluationStorageMode.Enable 有效）|
|words|List<TAIOralEvaluationWord>|单词详细发音评估结果|
|SuggestedScore | Double |  建议评分，取值范围[0,100] |
|sentenceInfoSet |List<TAIOralEvaluationWord>| 断句中间结果，待用户发音完全结束后，系统会给出一个综合所有句子的整体结果 |
	

#### TAIOralEvaluationWord 参数说明：

| 参数|类型|说明 |
|---|---|---|
|beginTime|Int|当前单词语音起始时间点，单位为ms|
|endTime|Int|当前单词语音终止时间点，单位为ms|
|pronAccuracy|Double|单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|Double|单词发音流利度，取值范围[0, 1]|
|word|String|当前词|
|matchTag|Int|当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词|
|phoneInfos	|List|	音素评估详情 <br>注：在 EvalMode 为2，3，5时此参数为空 |
|referenceWord	| String |	读音评估对应的单词 |

#### SentenceInfoSet 参数说明：

| 参数           | 类型    | 说明                                                      |
| -------------- | ------- | --------------------------------------------------------- |
| sentenceId     | Int     | 句子序号                                                  |
| words          | List    | 单词粒度详细发音评估结果                                  |
| pronAccuracy   | Double  | 音素发音准确度，取值范围[-1,   100]，当取-1时指完全不匹配 |
| pronFluency    | Double  | 单词发音流利度，取值范围[0,   1]                          |
| pronCompletion | Boolean | 发音完整度，取值范围[0,   1]，当为词模式时，取值无意义    |
| suggestScore   | Double  | 建议评分，取值范围[0,100]                                 |
	
#### TAIOralEvaluationPhoneInfo 参数说明：

| 参数           | 类型    | 说明                                                    |
| :------------- | :------ | :------------------------------------------------------ |
| beginTime      | Int     | 当前音素语音起始时间点，单位为 ms                        |
| endTime        | Int     | 当前音素语音终止时间点，单位为 ms                        |
| pronAccuracy   | Double  | 音素发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配 |
| detectedStress | Boolean | 当前音素是否检测为重音                                  |
| phone          | String  | 用户实际发音音素                                        |
| stress         | Boolean | 用户实际发音音素是否应为重音                            |
| rLetter        | String  | 音素对应的字母                                          |
| referencePhone | String  | 参考音素，在单词诊断模式下，代表标准音素                |



#### TAIError 参数说明：

| 参数      | 类型   | 说明                                                         |
| :-------- | :----- | :----------------------------------------------------------- |
| Code      | Int    | 返回错误码<br>0：成功<br>1：参数错误<br>2：json 解析错误<br>3：http 请求错误<br>4：服务器错误详细错误信息请查看 desc 参数 |
| desc      | String | 详细错误描述                                                 |
| requestId | String | 请求 ID，用于订单唯一标识                                   |

