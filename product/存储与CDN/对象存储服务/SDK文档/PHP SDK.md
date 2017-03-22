## 开发准备

### SDK 获取

GitHub 项目地址：[https://github.com/tencentyun/cos-php-sdk](https://github.com/tencentyun/cos-php-sdk)

Composer 项目名：tencentyun/cos-php-sdk

### 开发环境

1. 依赖环境：PHP 5.3.0 版本及以上
2. 从控制台获取APP ID、SecretID、SecretKey。



### SDK 配置

下载 SDK 后，使用 composer 安装，直接执行下述命令：

``` php
php composer.phar require tencentyun/cos-php-sdk
```

在使用 SDK 时，加载 include.php 即可。

``` php
require('./include.php'); 
use Qcloud_cos\Auth; 
use Qcloud_cos\Cosapi;
```

若需要支持 HTTPS ，修改 conf.php 中的 API_COSAPI_END_POINT 的值为如下：

``` php
const API_COSAPI_END_POINT = 'https://web.file.myqcloud.com/files/v1/';
```

## 生成签名

### 多次有效签名

#### 方法原型

``` php
public static function appSign($expired, $bucketName);	
```

#### 参数说明

| 参数名        | 类型     | 必填   | 参数描述         |
| ---------- | ------ | ---- | ------------ |
| expired    | long   | 否    | 过期时间，Unix时间戳 |
| bucketName | String | 是    | bucket 名称    |

#### 返回结果说明

base64编码的字符串

#### 示例

``` php
$expired = time() + 60;	
$bucketName = 'testbucket';
$sign = Auth::appSign($expired, $bucketName);
```

### 单次有效签名

#### 方法原型

``` php
public static function appSign_once($path, $bucketName);
```

#### 参数说明

| 参数名        | 类型     | 必填   | 参数描述                                     |
| ---------- | ------ | ---- | ---------------------------------------- |
| path       | String | 是    | 文件路径，以斜杠开头，例如 /filepath/filename，为文件在此 bucketname 下的全路径 |
| bucketName | String | 是    | bucket 名称                                |
#### 返回结果说明

base64编码的字符串
#### 示例

``` php
$bucketName = 'testbucket';
$path = "/myFloder/myFile.rar";
$sign = Auth::appSign_once($path, $bucketName);
```

更多签名相关的详细说明，参考[签名算法](/document/product/430/5993) 

## 目录操作

### 创建目录

接口说明：用于目录的创建，可通过此接口在指定 bucket 下创建目录。

#### 方法原型

``` php
public static function createFolder($bucketName, $path, $bizAttr = null);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**      |
| ---------- | ------ | ------ | ------------- |
| bucketName | String | 是      | bucket 名称     |
| path       | String | 是      | 目录全路径         |
| bizAttr    | String | 否      | 目录属性信息，业务自行维护 |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | 是    | 错误码，成功时为0                                |
| message | String | 是    | 错误信息                                     |
| data    | Array  | 否    | 返回数据，请参考[《Restful API 创建目录》](/document/product/430/6000) |

#### 示例

``` php
$bizAttr = "attr_folder";
$result  = Cosapi::createFolder($bu	cketName, $path,$bizAttr)
```

### 目录更新

接口说明：用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。

#### 方法原型

``` php
public static function updateFolder($bucketName, $path, $bizAttr = null);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | 是      | bucket 名称 |
| path       | String | 是      | 目录路径      |
| bizAttr    | String | 否      | 目录属性信息    |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | 是    | 错误码，成功时为0 |
| message | String | 是    | 错误信息      |

#### 示例

``` php
$bizAttr = "folder new attribute";
$result  = Cosapi::updateFolder($bucketName, $path, $bizAttr)
```

### 目录查询

接口说明：用于目录属性的查询，调用者可以通过此接口查询目录的属性。

#### 方法原型

``` php
public static function statFolder($bucketName, $path);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | 是      | bucket 名称 |
| path       | String | 是      | 目录路径      |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | 是    | 错误码，成功时为0                                |
| message | String | 是    | 错误信息                                     |
| data    | Array  | 否    | 目录属性数据，请参考[《Restful API 目录查询》](/document/product/430/6002) |

#### 示例

``` php
$result = Cosapi::statFolder($bucketName, $path);
```

### 删除目录

接口说明：用于目录的删除，调用者可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

#### 方法原型

``` php
public static function delFolder($bucketName, $path);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | 是      | bucket 名称 |
| path       | String | 是      | 目录全路径     |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | 是    | 错误码，成功时为0 |
| message | String | 是    | 错误信息      |

#### 示例

``` php
$result = Cosapi::delFolder($bucketName, $path);
```

### 列举目录中的文件和目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

#### 方法原型

``` php
public static function listFolder($bucketName, $path, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | 是      | bucket名称                                 |
| path       | String | 是      | 目录的全路径                                   |
| num        | int    | 否      | 要查询的目录/文件数量                              |
| context    | String | 否      | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 否      | 默认正序(=0), 填1为反序                          |
| pattern    | String | 否      | eListBoth：列举文件和目录；eListDirOnly：仅列举目录；eListFileOnly：仅列举文件 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | 是      | API 错误码，成功时为0                            |
| message | String | 是      | 错误信息                                     |
| data    | Array  | 是      | 返回数据，请参考[《Restful API 目录列表》](/document/product/430/6012) |

#### 示例

``` php
$result = Cosapi::listFolder($bucketName, $path, 20, 'eListBoth',0);
```

### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

#### 方法原型

``` php
public static function prefixSearch($bucketName, $prefix, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | 是      | bucket名称，bucket创建参见[创建Bucket](/document/product/430/5887) |
| prefix     | String | 是      | 列出含此前缀的所有文件(带全路径)                        |
| num        | int    | 否      | 要查询的目录/文件数量                              |
| context    | String | 否      | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 否      | 默认正序(=0), 填1为反序                          |
| pattern    | String | 否      | eListBoth：列举文件和目录；eListDirOnly：仅列举目录；eListFileOnly：仅列举文件 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | 是      | 错误码，成功时为0                                |
| message | String | 是      | API 错误信息                                 |
| data    | Array  | 是      | 返回数据，请参考[《Restful API 目录列表》](/document/product/430/6012) |

#### 示例

``` php
$prefix= "/myFolder/2015-";
$result = Cosapi::prefixSearch($bucketName, $prefix, 20, 'eListBoth',0);
```

## 文件操作

### 文件上传

接口说明：文件上传的统一接口，对于大于20M的文件，内部会通过多次分片的方式进行文件上传。

#### 方法原型

``` php
public static function upload($bucketName, $srcPath, $dstPath, 
               $bizAttr = null, $slicesize = null, $insertOnly = null);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| bucketName | String | 是      | bucket名称，bucket创建参见[创建Bucket](/document/product/430/5887) |
| srcPath    | String | 是      | 本地要上传文件的全路径                              |
| dstPath    | String | 是      | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttr    | String | 否      | 文件属性，业务端维护                               |
| slicesize  | int    | 否      | 文件分片大小，当文件大于20M时，SDK内部会通过多次分片的方式进行上传，默认分片大小为1M，支持的最大分片大小为3M |
| insertOnly | int    | 否      | 同名文件是否进行覆盖。0：覆盖；1：不覆盖                    |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**                                 |
| ------- | ------ | ---- | ---------------------------------------- |
| code    | Int    | 是    | 错误码，成功时为0                                |
| message | String | 是    | 错误信息                                     |
| data    | Array  | 是    | 返回数据，请参考[《Restful API 创建文件》](/document/product/430/6005) |

#### 示例

``` php
$dstPath = "/myFolder/test.mp4";
$bizAttr = "";
$insertOnly = 0;
$sliceSize = 3 * 1024 * 1024;
$result = Cosapi::upload($bucketName,$srcPath,$dstPath ,"biz_attr");
```

### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

``` php
public static function update($bucketName, $path, 
                  $bizAttr = null, $authority=null,$customer_headers_array=null);
```

#### 参数说明

| **参数名**                | **类型** | **必填** | **参数描述**                                 |
| ---------------------- | ------ | ------ | ---------------------------------------- |
| bucketName             | String | 是      | bucket 名称                                |
| path                   | String | 是      | 文件在文件服务端的全路径，不包括/appid/bucketname        |
| bizAttr                | String | 否      | 待更新的文件属性信息                               |
| authority              | String | 否      | eInvalid(继承Bucket的读写权限)；eWRPrivate(私有读写)；eWPrivateRPublic(公有读私有写) |
| customer_headers_array | String | 否      | 用户自定义头域。可携带参数名分别为：'Cache-Control'、'Content-Type'、'Content-Disposition'、'Content-Language'、以及以'x-cos-meta-'为前缀的参数名称 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |

#### 示例

``` php
$bizAttr = "";
$authority = "eWPrivateRPublic";
$customer_headers_array = array(
    'Cache-Control' => "no",
    'Content-Language' => "ch",
);
$result = Cosapi::update($bucketName, $dstPath, $bizAttr,$authority, $customer_headers_array);
```

### 文件查询

接口说明：用于文件的查询，调用者可以通过此接口查询文件的各项属性信息。

#### 方法原型

``` php
 public static function stat($bucketName, $path); 
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**     |
| ---------- | ------ | ------ | ------------ |
| bucketName | String | 是      | bucket 名称    |
| path       | String | 是      | 文件在文件服务端的全路径 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                                 |
| ------- | ------ | ------ | ---------------------------------------- |
| code    | Int    | 是      | 错误码，成功时为0                                |
| message | String | 是      | 错误信息                                     |
| data    | Array  | 是      | 文件属性数据，请参考[《Restful API 文件查询》](/document/product/430/6008) |

#### 示例

``` php
$result = Cosapi::stat($bucketName, $path);
```

### 文件删除

接口说明：用于文件的删除，调用者可以通过此接口删除已经上传的文件。

#### 方法原型

``` php
public static function delFile($bucketName, $path);
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**  |
| ---------- | ------ | ------ | --------- |
| bucketName | String | 是      | bucket 名称 |
| path       | String | 是      | 文件的全路径    |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |

#### 示例

``` php
$result = Cosapi::delFile($bucketName, $path);
```
