## 腾讯短信服务
目前腾讯云短信为客户提供 **国内短信、国内语音** 和 **国际短信** 三大服务，腾讯云短信 SDK 支持以下操作：

### 国内短信
国内短信支持操作： [指定模板单发短信](#指定模板单发短信)、[指定模板群发短信](#指定模板群发短信)、[拉取短信回执和短信回复状态](#拉取短信回执)。

> 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)开通权限，量大客户可以使用此功能批量拉取，其他客户不建议使用。

### 国际短信
国际短信支持操作： [指定模板单发短信](#指定模板单发短信)、[指定模板群发短信](#指定模板群发短信)、[拉取短信回执和短信回复状态](#拉取短信回执)。

> 国际短信和国内短信使用同一接口，只需替换相应的国家码与手机号码，每次请求群发接口手机号码需全部为国内或者国际手机号码。

### 语音通知
语音通知支持操作：[发送语音验证码](#发送语音验证码)、[发送语音通知](#发送语音通知)、[上传语音文件](#上传语音文件)、[按语音文件 fid 发送语音通知](#按语音文件fid发送语音通知)、[指定模板发送语音通知](#指定模板发送语音通知)。

## 开发准备
### SDK 获取
短信 C# SDK 在 Github 中的下载地址：[短信 C# SDK](https://github.com/qcloudsms/qcloudsms_csharp)。

### 开发前准备
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

- **nuget：**
要使用 qcloudsms_csharp 功能，只需要在 .nuspec 文件中添加如下依赖：
```xml
<dependencies>
  <dependency id="qcloud.qcloudsms_csharp" version="0.1.5" />
</dependencies>
```

或者参考 [nuget 官方网站](https://docs.microsoft.com/en-us/nuget/quickstart/use-a-package) 进行安装。

### 命令行
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

### 相关资料
若您对接口存在疑问，可以查阅 [开发指南](https://cloud.tencent.com/document/product/382/13297) 、[API文档](https://qcloudsms.github.io/qcloudsms_java/) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

## 示例
- **准备必要参数**

```csharp
// 短信应用SDK AppID
int appid = 122333333;

// 短信应用SDK AppKey
string appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";

// 需要发送短信的手机号码
string[] phoneNumbers = {"21212313123", "12345678902", "12345678903"};

// 短信模板ID，需要在短信应用中申请
int templateId = 7839; // NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
//templateId 7839 对应的内容是"您的验证码是: {1}"
// 签名
string smsSign = "腾讯云"; // NOTE: 这里的签名只是示例，请使用真实的已申请的签名, 签名参数使用的是`签名内容`，而不是`签名ID`
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

> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


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

>群发一次请求最多支持200个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持(QQ:3012203387)。
>无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

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

> 语音验证码发送只需提供验证码数字，例如当msg=“5678”时，您收到的语音通知为“您的语音验证码是5678”，如需自定义内容，可以使用语音通知。

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
    var result = vspsender.send("86", phoneNumbers[0], 2, "您的验证码是: 54321", 2, "");
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

<a id="拉取短信回执" ></a>

- **拉取短信回执以及回复**

```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;

using System;

try
{
    // Note: 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)开通权限
    int maxNum = 10;  // 单次拉取最大量
    SmsStatusPuller spuller = new SmsStatusPuller(appid, appkey);

    // 拉取短信回执
    var callbackResult = spuller.pullCallback(maxNum);
    Console.WriteLine(callbackResult);

    // 拉取回复
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

> **注意：**
> 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;

using System;

try
{
    int beginTime = 1511125600;  // 开始时间(UNIX timestamp)
    int endTime = 1511841600;    // 结束时间(UNIX timestamp)
    int maxNum = 10;             // 单次拉取最大量
    SmsMobileStatusPuller mspuller = new SmsMobileStatusPuller(appid, appkey);

    // 拉取短信回执
    var callbackResult = mspuller.pullCallback("86",
        phoneNumbers[0], beginTime, endTime, maxNum);
    Console.WriteLine(callbackResult);

    // 拉取回复
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
> 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)开通权限，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送国际短信**

国际短信与国内短信发送类似, 发送国际短信只需替换相应国家码。


<a id="上传语音文件" ></a>

- **上传语音文件**

```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;

using System;
using System.IO;

try
{
    // Note: 语音文件大小上传限制400K字节
    String filePath = "/path/to/example.mp3";
    byte[] content = File.ReadAllBytes(filePath);
    VoiceFileUploader uploader = new VoiceFileUploader(appid, appkey);
    VoiceFileUploaderResult result = uploader.upload(content, VoiceFileUploader.ContentType.MP3);
    // 上传成功后，result里会带有语音文件的fid
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
> 语音文件上传功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。


<a id="按语音文件fid发送语音通知" ></a>

- **按语音文件 fid 发送语音通知**

```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.json;
using qcloudsms_csharp.httpclient;

using System;

try
{
    // Note: 这里fid来自`上传语音文件`接口返回的响应，要按语音
    //       文件fid发送语音通知，需要先上传语音文件获取fid
    String fid = "43847b4649ca38f37e596ec2281ce6a56a2a2a13.mp3";
    FileVoiceSender fvsender = new FileVoiceSender(appid, appkey);
    FileVoiceSenderResult result = fvsender.send("86",  phoneNumbers[0], fid, 2, "");
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
>按语音文件fid发送语音通知功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。


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
    string[] parameters = { "5678" };//数组具体的元素个数和模板中变量个数必须一致，例如事例中 templateId:5678 对应一个变量，参数数组中元素个数也必须是一个。
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

### 使用连接池

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
            threads[i].Start(new SmsArg(ssender, "86", phoneNumbers[i], "您验证码是：5678"));
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

### 使用自定义 HTTP client 实现

如果需要使用自定义的 HTTP client 实现，只需实现 `qcloudsms_csharp.httpclient.IHTTPClient` 接口，并在构造API 对象时传入自定义 HTTP client 即可，一个参考示例如下：

```csharp
using qcloudsms_csharp;
using qcloudsms_csharp.httpclient;

// using myhttp_namespace;

public class CustomHTTPClient : IHTTPClient
{
    public HTTPResponse fetch(HTTPRequest request)
    {
        // 1. 创建自定义HTTP request
        // MyHTTPrequest req = MyHTTPRequest.build(request)

        // 2. 创建自定义HTTP cleint
        // MyHTTPClient client = new MyHTTPClient();

        // 3. 使用自定义HTTP client获取HTTP响应
        // MyHTTPResponse response = client.fetch(req);

        // 4. 转换HTTP响应到HTTPResponse
        // HTTPResponse res = transformToHTTPResponse(response);

        // 5. 返回HTTPResponse实例
        // return res;
    }

    public void close()
    {
    }
}

// 创建自定义HTTP client
CustomHTTPClient httpclient = new CustomHTTPClient();
// 构造API对象时传入自定义HTTP client
SmsSingleSender ssender = new SmsSingleSender(appid, appkey, httpclient);
```

>  **注意：**
>  上面的这个示例代码只作参考，无法直接编译和运行，需要作相应修改。
