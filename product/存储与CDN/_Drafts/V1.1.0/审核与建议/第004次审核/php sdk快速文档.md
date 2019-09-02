## 开发准备
###SDK 获取


> <font size=4 color=red> 尽量写详细一点哈，比如github获取到源码之后，如何集成到自己的工程当中。使用composer的update之类的。</font>
> by stongdong

#### github

```php
#在github中获取代码
https://github.com/tencentyun/cos-php-sdk-v5
```
#### composer

```php
#利用composer下载
{
    "require": {
        "qcloud/cos-sdk-v5": ">=1.0"
    }
}
```

## 快速入门 
```
可参照Demo程序，详见https://github.com/tencentyun/cos-php-sdk-v5/blob/master/sample.php
```
### 配置文件
```php
require(__DIR__ . DIRECTORY_SEPARATOR . 'cos-autoloader.php');

$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'appId' => getenv('COS_APPID'),
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));
```
### 上传文件

> <font size=4 color=red> 简单介绍一下上传文件需要的一些必要信息，比如bucketname和本地文件，这里有没有什么需要注意的地方。是否需要引入什么库。之类，目前内容太多代码，反而描述性的信息少了。</font>
> by stongdong

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

> <font size=4 color=red> 简单介绍一下载文件需要的一些必要信息，比如bucketname和本地文件，这里有没有什么需要注意的地方。是否需要引入什么库。之类，目前内容太多代码，反而描述性的信息少了。</font>
> by stongdong

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
