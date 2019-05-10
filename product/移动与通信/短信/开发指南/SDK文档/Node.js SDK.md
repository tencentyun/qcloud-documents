
## SDK 功能简介
目前腾讯云短信为客户提供**国内短信、国际短信**和**国内语音**三大服务，腾讯云短信 SDK 支持以下操作：

### 国内短信
国内短信支持以下操作：
- [单发短信](#单发短信)
- [指定模板单发短信](#指定模板单发短信)
- [群发短信](#群发短信)
- [指定模板群发短信](#指定模板群发短信)
- [拉取短信回执和短信回复状态](#拉取短信回执)

>? 短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387）开通权限，量大客户可以使用此功能批量拉取，其他客户不建议使用。

### 国际短信
国际短信支持以下操作：
- [单发短信](#单发短信)
- [指定模板单发短信](#指定模板单发短信)
- [群发短信](#群发短信)
- [指定模板群发短信](#指定模板群发短信)
- [拉取短信回执](#拉取短信回执)

>? 国际短信和国内短信使用同一接口，只需替换相应的国家码与手机号码，每次请求群发接口手机号码需全部为国内或者国际手机号码。

### 国内语音
语音通知支持以下操作：
- [发送语音验证码](#发送语音验证码)
- [发送语音通知](#发送语音通知)
- [指定模板发送语音通知](#指定模板发送语音通知)

## SDK 使用指南
### 相关资料
各个接口及其参数的详情介绍请参考 [API 指南](https://cloud.tencent.com/document/product/382/13297) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_js) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

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

- **准备必要参数和实例化 QcloudSms**

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

>?如需发送海外短信，同样可以使用此接口，只需将国家码 `86` 改写成对应国家码号。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

<a id="指定模板单发短信" ></a>
- **指定模板 ID 单发短信**

```javascript
var ssender = qcloudsms.SmsSingleSender();
var params = ["5678"];
ssender.sendWithParam(86, phoneNumbers[0], templateId,
  params, smsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```

>?如需发送海外短信，同样可以使用此接口，只需将国家码 `86` 改写成对应国家码号。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

<a id="群发短信" ></a>
- **群发短信**

```
var smsType = 0;  // Enum{0: 普通短信, 1: 营销短信}
var msender = qcloudsms.SmsMultiSender();
msender.send(smsType, "86", phoneNumbers,
  "【腾讯云】您的验证码是: 5678", "", "", callback);
```

>?一次群发请求最多支持200个号码，如对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**

```javascript
var msender = qcloudsms.SmsMultiSender();
var params = ["5678"];
msender.sendWithParam("86", phoneNumbers, templateId,
  params, smsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```

>?一次群发请求最多支持200个号码，如对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="发送语音验证码" ></a>
- **发送语音验证码**

```javascript
var cvsender = qcloudsms.CodeVoiceSender();
cvsender.send("86", phoneNumbers[0], "1234", 2, "", callback);
```

>?语音验证码发送只需提供验证码数字，如需自定义内容，可以使用语音通知。
>例如，当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是五六七八。”。


<a id="发送语音通知" ></a>
- **发送语音通知**

```javascript
var pvsender = qcloudsms.PromptVoiceSender();
pvsender.send("86", phoneNumbers[0], 2, "5678", 2, "", callback);
```

>?发送语音通知时，数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。
例如，当 msg=“您的语音验证码是5678。” 时，您收到的语音通知为“您的语音验证码是五千六百七十八。”。当 msg=“您的语音验证码是5,6,7,8。”时，您收到的语音通知为“您的语音验证码是五六七八。”。

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

>?短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

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

>?短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送国际短信**
国际短信与国内短信发送类似，发送国际短信只需替换相应国家码。


<a id="指定模板发送语音通知" ></a>
- **指定模板发送语音通知**

```javascript
var templateId = 12345;
var params = ["5678"];
var tvsender = qcloudsms.TtsVoiceSender();
tvsender.send("86", phoneNumbers[0], templateId, params, 2, "", callback);
```

>?指定模板 ID 发送语音通知时，数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。
例如，当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是五千六百七十八。”。当 msg=“5,6,7,8”时，您收到的语音通知为“您的语音验证码是五六七八。”。
