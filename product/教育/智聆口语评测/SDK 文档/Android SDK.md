
##  概述
腾讯云智聆口语评测（英文版）（Smart Oral Evaluation-English，SOE-E）是腾讯云推出的语音评测产品，是基于英语口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的英语口语发音评测。腾讯云智聆口语评测（英文版）支持单词和句子模式的评测，多维度反馈口语表现，可广泛应用于英语口语类教学应用中。
TAISDK是一款封装了腾讯云教育AI能力的SDK，通过集成SDK，用户可以快速接入相关产品功能，如数学作业批改、智聆口语评测等。本文档介绍智聆口语评测Android SDK相关说明，如需其他产品的调用说明，可到对应产品的产品文档查看。

本文档只对 Android SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 使用说明
#### 工程及 Demo 源码
[工程及 Demo 源码的 GitHub 地址>>](https://github.com/TencentCloud/tencentcloud-sdk-android-soe)
本 SDK 的主文件为 tencentsoe-sdk-release.aar，直接引入项目中即可。
- 如果您需要调用 MP3录音功能，则还需引入 mp3recorder.aar。
- 如果您需要运行 Demo，请对 SECRET_ID 和 SECRET_KEY 赋值。

####  第三方库依赖
本 SDK 依赖以下第三方库：
```gradle
implementation 'com.squareup.okhttp3:okhttp:3.11.0'
implementation 'com.google.code.gson:gson:2.8.5'
```
#### 使用权限
本 SDK 需要以下权限：
```xml
android.permission.INTERNET
android.permission.RECORD_AUDIO
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
```


### 一、获取密钥

secretId和secretKey是使用SDK的安全凭证，通过以下方式获取

![](http://dldir1.qq.com/hudongzhibo/taisdk/document/taisdk_cloud_1.png)


### 二、SDK集成

#### 1、导入SDK

[Demo源码下载](https://github.com/TencentCloud/tencentcloud-sdk-android-soe)

在build.gradle引入依赖包

```java
implementation 'com.tencent.taisdk:taisdk:1.2.0.59'
```

#### 2、接口调用



##### 智聆口语评测

```java
//一、声明并定义对象
private TAIOralEvaluation oral = new TAIOralEvaluation();
```

```java
//二、设置数据回调
this.oral.setListener(new TAIOralEvaluationListener() {
    @Override
    public void onEvaluationData(final TAIOralEvaluationData data, final TAIOralEvaluationRet result, final TAIError error) {
        //数据和结果回调（只有data.bEnd为true，result有效）
    }
});
```

* 内部录制（SDK内部录制音频并传输，推荐）

```java
//三、初始化参数
TAIOralEvaluationParam param = new TAIOralEvaluationParam();
param.context = this;
param.appId = "";
param.sessionId = String.format("%d", System.currentTimeMillis() / 1000);
param.workMode = TAIOralEvaluationWorkMode.ONCE;
param.evalMode = TAIOralEvaluationEvalMode.SENTENCE;
param.storageMode = TAIOralEvaluationStorageMode.DISABLE;
param.serverType = TAIOralEvaluationServerType.ENGLISH;
param.fileType = TAIOralEvaluationFileType.MP3;//只支持mp3
param.scoreCoeff = 1.0;
param.refText = "";
param.secretId = "";
param.secretKey = "";
//四、开始录制
this.oral.startRecordAndEvaluation(param, new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});

```

```java
//五、结束录制
this.oral.stopRecordAndEvaluation(new TAIOralEvaluationCallback() {
    @Override
    public void onResult(final TAIError error) {
        //结果返回
    }
});
```


* 外部录制（SDK外部录制音频数据作为Api调用参数）


```java
//三、初始化参数
TAIOralEvaluationParam param = new TAIOralEvaluationParam();
param.context = this;
param.appId = "";
param.sessionId = String.format("%d", System.currentTimeMillis() / 1000);
param.workMode = TAIOralEvaluationWorkMode.ONCE;
param.evalMode = TAIOralEvaluationEvalMode.SENTENCE;
param.storageMode = TAIOralEvaluationStorageMode.DISABLE;
param.serverType = TAIOralEvaluationServerType.ENGLISH;
param.fileType = TAIOralEvaluationFileType.MP3;//只支持mp3
param.scoreCoeff = 1.0;
param.refText = "hello guagua";
param.secretId = "";
param.secretKey = "";
//四、传输数据
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

注意事项

> 外部录制三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败


#### 3、签名

secretKey属于安全敏感参数，线上版本一般由业务后台生成[临时secretKey](https://cloud.tencent.com/document/api/598/13895)或者SDK外部签名返回到客户端。

>（1）内部签名：sdk内部通过用户提供的secretKey和secretId计算签名，用户无需关心签名细节

>（2）外部签名：sdk外部调用getStringToSign获取签名字符串，然后根据[签名规则（参考步骤三）](https://cloud.tencent.com/document/product/884/30657) 进行签名。口语评测时需提供secretId、timestamp和signature参数

```java
//获取签名所需字符串
public String getStringToSign(long timestamp);
```

注意事项

>时间戳timestamp必须和TAIEvaluationParam参数的timestamp一致



#### 4、参数说明

##### 公共参数
* TAICommonParam参数说明

| 参数|类型|必填|说明 |
|---|---|---|---|
|context|Context|是|上下文|
|appId|String|是|appId|
|timeout|int|否|超时时间，默认30秒|
|secretId|String|是|密钥Id|
|secretKey|String|内部签名：必填|密钥Key|
|signature|String|外部签名：必填|签名|
|timestamp|long|外部签名：必填|秒级时间戳|


* TAIError参数说明

| 参数|类型|说明 |
|---|---|---|
|code|int|错误码|
|desc|String|错误描述|
|requestId|String|请求id，定位错误信息|



##### 智聆口语评测

* TAIOralEvaluationParam参数说明

| 参数|类型|必填|说明 |
|---|---|---|---|
|sessionId|String|是|一次批改唯一标识|
|workMode|TAIOralEvaluationWorkMode|是|传输方式|
|evalMode|TAIOralEvaluationEvalMode|是|评测模式|
|fileType|TAIOralEvaluationFileType|是|数据格式（目前支持mp3）|
|storageMode|TAIOralEvaluationStorageMode|是|是否存储音频文件|
|serverType|TAIOralEvaluationServerType|是|语言类型|
|scoreCoeff|double|是|苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段|
|refText|String|是|被评估语音对应的文本|

* TAIOralEvaluationData参数说明

| 参数|类型|说明 |
|---|---|---|
|seqId|NSInteger|分片序列号|
|bEnd|BOOL|是否最后一个分片|
|audio|NSData|音频数据|


* TAIMathCorrectionRet参数说明

| 参数|类型|说明 |
|---|---|---|
|sessionId|String|一次批改唯一标识|
|pronAccuracy|double|发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|double|发音流利度，取值范围[0, 1]，当为词模式时，取值无意义|
|pronCompletion|double|发音完整度，取值范围[0, 1]，当为词模式时，取值无意义|
|audioUrl|String|保存语音音频文件的下载地址（TAIOralEvaluationStorageMode.Enable有效）|
|words|List<TAIOralEvaluationWord>|详细发音评估结果|

* TAIOralEvaluationWord参数说明

| 参数|类型|说明 |
|---|---|---|
|beginTime|int|当前单词语音起始时间点，单位为ms|
|endTime|int|当前单词语音终止时间点，单位为ms|
|pronAccuracy|double|单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配|
|pronFluency|double|单词发音流利度，取值范围[0, 1]|
|word|String|当前词|
|matchTag|int|当前词与输入语句的匹配情况，0:匹配单词、1：新增单词、2：缺少单词|

