## 1. 接入准备
### 1.1 SDK 获取
一句话识别 Android SDK 及 Demo 下载地址：[Android SDK](https://main.qcloudimg.com/raw/12d8f3ebe1ed16190b874c910db1369c/QCloudOneSentenceSDK_v1.0.0.zip)

### 1.2 接入须知
+ 开发者在调用前请先查看一句话识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/35721)，了解接口的使用要求和使用步骤 。
+ 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 等），且系统为**Android 4.0**及其以上版本。

### 1.3 开发环境
1）**添加一句话识别 SDK aar**

将 **qcloudasrsdk\_1.0\_release.aar** 放在 libs 目录下，在 App 的 build.gradle 文件中添加以下代码。

```
  implementation(name: 'qcloudasrsdk_1.0_release', ext: 'aar')
```

2）**添加其他依赖，在 App 的 build.gradle 文件中添加以下代码**。

```
 implementation 'com.google.code.gson:gson:2.8.5'
 implementation 'com.squareup.okhttp3:okhttp:4.0.0-RC1'
 implementation 'com.squareup.okio:okio:1.11.0'
 implementation 'org.slf4j:slf4j-api:1.7.25'
```

3）**在 AndroidManifest.xml 添加如下权限**：

```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.WRITE_SETTINGS" />
< uses-permission android:name="android.permission.READ_PHONE_STATE"/>
< uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
< uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```

## 2. 快速接入

### 2.1 开发流程及接入示例

1）**创建 QCloudOneSentenceRecognizer 示例**

```
QCloudOneSentenceRecognizer recognizer = new QCloudOneSentenceRecognizer(this, appid, secretId, secretKey);
```
2）**设置识别结果回调**

```
recognizer.setCallback(this);
```
3）**调用示例**

+ **通过语音 URL 调用**

```
String audioUrl = "https://img.soulapp.cn/audio/2019-07-22/9ed1a797-93b5-4268-be6d-5660cc3e894e.mp3";
recognizer.recognize(audioUrl, QCloudAudioFormat.QCloudAudioFormatMp3, QCloudAudioFrequence.QCloudAudioFrequence16k);
```

+ **通过语音数据调用**

```
AssetManager am = getResources().getAssets();
InputStream is = am.open("onesentence.mp3");
int length = is.available();
byte[] audioData = new byte[length];
is.read(audioData);
recognizer.recognize(audioData, QCloudAudioFormat.QCloudAudioFormatMp3, QCloudAudioFrequence.QCloudAudioFrequence16k);
```

+ **通过 SDK 内置录音器**

```
recognizer.recognizeWithRecorder();
```

### 2.2 关键类说明
**QCloudOneSentenceRecognizer** :一句话识别入口类

```
/**
 * 初始化方法，关于AppId, SecretId, SecretKey的获取见一句话识别接口说明中的使用步骤
 * @param activity app activity
 * @param appId 腾讯云appid
 * @param secretId 腾讯云secretId
 * @param secretKey 腾讯云secretKey
 */
public QCloudOneSentenceRecognizer(AppCompatActivity activity, String appId, String secretId, String secretKey);
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

**QCloudOneSentenceRecognizerListener** : 开始录音、结束录音以及识别结果回调

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


