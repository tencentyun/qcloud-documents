## 开发准备
### SDK 获取
短信 PHP SDK 在 Github 中的下载地址：[短信 PHP SDK](https://github.com/qcloudsms/qcloudsms_php)。

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

- **Composer 配置：**
qcloudsms_php 采用 composer 进行安装，要使用 qcloudsms 功能，只需要在 composer.json 中添加如下依赖：
```json
{
  "require": {
    "qcloudsms/qcloudsms_php": "0.1.*"
  }
}
```

- **手动配置：**

 1.手动下载或 clone 最新版本 qcloudsms_php 代码。
 2.把 qcloudsms_php src 目录下的代码放入 Autoloading 目录。

## 快速入门

若您对接口存在疑问，可以查阅 [API 文档](https://cloud.tencent.com/document/product/382/13297)。

- **准备必要参数**
```php
$appid = 122333333;
$appkey = "111111111112132312xx";
$phoneNumber1 = "21212313123";
$phoneNumber2 = "12345678902";
$phoneNumber3 = "12345678903";
$templId = 7839;
```

- **单发短信**
```php
use Qcloud\Sms\SmsSingleSender;
try {
    $sender = new SmsSingleSender($appid, $appkey);
    $result = $sender->send(0, "86", $phoneNumber2,
        "测试短信，普通单发，深圳，小明，上学。", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **注意：**
> - 发送短信没有指定模板ID时，发送的内容需要与已审核通过的模板内容相匹配，才可能下发成功，否则返回失败。
> - 如需发送国际短信，同样可以使用此接口，只需将国家码"86"改写成对应国家码号。

- **指定模板 ID 单发短信**
```php
use Qcloud\Sms\SmsSingleSender;
try {
    $sender = new SmsSingleSender($appid, $appkey);
    $params = ["指定模板单发", "深圳", "小明"];
    // 假设模板内容为：测试短信，{1}，{2}，{3}，上学。
    $result = $sender->sendWithParam("86", $phoneNumber2, $templId,
        $params, "", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **注意：**
> 无论单发短信还是指定模板 ID 单发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

- **群发短信**
```php
use Qcloud\Sms\SmsMultiSender;
try {
    $phoneNumbers = [$phoneNumber1, $phoneNumber2, $phoneNumber3];
    $sender = new SmsMultiSender($appid, $appkey);
    $result = $sender->send(0, "86", $phoneNumbers,
        "测试短信，普通群发，深圳，小明，上学。", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

- **指定模板 ID 群发**
```php
use Qcloud\Sms\SmsMultiSender;
try {
    $phoneNumbers = [$phoneNumber1, $phoneNumber2, $phoneNumber3];
    $sender = new SmsMultiSender($appid, $appkey);
    $params = ["指定模板群发", "深圳", "小明"];
    $result = $sender->sendWithParam("86", $phoneNumbers,
        $templId, $params, "", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **注意：**
> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。

- **发送语音验证码**
```php
use Qcloud\Sms\SmsVoiceVerifyCodeSender;
try {
    $sender = new SmsVoiceVerifyCodeSender($appid, $appkey);
    $result = $sender->send("86", $phoneNumber1, "1234", 2, "");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```
> **注意：**
>  语音验证码发送只需提供验证码数字，例如在 msg=“123”，您收到的语音通知为“您的语音验证码是1 2 3”，如需自定义内容，可以使用语音通知。

- **发送语音通知**
```php
use Qcloud\Sms\SmsVoicePromptSender;
try {
    $sender = new SmsVoicePromptSender($appid, $appkey);
    $result = $sender->send("86", $phoneNumber1, 2, "1234", "");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

- **拉取短信回执以及回复**
```php
use Qcloud\Sms\SmsStatusPuller;
try {
    $puller = new SmsStatusPuller($appid, $appkey);

    // 拉取短信回执
    $callbackResult = $puller->pullCallback(10);
    $callbackRsp = json_decode($callbackResult);
    echo $callbackResult;

    // 拉取回复
    $replyResult = $puller->pullReply(10);
    $replyRsp = json_decode($replyResult);
    echo $replyResult;
} catch (\Exception $e) {
    echo var_dump($e);
}
```
>**注意：**
>短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送海外短信**
海外短信与国内短信发送类似。
