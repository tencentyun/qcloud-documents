## 开发准备

### SDK 获取

COS服务的Node.js sdk的下载地址： [https://github.com/tencentyun/cos-nodejs-sdk.git](https://github.com/tencentyun/cos-nodejs-sdk.git)

### 开发环境

1. sdk采用Node.js v0.10.29版本开发， 推荐使用相同的版本。
2. 从控制台获取APP ID、SecretID、SecretKey，详情参考权限控制。


### SDK 配置

下载 Node.js SDK 后，可通过以下两种方式安装：

+ 执行 npm install qcloud_cos 直接安装。


+ 执行git clone [https://github.com/tencentyun/cos-nodejs-sdk.git](https://github.com/tencentyun/cos-nodejs-sdk.git) 或者直接在github网站下载zip包

注意：sdk依赖formstream包，使用方法二需要自行安装此包。

在IDE中导入qcloud_cos包

```Node.js
var qcloud = require('qcloud_cos');
```

若需要支持 HTTPS 协议上传，则将 qcloud_cos/lib/conf.js 文件中变量 API_COS_END_POINT 中的http修改为 https 即可。

## 生成签名

### 多次有效签名

#### 方法原型

```
function signMore(bucket, expired);
```

#### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| expired | long   | 是        | 无       | 过期时间，Unix时间戳                             |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |

#### 返回结果说明

签名字符串。

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

var expired = parseInt(Date.now() / 1000) + conf.EXPIRED_SECONDS;
var sign  = qcloud.auth.signMore(bucket, expired);
```

### 单次有效签名

#### 方法原型

```
function signOnce(bucket, fileid);
```

#### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| fileid  | String | 是        | 无       | 文件唯一的标识，格式/appid/bucketname/filepath/filename，其中/filepath/filename为文件在此bucketname下的全路径 |

#### 返回结果说明

签名字符串

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

var sign  = qcloud.auth.signOnce(bucket, 		'/'+conf.APPID+'/'+bucketname+'/'+remoteFilepath);
```

更多签名相关详细说明，请参考[权限控制](https://cloud.tencent.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF) 。

## 目录操作

### 创建目录

接口说明：用于目录的创建，可以通过此接口在指定bucket下创建目录。

#### 方法原型

```
function createFolder(bucket, path, bizattr, callback);
```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，如果忘记api会补齐      |
| bizattr  | String   | 否        | 空串      | 目录绑定的属性信息，业务自行维护                         |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

#### 返回结果说明

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.createFolder('bucketname', '/myFolder/', function(ret) {
	//deal with ret
});
```

### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```
function updateFolder(bucket, path, bizattr, callback);
```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，如果忘记api会补齐      |
| bizattr  | String   | 是        | 无       | 新的目录绑定的属性信息                              |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

#### 返回结果说明

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.updateFolder('bucketname', '/myFolder/', 'bizAttribute', function(ret) {//deal with ret});
```

### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

#### 方法原型

```
function statFolder(bucket, path, callback);

```

#### 参数说明

| **参数名**  | **类型**   | **是否必须** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，如果忘记api会补齐          |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

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

```
var qcloud = require('qcloud_cos');
//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.statFolder('bucketname', '/myFolder/', function(ret) {
	//deal with ret
});
```

### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

#### 方法原型

```
function deleteFolder(bucket, path, callback);

```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，如果忘记api会补齐          |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

#### 返回结果说明

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.deleteFolder('bucketname', '/myFolder/', function(ret) {
	//deal with ret
});
```

### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

#### 方法原型

```
function list(bucket, path, num, pattern, order, context, callback);
```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值**   | **参数描述**                                 |
| -------- | -------- | -------- | --------- | ---------------------------------------- |
| bucket   | String   | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无         | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| num      | int      | 否        | 20        | 要查询的目录/文件数量                              |
| context  | String   | 否        | 空串        | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order    | int      | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern  | String   | 否        | eListBoth | pattern eListFileOnly=>仅列举文件，ListDirOnly=>仅列举目录，eListBoth=>列举目录&文件 |
| callback | function | 否        | 输出返回结果    | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

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

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.list('bucketname', '/myFolder/', 20, 'eListBoth', 0, '', function(ret) {//deal with ret});
```

### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

#### 方法原型

```
function prefixSearch(bucket, path, prefix, num, pattern, order, context, callback);
```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值**   | **参数描述**                                 |
| -------- | -------- | -------- | --------- | ---------------------------------------- |
| bucket   | String   | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无         | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| prefix   | String   | 否        | 空串        | 读取文件/目录前缀                                |
| num      | int      | 否        | 20        | 要查询的目录/文件数量                              |
| context  | String   | 否        | 空串        | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order    | int      | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern  | String   | 否        | eListBoth | pattern eListFileOnly=>仅列举文件；ListDirOnly=>仅列举目录；eListBoth=>列举文件&目录 |
| callback | function | 否        | 输出返回结果    | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

#### 返回结果说明

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
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

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.prefixSearch('bucketname', '/myFolder/', '20150606_', 20, 'eListBoth', 0, '', function(ret) {
	//deal with ret
});
```

## 文件操作

### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

#### 方法原型

```
function upload(filePath, bucket, dstpath, bizattr, insertOnly, callback);
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket     | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| dstpath    | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| filepath   | String   | 是        | 无       | 本地要上传文件的全路径                              |
| bizattr    | String   | 否        | 空串      | 文件属性，业务端维护                               |
| insertOnly | Int      | 否        | 无       | insertOnly==0 表示允许覆盖文件 1表示不允许 其他值忽略      |
| callback   | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

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

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.upload('test.mp4', 'bucketName', '/myFolder/mycos.txt', 1, function(ret) {
	//deal with ret
});
```

### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url和唯一标识resource_path（用于调用其他api）。

#### 方法原型

```
function upload_slice(filePath, bucket, dstpath, bizattr, slice_size, session, insertOnly, callback);
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值**    | **参数描述**                                 |
| ---------- | -------- | -------- | ---------- | ---------------------------------------- |
| bucket     | String   | 是        | 无          | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| dstpath    | String   | 是        | 无          | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| filepath   | String   | 是        | 无          | 本地要上传文件的全路径                              |
| bizattr    | String   | 否        | 空串         | 文件属性，业务端维护                               |
| sliceSize  | Int      | 否        | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置                      |
| session    | String   | 否        | 空串         | 续传时透传的session，一般不设置。                     |
| insertOnly | Int      | 否        | 无          | insertOnly==0 表示允许覆盖文件 1表示不允许 其他值忽略      |
| callback   | function | 否        | 输出返回结果     | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

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

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.upload_slice('test.mp4', 'bucketName', '/myFolder/mycos.txt', 'bizattr', 2*1024*1024, null, 1, function(ret) {
	//deal with ret
});
```

### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```
function updateFile(bucket, path, bizattr, authority, custom_headers, callback);
```

#### 参数说明

| **参数名**        | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket         | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path           | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizattr        | String   | 是        | 无       | 待更新的文件属性信息                               |
| authority      | String   | 否        | 无       | eInvalid,eWRPrivate,eWPrivateRPublic,文件可以与bucket拥有不同的权限类型，已经设置过权限的文件如果想要撤销，直接赋值为eInvalid，则会采用bucket的权限 |
| custom_headers | String   | 否        | 无       | 自定义header对象                              |
| callback       | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |


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

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

var headers = {
    "Cache-Control": "no-cache",
    "Content-Type" : "application/json"
};

qcloud.cos.updateFile('bucketName', '/myFolder/test.txt', 'bizattr', 'eWRPrivate', headers, function(ret) {
	//deal with ret
});
```

### 文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

#### 方法原型

```
function statFile(bucket, path, callback);
```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

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
| data.sha            | String | 是          | 文件sha                          |
| data.access_url     | String | 是          | 生成的文件下载url                     |
| data.authority      | String | 否          | 无                              |
| data.custom_headers | String | 否          | 无                              |

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.statFile('bucketName', '/myFolder/test.txt', function(ret) {
	//deal with ret
});
```

### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

#### 方法原型

```
function deleteFile(bucket, path, callback);

```

#### 参数说明

| **参数名**  | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | -------- | -------- | ------- | ---------------------------------------- |
| bucket   | String   | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path     | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| callback | function | 否        | 输出返回结果  | 结构为function(ret){}的函数，ret为json结构，默认直接输出。 |

#### 返回结果说明

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx'); 

qcloud.cos.deleteFile('bucketName', '/myFolder/test.txt', function(ret) {
	//deal with ret
});
```


### 文件移动

接口说明：用于文件的移动和重命名。

#### 方法原型

```javascript
function moveFile(bucket, path, destPath, overWrite, callback);
```

#### 参数说明

| **参数名**    | **类型**   | **是否必填** | **默认值** | **参数描述**                           |
| ---------- | -------- | -------- | ------- | ---------------------------------- |
| success    | Function | 是        | 无       | 参见通用参数successCallBack              |
| error      | Function | 是        | 无       | 参见通用参数errorCallBack                |
| bucketName | String   | 是        | 无       | 参见通用参数bucketName                   |
| path       | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |
| destPath   | String   | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname |
| overWrite  | Int      | 否        | 无       | 是否覆盖同名文件, 0表示不覆盖 1表示覆盖 可选参数        |

#### 返回结果说明

| **参数名** | **类型** | **必然返回** | **参数描述**  |
| ------- | ------ | -------- | --------- |
| code    | Int    | 是        | 错误码，成功时为0 |
| message | String | 是        | 错误信息      |

#### 示例

```javascript
var qcloud = require('qcloud_cos');

//如果conf.js中已经设置好APPID和SECRET_KEY则不需要此步骤。
qcloud.conf.setAppInfo('10000','xxxxxx','xxxxxx');

qcloud_cos.cos.moveFile('0001', '123/test02.js', '/345/test01.js', 0, function(ret) {
    console.log('moveFile done');
    console.log(ret);
    console.log('###########');
});
```