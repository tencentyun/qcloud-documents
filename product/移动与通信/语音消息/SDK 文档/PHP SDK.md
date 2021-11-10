SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [语音消息 API](https://cloud.tencent.com/document/product/1128/51569)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#SendTtsVoice)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。

## 前提条件
- 已开通语音消息服务，具体操作请参见 [快速入门](https://cloud.tencent.com/document/product/1128/37343)。
- 已准备依赖环境：PHP 5.6.0 版本及以上。
- 已在访问管理控制台 >**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 语音消息的调用地址为`vms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/1128/51569)。
- 下载 SDK 源码请访问 [PHP SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-php)。

## 安装 SDK
[Composer](https://www.phpcomposer.com) 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 安装 Composer。
 - Windows 环境：请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包并进行安装。
 - UNIX 环境：执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
```
2. 添加依赖。
```
composer require tencentcloud/tencentcloud-sdk-php
```
3. 在代码中添加以下引用代码。
>!本文仅为示例，composer 会在项目根目录下生成 vendor 目录，`/path/to/`为项目根目录的实际绝对路径，如果是在项目根目录执行，可以省略绝对路径。
>
```
require '/path/to/vendor/autoload.php';
```

## 示例代码[](id:example)
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vms&Version=2020-09-02&Action=SendCodeVoice) 自动化生成 Demo 代码。
每个接口都有一个对应的 Request 结构和一个 Response 结构。示例代码如下所示。

### 发送语音验证码

```
<?php
require_once '../vendor/autoload.php';
// 导入 VMS 的 client
use TencentCloud\Vms\V20200902\VmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Vms\V20200902\Models\SendCodeVoiceRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

try {
    /* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
     */

    $cred = new Credential("secretId", "secretKey");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("vms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 TC3-HMAC-SHA256）
    $clientProfile->setHttpProfile($httpProfile);

    /* 实例化 VMS 的 client 对象，clientProfile 是可选的
     * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
     */
    $client = new VmsClient($cred, "ap-guangzhou", $clientProfile);

    // 实例化一个 VMS 发送短信请求对象，每个接口都会对应一个 request 对象。
    $req = new SendCodeVoiceRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
       * 帮助链接：
       * 语音消息控制台：https://console.cloud.tencent.com/vms
       * vms helper：https://cloud.tencent.com/document/product/1128/37720 */

    // 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"
    $req->CodeMessage = "1234";
    /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
     * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号 
     */
    $req->CalledNumber = "+8613711112222";
    // 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666
    $req->VoiceSdkAppid = "1400006666";
    // 播放次数，可选，最多3次，默认2次
    $req->PlayTimes = 2;
    // 用户的 session 内容，腾讯 server 回包中会原样返回
    $req->SessionContext = "xxxx";

    // 通过 client 对象调用 SendCodeVoice 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->SendCodeVoice($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->RequestId);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

### 指定模版发送语音通知[](id:SendTtsVoice)

```
<?php
require_once '../vendor/autoload.php';
// 导入 VMS 的 client
use TencentCloud\Vms\V20200902\VmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Vms\V20200902\Models\SendTtsVoiceRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

try {
    /* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
     */

    $cred = new Credential("secretId", "secretKey");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("vms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 TC3-HMAC-SHA256）
    $clientProfile->setHttpProfile($httpProfile);

    /* 实例化 VMS 的 client 对象，clientProfile 是可选的
     * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
     */
    $client = new VmsClient($cred, "ap-guangzhou", $clientProfile);

    // 实例化一个 VMS 发送短信请求对象，每个接口都会对应一个 request 对象。
    $req = new SendTtsVoiceRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
       * 帮助链接：
       * 语音消息控制台：https://console.cloud.tencent.com/vms
       * vms helper：https://cloud.tencent.com/document/product/1128/37720 */

    // 模板 ID，必须填写在控制台审核通过的模板 ID，可登陆 [语音消息控制台] 查看模板 ID
    $req->TemplateId = "4356";
    // 模板参数，若模板没有参数，请提供为空数组
    $req->TemplateParamSet = array("7652");
    /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
        * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号 */
    $req->CalledNumber = "+8613711112222";
    // 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666
    $req->VoiceSdkAppid = "1400006666";
    // 播放次数，可选，最多3次，默认2次
    $req->PlayTimes = 2;
    // 用户的 session 内容，腾讯 server 回包中会原样返回
    $req->SessionContext = "xxxx";

    // 通过 client 对象调用 SendTtsVoice 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->SendTtsVoice($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->RequestId);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```
