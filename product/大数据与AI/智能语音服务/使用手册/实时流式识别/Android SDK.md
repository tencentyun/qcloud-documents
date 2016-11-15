
## 开发准备
### SDK下载
智能语音服务实时流式识别 Android SDK 及 Demo下载地址：[Android SDK][1]  

### 包文件目录
| 包名称    | 文件目录    | 说明 |
| --- | --- | --- | 
|com.qq.wx.voice.vad   |  /  | 语音处理包 |
| com.tencent.aai  |  /  |实时识别服务接口包  |
|    | /audio    |语音流处理 |
|    | /auth      |鉴权处理  |
|    | /common   |通用功能函数  |
|    | /config   |项目配置  |
|    |/exception  | 异常处理  |
|    | /listener |用户回调  |
|    | /log    |日志  |
|    | /model    | 定义语音请求   |
|    | /net  | 网络请求 |
|    | /task  |网络任务处理  |


### 运行环境配置

#### 引入.so文件
将libWXVoice.so文件放入main/jniLibs/armeabi目录下。

#### 引入jar包
将okhttp.jar、okio.jar、slf4j.jar以及aai-2.0.jar放入到app/libs/目录下。

#### AndroidManifest.xml设置
需要添加如下权限：
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.WRITE_SETTINGS" />
< uses-permission android:name="android.permission.READ_PHONE_STATE"/>
< uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
< uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```
## SDK重要类说明
下面着重介绍智能语音服务实时流式识别Android SDK各重要类及核心接口的功能及使用场景。

### AudioRecognizeRequest
该类是客户端定义的语音识别请求的抽象，通过发送请求即可开始启用语音识别服务。可以给请求设置语音处理参数（引擎模型、识别文本、返回方式等），如果未指定采用默认参数。
 
 #### 初始化
 AudioRecognizeRequest对象通过Builder对象进行初始化，只需要设置自定义模板即可，或者直接采用默认模板进行识别。

初始化示例如下：
```
AudioRecognizeRequest.Builder builder = new AudioRecognizeRequest.Builder();
AudioRecognizeRequest audioRecognizeRequest = builder
        .templateName("templateName") // 设置在控制台定义好的处理模板
        .template(new AudioRecognizeTemplate(1,1,1)) // 设置自定义模板
        .build();
 ```
#### 请求ID
每初始化一个请求都会自动生成一个requestId，用来唯一标识这个请求，并可以利用这个ID来停止、取消语音识别任务。
可通过getRequestId()方法来获得，如下：
```
Int requestId = audioRecognizeRequest.getRequestId();
```
### AudioRecognizeResult
 语音识别结果对象，和AudioRecognizeRequest对象相对应，用于返回语音识别的结果。AudioRecognize设置为同步返回时，每一个语音分片均会返回结果，否则只在语音流的最后一个分片的回包中返回识别结果。通过回调接口获得AudioRecognizeResult对象后，调用getText()方法即可得到识别的文本结果。
    
### AudioRecognizeConfiguration
语音识别时的配置，可以设置：
1. 是否开启静音检测，默认开启；
2. 是否开启检测说话超时，默认开启；
3. 是否开启检测说话结束超时，默认开启；
4. 两段语音流的最小间隔时间，默认1.5s；
5. 两段语音流的最大间隔时间，默认5s；
6. 检测说话起点超时时间，默认5s；
7. 音量回调时间，默认80ms，以40ms为步进。

### AudioRecognizeTemplate
自定义的语音模板，需要设置的参数包括：
1. 包括引擎模型，默认为通用领域模型；
2. 识别结果编码方式，默认utf-8编码；
3. 识别结果返回方式，默认为尾包返回。

### AudioRecognizeResultListener
语音识别结果监听类，识别成功返回语音识别的结果，识别失败则通过ClientException和ServerException返回错误原因。
类对应接口如下：
1. 返回单个语音流的识别结果
 ```
void onSliceSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```
  参数说明：
   request：语音识别请求；
   result: 请求结果
   order:该分片在语音流中的顺序
2. 返回整个语音流的识别结果
 ```
void onSegmentSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
 ```
 参数说明：
 request：语音识别请求；
result: 请求结果
order:该语音流在所欲语音流中的顺序
3. 返回整个语音识别结果
```
void onSuccess(AudioRecognizeRequest request, String result);
```
4. 识别失败返回
 ```
void onFailure(T1 request, ClientException clientException, ServerException serverException);
```
### AudioRecognizeStateListener

返回语音识别的状态，包括开始录音、开始识别、结束录音以及结束识别，并包含了语音音量回调接口。
1. 开始录音回调接口
```
void onStartRecord(AudioRecognizeRequest request);
```
2. 结束录音回调接口
 ```
void onStopRecord(AudioRecognizeRequest request);
```
3. 开始识别回调接口
```
void onStartRecognize(AudioRecognizeRequest request);
```
4. 结束识别回调接口
```
void onStopRecognize(AudioRecognizeRequest request);
```
5. 返回音量
```
void onVoiceVolume(AudioRecognizeRequest request, int volume);
```
### AudioRecognizeTimeoutListener
语音流超时监听类，包含了起始超时和结束超时。
1. 语音流起始超时：
```
void onFirstVoiceFlowTimeout(AudioRecognizeRequest request);
 ```
 2. 语音流结束超时：
```
void onNextVoiceFlowTimeout(AudioRecognizeRequest request);
```

### AbsCredentialProvider
签名鉴权类，用户需要自己实现这个类，将原始的签名串进行加密。SDK中LocalCredentialProvider实现了这个接口，但需要用户提供secretKey，为了安全性，强烈建议由用户自己在第三方服务器上进行签名。签名接口：
```
String getAudioRecognizeSign(String source);
```
### AAIClient
语音服务的核心类，用户可以调用该类来开始、停止以及取消语音识别，并返回识别结果和状态。
1. 初始化
利用用户申请的appid、secretId、自己实现的签名类以及clientConfiguration（可选参数）即可初始化一个AAIClient对象。
```
AAIClient aaiClient = new AAIClient(context, appid, secretId, credentialProvider);
```
2. 启动语音识别
设置AudioRecognizeResultListener（必选）和audioRecognizeConfiguration（可选）回调接口监听识别结果（异步处理）。
```     
aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener, audioRecognizeConfiguration);
```
3. 设置识别状态监听
requestId标识请求的ID号；audioRecognizeStateListener是状态监听器。
```
aaiClient.setAudioRecognizeListener(requestId, audioRecognizeStateListener);
```
4.  设置超时监听
requestId是请求的ID号；audioRecognizeStateListener是超时监听器。
```
aaiClient.setAudioFlowTimeoutListener(requestId,  audioRecognizeTimeoutListener);
```
5. 停止语音识别
 通过请求的ID号来停止请求。
```
aaiClient.stopAudioRecognize(requestId);
```
6. 取消语音识别
通过请求的ID号来取消请求。
```
aaiClient.cancelAudioRecognize(requestId);
```
7. 判断识别服务是否空闲
当前没有请求在录音状态时（可以是识别状态），识别服务即为空闲状态，这时可以启动另一个语音识别请求。
```
aaiClient.isAudioRecognizeIdle();
```          
8. 释放AAIClient
```
aaiClient.release();
```
### AAILogger
用户可以利用AAILogger来控制日志的输出，可以选择性的输出debug、info、warn以及error级别的日志信息。
```
public static void disableDebug();
public static void disableInfo();
public static void disableWarn();
public static void disableError();
public static void enableDebug();
public static void enableInfo();
public static void enableWarn();
public static void enableError();
```


  [1]: https://mc.qcloudimg.com/static/archive/e463257daf21b76e08b851c2e5d5bfd0/qcloud-aai-android.zip