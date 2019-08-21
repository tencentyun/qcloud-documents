## 接入准备

### SDK 获取
实时语音识别 Java SDK 以及 Demo 的下载地址：[Java SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/java_realtime_asr_sdk.tar.gz)。

### 接入须知
开发者在调用前请先查看实时语音识别的[ 接口说明](https://cloud.tencent.com/document/product/1093/37138)，了解接口的**使用要求**和**使用步骤**。


### 开发环境
**环境依赖**
该接口需要满足 JDK1.8 及以上版本。

**安装 SDK**
+ 本 SDK 文件夹包含了 Jar 包和源码。源码可通过 Eclipse 直接打开，或将 src 拷至 IDEA 等软件中使用。    
+ 可以先浏览 docs 目录中的“压缩包目录结构说明.png”，了解该SDK的主要结构。   
+ Jar 包使用步骤举例如下：
	+ 找到 out 和 lib 文件夹中的 jar 文件。将所有的 jar文件 复制到您的工程文件夹中。如果第三方 jar 文件和您已使用的 jar 文件有重复，可选择其一。
	+ 右键单击 Eclipse 选择【您的项目】>【Properties】>【Java Build Path】>【Add JARs】。
	+ 将 jar 文件 include 到您的项目中。包括 out 文件夹中的 real\_asr\_sdk\_1.5.jar 和 lib 中的8个依赖工具包。

+ 添加完成后用户即可在工程中使用实时语音 SDK 。

## 快速接入

### 开发流程介绍
+ **新建一个服务**

```
this.receiverEntrance = new ReceiverEntrance(taskId);
```

+ **启动服务**

```
this.receiverEntrance.start();
```

+ **注册 N 个回调 Handler**

```
this.receiverEntrance.registerReponseHandler(new MyResponseHandler(this.taskId));
```

+ **添加数据**

```
this.voiceAddingTask = new VoiceAddingTask(this.receiverEntrance, voiceFile);
```

+ **执行**

```
this.voiceAddingTask.start();
```

### 主要接口方法说明

+ **start**

```
/*
** 将异步服务启动起来。对于当前对象，仅需调用一次。
*/
public void start() {
	this.requestService.start();
	this.notifyService.start();
}
```  
+ **registerReponseHandler**

```
/*
** 回调接口注册。即：注册接收回复的处理类，回复数据收到后，处理类中的onUpdate方法会被调用。
** @param flowHandler 用户自己的实现了flowHandler接口的类。
*/
public void registerReponseHandler(FlowHandler flowHandler) {
	this.notifyService.register(flowHandler);
}
``` 
+ **add**

```
/*
** 增加声音数据到缓存。
** @param content 字节数组
** @return true 表示成功。false 表示添加失败，通常是因为调用太频繁，内存积压太多数据（暂定：超过1万条）未被发出造成。
*/
public boolean add(byte[] content) {
	return this.receiverCache.add(content);
}

/*
** 增加声音数据到缓存且标识当前这份数据是否为一句语音的结尾。
** @param content  字节数组
** @param endFlag  结束标记
** @return true 表示成功。false 表示添加失败，通常是因为调用太频繁，内存积压太多数据（暂定：超过1万条）未被发出造成。
*/
public boolean add(byte[] content, boolean endFlag) {
	return this.receiverCache.add(content, endFlag);
}
```

+ **voiceEnd**

```
/*
** 标记当前声音数据到达一句的结尾。
*/
public void voiceEnd() {
	this.receiverCache.voiceEnd();
}
```  

+ **stopService**

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




### 入门示例

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
