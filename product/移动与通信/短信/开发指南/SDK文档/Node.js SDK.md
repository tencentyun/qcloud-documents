## SDK 功能简介
目前腾讯云短信为客户提供**国内短信、语音短信**和**国际短信**服务，腾讯云短信 SDK 支持以下操作：

| 国内短信             | 语音短信               | 国际短信                 |
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
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/382/13297) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_js) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDKAppID 和 AppKey**
云短信应用 **SDKAppID** 和 **AppKey** 可在 [短信控制台](https://console.cloud.tencent.com/sms) 的应用信息里获取。如您尚未添加应用，请登录 [短信控制台](https://console.cloud.tencent.com/sms) 添加应用。
- **申请签名并确认审核通过**
一个完整的短信由短信**签名**和**短信正文内容**两部分组成，短信**签名**需申请和审核，**签名**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建签名](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。发送国际短信时，允许不携带签名。
- **申请模板并确认审核通过**
短信或语音正文内容**模板**需申请和审核，**模板**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建正文模板](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E6.9D.BF)。

### 配置 SDK

- **npm 配置：**
qcloudsms_js 采用 npm 进行安装，要使用 qcloudsms 功能，只需要执行：
```shell
npm install qcloudsms_js
```

- **手动配置：**
 1.手动下载或 clone 最新版本 qcloudsms_js 代码。
 2.把 qcloudsms_js 把代码放入项目目录。
 3.在项目里 require qcloudsms_js， 如： `var moduleName = require("path/to/qcloudsms_js")`。


### 示例代码

>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改。

- 准备必要参数和实例化 QcloudSms
```javascript
var QcloudSms = require("qcloudsms_js");
// 短信应用 SDK AppID
var appid = 1400009099;  // SDK AppID 以1400开头
// 短信应用 SDK AppKey
var appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
// 需要发送短信的手机号码
var phoneNumbers = ["21212313123", "12345678902", "12345678903"];
// 短信模板 ID，需要在短信控制台中申请
var templateId = 7839;  // NOTE: 这里的模板ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
// 签名
var smsSign = "腾讯云";  // NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台申请
// 实例化 QcloudSms
var qcloudsms = QcloudSms(appid, appkey);
// 设置请求回调处理, 这里只是演示，用户需要自定义相应处理回调
function callback(err, res, resData) {
    if (err) {
        console.log("err: ", err);
    } else {
        console.log("request data: ", res.req);
        console.log("response data: ", resData);
    }
}
```

<a id="单发短信" ></a>
- **单发短信**
```javascript
var smsType = 0; // Enum{0: 普通短信, 1: 营销短信}
var ssender = qcloudsms.SmsSingleSender();
ssender.send(smsType, 86, phoneNumbers[0],
  "【腾讯云】您的验证码是: 5678", "", "", callback);
```

<a id="指定模板单发短信" ></a>
- **指定模板 ID 单发短信**
```javascript
var ssender = qcloudsms.SmsSingleSender();
var params = ["5678"];
ssender.sendWithParam(86, phoneNumbers[0], templateId,
  params, smsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```

<a id="群发短信" ></a>
- **群发短信**
```
var smsType = 0;  // Enum{0: 普通短信, 1: 营销短信}
var msender = qcloudsms.SmsMultiSender();
msender.send(smsType, "86", phoneNumbers,
  "【腾讯云】您的验证码是: 5678", "", "", callback);
```
<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**
```javascript
var msender = qcloudsms.SmsMultiSender();
var params = ["5678"];
msender.sendWithParam("86", phoneNumbers, templateId,
  params, smsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```

<a id="拉取短信回执" ></a>
- **拉取短信回执以及回复**
```javascript
var maxNum = 10;  // 单次拉取最大量
var spuller = qcloudsms.SmsStatusPuller();
// 拉取短信回执
spuller.pullCallback(maxNum, callback);
// 拉取回复，国际短信不支持回复功能
spuller.pullReply(maxNum, callback);
```

- **拉取单个手机短信状态**
```javascript
var beginTime = 1511125600;  // 开始时间（UNIX timestamp）
var endTime = 1511841600;    // 结束时间（UNIX timestamp）
var maxNum = 10;             // 单次拉取最大量
var mspuller = qcloudsms.SmsMobileStatusPuller();
// 拉取短信回执
mspuller.pullCallback("86", phoneNumbers[0], beginTime, endTime, maxNum, callback);
// 拉取回复，国际短信不支持回复功能
mspuller.pullReply("86", phoneNumbers[0], beginTime, endTime, maxNum, callback);
```

<a id="发送语音验证码" ></a>
- **发送语音验证码**
```javascript
var cvsender = qcloudsms.CodeVoiceSender();
cvsender.send("86", phoneNumbers[0], "1234", 2, "", callback);
```


<a id="发送语音通知" ></a>
- **发送语音通知**
```javascript
var pvsender = qcloudsms.PromptVoiceSender();
pvsender.send("86", phoneNumbers[0], 2, "5678", 2, "", callback);
```
<a id="指定模板发送语音通知" ></a>
- **指定模板发送语音通知**
```javascript
var templateId = 12345;
var params = ["5678"];
var tvsender = qcloudsms.TtsVoiceSender();
tvsender.send("86", phoneNumbers[0], templateId, params, 2, "", callback);
```

- **发送国际短信**
发送国际短信与发送国内短信类似，只需替换相应的国家码或地区码。详细示例请参考：
 - [单发短信](#单发短信)
 - [指定模板单发短信](#指定模板单发短信)
 - [群发短信](#群发短信)
 - [指定模板群发短信](#指定模板群发短信)
 - [拉取短信回执](#拉取短信回执)

