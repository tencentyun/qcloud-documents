## 简介

本文档提供关于存储桶的基本操作和访问控制列表（ACL）的相关 API 概览以及 SDK 示例代码。

**基本操作**

| API                                                          | 操作名             | 操作描述                           |
| ------------------------------------------------------------ | ------------------ | ---------------------------------- |
| [GET Service](https://cloud.tencent.com/document/product/436/8291) | 查询存储桶列表     | 查询指定账号下所有的存储桶列表     |
| [PUT Bucket](https://cloud.tencent.com/document/product/436/7738) | 创建存储桶         | 在指定账号下创建一个存储桶         |
| [HEAD Bucket](https://cloud.tencent.com/document/product/436/7735) | 检索存储桶及其权限 | 检索存储桶是否存在且是否有权限访问 |
| [DELETE Bucket](https://cloud.tencent.com/document/product/436/7732) | 删除存储桶         | 删除指定账号下的空存储桶           |

**访问控制列表（ACL）**

| API                                                          | 操作名         | 操作描述              |
| ------------------------------------------------------------ | -------------- | --------------------- |
| [PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737) | 设置存储桶 ACL | 设置指定存储桶的访问权限控制列表（ACL） |
| [GET Bucket acl](https://cloud.tencent.com/document/product/436/7733) | 查询存储桶 ACL | 获取指定存储桶的访问权限控制列表（ACL） |

## 基本操作

### 查询存储桶列表

#### 功能说明

查询指定账号下所有存储桶列表（GET Service）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model listBucket(array $args = array())
```

#### 请求示例

```php
//查询 bucket 列表
try {
    $result = $cosClient->listBuckets();
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```


#### 返回结果示例
```php
Array
(
    [data:protected] => Array
        (
            [Owner] => Array
                (
                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                    [DisplayName] => 100000000001
                )

            [Buckets] => Array
                (
                    [0] => Array
                        (
                            [Name] => examplebucket-1250000000
                            [Location] => ap-beijing
                            [CreationDate] => 2016-07-29T03:09:54Z
                        )

                    [1] => Array
                        (
                            [Name] => examplebucket2-1250000000
                            [Location] => ap-beijing
                            [CreationDate] => 2017-08-02T04:00:24Z
                        )

                )

            [RequestId] => NWE3YzgxZmFfYWZhYzM1MGFfMzc3MF9iOGY5OQ==
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Owner | Array | 存储桶所有者信息                         | 无 |
| ID | String | 存储桶所有者 ID                         | Owner |
| DisplayName | String | 存储桶所有者的名字信息         | Owner |
| Buckets | Array | 存储桶列表                     | 无 |
| Bucket | Array | 存储桶信息                     | Buckets |
| Name | String | 存储桶名称                         | Bucket |
| Location | String | 存储桶所在的地域名               | Bucket  |
| CreationDate | String | 存储桶创建的时间             | Bucket  |


### 创建存储桶

#### 功能说明

在指定账号下创建一个存储桶（PUT Bucket）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model createBucket(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->createBucket(array(
        'Bucket' => 'examplebucket-1250000000' //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |


### 检索存储桶及其权限

#### 功能说明

确认 Bucket 是否存在且是否有权限访问（HEAD Bucket）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model headBucket(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->headBucket(array(
        'Bucket' => 'examplebucket-1250000000' //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |


### 删除存储桶

#### 功能说明

删除指定账号下的空存储桶。

#### 方法原型

```php
public Guzzle\Service\Resource\Model deleteBucket(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->deleteBucket(array(
        'Bucket' => 'examplebucket-1250000000' //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |

## 访问控制列表

### 设置存储桶 ACL

#### 功能说明

设置指定存储桶的访问权限控制列表（ACL）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model putBucketAcl(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->putBucketAcl(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'ACL' => 'private',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/100000000001:uin/100000000001',
                    'ID' => 'qcs::cam::uin/100000000001:uin/100000000001',
                    'Type' => 'CanonicalUser',
                ),  
                'Permission' => 'FULL_CONTROL',
            ),  
            // ... repeated
        ),  
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/100000000001:uin/100000000001',
            'ID' => 'qcs::cam::uin/100000000001:uin/100000000001',
        )));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| Grants | Array | ACL权限列表                         | 无 |
| Grant | Array | ACL权限信息         | Grants |
| Grantee | Array | ACL权限信息                     | Grant |
| Type | String | 所有者权限类型        | Grantee  |
| Permission | String | 权限类型，可选值： FULL_CONTROL 、 WRITE 、 READ | Grant  |
| ACL | String | 整体权限类型，可选值：private 、 public-read 、public-read-write | 无 |
| Owner | String | 存储桶所有者信息        | 无  |
| DisplayName | String | 权限所有者的名字信息      | Grantee/Owner |
| ID | String | 权限所有者 ID              | Grantee/Owner |



### 查询存储桶 ACL

#### 功能说明

获取指定存储桶的访问权限控制列表（ACL）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model getBucketAcl(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->getBucketAcl(array(
        'Bucket' => 'examplebucket-1250000000' //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 返回结果示例
```php
Array
(
    [data:protected] => Array
        (
          [Owner] => Array
              (
                 [ID] => qcs::cam::uin/100000000001:uin/100000000001
                 [DisplayName] => qcs::cam::uin/100000000001:uin/100000000001
              )

          [Grants] => Array
                (
                  [0] => Array
                      (
                        [Grantee] => Array
                           (
                             [ID] => qcs::cam::uin/100000000001:uin/100000000001
                             [DisplayName] => qcs::cam::uin/100000000001:uin/100000000001
                           )

                        [Permission] => FULL_CONTROL
                      )

                )

          [RequestId] => NWE3YzhjMTRfYzdhMzNiMGFfYjdiOF8yYzZmMzU=
        )
)
```
#### 返回结果说明


| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Grants | Array | ACL 权限列表                         | 无 |
| Grant | Array | ACL 权限信息         | Grants |
| Grantee | Array | ACL 权限信息                     | Grant |
| Permission | String | 权限类型，可选值： FULL_CONTROL 、WRITE 、 READ | Grant  |
| Owner | String | 存储桶所有者信息        | 无  |
| DisplayName | String | 权限所有者的名字信息      | Grantee/Owner |
| ID | String | 权限所有者 ID              | Grantee/Owner |

