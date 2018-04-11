## 开发准备
### SDK 获取
短信 Java SDK 在 Github 中的下载地址：[短信 Java SDK](https://github.com/qcloudsms/qcloudsms_java)。

### 开发准备
**1. 申请 SDK AppID 以及 App Key：**
在开始本教程之前，您需要先获取 SDK AppID 和 App Key，如您尚未申请，请到 [短信控制台](https://console.cloud.tencent.com/sms) 中添加应用。应用添加成功后您将获得 SDK AppID 以及 App Key。
>**注意：**
> SDK AppID 是以 14xxxxx 开头。

**2. 申请签名：**
下发短信必须携带签名，您可以在短信 [控制台](https://console.cloud.tencent.com/sms) 中申请短信签名，详细申请操作参考 [创建签名](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。

**3. 申请模板：**
下发短信内容必须经过审核，您可以在短信 [控制台](https://console.cloud.tencent.com/sms) 中申请短信模板，详细申请操作参考 [创建正文模板](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E7.89.88)。

完成以上三项便可开始代码开发。

### SDK 配置
qcloudsms 可以采用多种方式进行配置，我们提供以下三种方法供用户使用：
- **maven**
 要使用 qcloudsms 功能，需要在 pom.xml 中添加如下依赖： 
```
<dependency>
  	<groupId>com.github.qcloudsms</groupId>
  	<artifactId>sms</artifactId>
  	<version>1.0.2</version>
</dependency>
```

- **sbt**
```
libraryDependencies += "com.github.qcloudsms" % "sms" % "1.0.2"
```

- **其他方法**
**方法1：** 将 [源代码	](https://github.com/qcloudsms/qcloudsms_java/tree/master/src) 直接引入到项目工程中。
**方法2：**将 [JAR包]( http://central.maven.org/maven2/com/github/qcloudsms/sms/0.9.2/sms-0.9.2.jar) 直接引入到您的工程中。
>**注意：**
由于 qcloudsms 中需要使用以下四个依赖项目：
[org.json](http://central.maven.org/maven2/org/json/json/20170516/json-20170516.jar) ，[httpclient](http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar)，[httpcore](http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.7/httpcore-4.4.7.jar)，[httpmine](http://central.maven.org/maven2/org/apache/httpcomponents/httpmime/4.5.3/httpmime-4.5.3.jar)，采用方法 1，方法 2 都需要将以上四个 jar 包导入工程。


## 快速入门
若您对接口存在疑问，可以查阅 [API 文档](https://cloud.tencent.com/document/product/382/13297)。

首先导入库：
```
import com.github.qcloudsms.*;
```
导入 qcloudsms 库之后可以开始发送短信。

- **单发短信**
```java
 try {
        SmsSingleSender sender = new   SmsSingleSender(appid, "replace with key");
	SmsSingleSenderResult result = sender.send(0, "86", "18326693192", "【腾讯】验证码测试1234", "", "123");
	System.out.print(result);
 } catch (Exception e) {
	e.printStackTrace();
 }
```
> **注意：**
> 如需发送国际短信，同样可以使用此接口，只需将国家码"86"改写成对应国家码号。

- **指定模板 ID 单发短信**
```java
//假设短信模板 id 为 123，模板内容为：测试短信，{1}，{2}，{3}，上学。
 SmsSingleSender sender = new SmsSingleSender(appid,"replace with key");
 ArrayList<String> params = new ArrayList<String>();
 params.add("指定模板单发");
 params.add("深圳");
 params.add("小明");
 SmsSingleSenderResult   result = sender.sendWithParam("86", "18326693192", 123, params, "", "", "");
 System.out.println(result);
```
> **注意：**
> 无论单发短信还是指定模板 ID 单发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

- **群发短信**
```java
// 初始化群发
SmsMultiSender multiSender = new SmsMultiSender(appid, "replace with key");
// 普通群发
// 下面是 3 个假设的号码
ArrayList<String> phoneNumbers = new ArrayList<String>();
phoneNumbers.add("13101116651");
phoneNumbers.add("13101116652");
phoneNumbers.add("13101116653");
SmsMultiSenderResult multiSenderResult = multiSender.send(0, "86", phoneNumbers, 
	"【腾讯】测试短信，普通群发，深圳，小明，上学。", "", "");
System.out.println(multiSenderResult);
```

- **指定模板 ID 群发**
```java
SmsMultiSender multiSender = new SmsMultiSender(appid, "replace with key");
// 下面是 3 个假设的号码
ArrayList<String> phoneNumbers = new ArrayList<String>();
phoneNumbers.add("13101116651");
phoneNumbers.add("13101116652");
phoneNumbers.add("13101116653");
// 假设短信模板 id 为 123，模板内容为：测试短信，{1}，{2}，{3}，上学。
params = new ArrayList<String>();
params.add("指定模板群发");
params.add("深圳");
params.add("小明");
multiSenderResult = multiSender.sendWithParam("86", phoneNumbers, 123, params, "", "", "");
System.out.println(multiSenderResult);
```
> **注意：**
> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。

- **发送语音验证码**
```java
  //语音验证码发送
  SmsVoiceVerifyCodeSender smsVoiceVerifyCodeSender = new SmsVoiceVerifyCodeSender(appid, "replace with key");
  SmsVoiceVerifyCodeSenderResult smsVoiceVerifyCodeSenderResult = smsVoiceVerifyCodeSender.send("86",
      "1310555552", "123",2,"");
  System.out.println(smsVoiceVerifyCodeSenderResult);
```
>**注意：**
>语音验证码发送只需提供验证码数字，例如在 msg=“123”，您收到的语音通知为“您的语音验证码是 1 2 3”，如需自定义内容，可以使用语音通知。

- **发送语音通知**
```java
   SmsVoicePromptSender smsVoicePromtSender = new SmsVoicePromptSender(appid, "replace with key");
   SmsVoicePromptSenderResult smsSingleVoiceSenderResult = smsVoicePromtSender.send("86", "13758028086", 2,2,
     "欢迎使用XXX，本次活动xxx", "");
   System.out.println(smsSingleVoiceSenderResult);
```

- **拉取短信回执以及回复**
```java
   SmsStatusPuller pullstatus = new SmsStatusPuller(appid, "replace with key");
   SmsStatusPullCallbackResult callbackResult = pullstatus.pullCallback(10);
   System.out.println(callbackResult);
   SmsStatusPullReplyResult replyResult = pullstatus.pullReply(10);
   System.out.println(replyResult);
```
> **注意：**
>  短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送国际短信**
国际短信参考单发短信。


