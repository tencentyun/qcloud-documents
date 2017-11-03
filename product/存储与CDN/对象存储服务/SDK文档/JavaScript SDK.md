## 开发准备

### SDK 获取

对象存储服务的Javascript SDK的下载地址： [https://github.com/tencentyun/cos-js-sdk](https://github.com/tencentyun/cos-js-sdk)

###  开发环境

1. SDK需要浏览器支持HTML 5；
2. SDK需要浏览器支持Flash；
3. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/document/product/430/5891) ；

### SDK 配置

直接下载github上提供的源代码，将SDK中sdk文件夹包含到您的项目中，使用SDK之前，加载相关支持的Javascript文件即可。

```javascript
<script type="text/javascript" src="sdk/jquery1x.min.js"></script>
<script type="text/javascript" src="sdk/qcloud_sdk.js"></script>
<script type="text/javascript" src="sdk/swfobject.js"></script>
```

本SDK需要jQuery的支持，如果您的项目已经引入jQuery，那么可以省略jquery1x.min.js的引入。

## 生成签名

### 多次有效签名

#### 方法原型

```javascript
public static function appSign($expired, $bucketName)
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| expired    | long   | 否        | 无       | 过期时间，Unix时间戳                             |
| bucketName | String | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](/document/product/430/5887) |

#### 返回结果说明

返回值：签名字符串

### 单次有效签名

#### 方法原型

```javascript
public static function appSign_once($path, $bucketName)
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](/document/product/430/5887) |
| path       | String | 是        | 无       | 文件路径，以斜杠开头，例如/filepath/filename，为文件在此bucketname下的全路径 |

#### 返回结果说明

返回值：签名字符串

## 目录操作

在进行接口调用操作前，需要生成 CosCloud 对象，对象原型入下：

```
var cos = new CosCloud(appid, signUrl);
```

+ appid：为项目的 APPID；


+ signUrl：为服务端签名地址，默认为当前目录下Sign.php。



SDK的每个方法都需要三个通用参数：

**successCallBack**：当方法能从服务端正确的取回数据时，回调的方法。结果以字符串形式返回，方法定义如下：

```
var successCallBack = function(result){
  $("#result").val(result);
};

```

**errorCallBack**：当请求服务端出现网络错误时，调用该方法。方法定义如下：

```
var errorCallBack = function(result){
  $("#result").val(result.responseText);
}

```

**bucketName**：bucket名称，bucket创建参见[创建Bucket

### 创建目录

接口说明：可以通过此接口在指定bucket下创建目录。

#### 方法原型

```javascript
cos.createFolder = function(success, error, bucketName, remotePath)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| ---------- | -------- | -------- | ------- | --------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack   |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName      |
| remotePath | String   | 是        | 无       | 需要创建目录的全路径            |

#### 返回结果说明

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

#### 示例

```javascript
cos.createFolder(successCallBack, errorCallBack, bucketName, "/newfolder/");
```

### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```javascript
 cos.updateFolder = function(success, error, bucketName, remotePath, bizAttribute)
```

#### 参数说明

| **参数名**      | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| ------------ | -------- | -------- | ------- | --------------------- |
| success      | Function | 是        | 无       | 参见通用参数successCallBack |
| error        | Function | 是        | 无       | 参见通用参数errorCallBack   |
| bucketName   | String   | 是        | 无       | 参见通用参数bucketName      |
| remotePath   | String   | 是        | 无       | 需要创建目录的全路径            |
| bizAttribute | String   | 是        | 无       | 新的目录绑定的属性信息           |

#### 返回结果说明

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```javascript
cos.updateFolder(successCallBack, errorCallBack, bucketName, "/newfolder/", "This is sdk test folder");
```

### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

#### 方法原型

```
 cos.getFolderStat = function(success, error, bucketName, remotePath)

```

#### 参数说明：

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| ---------- | -------- | -------- | ------- | --------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack   |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName      |
| remotePath | String   | 是        | 无       | 目录的全路径                |

#### 返回结果说明

| **参数名**       | **类型** | **参数描述**         |
| ------------- | ------ | ---------------- |
| code          | Int    | 错误码，成功时为0        |
| message       | String | 错误信息             |
| data          | Array  | 目录属性数据           |
| data.biz_attr | String | 目录绑定的属性信息，业务自行维护 |
| data.ctime    | String | 目录的创建时间，unix时间戳  |
| data.mtime    | String | 目录的修改时间，unix时间戳  |
| data.name     | String | 目录的名称            |

#### 示例

```javascript
cos.getFolderStat(successCallBack, errorCallBack, bucketName, "/newfolder/");
```

### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

#### 方法原型

```javascript
 cos.deleteFolder = function(success, error, bucketName, remotePath)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**              |
| ---------- | -------- | -------- | ------- | --------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack   |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName      |
| remotePath | String   | 是        | 无       | 目录的全路径                |

#### 返回结果说明

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```
cos.deleteFolder(successCallBack, errorCallBack, bucketName, "/newfolder/");
```

### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

#### 方法原型

```javascript
 cos.getFolderList = function(success, error, bucketName, remotePath, num, context, order, pattern, prefix)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值**   | **参数描述**                                 |
| ---------- | -------- | -------- | --------- | ---------------------------------------- |
| success    | Function | 是        | 无         | 参见通用参数successCallBack                    |
| error      | Function | 是        | 无         | 参见通用参数errorCallBack                      |
| bucketName | String   | 是        | 无         | 参见通用参数bucketName                         |
| remotePath | String   | 是        | 无         | 目录的全路径                                   |
| num        | int      | 是        | 无         | 要查询的目录/文件数量                              |
| context    | String   | 是        | 无         | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int      | 是        | 无         | 默认正序(=0), 填1为反序                          |
| pattern    | String   | 否        | eListBoth | eListBoth,eListDirOnly,eListFileOnly 默认both |
| prefix     | String   | 否        | 无         | 列出含此前缀的所有文件                              |


#### 返回结果说明

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
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
| data.infos.authority  | String | 否            | eInvalid,eWRPrivate,eWPrivateRPublic,文件可以与bucket拥有不同的权限类型，已经设置过权限的文件如果想要撤销，直接赋值为eInvalid，则会采用bucket的权限 |

#### 示例

```javascript
cos.getFolderList(successCallBack, errorCallBack, bucketName, "/", 20, "", 0);
```

## 文件操作

### 文件上传

接口说明：用于较小文件(一般小于10MB)的上传，可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

#### 方法原型

```javascript
cos.uploadFile = function(success, error, bucketName, remotePath, file)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                            |
| ---------- | -------- | -------- | ------- | ----------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack               |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                 |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                    |
| remotePath | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname  |
| file       | File     | 是        | 无       | 本地要上传文件的文件对象                        |
| insertOnly | Int      | 否        | 无       | insertOnly==0 表示允许覆盖文件 1表示不允许 其他值忽略 |

#### 返回结果说明

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```javascript
cos.uploadFile(successCallBack, errorCallBack, bucketName, "/tel.txt", files[0]);
```

### 文件分片上传

接口说明：用于较大文件(一般大于10MB)的上传，可以通过此接口上传较大文件并获得文件的url和唯一标识resource_path（用于调用其他api）。

#### 方法原型

```javascript
cos.sliceUploadFile = function(success, error, bucketName, remotePath, file)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | -------- | -------- | ------- | ---------------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack                    |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                      |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                         |
| remotePath | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| file       | File     | 是        | 无       | 本地要上传文件的文件对象                             |
| insertOnly | Int      | 否        | 无       | insertOnly==0 表示允许覆盖文件 1表示不允许 其他值忽略      |
| sliceSize  | Int      | 否        | 无       | 分片大小，正整数类型，目前支持512K,1M,2M,3M，512K==512*1024,1M==1*1024*1024 |

#### 返回结果说明

| **参数名**            | **类型** | **必然返回** | **参数描述**                   |
| ------------------ | ------ | -------- | -------------------------- |
| code               | Int    | 是        | 错误码，成功时为0                  |
| message            | String | 是        | 错误信息                       |
| data               | Array  | 是        | 返回数据                       |
| data.access_url    | Bool   | 是        | 生成的文件下载url                 |
| data.url           | String | 是        | 操作文件的url                   |
| data.resource_path | String | 是        | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```javascript
cos.sliceUploadFile(successCallBack, errorCallBack, bucketName, "/movie/" + files[0].name, files[0])
```

### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```javascript
 cos.getFileStat = function(success, error, bucketName, remotePath)
```

#### 参数说明：

| **参数名**        | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------------- | -------- | -------- | ------- | ---------------------------------------- |
| success        | Function | 是        | 无       | 参见通用参数successCallBack                    |
| error          | Function | 是        | 无       | 参见通用参数errorCallBack                      |
| bucketName     | String   | 是        | 无       | 参见通用参数bucketName                         |
| remotePath     | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| file           | File     | 是        | 无       | 本地要上传文件的文件对象                             |
| authority      | String   | 否        | 无       | eInvalid,eWRPrivate,eWPrivateRPublic,文件可以与bucket拥有不同的权限类型，已经设置过权限的文件如果想要撤销，直接赋值为eInvalid，则会采用bucket的权限 |
| custom_headers | String   | 否        | 无       | 自定义header对象                              |


#### 自定义header对象说明

| **参数名**             | **类型** | **是否必然返回** | **参数描述**  |
| ------------------- | ------ | ---------- | --------- |
| Cache-Control       | String | 否          | 文件的缓存机制   |
| Content-Type        | String | 否          | 文件的MIME信息 |
| Content-Disposition | String | 否          | MIME协议的扩展 |
| Content-Language    | String | 否          | 文件的语言     |
| x-cos-meta-自定义内容    | String | 否          | 自定义信息     |

#### 返回结果说明

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```javascript
cos.sliceUploadFile(successCallBack, errorCallBack, bucketName, "/movie/" + files[0].name, files[0])
```

###  文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

#### 方法原型

```javascript
cos.getFileStat = function(success, error, bucketName, remotePath)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                           |
| ---------- | -------- | -------- | ------- | ---------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack              |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                   |
| remotePath | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |

#### 自定义header对象说明

| **参数名**             | **类型** | **是否必然返回** | **参数描述**  |
| ------------------- | ------ | ---------- | --------- |
| Cache-Control       | String | 否          | 文件的缓存机制   |
| Content-Type        | String | 否          | 文件的MIME信息 |
| Content-Disposition | String | 否          | MIME协议的扩展 |
| Content-Language    | String | 否          | 文件的语言     |
| x-cos-meta-自定义内容    | String | 否          | 自定义信息     |

#### 返回结果说明

| **参数名**             | **类型** | **是否必然返回** | **参数描述**                       |
| ------------------- | ------ | ---------- | ------------------------------ |
| code                | Int    | 是          | 错误码，成功时为0                      |
| message             | String | 是          | 错误信息                           |
| data                | Array  | 是          | 文件属性数据                         |
| data.name           | String | 是          | 文件或目录名                         |
| data.biz_attr       | String | 是          | 文件属性，业务端维护                     |
| data.ctime          | String | 是          | 文件的创建时间，unix时间戳                |
| data.mtime          | String | 是          | 文件的修改时间，unix时间戳                |
| data.filesize       | Int    | 是          | 文件大小                           |
| data.filelen        | Int    | 是          | 文件已传输大小(通过与filesize对比可知文件传输进度) |
| data.sha            | String | 是          | 文件文件sha                        |
| data.access_url     | String | 是          | 生成的文件下载url                     |
| data.authority      | String | 否          | 无                              |
| data.custom_headers | String | 否          | 无                              |

#### 示例

```javascript
cos.getFileStat(successCallBack, errorCallBack, bucketName, "/tel.txt");
```

### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

#### 方法原型

```javascript
cos.deleteFile = function(success, error, bucketName, remotePath)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                           |
| ---------- | -------- | -------- | ------- | ---------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack              |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                   |
| remotePath | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |

#### 返回结果说明

| **参数名** | **类型** | **必然返回** | **参数描述**  |
| ------- | ------ | -------- | --------- |
| code    | Int    | 是        | 错误码，成功时为0 |
| message | String | 是        | 错误信息      |

#### 示例

```javascript
cos.deleteFile(successCallBack, errorCallBack, bucketName, "/tel.txt");
```


### 文件移动

接口说明：用于文件的移动和重命名。

#### 方法原型

```javascript
cos.moveFile = function(success, error, bucketName, remotePath, destPath, overWrite)
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                           |
| ---------- | -------- | -------- | ------- | ---------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack              |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                   |
| remotePath | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |
| destPath   | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |
| overWrite  | Int      | 否        | 无       | 是否覆盖同名文件, 0表示不覆盖 1表示覆盖 可选参数        |

#### 返回结果说明

| **参数名** | **类型** | **必然返回** | **参数描述**  |
| ------- | ------ | -------- | --------- |
| code    | Int    | 是        | 错误码，成功时为0 |
| message | String | 是        | 错误信息      |

#### 示例

```javascript
var destPath = "/222/tel.txt";
var overWrite = 1;
cos.moveFile(successCallBack, errorCallBack, bucketName, "/tel.txt", destPath, overWrite);
```


