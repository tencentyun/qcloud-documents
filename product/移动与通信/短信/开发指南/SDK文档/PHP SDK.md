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


## 开发
### SDK 获取
短信 PHP SDK 在 Github 中的下载地址：[短信 PHP SDK](https://github.com/qcloudsms/qcloudsms_php)。

### 开发准备
**1. 申请 SDK AppID 以及 App Key：**
在开始本教程之前，您需要先获取 SDK AppID 和 App Key，如您尚未申请，请到 [短信控制台](https://console.cloud.tencent.com/sms) 中添加应用。应用添加成功后您将获得 SDK AppID 以及 App Key。

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
> Composer 的使用可以参考 demo 目录下面的示例。

- **手动配置：**

 1.手动下载或 clone 最新版本 qcloudsms_php 代码。
 2.把 qcloudsms_php src 目录下的代码放入 Autoloading 目录。
 3.require qcloudsms_php src 目录下面的 index.php，即可使用，如把 qcloudsms 放在当前目录下，只需要:
```
require __DIR__ . "/qcloudsms_php/src/index.php";
```

## 示例

若您对接口存在疑问，可以查阅 [API 文档](https://cloud.tencent.com/document/product/382/13297)、[SDK文档](https://qcloudsms.github.io/qcloudsms_php/) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

- **准备必要参数**

```php
/ 短信应用SDK AppID
$appid = 1400009099; // 1400开头

// 短信应用SDK AppKey
$appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";

// 需要发送短信的手机号码
$phoneNumbers = ["21212313123", "12345678902", "12345678903"];
//templateId7839对应的内容是"您的验证码是: {1}"
// 短信模板ID，需要在短信应用中申请
$templateId = 7839;  // NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请

$smsSign = "腾讯云"; // NOTE: 这里的签名只是示例，请使用真实的已申请的签名，签名参数使用的是`签名内容`，而不是`签名ID`
```


<a id="指定模板单发短信" ></a>

- **指定模板 ID 单发短信**

```php
use Qcloud\Sms\SmsSingleSender;

try {
    $ssender = new SmsSingleSender($appid, $appkey);
    $params = ["5678"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中 templateId:5678对应一个变量，参数数组中元素个数也必须是一个
    $result = $ssender->sendWithParam("86", $phoneNumbers[0], $templateId,
        $params, $smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="指定模板群发短信" ></a>

- **指定模板 ID 群发短信**

```php
use Qcloud\Sms\SmsMultiSender;

try {
    $msender = new SmsMultiSender($appid, $appkey);
    $params = ["5678"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中 templateId:5678对应一个变量，参数数组中元素个数也必须是一个
    $result = $msender->sendWithParam("86", $phoneNumbers,
        $templateId, $params, $smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持(QQ:3012203387)。
> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="发送语音验证码"></a>

- **发送语音验证码**

```php
use Qcloud\Sms\SmsVoiceVerifyCodeSender;

try {
    $vvcsender = new SmsVoiceVerifyCodeSender($appid, $appkey);
    $result = $vvcsender->send("86", $phoneNumbers[0], "5678", 2, "");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>  语音验证码发送只需提供验证码数字，例如在 msg=“5678”，您收到的语音通知为“您的语音验证码是5 6 7 8”，如需自定义内容，可以使用语音通知。

<a id="发送语音通知" ></a>

- **发送语音通知**

```php
use Qcloud\Sms\SmsVoicePromptSender;

try {
    $vpsender = new SmsVoicePromptSender($appid, $appkey);
    $result = $vpsender->send("86", $phoneNumbers[0], 2, "5678", "");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

<a id="拉取短信回执" ></a>

- **拉取短信回执以及回复**

```php
use Qcloud\Sms\SmsStatusPuller;

try {
    $sspuller = new SmsStatusPuller($appid, $appkey);

    // 拉取短信回执
    $callbackResult = $spuller->pullCallback(10);
    $callbackRsp = json_decode($callbackResult);
    echo $callbackResult;

    // 拉取回复
    $replyResult = $spuller->pullReply(10);
    $replyRsp = json_decode($replyResult);
    echo $replyResult;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```php
use Qcloud\Sms\SmsMobileStatusPuller;

try {
    $beginTime = 1511125600;  // 开始时间(UNIX timestamp)
    $endTime = 1511841600;    // 结束时间(UNIX timestamp)
    $maxNum = 10;             // 单次拉取最大量
    $mspuller = new SmsMobileStatusPuller($appid, $appkey);

    // 拉取短信回执
    $callbackResult = $mspuller->pullCallback("86", $phoneNumbers[0],
        $beginTime, $endTime, $maxNum);
    $callbackRsp = json_decode($callbackResult);
    echo $callbackResult;

    // 拉取回复
    $replyResult = $mspuller->pullReply("86", $phoneNumbers[0],
        $beginTime, $endTime, $maxNum);
    $replyRsp = json_decode($replyResult);
    echo $replyResult;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。


- **发送国际短信**
国际短信与国内短信发送类似,发送国际短信只需替换相应国家码。

<a id="上传语音文件" ></a>

- **上传语音文件**

```php
use Qcloud\Sms\VoiceFileUploader;

try {
    // Note: 语音文件大小上传限制400K字节
    $filepath = "path/to/example.mp3";
    $fileContent = file_get_contents($filepath);
    if ($fileContent == false) {
        throw new \Exception("can not read file " . $filepath);
    }

    $contentType = VoiceFileUploader::MP3;
    $uploader = new VoiceFileUploader($appid, $appkey);
    $result = $uploader->upload($fileContent, $contentType);
    // 上传成功后，$rsp里会带有语音文件的fid
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>语音文件上传功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。


<a id="按语音文件fid发送语音通知" ></a>

- **按语音文件 fid 发送语音通知**

```php
use Qcloud\Sms\FileVoiceSender;

try {
    // Note：这里$fid来自`上传语音文件`接口返回的响应，要按语音
    //    文件fid发送语音通知，需要先上传语音文件获取$fid
    $fid = "73844bb649ca38f37e596ec2781ce6a56a2a3a1b.mp3";
    $fvsender = new FileVoiceSender($appid, $appkey);
    $result = $fvsender->send("86", $phoneNumbers[0], $fid);
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>按语音文件 fid 发送语音通知功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。

<a id="指定模板发送语音通知" ></a>

- **指定模板发送语音通知**

```php
use Qcloud\Sms\TtsVoiceSender;

try {
    $templateId = 1013;
    $params = ["54321"];//数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:54321对应一个变量，参数数组中元素个数也必须是一个
    $tvsender = new TtsVoiceSender($appid, $appkey);
    $result = $tvsender->send("86", $phoneNumbers[0], $templateId, $params);
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```
