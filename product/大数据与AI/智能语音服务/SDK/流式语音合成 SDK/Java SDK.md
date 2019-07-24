
流式语音合成 Java SDK [下载地址](https://main.qcloudimg.com/raw/4ac072510ae1fa09afb50a6277fc547b/java_stream_tts_sdk_v1.0.tar.gz )。

接口请求域名：aai.cloud.tencent.com/tts。  

腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。 腾讯 TTS 技术可以应用到很多场景，例如，移动 App 语音播报新闻；智能设备语音提醒；支持车载导航语音合成的个性化语音播报。本接口内测期间免费使用。  

## 开发环境
**基础编译环境**
jdk1.8及以上

本文件夹包含了 Jar 包和源码。源码可通过 Eclipse 直接打开，或将 src 拷至 IDEA 等软件中。

JAR 包使用步骤举例如下：
1. 找到：out 和 lib 文件夹中的 jar 文件，一共16个(包括5个source jar）。
2. 将 jar 复制到您的工程文件夹中。如果第三方 Jar 和您已使用的 Jar 有重复，可选择其一。
3. 右键单击 Eclipse ，选择【您的项目】>【Properties】>【Java Build Path】>【Add JARs】。
4. 将 jar文件 include 到您的项目中。包括：out文件夹中的：tts-sdk-1.0.jar 和第三方的10个依赖工具包。

添加完成后，用户就可以在工程中使用TTS语音合成SDK了。

##  <span id="result">获取用户信息</span>
**获取 AppID，SecretId 与 SecretKey**
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**更改用户信息配置文件**
将查询到的用户信息更改到 SDK 中。

```
/**
* 用户的语音请求基本参数，仅需配置一次，全局使用。通常是注册腾讯云账号后，登录控制台，从“个人 API 密钥”中获得。
* 获取方法请查看： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
* 请用户务必将自己的各项参数值赋值到本类对应变量中。
*/
public class AsrBaseConfig {
	public static String secretId = "AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8";
	public static String secretKey = "kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP";
	public static String appId = "1255628450";
}
```

## 开发相关
**请求参数** 

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| Action |  是 | String | 本接口取值：TextToStreamAudio，不可更改。 |
| AppId  |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| SecretId | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| Timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳。|
| Expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK 默认设置 1 h。
| Text | 是 | String | 合成语音的源文本，最大支持800字符。|
| SessionId | 是 | String | 一次请求对应一个 SessionId，会原样返回，建议传入类似于 uuid 的字符串防止重复。|
| ModelType | 否 | Int | 模型类型，1：默认模型，此字段只需设置为1即可。|
| Volume | 否 | Float | 音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。没有静音选项。<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| Speed | 否 | Int | 语速，范围：[-2，2]分别对应不同语速：<br>-2代表0.6倍 <br>-1代表0.8倍<br>0代表1.0倍（默认）<br>1代表1.2倍<br>2代表1.5倍<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| ProjectId | 否 | Int | 项目 ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0 。|
| VoiceType | 否 | Int | 音色选择：<br>0：亲和女声（默认）<br>1：亲和男声<br>2：成熟男声<br>3：活力男声<br>4：温暖女声<br>5：情感女声<br>6：情感男声|
| PrimaryLanguage | 否 | Int | 主语言类型：<br>1：中文（默认）<br>2：英文 |
| SampleRate | 否 | Int | 音频采样率：<br>16000:16k（默认）<br>8000:8k |
| Codec | 否 | String | 返回音频格式：<br>opus：返回多段含 opus 压缩分片音频，数据量小，建议使用（默认）。<br>pcm：返回二进制 pcm 音频，使用简单，但数据量大。|

**请求接口**
**initBaseParameters**
```
/*
** 初始化基础参数, 请将下面的参数值配置成你自己的值。配置可中途修改，正常情况下立即生效。
** 参数获取方法可参考： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
*/
private static void initBaseParameters() {
	// Required
	// AsrBaseConfig.appId = "YOUR_APP_ID_SET_HERE";
	// AsrBaseConfig.secretId = "YOUR_SECRET_ID";
	// AsrBaseConfig.secretKey = "YOUR_SECRET_KEY";

	// optional，根据自身需求设置配置值， 不配则使用默认值。
	TtsConfig.VOLUME = 5; // 音量大小, 范围[0，10]，默认为0，表示正常音量。
	// TtsConfig.REQUEST_ENCODE = RequestEncode.UTF_8; // 传入的文字所采用的编码，默认为utf-8
	// TtsConfig.SPEED = 0; // 语速，范围[-2，2]. -2: 0.6倍; -1: 0.8倍; 0:1.0倍（默认）; 1: 1.2倍; 2: 1.5倍 。其他值：1.0 倍。
	// TtsConfig.VOICE_TYPE = 0; // 音色： 0：亲和女声（默认） 1：亲和男声 2：成熟男声 3：活力男声 4：温暖女声 5：情感女声 6：情感男声
	// TtsConfig.SAMPLE_RATE = 16000;// 音频采样率： 16000：16k（默认）; 8000：8k
	// TtsConfig.PRIMARY_LANGUAGE = 1;// 主语言类型： 1-中文（默认） 2-英文
	// TtsConfig.CODEC = CodeC.PCM; // 无需修改。暂未支持Opus方式。
}
```
**sendStringRequest**
```
/*
** 从字节数组读取语音数据，发送请求。
*/
private void sendStringRequest() {
	// 方法1：
	TtsSynSender ttsSynSender = new TtsSynSender(); // 创建之后可重复使用
	String text = "早上好，今天天气真不错。";
	TtsResponse response = ttsSynSender.request(text, "session-id-123");
	// TtsResponse response2 = ttsSynSender.sendRequest(text);
	printAndSaveReponse(response);

	// 方法2：
	String filePath = "testTtsFiles/test_article.txt";
	List<TtsResponse> list = ttsSynSender.requestFromFile(filePath, StandardCharsets.UTF_8, "Session-Id-xxx");
	for (TtsResponse ttsResponse : list) {
		printAndSaveReponse(ttsResponse);
	}
}
```

**简单开发流程介绍**  
```
先初始化一次基本参数：
AsrBaseConfig.appId = "YOUR_APP_ID_SET_HERE";
AsrBaseConfig.secretId = "YOUR_SECRET_ID";
AsrBaseConfig.secretKey = "YOUR_SECRET_KEY";
TtsConfig.VOLUME = 5; // 音量大小
.....

然后开始调用：
方法一. 同步调用：
TtsSynSender ttsSynSender = new TtsSynSender(); 
TtsResponse response = ttsSynSender.request(text, "session-id-123");
byte[] pcmBytes = response.getResponseBytes();
String sessionId = response.getSessionId(); // 即： "session-id-123"
或者：
List<TtsResponse> list = ttsSynSender.requestFromFile(filePath, "session-id-xxx");
详见实例类：
/TtsSdkJava/src/com/tencent/cloud/asr/tts/sdk/TtsRequestSample.java


方法二. 异步多线程调用：
线程A不断add文本，线程B收取合成的语音结果字节数组。详见实例类：
/TtsSdkJava/src/com/tencent/cloud/asr/tts/sdk/TtsAsynRequestSample.java
```


## Java 快速入门示例

```
public class TtsRequestSample {

	static {
		initBaseParameters();
	}

	public static void main(String[] args) {
		TtsRequestSample ttsRequestSample = new TtsRequestSample();
		ttsRequestSample.start();
	}

	private void start() {
		this.sendStringRequest();
		System.exit(0);
	}

	/**
	 * 从字节数组读取语音数据，发送请求。
	 */
	private void sendStringRequest() {
		// 方法1：
		TtsSynSender ttsSynSender = new TtsSynSender(); // 创建之后可重复使用
		String text = "早上好，今天天气真不错。";
		TtsResponse response = ttsSynSender.request(text, "session-id-123");
		// TtsResponse response2 = ttsSynSender.sendRequest(text);
		printAndSaveReponse(response);

		// 方法2：
		String filePath = "testTtsFiles/test_article.txt";
		List<TtsResponse> list = ttsSynSender.requestFromFile(filePath, StandardCharsets.UTF_8, "Session-Id-xxx");
		for (TtsResponse ttsResponse : list) {
			printAndSaveReponse(ttsResponse);
		}
	}

	private void printAndSaveReponse(TtsResponse response) {
		if (response != null) {
			new File("logs").mkdirs();
			File pcmFile = new File("logs/" + response.getSessionId() + ".pcm");
			this.savePcmFile(response.getResponseBytes(), pcmFile);
			File wavFile = new File("logs/" + response.getSessionId() + "_Convert.wav");
			this.saveToWavFile(response.getResponseBytes(), pcmFile, wavFile);
			System.out.println("Response: " + response.getSessionId() + ", length: "
					+ response.getResponseBytes().length + ", result saved at: " + pcmFile.getAbsolutePath());
		} else
			System.out.println("Result is null.");
	}

	/**
	 * 初始化基础参数, 请将下面的参数值配置成你自己的值。配置可中途修改，正常情况下立即生效。
	 * 
	 * 参数获取方法可参考： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
	 */
	private static void initBaseParameters() {
		// Required
		// AsrBaseConfig.appId = "YOUR_APP_ID_SET_HERE";
		// AsrBaseConfig.secretId = "YOUR_SECRET_ID";
		// AsrBaseConfig.secretKey = "YOUR_SECRET_KEY";

		// optional，根据自身需求设置配置值， 不配则使用默认值。
		TtsConfig.VOLUME = 5; // 音量大小, 范围[0，10]，默认为0，表示正常音量。
		// TtsConfig.REQUEST_ENCODE = RequestEncode.UTF_8; // 传入的文字所采用的编码，默认为utf-8
		// TtsConfig.SPEED = 0; // 语速，范围[-2，2]. -2: 0.6倍; -1: 0.8倍; 0:1.0倍（默认）; 1: 1.2倍; 2: 1.5倍 。其他值：1.0 倍。
		// TtsConfig.VOICE_TYPE = 0; // 音色： 0：亲和女声（默认） 1：亲和男声 2：成熟男声 3：活力男声 4：温暖女声 5：情感女声 6：情感男声
		// TtsConfig.SAMPLE_RATE = 16000;// 音频采样率： 16000：16k（默认）; 8000：8k
		// TtsConfig.PRIMARY_LANGUAGE = 1;// 主语言类型： 1-中文（默认） 2-英文
		// TtsConfig.CODEC = CodeC.PCM; // 无需修改。暂未支持Opus方式。
	}

	private void savePcmFile(byte[] response, File file) {
		try {
			FileOutputStream out = new FileOutputStream(file, false);
			out.write(response);
			out.close();
		} catch (IOException e) {
			System.err.println("Failed save data to: " + file + ", error: " + e.getMessage());
		}

	}

	/**
	 * 将Pcm文件转换成wav文件保存起来。请将方法中的参数改成自己的语音文件对应的值，本方法仅供参考。
	 * 
	 * 如需改成追加形式输出，请自行修改convert2Wav()方法中new FileOutputStream的参数。
	 */
	private void saveToWavFile(byte[] responseBytes, File pcmFile, File wavFile) {
		int bitNum = TtsConfig.SAMPLE_RATE == 16000 ? 16 : 8;
		PcmUtils.convert2Wav(pcmFile, wavFile, TtsConfig.SAMPLE_RATE, 1, bitNum);
	}
}```




