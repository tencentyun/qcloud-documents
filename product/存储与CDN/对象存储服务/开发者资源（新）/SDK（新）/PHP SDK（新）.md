



### 开发准备

#### SDK 获取

GitHub 项目地址：[https://github.com/tencentyun/cos-php-sdk](https://github.com/tencentyun/cos-php-sdk)

Composer 项目名：tencentyun/cos-php-sdk

#### 

#### 开发环境

1. 依赖环境：PHP 5.3.0 版本及以上
2. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/doc/product/227/权限控制)。






#### SDK 配置

下载 SDK 后，使用 composer 安装，直接执行下述命令：

```php
php composer.phar require tencentyun/cos-php-sdk
```

在使用 SDK 时，加载 include.php 即可。

```php
require('./include.php'); 
use Qcloud_cos\Auth; 
use Qcloud_cos\Cosapi;
```

若需要支持 HTTPS ，修改 conf.php 中的 API_COSAPI_END_POINT 的值为如下：

```php
const API_COSAPI_END_POINT = 'https://web.file.myqcloud.com/files/v1/';
```



### 生成签名

#### 多次有效签名

##### 方法原型

```php
public static function appSign($expired, $bucketName);	
```

##### 参数说明

| 参数名        | 类型     | 是否必填 | 默认值  | 参数描述         |
| ---------- | ------ | ---- | ---- | ------------ |
| expired    | long   | 否    | 无    | 过期时间，Unix时间戳 |
| bucketName | String | 是    | 无    | bucket 名称    |

##### 示例

```php
$expired = time() + 60;	
$bucketName = 'testbucket';
$sign = Auth::appSign($expired, $bucketName);
```



#### 单次有效签名

##### 方法原型

```php
public static function appSign_once($path, $bucketName);
```

##### 参数说明

| 参数名        | 类型     | 是否必填 | 默认值  | 参数描述                                     |
| ---------- | ------ | ---- | ---- | ---------------------------------------- |
| path       | String | 是    | 无    | 文件路径，以斜杠开头，例如 /filepath/filename，为文件在此 bucketname 下的全路径 |
| bucketName | String | 是    | 无    | bucket 名称                                |

##### 示例

```php
$bucketName = 'testbucket';
$path = "/myFloder/myFile.rar";
$sign = Auth::appSign_once($path, $bucketName);
```

更多签名相关的详细说明，参考[权限控制](/doc/product/227/权限控制)。



### 目录操作

#### 创建目录

接口说明：用于目录的创建，可通过此接口在指定 bucket 下创建目录。

##### 方法原型

```php
public static function createFolder($bucketName, $path,$bizAttr = null);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                         |
| ---------- | ------ | -------- | ---- | -------------------------------- |
| bucketName | String | 是        | 无    | bucket 名称                        |
| path       | String | 是        | 无    | 需要创建目录的全路径，以"/"开头,以"/"结尾，api 会补齐 |
| bizAttr    | String | 否        | null | 目录绑定的属性信息，业务自行维护                 |

##### 返回值说明(json)

| **参数名**            | **类型** | **参数描述**           |
| ------------------ | ------ | ------------------ |
| httpcode           | Int    | http 响应码，请求正常时为200 |
| code               | Int    | 错误码，成功时为0          |
| message            | String | 错误信息               |
| data               | Array  | 返回数据               |
| data.ctime         | String | 目录的创建时间，unix时间戳    |
| data.resource_path | String | 目录的资源路径            |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/";
$bizAttr = "attr_folder";
$result  = Cosapi::createFolder($bucketName, $path,$bizAttr)
```



#### 目录更新

接口说明：用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```php
public static function updateFolder($bucketName, $path, $bizAttr);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                         |
| ---------- | ------ | -------- | ---- | -------------------------------- |
| bucketName | String | 是        | 无    | bucket 名称                        |
| path       | String | 是        | 无    | 需要创建目录的全路径，以"/"开头,以"/"结尾，api 会补齐 |
| bizAttr    | String | 否        | null | 新的目录绑定的属性信息                      |

##### 返回值说明(json)

| **参数名**  | **类型** | **参数描述**          |
| -------- | ------ | ----------------- |
| httpcode | Int    | http响应码，请求正常时为200 |
| code     | Int    | 错误码，成功时为0         |
| message  | String | 错误信息              |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/";
$bizAttr = "attr_folder_new";
$result  = Cosapi::updateFolder($bucketName, $path,$bizAttr)
```



#### 目录查询

接口说明：用于目录属性的查询，调用者可以通过此接口查询目录的属性。

##### 原型方法

```php
public static function statFolder($bucketName, $path);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                         |
| ---------- | ------ | -------- | ---- | -------------------------------- |
| bucketName | String | 是        | 无    | bucket 名称                        |
| path       | String | 是        | 无    | 需要创建目录的全路径，以"/"开头,以"/"结尾，api 会补齐 |

##### 返回值说明(json)

| **参数名**       | **类型** | **参数描述**          |
| ------------- | ------ | ----------------- |
| httpcode      | Int    | http响应码，请求正常时为200 |
| code          | Int    | 错误码，成功时为0         |
| message       | String | 错误信息              |
| data          | Array  | 目录属性数据            |
| data.biz_attr | String | 目录绑定的属性信息，业务自行维护  |
| data.ctime    | String | 目录的创建时间，unix时间戳   |
| data.mtime    | String | 目录的修改时间，unix时间戳   |
| data.name     | String | 目录的名称             |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Cosapi::statFolder($bucketName, $path);
```



#### 删除目录

接口说明：用于目录的删除，调用者可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

##### 方法原型

```php
public static function delFolder($bucketName, $path);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                         |
| ---------- | ------ | -------- | ---- | -------------------------------- |
| bucketName | String | 是        | 无    | bucket 名称                        |
| path       | String | 是        | 无    | 需要创建目录的全路径，以"/"开头,以"/"结尾，api 会补齐 |

##### 返回值说明(json)

| **参数名**  | **类型** | **参数描述**          |
| -------- | ------ | ----------------- |
| httpcode | Int    | http响应码，请求正常时为200 |
| code     | Int    | 错误码，成功时为0         |
| message  | String | 错误信息              |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Cosapi::delFolder($bucketName, $path);
```



#### 列举目录中的文件和目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

##### 方法原型

```php
public static function listFolder($bucketName, $path, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值       | **参数描述**                                 |
| ---------- | ------ | -------- | --------- | ---------------------------------------- |
| bucketName | String | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无         | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| num        | int    | 否        | 20        | 要查询的目录/文件数量                              |
| context    | String | 否        | null      | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern    | String | 否        | eListBoth | eListBoth=>列举文件&目录；eListDirOnly=>仅列举目录；eListFileOnly=>仅列举文件 |

##### 返回值说明(json)

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| httpcode              | Int    | 是            | http响应码，请求正常时为200                        |
| code                  | Int    | 是            | API 错误码，成功时为0                            |
| message               | String | 是            | 错误信息                                     |
| data                  | Array  | 是            | 返回数据                                     |
| data.has_more         | Bool   | 是            | 是否有内容可以继续往前/往后翻页                         |
| data.context          | String | 是            | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| data.dircount         | String | 是            | 子目录数量(总)                                 |
| data.filecount        | String | 是            | 子文件数量(总)                                 |
| data.infos            | Array  | 是            | 文件、目录集合，可以为空                             |
| data.infos.name       | String | 是            | 文件或目录名                                   |
| data.infos.biz_attr   | String | 是            | 目录或文件属性，业务端维护                            |
| data.infos.ctime      | String | 是            | 目录或文件的创建时间，unix时间戳                       |
| data.infos.mtime      | String | 是            | 目录或文件的修改时间，unix时间戳                       |
| data.infos.filesize   | Int    | 否(当类型为文件时返回) | 文件大小                                     |
| data.infos.filelen    | Int    | 否(当类型为文件时返回) | 文件已传输大小(通过与filesize对比可知文件传输进度)           |
| data.infos.sha        | String | 否(当类型为文件时返回) | 文件sha                                    |
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的文件下载url                               |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Cosapi::listFolder($bucketName, $path, 20, 'eListBoth',0); xxxxxxxxxx 
```



#### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

##### 原型方法

```php
public static function prefixSearch($bucketName, $prefix, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值       | **参数描述**                                 |
| ---------- | ------ | -------- | --------- | ---------------------------------------- |
| bucketName | String | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| prefix     | String | 是        | 无         | 列出含此前缀的所有文件(带全路径)                        |
| num        | int    | 否        | 20        | 要查询的目录/文件数量                              |
| context    | String | 否        | null      | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern    | String | 否        | eListBoth | eListBoth=>列举文件&目录；eListDirOnly=>仅列举目录；eListFileOnly=>仅列举文件 |

##### 返回值说明(json)

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| httpcode              | Int    | 是            | http响应码，请求正常时为200                        |
| code                  | Int    | 是            | 错误码，成功时为0                                |
| message               | String | 是            | API 错误信息                                 |
| data                  | Array  | 是            | 返回数据                                     |
| data.has_more         | Bool   | 是            | 是否有内容可以继续往前/往后翻页                         |
| data.context          | String | 是            | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| data.dircount         | String | 是            | 子目录数量(总)                                 |
| data.filecount        | String | 是            | 子文件数量(总)                                 |
| data.infos            | Array  | 是            | 文件、目录集合，可以为空                             |
| data.infos.name       | String | 是            | 文件或目录名                                   |
| data.infos.biz_attr   | String | 是            | 目录或文件属性，业务端维护                            |
| data.infos.ctime      | String | 是            | 目录或文件的创建时间，unix时间戳                       |
| data.infos.mtime      | String | 是            | 目录或文件的修改时间，unix时间戳                       |
| data.infos.filesize   | Int    | 否(当类型为文件时返回) | 文件大小                                     |
| data.infos.filelen    | Int    | 否(当类型为文件时返回) | 文件已传输大小(通过与filesize对比可知文件传输进度)           |
| data.infos.sha        | String | 否(当类型为文件时返回) | 文件sha                                    |
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的文件下载url                               |

##### 示例

```php
$bucketName = "myBucket";
$prefix= "/myFolder/2015-";
$result = Cosapi::prefixSearch($bucketName, $prefix, 20, 'eListBoth',0);
```



### 文件操作

#### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，调用者可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

##### 原型方法

```php
public static function upload($srcPath, $bucketName, $dstPath, $bizAttr = null);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                                 |
| ---------- | ------ | -------- | ---- | ---------------------------------------- |
| srcPath    | String | 是        | 无    | 本地要上传文件的全路径                              |
| bucketName | String | 是        | 无    | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstPath    | String | 是        | 无    | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttr    | String | 否        | null | 文件属性，业务端维护                               |

##### 返回值说明(json)

| **参数名**            | **类型** | 是否必然返回 | **参数描述**                   |
| ------------------ | ------ | ------ | -------------------------- |
| httpcode           | Int    | 是      | http响应码，请求正常时为200          |
| code               | Int    | 是      | 错误码，成功时为0                  |
| message            | String | 是      | 错误信息                       |
| data               | Array  | 是      | 返回数据                       |
| data.access_url    | Bool   | 是      | 生成的文件下载url                 |
| data.url           | String | 是      | 操作文件的url                   |
| data.resource_path | String | 是      | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```php
$srcPath= "/data/test.mp4";
$bucketName = "myBucket";
$dstPath = "/myFolder/test.mp4";
$result = Cosapi::upload($srcPath,$bucketName,dstPath ,"biz_attr");
```



#### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url和唯一标识resource_path（用于调用其他api）。

##### 方法原型

```php
public static function upload_slice(
            $srcPath, $bucketName, $dstPath, 
            $bizAttr = null, $sliceSize = self::DEFAULT_SLICE_SIZE, $session = null);
```

##### 参数说明

| **参数名**    | **类型** | **必须** | **默认值**    | **参数描述**                                 |
| ---------- | ------ | ------ | ---------- | ---------------------------------------- |
| srcPath    | String | 是      | 无          | 本地要上传文件的全路径                              |
| bucketName | String | 是      | 无          | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstPath    | String | 是      | 无          | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttr    | String | 否      | null       | 文件属性，业务端维护                               |
| sliceSize  | Int    | 否      | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置                      |
| session    | String | 否      | null       | 如果是断点续传, 则带上(唯一标识此文件传输过程的id, 由后台下发, 调用方透传) |

##### 返回值说明(json)

| **参数名**            | **类型** | **必然返回** | **参数描述**                   |
| ------------------ | ------ | -------- | -------------------------- |
| httpcode           | Int    | 是        | http响应码，请求正常时为200          |
| code               | Int    | 是        | 错误码，成功时为0                  |
| message            | String | 是        | 错误信息                       |
| data               | Array  | 是        | 返回数据                       |
| data.access_url    | Bool   | 是        | 生成的文件下载url                 |
| data.url           | String | 是        | 操作文件的url                   |
| data.resource_path | String | 是        | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```php
$srcPath= "/data/test.mp4";
$bucketName = "myBucket";
$dstPath = "/myFolder/";
$result = Cosapi::upload_slice($srcPath,$bucketName,dstPath ,"biz_attr");
```



#### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 原型方法

```php
public static function update($bucketName, $path, $bizAttr = null);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                          |
| ---------- | ------ | -------- | ------- | --------------------------------- |
| bucketName | String | 是        | 无       | bucket 名称                         |
| path       | String | 是        | 无       | 文件在文件服务端的全路径，不包括/appid/bucketname |
| bizAttr    | String | 否        | null    | 待更新的文件属性信息                        |

##### 返回值说明(json)

| **参数名**  | **类型** | **必然返回** | **参数描述**          |
| -------- | ------ | -------- | ----------------- |
| httpcode | Int    | 是        | http响应码，请求正常时为200 |
| code     | Int    | 是        | 错误码，成功时为0         |
| message  | String | 是        | 错误信息              |

##### 示例

```php
$bucketNam = "myBucket";
$path = "/myFolder/test.mp4";
$result = Cosapi::update($bucketName, $path,"attr_file_new");
```



#### 文件查询

接口说明：用于文件的查询，调用者可以通过此接口查询文件的各项属性信息。

##### 原型方法

```php
 public static function stat($bucketName, $path); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                          |
| ---------- | ------ | -------- | ------- | --------------------------------- |
| bucketName | String | 是        | 无       | bucket 名称                         |
| path       | String | 是        | 无       | 文件在文件服务端的全路径，不包括/appid/bucketname |

##### 返回值说明(json)

| **参数名**         | **类型** | **是否必然返回** | **参数描述**                       |
| --------------- | ------ | ---------- | ------------------------------ |
| httpcode        | Int    | 是          | http响应码，请求正常时为200              |
| code            | Int    | 是          | 错误码，成功时为0                      |
| message         | String | 是          | 错误信息                           |
| data            | Array  | 是          | 文件属性数据                         |
| data.name       | String | 是          | 文件或目录名                         |
| data.biz_attr   | String | 是          | 文件属性，业务端维护                     |
| data.ctime      | String | 是          | 文件的创建时间，unix时间戳                |
| data.mtime      | String | 是          | 文件的修改时间，unix时间戳                |
| data.filesize   | Int    | 是          | 文件大小                           |
| data.filelen    | Int    | 是          | 文件已传输大小(通过与filesize对比可知文件传输进度) |
| data.sha        | String | 是          | 文件sha                          |
| data.access_url | String | 是          | 生成的文件下载url                     |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/test.mp4";
$result = Cosapi::stat($bucketName, $path);
```



#### 文件删除

接口说明：用于文件的删除，调用者可以通过此接口删除已经上传的文件。



##### 原型方法

```php
public static function del($bucketName, $path);
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                          |
| ---------- | ------ | -------- | ------- | --------------------------------- |
| bucketName | String | 是        | 无       | bucket 名称                         |
| path       | String | 是        | 无       | 文件在文件服务端的全路径，不包括/appid/bucketname |

##### 返回值说明(json)

| **参数名**  | **类型** | **必然返回** | **参数描述**          |
| -------- | ------ | -------- | ----------------- |
| httpcode | Int    | 是        | http响应码，请求正常时为200 |
| code     | Int    | 是        | 错误码，成功时为0         |
| message  | String | 是        | 错误信息              |

##### 示例

```php
$bucketName = "myBucket";
$path = "/myFolder/test.mp4";
$result = Cosapi::del($bucketName, $path);
```







