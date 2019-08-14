实时语音识别 Java SDK [下载地址](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/java_realtime_asr_sdk.tar.gz)。


## 功能简介
语音识别（ASR）可以把音频数据转换为文本，需要持续对音频进行识别的场景，推荐使用实时语音识别，例如视频录制时候的实时字幕，语音对话机器人等。    

- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。  
- 采样率和位深度：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别。
- 我们建议每300或者500毫秒发送一次音频，对此，客户端需要做一些必要的缓存逻辑。
- VAD（Voice Activity Detection）指对语音进行分段的技术，是算法通过对语音之间的停顿进行检测，判断用户说话间的的分句。
- voice_id 用于识别单次对话请求。如果用户持续说话一段时间，包含了很多句话，可以采用一个 voice_id 发送一系列的语音数据，seq 字段表示序号，从0开始。voice_id 不能重复，重复会导致识别错误。

例如，用户说：“今天天气好。”，大概2到3秒的时间。假设1秒发3个请求，则共计会发送8个左右的请求。服务器会返回相应个回包。类似于：
```
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":0,"text":"今"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":1,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":2,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":3,"text":"今天天气"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":4,"text":"今天天气好"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":5,"text":"今天天气好。"}
```

## 开发环境

**依赖环境**
JDK1.8 及以上
**安装 SDK**
本文件夹包含了 Jar 包和源码。源码可通过 Eclipse 直接打开，或将 src 拷至 IDEA 等软件中也可以。
可以先浏览 docs 目录中的图片: 压缩包目录结构说明.png，然后再查看本说明。

JAR 包使用步骤举例如下：
1. 找到：out 和 lib 文件夹中的 jar 文件，一共12个(包括3个 source jar）。
2. 将 jar 复制到您的工程文件夹中。如果第三方 Jar 和您已使用的 Jar 有重复，可选择其一。
3. 右键单击 Eclipse 选择【您的项目】>【Properties】>【Java Build Path】>【Add JARs】。
4. 将 jar 文件 include 到您的项目中。包括：out 文件夹中的：real_asr_sdk_1.5.jar 和第三方的8个依赖工具包。

添加完成后，用户可在工程中使用实时语音 SDK 。

## <span id="result">获取用户信息</span>
-  使用本接口之前需要先 [注册](https://cloud.tencent.com/register) 腾讯云账号，获得 AppID，SecretID 及 SecretKey。  
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。 
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。
- 在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。这一步相当于注册，否则无法使用。

**将 AppID、SecretId、SecretKey 配置到 SDK 中。**

```
/**
 * 用户的语音请求基本参数，仅需配置一次，全局使用。通常是注册腾讯云账号后，登录控制台，从“个人API密钥”中获得。
 * 
 * 获取方法请查看： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
 * 
 * 请用户务必将自己的各项参数值赋值到本类对应变量中。
 * 
 */
public class AsrBaseConfig {
	public static String secretId = "AKID*****************************";
	
	public static String secretKey = "kKm2****************************";

	public static String appId = "1255*******";
}
```


## 开发相关
**请求参数** 

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的AppId，具体可以参考 [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。1：实时流式识别。|
| engine\_model\_type | 否 | String | 引擎类型引擎模型类型。8k_0:8k 通用，16k_0:16k 通用，16k_en:16k英文。|
| result\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5|
| res_type | 否 | Int | 结果返回方式。 1：同步返回；0：尾包返回。|
| voice_format | 否 | Int | 语音编码方式，可选，默认值为 4。1：wav(pcm)；4：speex(sp)；6：silk；8：mp3(仅16k_0模型支持)。|
| needvad | 否 | Int | 0为后台不做 vad 分段，1为后台做自动 vad 分段。|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位。|
| seq | 是 | Int | 	语音分片的序号从0开始。|
| end | 是 | Int | 是否为最后一片，最后一片语音片为1，其余为0。 |
| source | 是 | Int | 设置为0。 |
| voice_id | 是 | String | 16 位 String 串作为每个音频的唯一标识，用户自己生成。|
| projectid  | 否 | Int | 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID：0 |
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳。|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK默认设置1小时。|
| timeout | 是 | Int | 设置超时时间单位为毫秒。|

**返回参数**

| 参数名称 |  描述 |  
| --- | --- |
| code |  0：正常，其他，发生错误。 |
| message | 如果是0就是 success，不是0就是错误的原因信息。 |
| voice_id | 表示这通音频的标记，同一个音频流这个标记一样。 |
| seq | 语音分片的信号。<br> 如果请求参数 needvad为0的话，表示不需要后台做 vad，这里的 seq 就是发送过来的 seq 的序号。<br>如果请求参数 needvad 为1，则表示需要后台做 vad，因后台做 vad ，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，这里返回的 seq 就为0 。|
| text |  如果请求参数 needvad 为0的，表示不需要后台做 vad，text 的值是分片的识别结果。<br>如果请求参数 needvad 为1的话，表示需要后台做 vad，因为后台做 vad 的话，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，text 为"" 。|
| result_number | 请求参数 needvad=1， 此字段有效<br>result_number 表示后面的 result_list 里面有几段结果，如果是0表示没有结果，可能是遇到中间是静音了。<br>如果是1表示 result\_list 有一个结果， 在发给服务器分片很大的情况下可能会出现多个结果，正常情况下都是1个结果。 |
| result_list | 请求参数 needvad=1， 此字段有效 <br>slice\_type: 返回分片类型标记， 0表示一小段话开始，1表示在小段话的进行中，2表示小段话的结束<br>index 表示第几段话<br>start\_time  当前分片所在小段的开始时间（相对整个音频流）。<br>end\_time 当前分片在整个音频流中的结束时间。<br>voice\_text_str 识别结果。 |
| final | 0 表示还在整个音频流的中间部分。<br>1 表示是整个音频流的最后一个包。<br>例如在电信电话场景中，是否是客户端发送的最后一个包的识别结果。 |

**请求 url 参数示例**

```
http://asr.cloud.tencent.com/asr/v1/125000001?
end=0&
engine_model_type=16k_0&
expired=1558016577&
nonce=434303218&
res_type=0&
result_text_format=0&
secretid=XXXXXXXXXXXXXXXXXXXXXXX&
needvad=1&
seq=0&
source=0&
sub_service_type=1&
timeout=5000&
timestamp=1558010577&
voice_format=1&
voice_id=82510017d7deb33e
```

其中v1表示 API 的版本，v1.0，后面125000001是 AppID，各个参数的说明参考上表。

**接口说明**

核心接口方法解释如下：  

**start**
```
/*
** 将异步服务启动起来。对于当前对象，仅需调用一次。
*/
public void start() {
	this.requestService.start();
	this.notifyService.start();
}
```  
**registerReponseHandler**
```
/*
** 回调接口注册。即：注册接收回复的处理类，回复数据收到后，处理类中的onUpdate方法会被调用。
** @param flowHandler 用户自己的实现了flowHandler接口的类。
*/
public void registerReponseHandler(FlowHandler flowHandler) {
	this.notifyService.register(flowHandler);
}
``` 
**add**
```
/*
** 增加声音数据到缓存。
** @param content 字节数组
** @return true表示成功。false表示添加失败，通常是因为调用太频繁，内存积压太多数据（暂定：超过1万条）未被发出造成。
*/
public boolean add(byte[] content) {
	return this.receiverCache.add(content);
}

/*
** 增加声音数据到缓存且标识当前这份数据是否为一句语音的结尾。
** @param content  字节数组
** @param endFlag  结束标记
** @return true表示成功。false表示添加失败，通常是因为调用太频繁，内存积压太多数据（暂定：超过1万条）未被发出造成。
*/
public boolean add(byte[] content, boolean endFlag) {
	return this.receiverCache.add(content, endFlag);
}
```

**voiceEnd**
```
/*
** 标记当前声音数据到达一句的结尾。
*/
public void voiceEnd() {
	this.receiverCache.voiceEnd();
}
```  
**stopService**
```
/*
** 停止服务清空缓存。服务停止后，不会再占用资源。包括：停止异步发送线程 和 通知线程
*/
public void stopService() {
	this.notifyService.stop();
	this.requestService.stop();
	this.receiverCache.clear();
} 
```


**简单开发流程介绍**
**新建一个服务**
```
this.receiverEntrance = new ReceiverEntrance(taskId);
```
**启动服务**
```
this.receiverEntrance.start();
```
**注册 N 个回调 Handler**
```
this.receiverEntrance.registerReponseHandler(new MyResponseHandler(this.taskId));
```
**添加数据**
```
this.voiceAddingTask = new VoiceAddingTask(this.receiverEntrance, voiceFile);
```
**执行**
```
this.voiceAddingTask.start();
```
## Java 快速入门示例

```
public class RasrRequestSample {

	static {
		initBaseParameters();
	}

	public static void main(String[] args) {
		RasrRequestSample rasrRequestSample = new RasrRequestSample();
		rasrRequestSample.start();
	}

	private void start() {
		this.sendBytesRequest();
		System.exit(0);
	}

	/**
	 * 从字节数组读取语音数据，发送请求。
	 */
	private void sendBytesRequest() {
		RequestSender requestSender = new RequestSender();
		byte[] content = ByteUtils.inputStream2ByteArray("test_wav/8k/8k.wav");
		VoiceResponse voiceResponse = requestSender.sendFromBytes(content);
		printReponse(voiceResponse);
	}

	private void printReponse(VoiceResponse voiceResponse) {
		if (voiceResponse != null)
			System.out.println("Result is: " + voiceResponse.getOriginalText());
		else
			System.out.println("Result is null.");
	}

	/**
	 * 初始化基础参数, 请将下面的参数值配置成您自己的值。
	 * 
	 * 参数获取方法可参考： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
	 */
	private static void initBaseParameters() {
		AsrInternalConfig.setSdkRole(SdkRole.ONLINE); // VAD版用户请务必赋值为 SdkRole.VAD
		AsrPersonalConfig.responseEncode = ResponseEncode.UTF_8;
		AsrPersonalConfig.engineModelType = EngineModelType._8k_0;
		AsrPersonalConfig.voiceFormat = VoiceFormat.wav;
	}
}
```

