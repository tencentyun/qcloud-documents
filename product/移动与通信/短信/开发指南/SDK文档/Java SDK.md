## SDK 功能简介
目前腾讯云短信为客户提供**国内短信、语音短信**和**国际短信**服务，腾讯云短信 SDK 支持以下操作：

| 国内短信             | 语音短信              | 国际短信                 |
| ------------------ | ---------------------- | ---------------- |
| <li>[单发短信](#单发短信)<li>[指定模板单发短信](#指定模板单发短信)<li>[群发短信](#群发短信)<li>[指定模板群发短信](#指定模板群发短信)<li>[拉取短信回执和短信回复状态](#拉取短信回执) | <li>[发送语音验证码](#发送语音验证码)<li>[发送语音通知](#发送语音通知)<li>[指定模板发送语音通知](#指定模板发送语音通知) | <li>[单发短信](#单发短信)<li>[指定模板单发短信](#指定模板单发短信)<li>[群发短信](#群发短信)<li>[指定模板群发短信](#指定模板群发短信)<li>[拉取短信回执](#拉取短信回执) |

>?
>- 群发短信
>一次群发请求最多支持200个号码，如对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：[3012203387](https://main.qcloudimg.com/raw/e674a37df984126f53ab9cbf4b9a168a.html)）。
>- 拉取短信回执
>该功能默认关闭。您可以根据实际需求联系腾讯云短信技术支持（QQ：[3012203387](https://main.qcloudimg.com/raw/e674a37df984126f53ab9cbf4b9a168a.html)）开通，实现批量拉取短信回执。
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#发送语音通知)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。

## SDK 使用指南
### 相关资料
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/382/13297) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_java) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDKAppID 和 AppKey**
云短信应用 **SDKAppID** 和 **AppKey** 可在 [短信控制台](https://console.cloud.tencent.com/sms) 的应用信息里获取。如您尚未添加应用，请登录 [短信控制台](https://console.cloud.tencent.com/sms) 添加应用。
- **申请签名并确认审核通过**
一个完整的短信由短信**签名**和**短信正文内容**两部分组成，短信**签名**需申请和审核，**签名**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建签名](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。发送国际短信时，允许不携带签名。
- **申请模板并确认审核通过**
短信或语音正文内容**模板**需申请和审核，**模板**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建正文模板](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E6.9D.BF)。


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
// 短信应用 SDK AppID
int appid = 1400009099; // SDK AppID 以1400开头
// 短信应用 SDK AppKey
String appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
// 需要发送短信的手机号码
String[] phoneNumbers = {"21212313123", "12345678902", "12345678903"};
// 短信模板 ID，需要在短信应用中申请
int templateId = 7839; // NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
// 签名
String smsSign = "腾讯云"; // NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台申请
```

<a id="单发短信"></a>
- **单发短信**
```java
import com.github.qcloudsms.SmsSingleSender;
import com.github.qcloudsms.SmsSingleSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    SmsSingleSender ssender = new SmsSingleSender(appid, appkey);
    SmsSingleSenderResult result = ssender.send(0, "86", phoneNumbers[0],
        "【腾讯云】您的验证码是: 5678", "", "");
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

<a id="指定模板单发短信"></a>
- **指定模板 ID 单发短信**
```java
import com.github.qcloudsms.SmsSingleSender;
import com.github.qcloudsms.SmsSingleSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    String[] params = {"5678"};
    SmsSingleSender ssender = new SmsSingleSender(appid, appkey);
    SmsSingleSenderResult result = ssender.sendWithParam("86", phoneNumbers[0],
        templateId, params, smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
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

<a id="群发短信" ></a>
- **群发短信**
```java
import com.github.qcloudsms.SmsMultiSender;
import com.github.qcloudsms.SmsMultiSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    SmsMultiSender msender = new SmsMultiSender(appid, appkey);
    SmsMultiSenderResult result =  msender.send(0, "86", phoneNumbers,
        "【腾讯云】您的验证码是: 5678", "", "");
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


<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**
```java
import com.github.qcloudsms.SmsMultiSender;
import com.github.qcloudsms.SmsMultiSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    String[] params = {"5678"};
    SmsMultiSender msender = new SmsMultiSender(appid, appkey);
    SmsMultiSenderResult result =  msender.sendWithParam("86", phoneNumbers,
        templateId, params, smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
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

<a id="拉取短信回执" > </a>
- **拉取短信回执以及回复**
```java
import com.github.qcloudsms.SmsStatusPuller;
import com.github.qcloudsms.SmsStatusPullCallbackResult;
import com.github.qcloudsms.SmsStatusPullReplyResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    // Note: 短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387）开通权限
    int maxNum = 10;  // 单次拉取最大量
    SmsStatusPuller spuller = new SmsStatusPuller(appid, appkey);

    // 拉取短信回执
    SmsStatusPullCallbackResult callbackResult = spuller.pullCallback(maxNum);
    System.out.println(callbackResult);

    // 拉取回复，国际短信不支持回复功能
    SmsStatusPullReplyResult replyResult = spuller.pullReply(maxNum);
    System.out.println(replyResult);
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

- **拉取单个手机短信状态**
```java
import com.github.qcloudsms.SmsMobileStatusPuller;
import com.github.qcloudsms.SmsStatusPullCallbackResult;
import com.github.qcloudsms.SmsStatusPullReplyResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    int beginTime = 1511125600;  // 开始时间（UNIX timestamp）
    int endTime = 1511841600;    // 结束时间（UNIX timestamp）
    int maxNum = 10;             // 单次拉取最大量
    SmsMobileStatusPuller mspuller = new SmsMobileStatusPuller(appid, appkey);

    // 拉取短信回执
    SmsStatusPullCallbackResult callbackResult = mspuller.pullCallback("86",
        phoneNumbers[0], beginTime, endTime, maxNum);
    System.out.println(callbackResult);

    // 拉取回复，国际短信不支持回复功能
    SmsStatusPullReplyResult replyResult = mspuller.pullReply("86",
        phoneNumbers[0], beginTime, endTime, maxNum);
    System.out.println(replyResult);
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

<a id="发送语音通知" > </a>
- **发送语音通知**
```java
import com.github.qcloudsms.SmsVoicePromptSender;
import com.github.qcloudsms.SmsVoicePromptSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import org.json.JSONException;
import java.io.IOException;
try {
    SmsVoicePromptSender vpsender = new SmsVoicePromptSender(appid, appkey);
    SmsVoicePromptSenderResult result = vpsender.send("86", phoneNumbers[0],
        2, 2, "5678", "");
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

- **发送国际短信**
发送国际短信与发送国内短信类似，只需替换相应的国家码或地区码。详细示例请参考：
 - [单发短信](#单发短信)
 - [指定模板单发短信](#指定模板单发短信)
 - [群发短信](#群发短信)
 - [指定模板群发短信](#指定模板群发短信)
 - [拉取短信回执](#拉取短信回执)


- **使用代理**
部分环境需要使用代理才能上网，可使用 ProxyHTTPClient 来发送请求，示例如下：
```java
import com.github.qcloudsms.SmsSingleSender;
import com.github.qcloudsms.SmsSingleSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import com.github.qcloudsms.httpclient.ProxyHTTPClient;
import org.json.JSONException;
import java.io.IOException;
try {
   // 创建一个代理 httpclient
    ProxyHTTPClient httpclient = new ProxyHTTPClient("127.0.0.1", 8080, "http");

    String[] params = {"5678"};
    SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);
    SmsSingleSenderResult result = ssender.sendWithParam("86", phoneNumbers[0],
        templateId, params, smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
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

- **使用连接池**
多个线程可以共用一个连接池发送 API 请求，多线程并发单发短信示例如下：
```java
import com.github.qcloudsms.SmsSingleSender;
import com.github.qcloudsms.SmsSingleSenderResult;
import com.github.qcloudsms.httpclient.HTTPException;
import com.github.qcloudsms.httpclient.PoolingHTTPClient;
import org.json.JSONException;
import java.io.IOException;
class SmsThread extends Thread {

    private final SmsSingleSender sender;
    private final String nationCode;
    private final String phoneNumber;
    private final String msg;

    public SmsThread(SmsSingleSender sender, String nationCode, String phoneNumber, String msg) {
        this.sender = sender;
        this.nationCode = nationCode;
        this.phoneNumber = phoneNumber;
        this.msg = msg;
    }

    @Override
    public void run() {
        try {
            SmsSingleSenderResult result = sender.send(0, nationCode, phoneNumber, msg, "", "");
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
    }
}
public class SmsTest {

    public static void main(String[] args) {

        int appid = 122333333;
        String appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
        String[] phoneNumbers = {
            "21212313123", "12345678902", "12345678903",
            "21212313124", "12345678903", "12345678904",
            "21212313125", "12345678904", "12345678905",
            "21212313126", "12345678905", "12345678906",
            "21212313127", "12345678906", "12345678907",
        };

        // 创建一个连接池 httpclient, 并设置最大连接量为10
        PoolingHTTPClient httpclient = new PoolingHTTPClient(10);

        // 创建 SmsSingleSender 时传入连接池 http client
        SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);

        // 创建线程
        SmsThread[] threads = new SmsThread[phoneNumbers.length];
        for (int i = 0; i < phoneNumbers.length; i++) {
            threads[i] = new SmsThread(ssender, "86", phoneNumbers[i], "您验证码是：5678");
        }

        // 运行线程
        for (int i = 0; i < threads.length; i++) {
            threads[i].start();
        }

        // join 线程
        for (int i = 0; i < threads.length; i++) {
            threads[i].join();
        }

        // 关闭连接池 httpclient
        httpclient.close();
    }
}
```

- **使用自定义 HTTP client 实现**
如果需要使用自定义的 HTTP client 实现，只需实现 `com.github.qcloudsms.httpclient.HTTPClient` 接口，并在构造 API 对象时传入自定义 HTTP client 即可，参考示例如下：
```java
import com.github.qcloudsms.httpclient.HTTPClient;
import com.github.qcloudsms.httpclient.HTTPRequest;
import com.github.qcloudsms.httpclient.HTTPResponse;
import java.io.IOException;
import java.net.URISyntaxException;
// import com.example.httpclient.MyHTTPClient
// import com.exmaple.httpclient.MyHTTPRequest
// import com.example.httpclient.MyHTTPresponse
public class CustomHTTPClient implements HTTPClient {

    public HTTPResponse fetch(HTTPRequest request) throws IOException, URISyntaxException {
        // 1. 创建自定义 HTTP request
        // MyHTTPrequest req = MyHTTPRequest.build(request)

        // 2. 创建自定义 HTTP cleint
        // MyHTTPClient client = new MyHTTPClient();

        // 3. 使用自定义 HTTP client 获取 HTTP 响应
        // MyHTTPResponse response = client.fetch(req);

        // 4. 转换 HTTP 响应到 HTTPResponse
        // HTTPResponse res = transformToHTTPResponse(response);

        // 5. 返回 HTTPResponse 实例
        // return res;
    }

    public void close() {
        // 如果需要关闭必要资源
    }
}
// 创建自定义 HTTP client
CustomHTTPClient httpclient = new CustomHTTPClient();
// 构造 API 对象时传入自定义 HTTP client
SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);
```
