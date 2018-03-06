## 开发准备
### SDK 获取
短信 Node.js SDK 在 Github 中的下载地址：[短信 Node.js SDK](https://github.com/qcloudsms/qcloudsms_js)。

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

- **npm 配置：**
qcloudsms_js 采用 npm 进行安装，要使用 qcloudsms 功能，只需要执行：
```shell
npm install qcloudsms_js
```

- **手动配置：**

 1.手动下载或 clone 最新版本 qcloudsms_js 代码。
 2.把 qcloudsms_js 把代码放入项目目录。
 3.在项目里 require qcloudsms_js， 如： `var moduleName = require("path/to/qcloudsms_js")`。

## 快速入门

若您对接口存在疑问，可以查阅 [API 文档](https://cloud.tencent.com/document/product/382/13297)。

- **准备必要参数和实例化 QcloudSms**
```javascript
var QcloudSms = require("qcloudsms_js");
var appid = 122333333;
var appkey = "111111111112132312xx";
var phoneNumbers = ["21212313123", "12345678902", "12345678903"];
var templId = 7839;
var qcloudsms = QcloudSms(appid, appkey);
// 请求回调处理, 这里只是演示，用户需要自定义相应处理回调
function callback(err, res, resData) {
    if (err)
        console.log("err: ", err);
    else
        console.log("response data: ", resData);
}
```

- **单发短信**
```javascript
var ssender = qcloudsms.SmsSingleSender();
ssender.send(0, 86, phoneNumbers[0],
  "测试短信，普通单发，深圳，小明，上学。", "", "", callback);
```
> **注意：**
> 发送短信没有指定模板ID时，发送的内容需要与已审核通过的模板内容相匹配，才可能下发成功，否则返回失败。
> 如需发送海外短信，同样可以使用此接口，只需将国家码"86"改写成对应国家码号。

- **指定模板 ID 单发短信**
```javascript
var ssender = qcloudsms.SmsSingleSender();
var params = ["指定模板单发", "深圳", "小明"];
ssender.sendWithParam(86, phoneNumbers[0], templId,
  params, "", "", "", callback);
```
> **注意：**
> 无论单发短信还是指定模板 ID 单发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

- **群发短信**
```javascript
var msender = qcloudsms.SmsMultiSender();
msender.send(0, "86", phoneNumbers,
  "测试短信，普通群发，深圳，小明，上学。", "", "", callback);
```

- **指定模板 ID 群发**
```javascript
var msender = qcloudsms.SmsMultiSender();
var params = ["指定模板群发", "深圳", "小明"];
msender.sendWithParam("86", phoneNumbers, templId,
  params, "", "", "", callback);
```
> **注意：**
> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。

- **发送语音验证码**
```javascript
var vpsender = qcloudsms.SmsVoicePromptSender();
vpsender.send("86", phoneNumbers[0], 2, "1234", 2, "", callback);
```
> **注意：**
> 语音验证码发送只需提供验证码数字，例如在 msg=“123”，您收到的语音通知为“您的语音验证码是1 2 3”，如需自定义内容，可以使用语音通知。

- **发送语音通知**
```javascript
var vvcsender = qcloudsms.SmsVoiceVerifyCodeSender();
vvcsender.send("86", phoneNumbers[0], "1234", 2, "", callback);
```

- **拉取短信回执以及回复**
```javascript
var spuller = qcloudsms.SmsStatusPuller();
// 拉取短信回执
spuller.pullCallback(10, callback);
// 拉取回复
spuller.pullReply(10, callback);
```
>**注意：**
>短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**
```javascript
var mspuller = qcloudsms.SmsMobileStatusPuller();
// 拉取短信回执
mspuller.pullCallback("86", phoneNumbers[0], 1511125600, 1511841600, 10, callback);
// 拉取回复
mspuller.pullReply("86", phoneNumbers[0], 1511125600, 1511841600, 10, callback);
```

- **发送海外短信**
海外短信与国内短信发送类似。
