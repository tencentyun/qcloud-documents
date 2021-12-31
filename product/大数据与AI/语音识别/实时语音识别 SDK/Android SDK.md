Android SDK 接入请观看视频：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1692-20716?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 接入准备
### SDK 获取
实时语音识别 Android SDK 及 Demo 下载地址：[Android SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/QCloudSDK_Android_v2.6.6.zip)。

### 接入须知
- 开发者在调用前请先查看实时语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37138)，了解接口的**使用要求**和**使用步骤**。
- 该接口需要手机能够连接网络（GPRS、3G 或 Wi-Fi 等），且系统为 **Android 4.0** 及其以上版本。

### 开发环境
- 引入 aar 包
  speech_release.aar：腾讯云语音识别 SDK。
```
implementation(name: 'speech_release', ext: 'aar')
```
- 添加相关依赖
  okhttp3、okio、gson 和 slf4j 依赖添加，在 build.gradle 文件中添加：
```
	implementation 'com.squareup.okhttp3:okhttp:4.2.2' 
	implementation 'com.squareup.okio:okio:1.11.0'
	implementation 'com.google.code.gson:gson:2.8.5'
	implementation 'org.slf4j:slf4j-api:1.7.25'
```
- 在 AndroidManifest.xml 添加如下权限：
```
	< uses-permission android:name="android.permission.RECORD_AUDIO"/>
	< uses-permission android:name="android.permission.INTERNET"/>
	< uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

## 快速接入
[](id:documen)
### 启动实时语音识别
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

/**您也可以使用临时证书鉴权
* * 1.通过sts 获取到临时证书,此步骤应在您的服务器端实现，见https://cloud.tencent.com/document/product/598/33416
*   2.通过临时密钥调用接口
* **/
  // aaiClient = new AAIClient(MainActivity.this, appid, projectId,"临时secretId", "临时secretKey","对应的token" ,credentialProvider);

	 // 2、初始化语音识别请求。
	final AudioRecognizeRequest audioRecognizeRequest = builder
				.pcmAudioDataSource(new AudioRecordDataSource()) // 设置数据源
				.template(new AudioRecognizeTemplate(
				EngineModelType.EngineModelType16K.getType(),0)) 
				// 设置自定义模板
				.setFilterDirty(0)  // 0 ：默认状态 不过滤脏话 1：过滤脏话
				.setFilterModal(0) // 0 ：默认状态 不过滤语气词  1：过滤部分语气词 2:严格过滤
				.setFilterPunc(0) // 0 ：默认状态 不过滤句末的句号 1：滤句末的句号
				.setNeedvad(1) //0：关闭 vad，1：默认状态 开启 vad。语音时长超过一分钟需要开启,如果对实时性要求较高,并且时间较短的识别,建议关闭,可以显著降低onSliceSuccess结果返回的时延以及stop后onSegmentSuccess和onSuccess返回的时延
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

### 停止实时语音识别

```
// 1、获得请求的 ID
final int requestId = audioRecognizeRequest.getRequestId();
// 2、调用stop方法
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
	    //停止语音识别，等待当前任务结束
            aaiClient.stopAudioRecognize(requestId);
        }
    }
}).start();
```

### 取消实时语音识别

```
// 1、获得请求的id
final int requestId = audioRecognizeRequest.getRequestId();
// 2、调用cancel方法
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
	    //取消语音识别，丢弃当前任务
            aaiClient.cancelAudioRecognize(requestId);
        }
    }
}).start();
```

## 主要接口类和方法说明
### 计算签名
调用者需要自己实现 AbsCredentialProvider 接口来计算签名，此方法为 SDK 内部调用，上层不用关心 source 来源。

**计算签名函数如下：**
```
/**
* 签名函数：将原始字符串进行加密，具体的加密算法见以下说明。
* @param source 原文字符串
* @return 加密后返回的密文
*/
String getAudioRecognizeSign(String source);
```

**计算签名算法**   
先以 SecretKey 对 source 进行 HMAC-SHA1 加密，然后对密文进行 Base64 编码，获得最终的签名串。即：sign=Base64Encode(HmacSha1(source，secretKey))。

为方便用户测试，SDK 已提供一个实现类 **LocalCredentialProvider**，但为保证 SecretKey 的安全性，请仅在测试环境下使用，正式版本建议上层实现接口 **AbsCredentialProvider** 中的方法。

### 初始化 AAIClient
AAIClient 是语音服务的核心类，用户可以调用该类来开始、停止以及取消语音识别。
```
public AAIClient(Context context, int appid, int projectId, String secreteId, AbsCredentialProvider credentialProvider) throws ClientException
```

| 参数名称           | 类型                  | 是否必填 | 参数描述           |
| ------------------ | --------------------- | -------- | ------------------ |
| context            | Context               | 是       | 上下文             |
| appid              | Int                   | 是       | 腾讯云注册的 AppID |
| projectId          | Int                   | 否       | 用户的 projectId   |
| secreteId          | String                | 是       | 用户的 SecreteId   |
| credentialProvider | AbsCredentialProvider | 是       | 鉴权类             |

**示例：**
```
try {
    AaiClient aaiClient = new AAIClient(context, appid, projectId, secretId, credentialProvider);
} catch (ClientException e) {
    e.printStackTrace();
}
```
如果 aaiClient 不再需要使用，请调用 release() 方法释放资源：
```
aaiClient.release();
```

###  配置全局参数
用户调用 ClientConfiguration 类的静态方法来修改全局配置。

| 方法                                 | 方法描述               | 默认值 | 有效范围      |
| ------------------------------------ | ---------------------- | ------ | ------------- |
| setMaxAudioRecognizeConcurrentNumber | 语音识别最大并发请求数 | 2      | 1 - 5         |
| setMaxRecognizeSliceConcurrentNumber | 语音识别分片最大并发数 | 5      | 1 - 5         |
| setAudioRecognizeSliceTimeout        | HTTP 读超时时间        | 5000ms | 500 - 10000ms |
| setAudioRecognizeConnectTimeout      | HTTP 连接超时时间      | 5000ms | 500 - 10000ms |
| setAudioRecognizeWriteTimeout        | HTTP 写超时时间        | 5000ms | 500 - 10000ms |

**示例：**
```
ClientConfiguration.setMaxAudioRecognizeConcurrentNumber(2)
ClientConfiguration.setMaxRecognizeSliceConcurrentNumber(5)
ClientConfiguration.setAudioRecognizeSliceTimeout(2000)
ClientConfiguration.setAudioRecognizeConnectTimeout(2000)
ClientConfiguration.setAudioRecognizeWriteTimeout(2000)
```

### 设置结果监听器
AudioRecognizeResultListener 可以用来监听语音识别的结果，共有如下四个接口：
- 语音分片的语音识别结果回调接口
```
void onSliceSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```
<table>
<thead>
<tr>
<th>参数</th>
<th>参数类型</th>
<th>参数描述</th>
</tr>
</thead>
<tbody><tr>
<td>request</td>
<td>AudioRecognizeRequest</td>
<td>语音识别请求</td>
</tr>
<tr>
<td>result</td>
<td>AudioRecognizeResult</td>
<td>语音分片的语音识别结果</td>
</tr>
<tr>
<td>order</td>
<td>Int</td>
<td>该语音分片所在语音流的次序</td>
</tr>
</tbody></table>
- 语音流的语音识别结果回调接口
```
void onSegmentSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```
<table>
<thead>
<tr>
<th>参数</th>
<th>参数类型</th>
<th>参数描述</th>
</tr>
</thead>
<tbody><tr>
<td>request</td>
<td>AudioRecognizeRequest</td>
<td>语音识别请求</td>
</tr>
<tr>
<td>result</td>
<td>AudioRecognizeResult</td>
<td>语音分片的语音识别结果</td>
</tr>
<tr>
<td>order</td>
<td>Int</td>
<td>该语音流的次序</td>
</tr>
</tbody></table>
- 返回所有的识别结果
```
void onSuccess(AudioRecognizeRequest request, String result);
```
<table>
<thead>
<tr>
<th>参数</th>
<th>参数类型</th>
<th>参数描述</th>
</tr>
</thead>
<tbody><tr>
<td>request</td>
<td>AudioRecognizeRequest</td>
<td>语音识别请求</td>
</tr>
<tr>
<td>result</td>
<td>String</td>
<td>所有的识别结果</td>
</tr>
</tbody></table>
- 语音识别请求失败回调函数
```
void onFailure(AudioRecognizeRequest request, final ClientException clientException, final ServerException serverException,String response);
```
<table>
<thead>
<tr>
<th>参数</th>
<th>参数类型</th>
<th>参数描述</th>
</tr>
</thead>
<tbody><tr>
<td>request</td>
<td>AudioRecognizeRequest</td>
<td>语音识别请求</td>
</tr>
<tr>
<td>clientException</td>
<td>ClientException</td>
<td>客户端异常</td>
</tr>
<tr>
<td>serverException</td>
<td>ServerException</td>
<td>服务端异常</td>
</tr>
<tr>
<td>response</td>
<td>String</td>
<td>	服务端返回的 json 字符串</td>
</tr>
</tbody></table>

示例代码详见 [入门示例](#documen)。

### 设置语音识别参数
通过构建 AudioRecognizeConfiguration 类，可以设置语音识别时的配置：

| 参数名称                | 类型    | 是否必填 | 参数描述                                           | 默认值 |
| ----------------------- | ------- | -------- | -------------------------------------------------- | ------ |
| setSilentDetectTimeOut  | Boolean | 否       | 是否开启静音检测，开启后说话前的静音部分不进行识别 | true   |
| audioFlowSilenceTimeOut | Int     | 否       | 开启检测说话启始超时，开启后超时会自动停止录音     | 5000ms |
| minVolumeCallbackTime   | Int     | 否       | 两个语音流最短分割时间                                       | 2000ms   |

**示例：**
```
AudioRecognizeConfiguration audioRecognizeConfiguration = new AudioRecognizeConfiguration.Builder()
	.setSilentDetectTimeOut(true)// 是否使能静音检测，false 表示不检查静音部分
        .audioFlowSilenceTimeOut(5000) // 静音检测超时停止录音
    	.minVolumeCallbackTime(80) // 音量回调时间
    	.build();

// 启动语音识别
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null) {
            aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener, audioRecognizeConfiguration);
        }
    }
}).start();
```

### 设置状态监听器
AudioRecognizeStateListener 可以用来监听语音识别的状态，一共有如下八个接口：

| 方法                       | 方法描述                                                     |
| -------------------------- | ------------------------------------------------------------ |
| onStartRecord              | 开始录音                                                     |
| onStopRecord               | 结束录音                                                     |
| onVoiceFlowStart           | 检测到语音流的起点                                           |
| onVoiceFlowStartRecognize  | 语音流开始识别                                               |
| onVoiceFlowFinishRecognize | 语音流结束识别                                               |
| onVoiceVolume              | 音量                                                         |
| onNextAudioData            | 返回音频流，用于返回宿主层做录音缓存业务。new AudioRecordDataSource(true) 传递 true 时生效 |

### 设置超时监听器
AudioRecognizeTimeoutListener 可以用来监听语音识别的超时，一共有如下两个接口：

| 方法                    | 方法描述             |
| ----------------------- | -------------------- |
| onFirstVoiceFlowTimeout | 检测第一个语音流超时 |
| onNextVoiceFlowTimeout  | 检测下一个语音流超时 |

**示例：**
```
AudioRecognizeStateListener audioRecognizeStateListener = new AudioRecognizeStateListener() {
  @Override
  public void onStartRecord(AudioRecognizeRequest audioRecognizeRequest) {
      // 开始录音
  }
    @Override
  public void onStopRecord(AudioRecognizeRequest audioRecognizeRequest) {
// 结束录音
  }
    @Override
  public void onVoiceFlowStart(AudioRecognizeRequest audioRecognizeRequest, int i) {
// 语音流开始
  }
    @Override
  public void onVoiceFlowFinish(AudioRecognizeRequest audioRecognizeRequest, int i) {
// 语音流结束
  }
    @Override
  public void onVoiceFlowStartRecognize(AudioRecognizeRequest audioRecognizeRequest, int i) {
// 语音流开始识别
  }
    @Override
  public void onVoiceFlowFinishRecognize(AudioRecognizeRequest audioRecognizeRequest, int i) {
// 语音流结束识别
  }
    @Override
  public void onVoiceVolume(AudioRecognizeRequest audioRecognizeRequest, int i) {
// 音量回调
  }
};
/**
    * 返回音频流，
    * 用于返回宿主层做录音缓存业务。
    * 由于方法跑在sdk线程上，这里多用于文件操作，宿主需要新开一条线程专门用于实现业务逻辑
    * new AudioRecordDataSource(true) 有效，否则不会回调该函数
    * @param audioDatas
  */
    @Override
    public void onNextAudioData(final short[] audioDatas, final int readBufferLength){
    }
```

### 其他重要类说明
#### **AudioRecognizeRequest**
templateName 和 customTemplate 都设置时，优先使用 templateName 的设置。

| 参数名称           | 类型                   | 是否必填 | 参数描述                 | 默认值        |
| ------------------ | ---------------------- | -------- | ------------------------ | ------------- |
| pcmAudioDataSource | PcmAudioDataSource     | 是       | 音频数据源               | 无            |
| templateName       | String                 | 否       | 用户控制台设置的模板名称 | 无            |
| customTemplate     | AudioRecognizeTemplate | 否       | 用户自定义的模板         | ("16k_zh", 1) |

#### **AudioRecognizeResult**
语音识别结果对象，和 AudioRecognizeRequest 对象相对应，用于返回语音识别的结果。

| 参数名称 | 类型   | 参数描述                  |
| -------- | ------ | ------------------------- |
| code     | Int    | 识别状态码                |
| message  | String | 识别提示信息              |
| text     | String | 识别结果                  |
| seq      | Int    | 该语音分片的序号          |
| voiceId  | String | 该语音分片所在语音流的 ID |
| cookie   | String | cookie 值                 |

#### **AudioRecognizeTemplate**
自定义的语音模板，需要设置的参数包括：

| 参数名称        | 类型   | 是否必填 | 参数描述     |
| --------------- | ------ | -------- | ------------ |
| engineModelType | String | 是       | 引擎模型类型 |
| resType         | Int    | 是       | 结果返回方式 |

**示例：**
```
AudioRecognizeTemplate audioRecognizeTemplate = new AudioRecognizeTemplate("16k_zh",1);
```

#### **PcmAudioDataSource**
用户可以实现这个接口来识别单通道、采样率16k的 PCM 音频数据。主要包括如下几个接口：
- 向语音识别器添加数据，将长度为 length 的数据从下标0开始复制到 audioPcmData 数组中，并返回实际的复制的数据量的长度。
```
int read(short[] audioPcmData, int length);
```
- 启动识别时回调函数，用户可以在这里做些初始化的工作。
```
void start() throws AudioRecognizerException;
```
- 结束识别时回调函数，用户可以在这里进行一些清理工作。
```
void stop();
```
- 获取 sdk Pcm 格式录音源文件路径。
```
void savePcmFileCallBack(String filePath);
```
- 获取 sdk wav 格式录音源文件路径。
```
void saveWaveFileCallBack(String filePath);
```
- 设置语音识别器每次最大读取数据量。
```
int maxLengthOnceRead();
```


#### **AudioRecordDataSource**
PcmAudioDataSource 接口的实现类，可以直接读取麦克风输入的音频数据，用于实时识别。

#### **AudioFileDataSource**
PcmAudioDataSource 接口的实现类，可以直接读取单通道、采样率16k的 PCM 音频数据的文件。

>!其他格式的数据无法正确识别。

#### **AAILogger**
用户可以利用 AAILogger 来控制日志的输出，可以选择性的输出 debug、info、warn 以及 error 级别的日志信息。

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

## 音频数据本地缓存指引
宿主层可根据自身业务需求选择将音频保存到本地或者不保存。若需要保存到本地可按照如下步骤进行操作：
1. `new AudioRecordDataSource(isSaveAudioRecordFiles)` 初始化时，`isSaveAudioRecordFiles` 设置为 true。
2. `AudioRecognizeStateListener.onStartRecord` 回调函数内添加创建本次录音的文件逻辑。路径、文件名可支持自定义。
3. `AudioRecognizeStateListener.onStopRecord` 回调函数内添加关流逻辑。（可选）将 PCM 文件转存为 WAV 文件。
4. `AudioRecognizeStateListener.onNextAudioData` 回调函数内添加将音频流写入本地文件的逻辑。
5. 由于回调函数均跑在 sdk 线程中。为了避免写入业务耗时问题影响 sdk 内部运行流畅度，建议将上述步骤放在单独线程池里完成，详情见 Demo 工程中的 `MainActivity` 类中的示例代码。
