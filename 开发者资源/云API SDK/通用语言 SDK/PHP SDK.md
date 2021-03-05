## 简介

* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式。
* 本文以 PHP SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* PHP 5.6.33 版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/494e3420874b6ba9421c98a3717531ab.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。


## 安装 PHP SDK 3.0
通过 Composer 获取安装是使用 PHP SDK 推荐方法，Composer 是 PHP 的依赖管理工具。关于 Composer 详细可参见 [Composer 官网](https://getcomposer.org/download/)。 
>? Composer 需要 PHP 5.3.2+ 以上版本，且需要开启 openssl。
### 步骤1：安装 Composer
 - Windows 环境请访问 [Composer](https://getcomposer.org/download/) 官网下载安装包安装。
 - Unix 环境在命令行中执行以下命令安装：
```
curl -sS https://getcomposer.org/installer | php
```
```
sudo mv composer.phar /usr/local/bin/composer
```

### 步骤2：添加镜像源
中国大陆地区的用户可以使用腾讯云镜像源提高下载速度，在打开的命令窗口执行以下命令：
```
composer config -g repos.packagist composer https://mirrors.tencent.com/composer/
```

### 步骤3：添加依赖
在打开的命令窗口执行命令安装 SDK（安装到指定位置），例如安装到`C:\Users\···>`目录下，则在指定的位置打开命令窗口，并执行以下命令：

```
composer require tencentcloud/tencentcloud-sdk-php
```

### 步骤4：添加引用
在代码中添加以下引用代码。注意：如下仅为示例，Composer 会在项目根目录下生成 vendor 目录，/path/to/ 为项目根目录的实际绝对路径（如果是在当前目录执行，可以省略绝对路径）。
```
require '/path/to/vendor/autoload.php';
```

>?
>- 如果只想安装某个产品的，可以使用`composer require tencentcloud/`产品名，例如`composer require tencentcloud/cvm`。
>- 更多 SDK 支持的云产品，请参见 [云产品名列表](https://cloud.tencent.com/document/product/494/42698#.E6.94.AF.E6.8C.81-sdk-3.0.E7.89.88.E6.9C.AC.E7.9A.84.E4.BA.91.E4.BA.A7.E5.93.81.E5.88.97.E8.A1.A8)。

## 使用 SDK
- 推荐使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer)，提供在线调用、签名验证、SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 3.0 和 SDK 的难度。
- 还可以参考 SDK 仓库中 [examples](https://github.com/TencentCloud/tencentcloud-sdk-php/tree/master/examples) 目录中的示例，展示了更多的用法。

下面以查询实例接口 DescribeInstances 为例:
<dx-codeblock>
::: 简化版 php
```php
<?php
require_once '/path/to/vendor/autoload.php';

use TencentCloud\Cvm\V20170312\Models\DescribeInstancesRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;

try {
     $cred = new Credential("secretId", "secretKey");
     $client = new CvmClient($cred, "ap-guangzhou");
     $req = new DescribeInstancesRequest();
     $resp = $client->DescribeInstances($req);
     print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
     echo $e;
}
```
:::
::: 详细版 php
```php
<?php
require_once '/path/to/vendor/autoload.php';
// 导入对应产品模块的client
use TencentCloud\Cvm\V20170312\CvmClient;
// 导入要请求接口对应的Request类
use TencentCloud\Cvm\V20170312\Models\DescribeInstancesRequest;
use TencentCloud\Cvm\V20170312\Models\Filter;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

try {
     // 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
     $cred = new Credential("secretId", "secretKey");

    // 实例化一个http选项，可选的，没有特殊需求可以跳过
     $httpProfile = new HttpProfile();
     // 配置代理
     // $httpProfile->setProxy("https://ip:port");
     $httpProfile->setReqMethod("GET");  // post请求(默认为post请求)
     $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒(默认60秒)
     $httpProfile->setEndpoint("cvm.ap-shanghai.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)

    // 实例化一个client选项，可选的，没有特殊需求可以跳过
     $clientProfile = new ClientProfile();
     $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法(默认为HmacSHA256)
     $clientProfile->setHttpProfile($httpProfile);

    // 实例化要请求产品(以cvm为例)的client对象,clientProfile是可选的
     $client = new CvmClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个cvm实例信息查询请求对象,每个接口都会对应一个request对象。
     $req = new DescribeInstancesRequest();

    // 填充请求参数,这里request对象的成员变量即对应接口的入参
     // 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
     $respFilter = new Filter();  // 创建Filter对象, 以zone的维度来查询cvm实例
     $respFilter->Name = "zone";
     $respFilter->Values = ["ap-shanghai-1", "ap-shanghai-2"];
     $req->Filters = [$respFilter];  // Filters 是成员为Filter对象的列表

    // 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的
     // 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应
     $resp = $client->DescribeInstances($req);

    // 输出json格式的字符串回包
     print_r($resp->toJsonString());

    // 也可以取出单个值。
     // 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
     print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
     echo $e;
}
```
:::
</dx-codeblock>


### 更多示例

您可以在 [Github Examples](https://github.com/tencentcloud/tencentcloud-sdk-php/tree/master/examples) 目录下找到更详细的示例。

## 相关配置

### 代理

如果是有代理的环境下，需要设置系统环境变量`https_proxy`，否则可能无法正常调用，抛出连接超时的异常。 或者使用 GuzzleHttp 代理配置:

```
$cred = new Credential("secretId", "secretKey");

$httpProfile = new HttpProfile();
$httpProfile->setProxy('https://ip:port');

$clientProfile = new ClientProfile();
$clientProfile->setHttpProfile($httpProfile);

$client = new OcrClient($cred, 'ap-beijing', $this->clientProfile);
```

## 常见问题
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
</dx-accordion>


