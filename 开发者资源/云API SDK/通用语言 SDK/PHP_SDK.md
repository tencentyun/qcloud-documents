## 简介

* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式。
* 本文以 PHP SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* PHP 5.6.33 版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/78145f9e6a830a188304991552a5c614.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的API文档。


## 步骤1：搭建所需环境 (可选)

如果您已经在本地部署了 PHP 环境，可忽略此步骤。

### 配置语言环境

1. 官网下载 [PHP 5.6.33](https://windows.php.net/downloads/releases/archives/) 安装包。本文是 windows10 X64 系统，因此选择 php-5.6.33-Win32-VC11-x64.zip版本。
2. 解压到指定文件夹，这里以`F:\software\language\PHP`为例。
3. 配置环境变量。进入【我的电脑】>【属性】>【高级系统设置】>【环境变量】。双击【系统变量】中的【Path】，添加`F:\software\language\PHP`。
4. 验证环境变量是否安装成功。打开“命令行窗口”，输入命令`php -v`，如下图所示，则安装 PHP 环境成功。 
![](https://main.qcloudimg.com/raw/02879376f1e5025b2b016bd114671886.png)

#### 配置 PHP

复制`F:\software\language\PHP\php.ini-development`并重命名为`php.ini`，修改如下内容：

* 去掉 **extension=php_openssl.dll** 前面的分号（**;**）。
![](https://main.qcloudimg.com/raw/de34c465888b9b1659d1a8550943c1a2.png)
- 将 extension_dir = "ext" 改为 extension_dir = "F:/software/language/PHP/ext"，实际情况以您 PHP 安装路径为准。
![](https://main.qcloudimg.com/raw/55d950c0563a1d33fb37d772a297b349.png)

### 安装 Apache 服务器

这里以2.4.43版本 Windows 安装为例。

#### 下载

1. [官网](http://httpd.apache.org/download.cgi) 下载 Apache。
![](https://main.qcloudimg.com/raw/0cb567580c3f5da19cd827e49bfaa8d8.png)

2. 选择 ApacheHaus。
![](https://main.qcloudimg.com/raw/73e25f43f1dc9d75c08d12df95d25aa7.png)

3. 根据系统选择对应的版本（本文选择64位的），开始下载。 
![](https://main.qcloudimg.com/raw/5bd6e4a58095436dfc8b01f20fe44452.png)

#### 安装

1. 解压 httpd-2.4.43-o111g-x64-vc15.zip，得到如下文件夹。 
![](https://main.qcloudimg.com/raw/32a24b35e729316cd903fd634579d97e.png)
2. readme_first.html 文件里面详细说明了安装步骤和方式，大致如下：
   1. 用管理员身份打开 Windows 命令窗口并 cd 到 \Apache24\bin（该路径是指 Apache 的解压路径）目录，执行命令：
```
httpd.exe
```
因为本文 Apache 存放的路径**不是默认路径**，执行会报错，此时需要在配置文件里将路径改为正确路径，即可执行成功：

	打开 Apache 安装地址：Apache24\conf\httpd.conf 文件，搜索 Define SRVROOT（只有一处），将其后面的双引号内的路径改为 Apache 的**实际解压路径后保存即可，注意此处保存的地址是“/”**。

	本文的示例地址为：F:\software\language\system\Apache\Apache24。
![](https://main.qcloudimg.com/raw/99be20d788929c0a5f2a4a7dce23bb70.png)  

 2. 打开浏览器访问：http://localhost/，显示如下内容，则访问成功。
![](https://main.qcloudimg.com/raw/1392870853060e4c9fed5f43df101faa.png) 
 3. 在前面打开的命令窗口输入 **Ctrl+C** 即可关闭服务器。
 4. 将 Apache 安装到系统服务，执行以下命令： 
```
httpd -k install
```
为了方便，可以将 httpd 命令加到环境变量中使其全局生效：【我的电脑】>【属性】>【高级系统设置】>【环境变量】>【系统变量】>【Path】，编辑 Path，将 F:\software\language\system\Apache\Apache24\bin 路径加到后面。 
 5. 启动服务器：httpd -k start，打开浏览器访问：http://localhost/ 测试是否启动成功。您还可以找到 bin 目录下的 ApacheMonitor.exe，通过双击来打开、关闭或重启服务器。除了启动命令，还有其他的命令：
```
     (命令均需要用管理员身份打开 cmd 窗口下执行)
     关闭 Apache        httpd -k stop
     重启 Apache        httpd -k restart
     卸载 Apache        httpd -k uninstall
     查看 Apache 版本     httpd -V
     命令帮助           httpd -h
```

### Apache 支持 PHP

#### 添加 PHP 模块

在 Apache 配置文件`F:\software\language\system\Apache\Apache24\conf\httpd.conf`中（`#LoadModule xxx`后）添加(注意此处为正斜杠“/”，此处路径仅作为示范，请以实际路径为准)：
```
PHPIniDir "F:/software/language/PHP"
LoadModule php5_module "F:/software/language/PHP/php5apache2_4.dll"
```
#### 添加 PHP 文件后缀

在 Apache 配置文件`F:\software\language\system\Apache\Apache24\conf\httpd.conf`，即：

```php+HTML
<IfModule mime_module>
	TypesConfig conf/mime.types
		....
</IfModule>
```

中，添加`AddType application/x-httpd-php .php`，即：

```
<IfModule mime_module>
	TypesConfig conf/mime.types
	....
	AddType application/x-httpd-php .php
</IfModule>
```

#### 添加主页 index.php

在 Apache 配置文件`F:\software\language\system\Apache\Apache24\conf\httpd.conf`，即：

```
<IfModule dir_module>
	DirectoryIndex index.html
</IfModule>
```

中，在`index.html`前添加`index.php`，即：

```
<IfModule dir_module>
	DirectoryIndex index.php index.html
</IfModule>
```

#### 测试效果

在`F:\software\language\system\Apache\Apache24\htdocs`下创建“index.php”，代码为：

```php
<?php
	{
		echo "php hello world";
	};
?>
```

重启 Apache（管理员身份运行 CMD，输入`httpd -k restart`），浏览器访问`localhost`，看到 php hello world 即为配置成功。

### Composer 介绍与安装

Composer 是 PHP 的一个依赖管理工具。我们可以在项目中声明所依赖的外部工具库，Composer 会帮您安装这些依赖的库文件，有了 Composer，我们就可以很轻松的使用一个命令将其他代码引用到我们的项目中来。

> ?
>
> * Composer 默认情况下不是全局安装，而是基于指定的项目的某个目录中（例如 vendor）进行安装。
> * Composer 需要 PHP 5.3.2+ 以上版本，且需要开启 openssl，上文已介绍开启方法。
> * Composer 可运行在 Windows、Linux 以及 OSX 平台上。

1. 下载 [composer 官网](https://getcomposer.org/download/) 的 exe 可执行文件。
![](https://main.qcloudimg.com/raw/d10fb280ddd5d2a8c6a1570f9fd979b8.png)
2. 安装时，需要注意的是：
    * 在安装过程中，下面地址如果不是 php.exe（PHP 语言文件的根路径下）的地址，需要手动调整为 php.exe 文件所在的地址。 
    ![img](https://main.qcloudimg.com/raw/c19a53c66568ae122ba8e2852cb76eac.png)
	* 如果出现下面的情况，说明防火墙阻止了非中国大陆地区服务器的文件。
![](https://main.qcloudimg.com/raw/fe3e892536cbcf3d49217e7114239075.png)
	* 验证 composer 是否安装成功，在打开的命令窗口执行`composer -V`，如下图所示，即安装成功。
	![](https://main.qcloudimg.com/raw/c9be45720b8b6833972fcd4e104a454a.png)

## 步骤2：安装 PHP SDK 3.0

中国大陆地区的用户可以使用国内镜像源提高下载速度，在打开的命令窗口执行以下命令，更改 Packagist 为国内镜像：

```
composer config -g repo.packagist composer https://packagist.phpcomposer.com
```

在打开的命令窗口执行命令安装 SDK（安装到指定位置），例如安装到`C:\Users\···>`目录下，则在指定的位置打开命令窗口，并执行以下命令：

```
composer require tencentcloud/tencentcloud-sdk-php
```

如下图所示，即安装 SDK 成功。
![](https://main.qcloudimg.com/raw/e8948ce3e75f37d10236f5f32ad558da.png)

## 步骤3：获取凭证与调用地址

### 获取安全凭证

安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取。

>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**

### 获取调用地址

调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，详情请参见各产品下的“请求结构”文档。例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。

## 步骤4：使用 SDK

在代码中添加以下引用代码。示例中仅为参考，composer 会在项目根目录下生成 vendor 目录，`/path/to/`为项目根目录的实际绝对路径，如果是在当前目录执行，可以省略绝对路径。

```
require '/path/to/vendor/autoload.php'; 
```

您还可以将以下示例放入`F:\software\language\system\Apache\Apache24\htdocs`中，启动 Apache 服务，通过浏览器访问`http://localhost/DescribeZones.php`或`http://localhost/DescribeInstances.php`。

### 示例1：查看可用区列表

创建一个 DescribeZones.php 文件（需要将密钥等信息更换为真实值）：

```php
<?php
require_once '/path/to/vendor/autoload.php'; 
use TencentCloud\Cvm\V20170312\CvmClient;
use TencentCloud\Cvm\V20170312\Models\DescribeZonesRequest;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;

try {
    $cred = new Credential("secretId", "secretKey");

    $client = new CvmClient($cred, "ap-guangzhou");

    $req = new DescribeZonesRequest();

    $resp = $client->DescribeZones($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

在命令端进入到 DescribeZones.php 文件所在的目录下，执行`php DescribeZones.php`即可获取数据。

### 示例2：查看实例列表

创建一个 DescribeInstances.php 文件（需要将密钥等信息更换为真实值）。

```php
<?php
require_once '/path/to/vendor/autoload.php'; 
// 导入对应产品模块的 client
use TencentCloud\Cvm\V20170312\CvmClient;
// 导入要请求接口对应的 Request 类
use TencentCloud\Cvm\V20170312\Models\DescribeInstancesRequest;
use TencentCloud\Cvm\V20170312\Models\Filter;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Common\Credential;
// 导入可选配置类
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;

try {
    // 实例化一个证书对象，入参需要传入腾讯云账户 secretId，secretKey
    //$cred = new Credential("secretId", "secretKey");
    $cred = new Credential(getenv("TENCENTCLOUD_SECRET_ID"), getenv("TENCENTCLOUD_SECRET_KEY"));

    // 实例化一个 http 选项，可选的，没有特殊需求可以跳过
    $httpProfile = new HttpProfile();
    $httpProfile->setReqMethod("GET");  // post 请求 (默认为 post 请求)
    $httpProfile->setReqTimeout(30);    // 请求超时时间，单位为秒 (默认60秒)
    $httpProfile->setEndpoint("cvm.ap-shanghai.tencentcloudapi.com");  // 指定接入地域域名 (默认就近接入)

    // 实例化一个 client 选项，可选的，没有特殊需求可以跳过
    $clientProfile = new ClientProfile();
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  // 指定签名算法 (默认为 HmacSHA256)
    $clientProfile->setHttpProfile($httpProfile);

    // 实例化要请求产品 (以 cvm 为例) 的 client 对象, clientProfile 是可选的
    $client = new CvmClient($cred, "ap-shanghai", $clientProfile);

    // 实例化一个 cvm 实例信息查询请求对象,每个接口都会对应一个 request 对象。
    $req = new DescribeInstancesRequest();

    // 填充请求参数,这里 request 对象的成员变量即对应接口的入参
    // 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
    $respFilter = new Filter();  // 创建 Filter 对象, 以 zone 的维度来查询 cvm 实例
    $respFilter->Name = "zone";
    $respFilter->Values = ["ap-shanghai-1", "ap-shanghai-2"];
    $req->Filters = [$respFilter];  // Filters 是成员为 Filter 对象的列表

    // 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的
    // 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应
    $resp = $client->DescribeInstances($req);

    // 输出 json 格式的字符串回包
    print_r($resp->toJsonString());

    // 也可以取出单个值。
    // 您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
    print_r($resp->TotalCount);
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

在命令端进入到 DescribeInstances.php 文件所在的目录下，执行 php DescribeInstances.php 即可获取数据。

### 更多示例

您可以在 [github examples](https://github.com/tencentcloud/tencentcloud-sdk-php/tree/master/examples) 目录下找到更详细的示例。

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

### 证书问题

如果您的 PHP 环境证书有问题，可能会遇到报错，类似于`cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html`，请尝试按以下步骤解决：

1. 到 https://curl.haxx.se/ca/cacert.pem 下载证书文件`cacert.pem`，将其保存到 PHP 安装路径下。
2. 编辑`php.ini`文件，删除`curl.cainfo`配置项前的分号注释符（;），值设置为保存的证书文件`cacert.pem`的绝对路径。
3. 重启依赖 PHP 的服务。

### php_curl 扩展

此 SDK 依赖的 GuzzleHttp 需要开启 php_curl 扩展，查看环境上的 php.ini 环境确认是否已启用，例如在 Linux 环境下，PHP 7.1 版本，托管在 apache 下的服务，可以打开 /etc/php/7.1/apache2/php.ini，查看 extension=php_curl.dll 配置项是否已被注释，请删除此项配置前的注释符并重启 apache。

### Web 访问异常

命令行下执行正常，但是放在 Web 服务器执行则报错：

cURL error 0: The cURL request was retried 3 times and did not succeed. The most likely reason for the failure is that cURL was unable to rewind the body of the request and subsequent retries resulted in the same error. Turn on the debug option to see what went wrong. See https://bugs.php.net/bug.php?id=47204 for more information. (see http://curl.haxx.se/libcurl/c/libcurl-errors.html)

此问题出现情况不一。可以运行`php -r "echo sys_get_temp_dir();"`，打印系统默认临时目录绝对路径，然后在`php.ini`配置`sys_temp_dir`为这个值，尝试是否能解决。

### 源码安装问题

为了支持部分源码安装的需要，我们将依赖的包文件放在 vendor 目录中，又考虑到不能造成对 composer 的不兼容，github 不得不设置禁止导出 vendor 目录，造成必须使用`git clone`命令才能拿到 vendor 目录的情况，对一些不熟悉 github 的用户造成了困扰。从3.0.188版本开始，我们暂时移除了源码安装，必须使用 composer 安装 SDK 和依赖的包。
