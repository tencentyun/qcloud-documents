
# 日志管理

## 简介
本文档提供关于日志管理的 API 概览以及 SDK 示例代码。

| API            | 操作名       | 操作描述 |
| --------------------------- | ------------ | -------- |
| [PUT Bucket logging](https://cloud.tencent.com/document/product/436/17054) | 设置日志管理 | 为源存储桶开启日志记录 |
| [GET Bucket logging](https://cloud.tencent.com/document/product/436/17053) | 查询日志管理 | 查询源存储桶的日志配置信息 |


### 设置日志管理

#### 功能说明

PUT Bucket logging 为源存储桶开启日志记录，将源存储桶的访问日志保存到指定的目标存储桶中。

#### 方法原型
```
public Guzzle\Service\Resource\Model PutBucketLogging(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketLogging(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'LoggingEnabled' => array(
            'TargetBucket' => 'examplebucket2-1250000000',
            'TargetPrefix' => '', 
        )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 开启日志功能的源存储桶名称，命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |
| TargetBucket | 存放日志的目标存储桶名称，命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)  | String                        |
| TargetPrefix | 日志存放在目标存储桶的指定路径  | String


### 查询日志管理

#### 功能说明

GET Bucket logging 查询指定存储桶的日志配置信息。

#### 方法原型

```
public Guzzle\Service\Resource\Model GetBucketLogging(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->getBucketLogging(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 源存储桶名称，命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [LoggingEnabled] => Array
        (
            [TargetBucket] => examplebucket2-1250000000
            [TargetPrefix] => 
        )

    [RequestId] => NWRmMWJjOThfMjZiMjU4NjRfODY4X2ExMjcyYg==
)
```

#### 返回结果说明

| 成员变量| 描述  | 类型  |
| ----| ---- | ---- |
| TargetBucket | 日志存储的目标存储桶  | String |
| TargetPrefix | 日志存储的目标存储桶路径  | String   |


# 存储桶标签

## 简介
本文档提供关于存储桶标签的 API 概览以及 SDK 示例代码。

| API                                                          | 操作名         | 操作描述                         |
| ------------------------------------------------------------ | -------------- | -------------------------------- |
| [PUT Bucket tagging](https://cloud.tencent.com/document/product/436/34838) | 设置存储桶标签 | 为已存在的存储桶设置标签         |
| [GET Bucket tagging](https://cloud.tencent.com/document/product/436/34837) | 查询存储桶标签 | 查询指定存储桶下已有的存储桶标签 |
| [DELETE Bucket tagging](https://cloud.tencent.com/document/product/436/34836) | 删除存储桶标签 | 删除指定的存储桶标签             |


### 设置存储桶标签

#### 功能说明

PUT Bucket tagging 用于为已存在的存储桶设置标签。

#### 方法原型
```
public Guzzle\Service\Resource\Model PutBucketTagging(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketTagging(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'TagSet' => array(
            array('Key'=>'key1',
                  'Value'=>'value1',
            ),  
            array('Key'=>'key2',
                  'Value'=>'value2',
            ),  
        ),  
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String |
| Key  | 标签的键值 | String |
| Value  | 标签的值 | String |


### 查询存储桶标签

#### 功能说明

DELETE Bucket tagging 用于查询指定存储桶下已有的存储桶标签。

#### 方法原型
```
public Guzzle\Service\Resource\Model GetBucketTagging(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->getBucketTagging(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [TagSet] => Array
        (
            [0] => Array
                (
                    [Key] => key1
                    [Value] => value1
                )

            [1] => Array
                (
                    [Key] => key2
                    [Value] => value2
                )

        )
    [RequestId] => NWRmMWVkMjFfMjJiMjU4NjRfNWQ3X2EwMWVjNA==
)
```

#### 返回结果说明
| 成员变量| 描述  | 类型  |
| ----| ---- | ---- |
| Key  | 标签的键值 | String |
| Value  | 标签的值 | String |


### 删除存储桶标签

#### 功能说明

DELETE Bucket tagging 用于删除指定存储桶下已有的存储桶标签。

#### 方法原型
```
public Guzzle\Service\Resource\Model DeleteBucketTagging(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->deleteBucketTagging(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
    );
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |



# 自定义域名

## 简介
本文档提供关于自定义域名的 API 概览以及 SDK 示例代码。

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| PUT Bucket domain | 设置自定义域名   | 设置存储桶的自定义域名信息 |
| GET Bucket domain | 查询自定义域名 | 查询存储桶的自定义域名信息 |

### 设置自定义域名

#### 功能说明

PUT Bucket domain 用于为存储桶配置自定义域名。

#### 方法原型
```
public Guzzle\Service\Resource\Model PutBucketDomain(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketDomain(array( 
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID 
        'DomainRules' => array( 
            array( 
                'Name' => 'www.qq.com', 
                'Status' => 'ENABLED', 
                'Type' => 'REST', 
                'ForcedReplacement' => 'CNAME', 
            ),  
            // ... repeated 
        ),  
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |
| Name | 自定义域名  | String |
| Status | 域名上线状态，可选值有 ENABLED、DISABLED | String |
| Type | 绑定的源站类型，可选值有 REST、WEBSITE | String |
| ForcedReplacement | 强制覆盖已存在的配置，可选值有 CNAME、TXT | String |


#### 返回错误码说明

该请求可能会发生的一些常见的特殊错误如下：

| 状态码|说明  |
| ----| --- |
| HTTP 409 Conflict | 该域名记录已存在，且请求中没有设置强制覆盖。或者该域名记录不存在，且请求中设置了强制覆盖。 |
| HTTP 451 Unavailable For Legal Reasons | 该域名是中国境内域名，并且没有备案 |

### 查询自定义域名

#### 功能说明

GET Bucket domain 用于查询存储桶的自定义域名信息。

#### 方法原型
```
public Guzzle\Service\Resource\Model GetBucketDomain(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->getBucketDomain(array( 
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [DomainRules] => Array
        (
            [0] => Array
                (
                    [Status] => ENABLED
                    [Name] => www.qq.com
                    [Type] => REST
                )

        )
    [DomainTxtVerification] => tencent-cloud-cos-verification=9d2258433b1f38c7dd4b29fe272d2128
)
```

#### 返回结果说明

| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| Name | 自定义域名  | String |
| Status | 域名上线状态，可选值有 ENABLED、DISABLED | String |
| Type | 绑定的源站类型，可选值有 REST、WEBSITE | String |
| ForcedReplacement | 强制覆盖已存在的配置，可选值有 CNAME、TXT | String |
| DomainTXTVerification | cos+地域+bucket+存储桶 GMT 创建时间字段的md5校验值 | String |

#### 返回参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| x-cos-domain-txt-verification  | 域名校验信息，该字段是一个 MD5 校验值，原串格式为：cos[Region][BucketName-APPID][BucketCreateTime]，其中 Region 为存储桶所在地域，BucketCreateTime 为存储桶 GMT 创建时间 | String |


# 静态网站

## 简介
本文档提供关于静态网站的 API 概览以及 SDK 示例代码。

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket website](https://cloud.tencent.com/document/product/436/19223) | 设置静态网站   | 设置存储桶的静态网站配置 |
| [GET Bucket website](https://cloud.tencent.com/document/product/436/19222) | 查询静态网站配置 | 查询存储桶的静态网站配置 |
| [DELETE Bucket website](https://cloud.tencent.com/document/product/436/19221) | 删除静态网站配置 | 删除存储桶的静态网站配置 |


### 设置静态网站

#### 功能说明

PUT Bucket website 用于为存储桶配置静态网站。

#### 方法原型
```
public Guzzle\Service\Resource\Model PutBucketWebsite(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketWebsite(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'IndexDocument' => array(
            'Suffix' => 'index.html',
        ),
        'RedirectAllRequestsTo' => array(
            'Protocol' => 'https',
        ),
        'ErrorDocument' => array(
            'Key' => 'Error.html',
        ),
        'RoutingRules' => array(
            array(
                'Condition' => array(
                    'HttpErrorCodeReturnedEquals' => '405',
                ),
                'Redirect' => array(
                    'Protocol' => 'https',
                    'ReplaceKeyWith' => '404.html',
                ),
            ),  
            // ... repeated
        ),  
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明

| 参数名称                        | 父节点                | 描述                                                         | 类型      | 必选 |
| --------------------------- | --------------------- | ------------------------------------------------------------ | --------- | ---- |
| Bucket  |  无 | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String       |是                  |
| IndexDocument               | 无  | 索引文档                                                     | Array | 是   |
| Suffix                      | IndexDocument         | 指定索引文档                                                 | String    | 是   |
| ErrorDocument               | 无  | 错误文档                                                     | Array | 否   |
| Key                         | ErrorDocument         | 指定通用错误返回                                             | String    | 否   |
| RedirectAllRequestsTo       | 无  | 重定向所有请求                                               | Array | 否   |
| Protocol                    | RedirectAllRequestsTo | 指定全站重定向的协议，只能设置为 https                        | String    | 否   |
| RoutingRules                | 无  | 设置重定向规则，最多设置100条 RoutingRule                     | Array | 否   |
| RoutingRule                 | RoutingRules          | 设置单条重定向规则，包括前缀匹配重定向和错误码重定向         | Array | 否   |
| Condition                   | RoutingRule           | 指定重定向发生的条件，前缀匹配重定向和错误码重定向只能指定一个 | Array | 否   |
| HttpErrorCodeReturnedEquals | Condition             | 指定重定向错误码，只支持配置4XX返回码，优先级高于ErrorDocument | Interger  | 否   |
| KeyPrefixEquals             | Condition             | 指定前缀重定向的路径，替换指定的 folder/                      | String    | 否   |
| Redirect                    | RoutingRule           | 指定满足重定向 conditon 时重定向的具体替换规则                 | Array | 否   |
| ReplaceKeyWith              | Redirect              | 替换整个 Key 为指定的内容                                      | String    | 否   |
| ReplaceKeyPrefixWith        | Redirect              | 替换匹配到的前缀为指定的内容，Conditon 为 KeyPrefixEquals 才可设置 | String    | 否   |


### 查询静态网站配置

#### 功能说明

GET Bucket website 用于查询与存储桶关联的静态网站配置信息。

#### 方法原型
```
public Guzzle\Service\Resource\Model GetBucketWebsite(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->getBucketWebsite(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | xxx                         |

#### 返回结果示例
```php
GuzzleHttp\Command\Result Object
(
    [RedirectAllRequestsTo] => Array
        (
            [Protocol] => https
        )

    [IndexDocument] => Array
        (
            [Suffix] => index.html
        )

    [ErrorDocument] => Array
        (
            [Key] => Error.html
        )

    [RoutingRules] => Array
        (
            [0] => Array
                (
                    [Condition] => Array
                        (
                            [HttpErrorCodeReturnedEquals] => 405
                        )

                    [Redirect] => Array
                        (
                            [Protocol] => https
                            [ReplaceKeyWith] => 404.html
                        )

                )

        )
    [RequestId] => NWRmMzQ3YjlfMTlhYTk0MGFfNzMzYl84YWIyNjc=
)
```
#### 返回结果说明

| 参数名称  |  描述                                                         | 类型      | 
| --------------------------- |------------------------------------------------------------ | --------- |
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String       |
| IndexDocument               |索引文档                                                     | Array | 
| Suffix                      | 指定索引文档                                                 | String    | 
| ErrorDocument               | 错误文档                                                     | Array | 
| Key                         | 指定通用错误返回                                             | String    |
| RedirectAllRequestsTo       | 重定向所有请求                                               | Array | 
| Protocol                    | 指定全站重定向的协议，只能设置为 https                        | String    | 
| RoutingRules                | 设置重定向规则，最多设置100条 RoutingRule                     | Array | 
| RoutingRule                 | 设置单条重定向规则，包括前缀匹配重定向和错误码重定向         | Array | 
| Condition                   | 指定重定向发生的条件，前缀匹配重定向和错误码重定向只能指定一个 | Array | 
| HttpErrorCodeReturnedEquals | 指定重定向错误码，只支持配置4XX返回码，优先级高于ErrorDocument | Interger  | 
| KeyPrefixEquals             | 指定前缀重定向的路径，替换指定的 folder/                      | String    | 
| Redirect                    | 指定满足重定向 conditon 时重定向的具体替换规则                 | Array | 
| ReplaceKeyWith              | 替换整个 Key 为指定的内容                                      | String    | 
| ReplaceKeyPrefixWith        | R替换匹配到的前缀为指定的内容，Conditon 为 KeyPrefixEquals 才可设置 | String    | 



### 删除静态网站配置

#### 功能说明

DELETE Bucket website 用于删除存储桶中的静态网站配置。

#### 方法原型
```
public Guzzle\Service\Resource\Model DeleteBucketWebsite(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->deleteBucketWebsite(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |


# 清单

## 简介
本文档提供关于清单的 API 概览以及 SDK 示例代码。

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket inventory](https://cloud.tencent.com/document/product/436/33707) | 设置清单任务   | 设置存储桶的清单任务 |
| [GET Bucket inventory](https://cloud.tencent.com/document/product/436/33705) | 查询清单任务 | 查询存储桶的清单任务 |
| [DELETE Bucket inventory](https://cloud.tencent.com/document/product/436/33704) | 删除清单任务 | 删除存储桶的清单任务 |


### 设置清单任务

#### 功能说明

PUT Bucket inventory 用于在存储桶中创建清单任务。

#### 方法原型
```
public Guzzle\Service\Resource\Model PutBucketInventory(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketInventory(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'Id' => 'string',
        'Destination' => array(
            'COSBucketDestination'=>array(
                'Format' => 'CSV',
                'AccountId' => '100000000001',
                'Bucket' => 'qcs::cos:ap-chengdu::examplebucket-125000000',
                'Prefix' => 'string',
            )
        ),      
        'IsEnabled' => 'True',
        'Schedule' => array(
            'Frequency' => 'Daily',
        ),  
        'Filter' => array(
            'Prefix' => 'string',
        ),  
        'IncludedObjectVersions' => 'Current',
        'OptionalFields' => array(
            'Size', 
            'ETag',
        )
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}

```

#### 参数说明

| 参数名称                 | 父节点                 | 描述                                                         | 类型      | 是否必选 |
| ---------------------- | ---------------------- | ------------------------------------------------------------ | --------- | -------- |
| Bucket  |  无 | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |Array | 是       |
| Id                     | 无 | 清单的名称，与请求参数中的 id 对应                         | Array | 是       |
| IsEnabled              | 无 | 清单是否启用的标识：<br><li>如果设置为 true，清单功能将生效<br><li>如果设置为 false，将不生成任何清单 | String    | 是       |
| IncludedObjectVersions | 无 | 是否在清单中包含对象版本：<br><li>如果设置为 All，清单中将会包含所有对象版本，并在清单中增加 VersionId，IsLatest，DeleteMarker 这几个字段<br><li>如果设置为 Current，则清单中不包含对象版本信息 | String    | 是       |
| Filter                 | 无 | 筛选待分析对象。清单功能将分析符合 Filter 中设置的前缀的对象 | Array | 否       |
| Prefix                 | Filter                 | 需要分析的对象的前缀                                       | String    | 否       |
| OptionalFields         | 无 | 清单结果中可选包含的分析项目名称，可选字段包括：Size，LastModifiedDate，StorageClass，ETag，IsMultipartUploaded，ReplicationStatus                           | Array | 否       |
| Schedule               | 无 | 配置清单任务周期                                           | Array | 是       |
| Frequency              | Schedule               | 清单任务周期，可选项为按日或者按周，枚举值：Daily、Weekly      | String    | 是       |
| Destination            | 无 | 描述存放清单结果的信息                                     | Array | 是       |
| COSBucketDestination   | Destination            | 清单结果导出后存放的存储桶信息                             | Array | 是       |
| Bucket                 | COSBucketDestination   | 清单分析结果的存储桶名                                    | String    | 是       |
| AccountId              | COSBucketDestination   | 存储桶的所有者 UIN，例如100000000001                                            | String    | 否       |
| Prefix                 | COSBucketDestination   | 清单分析结果的前缀                                         | String    | 否       |
| Format                 | COSBucketDestination   | 清单分析结果的文件形式，可选项为 CSV 格式                  | String    | 是       |
| Encryption             | COSBucketDestination   | 为清单结果提供服务端加密的选项                             | Array | 否       |
| SSE-COS                | Encryption             | COS 托管密钥的加密方式，无需填充                           | String | 否       |

其他清单配置参数请参考API文档。


#### 错误码说明

该请求可能会发生的一些常见的特殊错误如下：

| 错误码| 描述  | 状态码  |
| ----| ---- | ---- |
| InvalidArgument  | 不合法的参数值 | HTTP 400 Bad Request |
| TooManyConfigurations | 清单数量已经达到1000条的上限  | HTTP 400 Bad Request |
| AccessDenied | 未授权的访问。您可能不具备访问该存储桶的权限 | HTTP 403 Forbidden |

### 查询清单任务

#### 功能说明

GET Bucket inventory 接口用于查询存储桶中用户的清单任务信息。

#### 方法原型
```
public Guzzle\Service\Resource\Model GutBucketInventory(array $args = array());

```

#### 请求示例
```php
try {
    $result = $cosClient->getBucketInvnetory(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'Id' => 'string',
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | bucket                         |
| Id | 清单任务的名称，合法字符：a-z，A-Z，0-9，-，_，.  | String |

#### 返回结果示例
```php
GuzzleHttp\Command\Result Object
(
    [Destination] => Array
        (
            [COSBucketDestination] => Array
                (
                    [Format] => CSV
                    [AccountId] => 100000000001
                    [Bucket] => qcs::cos:ap-chengdu::examplebucket-125000000
                    [Prefix] => String
                )

        )

    [Schedule] => Array
        (
            [Frequency] => Daily
        )

    [OptionalFields] => Array
        (
            [0] => Size
            [1] => ETag
        )

    [IsEnabled] => true
    [Id] => string
    [IncludedObjectVersions] => Current
    [RequestId] => NWRmMzQwMDVfMjNiMjU4NjRfOGQ4MV9iN2JkYWU=
)
```

#### 返回结果说明
| 参数名称               | 描述                                                         | 类型      |
| -------------------- | ------------------------------------------------------------ | --------- | 
| Bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |Array | 
| Id                     | 清单的名称，与请求参数中的 id 对应                         | Array | 
| IsEnabled              |  清单是否启用的标识：<br><li>如果设置为 true，清单功能将生效<br><li>如果设置为 false，将不生成任何清单 | String    | 
| IncludedObjectVersions |  是否在清单中包含对象版本：<br><li>如果设置为 All，清单中将会包含所有对象版本，并在清单中增加 VersionId，IsLatest，DeleteMarker 这几个字段<br><li>如果设置为 Current，则清单中不包含对象版本信息 | String    | 
| Filter                 |  筛选待分析对象。清单功能将分析符合 Filter 中设置的前缀的对象 | Array | 
| Prefix                 |  需要分析的对象的前缀                                       | String    |
| OptionalFields         |  清单结果中可选包含的分析项目名称，可选字段包括：Size，LastModifiedDate，StorageClass，ETag，IsMultipartUploaded，ReplicationStatus                           | Array | 
| Schedule               | 配置清单任务周期                                           | Array | 
| Frequency              | 清单任务周期，可选项为按日或者按周，枚举值：Daily、Weekly      | String    |
| Destination            | 描述存放清单结果的信息                                     | Array | 
| COSBucketDestination   |  清单结果导出后存放的存储桶信息                             | Array | 
| Bucket                 |  清单分析结果的存储桶名                                    | String    | 
| AccountId              |存储桶的所有者 UIN，例如100000000001                                            | String    | 
| Prefix                 |  清单分析结果的前缀                                         | String    | 
| Format                 |  清单分析结果的文件形式                 | String    | 
| Encryption             |  为清单结果提供服务端加密的选项                             | Array |
| SSE-COS                |  COS 托管密钥的加密方式，无需填充                           | String |



### 删除清单任务

#### 功能说明

DELETE Bucket inventory 删除存储桶中指定的清单任务。

#### 方法原型
```
public Guzzle\Service\Resource\Model DeleteBucketInventory(array $args = array());
```
  
#### 请求示例
```php
try {
    $result = $cosClient->deleteBucketInvnetory(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'Id' => 'string',
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明
| 参数名称| 描述  | 类型  |
| ----| ---- | ---- |
| bucket  | 存储桶的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String                         |
| Id | 清单任务的名称，合法字符：a-z，A-Z，0-9，-，_，.  | String |
