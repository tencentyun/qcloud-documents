## SDK 功能简介
目前腾讯云短信为客户提供**国内短信、语音短信**和**国际/港澳台短信**服务，腾讯云短信 SDK 支持以下操作：

| 国内短信             | 语音短信               | 国际/港澳台短信                 |
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
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/382/13297) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_csharp) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDKAppID 和 AppKey**
云短信应用 **SDKAppID** 和 **AppKey** 可在 [短信控制台](https://console.cloud.tencent.com/sms) 的应用信息里获取。如您尚未添加应用，请登录 [短信控制台](https://console.cloud.tencent.com/sms) 添加应用。
- **申请签名并确认审核通过**
一个完整的短信由短信**签名**和**短信正文内容**两部分组成，短信**签名**需申请和审核，**签名**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建签名](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。发送国际/港澳台短信时，允许不携带签名。
- **申请模板并确认审核通过**
短信或语音正文内容**模板**需申请和审核，**模板**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建正文模板](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E6.9D.BF)。

### 配置 SDK

- **nuget：**
要使用 qcloudsms_csharp 功能，只需要在 .nuspec 文件中添加如下依赖：
```xml
<dependencies>
  <dependency id="qcloud.qcloudsms_csharp" version="0.1.5" />
</dependencies>
```
或参考 [nuget 官方网站](https://docs.microsoft.com/en-us/nuget/quickstart/use-a-package) 进行安装。

- **命令行**
 - Package Manager
```
Install-Package qcloud.qcloudsms_csharp -Version 0.1.5
```
 - .NET CLI
```
dotnet add package qcloud.qcloudsms_csharp --version 0.1.5
```
 - Paket CLI
```
paket add qcloud.qcloudsms_csharp --version 0.1.5
```

### 示例代码
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改。

- **准备必要参数**
```csharp
// 短信应用 SDK AppID
int appid = 122333333;
// 短信应用 SDK AppKey
string appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
// 需要发送短信的手机号码
string[] phoneNumbers = {"21212313123", "12345678902", "12345678903"};
// 短信模板 ID，需要在短信控制台中申请
int templateId = 7839; // NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
// 签名
string smsSign = "腾讯云"; // NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台申请
```

<a id="单发短信" ></a>
- **单发短信**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsSingleSender ssender = new SmsSingleSender(appid, appkey);
    var result = ssender.send(0, "86", phoneNumbers[0],
        "【腾讯云】您的验证码是: 5678", "", "");
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```

<a id="指定模板单发短信" ></a>
- **指定模板 ID 单发短信**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsSingleSender ssender = new SmsSingleSender(appid, appkey);
    var result = ssender.sendWithParam("86", phoneNumbers[0],
        templateId, new[]{ "5678" }, smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```


<a id="群发短信" ></a>
- **群发短信**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsMultiSender msender = new SmsMultiSender(appid, appkey);
    var result = msender.send(0, "86", phoneNumbers,
        "【腾讯云】您的验证码是: 5678", "", "");
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```


<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsMultiSender msender = new SmsMultiSender(appid, appkey);
    var sresult = msender.sendWithParam("86", phoneNumbers, templateId,
        new[]{"5678"}, smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    Console.WriteLine(sresult);
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```

<a id="拉取短信回执" ></a>
- **拉取短信回执以及回复**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    // Note: 短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387）开通权限
    int maxNum = 10;  // 单次拉取最大量
    SmsStatusPuller spuller = new SmsStatusPuller(appid, appkey);

    // 拉取短信回执
    var callbackResult = spuller.pullCallback(maxNum);
    Console.WriteLine(callbackResult);

    // 拉取回复，仅国内短信支持拉取回复状态
    var replyResult = spuller.pullReply(maxNum);
    Console.WriteLine(replyResult);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```

- **拉取单个手机短信状态**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    int beginTime = 1511125600;  // 开始时间（UNIX timestamp）
    int endTime = 1511841600;    // 结束时间（UNIX timestamp）
    int maxNum = 10;             // 单次拉取最大量
    SmsMobileStatusPuller mspuller = new SmsMobileStatusPuller(appid, appkey);

    // 拉取短信回执
    var callbackResult = mspuller.pullCallback("86",
        phoneNumbers[0], beginTime, endTime, maxNum);
    Console.WriteLine(callbackResult);

    // 拉取回复，国际/港澳台短信不支持回复功能
    var replyResult = mspuller.pullReply("86",
        phoneNumbers[0], beginTime, endTime, maxNum);
    Console.WriteLine(replyResult);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```

<a id="发送语音验证码" ></a>
- **发送语音验证码**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsVoiceVerifyCodeSender vvcsender = new SmsVoiceVerifyCodeSender(appid, appkey);
    var result = vvcsender.send("86", phoneNumbers[0], "09876", 2, "");
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```


<a id="发送语音通知" ></a>
- **发送语音通知**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    SmsVoicePromptSender vspsender = new SmsVoicePromptSender(appid, appkey);
    var result = vspsender.send("86", phoneNumbers[0], 2, "您的验证码是: 5678", 2, "");
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```
<a id="指定模板发送语音通知" ></a>
- **指定模板发送语音通知**
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;
using System;
try
{
    int templateId = 45221;
    string[] parameters = { "5678" };
    TtsVoiceSender tvsender = new TtsVoiceSender(appid, appkey);
    TtsVoiceSenderResult result = tvsender.send("86", phoneNumbers[0],
        templateId, parameters, 2, "");
    Console.WriteLine(result);
}
catch (JSONException e)
{
    Console.WriteLine(e);
}
catch (HTTPException e)
{
    Console.WriteLine(e);
}
catch (Exception e)
{
    Console.WriteLine(e);
}
```

- **发送国际/港澳台短信**
发送国际/港澳台短信与发送国内短信类似，只需替换相应的国家码或地区码。详细示例请参考：
 - [单发短信](#单发短信)
 - [指定模板单发短信](#指定模板单发短信)
 - [群发短信](#群发短信)
 - [指定模板群发短信](#指定模板群发短信)
 - [拉取短信回执](#拉取短信回执)



- **使用连接池**
多个线程可以共用一个连接池发送 API 请求，多线程并发单发短信示例如下：
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.httpclient;
using qcloudsms_csharp.json;
using System;
using System.Threading;
public class SmsTest
{
    public class SmsArg
    {
        public SmsSingleSender sender;
        public string nationCode;
        public string phoneNumber;
        public string msg;

        public SmsArg(SmsSingleSender sender, string nationCode, string phoneNumber, string msg)
        {
            this.sender = sender;
            this.nationCode = nationCode;
            this.phoneNumber = phoneNumber;
            this.msg = msg;
        }
    }

    public static void SendSms(object data)
    {
        SmsArg arg = (SmsArg)data;
        try
        {
            var result = arg.sender.send(0, arg.nationCode, arg.phoneNumber, arg.msg, "", "");
            Console.WriteLine("{0}, {1}", result, arg.phoneNumber);
        }
        catch (JSONException e)
        {
            Console.WriteLine(e);
        }
        catch (HTTPException e)
        {
            Console.WriteLine(e);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
    }

    static void Main(string[] args)
    {
        int appid = 122333333;
        string appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
        string[] phoneNumbers = {
                "21212313123", "12345678902", "12345678903",
                "21212313124", "12345678903", "12345678904",
                "21212313125", "12345678904", "12345678905",
                "21212313126", "12345678905", "12345678906",
                "21212313127", "12345678906", "12345678907",
            };

        // 创建一个连接池httpclient
        PoolingHTTPClient httpclient = new PoolingHTTPClient();

        // 创建SmsSingleSender时传入连接池http client
        SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);

        // 创建线程
        Thread[] threads = new Thread[phoneNumbers.Length];
        for (int i = 0; i < phoneNumbers.Length; i++)
        {
            threads[i] = new Thread(SmsTest.SendSms);
        }

        // 运行线程
        for (int i = 0; i < threads.Length; i++)
        {
            threads[i].Start(new SmsArg(ssender, "86", phoneNumbers[i], "您验证码是："));
        }

        // join线程
        for (int i = 0; i < threads.Length; i++)
        {
            threads[i].Join();
        }

        // 关闭连接池httpclient
        httpclient.close();
    }
}
```

- **使用自定义 HTTP client 实现**
如果需要使用自定义的 HTTP client 实现，只需实现 `qcloudsms_csharp.httpclient.IHTTPClient` 接口，并在构造 API 对象时传入自定义 HTTP client 即可，参考示例如下：
```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.httpclient;
// using myhttp_namespace;
public class CustomHTTPClient : IHTTPClient
{
    public HTTPResponse fetch(HTTPRequest request)
    {
        // 1. 创建自定义 HTTP request
        // MyHTTPrequest req = MyHTTPRequest.build(request)

        // 2. 创建自定义 httpclient
        // MyHTTPClient client = new MyHTTPClient();

        // 3. 使用自定义 httpclient 获取 HTTP 响应
        // MyHTTPResponse response = client.fetch(req);

        // 4. 转换 HTTP 响应到 HTTPResponse
        // HTTPResponse res = transformToHTTPResponse(response);

        // 5. 返回 HTTPResponse 实例
        // return res;
    }

    public void close()
    {
    }
}
// 创建自定义 httpclient
CustomHTTPClient httpclient = new CustomHTTPClient();
// 构造 API 对象时传入自定义 httpclient
SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);
```
