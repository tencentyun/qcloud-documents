
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


 ### 相关资料
 若您对接口存在疑问，可以查阅 [开发指南](https://cloud.tencent.com/document/product/382/13297) 、[API文档](https://qcloudsms.github.io/qcloudsms_java/) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。


## 示例

- **准备必要参数和实例化 QcloudSms**

```javascript
var QcloudSms = require("qcloudsms_js");

// 短信应用SDK AppID
var appid = 1400009099;  // SDK AppID是1400开头

// 短信应用SDK AppKey
var appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";

// 需要发送短信的手机号码
var phoneNumbers = ["21212313123", "12345678902", "12345678903"];

// 短信模板ID，需要在短信应用中申请
var templateId = 7839;  // NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
//templateId 7839 对应的内容是"您的验证码是: {1}"
// 签名
var smsSign = "腾讯云";  // NOTE: 这里的签名只是示例，请使用真实的已申请的签名, 签名参数使用的是`签名内容`，而不是`签名ID`

// 实例化QcloudSms
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

<a id="指定模板单发短信" ></a>

- **指定模板 ID 单发短信**

```javascript
var ssender = qcloudsms.SmsSingleSender();
var params = ["5678"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
ssender.sendWithParam(86, phoneNumbers[0], templateId,
  params, SmsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```
> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="指定模板群发短信" ></a>

- **指定模板 ID 群发短信**

```javascript
var msender = qcloudsms.SmsMultiSender();
var params = ["5678"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
msender.sendWithParam("86", phoneNumbers, templateId,
  params, smsSign, "", "", callback);  // 签名参数未提供或者为空时，会使用默认签名发送短信
```
> **注意：**
> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。


<a id="发送语音验证码" ></a>

- **发送语音验证码**

```javascript
var cvsender = qcloudsms.CodeVoiceSender();
cvsender.send("86", phoneNumbers[0], "1234", 2, "", callback);
```
> 语音验证码发送只需提供验证码数字，例如当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是 5 6 7 8”，如需自定义内容，可以使用语音通知。

<a id="发送语音通知" ></a>

- **发送语音通知**

```javascript
var pvsender = qcloudsms.PromptVoiceSender();
pvsender.send("86", phoneNumbers[0], 2, "5678", 2, "", callback);
```

<a id="拉取短信回执" ></a>

- **拉取短信回执以及回复**

```javascript
var maxNum = 10;  // 单次拉取最大量
var spuller = qcloudsms.SmsStatusPuller();
// 拉取短信回执
spuller.pullCallback(maxNum, callback);
// 拉取回复
spuller.pullReply(maxNum, callback);
```
>短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```javascript
var beginTime = 1511125600;  // 开始时间(UNIX timestamp)
var endTime = 1511841600;    // 结束时间(UNIX timestamp)
var maxNum = 10;             // 单次拉取最大量
var mspuller = qcloudsms.SmsMobileStatusPuller();
// 拉取短信回执
mspuller.pullCallback("86", phoneNumbers[0], beginTime, endTime, maxNum, callback);
// 拉取回复
mspuller.pullReply("86", phoneNumbers[0], beginTime, endTime, maxNum, callback);
```
>短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送国际短信**
国际短信与国内短信发送类似, 发送国际短信只需替换相应国家码。


<a id="上传语音文件" ></a>

- **上传语音文件**

```javascript
var fs = require("fs");

// Note: 语音文件大小上传限制400K字节
var filePath = "/home/pf/data/download/scripts/voice/4162.mp3";
var fileContent = fs.readFileSync(filePath);
var uploader = qcloudsms.VoiceFileUploader();
// 上传成功后，callback里会返回语音文件的fid
uploader.upload(fileContent, "mp3", callback);
```
>语音文件上传功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。


<a id="按语音文件fid发送语音通知" ></a>

- **按语音文件 fid 发送语音通知**

```javascript
// Note：这里fid来自`上传语音文件`接口返回的响应，要按语音
//    文件fid发送语音通知，需要先上传语音文件获取fid
var fid = "c799d10a43ec109f02f2288ca3c85b79e7700c98.mp3";
var fvsender = qcloudsms.FileVoiceSender();
fvsender.send("86", phoneNumbers[0], fid, 2, "", callback);
```
>按语音文件 fid 发送语音通知功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。



<a id="指定模板发送语音通知" ></a>

- **指定模板发送语音通知**

```javascript
var templateId = 12345;
var params = ["5678"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
var tvsender = qcloudsms.TtsVoiceSender();
tvsender.send("86", phoneNumbers[0], templateId, params, 2, "", callback);
```
