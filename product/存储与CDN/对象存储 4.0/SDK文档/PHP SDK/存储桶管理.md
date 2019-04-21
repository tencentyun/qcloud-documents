## 简介
本文档提供关于跨域名访问和生命周期相关的 API 概览以及 SDK 示例代码。

**跨域名访问**

| API                                                          | 操作名       | 操作描述                       |
| ------------------------------------------------------------ | ------------ | ------------------------------ |
| [PUT Bucket cors](https://cloud.tencent.com/document/product/436/8279) | 设置跨域配置 | 设置 Bucket 的跨域名访问权限     |
| [GET Bucket cors](https://cloud.tencent.com/document/product/436/8274) | 查询跨域配置 | 查询 Bucket 的跨域名访问配置信息 |
| [DELETE Bucket cors](https://cloud.tencent.com/document/product/436/8283) | 删除跨域配置 | 删除 Bucket 的跨域名访问配置信息 |

**生命周期**

| API                                                          | 操作名       | 操作描述                         |
| ------------------------------------------------------------ | ------------ | -------------------------------- |
| [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280) | 设置生命周期 | 设置 Bucket 的生命周期管理的配置 |
| [GET Bucket lifecycle](https://cloud.tencent.com/document/product/436/8278) | 查询生命周期 | 查询 Bucket 生命周期管理的配置   |
| [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284) | 删除生命周期 | 删除 Bucket 生命周期管理的配置   |

## 跨域访问
### 设置跨域配置

#### 功能说明

设置指定存储桶的跨域名访问配置信息（PUT Bucket cors）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model putBucketCors(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->putBucketCors(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'CORSRules' => array(
            array(
                'AllowedHeaders' => array('*',),
                'AllowedMethods' => array('Put', ),
                'AllowedOrigins' => array('*', ),
                'ExposeHeaders' => array('*', ),
                'MaxAgeSeconds' => 1,
            ),  
            // ... repeated
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

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| CORSRules | Array | 跨域信息列表                         | 无 |
| CORSRule | Array | 跨域信息         | CORSRules |
| AllowedMethods | String | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE                     | CORSRule |
| AllowedOrigins | String | 允许的访问来源，支持通配符 `*`， 格式为：协议://域名[:端口]如：`http://www.qq.com`        | CORSRule  |
| AllowedHeaders | String | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符`*` | CORSRule  |
| ExposeHeaders | String |设置浏览器可以接收到的来自服务器端的自定义头部信息 | CORSRule |
| MaxAgeSeconds | Int | 设置 OPTIONS 请求得到结果的有效期        | CORSRule|
| ID | String | 配置规则的 ID              | CORSRule |


### 查询跨域配置

#### 功能说明

查询指定存储桶的跨域名访问配置信息（GET Bucket cors）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model getBucketCors(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->getBucketCors(array(
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

#### 返回结果示例
```php
Array
(
    [data:protected] => Array
        (
            [CORSRules] => Array
                (
                    [0] => Array
                        (
                            [ID] => 1234
                            [AllowedHeaders] => Array
                                (
                                    [0] => *
                                )
                            [AllowedMethods] => Array
                                (
                                    [0] => PUT
                                )
                            [AllowedOrigins] => Array
                                (
                                    [0] => http://www.qq.com
                                )
                        )
                )
            [RequestId] => NWE3YzhkMmRfMTdiMjk0MGFfNTQzZl8xNWUwMGU=
        )
)
```
#### 返回结果说明


| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| CORSRules | Array | 跨域信息列表                         | 无 |
| CORSRule | Array | 跨域信息         | CORSRules |
| AllowedMethods | String | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE                     | CORSRule |
| AllowedOrigins | String | 允许的访问来源，支持通配符`*`， 格式为：协议://域名[:端口]。例如：`http://www.qq.com`        | CORSRule  |
| AllowedHeaders | String | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符`*` | CORSRule  |
| ExposeHeaders | String |设置浏览器可以接收到的来自服务器端的自定义头部信息 | CORSRule |
| MaxAgeSeconds | Int | 设置 OPTIONS 请求得到结果的有效期        | CORSRule|
| ID | String | 配置规则的 ID              | CORSRule |


### 删除跨域配置

#### 功能说明

删除指定存储桶的跨域名访问配置（DELETE Bucket cors）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model deleteBucketCors(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->deleteBucketCors(array(
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


## 生命周期
### 设置生命周期

#### 功能说明

设置指定存储桶的生命周期配置信息（PUT Bucket lifecycle）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model putBucketLifecycle(array $args = array());
```
 
#### 请求示例
```php
try {
    $result = $cosClient->putBucketCors(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Rules' => array(
            array(
                'Expiration' => array(
                    'Days' => integer,
                ),  
                'ID' => 'string',
                'Filter' => array(
                    'Prefix' => 'string'
                ),  
                'Status' => 'string',
                'Transitions' => array(
                    array(
                        'Days' => integer,
                        'StorageClass' => 'string'
                    ),  
                    // ... repeated
                ),  
            ),  
            // ... repeated
        )   
    );  
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
| Rules | Array | 生命周期信息列表                         | 无 |
| Rule | Array | 生命周期信息         | Rules |
| Expiration | Array | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date | Rule |
| Transition | Array | 设置 Object 转换存储类型规则 | Rule  |
| Filter | Array | 用于描述规则影响的 Object 集合 | Rule  |
| Prefix | String | 过滤的对象的前缀 | Filter  |
| Status | String |设置 Rule 是否启用，可选值为 Enabled 、 Disabled | Rule |
| ID | String | 配置规则的 ID              | Rule |
| Days | Int | 设置生效的天数     | Expiration / Transition |
| Date | Int / String | 设置生效的日期     | Expiration / Transition |
| StorageClass | String | 转换的文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE，默认值：STANDARD     | Transition |

### 查询生命周期

#### 功能说明

设置 Bucket 生命周期管理的配置（GET Bucket lifecycle）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model getBucketLifecycle(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->getBucketLifecycle(array(
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

#### 返回结果示例
```php
Array
(
    [data:protected] => Array
        (
            [Rules] => Array
                (
                    [0] => Array
                        (
                            [ID] => id1
                            [Filter] => Array
                                (
                                    [Prefix] => documents/
                                )
                            [Status] => Enabled
                            [Transition] => Array
                                (
                                    [Days] => 200
                                    [StorageClass] => Standard_IA
                                )
                            [Expiration] => Array
                                (
                                    [Days] => 1000
                                )
                        )
                )
            [RequestId] => NWE3YzhlZjNfY2FhMzNiMGFfNDVkNF8yZDIxODE=
        )
)
```
#### 返回结果说明


| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Rules | Array | 生命周期信息列表                         | 无 |
| Rule | Array | 生命周期信息         | Rules |
| Expiration | Array | 设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date | Rule |
| Transition | Array | 设置 Object 转换存储类型规则 | Rule  |
| Filter | Array | 用于描述规则影响的 Object 集合 | Rule  |
| Prefix | String | 过滤的对象的前缀 | Filter  |
| Status | String |设置 Rule 是否启用，可选值为 Enabled 、 Disabled | Rule |
| ID | String | 配置规则的 ID              | Rule |
| Days | Int | 设置生效的天数     | Expiration / Transition |
| Date | Int / String | 设置生效的日期     | Expiration / Transition |
| StorageClass | String | 转换的文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE，默认值：STANDARD     | Transition |



### 删除生命周期

#### 功能说明

删除 Bucket 生命周期管理的配置（DELETE Bucket lifecycle）。

#### 方法原型
```php
public Guzzle\Service\Resource\Model deleteBucketLifecycle(array $args = array());
```

#### 请求示例
```php
try {
    $result = $cosClient->deleteBucketLifecycle(array(
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
