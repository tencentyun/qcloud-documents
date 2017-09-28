## 开发准备
### SDK 下载
智能语音服务实时流式识别 Android SDK 及 Demo 下载地址：[Android SDK][1]

### 开发前
1. 开发者使用实时流式识别功能前，需要先在腾讯云- [控制台](https://console.cloud.tencent.com/) 注册账号，并获得 APPID、SecretId 和 SecretKey 等；
2. 手机必须要有网络（GPRS、3G 或 WiFi 等）；
3. 支持 Android 4.0 及其以上版本；

### 运行环境配置

##### 引入 .so 文件
- libWXVoice.so：腾讯语音检测 so 库

##### 引入 jar 包
- aai-2.1.2.jar：腾讯云智能语音 SDK
- okhttp-3.2.0.jar
- okio-1.6.0.jar
- slf4j-android-1.6.1-RC1.jar

腾讯云智能语音服务 SDK 支持本地构建或者远程构建两种方式：
#### 本地构建
可以直接下载 Android SDK 及 Demo，然后集成对应的 so 文件和 jar 包（均在 sdk-source 目录下），最后将 okhttp3、okio 和 slf4j 三个库也集成到 app 中。
#### 远程构建
在 build.gradle 文件中添加：
```
compile 'com.tencent.aai:aai:2.1.2:@aar'
compile 'com.squareup.okhttp3:okhttp:3.6.0'
compile 'org.slf4j:slf4j-android:1.6.1-RC1'
```
如果您使用 gradle 来进行工程构建，我们强烈建议使用远程构建的方式来构建您的应用。

#### 在 AndroidManifest.xml 添加如下权限：
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.WRITE_SETTINGS" />
< uses-permission android:name="android.permission.READ_PHONE_STATE"/>
< uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
< uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```
## 快速入门

### 启动语音识别
```
int appid = XXX;
int projectid = XXX;
String secretId = "XXX";

// 为了方便用户测试，sdk提供了本地签名，但是为了secretKey的安全性，正式环境下请自行在第三方服务器上生成签名。
AbsCredentialProvider credentialProvider = new LocalCredentialProvider("your secretKey");

final AAIClient aaiClient;
try {
    // 1、初始化AAIClient对象。
    aaiClient = new AAIClient(this, appid, projectid, secretId, credentialProvider);

    // 2、初始化语音识别请求。
    final AudioRecognizeRequest audioRecognizeRequest = new AudioRecognizeRequest.Builder()
            .pcmAudioDataSource(new AudioRecordDataSource()) // 设置语音源为麦克风输入
            .build();

    // 3、初始化语音识别结果监听器。
    final AudioRecognizeResultListener audioRecognizeResultListener = new AudioRecognizeResultListener() {
        @Override
        public void onSliceSuccess(AudioRecognizeRequest audioRecognizeRequest, AudioRecognizeResult audioRecognizeResult, int i) {
			// 返回语音分片的识别结果
        }

        @Override
        public void onSegmentSuccess(AudioRecognizeRequest audioRecognizeRequest, AudioRecognizeResult audioRecognizeResult, int i) {
			// 返回语音流的识别结果
        }

        @Override
        public void onSuccess(AudioRecognizeRequest audioRecognizeRequest, String s) {
			// 返回所有的识别结果
        }

        @Override
        public void onFailure(AudioRecognizeRequest audioRecognizeRequest, ClientException e, ServerException e1) {
			// 识别失败
        }
    };

    // 4、启动语音识别
    new Thread(new Runnable() {
        @Override
        public void run() {
            if (aaiClient!=null) {
                aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener);
            }
        }
    }).start();

} catch (ClientException e) {
    e.printStackTrace();
}
```
### 停止语音识别
```
// 1、获得请求的id
final int requestId = audioRecognizeRequest.getRequestId();
// 2、调用stop方法
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
            aaiClient.stopAudioRecognize(requestId);
        }
    }
}).start();
```
### 取消语音识别
```
// 1、获得请求的id
final int requestId = audioRecognizeRequest.getRequestId();
// 2、调用cancel方法
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
            aaiClient.cancelAudioRecognize(requestId);
        }
    }
}).start();
```
