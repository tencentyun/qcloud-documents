## SDK 功能简介

语音消息 SDK 支持以下操作：
- [发送语音验证码](#发送语音验证码)
- [指定模板发送语音通知](#指定模板发送语音通知)

>?
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#指定模板发送语音通知)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。

## SDK 使用指南
### 相关资料
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/1128/37530) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_java) 和 [错误码](https://cloud.tencent.com/document/product/1128/37531)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDK AppID 和 App Key**
语音消息应用 **SDK AppID** 和 **App Key** 可在 [语音消息控制台](https://console.cloud.tencent.com/vms) 的应用信息里获取。如您尚未添加应用，请登录语音消息控制台 [创建应用](https://cloud.tencent.com/document/product/1128/37461)。
- **申请模板并确认审核通过**
语音正文内容**模板**需申请和审核，**模板**可在 [语音消息控制台](https://console.cloud.tencent.com/vms) 的【应用管理】>【语音模板】页面申请，详细申请操作请参见 [配置语音模板](https://cloud.tencent.com/document/product/1128/37517)。


### 配置 SDK
qcloudsms_java 可以采用多种方式进行安装，我们提供以下三种方法供用户使用：

- **maven**
使用 qcloudsms_java 功能前，需要先在 pom.xml 中添加如下依赖：
```
<dependency>
  <groupId>com.github.qcloudsms</groupId>
  <artifactId>qcloudsms</artifactId>
  <version>1.0.6</version>
</dependency>
```

- **sbt**
```
libraryDependencies += "com.github.qcloudsms" % "sms" % "1.0.6"
```

- **其他**

 - 方法1
 将 [源代码](https://github.com/qcloudsms/qcloudsms_java/tree/master/src) 直接引入到项目工程中。
 >?由于 qcloudsms_java 依赖四个依赖项目 library： [org.json](http://central.maven.org/maven2/org/json/json/20170516/json-20170516.jar)，[httpclient](http://central.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar)，[httpcore](http://central.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.7/httpcore-4.4.7.jar) 和 [httpmine](http://central.maven.org/maven2/org/apache/httpcomponents/httpmime/4.5.3/httpmime-4.5.3.jar)。若采用方法1，需要将以上四个 jar 包一并导入工程。

 - 方法2
 将 [JAR 包](https://github.com/qcloudsms/qcloudsms_java/releases) 直接引入到您的工程中。

### 示例代码

>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改。

- **准备必要参数**
```java
// 语音消息应用 SDK AppID
int appid = 1400009099; // SDK AppID 以1400开头
// 语音消息应用 App Key
String appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
// 需要发送语音消息的手机号码
String[] phoneNumbers = {"21212313123", "12345678902", "12345678903"};
// 语音模板 ID，需要在语音消息控制台中申请
int templateId = 7839; // NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在语音消息控制台中申请
```

<a id="发送语音验证码" ></a>
- **发送语音验证码**
```java
import com.github.qcloudsms.SmsVoiceVerifyCodeSender;
import com.github.qcloudsms.SmsVoiceVerifyCodeSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    SmsVoiceVerifyCodeSender vvcsender = new SmsVoiceVerifyCodeSender(appid,appkey);
    SmsVoiceVerifyCodeSenderResult result = vvcsender.send("86", phoneNumbers[0],
        "5678", 2, "");
    System.out.println(result);
} catch (HTTPException e) {
    // HTTP 响应码错误
    e.printStackTrace();
} catch (JSONException e) {
    // JSON 解析错误
    e.printStackTrace();
} catch (IOException e) {
    // 网络 IO 错误
    e.printStackTrace();
}
```


<a id="指定模板发送语音通知" > </a>
- **指定模板发送语音通知**
```java
import com.github.qcloudsms.TtsVoiceSender;
import com.github.qcloudsms.TtsVoiceSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    int templateId = 45221;
    String[] params = {"5678"};
    TtsVoiceSender tvsender = new TtsVoiceSender(appid, appkey);
    TtsVoiceSenderResult result = tvsender.send("86", phoneNumbers[0],
        templateId, params, 2, "");
    System.out.println(result);
} catch (HTTPException e) {
    // HTTP 响应码错误
    e.printStackTrace();
} catch (JSONException e) {
    // JSON 解析错误
    e.printStackTrace();
} catch (IOException e) {
    // 网络 IO 错误
    e.printStackTrace();
}
```
