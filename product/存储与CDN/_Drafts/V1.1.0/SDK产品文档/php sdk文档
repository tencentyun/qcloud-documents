##开发准备
###SDK 获取
####github
在github中获取代码
```php
https://github.com/tencentyun/cos-php-sdk-v5
```
####composer
利用composer下载

```php
{
    "require": {
        "qcloud/cos-sdk-v5": ">=1.0"
    }
}
```
##快速入门 
```php
require(__DIR__ . DIRECTORY_SEPARATOR . 'cos-autoloader.php');
#配置文件
$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'appId' => getenv('COS_APPID'),
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));

#上传文件
try {
    $result = $cosClient->putObject(array(
        'Bucket' => 'testbucket',
        'Key' => '11',
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

#下载文件
try {
    $result = $cosClient->getObject(array(
        'Bucket' => 'testbucket',
        'Key' => '111'));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}
```
