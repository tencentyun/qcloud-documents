
本文主要介绍适用于 PHP 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 PHP 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。

## 依赖环境
- PHP 5.6.33 版本及以上。
- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

[Composer](https://www.phpcomposer.com) 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 安装 Composer。
 - Windows 环境：请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包并进行安装。
 - UNIX 环境：执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```
2. 建议中国大陆地区的用户设置腾讯云镜像源：`composer config -g repos.packagist composer https://mirrors.tencent.com/composer/`
3. 添加依赖：
```
composer require tencentcloud/tencentcloud-sdk-php
```
4. 在代码中添加以下引用代码。
>!本文仅为示例，composer 会在项目根目录下生成 vendor 目录，`/path/to/`为项目根目录的实际绝对路径，如果是在项目根目录执行，可以省略绝对路径。
>
```
require '/path/to/vendor/autoload.php';
```

<span id="example"></span>
## 示例
本文以云服务器查询可用区接口为例，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-php/tree/master/examples)。

```php
<?php
require 'vendor/autoload.php';
// 导入对应产品模块的client
use TencentCloud\Cvm\V20170312\CvmClient;
// 导入要请求接口对应的Request类
use TencentCloud\Cvm\V20170312\Models\DescribeZonesRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
try {
    // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
    $cred = new Credential("secretId", "secretKey");

    // # 实例化要请求产品(以cvm为例)的client对象
    $client = new CvmClient($cred, "ap-guangzhou");

    // 实例化一个请求对象
    $req = new DescribeZonesRequest();

    // 通过client对象调用想要访问的接口，需要传入请求对象
    $resp = $client->DescribeZones($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

## 常见问题
### 代理
在有代理的环境下，需要设置系统环境变量`https_proxy`，否则可能无法正常调用，抛出连接超时的异常。
或使用 GuzzleHttp 代理配置：
```php
$cred = new Credential("secretId", "secretKey");

$httpProfile = new HttpProfile();
$httpProfile->setProxy('https://ip:port');

$clientProfile = new ClientProfile();
$clientProfile->setHttpProfile($httpProfile);

$client = new OcrClient($cred, 'ap-beijing', $this->clientProfile);
```

### 证书问题
如果 PHP 环境证书有问题，遇到类似`cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html`报错，请尝试参照以下步骤解决：
1. 下载证书文件 [cacert.pem](https://curl.haxx.se/ca/cacert.pem)，将其保存到 PHP 安装路径下。
2. 编辑`php.ini`文件，删除`curl.cainfo`配置项前的分号注释符（;），值设置为保存的证书文件`cacert.pem`的绝对路径。
3. 重启依赖 PHP 的服务。

### php_curl 扩展
SDK 依赖的 GuzzleHttp 需要开启 php_curl 扩展，查看环境上的`php.ini`环境确认是否已启用。
例如，在 Linux 环境下，PHP 7.1 版本，托管在 apache 下的服务，可以打开`/etc/php/7.1/apache2/php.ini`中查看`extension=php_curl.dll`配置项是否被注释，请删除该项配置前的注释符并重启 apache。

### Web 访问异常
命令行下执行正常，但是放在 Web 服务器执行则报错：cURL error 0: The cURL request was retried 3 times and did not succeed. The most likely reason for the failure is that cURL was unable to rewind the body of the request and subsequent retries resulted in the same error. Turn on the debug option to see what went wrong. See https://bugs.php.net/bug.php?id=47204 for more information. (see http://curl.haxx.se/libcurl/c/libcurl-errors.html)。
此问题出现情况不一，可以运行 `php -r "echo sys_get_temp_dir();"` 打印系统默认临时目录绝对路径，然后在`php.ini`配置`sys_temp_dir`为打印出的路径，尝试是否能解决。


## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请参考 [旧版 PHP SDK](https://github.com/QcloudApi/qcloudapi-sdk-php)，但不再维护更新，推荐使用新版 SDK。
