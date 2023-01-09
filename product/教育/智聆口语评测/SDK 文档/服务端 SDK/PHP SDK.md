## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
Tencent Cound API 3.0 SDK，封装了腾讯云的 SDK，通过集成SDK，可以快速接入相关产品功能，如智聆口语评测，数学作业批改，英文作文批改。本文档介绍 [智聆口语评测](https://cloud.tencent.com/document/product/884/19309) 相关说明。

## 流程图
流程图请参见 [服务模式](https://cloud.tencent.com/document/product/884/33697)。

## SDK 集成准备
1. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在访问管理 > 访问密钥 > [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取该凭证。
>! 密钥属于敏感信息，正式密钥仅可在调试使用，线上环境情况下，为了防止他人盗取，推荐使用 [临时签名](https://cloud.tencent.com/document/product/884/31888#SecretKey)，具体请参考 [签名](https://cloud.tencent.com/document/product/884/31888#SecretKey) 相关内容。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3049463174ada47857762086690e7c26.png)
2. 设备准备
准备一台电脑。

## SDK DEMO 使用流程
1. 安装依赖环境
安装 PHP 5.6.0 版本及以上。

2. 下载 SDK
从 github 下载 [tencentcloud-sdk-php](https://github.com/TencentCloud/tencentcloud-sdk-php)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-php.git
```
3. 获取安装
	- 安装 Composer 
windows 环境请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包安装。
unix 环境在命令行中执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```
	- 更换镜像源
建议中国大陆地区的用户设置腾讯云镜像源：
```
composer config -g repos.packagist composer https://mirrors.tencent.com/composer/
```
	- 安装 SDK
执行命令：
```
composer require tencentcloud/tencentcloud-sdk-php
```
添加依赖。如果只想安装某个产品的，可以使用：
```
composer require tencentcloud/产品名
```
例如：
```
composer require tencentcloud/soe
```
	- 导入 SDK
在代码中添加以下引用代码。注意：如下仅为示例，composer 会在项目根目录下生成 vendor 目录，/path/to/
为项目根目录的实际绝对路径，如果是在当前目录执行，可以省略绝对路径。
```
require '/path/to/vendor/autoload.php';
```

4. 运行项目
	1. 进入 `examples/soe/v20180903/init_oral_process.php`，填入 SecretId 和 SecretKey。
```
// 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("", "");
```
	2. 填入请求参数，参考 [InitOralProcess](https://cloud.tencent.com/document/product/884/19319)，运行项目，进行评测。
```
$client = new SoeClient($cred, "", $clientProfile);

// 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
$req = new InitOralProcessRequest();
$req->RefText = "since";
$req->WorkMode = 0;
$req->EvalMode = 1;
$req->ScoreCoeff = 3.5;
$req->SessionId = "stress_test_956938";

$resp = $client->InitOralProcess($req);

// 输出json格式的字符串回包
print_r($resp->toJsonString());
```
	3. 获取评测结果，参考 [数据结构](https://cloud.tencent.com/document/product/884/19320)。

## SDK 使用方法
### 临时密钥（推荐）
客户端为了密钥安全性，需要考虑在服务端使用临时密钥，对密钥进行加密处理。PHP 临时密钥参考如下（填入密钥信息使用）：
```
<?php
require_once __DIR__.'/../../../vendor/autoload.php';
// 导入对应产品模块的client
use TencentCloud\Sts\V20180813\StsClient;

// 导入要请求接口对应的Request类
use TencentCloud\Sts\V20180813\Models\GetFederationTokenRequest;
use TencentCloud\Sts\V20180813\Models\GetFederationTokenResponse;

use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

try {
    // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("secretId", "secretKey");
    //$cred = new Credential(getenv(""), getenv("");

    // 实例化一个http选项，可选的，没有特殊需求可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // post请求(默认为post请求)
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒(默认60秒)
    $httpProfile->setEndpoint("sts.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)

    // 实例化一个client选项，可选的，没有特殊需求可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法(默认为HmacSHA256)
    $clientProfile->setHttpProfile($httpProfile);

    $client = new StsClient($cred, "ap-beijing", $clientProfile);

    // 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
    $req = new GetFederationTokenRequest();
    $req->Name = "soe";
    $req->Policy = "{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\", \"action\": [\"soe:TransmitOralProcessWithInit\"], \"resource\": \"*\"}}";

    $resp = $client->GetFederationToken($req);

    // 输出json格式的字符串回包
    print_r($resp->toJsonString());

}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```
### 内部签名（推荐）
#### 发音数据传输接口附带初始化过程(推荐)
[TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口使用示例：
```
<?php
require_once __DIR__.'/../../../vendor/autoload.php';
// 导入对应产品模块的client
use TencentCloud\Soe\V20180724\SoeClient;

// 导入要请求接口对应的Request类
use TencentCloud\Soe\V20180724\Models\TransmitOralProcessWithInitRequest;
use TencentCloud\Soe\V20180724\Models\TransmitOralProcessWithInit;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

function  uuid()
{
    $chars = md5(uniqid(mt_rand(), true));
    $uuid = substr ( $chars, 0, 8 ) . '-'
        . substr ( $chars, 8, 4 ) . '-'
        . substr ( $chars, 12, 4 ) . '-'
        . substr ( $chars, 16, 4 ) . '-'
        . substr ( $chars, 20, 12 );
    return $uuid ;
}

try {
    // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("", "");
    //$cred = new Credential(getenv(""), getenv("");
    $musicfile = "1.wav"; //本地音频文件
    $musicData = file_get_contents($musicfile);
    $base64Data = base64_encode($musicData);
    // 实例化一个http选项，可选的，没有特殊需求可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // post请求(默认为post请求)
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒(默认60秒)
    $httpProfile->setEndpoint("soe.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)

    // 实例化一个client选项，可选的，没有特殊需求可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法(默认为HmacSHA256)
    $clientProfile->setHttpProfile($httpProfile);

    $client = new SoeClient($cred, "", $clientProfile);

    // 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
    $req = new TransmitOralProcessWithInitRequest();
    $req->RefText = "since";
    $req->WorkMode = 0;
    $req->EvalMode = 1;
    $req->ScoreCoeff = 3.5;
    $req->SessionId = uuid();
    $req->VoiceFileType = 2;
    $req->SeqId = 1;
    $req->VoiceEncodeType = 1;
    $req->IsEnd = 1;
    $req->UserVoiceData = $base64Data;
    $resp = $client->TransmitOralProcessWithInit($req);

    // 输出json格式的字符串回包
    print_r($resp->toJsonString());

    // 也可以取出单个值。
    // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
}
catch(TencentCloudSDKException $e) {
    echo $e;
}

```

#### 发音评估初始化和发音数据传输接口
[InitOralProcess](https://cloud.tencent.com/document/api/884/19319) 和 [TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318) 组合使用示例：
```
<?php
require_once __DIR__ . '/../../../vendor/autoload.php';

// 导入对应产品模块的client
use TencentCloud\Soe\V20180724\SoeClient;

// 导入要请求接口对应的Request类
use TencentCloud\Soe\V20180724\Models\InitOralProcessRequest;
use TencentCloud\Soe\V20180724\Models\InitOralProcess;
use TencentCloud\Soe\V20180724\Models\TransmitOralProcessRequest;
use TencentCloud\Soe\V20180724\Models\TransmitOralProcessResponse;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;

// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

function uuid()
{
    $chars = md5(uniqid(mt_rand(), true));
    $uuid = substr($chars, 0, 8) . '-'
        . substr($chars, 8, 4) . '-'
        . substr($chars, 12, 4) . '-'
        . substr($chars, 16, 4) . '-'
        . substr($chars, 20, 12);
    return $uuid;
}

try {
    $sessionid = uuid();
    // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("", "");
    //$cred = new Credential(getenv(""), getenv("");

    // 实例化一个http选项，可选的，没有特殊需求可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // post请求(默认为post请求)
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒(默认60秒)
    $httpProfile->setEndpoint("soe.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)

    // 实例化一个client选项，可选的，没有特殊需求可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法(默认为HmacSHA256)
    $clientProfile->setHttpProfile($httpProfile);

    $client = new SoeClient($cred, "", $clientProfile);

    // 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
    $req = new InitOralProcessRequest();
    $req->RefText = "since";
    $req->WorkMode = 0;
    $req->EvalMode = 1;
    $req->ScoreCoeff = 3.5;
    $req->SessionId = $sessionid;

    $resp = $client->InitOralProcess($req);

    // 输出json格式的字符串回包
    print_r($resp->toJsonString());

    $musicfile = "1.wav"; //本地音频文件
    $musicData = file_get_contents($musicfile);
    $base64Data = base64_encode($musicData);

    // 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
    $transreq = new TransmitOralProcessRequest();
    $transreq->SessionId = $sessionid;
    $transreq->VoiceFileType = 2;
    $transreq->SeqId = 1;
    $transreq->VoiceEncodeType = 1;
    $transreq->IsEnd = 1;
    $transreq->UserVoiceData = $base64Data;
    $transresp = $client->TransmitOralProcess($transreq);

    // 输出json格式的字符串回包
    print_r($transresp->toJsonString());

    // 也可以取出单个值。
    // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
//    print_r($transresp->TotalCount);

    // 也可以取出单个值。
    // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
} catch (TencentCloudSDKException $e) {
    echo $e;
}
```

#### 关键词评测
[KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 接口使用示例：
```
<?php
require_once __DIR__.'/../../../vendor/autoload.php';
// 导入对应产品模块的client
use TencentCloud\Soe\V20180724\SoeClient;

// 导入要请求接口对应的Request类
use TencentCloud\Soe\V20180724\Models\KeywordEvaluateRequest;
use TencentCloud\Soe\V20180724\Models\KeywordEvaluate;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

function  uuid()
{
    $chars = md5(uniqid(mt_rand(), true));
    $uuid = substr ( $chars, 0, 8 ) . '-'
        . substr ( $chars, 8, 4 ) . '-'
        . substr ( $chars, 12, 4 ) . '-'
        . substr ( $chars, 16, 4 ) . '-'
        . substr ( $chars, 20, 12 );
    return $uuid ;
}

try {
    // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("secretId", "secretKey");
    //$cred = new Credential(getenv(""), getenv("");
    $musicfile = "1.wav";
    $musicData = file_get_contents($musicfile);
    $base64Data = base64_encode($musicData);
    // 实例化一个http选项，可选的，没有特殊需求可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("POST");  // post请求(默认为post请求)
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒(默认60秒)
    $httpProfile->setEndpoint("soe.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)

    // 实例化一个client选项，可选的，没有特殊需求可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法(默认为HmacSHA256)
    $clientProfile->setHttpProfile($httpProfile);

    $client = new SoeClient($cred, "", $clientProfile);

    // 实例化一个ecc实例信息查询请求对象,每个接口都会对应一个request对象。
    $req = new KeywordEvaluateRequest();
    $params = array(
        "SeqId" => 1,
        "IsEnd" => 1,
        "VoiceFileType" => 2,
        "VoiceEncodeType" => 1,
        "UserVoiceData" => $base64Data,
        "SessionId" => uuid(),
        "Keywords" => array(
            array(
                "RefText" => "since",
                "EvalMode" => 1,
                "ServerType" => 0,
                "ScoreCoeff" => 3,
                "TextMode" => 0
            ),
            array(
                "RefText" => "car",
                "EvalMode" => 0,
                "ServerType" => 0,
                "ScoreCoeff" => 1,
                "TextMode" => 0
            )
        )
    );
    $req->fromJsonString(json_encode($params));
    $resp = $client->KeywordEvaluate($req);

    // 输出json格式的字符串回包
    print_r($resp->toJsonString());

    // 也可以取出单个值。
    // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
}
catch(TencentCloudSDKException $e) {
    echo $e;
}

```

### 外部签名（不推荐）
使用 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口演示。
1. 生成 curl
```
<?php
$secretId = "";
$secretKey = "";
$host = "soe.tencentcloudapi.com";
$service = "soe";
$version = "2018-07-24";
$action = "TransmitOralProcessWithInit";
$region = "ap-guangzhou";
$timestamp = time();
//$timestamp = 1551113065;
$algorithm = "TC3-HMAC-SHA256";

// step 1: build canonical request string
$httpRequestMethod = "POST";
$canonicalUri = "/";
$canonicalQueryString = "";
$canonicalHeaders = "content-type:application/json; charset=utf-8\n"."host:".$host."\n";
$signedHeaders = "content-type;host";
$payload = '{"SeqId": 1, "IsEnd": 1, "VoiceFileType": 3, "VoiceEncodeType": 1, "UserVoiceData": "//MoxAALuN4gAUkwAYQh1xWKzZAAMDZPRAKCRiYoJEEP/c4jHPJk0zAGA02ghGPERnaPZARHP8f+BkQQ/CqjfIxQLhkl2RAz//MoxAwPgNqoAZp4ADtQSTWOF1F+AEmTEImdt6jsb6WhXxTCvtkfiVUSLYdfX7hHvulYVqRfAZ+XOecxF//ph/+HbmNezSs8//MoxAkO4Oq4y9pQACMIy2HqbczDokotX71inxey/+udQMhypprA6IdjTWZWb0/QeaAFihx9/dr6NrdmgLOhat/++GIFmkGq//MoxAgOOO7UAHvKcD4u3EwOF9XNMK99Nu9Malj/0ERAqKi6tqYOCnGMAYuPg4il3/+fNB4QBhqZkYLEFC36InsC0mtHtEHf//MoxAoNYPLQAIPScBN69jsHpVNf/FFkPLf/UQ5X6QoAgm+QLisHkaUGoJEMFc///21mX2f9aRil/+KtwSkZ0XEtUWAzE23n//MoxA8Q4OrAAHvecHuoXU9pmuMRsAAl5kxR+iGa25Xy5K5DZndk+5GjFi4ruA3Po3Y////6CJMIhNvYgUhIGXFlFdljblAF//MoxAYOOLcWXmrSTqAB3RCZhvPpqgorarEywEZfpMLiImr/EbP9oFSJ/tRkmWkyCqSB7////ZGIiBim4gD60h/bQ8PAPWCj//MoxAgNMK7dlGveTCGa8yD4Mq/3dFs2/HPQW1XSttIJyKLf22MNsUyxqRmPUuHgi0b////9eQ9wkusmAPBsncNhPkwKoUqn//MoxA4MyK7IAGteTC6OJRT0Ugvx6Ur7OCiUV3r9HnSoYlWVg6oBkf////vLEFNRFMnV8nAFvQwtRZv2MBA4/bybO662jmbd//MoxBUMWNrIAGvMcOK8QpNEgWIosuBaLtuJf9k8M////7UF2StBPfNK6hDgnRvqAyTP/SiQH8hU31/HJqzWg1N61Y0lmoYI//MoxB4NINbEAGvQcGCCb5XfJDJD///1PwmCwKnlG36HrNEa6iqFSihJgRArUoxkzNS9Nr7hnHzGj4peHNfx0dx3LDJ2SFjN//MoxCQMcMrEAIvMcFl0ir////A6xOIktb+mtyEzawnALISGYieXWnFQ5AFCGKxU3XkVteSTc2uUS0oUBAWA0eU+W/t/9QVD//MoxC0NKMa8KmIEcEDQPB2WBqDVr/8/52mU2Dx0NTL1rqQqpzzbAf/0iBIOu37LJ1HPQzcM7dkKXYXETT9ZXqET//UHZbrV//MoxDMMkN6QUNJEcCkoBAN01mbKkI1yPAyqjxXtZltKeAxYa4aAqf+eSGHFlLlKD6m2O9vnhi9qmO////s/+lVRTMnty4ke//MoxDsM0Dp4H1kQABcA/8JwUE/8ciCyT/8YceY5ETf/8RgchQJAcBKf/5OGEHIPMwJQTP//83QGHJdyTGHHmQP///yTJceB//MoxEIXmxqkAYdoAdL49B6EoTBLB4BaP////wtAwA80jQvqY+XDQvrKtXQiaPYkjALhtQTGjWUR4g9zGdfMjohS5vsRp3Xo//MoxB4UcuLQAYcoAb+onWzt9f+RhpFP7qevrbvcyIFMkVE+uYqgxxbzTrFaiZ27KGnYnMR+UYQwfHKYo78ih2r+1cO1qvRa//MoxAcNkp68AYIoAHv6P9ef7/qHBTqpfQWY1u230+YsSHE+2/2RH7SlnoAx0+tLJ/r6CcvMYWMVd9n66oKbdTGxwbruYXOO//MoxAsOchKQAYI4ACXC5rVY5PHD9jnod+arRqj5hL80xXnzl9f+sgPH/uPP/+3lHRircOlTv5Fm0l+qx+zHquq7CjCgJhQE//MoxAwNqSGQA8MQAEkzN/+hjPq1W//qygIlAICFKAnvBpZ0sWPCV1WCpU6DQ87/Ue6vyUGiwNVMQU1FMy45OS41VVVVVVVV", "SessionId": "test_1432543", "RefText": "bick sdfad", "WorkMode": 1, "EvalMode": 1, "ScoreCoeff": 1}';
$hashedRequestPayload = hash("SHA256", $payload);
$canonicalRequest = $httpRequestMethod."\n"
    .$canonicalUri."\n"
    .$canonicalQueryString."\n"
    .$canonicalHeaders."\n"
    .$signedHeaders."\n"
    .$hashedRequestPayload;
echo $canonicalRequest.PHP_EOL;

// step 2: build string to sign
$date = gmdate("Y-m-d", $timestamp);
$credentialScope = $date."/".$service."/tc3_request";
$hashedCanonicalRequest = hash("SHA256", $canonicalRequest);
$stringToSign = $algorithm."\n"
    .$timestamp."\n"
    .$credentialScope."\n"
    .$hashedCanonicalRequest;
echo $stringToSign.PHP_EOL;

// step 3: sign string
$secretDate = hash_hmac("SHA256", $date, "TC3".$secretKey, true);
$secretService = hash_hmac("SHA256", $service, $secretDate, true);
$secretSigning = hash_hmac("SHA256", "tc3_request", $secretService, true);
$signature = hash_hmac("SHA256", $stringToSign, $secretSigning);
echo $signature.PHP_EOL;

// step 4: build authorization
$authorization = $algorithm
    ." Credential=".$secretId."/".$credentialScope
    .", SignedHeaders=content-type;host, Signature=".$signature;
echo $authorization.PHP_EOL;

$curl = "curl -X POST https://".$host
    .' -H "Authorization: '.$authorization.'"'
    .' -H "Content-Type: application/json; charset=utf-8"'
    .' -H "Host: '.$host.'"'
    .' -H "X-TC-Action: '.$action.'"'
    .' -H "X-TC-Timestamp: '.$timestamp.'"'
    .' -H "X-TC-Version: '.$version.'"'
    .' -H "X-TC-Region: '.$region.'"'
    ." -d '".$payload."'";
echo $curl.PHP_EOL;
```

2. 根据签名信息，进行调用
```
$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_URL => 'https://soe.tencentcloudapi.com',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => '',
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 0,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS =>$payload,
    CURLOPT_HTTPHEADER => array(
        "Authorization: $authorization",
        'Content-Type: application/json; charset=utf-8',
        'Host: soe.tencentcloudapi.com',
        'X-TC-Action: TransmitOralProcessWithInit',
        "X-TC-Timestamp: $timestamp",
        'X-TC-Version: 2018-07-24',
        'X-TC-Region: ap-guangzhou'
    ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

## 参数说明
### 请求参数说明

| 接口名称 | 接口功能 | 
|---------|---------|
| [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 	| 发音数据传输接口附带初始化过程（常用实践）| 
| [InitOralProcess](https://cloud.tencent.com/document/api/884/19319)	| 发音评估初始化| 
| [KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 	| 关键词评测| 
|[TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318)	|发音数据传输接口|
 
### 返回结果说明
参考 API 文档 [数据结构](https://cloud.tencent.com/document/api/884/19320)。

## 错误码
参考 API 文档 [错误码](https://cloud.tencent.com/document/api/884/30658)。

## 常见问题
参考 [常见问题](https://cloud.tencent.com/document/product/884/32593)。 






