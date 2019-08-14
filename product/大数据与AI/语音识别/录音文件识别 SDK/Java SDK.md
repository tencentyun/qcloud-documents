## 1. 接入准备

### 1.1 SDK 获取

录音文件识别 Java SDK 以及 Demo 的下载地址：[Java SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/java_record_asr_sdk.tar.gz)。

### 1.2 接入须知

开发者在调用前请先查看录音文件识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/35721) ，了解接口的**使用要求**和**使用步骤**。

### 1.3 开发环境

**环境依赖**

该接口需要的 JDK 版本要满足1.8及以上。 

**安装 SDK**

+ 本文件夹包含了 jar 包和源码。源码可通过 Eclipse 直接打开，或将 src 拷至 IDEA 等软件中。   
+ jar 包使用步骤如下：
	+ 找到 out 和 lib 文件夹中的 jar 文件，将所有的 jar文件复制到您的工程文件夹中。如果第三方 jar文件和您已使用的 jar文件有重复，可选择其一。   
	+ 右键单击 Eclipse 选择【您的项目】>【Properties】>【Java Build Path】>【Add JARs】。   
	+ 将 jar 文件 include 到您的项目中。包括out 文件夹中的 off\_asr\_sdk\_1.0.jar 和 lib 中的9个依赖工具包。
+ 添加完成后用户即可在工程中使用录音文件识别 SDK 。

## 2. 快速接入

### 2.1 开发流程介绍

录音文件识别支持以下两种数据上传方式。

**指定 Url，发出请求**：

```
//指定语音文件的Url，发出请求。建议使用此方法。
OasrRequesterSender oasrRequesterSender = new OasrRequesterSender();
OasrBytesRequest oasrBytesRequest = new OasrBytesRequest("http://xxx.xx.xxx",
		"https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav");
//发送请求
OasrResponse oasrResponse = oasrRequesterSender.send(oasrBytesRequest);
```

**以 HttpBody 方式，发出请求**：

```
// 从文件中读取语音数据，通过HttpBody发出请求。语音文件大小需小于5兆才可使用此方法。
OasrRequesterSender oasrRequesterSender = new OasrRequesterSender();
byte[] content = ByteUtils.inputStream2ByteArray("test_wav/8k/8k.wav");
OasrBytesRequest oasrBytesRequest = new OasrBytesRequest("http://xxx.xx.xxx", content);
//发送请求
OasrResponse oasrResponse = oasrRequesterSender.send(oasrBytesRequest);
```

### 2.2 主要接口方法说明

**initBaseParameters**

+ 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取您的 AppID、SecretId、SecretKey。

```
/*
** 初始化基础参数, 请将下面的参数值配置成您自己的值。
** 
** 参数获取方法可参考： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
*/
private static void initBaseParameters() {
	// required, 必须配置
	// AsrBaseConfig.appId = "YOUR_APP_ID_SET_HERE";
	// AsrBaseConfig.secretId = "YOUR_SECRET_ID";
	// AsrBaseConfig.secretKey = "YOUR_SECRET_KEY";
	AsrInternalConfig.SUB_SERVICE_TYPE = 0; // 0表示离线识别

	// optional，根据自身需求配置值
	AsrPersonalConfig.engineModelType = EngineModelType._8k_0;
	AsrPersonalConfig.voiceFormat = VoiceFormat.wav;
}
```
**sendUrlRequest**

```
/*
** 指定语音文件的Url，发出请求。建议使用此方法。
*/
private void sendUrlRequest() {
	OasrBytesRequest oasrBytesRequest = new OasrBytesRequest("http://xxx.xx.xxx",
			"https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav");
	// oasrBytesRequest.setChannelNum(2); //设置为2声道语音，默认为1声道。目前仅8K语音支持2声道。
	OasrResponse oasrResponse = this.oasrRequesterSender.send(oasrBytesRequest);
	this.printReponse(oasrResponse);
}
```
**sendBytesRequest**

```
/*
** 从文件中读取语音数据，通过HttpBody发出请求。语音文件大小需小于5兆才可使用此方法。
*/
private void sendBytesRequest() {
	byte[] content = ByteUtils.inputStream2ByteArray("test_wav/8k/8k.wav");
	OasrBytesRequest oasrBytesRequest = new OasrBytesRequest("http://xxx.xx.xxx", content);
	//特别设置为2声道，默认为1声道。目前仅8K语音支持2声道。
	oasrBytesRequest.setChannelNum(2); 
	OasrResponse oasrResponse = this.oasrRequesterSender.send(oasrBytesRequest);
	this.printReponse(oasrResponse);
}
```
**start**

```
/*
** 启动服务
*/
private void start() {
	this.sendUrlRequest();
	System.exit(0);
}
```



### 2.3 入门示例

```
public class OasrRequestSample {

	private OasrRequesterSender oasrRequesterSender = new OasrRequesterSender();

	static {
		initBaseParameters();
	}

	public static void main(String[] args) {
		OasrRequestSample rasrRequestSample = new OasrRequestSample();
		rasrRequestSample.start();
	}

	private void start() {
		this.sendUrlRequest();
		System.exit(0);
	}

	/**
	 * 指定语音文件的Url，发出请求。建议使用此方法。
	 */
	private void sendUrlRequest() {
		OasrBytesRequest oasrBytesRequest = new OasrBytesRequest("http://xxx.xx.xxx",
				"https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav");
		OasrResponse oasrResponse = this.oasrRequesterSender.send(oasrBytesRequest);
		this.printReponse(oasrResponse);
	}

	private void printReponse(OasrResponse oasrResponse) {
		if (oasrResponse != null)
			System.out.println("Result is: " + oasrResponse.getOriginalText());
		else
			System.out.println("Result is null.");
	}

	/**
	 * 初始化基础参数, 请将下面的参数值配置成您自己的值。
	 * 
	 * 参数获取方法可参考： <a href="https://cloud.tencent.com/document/product/441/6203">签名鉴权 获取签名所需信息</a>
	 */
	private static void initBaseParameters() {
		AsrInternalConfig.SUB_SERVICE_TYPE = 0; // 0表示离线识别
		// optional，根据自身需求配置值
		AsrPersonalConfig.engineModelType = EngineModelType._8k_0;
		AsrPersonalConfig.voiceFormat = VoiceFormat.wav;
	}

}
```
