## 下载与安装

#### 相关资源
- 对象存储 COS 的 XML PHP SDK 源码下载地址：[XML PHP SDK](https://github.com/tencentyun/cos-php-sdk-v5/releases)。
- SDK 快速下载地址：[XML PHP SDK](https://cos-sdk-archive-1253960454.file.myqcloud.com/cos-php-sdk-v5/latest/cos-php-sdk-v5.zip)。
- 示例 Demo 程序地址：[PHP sample](https://github.com/tencentyun/cos-php-sdk-v5/tree/master/sample)。
- SDK 文档中的所有示例代码请参见 [SDK 代码示例](https://github.com/tencentyun/cos-snippets/tree/master/php)。
- SDK 更新日志请参见 [ChangeLog](https://github.com/tencentyun/cos-php-sdk-v5/blob/master/CHANGELOG.md)。

#### 环境依赖

*   PHP 5.6+
    您可以通过`php -v`命令查看当前的 PHP 版本。
>!如果您的 PHP 版本`>=5.3` 且`<5.6` ，请使用 [ v1.3 ](https://github.com/tencentyun/cos-php-sdk-v5/tree/1.3) 版本。
-  cURL 扩展
您可以通过`php -m`命令查看 cURL 扩展是否已经安装好。
 - Ubuntu 系统中，您可以使用 apt-get 包管理器安装 PHP 的 cURL 扩展，安装命令如下：
```shell
sudo apt-get install php-curl
```
 - CentOS 系统中，您可以使用 yum 包管理器安装 PHP 的 cURL 扩展。
```shell
sudo yum install php-curl
```

#### 安装 SDK
SDK 安装有三种方式：[Composer 方式](#composer)、[Phar 方式](#phar) 和 [源码方式](#Source)。

<span id="composer"></span>
#### Composer 方式
推荐使用 Composer 安装 cos-php-sdk-v5，Composer 是 PHP 的依赖管理工具，允许您声明项目所需的依赖，然后自动将它们安装到您的项目中。
>?您可以在 [Composer 官网](https://getcomposer.org/) 上找到更多关于如何安装 Composer，配置自动加载以及用于定义依赖项的其他最佳实践等相关信息。

**安装步骤**
1. 打开终端。
2. 下载 Composer，执行以下命令。
```shell
curl -sS https://getcomposer.org/installer | php
```
3. 创建一个名为`composer.json`的文件，内容如下。
```json
{
    "require": {
        "qcloud/cos-sdk-v5": ">=2.0"
    }
}
```
4. 使用 Composer 安装，执行以下命令。
```shell
php composer.phar install
```
使用该命令后会在当前目录中创建一个 vendor 文件夹，里面包含 SDK 的依赖库和一个 autoload.php 脚本，方便在项目中调用。
5. 通过 autoloader 脚本调用 cos-php-sdk-v5。
```php
require '/path/to/sdk/vendor/autoload.php';
```
至此，您的项目已经可以使用 COS XML PHP SDK 了。

<span id="phar"></span>
#### Phar 方式
Phar 方式安装 SDK 的步骤如下：
1. 在 [GitHub 发布页面](https://github.com/tencentyun/cos-php-sdk-v5/releases) 下载相应的 phar 文件。
2.  在代码中引入 phar 文件：

```php
require  '/path/to/cos-sdk-v5.phar';
```

<span id="Source"></span>
#### 源码方式
源码方式安装 SDK 的步骤如下：
1.  在 [ SDK 下载页面](https://github.com/tencentyun/cos-php-sdk-v5/releases) 下载`cos-sdk-v5.tar.gz`压缩文件。
>!`Source code`压缩包为 Github 默认打包的代码包，里面不包含`vendor`目录。
2.  解压后通过 `autoload.php` 脚本加载 SDK：

```php
require '/path/to/sdk/vendor/autoload.php';
```


## 开始使用
下面为您介绍如何使用 COS PHP SDK 完成一个基础操作，如初始化客户端、创建存储桶、查询存储桶列表、上传对象、查询对象列表、下载对象和删除对象。

### 初始化

[//]: # (.cssg-snippet-global-init)
```php
$secretId = "COS_SECRETID"; //"云 API 密钥 SecretId";
$secretKey = "COS_SECRETKEY"; //"云 API 密钥 SecretKey";
$region = "COS_REGION"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
```

若您使用 [临时密钥](https://cloud.tencent.com/document/product/436/14048) 初始化，请用下面方式创建实例。

[//]: # (.cssg-snippet-global-init-sts)
```php
$tmpSecretId = "COS_SECRETID"; //"临时密钥 SecretId";
$tmpSecretKey = "COS_SECRETKEY"; //"临时密钥 SecretKey";
$tmpToken = "COS_TOKEN"; //"临时密钥 token";
$region = "COS_REGION"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $tmpSecretId,
            'secretKey' => $tmpSecretKey,
            'token' => $tmpToken)));
```

### 创建存储桶

[//]: # (.cssg-snippet-put-bucket)
```php
try {
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $result = $cosClient->createBucket(array('Bucket' => $bucket));
    //请求成功
    print_r($result);
} catch (\Exception $e) {
    //请求失败
    echo($e);
}
```

### 查询存储桶列表

[//]: # (.cssg-snippet-get-service)
```php
try {
    //请求成功
    $result = $cosClient->listBuckets();
    print_r($result);
} catch (\Exception $e) {
    //请求失败
    echo($e);
}
```


### 上传对象
>!
* 使用 putObject 接口上传文件（最大5G）。
* 使用 Upload 接口分块上传文件，Upload 接口为复合上传接口，对小文件进行简单上传，对大文件进行分块上传。
* 参数说明可参见 [对象操作](https://cloud.tencent.com/document/product/436/34282#.E7.AE.80.E5.8D.95.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1) 文档。

[//]: # (.cssg-snippet-put-object-comp)
```php
# 上传文件
## putObject(上传接口，最大支持上传5G文件)
### 上传内存中的字符串
try {
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $key = "exampleobject";
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 上传文件流
try {
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $key = "exampleobject";
    $srcPath = "path/to/localFile";//本地文件绝对路径
    $file = fopen($srcPath, "rb");
    if ($file) {
        $result = $cosClient->putObject(array(
            'Bucket' => $bucket,
            'Key' => $key,
            'Body' => $file));
        print_r($result);
    }
} catch (\Exception $e) {
    echo "$e\n";
}

## Upload(高级上传接口，默认使用分块上传最大支持50T)
### 上传内存中的字符串
try {    
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $key = "exampleobject";
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = 'Hello World!');
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 上传文件流
try {    
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $key = "exampleobject";
    $srcPath = "path/to/localFile";//本地文件绝对路径
    $file = fopen($srcPath, 'rb');
    if ($file) {
        $result = $cosClient->Upload(
            $bucket = $bucket,
            $key = $key,
            $body = $file);
    }
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

### 查询对象列表

[//]: # (.cssg-snippet-get-bucket)
```php
try {
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $result = $cosClient->listObjects(array(
        'Bucket' => $bucket
    ));
    // 请求成功
    if (isset($result['Contents'])) {
        foreach ($result['Contents'] as $rt) {
            print_r($rt);
        }
    }
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

单次调用`listObjects`接口一次只能查询1000个对象，如需要查询所有的对象，则需要循环调用。

[//]: # (.cssg-snippet-get-bucket-recursive)
```php
try {
    $bucket = "examplebucket-1250000000"; //存储桶名称 格式：BucketName-APPID
    $prefix = ''; //列出对象的前缀
    $marker = ''; //上次列出对象的断点
    while (true) {
        $result = $cosClient->listObjects(array(
            'Bucket' => $bucket,
            'Marker' => $marker,
            'MaxKeys' => 1000 //设置单次查询打印的最大数量，最大为1000
        ));
        if (isset($result['Contents'])) {
            foreach ($result['Contents'] as $rt) {
                // 打印key
                echo($rt['Key'] . "\n");
            }
        }
        $marker = $result['NextMarker']; //设置新的断点
        if (!$result['IsTruncated']) {
            break; //判断是否已经查询完
        }
    }
} catch (\Exception $e) {
    echo($e);
}
```

### 下载对象
* 使用 getObject 接口下载文件。
* 使用 getObjectUrl 接口获取文件下载 URL。

[//]: # (.cssg-snippet-get-object-comp)
```php
# 下载文件
## getObject(下载文件)
### 下载到内存
try {
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即称对象键
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key));
    // 请求成功
    echo($result['Body']);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}

### 下载到本地
try {
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即称对象键
    $localPath = @"path/to/localFile";//下载到本地指定路径
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'SaveAs' => $localPath));
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}

### 指定下载范围
/*
 * Range 字段格式为 'bytes=a-b'
 */
try {
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即称对象键
    $localPath = @"path/to/localFile";//下载到本地指定路径
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Range' => 'bytes=0-10',
        'SaveAs' => $localPath));
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}

## getObjectUrl(获取文件 UrL)
try {    
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即称对象键
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

### 删除对象

[//]: # (.cssg-snippet-delete-object-comp)
```php
# 删除 object
## deleteObject
try {
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即称对象键
    $result = $cosClient->deleteObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'VersionId' => 'string'
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
# 删除多个 object
## deleteObjects
try {
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key1 = "exampleobject1"; //对象在存储桶中的位置，即称对象键
    $key2 = "exampleobject2"; //对象在存储桶中的位置，即称对象键
    $result = $cosClient->deleteObjects(array(
        'Bucket' => $bucket,
        'Objects' => array(
            array(
                'Key' => $key1,
            ),
            array(
                'Key' => $key2,
            ),
            //...
        ),
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```
