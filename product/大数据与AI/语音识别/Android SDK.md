## 接入准备
### SDK 获取
一句话识别 Android SDK 及 Demo 下载地址：[接入 SDK 下载](https://console.cloud.tencent.com/asr/download)。

### 接入须知
- 开发者在调用前请先查看一句话识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的使用要求和使用步骤。  
- 该接口需要手机能够连接网络（3G、4G、5G 或 Wi-Fi 等），且系统为 **Android 5.0** 及其以上版本。

### 开发环境
1. **添加一句话识别 SDK aar**
   将 **asr-one-sentence-release.aar** 放在 libs 目录下，在 App 的 build.gradle 文件中添加以下代码。
```
  implementation(name: 'asr-one-sentence-release', ext: 'aar')
```
2. **添加其他依赖，在 App 的 build.gradle 文件中添加以下代码**。
```
 implementation 'com.google.code.gson:gson:2.8.5'
```
3. **在 AndroidManifest.xml 添加如下权限**：
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
```
4. **如果需要使用SDK内置录音器录音，在 AndroidManifest.xml 声明如下 service：**
```
<service android:name="com.tencent.cloud.qcloudasrsdk.onesentence.recorder.QCloudAudioMp3RecoderService" />
```

### 混淆规则
```
-keepclasseswithmembernames class * { # 保持 native 方法不被混淆
native <methods>;
}
-keep public class com.tencent.cloud.qcloudasrsdk.*
```

## 快速接入
### 开发流程及接入示例
1. **创建 QCloudOneSentenceRecognizer 示例**
```
QCloudOneSentenceRecognizer recognizer = new QCloudOneSentenceRecognizer(this, appid, secretId, secretKey);
```
2. **设置识别结果回调**
```
recognizer.setCallback(this);
```
3. **调用示例**
 - **通过语音 URL 调用**
```
QCloudOneSentenceRecognitionParams params = (QCloudOneSentenceRecognitionParams)QCloudOneSentenceRecognitionParams.defaultRequestParams();

params.setSourceType(QCloudSourceType.QCloudSourceTypeUrl); //调用方式:URL
params.setUrl("http://liqiansunvoice-1255628450.cosgz.myqcloud.com/test.wav"); // 设置音频文件的URL下载地址(请替换为您自己的地址)
params.setVoiceFormat("wav"); //设置音频文件格式，支持wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac。

params.setFilterDirty(0);// 0 ：默认状态 不过滤脏话 1：过滤脏话
params.setFilterModal(0);// 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
params.setFilterPunc(0); // 0 ：默认状态 不过滤句末的句号 1：滤句末的句号
params.setConvertNumMode(1);//1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
// 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
//params.setHotwordId("1335468b9e7c11ea9ae9446a2eb5fd98"); 

//设置识别引擎，默认16k_zh,见 https://cloud.tencent.com/document/product/1093/35646
params.setEngSerViceType("16k_zh");

recognizer.recognize(params);
```
 - **通过语音数据调用**
```
AssetManager am = getResources().getAssets();
is = am.open("test1.mp3");
int length = is.available();
byte[] audioData = new byte[length];
is.read(audioData);

//配置识别参数,详细参数说明见： https://cloud.tencent.com/document/product/1093/35646
QCloudOneSentenceRecognitionParams  params = (QCloudOneSentenceRecognitionParams)QCloudOneSentenceRecognitionParams.defaultRequestParams();

params.setSourceType(QCloudSourceType.QCloudSourceTypeData); //调用方式:通过语音数据调用
params.setData(audioData);
params.setVoiceFormat("mp3");//识别音频的音频格式，支持wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac。

params.setFilterDirty(0);// 0 ：默认状态 不过滤脏话 1：过滤脏话
params.setFilterModal(0);// 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
params.setFilterPunc(0); // 0 ：默认状态 不过滤句末的句号 1：滤句末的句号
params.setConvertNumMode(1);//1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
// 热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。
//params.setHotwordId(""); 
//默认16k_zh，更多引擎参数详见https://cloud.tencent.com/document/product/1093/35646 内的EngSerViceType字段
params.setEngSerViceType("16k_zh"); 

recognizer.recognize(params);
```
 - **通过 SDK 内置录音器并识别**
```

/**
* setDefaultParams 默认参数param
* @param filterDirty    0 ：默认状态 不过滤脏话 1：过滤脏话
* @param filterModal    0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
* @param filterPunc     0 ：默认状态 不过滤句末的句号 1：滤句末的句号
* @param convertNumMode 1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
* @param hotwordId  热词id，不使用则传null
* @param engSerViceType  引擎模型类型，传null默认使用“16k_zh”
*/
recognizer.setDefaultParams(filterDirty, filterModal, filterPunc, convertNumMode,hotwordId,engSerViceType);
recognizer.recognizeWithRecorder();
```

### 关键类说明
**QCloudOneSentenceRecognizer**：一句话识别入口类

```
/**
 * 初始化方法-直接鉴权，关于 AppId, SecretId, SecretKey 的获取见一句话识别接口说明中的使用步骤
 * @param activity app activity
 * @param appId 腾讯云appid
 * @param secretId 腾讯云secretId
 * @param secretKey 腾讯云secretKey
 */
public QCloudOneSentenceRecognizer(AppCompatActivity activity, String appId, String secretId, String secretKey);


/**
 * 初始化方法-使用STS临时证书鉴权，详见https://cloud.tencent.com/document/product/598/33416
 * @param activity app activity
 * @param appId 腾讯云appid
 * @param secretId 腾讯云 临时的secretId
 * @param secretKey 腾讯云 临时的secretKey
 * @param token 腾讯云 token
 */
public QCloudOneSentenceRecognizer(Activity activity, String appId, String secretId, String secretKey, String token);

 /**
  * 通过语音url进行一句话识别的快捷入口, 本地参数校验不通过抛出异常
  * @param audioUrl 资源url 如http://www.qq.music/hello.mp3
  * @param audioFormat 语音数据格式，QCloudAudioFormat
  * @param frequence 引擎模型类型，QCloudAudioFrequence枚举类获取对应模型名称，也可直接传符串，此参数与API文档EngSerViceType对应
  */
 public void recognize(String audioUrl, QCloudAudioFormat audioFormat, String frequence) throws Exception;
 
/**
  * 通过语音数据进行一句话识别的快捷入口, 本地参数校验不通过抛出异常
  * @param audioData 语音数据
  * @param audioFormat 语音数据格式，QCloudAudioFormat
  * @param frequence 语音数据采样率，QCloudAudioFrequence
  */
 public void recognize(byte[] audioData, QCloudAudioFormat audioFormat, QCloudAudioFrequence frequence) throws Exception;
/**
 * 通过QCloudOneSentenceRecognitionParams调用一句话识别, 调用[QCloudCommonParams defaultRequestParams]方法获取默认参数，
 * 然后根据需求设置参数
 * @param params请求参数
 */
public void recognize(QCloudOneSentenceRecognitionParams params) throws Exception;
/**
 * 通过sdk内置录音器开启一句话识别
 */
public void recognizeWithRecorder() throws Exception;
```

**QCloudOneSentenceRecognizerListener**：开始录音、结束录音以及识别结果回调
```
public interface QCloudOneSentenceRecognizerListener {
 /**
  * 开始录音回调
  */
 public abstract void didStartRecord();
 /**
  * 结束录音回调
  */
 public abstract void didStopRecord();
 /**
  * 识别结果回调
  */
 public abstract void recognizeResult(QCloudOneSentenceRecognizer recognizer, String result, Exception exception);
}
```

