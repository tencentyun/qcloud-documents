
SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/38764)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口
>一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。


## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：PHP 5.6.33 及以上版本。
- 已在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/38764)。
- 下载 SDK 源码请访问 [PHP SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-php)。

## 安装 SDK


[Composer](https://www.phpcomposer.com) 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 安装 Composer。
 - Windows 环境：请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包并进行安装。
 - UNIX 环境：执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
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
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。


### 申请短信模板

```
<?php
require_once '../../../TCloudAutoLoader.php';
// 导入 SMS 模块的 client
use TencentCloud\Sms\V20190711\SmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Sms\V20190711\Models\AddSmsTemplateRequest;
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
    
		$cred = new Credential("xxx", "xxx");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    // 配置代理
    // $httpProfile->setProxy("https://ip:port");
    $httpProfile->setReqMethod("GET");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 HmacSHA256）
    $clientProfile->setHttpProfile($httpProfile);

    // 实例化 SMS 的 client 对象，clientProfile 是可选的
    $client = new SmsClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个 AddSmsTemplateRequest 请求对象，每个接口都会对应一个 request 对象。
    $req = new AddSmsTemplateRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
	   * 帮助链接：
	   * 短信控制台：https://console.cloud.tencent.com/smsv2
  	 * sms helper：https://cloud.tencent.com/document/product/382/3773
  	*/
	
	/* 模板名称 */
	$req->TemplateName = "腾讯云";
	/* 模板内容 */
	$req->TemplateContent = "{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。";
	/* 短信类型：0表示普通短信, 1表示营销短信 */
	$req->SmsType = 0;
	/* 是否国际/港澳台短信：
		0表示国内短信
		1表示国际/港澳台短信 */
	$req->International = 0;
	/* 模板备注：例如申请原因，使用场景等 */
	$req->Remark = "xxx";

    // 通过 client 对象调用 AddSmsTemplate 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->AddSmsTemplate($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

### 发送短信

```
<?php
require_once '../../../TCloudAutoLoader.php';
// 导入 SMS 的 client
use TencentCloud\Sms\V20190711\SmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Sms\V20190711\Models\SendSmsRequest;
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

    $cred = new Credential("xxx", "xxx");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    // 配置代理
    // $httpProfile->setProxy("https://ip:port");
    $httpProfile->setReqMethod("GET");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 HmacSHA256）
    $clientProfile->setHttpProfile($httpProfile);

    // 实例化 SMS 的 client 对象，clientProfile 是可选的
    $client = new SmsClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个 sms 发送短信请求对象，每个接口都会对应一个 request 对象。
    $req = new SendSmsRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
       * 帮助链接：
       * 短信控制台：https://console.cloud.tencent.com/smsv2
       * sms helper：https://cloud.tencent.com/document/product/382/3773 */

    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
    $req->SmsSdkAppid = "1400787878";
    /* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，可登录 [短信控制台] 查看签名信息 */
    $req->Sign = "xxx";
    /* 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper] */
    $req->ExtendCode = "";
    /* 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
	   * 例如+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号*/
    $req->PhoneNumberSet = array("+8613711112222", "+8613711333222", "+8613711144422");
    /* 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper] */
    $req->SenderId = "";
    /* 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
    $req->SessionContext = "xxx";
    /* 模板 ID: 必须填写已审核通过的模板 ID。可登录 [短信控制台] 查看模板 ID */
    $req->TemplateID = "449739";
    /* 模板参数: 若无模板参数，则设置为空*/
    $req->TemplateParamSet = array("0");


    // 通过 client 对象调用 SendSms 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->SendSms($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

### 拉取回执状态


```
<?php
require_once '../../../TCloudAutoLoader.php';
// 导入 SMS 模块的 client
use TencentCloud\Sms\V20190711\SmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Sms\V20190711\Models\PullSmsSendStatusRequest;
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

    $cred = new Credential("xxx", "xxx");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    // 配置代理
    // $httpProfile->setProxy("https://ip:port");
    $httpProfile->setReqMethod("GET");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 HmacSHA256）
    $clientProfile->setHttpProfile($httpProfile);

    // 实例化 SMS 的 client 对象，clientProfile 是可选的
    $client = new SmsClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个 SMS 发送短信请求对象,每个接口都会对应一个request对象
    $req = new PullSmsSendStatusRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
       * 帮助链接：
       * 短信控制台：https://console.cloud.tencent.com/smsv2
       * sms helper：https://cloud.tencent.com/document/product/382/3773 */

    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
    $req->SmsSdkAppid = "1400787878";
    /* 拉取最大条数，最多100条 */
    $req->Limit = 10;


    // 通过 client 对象调用 PullSmsSendStatus 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->PullSmsSendStatus($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```


### 统计短信发送数据

```
<?php
require_once '../../../TCloudAutoLoader.php';
// 导入 SMS 模块的 client
use TencentCloud\Sms\V20190711\SmsClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Sms\V20190711\Models\SendStatusStatisticsRequest;
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

    $cred = new Credential("xxx", "xxx");
    //$cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选，无特殊需求时可以跳过
    $httpProfile = new HttpProfile();
    // 配置代理
    // $httpProfile->setProxy("https://ip:port");
    $httpProfile->setReqMethod("GET");  // POST 请求（默认为 POST 请求）
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒（默认60秒）
    $httpProfile->setEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名（默认就近接入）

    // 实例化一个 client 选项，可选，无特殊需求时可以跳过。
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法（默认为 HmacSHA256）
    $clientProfile->setHttpProfile($httpProfile);

    // 实例化 SMS 的 client 对象，clientProfile 是可选的
    $client = new SmsClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个 SMS 发送短信请求对象，每个接口都会对应一个 request 对象
    $req = new SendStatusStatisticsRequest();

    /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
     * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
     * 基本类型的设置:
       * 帮助链接：
       * 短信控制台：https://console.cloud.tencent.com/smsv2
       * sms helper：https://cloud.tencent.com/document/product/382/3773 */

    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
    $req->SmsSdkAppid = "1400787878";
    /* 拉取最大条数，最多100条 */
    $req->Limit = 10;
    /* 偏移量 注：目前固定设置为0 */
    $req->Offset = 0;
    /* 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时 */
    $req->StartDateTime = "2019122500";
    /* 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
	 * 注：EndDataTime 必须大于 StartDateTime */
    $req->EndDataTime = "2019122523";

    // 通过 client 对象调用 SendStatusStatistics 方法发起请求。注意请求方法名与请求对象是对应的
    $resp = $client->SendStatusStatistics($req);

    // 输出 JSON 格式的字符串回包
    print_r($resp->toJsonString());

    // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

## 常见问题[](id:point)
<dx-accordion>
::: 证书问题
如果您的 PHP 环境证书有问题，可能会遇到报错，类似于`cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html`，请尝试按以下步骤解决：

1. 到 https://curl.haxx.se/ca/cacert.pem 下载证书文件`cacert.pem`，将其保存到 PHP 安装路径下。
2. 编辑`php.ini`文件，删除`curl.cainfo`配置项前的分号注释符（;），值设置为保存的证书文件`cacert.pem`的绝对路径。
3. 重启依赖 PHP 的服务。
:::
::: php_curl\s扩展
此 SDK 依赖的 GuzzleHttp 需要开启 php_curl 扩展，查看环境上的 php.ini 环境确认是否已启用，例如在 Linux 环境下，PHP 7.1 版本，托管在 apache 下的服务，可以打开 /etc/php/7.1/apache2/php.ini，查看 extension=php_curl.dll 配置项是否已被注释，请删除此项配置前的注释符并重启 apache。
:::
::: Web\s访问异常
命令行下执行正常，但是放在 Web 服务器执行则报错：

`cURL error 0: The cURL request was retried 3 times and did not succeed. The most likely reason for the failure is that cURL was unable to rewind the body of the request and subsequent retries resulted in the same error. Turn on the debug option to see what went wrong. See https://bugs.php.net/bug.php?id=47204 for more information. (see http://curl.haxx.se/libcurl/c/libcurl-errors.html)`

此问题出现情况不一。可以运行`php -r "echo sys_get_temp_dir();"`，打印系统默认临时目录绝对路径，然后在`php.ini`配置`sys_temp_dir`为这个值，尝试是否能解决。
:::
::: 源码安装问题
为了支持部分源码安装的需要，我们将依赖的包文件放在 vendor 目录中，又考虑到不能造成对 composer 的不兼容，github 不得不设置禁止导出 vendor 目录，造成必须使用`git clone`命令才能拿到 vendor 目录的情况，对一些不熟悉 github 的用户造成了困扰。从3.0.188版本开始，我们暂时移除了源码安装，必须使用 composer 安装 SDK 和依赖的包。
:::
::: 代理设置
在有代理的环境下，需要设置系统环境变量`https_proxy`，否则可能无法正常调用，抛出连接超时的异常。
或使用 GuzzleHttp 代理配置：
```php
$cred = new Credential("secretId", "secretKey");

$httpProfile = new HttpProfile();
$httpProfile->setProxy('https://ip:port');

$clientProfile = new ClientProfile();
$clientProfile->setHttpProfile($httpProfile);
```
:::
</dx-accordion>
