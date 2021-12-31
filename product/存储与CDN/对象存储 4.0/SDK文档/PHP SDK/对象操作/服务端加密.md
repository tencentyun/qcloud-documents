
如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

[//]: # (.cssg-snippet-put-object-sse)
```php
try {
    $result = $cosClient->putObject(array(
	        'Bucket' => 'examplebucket-125000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
	        'Key' => 'exampleobject'
	        'Body' => 'string',
	        'ServerSideEncryption' => 'AES256',	//SSE-COS加密
	    ),
	);
    print_r ($result);
} catch (Qcloud\Cos\Exception\ServiceResponseException $e) {
    echo $e;
}
```

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。SDK 通过在上传时设置 `SSE` 相关头部字段来完成。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- customerKey：用户提供的密钥，传入一个32字节的字符串，支持数字、字母、字符的组合，不支持中文。
>- 如果上传的源文件调用了该方法，那么在使用 GET（下载）、HEAD（查询）时对源对象操作的时候也要调用该方法。

[//]: # (.cssg-snippet-put-object-sse-c)
```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
            
$bucket = 'examplebucket-125000000'; //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
$key = 'exampleobject';
try {
    $customerKey = 'abcdefghijklmnopqrstuvwxyz123456'; //32字节的字符串，支持数字、字母、字符的组合，不支持中文
    $SSECustomerKey = base64_encode($customerKey);
    $SSECustomerKeyMd5 = base64_encode(md5($customerKey, true));
    $result = $cosClient->putObject(array(
            'Bucket' => $bucket, 
            'Key' => $key,
            'Body' => 'string',
            'SSECustomerAlgorithm' => 'AES256',
            'SSECustomerKey' => $SSECustomerKey,
            'SSECustomerKeyMD5' => $SSECustomerKeyMd5,
        )); 
    print_r ($result);
} catch (Qcloud\Cos\Exception\ServiceResponseException $e) {
    echo $e; 
}
```
