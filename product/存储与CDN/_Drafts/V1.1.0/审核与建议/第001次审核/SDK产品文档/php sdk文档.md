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

> <font size=4 color=red>  把Demo的地址附上来，可以引导用户去demo里面查看</font>
> by stongdong


##快速入门 

> <font size=4 color=red> 关键的数据appid region secretId 和 secretKey从哪里获取，要写出来，并给出链接</font>
> by stongdong


> <font size=4 color=red> 把步骤拆分一下，分成初始化配置、上传、下载等章节</font>
> by stongdong


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
