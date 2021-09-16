如果您细心对比过 JSON PHP SDK 和 XML PHP SDK 的文档，您会发现并不是一个简单的增量更新。XML PHP SDK 不仅在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和传输性能上也做了非常大的改进。如果您想要升级到 XML PHP SDK，请参考下面的指引，完成 PHP SDK 的升级工作。

## 功能对比

下表列出了 JSON PHP SDK 和 XML PHP SDK 的主要功能对比：

| 功能       | XML PHP SDK         | JSON PHP SDK                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式<br>简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB） | 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分块上传<br>简单上传最大支持20MB<br>分块上传最大支持64GB |
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶 ACL<br>获取设置存储桶 ACL<br>删除设置存储桶 ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不单独提供接口   | 创建目录<br>查询目录<br>删除目录 |


## 升级步骤
请按照下面4个步骤升级 PHP SDK。

### 步骤1：更新 PHP SDK

有三种方式安装 COS XML PHP SDK：
* [Composer 方式](#composer)
* [Phar 方式](#phar)
* [源码方式](#sourcecode)

<span id="composer"></span>
#### Composer 方式
推荐用户使用 Composer 安装 COS XML PHP SDK，Composer 是 PHP 的依赖管理工具，允许您声明项目所需的依赖，然后自动将它们安装到您的项目中。

>? 您可以在 [Composer 官网](https://getcomposer.org/) 上找到更多关于如何安装 Composer，配置自动加载以及用于定义依赖项的其他最佳实践等相关信息。
>

使用 Composer 安装 XML PHP SDK 步骤如下：
1. 打开终端。
2. 下载 Composer，执行命令如下：
```
curl -sS https://getcomposer.org/installer | php
```
3. 创建一个名为`composer.json`的文件，内容如下：
```
{
    "require": {
        "qcloud/cos-sdk-v5": ">=2.0"
    }
}
```
4. 使用 Composer 安装，执行命令如下：
```
php composer.phar install
```
使用该命令后会在当前目录中创建一个 vendor 文件夹，里面包含 SDK 的依赖库和一个 autoload.php 脚本，方便用户在自己的项目中调用。
5. 通过 autoloader 脚本调用 XML PHP SDK。
```
require '/path/to/sdk/vendor/autoload.php';
```

至此，您的项目已经可以使用 COS XML PHP SDK 了。

<span id="phar"></span>
#### Phar 方式

Phar 方式安装 XML PHP SDK 的步骤如下：

1. 在 [Github 发布页面](https://github.com/tencentyun/cos-php-sdk-v5/releases) 下载相应的 phar 文件。
2. 在代码中引入 Phar 文件：
```
require  '/path/to/cos-sdk-v5.phar';
```

<span id="sourcecode"></span>
#### 源码方式

源码方式安装 SDK 的步骤如下：

1. 在 [Github 发布页面](https://github.com/tencentyun/cos-php-sdk-v5/releases) 下载相应的 cos-sdk-v5.tar.gz 压缩文件。
2. 解压通过 autoload.php 脚本加载 SDK。
```
require '/path/to/sdk/vendor/autoload.php';
```

### 步骤2：更改 SDK 初始化方式

在 XML PHP SDK 中，我们的初始化接口发生了一些变化，请您对应进行更改。

JSON PHP SDK 的初始化方式如下：

```php
require('cos-php-sdk-v4/include.php'); 
use Qcloud\Cos\Api;
//创建COSClientConfig对象，根据需要修改默认的配置参数
$config = array(
    'app_id' => '',
    'secret_id' => '',
    'secret_key' => '',
    'region' => 'gz',
    'timeout' => 60
);
//创建cosApi对象，实现对象存储的操作
$cosApi = new Api($config);
```

XML PHP SDK 的初始化方式如下：

```php
require '/path/to/sdk/vendor/autoload.php';
```

[//]: # (.cssg-snippet-global-init)
```php
$secretId = "SECRETID"; //"云 API 密钥 SecretId";
$secretKey = "SECRETKEY"; //"云 API 密钥 SecretKey";
$region = "COS_REGION"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
```


### 步骤3：更改存储桶名称和可用区域简称

XML PHP SDK 的存储桶名称和可用区域简称与 JSON PHP SDK 的不同，需要您进行相应的更改。

**存储桶 Bucket**
XML PHP SDK 存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。
例如`examplebucket-1250000000`，其中`examplebucket`为用户自定义字符串，`1250000000`为 APPID。

>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。您可登录腾讯云控制台， 在 [账号信息](https://console.cloud.tencent.com/developer) 查看 APPID。

**存储桶可用区域简称 Region**
XML PHP SDK 的存储桶可用区域简称发生了变化， 在初始化时，请按照下列表格填写 region 字段。

| 地域       | XML PHP SDK 地域简称         | JSON PHP SDK 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 香港       | ap-hongkong  | hk |
| 新加坡      | ap-singapore | sgp |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |


### 步骤4：更改 API
升级到 XML PHP SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。同时我们做了封装让 SDK 更加易用，具体请参考我们的示例和 [快速入门](https://cloud.tencent.com/document/product/436/12266) 文档。

API 变化有以下三点：

- **没有单独的目录接口**
在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象`project/a.txt`而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为`project/`，内容为空的对象，展示方式上模拟了传统文件夹。

 例如：上传对象`project/doc/a.txt`，分隔符`/`会模拟「文件夹」的展示方式，于是可以看到控制台上出现「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含了 a.txt 文件 。

 因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。使用场景里面有文件夹的概念，则需要提供创建文件夹的功能，您可以上传一个路径以`/ `结尾的0KB 文件。这样在您调用`GetBucket`接口时，就可以将这样的文件当做文件夹。

- **签名算法不同**
通常您不需要手动计算签名，但如果您将 SDK 的签名返回给前端使用，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。具体的算法请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

- **新增 API**
XML PHP SDK 增加了很多新的 API，包括：
 - 存储桶的操作，如 PutBucketRequest、GetBucketRequest、ListBucketRequest 等。
 - 存储桶 ACL 的操作，如 PutBucketACLRequest、GetBucketACLRequest 等。
 - 存储桶生命周期的操作，如 PutBucketLifecycleRequest、GetBucketLifecycleRequest 等。

具体请参考我们的 PHP SDK [快速入门](https://cloud.tencent.com/document/product/436/12266) 文档。



