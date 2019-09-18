## 开发准备
### SDK 下载
录音文件识别 Android SDK 及 Demo 下载地址：[Android SDK](https://main.qcloudimg.com/raw/12d8f3ebe1ed16190b874c910db1369c/QCloudOneSentenceSDK_v1.0.0.zip)

### 开发前
1. 开发者使用录音文件识别功能前，需要先在 [腾讯云-控制台](https://console.cloud.tencent.com/) 注册账号，
   并获得APPID、SecretId 和 SecretKey信息。
2. 手机必须要有网络（GPRS、3G 或 Wi-Fi 等）。
3. 支持 Android 4.0 及其以上版本。

### 运行环境配置
##### 添加录音文件识别SDK aar

将 **qcloudasrsdk_1.0_release.aar** 放在libs目录下，在app的build.gradle 文件中添加。
```
  implementation(name: 'qcloudasrsdk_1.0_release', ext: 'aar')
```

##### 添加其他依赖，在app的build.gradle 文件中添加。
```
 implementation 'com.google.code.gson:gson:2.8.5'
 implementation 'com.squareup.okhttp3:okhttp:4.0.0-RC1'
 implementation 'com.squareup.okio:okio:1.11.0'
 implementation 'org.slf4j:slf4j-api:1.7.25'
```

##### 在 AndroidManifest.xml 添加如下权限：
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.WRITE_SETTINGS" />
< uses-permission android:name="android.permission.READ_PHONE_STATE"/>
< uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
< uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```

### 示例
#### 创建QCloudFileRecognizer示例
```
QCloudFileRecognizer recognizer = new QCloudFileRecognizer(this, appid, secretId, secretKey);
```

#### 设置识别结果回调
```
recognizer.setCallback(this);
```

#### 调用方式示例
+ ##### 通过语音url调用
```
  QCloudFileRecognitionParams params = (QCloudFileRecognitionParams) QCloudFileRecognitionParams.defaultRequestParams();
  params.setUrl("http://client-sdk-1255628450.cossh.myqcloud.com/test%20audio/voice_WGVNG_8000.mp3");
  params.setSourceType(QCloudSourceType.QCloudSourceTypeUrl);
  fileRecognizer.recognize(params);
```

+ ##### 通过语音数据调用
```
  AssetManager am = getResources().getAssets();
  is = am.open("test1.mp3");
  int length = is.available();
  byte[] audioData = new byte[length];
  is.read(audioData);

  QCloudFileRecognitionParams params = (QCloudFileRecognitionParams) QCloudFileRecognitionParams.defaultRequestParams();
  params.setData(audioData);
  params.setSourceType(QCloudSourceType.QCloudSourceTypeData);
  fileRecognizer.recognize(params);
```


### 关键类说明
**QCloudFileRecognizer**录音文件识别入口类
```
/**
 * 初始化方法，关于AppId, SecretId, SecretKey 见https://cloud.tencent.com/document/product/441/6194
 * @param activity app activity
 * @param appId 腾讯云appid
 * @param secretId 腾讯云secretId
 * @param secretKey 腾讯云secretKey
 */
public QCloudFileRecognizer(AppCompatActivity activity, String appId, String secretId, String secretKey);

/**
 * 通过url或语音数据调用录音文件识别
 * @param params 请求参数
 * @return 返回本次请求的唯一标识别requestId
 */
public long recognize(QCloudFileRecognitionParams params) throws Exception;
```

**QCloudFileRecognizerListener**识别结果回调
```
public interface QCloudFileRecognizerListener {
    /**
     * 识别结果回调
     * @param recognizer 录音文件识别实例
     * @param requestId 请求唯一标识别
     * @param result 识别文本
     * @param exception 异常信息
     */
    public abstract void recognizeResult(QCloudFileRecognizer recognizer, final long requestId, String result, Exception exception);
}
```
