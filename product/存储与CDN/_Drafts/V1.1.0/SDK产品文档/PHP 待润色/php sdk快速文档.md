## 开发准备
### SDK 获取
#### 1. github
对象存储服务的 XML PHP SDK 资源下载地址：[XML PHP SDK](https://github.com/tencentyun/cos-php-sdk-v5 ) 。
演示示例 Demo 下载地址：[XML PHP SDK Demo](https://github.com/tencentyun/cos-php-sdk-v5/blob/master/sample.php) 。

#### 2. composer
在项目目录下，新建一个 composer.json 的文件，内容如下：
```php
{
    "require": {
        "qcloud/cos-sdk-v5": ">=1.0"
    }
}
```
然后使用下面的命令进行安装：
```
composer install
```
## 快速入门 

可参照 Demo 程序，详见 [XML PHP SDK Demo](https://github.com/tencentyun/cos-php-sdk-v5/blob/master/sample.php)。

### 配置文件
```php
#这里请填写cos-autoloader.php该文件所在的相对路径
require(__DIR__ . DIRECTORY_SEPARATOR . 'cos-autoloader.php');

$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'appId' => getenv('COS_APPID'),
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));
```
### 上传文件
使用 putObject 接口进行单文件的上传。使用 upload 接口则会自动判断文件大小，若超过阈值，则会分块上传。
* Bucket 填写上传到的存储桶的名字；
* Key 填上传到 cos 上的文件名；
* Body 填上传的文件内容。

```php
try {
    $result = $cosClient->putObject(array(
        'Bucket' => 'testbucket',
        'Key' => '11',
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
#分块上传
try {
    $result = $cosClient->upload(
                 $bucket='lewzylu02',
                 $key = '111.txt',
        $body=fopen("sample.php",'r+'));
    print_r($result);
    } catch (\Exception $e) {
    echo "$e\n";
}
```
### 下载文件
使用 getObject 接口下载文件。
```php
try {
    $result = $cosClient->getObject(array(
        'Bucket' => 'testbucket',
        'Key' => '111'));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}
```
