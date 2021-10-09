## 简介
PHP SDK 提供获取请求预签名 URL 接口，请求示例如下。

>?
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> 



## 永久密钥预签名请求示例

### 上传请求示例
[//]: # (.cssg-snippet-get-presign-upload-url)
```php
$secretId = "SECRETID"; //替换为您的永久密钥 SecretId
$secretKey = "SECRETKEY"; //替换为您的永久密钥 SecretKey
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
### 简单上传预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('putObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'Body' => 'string' //可为空或任意字符串
    ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 分块上传预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('uploadPart', array(
            'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
            'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
            'UploadId' => 'string',
            'PartNumber' => '1',
            'Body' => 'string'
            ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

### 下载请求示例
[//]: # (.cssg-snippet-get-presign-download-url)
```php
$secretId = "SECRETID"; //替换为您的永久密钥 SecretId
$secretKey = "SECRETKEY"; //替换为您的永久密钥 SecretKey
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $secretId,
            'secretKey' => $secretKey)));
### 简单下载预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('getObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject" //对象在存储桶中的位置，即对象键
        ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 使用封装的 getObjectUrl 获取下载签名
try {    
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即对象键
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes'); //签名的有效时间
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

## 临时密钥预签名请求示例

### 上传请求示例
[//]: # (.cssg-snippet-get-presign-sts-upload-url)
```php
$tmpSecretId = "SECRETID"; //替换为您的临时密钥 SecretId
$tmpSecretKey = "SECRETKEY"; //替换为您的临时密钥 SecretKey
$tmpToken = "COS_TOKEN"; //替换为您的临时密钥 token
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $tmpSecretId,
            'secretKey' => $tmpSecretKey,
            'token' => $tmpToken)));
### 简单上传预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('putObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'Body' => 'string'
        ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 分块上传预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('uploadPart', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'UploadId' => '',
        'PartNumber' => '1',
        'Body' => ''
        ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

### 下载请求示例
[//]: # (.cssg-snippet-get-presign-sts-download-url)
```php
$tmpSecretId = "SECRETID"; //替换为您的临时密钥 SecretId
$tmpSecretKey = "SECRETKEY"; //替换为您的临时密钥 SecretKey
$tmpToken = "COS_TOKEN"; //替换为您的临时密钥 token
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $tmpSecretId,
            'secretKey' => $tmpSecretKey,
            'token' => $tmpToken)));
### 简单下载预签名
try {
    $signedUrl = $cosClient->getPreSignedUrl('getObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject" //对象在存储桶中的位置，即对象键
    ), '+10 minutes'); //签名的有效时间
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 使用封装的 getObjectUrl 获取下载签名
try {    
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //对象在存储桶中的位置，即对象键
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes'); //签名的有效时间
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

