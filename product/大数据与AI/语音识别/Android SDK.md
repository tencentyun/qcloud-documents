Android SDK 接入请观看视频：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-20718?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 接入准备
### SDK 获取
一句话识别 Android SDK 及 Demo 下载地址：[Android SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_Android_v2.6.5.zip)。

### 接入须知
- 开发者在调用前请先查看一句话识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的使用要求和使用步骤。  
- 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 等），且系统为 **Android 4.0.3** 及其以上版本。

### 开发环境
1. **添加一句话识别 SDK aar**
   将 **speech_release.aar** 放在 libs 目录下，在 App 的 build.gradle 文件中添加以下代码。
```
  implementation(name: 'speech_release', ext: 'aar')
```
2. **添加其他依赖，在 App 的 build.gradle 文件中添加以下代码**。
```
 implementation 'com.google.code.gson:gson:2.8.5'
 implementation 'com.squareup.okhttp3:okhttp:4.2.2'
 implementation 'com.squareup.okio:okio:1.11.0'
 implementation 'org.slf4j:slf4j-api:1.7.25'
```
3. **在 AndroidManifest.xml 添加如下权限**：
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```
4. **在 AndroidManifest.xml 声明如下 service：**
```
<!--<service android:name=".service.MyIntentService"/>-->
<service android:name="com.tencent.cloud.qcloudasrsdk.recorder.service.QCloudAudioMp3RecoderService" />
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
String audioUrl = "https://img.soulapp.cn/audio/2019-07-22/9ed1a797-93b5-4268-be6d-5660cc3e894e.mp3";
recognizer.recognize(audioUrl, QCloudAudioFormat.QCloudAudioFormatMp3, QCloudAudioFrequence.QCloudAudioFrequence16k);
```
 - **通过语音数据调用**
```
AssetManager am = getResources().getAssets();
InputStream is = am.open("onesentence.mp3");
int length = is.available();
byte[] audioData = new byte[length];
is.read(audioData);
recognizer.recognize(audioData, QCloudAudioFormat.QCloudAudioFormatMp3, QCloudAudioFrequence.QCloudAudioFrequence16k);
```
 - **通过 SDK 内置录音器**
```
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
  * @param frequence 语音数据采样率，QCloudAudioFrequence
  */
 public void recognize(String audioUrl, QCloudAudioFormat audioFormat, QCloudAudioFrequence frequence) throws Exception;
 
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

