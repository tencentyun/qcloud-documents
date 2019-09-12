## 简介
PHP SDK 提供获取请求预签名 URL 接口。

## 永久密钥预签名请求示例

### 上传请求示例
```php
$secretId = "COS_SECRETID"; //替换为您的永久密钥 SecretId
$secretKey = "COS_SECRETKEY"; //替换为您的永久密钥 SecretKey
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
    $command = $cosClient->getCommand('putObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'Body' => '', //
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 分块上传预签名
try {
    $command = $cosClient->getCommand('uploadPart', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'UploadId' => '',
        'PartNumber' => '1',
        'Body' => '', 
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

### 下载请求示例
```php
$secretId = "COS_SECRETID"; //替换为您的永久密钥 SecretId
$secretKey = "COS_SECRETKEY"; //替换为您的永久密钥 SecretKey
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
### 简单下载预签名
try {
    $command = $cosClient->getCommand('getObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject" //对象在存储桶中的位置，即对象键
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
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
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

## 临时密钥预签名请求示例

### 上传请求示例
```php
$tmpSecretId = "COS_SECRETID"; //替换为您的临时密钥 SecretId
$tmpSecretKey = "COS_SECRETKEY"; //替换为您的临时密钥 SecretKey
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
    $command = $cosClient->getCommand('putObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'Body' => '', 
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

### 分块上传预签名
try {
    $command = $cosClient->getCommand('uploadPart', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject", //对象在存储桶中的位置，即对象键
        'UploadId' => '',
        'PartNumber' => '1',
        'Body' => '', 
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    // 请求成功
    echo ($signedUrl);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

### 下载请求示例
```php
$tmpSecretId = "COS_SECRETID"; //替换为您的临时密钥 SecretId
$tmpSecretKey = "COS_SECRETKEY"; //替换为您的临时密钥 SecretKey
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
    $command = $cosClient->getCommand('getObject', array(
        'Bucket' => "examplebucket-1250000000", //存储桶，格式：BucketName-APPID
        'Key' => "exampleobject" //对象在存储桶中的位置，即对象键
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
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
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```