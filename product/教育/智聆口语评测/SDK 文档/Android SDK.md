
##  概述
腾讯云智聆口语评测（英文版）（Smart Oral Evaluation-English，SOE-E）是腾讯云推出的语音评测产品，是基于英语口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的英语口语发音评测。腾讯云智聆口语评测（英文版）支持单词和句子模式的评测，多维度反馈口语表现，可广泛应用于英语口语类教学应用中。
本 SDK 为智聆口语测评（英文版）的 Android 版本，封装了对智聆口语测评（英文版）网络 API 的调用及本地音频文件处理，并提供简单的录音功能，使用者可以专注于从业务切入，方便简洁地进行二次开发。
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
#### 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在【[访问管理](https://console.cloud.tencent.com/cam/overview)】>【云 API 密钥】>【[API 密钥管理](https://console.cloud.tencent.com/cam/capi)】中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png)

##  使用示例
####  开始录音
```java
TencentSOE.startRecordMp3(Environment.getExternalStorageDirectory().getAbsolutePath() + "/SOE/", "soe");
```
####  停止录音
```java
TencentSOE.stopRecord();
```
####  验证 MP3文件格式
```java
String filePath = Environment.getExternalStorageDirectory().getAbsolutePath() + "/SOE/soe.mp3";
try {
    TencentSOE.checkMP3Format(filePath);
} catch (Exception e) {
    sendMessage(MSG_ERROR, e.getMessage());
}
```
#### 文件转 Base64字串
```java
String base64String = TencentSOE.encodeAudioFile(filePath);
```
#### 文件转 Base64字串数组
```java
ArrayList<String> base64StringArray = TencentSOE.encodeAudioFile(filePath, 512 * 1024);
```
#### 创建回调
```java
private SOECallback callback = new SOECallback() {
    public void onInitSuccess(InitOralProcessResponse response) {
        sendMessage(MSG_INIT_OK, response.toString());
    }

    public void onTransmitSuccess(int index, int isEnd, TransmitOralProcessResponse response) {
        Message msg = new Message();
        msg.what = MSG_TRANSMIT_OK;
        msg.arg1 = index;
        msg.arg2 = isEnd;
        msg.obj = response.toString();
        mMyHandler.sendMessage(msg);
    }

    public void onError(SOEError e) {
        sendMessage(MSG_INIT_ERROR, e.getMessage());
    }
};
```
#### 执行一次性评估
```java
String filePath = Environment.getExternalStorageDirectory().getAbsolutePath() + "/SOE/soe.wav";
String base64String = TencentSOE.encodeAudioFile(filePath);
TencentSOE.newInstance(SECRET_ID, SECRET_KEY)
          .setRefText(RefText)
          .setEvalMode(TencentSOE.EVAL_MODE_WORD)
          .setScoreCoeff(1.0f)
          .setVoiceFileType(TencentSOE.AUDIO_TYPE_WAV)
          .setUserVoiceData(base64String)
          .execute(callback);
```
#### 执行流式评估
```java
String filePath = Environment.getExternalStorageDirectory().getAbsolutePath() + "/SOE/soe.wav";
ArrayList<String> base64StringArray = TencentSOE.encodeAudioFile(filePath, 512 * 1024);
TencentSOE.newInstance(SECRET_ID, SECRET_KEY)
          .setRefText(RefText)
          .setEvalMode(TencentSOE.EVAL_MODE_WORD)
          .setScoreCoeff(1.0f)
          .setVoiceFileType(TencentSOE.AUDIO_TYPE_WAV)
          .setUserVoiceData(base64StringArray)// 或直接setUserVoiceData(filePath, 512 * 1024)
          .execute(callback);
```
#### 开启边录边传
```java
TencentSOE.newInstance(SECRET_ID, SECRET_KEY)
        .setRootUrl("soe.ap-guangzhou.tencentcloudapi.com/")// 非必要
        .setRegion("ap-guangzhou")// 非必要
        .setSoeAppId("default")// 非必要
        .setRefText(RefText)
        .setEvalMode(evalMode)
        .setWorkMode(TencentSOE.WORK_MODE_STREAM)
        .setScoreCoeff(1.0f)
        .setVoiceFileType(TencentSOE.AUDIO_TYPE_MP3)
        .setIsLongLifeSession(TencentSOE.SESSION_LIFE_SHORT)
        .setCallBack(callback)
        .startFrameRecord();
```
#### 停止边录边传
```java
TencentSOE.stopFrameRecord();
```
## 接口设计说明
本 SDK 的主入口类为 TencentSOE，以下方法皆从该类中调用。
本 SDK 支持链式调用，如无特殊说明，所有方法的返回值皆为 TencentSOE 实例。
- **TencentSOE newInstance（String SECRET_ID，String SECRET_KEY）**
功能：初始化。
参数：使用者为自己应用申请的 SecretId 和 SecretKey。
- **TencentSOE setRootUrl（String rootUrl）**
功能：设置测评服务地址。
参数：rootUrl 服务地址。
- **TencentSOE setRefText（String refText）**
功能：设置被评估语音对应的文本。
参数：refText 被评估语音对应的文本。
- **TencentSOE setWorkMode（Int workMode）**
功能：设置语音输入模式。
参数：workMode 语音输入模式，可选以下值。
 - TencentSOE.WORK_MODE_STREAM：流式分片。
 - TencentSOE.WORK_MODE_ONCE：非流式一次性评估。
- **TencentSOE setEvalMode（Int evalMode）**
功能：设置评估模式。
参数：evalMode 评估模式，可选以下值。
 - TencentSOE.EVAL_MODE_WORD：词模式，提供每个音节的评估信息。
 - TencentSOE.EVAL_MODE_SENTENCE：句子模式，提供完整度和流利度信息。
- **TencentSOE setScoreCoeff（Float scoreCoeff）**
功能：设置评价苛刻指数。
参数：scoreCoeff 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段。
- **TencentSOE setIsLongLifeSession（Int isLongLifeSession）**
功能：设置长效 session 标识。
参数：isLongLifeSession 当该参数为1时，session 的持续时间为300s，但会一定程度上影响第一个数据包的返回速度。
- **TencentSOE setVoiceFileType（Int voiceFileType）**
功能：设置语音文件类型。
参数：voiceFileType 语音文件类型，可选以下值。
 - TencentSOE.AUDIO_TYPE_RAW：Raw 格式。
 - TencentSOE.AUDIO_TYPE_WAV：Wav 格式。
 - TencentSOE.AUDIO_TYPE_MP3：Mp3格式（仅支持16k 采样率、16bit 编码、单声道）。
- **TencentSOE setRegion（String region）**
功能：设置公共参数。
参数：region 公共参数。
- **TencentSOE setSoeAppId（String soeAppId）**
功能：设置业务应用 ID。
参数：soeAppId 业务应用 ID，与账号应用 APPID 无关，是用来方便客户管理服务的参数，需要结合控制台使用。
- **boolean checkMP3Format（String path）**
功能：校验 MP3文件的采样率和声道。音频比特率过高会影响传输速度，建议不超过32kbps。
参数：path 音频文件路径。
返回：文件合规则返回 true，否则返回 false。
- **void startRecordWav（String path，String name）**
功能：启动 Wav 录制。
参数：
 - path：音频文件保存路径，须以`/`结尾。
 - name：音频文件保存名称，无须后缀名。
- **void startRecordMp3（String path, String name）**
功能：启动 MP3录制。
参数：
 - path 音频文件保存路径，须以`/`结尾。
 - name 音频文件保存名称，无须后缀名。
- **void stopRecord()**
功能：停止录音并在 startRecord 指定的位置保存 Wav 格式的音频文件。
- **String encodeAudioFile（String path）**
功能：将文件转成 base64字符串。
参数：path 文件路径。
返回：编码后的字串。
- **ArrayList &lt;String&gt;  encodeAudioFile（String path，Int dataPackageSize）**
功能：将文件转成base64 字符串数组 。
参数：
 - path：文件路径。
 - dataPackageSize：单个数据包的长度，单位为Byte，取值须为[4 * 1024, 1024 * 1024]之间
返回：编码后的字串数组。

- **TencentSOE setUserVoiceData（ArrayList &lt;String&gt;userVoiceDataArray）**
功能：设置待评测语音文件字串数组，调用该方法会同时将测评实例设置为流式传输模式。
参数：userVoiceDataArray 语音文件字串数组。
- **TencentSOE setUserVoiceData（String path，Int dataPackageSize）**
功能：设置待评测语音文件的路径及数据包长度，调用该方法会同时将测评实例设置为流式传输模式
参数：
 - path 文件路径。
 - dataPackageSize：单个数据包的长度，单位为 Byte，取值须为[4 * 1024，1024 * 1024]之间。
- **TencentSOE setUserVoiceData（String userVoiceData）**
功能：设置待评测语音文件字串，调用该方法会同时将测评实例设置为一次性传输模式。
参数：userVoiceData 语音文件字串。
- **void execute（SOECallback callback）**
功能：执行语音测评。
参数：callback测评事件回调。
- **TencentSOE startFrameRecord()**
功能：启动边录边传（录制的为 MP3格式）。
参数：callback 测评事件回调。
- **TencentSOE stopFrameRecord()**
功能：停止边录边传。
参数：callback测评事件回调。
- **interface SOECallback**
功能：测评事件回调接口类，包含以下三个方法。
 - void onInitSuccess(InitOralProcessResponse response);
功能：初始化成功回调。
参数：response 回调消息体。
 - void onTransmitSuccess(int index, int isEnd, TransmitOralProcessResponse response);
功能：数据包传输成功回调。
参数：
    - index 数据包索引序号，从1开始。
    - isEnd 是否传输完毕标志，0表示未完毕，1表示完毕。
    - response 回调消息体。
 - void onError(SOEError error);
功能：异常回调。
参数：error 异常或失败内容。
