##  概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高精准度的口语发音评测。腾讯云智聆口语评测支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
TAISDK 是一款封装了腾讯云教育 AI 能力的 SDK，通过集成 SDK，用户可以快速接入相关产品功能，如智聆口语评测、数学作业批改等。本文档介绍智聆口语评测 Android SDK 相关说明，通过封装 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口，实现音频录制和音频文件上传等功能，如需其他产品的调用说明，可在对应产品的产品文档查看。
>?本文档只对 Android SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。


## 流程图
![](https://main.qcloudimg.com/raw/adc1d339f5892577db7ab2c701ab8b06.jpg)

## SDK 集成准备

### 添加使用权限
本 SDK 需要以下权限：
```xml
android.permission.INTERNET
android.permission.RECORD_AUDIO
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
```

### 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在 **[访问管理](https://console.cloud.tencent.com/cam/overview) > 访问密钥  >  [API 密钥管理](https://console.cloud.tencent.com/cam/capi)** 中获取该凭证。
>!密钥属于敏感信息，正式密钥仅可在调试使用，线上环境情况下，为了防止他人盗取，应使用 [临时签名](https://cloud.tencent.com/document/product/884/31870#:~:text=%E5%88%B0%E5%AE%A2%E6%88%B7%E7%AB%AF%E3%80%82-,%E4%B8%B4%E6%97%B6%E7%AD%BE%E5%90%8D,-policy%20%E7%A4%BA%E4%BE%8B%E5%A6%82%E4%B8%8B)，具体请参考 [签名](https://cloud.tencent.com/document/product/884/31870#5.-.E7.AD.BE.E5.90.8D) 相关内容。

![](https://qcloudimg.tencent-cloud.cn/raw/3cb24b488a6d0d4e754c438d33a28e9e.png)

### 设备准备
一台电脑，一台 Android 系统的手机。

## SDK DEMO 使用流程
### 下载 demo
从 github 下载 TAISDK [demo](https://github.com/TencentCloud/tencentcloud-sdk-android-soe)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-android-soe.git
```
如果无法使用 git 或不清楚如何使用，可以单击 [这里](https://github.com/TencentCloud/tencentcloud-sdk-android-soe/archive/refs/heads/master.zip) 下载。

### 导入项目
使用 Android Studio（也可以使用其他开发工具）打开 demo 文件的 TAIDemo 目录，选择 Trust Project（信任项目）开始编译。
### 填写密钥
在 `app/java/com.tencent.taidemo/PrivateInfo` 下填写 appId、secretId 和 secretKey。[TAIOralEvaluationParam 参数说明](https://cloud.tencent.com/document/product/884/31870#:~:text=TAIOralEvaluationParam%20%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%EF%BC%9A)。
![](https://qcloudimg.tencent-cloud.cn/raw/21d92b3c38ade2c2100a6cb53c4eebd9.png)
### 运行项目
连接手机，打开开发者模式，点击 run 运行项目。下载 App 进行真机调试。由于模拟器无法获取录音权限，所以不推荐使用模拟器调试。

### 使用 demo
打开 App 选择口语评测。
![](https://qcloudimg.tencent-cloud.cn/raw/7d00226b771d651433d05e8e0a8c6df5.png)
设置评测参数后，选择开始录音或者外部 MP3文件。
![](https://qcloudimg.tencent-cloud.cn/raw/65b1f88eaa3ec22d8181ae1566e97bc6.png)

## SDK 使用方法
### 版本设置
demo 默认为当前最新版本，如果后续更新或使用老版本可以在 Gradle Scripts/build.grade 中修改依赖包。
![](https://qcloudimg.tencent-cloud.cn/raw/c44d98a996d483ec07fdec4a1eaa2b27.png)
![](https://qcloudimg.tencent-cloud.cn/raw/6ea4991d11f3af951838294ac7d90458.png)

### 接口调用
1. 声明并定义对象：
```
private TAIOralEvaluation oral = new TAIOralEvaluation();
```
2. 设置数据回调：
```
this.oral.setListener(new TAIOralEvaluationListener() {
    @Override
    public void onEvaluationData(final TAIOralEvaluationData data, final TAIOralEvaluationRet result, final TAIError error) {
        //数据和结果回调（只有data.bEnd为true，result有效）
    }
});
```
>! 请在开始录制音频前设置回调函数，您将通过 `TAIOralEvaluationListener` 接口中的 `onEvaluationData` 函数获取语音评测结果和错误信息。
>
```
public interface TAIOralEvaluationListener{
    void onEvaluationData(TAIOralEvaluationData data, TAIOralEvaluationRet result, TAIError error);
    void onFinalEvaluationData(TAIOralEvaluationData data, TAIOralEvaluationRet result, TAIError error);
    void onEndOfSpeech();
    void onVolumeChanged(int volume);
}
```

### 静音检测设置
1. 初始化 TAIRecorderParam 对象，并配置相关参数：
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
2. 上层通知
当检测到静音或者录音分贝变化时，通过 TAIOralEvaluationListenner 通知上层。
```
//检测到静音
@Override public void onEndOfSpeech() {     
    //这里可以根据业务逻辑处理，如停止录音或提示用户 
}  
    //音量发生变化
public void onVolumeChanged(finalint volume) {     
    //回调录音分贝大小[0-120] ，默认20
}
```

### 录制音频
#### 内部录制（SDK 内部录制音频并传输，推荐）
1. 初始化并设置相应参数
初始化 TAIOraEvaluation 对象，并通过实例化对象 param 设置评测文本、客户 ID、密码等信息，详细参数信息请查看下文参数说明。
```
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
param.token = "";
```
2. 开始录制
调用 startRecordAndEvaluation() 方法传入 TAIOralEvaluationParam 的 param 参数，并设置回调函数，即可开始录制。
```
//开始录制
this.oral.startRecordAndEvaluation(param, new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});

```
3. 结束录制
```
//结束录制
this.oral.stopRecordAndEvaluation(new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});
```

#### 外部录制（SDK 外部录制音频数据作为 API 调用参数）
上传外部录制音频数据时，调用 oralEvaluation() 方法，传入实例化后的 TAIOralEvaluationParam 对象及 TAIoralEvationData 对象，并设置回调函数获取错误信息。
```
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
param.token = "";

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
>! 外部录制三种格式（mp3、wav、raw/pcm）目前仅支持16k 采样率16bit 编码单声道，如果有不一致可能会导致评估不准确或失败。

### 签名
#### 临时签名（推荐）
SecretKey 属于安全敏感参数，线上版本一般由业务后台生成 [临时 SecretKey](https://cloud.tencent.com/document/product/1312/48195) 或者 SDK 外部签名返回到客户端。
智聆口语评测 [获取联合身份临时访问凭证](https://cloud.tencent.com/document/product/1312/48195) 请求参数参考：
```
Name = "soe",
Policy = "{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\",\"action\": [\"soe:TransmitOralProcessWithInit\"],\"resource\": \"*\"}}"
```
获取到临时凭证，需要填入 Token，TmpSecretId（请求参数 SecretId），TmpSecretKey（请求参数 SecretKey）。临时凭证默认半小时有效期，需要重复获取。
#### 内部签名（推荐）
SDK 内部通过用户提供的 SecretKey 和 SecretId 计算签名，用户无需关心签名细节。
#### 外部签名（不推荐）
SDK 外部调用 getStringToSign 获取签名字符串，然后根据 [计算签名](https://cloud.tencent.com/document/product/884/30657#3.-.E8.AE.A1.E7.AE.97.E7.AD.BE.E5.90.8D) 进行签名。口语评测时需提供 SecretId、timestamp 和 signature 参数。
```
//获取签名所需字符串
public String getStringToSign(long timestamp);
```
>! 时间戳 timestamp 必须和 TAIEvaluationParam 参数的 timestamp 一致。

## 参数说明
### 输入参数
#### TAIOralEvaluationParam 参数说明：
相应参数详细说明见 [发音数据传输接口附带初始化过程（常用实践）](https://cloud.tencent.com/document/product/884/32605) 文档。

| 参数               | 类型                         | 必填           | 说明                                                         |
| :----------------- | :--------------------------- | :------------- | :----------------------------------------------------------- |
| context            | Context                      | 是             | 上下文                                                       |
| AppID              | String                       | 是             | 账号应用 ID                                                   |
| timeout            | Int                          | 否             | 超时时间，默认30秒                                           |
| secretId           | String                       | 是             | 您在控制台获取的密钥 ID，临时密钥的 TmpSecretId                                    |
| secretKey          | String                       | 内部签名：必填 | 您在控制台获取的密钥 Key，临时密钥的 TmpSecretKey      |
| token     | 	String	| 临时签名：必填	| 临时密钥的 Token，仅在使用临时签名时需要设置此参数，详细获取方式请查看 [签名](https://cloud.tencent.com/document/product/884/31870#5.-.E7.AD.BE.E5.90.8D)| 
| signature          | String                       | 外部签名：必填 | 仅在使用外部签名时需要设置此参数，详细获取方式请查看 [签名](https://cloud.tencent.com/document/product/884/31870#5.-.E7.AD.BE.E5.90.8D) |
| timestamp          | Long                         | 外部签名：必填 | 秒级时间戳                                                   |
| soeAppId           | String                       | 否             | 业务应用 ID，与账号应用 AppID 无关，是用来方便客户管理服务的参数 |
| sessionId          | String                       | 是             | 一次评测唯一标识                                             |
| workMode           | TAIOralEvaluationWorkMode    | 是             | 语音输入模式，用于设置是否流式分片传输，推荐使用流式分片传输 |
| evalMode           | TAIOralEvaluationEvalMode    | 是             | 评测模式                                                     |
| isFixOn            | Boolean                      | 是             | 用于设置是否开启单词映射                                     |
| fileType           | TAIOralEvaluationFileType    | 是             | 用于设置输入的语音文件类型                                   |
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

## 错误码
参考 API 文档 [错误码](https://cloud.tencent.com/document/api/884/30658)。


## 常见问题
### 关于混淆规则
SDK 内部有做混淆规则，不需要再次混淆。暂不提供混淆方法。

### 使用 AndroidSDK 出现内存溢出的问题?	
设备内存不足，可以尝试使用分片传输。

### Android 端报 java.security.cert.CertPathValidatorException：Trustanchorforcertificationpathnotfound？	
1. 如果在请求服务器签名证书的阶段网络不稳定会导致 tls 连接失败。
2. 是否设置了代理，设置了代理会导致出现这个问题。

