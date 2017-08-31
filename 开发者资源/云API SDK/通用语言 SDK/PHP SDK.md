# PHP SDK
## 简介
欢迎使用腾讯云开发者工具套件（SDK）。为方便 PHP 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 PHP 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 PHP SDK 并开始调用。

## 依赖环境
1.  依赖环境：PHP 5.3.0 版本及以上
2. 从 [腾讯云控制台](https://console.qcloud.com) 开通相应产品，
3. [获取 SecretID、SecretKey](https://console.qcloud.com/capi) 以及调用地址（endpoint），endpoint 一般形式为`*.api.qcloud.com`，如CVM 的调用地址为 `cvm.api.qcloud.com`，具体参考各产品说明。
4. 下载相关资料并做好相关文件配置。

## 获取安装
安装 PHP SDK 前，先获取安全凭证。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 GitHub 获取源码安装
打开腾讯云为您提供的 PHP SDK GitHub 地址，[获取 GitHub 资源 >>](https://github.com/QcloudApi/qcloudapi-sdk-php)。
1. 在 `qcloudapi-sdk-php`的 github 地址上下载源码
2. 解压源码到您项目合适的位置
3. 配置方法可参考 Demo.java 示例配置和引用源码

### 通过 Composer  获取安装
通过  Composer 获取安装是使用 PHP SDK 的推荐方法，Composer 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Composer 详细可参考 [Composer 官网](http://www.phpcomposer.com/) 。
1. 安装 Composer
```
curl -sS https://getcomposer.org/installer | PHP
```
2. 在 composer.json 的 require 结构体中加入一行：
```
"tencentyun-api/qcloudapi-sdk-php": "dev-master"：
```
3. 运行 composer install 下载安装 PHP SDK
4. 配置方法可参考 Demo.php 示例配置和引用源码

## 入门 DEMO
以 CVM 创建（RunInstances）和查询（DescribeInstances）为例：
```
<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once './src/QcloudApi/QcloudApi.php';
$config = array('SecretId' => '你的 secretId',
'SecretKey' => '你的 secretKey',
'RequestMethod' => 'GET',
'DefaultRegion' => 'gz');
$cvm = QcloudApi::load(QcloudApi::MODULE_CVM, $config);
$package = array('offset' => 0, 'limit' => 3, 'SignatureMethod' =>'HmacSHA256');
$a = $cvm->DescribeInstances($package);
// $a = $cvm->generateUrl('DescribeInstances', $package);
if ($a === false) {
$error = $cvm->getError();
echo "Error code:" . $error->getCode() . ".\n";
echo "message:" . $error->getMessage() . ".\n";
echo "ext:" . var_export($error->getExt(), true) . ".\n";
} else {
var_dump($a);
}
echo "\nRequest :" . $cvm->getLastRequest();
echo "\nResponse :" . $cvm->getLastResponse();
echo "\n";

```