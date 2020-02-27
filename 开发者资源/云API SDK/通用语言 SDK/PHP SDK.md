## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0是云 API 3.0平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会陆续接入。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同和返回包格式相同等优点。
为方便 PHP 开发者调试和接入腾讯云产品 API，本文主要介绍适用于 PHP 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让您快速获取腾讯云 PHP SDK 并开始调用。

## 支持3.0版本的产品列表

SDK 3.0支持全部 API 3.0下的产品，本列表可能滞后于实际代码，如有疑问请咨询具体的产品。

<table>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
<td><a href="https://cloud.tencent.com/document/api/457/31853">容器服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/858/17761">容器实例服务</a></td>
</tr>
<tr>
 <td><a href="https://cloud.tencent.com/document/api/377/20423">弹性伸缩</a></td>
  <td><a href="https://cloud.tencent.com/document/api/583/17235">云函数</a></td>
  <td><a href="https://cloud.tencent.com/document/api/599/15880">批量计算</a></td>
  <td><a href="https://cloud.tencent.com/document/api/214/30667">负载均衡</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15755">私有网络</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
  <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务 DTS</a></td>
 <td><a href="https://cloud.tencent.com/document/api/236/15830">云数据库 MySQL</a></td>
 <td><a href="https://cloud.tencent.com/document/api/239/20002">云数据库 Redis</a></td>
 <td><a href="https://cloud.tencent.com/document/api/240/31797">云数据库 MongoDB</a></td>
 </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/237/16144">云数据库 MariaDB</a></td>
<td><a href="https://cloud.tencent.com/document/api/557/16124">分布式数据库 TDSQL</a></td>
 <td><a href="https://cloud.tencent.com/document/api/238/19927">云数据库 SQL Server</a></td>
  <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
   <td><a href="https://cloud.tencent.com/document/product/1130/39547">数据库智能管家 DBbrain</a></td>
   </tr>
   <tr>     
   <td><a href="https://cloud.tencent.com/document/product/596/39648">游戏数据库 TcaplusDB</a></td>
  <td><a href="https://cloud.tencent.com/document/api/692/16733">漏洞扫描服务</a></td>
   <td><a href="https://cloud.tencent.com/document/api/283/17742">移动应用安全</a></td>
   <td><a href="https://cloud.tencent.com/document/api/266/31753">云点播</a></td>
     <td><a href="https://cloud.tencent.com/document/api/267/20456">云直播</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/1073/37986">语音合成</a></td>
<td><a href="https://cloud.tencent.com/document/api/1093/35637">语音识别</a></td>
 <td><a href="https://cloud.tencent.com/document/api/551/15612">机器翻译</a></td>
<td><a href="https://cloud.tencent.com/document/api/656/18281">催收机器人</a></td>
<td><a href="https://cloud.tencent.com/document/api/884/19310">智聆口语评测</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/1122/40639">企业收付平台</a></td>
  <td><a href="https://cloud.tencent.com/document/api/845/30620">Elasticsearch Service</a></td>
<td><a href="https://cloud.tencent.com/document/api/382/38764">短信</a></td>
<td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
<td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
 </tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/248/30343">云监控</a></td>
 <td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
<td><a href="https://cloud.tencent.com/document/api/869/17778">电子合同服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
 <td><a href="https://cloud.tencent.com/document/api/563/16034">渠道合作伙伴</a></td>
  </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/1007/31320">人脸核身-云智慧眼</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1013/31737">威胁情报云查</a></td>
 <td><a href="https://cloud.tencent.com/document/api/647/37078">实时音视频</a></td>
   <td><a href="https://cloud.tencent.com/document/api/670/31052">人脸融合</a></td>
    <td><a href="https://cloud.tencent.com/document/api/867/32770">人脸识别</a></td>
   </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/1004/30607">数学作业批改</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1000/30698">数字版权管理</a></td>
   <td><a href="https://cloud.tencent.com/document/api/866/33515">文字识别</a></td>
   <td><a href="https://cloud.tencent.com/document/api/649/36037">腾讯微服务平台 TSF</a></td>
   <td><a href="https://cloud.tencent.com/document/api/597/40823">消息队列 CKafka</a></td>
   </tr>
  <tr>   
   <td><a href="https://cloud.tencent.com/document/api/228/30974">内容分发网络</a></td>
<td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
     </tr>
  </table>



## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度。


## 依赖环境
- PHP 5.6.33 版本及以上。
- 从腾讯云 [控制台](https://console.cloud.tencent.com/) 开通相应产品。
- 获取 SecretID、SecretKey 以及调用地址（endpoint）。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 必须严格保管，避免泄露**。
 - endpoint 一般形式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各产品说明。

## 获取安装

### 通过 Composer 安装（推荐）
[Composer](https://www.phpcomposer.com) 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 安装 Composer。
 - Windows 环境：请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包并进行安装。
 - UNIX 环境：执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
```
2. 在 composer.json 的 require 结构体中加入依赖。
>!**以下版本号仅为示例，请替换成 Composer 仓库上查看到最新的版本号。**
>
```
"tencentcloud/tencentcloud-sdk-php": "3.0.*"
```
3. 运行 composer install 下载安装 PHP SDK。
4. 添加以下引用代码，引用方法可参考 [示例](#example)。
```
require 'vendor/autoload.php';
```

### 通过源码包安装
1. 下载源码压缩包：
 - **方法一**：通过 git clone 下载源码。
 ```
git clone https://github.com/tencentcloud/tencentcloud-sdk-php
```
 - **方法二**：访问 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-php/tencentcloud-sdk-php.zip) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 添加以下引用代码，引用方法可参考 [示例](#example)。
```
require_once '../TCloudAutoLoader.php';
```

<span id="example"></span>
## 示例
以查询可用区接口为例:
```php
<?php
require_once '../../../TCloudAutoLoader.php';
// 导入对应产品模块的 client
use TencentCloud\Cvm\V20170312\CvmClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Cvm\V20170312\Models\DescribeZonesRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
try {
    // 实例化一个证书对象，入参需要传入腾讯云账户 SecretID，SecretKey
    $cred = new Credential("secretId", "secretKey");

    // 实例化要请求产品(以 CVM 为例)的 client 对象
    $client = new CvmClient($cred, "ap-guangzhou");

    // 实例化一个请求对象
    $req = new DescribeZonesRequest();

    // 通过 client 对象调用想要访问的接口，需要传入请求对象
    $resp = $client->DescribeZones($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

## 更多示例

您可以在 GitHub 仓库中 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-php/tree/master/examples) 下找到更详细的示例。

## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请参考 [旧版 PHP SDK](https://github.com/QcloudApi/qcloudapi-sdk-php)，但不再维护更新，推荐使用新版 SDK。
