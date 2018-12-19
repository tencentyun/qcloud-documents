## Preparations for Development
### Obtaining SDK
Download link for SMS PHP SDK in Github: [SMS PHP SDK](https://github.com/qcloudsms/qcloudsms_php).

### Preparations for Development
**1. Apply for SDK AppID and App Key:**
Before getting started, you need to obtain SDK AppID and App Key. If you have not done so, log in to the [SMS Console](https://console.cloud.tencent.com/sms) and add a project. After this, you can get an SDK AppID and an App Key.
>**Note:**
> SDK AppID begins with 14xxxxx.

**2. Apply for a signature:**
You must add a signature when sending an SMS message. You can apply for an SMS signature in the [SMS Console](https://console.cloud.tencent.com/sms). For more information, please see [here](https://intl.cloud.tencent.com/document/product/382/18053#create-signatureD).

**3. Apply for a template:**
The content of the SMS message you sent must be approved. You can apply for an SMS template in the SMS [Console](https://console.cloud.tencent.com/sms). For more information, please see [here](https://intl.cloud.tencent.com/document/product/382/18053#create-body-template).

You can proceed with code development after completing the above three steps.

### Configuring SDK

- **Composer configuration:**
"qcloudsms_php" is installed by using composer. To use Tencent Cloud SMS, you just need to add the following dependencies in composer.json.
```json
{
  "require": {
    "qcloudsms/qcloudsms_php": "0.1.*"
  }
}
```

- **Manual configuration:**

 1. Manually download or clone the latest version of qcloudsms_php code.
 2. Place the code under the directory qcloudsms_php src into the directory Autoloading.

## Getting Started

For any questions about APIs, see [API documentation](/document/product/382/13297).

- **Prepare necessary parameters**
```php
$appid = 122333333;
$appkey = "111111111112132312xx";
$phoneNumber1 = "21212313123";
$phoneNumber2 = "12345678902";
$phoneNumber3 = "12345678903";
$templId = 7839;
```

- **Send single SMS messages**
```php
use Qcloud\Sms\SmsSingleSender;
try {
    $sender = new SmsSingleSender($appid, $appkey);
    $result = $sender->send(0, "86", $phoneNumber2,
        "Test SMS message, common single SMS message, Shenzhen, Xiao Ming, go to school.", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **Note:**
> - If the template ID is not specified when you send an SMS message, the content can be delivered successfully only if it matches the approved template content. Otherwise a failure message is returned.
> - You can also use this API to send international SMS messages by changing the country code "86" to a corresponding country code.

- **Send single SMS messages with specified template ID**
```php
use Qcloud\Sms\SmsSingleSender;
try {
    $sender = new SmsSingleSender($appid, $appkey);
    $params = ["Send single SMS messages with a specified template ID", "Shenzhen", "Xiao Ming"];
    // Assume that the template content is: Test SMS message, {1}, {2}, {3}, go to school.
    $result = $sender->sendWithParam("86", $phoneNumber2, $templId,
        $params, "", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **Note:**
> You must apply for a template via the console and the template must be reviewed and approved before you can send single SMS messages successfully with or without specified template ID. Otherwise a failure message is returned.

- **Send bulk SMS messages**
```php
use Qcloud\Sms\SmsMultiSender;
try {
    $phoneNumbers = [$phoneNumber1, $phoneNumber2, $phoneNumber3];
    $sender = new SmsMultiSender($appid, $appkey);
    $result = $sender->send(0, "86", $phoneNumbers,
        "Test SMS message, common bulk SMS message, Shenzhen, Xiao Ming, go to school.", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```

- **Send bulk messages with a specified template ID**
```php
use Qcloud\Sms\SmsMultiSender;
try {
    $phoneNumbers = [$phoneNumber1, $phoneNumber2, $phoneNumber3];
    $sender = new SmsMultiSender($appid, $appkey);
    $params = ["Send bulk SMS messages with a specified template ID", "Shenzhen", "Xiao Ming"];
    $result = $sender->sendWithParam("86", $phoneNumbers,
        $templId, $params, "", "", "");
    $rsp = json_decode($result);
    echo $result;
} catch(\Exception $e) {
    echo var_dump($e);
}
```
> **Note:**
> A maximum of 200 phone numbers are supported for a request for sending bulk SMS messages. To send messages to more numbers, contact Tencent Cloud SMS technical support (QQ: 3012203387).

- **Send voice verification code**
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
> **Note:**
> Only numbers are required when you send verification code. For example, if the messages is 123, the voice notification you will receive is: "Your voice verification code is 1 2 3". To customize content, use voice notification.

- **Send voice notification**
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

- **Pull SMS report and reply**
```php
use Qcloud\Sms\SmsStatusPuller;
try {
    $puller = new SmsStatusPuller($appid, $appkey);

    // Pull SMS report
    $callbackResult = $puller->pullCallback(10);
    $callbackRsp = json_decode($callbackResult);
    echo $callbackResult;

    // Pull reply
    $replyResult = $puller->pullReply(10);
    $replyRsp = json_decode($replyResult);
    echo $replyResult;
} catch (\Exception $e) {
    echo var_dump($e);
}
```
>**Note:**
>To apply for SMS message-pulling feature, contact Tencent Cloud SMS technical support (QQ: 3012203387). Customers who need to pull a large number of messages can use this feature for batch operation. It is not recommended for those who do not have such a requirement.

- **Send international SMS message**
Similar to sending China SMS messages.

