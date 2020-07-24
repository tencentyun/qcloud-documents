## 签名
用户需要自己使用 AbsCredentialProvider 接口来计算签名，计算签名函数：
```
String getAudioRecognizeSign(String source);
```
计算最终签名算法：
先以 SecretKey 对 source 进行 HMAC-SHA1 加密，然后对密文进行 Base64 编码，获得最终的签名串。即：sign=Base64Encode(HmacSha1(source,secretKey))。
为了方便用户测试，SDK 已有一个实现类 LocalCredentialProvider，但为了保证 SecretKey 的安全性，请仅在测试环境下使用，正式版本下请在第三方服务器上获取签名。

## 初始化 AAIClient
AAIClient 是语音服务的核心类，用户可以调用该类来开始、停止以及取消语音识别。
```
public AAIClient(Context context, int appid, int projectId, String secreteId, AbsCredentialProvider credentialProvider) throws ClientException
```
参数名称|类型|是否必填|参数描述
--|--|--|--
context|Context|是|上下文
APPID|int|是|腾讯云注册的APPID
projectId|int|否|用户的projectId
secreteId|String|是|用户的SecreteId
credentialProvider|AbsCredentialProvider|是|鉴权类
示例
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
## 配置全局参数
用户调用 ClientConfiguration 类的静态方法来修改全局配置。

方法| 方法描述 | 默认值 | 有效范围
--|--
setServerProtocolHttps| 设置Https/Http协议 | true(Https) | false/true
setMaxAudioRecognizeConcurrentNumber | 语音识别最大并发请求数 | 2|1~5
setMaxRecognizeSliceConcurrentNumber | 语音识别分片最大并发数 | 5|1~5
setAudioRecognizeSliceTimeout | HTTP读超时时间 | 5000ms | 500~10000ms
setAudioRecognizeConnectTimeout | HTTP连接超时时间 | 5000ms| 500~10000ms
setAudioRecognizeWriteTimeout | Http写超时时间 | 5000ms| 500~10000ms
示例
```
ClientConfiguration.setServerProtocolHttps(true);
ClientConfiguration.setMaxAudioRecognizeConcurrentNumber(2)
ClientConfiguration.setMaxRecognizeSliceConcurrentNumber(5)
ClientConfiguration.setAudioRecognizeSliceTimeout(2000)
ClientConfiguration.setAudioRecognizeConnectTimeout(2000)
ClientConfiguration.setAudioRecognizeWriteTimeout(2000)
```
## 设置结果监听器
AudioRecognizeResultListener 可以用来监听语音识别的结果，共有如下四个接口：
- 语音分片的语音识别结果回调接口

```
void onSliceSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```

参数| 参数类型|参数描述 
--|--
request|AudioRecognizeRequest| 语音识别请求 
result |AudioRecognizeResult| 语音分片的语音识别结果
order|int| 该语音分片所在语音流的次序

- 语音流的语音识别结果回调接口

```
void onSegmentSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```

参数| 参数类型|参数描述 
--|--
request|AudioRecognizeRequest| 语音识别请求 
result |AudioRecognizeResult| 语音分片的语音识别结果
order|int| 该语音流的次序

- 返回所有的识别结果

```
void onSuccess(AudioRecognizeRequest request, String result);
```

参数| 参数类型|参数描述 
--|--
request|AudioRecognizeRequest| 语音识别请求 
result|String| 所有的识别结果

- 语音识别请求失败回调函数

```
void onFailure(AudioRecognizeRequest request, ClientException clientException, ServerException serverException);
```

参数| 参数类型|参数描述 
--|--
request|AudioRecognizeRequest| 语音识别请求 
clientException|ClientException| 客户端异常
serverException|ServerException|服务端异常
示例代码见 快速入门。

## 设置语音识别参数
通过构建 AudioRecognizeConfiguration 类，可以设置语音识别时的配置：

参数名称|类型|是否必填|参数描述|默认值
--|--|--|--
enableSilentDetect| boolean | 否 | 是否开启静音检测，开启后说话前的静音部分不进行识别|true
enableFirstAudioFlow|boolean |否|是否开启检测说话启始超时，开启后超时会自动停止录音|false
enableNextAudioFlow|boolean|否|是否开启检测说话结束超时，开启后超时会自动停止录音|false
minAudioFlowSilenceTime|int|否|两个语音流最短分割时间|1500ms
maxAudioFlowSilenceTime|int|否|语音终点超时时间|10000ms
maxAudioStartSilenceTime|int|否|语音起点超时时间|2000ms
minVolumeCallbackTime|int |否|音量回调时间|80ms
sensitive|float|否|语音识别敏感度，越小越敏感(范围1~5)|3

示例：
```
AudioRecognizeConfiguration audioRecognizeConfiguration = new AudioRecognizeConfiguration.Builder()
	.enableAudioStartTimeout(true) // 是否使能起点超时停止录音
    .enableAudioEndTimeout(true) // 是否使能终点超时停止录音
    .enableSilentDetect(true) // 是否使能静音检测，true表示不检查静音部分
    .minAudioFlowSilenceTime(1000) // 语音流识别时的间隔时间
    .maxAudioFlowSilenceTime(10000) // 语音终点超时时间
    .maxAudioStartSilenceTime(2000) // 语音起点超时时间
    .minVolumeCallbackTime(80) // 音量回调时间
	.sensitive(2.8) // 识别敏感度
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

## 设置状态监听器
AudioRecognizeStateListener 可以用来监听语音识别的的状态，一共有如下七个接口：

方法| 方法描述 
--|--
onStartRecord| 开始录音
onStopRecord | 结束录音
onVoiceFlowStart | 检测到语音流的起点 
onVoiceFlowFinish | 检测到语音流的终点 
onVoiceFlowStartRecognize | 语音流开始识别
onVoiceFlowFinishRecognize | 语音流结束识别 
onVoiceVolume | 音量 

## 设置超时监听器
AudioRecognizeTimeoutListener 可以用来监听语音识别的的超时，一共有如下两个接口：

方法| 方法描述 
--|--
onFirstVoiceFlowTimeout| 检测第一个语音流超时
onNextVoiceFlowTimeout | 检测下一个语音流超时

示例：
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

AudioRecognizeTimeoutListener audioRecognizeTimeoutListener = new AudioRecognizeTimeoutListener() {
    @Override
    public void onFirstVoiceFlowTimeout(AudioRecognizeRequest audioRecognizeRequest) {
        // 检测语音起始超时
    }

    @Override
    public void onNextVoiceFlowTimeout(AudioRecognizeRequest audioRecognizeRequest) {
		// 检测语音结束超时
    }
};

// 启动语音识别
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null) {
            aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener, audioRecognizeStateListener,audioRecognizeTimeoutListener, audioRecognizeConfiguration);
        }
    }
}).start();
```



## 其他重要类说明

### AudioRecognizeRequest
templateName 和 customTemplate 都设置时，优先使用 templateName 的设置。

参数名称|类型|是否必填|参数描述|默认值
--|--|--|--
pcmAudioDataSource|PcmAudioDataSource|是|音频数据源|无
templateName| String | 否 | 用户控制台设置的模板名称|无
customTemplate|AudioRecognizeTemplate|否|用户自定义的模板|(1, 0, 1)
### AudioRecognizeResult
语音识别结果对象，和 AudioRecognizeRequest 对象相对应，用于返回语音识别的结果。

参数名称|类型|参数描述
--|--|--|--
code|int|识别状态码
message| String | 识别提示信息
text|String|识别结果
seq|int|该语音分片的序号
voiceId|String|该语音分片所在语音流的ID
cookie|String|cookie 值

## AudioRecognizeTemplate
自定义的语音模板，需要设置的参数包括：

参数名称|类型|是否必填|参数描述
--|--|--|--
engineModelType|int|是|引擎模型类型
resultTextFormat| int | 是 | 识别文本结果的编码形式，可选值包括：UTF-8，GB2312，GBK，BIG5
resType|int|是|结果返回方式
示例：
```
AudioRecognizeTemplate audioRecognizeTemplate = new AudioRecognizeTemplate(1,0,1);
```
## PcmAudioDataSource
用户可以实现这个接口来识别单通道、采样率 16k 的 PCM 音频数据。主要包括如下几个接口：

- 向语音识别器添加数据，将长度为 length 的数据从下标 0 开始复制到 audioPcmData 数组中，并返回实际的复制的数据量的长度。

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
- 设置语音识别器每次最大读取数据量。

```
int maxLengthOnceRead();
```
## AudioRecordDataSource
PcmAudioDataSource 接口的实现类，可以直接读取麦克风输入的音频数据，用于实时识别。
## AudioFileDataSource
PcmAudioDataSource 接口的实现类，可以直接读取单通道、采样率 16k 的 PCM 音频数据的文件。
>**注意：**
>其他格式的数据无法正确识别。

## AAILogger
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