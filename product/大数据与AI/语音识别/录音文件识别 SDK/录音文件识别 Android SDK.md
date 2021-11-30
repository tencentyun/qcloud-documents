Android SDK 接入请观看视频：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-20717?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 开发准备
### SDK 下载
录音文件识别 Android SDK 及 Demo 下载地址：[Android SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_Android_v2.6.5.zip)。

### 接入须知
- 开发者使用录音文件识别功能前，需要先在 [腾讯云控制台](https://console.cloud.tencent.com/) 注册账号，并获得 APPID、SecretId 和 SecretKey 信息。
2. 手机必须要有网络（GPRS、3G 或 Wi-Fi 等）。
3. 支持 Android 4.0 及其以上版本。

### 运行环境配置
1. 添加录音文件识别 SDK aar，将 **speech_release.aar** 放在 libs 目录下，在 App 的 build.gradle 文件中添加。
```
  implementation(name: 'speech_release', ext: 'aar')
```
2. 添加其他依赖，在 App 的 build.gradle 文件中添加。
```
 implementation 'com.google.code.gson:gson:2.8.5'
 implementation 'com.squareup.okhttp3:okhttp:4.2.2'
 implementation 'com.squareup.okio:okio:1.11.0'
 implementation 'org.slf4j:slf4j-api:1.7.25'
```
3. 在 AndroidManifest.xml 添加如下权限。
```
< uses-permission android:name="android.permission.INTERNET"/>
```

## 快速接入
### 开发流程及接入示例
1. 创建 QCloudFileRecognizer 示例
```
QCloudFileRecognizer recognizer = new QCloudFileRecognizer(this, appid, secretId, secretKey);
```
2. 设置识别结果回调
```
recognizer.setCallback(this);
```
3. 调用方式示例
 - 通过语音 url 调用
```  
     QCloudFileRecognitionParams params = (QCloudFileRecognitionParams) QCloudFileRecognitionParams.defaultRequestParams();
                    params.setUrl("http://client-sdk-1255628450.cossh.myqcloud.com/test%20audio/voice_WGVNG_800.mp3");
                    params.setSourceType(QCloudSourceType.QCloudSourceTypeUrl);
                    params.setFilterDirty(0);// 0 ：默认状态 不过滤脏话 1：过滤脏话
                    params.setFilterModal(0);// 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
                    params.setConvertNumMode(1);//1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
                    params.setHotwordId("");  // 热词 id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词 id 设置，自动生效默认热词；如果进行了单独的热词 id 设置，那么将生效单独设置的热词 id。
                    fileRecognizer.recognize(params);
```
 - 通过语音数据调用
```
  AssetManager am = getResources().getAssets();
  is = am.open("test1.mp3");
  int length = is.available();
  byte[] audioData = new byte[length];
  is.read(audioData);

    QCloudFileRecognitionParams params = (QCloudFileRecognitionParams) QCloudFileRecognitionParams.defaultRequestParams();
                    params.setData(audioData);
                    params.setSourceType(QCloudSourceType.QCloudSourceTypeData);
                    params.setFilterDirty(0);// 0 ：默认状态 不过滤脏话 1：过滤脏话
                    params.setFilterModal(0);// 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
                    params.setConvertNumMode(1);//1：默认状态 根据场景智能转换为阿拉伯数字；0：全部转为中文数字。
                    params.setHotwordId(""); // 热词 id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词 id 设置，自动生效默认热词；如果进行了单独的热词 id 设置，那么将生效单独设置的热词 id。
                    fileRecognizer.recognize(params);
```

### 关键类说明
**QCloudFileRecognizer**：录音文件识别入口类
```
/**
 * 初始化方法 - 直接鉴权
 * @param appId 腾讯云 appid
 * @param secretId 腾讯云 secretId
 * @param secretKey 腾讯云 secretKey
 */
public QCloudFileRecognizer( String appId, String secretId, String secretKey);

/**
 * 初始化方法 - 使用临时sts证书鉴权
 * 1.通过sts 获取到临时证书 ,此步骤应在您的服务器端实现，
 * 见https://cloud.tencent.com/document/product/598/33416
 * 2.通过临时密钥调用接口
 * @param appId 腾讯云 appid
 * @param secretId 腾讯云 临时secretId
 * @param secretKey 腾讯云 临时secretKey
 * @param secretKey 腾讯云 token
 */
public QCloudFileRecognizer(String appId, String secretId, String secretKey, String token)；

/**
 * 通过 url 或语音数据调用录音文件识别
 * @param params 请求参数
 * @return 返回本次请求的唯一标识别 requestId
 */
public long recognize(QCloudFileRecognitionParams params) throws Exception;
```

**QCloudFileRecognizerListener**：识别结果回调
```
public interface QCloudFileRecognizerListener {
    /**
     * 识别结果回调
     * @param recognizer 录音文件识别实例
     * @param requestId 请求唯一标识别
     * @param result 识别文本
     * @param status 任务状态码：0：任务等待 1：任务执行中 2:任务成功 3：任务失败 
     * @param exception 异常信息
     *
     */
    void recognizeResult(QCloudFileRecognizer recognizer, final long requestId, String result, int status,Exception exception);
}
```
