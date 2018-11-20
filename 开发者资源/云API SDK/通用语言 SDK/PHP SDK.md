## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。目前已经支持 cvm、vpc、cbs 等产品，后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 PHP 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 PHP 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 PHP SDK 并开始调用。

## 支持 3.0 版本的产品列表

<table>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
    <td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
    <td><a href="https://cloud.tencent.com/document/api/215/15755 ">私有网络</a></td>
    <td><a href="https://cloud.tencent.com/document/api/236/15830 ">云数据库 MySQL</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/599/15880 ">批量计算</a></td>
    <td><a href="https://cloud.tencent.com/document/api/237/16144 ">云数据库 MariaDB</a></td>
    <td><a href="https://cloud.tencent.com/document/api/583/17235">无服务器云函数</a></td>
    <td><a href="https://cloud.tencent.com/document/api/557/16124 ">分布式数据库 DCDB</a></td>
  </tr>
<tr>
    <td><a href="https://cloud.tencent.com/document/api/386/18637 ">黑石物理服务器</a></td>
    <td><a href="https://cloud.tencent.com/document/api/563/16034 ">渠道合作伙伴</a></td>
    <td><a href="https://cloud.tencent.com/document/api/551/15612 ">机器翻译</a></td>
    <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
  </tr>
<tr>
    <td><a href="https://cloud.tencent.com/document/api/692/16733">Web 漏洞扫描</a></td>
    <td><a href="https://cloud.tencent.com/document/api/441/17362">智能语音服务</a></td>
    <td><a href="https://cloud.tencent.com/document/api/858/17760 ">容器实例服务</a></td>
    <td><a href="https://cloud.tencent.com/document/api/283/17741">应用安全</a></td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/869/17777">电子合同服务</a></td>
    <td><a href="https://cloud.tencent.com/document/api/656/18281">催收机器人</a></td>
    <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
    <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务 DTS</a></td>
  </tr>
    <tr>
    <td><a href="https://cloud.tencent.com/document/api/860/18448">腾讯优Mall</a></td>
    <td><a href="https://cloud.tencent.com/document/api/853/18384">腾讯优评</a></td>
    <td><a href="https://cloud.tencent.com/document/api/851/18295">智能钛机器学习</a></td>
    <td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
  </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
  <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
  <td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
  <td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/884/19310 ">智聆口语评测</a></td>
<td><a href="https://cloud.tencent.com/document/api/239/20001 ">云数据库 Redis</a></td>
<td><a href="https://cloud.tencent.com/document/api/238/19926 ">云数据库 SQL Server</a></td>
<td></td>
</tr>
  </table>


## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度，推荐使用。


## 依赖环境
1. PHP 5.6.33 版本及以上。
2. 从腾讯云 [控制台](https://console.cloud.tencent.com/) 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为 *.tencentcloudapi.com，如 CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

## 获取安装
安装 PHP SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey， SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 Composer 安装
通过 Composer 获取安装是使用 PHP SDK 的推荐方法，Composer 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Composer 详细可参考 [Composer 官网 ](https://www.phpcomposer.com/)。
1. 安装 Composer：
    windows 环境请访问 [Composer官网](https://getcomposer.org/download/) 下载安装包安装。
    unix 环境在命令行中执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
```
2. 在 composer.json 的 require 结构体中加入依赖：**注意这里的版本号只是举例,您可以在composer仓库上看到最新的版本号。**
```
"tencentcloud/tencentcloud-sdk-php": "3.0.8"
```
3. 运行 composer install 下载安装 PHP SDK。
4. 添加以下引用代码，引用方法可参考示例。
```
require 'vendor/autoload.php';
```

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-php) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-php/tencentcloud-sdk-php.zip) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 添加以下引用代码，引用方法可参考示例。
```
require_once '../TCloudAutoLoader.php';
```

## 示例
以查询可用区接口为例:
```php
<?php
require_once '../../../TCloudAutoLoader.php';
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

## 更多示例

您可以在 GitHub仓库 中 examples 目录下找到更详细的示例。

## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请到[旧版 PHP SDK](https://github.com/QcloudApi/qcloudapi-sdk-php)，但不再维护更新，推荐使用新版 SDK。
