
如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

[//]: # (.cssg-snippet-put-object-sse)
```php
try {
    $result = $cosClient->putObject(array(
	        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
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
require 'vendor/autoload.php';

$secretId = "SECRETID"; //"云 API 密钥 SecretId";
$secretKey = "SECRETKEY"; //"云 API 密钥 SecretKey";
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http，SSE-C必须使用https协议
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey
        )
    )
);

$bucket = 'examplebucket-125000000'; //格式：BucketName-APPID
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
