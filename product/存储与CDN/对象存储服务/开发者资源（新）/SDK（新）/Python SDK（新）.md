### 开发准备

#### SDK 获取

COS服务的Python2 sdk的下载地址： [https://github.com/tencentyun/cos-python-sdk.git](https://github.com/tencentyun/cos-python-sdk.git)



#### 开发环境

1. sdk采用Python2.7开发， 推荐使用相同的版本。如果使用其他版本，建议不要直接导入，自行调试为佳；
2. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/doc/product/227/权限控制)。






#### SDK 配置

下载 Python SDK 后，可通过如下方法进行安装：

+ 使用命令 pip install qcloud_cos 安装


+ 如果安装了git 命令行，执行git clone [https://github.com/tencentyun/cos-python-sdk.git](https://github.com/tencentyun/cos-python-sdk.git) 或者直接在github下载zip包。

注意：SDK 依赖 requests 包，使用方法二需自行安装。

在 IDE 中导入 qcloud_cos 包

```php
import qcloud_cos
```

若需支持 HTTPS，将 qcloud_cos/conf.py 文件中变量 API_COS_END_POINT 中的 http 修改为 https 即可。

```php
const API_COSAPI_END_POINT = 'https://web.file.myqcloud.com/files/v1/';
```



### 生成签名

#### 签名构造函数

##### 构造函数原型

```python
def __init__(self, secret_id, secret_key)
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | 默认值  | **参数描述**                           |
| ---------- | ------ | -------- | ---- | ---------------------------------- |
| secret_id  | String | 是        | 无    | 开发者的授权secret_id                    |
| secret_key | String | 是        | 无    | 开发者的授权secret_key，获取方式参考[权限控制](/doc/product/227/权限控制)。 |



#### 多次有效签名

##### 原型方法

```python
def sign_more(self, bucket, expired)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                           |
| ------- | ------ | -------- | ------- | ---------------------------------- |
| expired | long   | 是        | 无       | 过期时间，Unix时间戳                       |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](#) 。 |

##### 返回值说明

方法的返回结果为：签名字符串

##### 示例

```python
import qcloud_cos
qcloud_cos.conf.set_app_info(appid, secret_id, secret_key)
auth = qcloud_cos.Auth(secret_id, secret_key)
sign = auth.sign_more('bucketname', time.time() + 86400)
```



#### 单次有效签名

##### 原型方法

```php
def sign_once(self, bucket, fileid)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| fileid  | String | 是        | 无       | 过期时间，Unix时间戳                             |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](#) 。       |
| fileid  | String | 是        | 无       | 文件唯一的标识，格式/appid/bucketname/filepath/filename，其中/filepath/filename为文件在此bucketname下的全路径， |

##### 返回结果说明

方法的返回结果为：签名字符串

##### 示例

```python
import qcloud_cos
qcloud_cos.conf.set_app_info(appid, secret_id, secret_key)
auth = qcloud_cos.Auth(secret_id, secret_key)
sign = auth.sign_once('bucketname', '/appid/bucketname/myFolder/myFile.txt')
```



更多签名相关的详细说明，请参考[权限控制](#) 。



### 目录操作

#### 创建目录

接口说明：用于目录的创建，可以通过此接口在指定bucket下创建目录。

##### 方法原型

```python
def createFolder(self, bucket, path, bizattr='')
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，如果忘记，api会自动补齐   |
| bizattr | String | 否        | 空串      | 目录绑定的属性信息，业务自行维护                         |

##### 返回值说明(json)

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.createFolder('bucketname', '/myFolder/', 'bizAttribute')
```



#### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```python
def updateFolder(self, bucket, path, bizattr)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| bizattr | String | 是        | 无       | 新的目录绑定的属性信息                              |

##### 返回值说明(json)

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.updateFolder('bucketname', 'myFolder/', 'bizAttribute')
```



#### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

##### 方法原型

```python
def statFolder(self, bucket, path) 
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回值说明(json)

| **参数名**       | **类型** | **参数描述**         |
| ------------- | ------ | ---------------- |
| code          | Int    | 错误码，成功时为0        |
| message       | String | 错误信息             |
| data          | Array  | 目录属性数据           |
| data.biz_attr | String | 目录绑定的属性信息，业务自行维护 |
| data.ctime    | String | 目录的创建时间，unix时间戳  |
| data.mtime    | String | 目录的修改时间，unix时间戳  |
| data.name     | String | 目录的名称            |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.statFolder('bucketName', 'myFolder/')
```



#### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

##### 方法原型

```python
def deleteFolder(self, bucket, path) 
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回值说明(json)

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.deleteFolder('bucketname', 'myFolder/')
```



#### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

##### 方法原型

```python
def list(self, bucket, path, num=20, pattern='eListBoth', order=0, context='')
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值**   | **参数描述**                                 |
| ------- | ------ | -------- | --------- | ---------------------------------------- |
| bucket  | String | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无         | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| num     | int    | 否        | 20        | 要查询的目录/文件数量                              |
| context | String | 否        | 空串        | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order   | int    | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern | String | 否        | eListBoth | pattern eListFileOnly:只是文件，ListDirOnly:只是文件夹，eListBoth:全部 |

##### 返回值说明(json)

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

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.list('bucketname', 'myFolder/', 30, 'eListBoth', 0, '')
```



#### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

##### 方法原型

```python
def prefixSearch(self, bucket, path, prefix='', num=20, pattern='eListBoth', order=0, context='')
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值**   | **参数描述**                                 |
| ------- | ------ | -------- | --------- | ---------------------------------------- |
| bucket  | String | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无         | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| prefix  | String | 否        | 空串        | 读取文件/目录前缀                                |
| num     | int    | 否        | 20        | 要查询的目录/文件数量                              |
| context | String | 否        | 空串        | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order   | int    | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern | String | 否        | eListBoth | pattern eListFileOnly=>仅列举文件，ListDirOnly=>仅列举目录，eListBoth=>列举文件和目录 |

##### 返回值说明(json)

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

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.prefixSearch('bucketname', 'myFolder/', '20150606_', 30, 'eListBoth', 0, '')
```



### 文件操作

#### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，可以通过此接口上传较小的文件并获得文件的下载的url，较大的文件请使用分片上传接口。

##### 方法原型

```python
def upload(self, filepath, bucket, dstpath, bizattr='')
```

##### 参数说明

| **参数名**  | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| -------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket   | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstpath  | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| filepath | String | 是        | 无       | 本地要上传文件的全路径                              |
| bizattr  | String | 否        | 空串      | 文件属性，业务端维护                               |

##### 返回值说明(json)

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.upload('test.mp4', 'bucketName', 'myFolder/myFile.txt')
```



#### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url。

##### 方法原型

```python
def upload_slice(self, filepath, bucket, dstpath, bizattr='', slice_size=0, session='')
```

##### 参数说明

| **参数名**   | **类型** | **是否必填** | **默认值**    | **参数描述**                                 |
| --------- | ------ | -------- | ---------- | ---------------------------------------- |
| filepath  | String | 是        | 无          | 本地要上传文件的全路径                              |
| bucket    | String | 是        | 无          | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstpath   | String | 是        | 无          | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizattr   | String | 否        | 空串         | 文件属性，业务端维护                               |
| sliceSize | Int    | 否        | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置，传0代表使用默认值。           |
| session   | String | 否        | 空串         | 续传时透传的session，一般不设置。                     |

##### 返回值说明(json)

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.upload_slice('test.mp4', 'bucketName', 'myFolder/myFile.txt', 2*1024*1024)
```



#### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```python
def updateFile(self, srcpath, bucket, dstpath, bizattr)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| srcpath | String | 是        | 无       | 本地文件路径                                   |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizattr | String | 是        | 无       | 待更新的文件属性信息                               |

##### 返回值(json)

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

##### 示例

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.updateFile('bucketname', 'myFolder/myFile.txt', 'bizattr')
```



#### 文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

##### 方法原型

```python
def statFile(self, bucket, path)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

##### 返回值说明(json)

| **参数名**         | **类型** | **是否必然返回** | **参数描述**                       |
| --------------- | ------ | ---------- | ------------------------------ |
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

```python
cos = qcloud_cos.Cos(appid, secret_id, secret_key)
result = cos.statFile('bucketname', 'myFolder/myFile.txt')
```



#### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

##### 方法原型

```python
def deleteFile(self, bucket, path)
```

##### 参数说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| bucket  | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path    | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

##### 返回值(json)

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

##### 示例

```python
cos = qcloud_cos.Cosappid, secret_id, secret_key)
result = cos.deleteFile('bucketname', 'myFolder/myFile.txt')
```