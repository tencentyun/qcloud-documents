## 简介

本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明

查询对象访问 URL。

#### 使用示例

#### 示例一
```php
//获取带有签名的对象下载链接
try {    
    $bucket = "examplebucket-1250000000"; //存储桶，格式：BucketName-APPID
    $key = "exampleobject";  //此处的 key 为对象键，对象键是对象在存储桶中的唯一标识
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    // 请求成功
    echo $signedUrl;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

#### 示例二

```php
//获取不带有签名的对象下载链接，用于匿名下载或分发
try {
    $bucket = 'examplebucket-125000000'; //存储桶，格式：BucketName-APPID
    $key = "exampleobject"; //此处的 key 为对象键，对象键是对象在存储桶中的唯一标识
    $Url = $cosClient -> getObjectUrlWithoutSign($bucket, $key);
    // 请求成功
    echo $Url;
} catch (\Exception $e) {
    // 请求失败
    print_r($e);
}
```

>?更多示例请查看 [预签名 URL](https://cloud.tencent.com/document/product/436/34284)。

#### 参数说明

| 参数名  | 参数描述                                                     | 类型    | 是否必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | 存储桶的名称，命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，详情请参见 [对象概述](https://cloud.tencent.com/document/product/436/13324) | String  | 是   |
| Expires | 签名几秒后失效，默认为1800秒                                  | String  | 是   |

#### 返回结果说明

方法返回值为对象访问的 URL。
