## 基本 API 描述
> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

### 获取 Buckets 列表
#### 功能说明
List Buckets 列出指定 COS 中的存储桶。
 
#### 方法原型
```php
public Guzzle\Service\Resource\Model listBucket(array $args = array())
```

#### 示例

```php
//获取bucket列表
$result = $cosClient->listBuckets();
```

### 创建 Bucket 
#### 功能说明
Create Bucket 在指定账号下创建一个新的 Bucket，当 Bucket 已存在时会返回错误。

#### 方法原型

```php
// 创建桶
public Guzzle\Service\Resource\Model createBucket(array $args = array());
```

#### 参数说明

`$args` 是包含以下字段的关联数组：

| 字段名   |              描述                  |    类型     |  必填 |       
|------ | ------------ | -------------------------   |  ----------- |
| Bucket   |            存储桶名称               |  String     |  是           |      
| ACL     |         ACL权限控制         |  String     |  否           |   

#### 示例

```php
//创建桶
$result = $cosClient->createBucket(array('Bucket' => 'testbucket'));
```

### 删除 Bucket
#### 功能说明
delete Bucket 在指定账号下删除一个已经存在的 Bucket，删除时 Bucket 必须为空。

#### 方法原型

```php
// 删除桶
public Guzzle\Service\Resource\Model deleteBucket(array $args = array());
```

#### 参数说明

`$args` 是包含以下字段的关联数组：

| 字段名   |         描述                  |      类型     |  必填 |          
| ------ |------------ |  --------  | ---------------------------------- |
| Bucket   |             Bucket 名称               |  String     |  是           |     

#### 示例

```php
//删除桶
$result = $cosClient->deleteBucket(array('Bucket' => 'testbucket'));
```

### 简单文件上传 
#### 功能说明
Put Object 支持上传本地文件或输入流到指定的 Bucket 中。推荐上传不大于 20 MB 的小文件，单次上传大小限制为 5 GB，大文件上传请使用分块上传。

#### 方法原型

```php
public Guzzle\Service\Resource\Model putObject(array $args = array())
```

#### 参数说明

`$args` 是包含以下字段的关联数组：

| 字段名   |                     描述                  |  类型                | 必填 |  
| ------| ------------| --------   | --------------------------------- |
| Bucket   |                Bucket 名称               | String                |   是           |   
|    Key   |         对象名称         |  String                |   是           |   
|    Body  |                   对象的内容                 | String\Resource     |   是           |   
|    ACL    |                 ACL 权限控制                 |  String               |   否           |    
| Metadata | 用户的自定义头（x-cos-meta-）和 HTTP 头（metadata） |Associative-array&lt;string> | 否           | 

#### 示例

```php
// 从内存中上传
$cosClient->putObject(array(
    'Bucket' => 'testbucket',
    'Key' => 'hello.txt',
    'Body' => 'Hello World!'));

// 上传本地文件
$cosClient->putObject(array(
    'Bucket' => 'testbucket',
    'Key' => 'hello.txt',
    'Body' => fopen('./hello.txt', 'rb')));
```

### 分块文件上传
####  功能说明
Multi Upload 分块文件上传是通过将文件拆分成多个小块进行上传，多个小块可以并发上传，最大支持 40 TB。
分块文件上传的步骤为：
1. 初始化分块上传，获取 uploadid（Create Multi partUpload）。
2. 分块数据上传（可并发）（UploadPart）。
3. 完成分块上传（Complete Multipart Upload）。

另外还包含获取已上传分块（ListParts）， 终止分块上传（AbortMultipartUpload）。

#### 方法原型

```php
// 初始化分块上传
public Guzzle\Service\Resource\Model createMultipartUpload(array $args = array());

// 上传数据分块
public Guzzle\Service\Resource\Model uploadPart(array $args = array());
            
// 完成分块上传
public Guzzle\Service\Resource\Model completeMultipartUpload(array $args = array());

// 罗列已上传分块
public Guzzle\Service\Resource\Model listParts(array $args = array());

// 终止分块上传
public Guzzle\Service\Resource\Model abortMultipartUpload(array $args = array());
```
### 上传文件
#### 功能说明
Upload 调用此接口可以将本地的文件上传至指定 Bucket 中。
>单文件小于 5 M 时，使用单文件上传，反之使用分片上传。

#### 示例
```php
//上传文件
$result = $cosClient->upload(
                 $bucket = 'testbucket',
                 $key = '111.txt',
                 $body = '131213');
```


### 下载文件 
#### 功能说明
Get Object 调此接口将文件下载到本地或者下载到内存中。

#### 方法原型

```php
// 下载文件
public Guzzle\Service\Resource\Model getObject(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组：

| 字段名   |                  描述                  |     类型     |  必填 |  
| ------ | ----------- |  --------  | ---------------------------------- |
| Bucket   |                Bucket 名称               | String     |   是           |   
| Key      |           对象名称         | String     |是           |  
| SaveAs   |    保存到本地的本地文件路径                 | String     |  否           | 

#### 示例

```php
// 下载文件到内存
$result = $cosClient->getObject(array(
    'Bucket' => 'testbucket',
    'Key' => 'hello.txt'));

// 下载文件到本地
$result = $cosClient->getObject(array(
    'Bucket' => 'testbucket',
    'Key' => 'hello.txt',
    'SaveAs' => './hello.txt'));
```


### 删除文件 
#### 功能说明
Delete Object 用于删除 COS 上的对象。

#### 方法原型

```php
// 删除文件
public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组：

| 字段名   |                     描述                  |  类型     |必填 |  
| ------ | ----------- |  --------   | -------------------------------- |
| Bucket   |                Bucket 名称               | String     |  是           |  
| Key      |          对象名称         |  String     | 是           |  

#### 示例

```php
// 删除COS对象
$result = $cosClient->deleteObject(array(
    'Bucket' => 'testbucket',
    'Key' => 'hello.txt'));
```

### 获取对象属性
#### 功能说明
Head Object 用于查询获取 COS 上的对象属性。

#### 方法原型
```php
// 获取文件属性
public Guzzle\Service\Resource\Model headObject(array $args = array());
```

#### 参数说明

`$args` 是包含以下字段的关联数组：

| 字段名   |                      描述                  |  类型     | 必填 | 
| ------ | ------------ |  --------   |---------------------------------- |
| Bucket   |                  Bucket 名称               |String     |   是           |  
| Key      |          对象名称         | String     |   是           |  


#### 示例

```java
// 获取 COS 文件属性
$result $cosClient->headObject(array('Bucket' => 'testbucket', 'Key' => 'hello.txt'));
```

### 获取文件列表
#### 功能说明
List Bucket 查询获取 COS 上的文件列表。

#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model listObjects(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组： 
   
| 字段名   |                   描述                  | 类型     |  必填 |     
| ------ | ------------ | -------   | ---------------------------------- |
| Bucket   |              Bucket 名称               | String     |   是           |     
| Delimiter      |            分隔符         |String     |  否          |  
| Marker      |            标记        |String     |   否          |  
| MaxKeys      |            最大对象个数         |Int     |   否          |  
| Prefix      |            前缀         | String     |  否           | 

#### 示例

```php
// 获取 bucket 下成员
$result = $cosClient->listObjects(array('Bucket' => 'testbucket'));
```
### 配置 Bucket ACL 
#### 功能说明
Put Bucket ACL 接口用来写入 Bucket 的 ACL 表。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model putBucketACL(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
 | Bucket |Bucket 名称|String|  是|
 | Region |地域名称|String| 是|
 | ACL |定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|String| 否|
 | GrantRead |赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 是|
 | GrantWrite |赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 否|
 | GrantFullControl |赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 否|


#### 示例

```php
#putBucketACL
try {
    $result = $cosClient->PutBucketAcl(array(
        'Bucket' => 'testbucket',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        ),));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 获取 Bucket ACL
#### 功能说明
Get BucketACL 获取 Bucket 的访问权限控制列表。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model getBucketACL(array $args = array());
```

#### 参数说明

`$args` 是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| Bucket |Bucket 名称|String|  是| 

#### 示例
```php
#getBucketACL
try {
    $result = $cosClient->GetBucketAcl(array(
        'Bucket' => 'testbucket',));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 配置 Object ACL
#### 功能说明
Put Object ACL 接口用来写入 Object  的 ACL 表。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model putObjectACL(array $args = array());
```

#### 参数说明
`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| Bucket |Bucket 名称|String| 是|
| Region |地域名称|String| 是|
| Key |文件名称|String| 是|
| ACL |定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|String|是| 
| GrantRead |赋予被授权者读的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 否|
| GrantWrite |赋予被授权者写的权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 否|
| GrantFullControl |赋予被授权者读写权限。格式：id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"，<br>例如：`id="qcs::cam::uin/123:uin/123", id="qcs::cam::uin/123:uin/456"`|String| 否|

#### 示例
```php
#putObjectACL
try {
    $result = $cosClient->PutBucketAcl(array(
        'Bucket' => 'testbucket',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        ),));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 获取 Object ACL
#### 功能说明
Get Object ACL 获取 Object 的访问权限控制列表。

#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model getObjectACL(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| Bucket |Bucket 名称|String| 是|
| Key |文件名称|String| 是| 

#### 示例
```php
#getObjectACL
try {
    $result = $cosClient->getObjectAcl(array(
        'Bucket' => 'testbucket',
        'Key' => '11'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

### 配置 Bucket CORs
#### 功能说明
Put Bucket Cors 用于设置 Bucket 的跨域资源共享（COR）。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model putBucketCors(array $args = array());
```
#### 参数说明
`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| err |请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功，则为空|Object|  是| 
|data|请求成功时返回的对象，如果请求发生错误，则为空|Object| 是|
| CORSRules |说明跨域资源共享配置的所有信息列表|Array| 是|
| AllowedMethods |允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|Array| 否| 
| AllowedOrigins |允许的访问来源，支持通配符 *   格式为：协议://域名[:端口]如：`http://www.qq.com`|Array| 否| 
| AllowedHeaders |在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |Array| 否| 
| ExposeHeaders |设置浏览器可以接收到的来自服务器端的自定义头部信息|Array| 否| 
| MaxAgeSeconds |设置 OPTIONS 请求得到结果的有效期|String| 否| 
| ID |配置规则的 ID|String|  是|

#### 示例

```php
###putBucketCors
try {
    $result = $cosClient->putBucketCors(array(
        // Bucket is required
        'Bucket' => 'lewzylu02',
        // CORSRules is required
        'CORSRules' => array(
            array(
                'AllowedHeaders' => array('*',),
            // AllowedMethods is required
            'AllowedMethods' => array('Put', ),
            // AllowedOrigins is required
            'AllowedOrigins' => array('*', ),
            'ExposeHeaders' => array('*', ),
            'MaxAgeSeconds' => 1,
        ),
        // ... repeated
    ),
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 获取 Bucket CORs
#### 功能说明
Get Bucket Cors 获取 Bucket 的跨域资源共享（COR）信息。

#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model getBucketCors(array $args = array());
```
#### 参数说明
`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| Bucket |Bucket 名称|String| 是|

#### 示例

```php
#getBucketCors
try {
    $result = $cosClient->getBucketCors(array(
        // Bucket is required
        'Bucket' => 'lewzylu02',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 删除 Bucket CORs
#### 功能说明
Delete Bucket Cors  删除 Bucket 的跨域资源共享（COR）信息。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model deleteBucketCors(array $args = array());
```
#### 参数说明
`$args`是包含以下字段的关联数组：

|字段名 |描述 |类型 |必填|
|------|--------|-------|------|
| Bucket |Bucket 名称|String| 是|

#### 示例

```php
#deleteBucketCors
try {
    $result = $cosClient->deleteBucketCors(array(
        // Bucket is required
        'Bucket' => 'lewzylu02',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

### 复制对象
#### 功能说明
Copy Object 复制 Bucket 中的对象。
#### 方法原型

```php
// 获取文件列表
public Guzzle\Service\Resource\Model copyObject(array $args = array());
```

#### 参数说明

`$args`是包含以下字段的关联数组：

| 字段名   |           描述                  |  类型     | 必填 | 
| ----- | ------------ | --------   | -------------------- |
| Bucket   |                   Bucket 名称               |String     |   是           | 
| CopySource      |            复制来源         | String     |   是          | 
| Key      |           对象名称       | String     |   是          |  

#### 示例

```php
#copyobject
try {
    $result = $cosClient->copyObject(array(
        // Bucket is required
        'Bucket' => 'lewzylu02',
        // CopySource is required
        'CopySource' => 'lewzylu03-1252448703.cos.ap-guangzhou.myqcloud.com/tox.ini',
        // Key is required
        'Key' => 'string',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### Lifecycle 相关
#### 参数说明
参数说明详见官网文档
[Put Bucket Lifecycle ](https://cloud.tencent.com/document/product/436/8280) / [Get Bucket Lifecycle](https://cloud.tencent.com/document/product/436/8278) / [Delete Bucket Lifecycle](https://cloud.tencent.com/document/product/436/8284)

#### 示例

```php
#putBucketLifecycle
try {
    $result = $cosClient->putBucketLifecycle(array(
    // Bucket is required
    'Bucket' => 'lewzylu02',
    // Rules is required
    'Rules' => array(
        array(
            'Expiration' => array(
                'Days' => 1,
            ),
            'ID' => 'id1',
            'Filter' => array(
                'Prefix' => 'documents/'
            ),
            // Status is required
            'Status' => 'Enabled',
            'Transition' => array(
                'Days' => 100,
                'StorageClass' => 'NEARLINE',
            ),
            // ... repeated
        ),
    )));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
```php
#getBucketLifecycle
try {
    $result = $cosClient->getBucketLifecycle(array(
        // Bucket is required
        'Bucket' =>'lewzylu02',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
```php
#deleteBucketLifecycle
try {
    $result = $cosClient->deleteBucketLifecycle(array(
        // Bucket is required
        'Bucket' =>'lewzylu02',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

### 获取 Object 下载 URL
#### 功能说明
获得 Object 带签名的下载 URL。

#### 示例

```php
//获得object的下载url
$bucket =  'testbucket';
$key = 'hello.txt';
$region = 'cn-south';
$url = "/{$key}";
$request = $cosClient->get($url);
$signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
```
### 使用临时密钥

```php
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => 'cn-south',
        'timeout' => ,
        'credentials'=> array(
            'appId' => '',
            'secretId'    => '',
            'secretKey' => '',
            'token' => '')));
```
