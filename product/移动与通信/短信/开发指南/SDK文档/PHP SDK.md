## 腾讯短信服务
目前腾讯云短信为客户提供**国内短信、国内语音**和**国际短信**三大服务，腾讯云短信 SDK 支持以下操作：
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

>? 国际短信和国内短信使用同一接口，只需替换相应的国家码与手机号码，每次请求群发接口手机号码需全部为国内或者国际手机号码。

### 语音短信
语音通知支持以下操作：
- [发送语音验证码](#发送语音验证码)
- [发送语音通知](#发送语音通知)
- [指定模板发送语音通知](#指定模板发送语音通知)

## 开发
### 相关资料
各个接口及其参数的详情介绍请参考 [API 文档](https://cloud.tencent.com/document/product/382/13297) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

### 获取 SDK 
短信 PHP SDK 在 Github 中的下载地址：[短信 PHP SDK](https://github.com/qcloudsms/qcloudsms_php)。

### 开发前准备
在开始开发云短信应用之前，需要准备以下信息：
- **申请 SDK AppID 和 App Key：**
在开始本教程之前，您需要先获取 SDK AppID 和 App Key，如您尚未申请，请到 [短信控制台](https://console.cloud.tencent.com/sms) 中添加应用。应用添加成功后您将获得 SDK AppID 以及 App Key。
- **申请签名：**
一个完整的短信由短信**签名**和**短信正文内容**两部分组成，短信 **签名** 需申请和审核，**签名** 可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参考 [创建签名](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。
- **申请模板：**
短信或语音正文内容**模板**需申请和审核，**模板**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参考 [创建正文模板](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E6.9D.BF)。

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
>? Composer 的使用可以参考 demo 目录下面的示例。

- **手动配置：**

 1. 手动下载或 clone 最新版本 qcloudsms_php 代码。
 2. 把 qcloudsms_php src 目录下的代码放入 Autoloading 目录。
 3. 引入 require qcloudsms_php src 目录下面的 index.php，即可使用，如把 qcloudsms 放在当前目录下，只需要执行以下命令：
```
require __DIR__ . "/qcloudsms_php/src/index.php";
```

## 示例
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改。

- **准备必要参数**

```php
// 短信应用 SDK AppID
$appid = 1400009099; // SDK AppID 以1400开头

// 短信应用 SDK AppKey
$appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad";

// 需要发送短信的手机号码
$phoneNumbers = ["21212313123", "12345678902", "12345678903"];

// 短信模板 ID，需要在短信控制台中申请
$templateId = 7839;  // NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请

$smsSign = "腾讯云"; // NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台申请
```

<a id="单发短信" ></a>
- **单发短信**

```php
use Qcloud\Sms\SmsSingleSender;

try {
    $ssender = new SmsSingleSender($appid, $appkey);
    $result = $ssender->send(0, "86", $phoneNumbers[0],
        "【腾讯云】您的验证码是: 5678", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

>?如需发送海外短信，同样可以使用此接口，只需将国家码 `86` 改写成对应国家码号。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

<a id="指定模板单发短信" ></a>
- **指定模板 ID 单发短信**

```php
use Qcloud\Sms\SmsSingleSender;

try {
    $ssender = new SmsSingleSender($appid, $appkey);
    $params = ["5678"];
    $result = $ssender->sendWithParam("86", $phoneNumbers[0], $templateId,
        $params, $smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

>?如需发送海外短信，同样可以使用此接口，只需将国家码 `86` 改写成对应国家码号。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="群发短信" ></a>
- **群发短信**

```php
use Qcloud\Sms\SmsMultiSender;

try {
    $msender = new SmsMultiSender($appid, $appkey);
    $result = $msender->send(0, "86", $phoneNumbers,
        "【腾讯云】您的验证码是: 5678", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

>?一次群发请求最多支持200个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。
>无论单发/群发短信还是指定模板 ID 单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**

```php
use Qcloud\Sms\SmsMultiSender;

try {
    $msender = new SmsMultiSender($appid, $appkey);
    $params = ["5678"];
    $result = $msender->sendWithParam("86", $phoneNumbers,
        $templateId, $params, $smsSign, "", "");  // 签名参数未提供或者为空时，会使用默认签名发送短信
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

>? 群发一次请求最多支持200个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：3012203387）。
> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="发送语音验证码"></a>
- **发送语音验证码**

```php
use Qcloud\Sms\SmsVoiceVerifyCodeSender;

try {
    $vvcsender = new SmsVoiceVerifyCodeSender($appid, $appkey);
    $result = $vvcsender->send("86", $phoneNumbers[0], "5678");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>?语音验证码发送只需提供验证码数字，如需自定义内容，可以使用语音通知。
>例如，当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是五六七八。”。


<a id="发送语音通知" ></a>
- **发送语音通知**

```php
use Qcloud\Sms\SmsVoicePromptSender;

try {
    $vpsender = new SmsVoicePromptSender($appid, $appkey);
    $result = $vpsender->send("86", $phoneNumbers[0], 2, "5678");
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>?发送语音通知时，数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。
例如，当 msg=“您的语音验证码是5678。” 时，您收到的语音通知为“您的语音验证码是五千六百七十八。”。当 msg=“您的语音验证码是5,6,7,8。”时，您收到的语音通知为“您的语音验证码是五六七八。”。

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

>?短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```php
use Qcloud\Sms\SmsMobileStatusPuller;

try {
    $beginTime = 1511125600;  // 开始时间（UNIX timestamp）
    $endTime = 1511841600;    // 结束时间（UNIX timestamp）
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

>?短信拉取功能需要联系腾讯云短信技术支持（QQ：3012203387），量大客户可以使用此功能批量拉取，其他客户不建议使用。


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
    // 上传成功后，$rsp 里会带有语音文件的 fid
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>?语音文件上传功能需要联系腾讯云短信技术支持（QQ：3012203387）才能开通。


<a id="按语音文件fid发送语音通知" ></a>
- **按语音文件 fid 发送语音通知**

```php
use Qcloud\Sms\FileVoiceSender;

try {
    // Note：这里 $fid 来自`上传语音文件`接口返回的响应，如果需要按语音文件fid发送语音通知，需先上传语音文件获取 $fid
    $fid = "73844bb649ca38f37e596ec2781ce6a56a2a3a1b.mp3";
    $fvsender = new FileVoiceSender($appid, $appkey);
    $result = $fvsender->send("86", $phoneNumbers[0], $fid);
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```

>?按语音文件 fid 发送语音通知功能需要联系腾讯云短信技术支持（QQ：3012203387）才能开通。

<a id="指定模板发送语音通知" ></a>

- **指定模板发送语音通知**

```php
use Qcloud\Sms\TtsVoiceSender;

try {
    $templateId = 1013;
    $params = ["54321"];
    $tvsender = new TtsVoiceSender($appid, $appkey);
    $result = $tvsender->send("86", $phoneNumbers[0], $templateId, $params);
    $rsp = json_decode($result);
    echo $result;
} catch (\Exception $e) {
    echo var_dump($e);
}
```
>?指定模板 ID 发送语音通知时，数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。
例如，当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是五千六百七十八。”。当 msg=“5,6,7,8”时，您收到的语音通知为“您的语音验证码是五六七八。”。
