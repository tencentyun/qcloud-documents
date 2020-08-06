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
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/1128/37530) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_js) 和 [错误码](https://cloud.tencent.com/document/product/1128/37531)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDK AppID 和 App Key**
语音消息应用 **SDK AppID** 和 **App Key** 可在 [语音消息控制台](https://console.cloud.tencent.com/vms) 的应用信息里获取。如您尚未添加应用，请登录语音消息控制台 [创建应用](https://cloud.tencent.com/document/product/1128/37461)。
- **申请模板并确认审核通过**
语音正文内容**模板**需申请和审核，**模板**可在 [语音消息控制台](https://console.cloud.tencent.com/vms) 的【应用管理】>【语音模板】页面申请，详细申请操作请参见 [配置语音模板](https://cloud.tencent.com/document/product/1128/37517)。


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
// 语音消息应用 SDK AppID
var appid = 1400009099;  // SDK AppID 以1400开头
// 语音消息应用 App Key
var appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";
// 需要发送语音消息的手机号码
var phoneNumbers = ["21212313123", "12345678902", "12345678903"];
// 语音模板 ID，需要在语音消息控制台中申请
var templateId = 7839;  // NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在语音消息控制台中申请
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

<a id="发送语音验证码" ></a>
- **发送语音验证码**
```javascript
var cvsender = qcloudsms.CodeVoiceSender();
cvsender.send("86", phoneNumbers[0], "1234", 2, "", callback);
```


<a id="指定模板发送语音通知" ></a>
- **指定模板发送语音通知**
```javascript
var templateId = 12345;
var params = ["5678"];
var tvsender = qcloudsms.TtsVoiceSender();
tvsender.send("86", phoneNumbers[0], templateId, params, 2, "", callback);
```
