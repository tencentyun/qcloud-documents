## 开发准备

### 相关资源

* [GitHub地址](https://github.com/tencentyun/cos-python-sdk-v4) GitHub项目地址，欢迎贡献代码以及反馈问题。

* [PyPi](https://pypi.python.org/pypi/qcloud_cos_v4) PyPi项目地址 。
（本版本SDK基于JSON API封装组成）

### 环境依赖

python 2.7

获取python版本的方法:

- Linux Shell

```shell
$ python -V
Python 2.7.11
```

- Windows cmd

```shell
D:\>python -V
Python 2.7.11
```

如果提示不是内部或外部命令，请现在windows环境变量PATH里添加上python的绝对路径

### 安装SDK

- pip安装

```shell
pip install qcloud_cos_v4
```

- 源码安装

github上下载SDK, 解压后如下执行(如果提示permission deny, 需要有管理员权限)

```shell
python setup.py install
```

### 卸载SDK

```shell
pip uninstall qcloud_cos_v4
```


## 生成客户端对象

### 初始化客户端


```python
	appid = 100000                  # 替换为用户的appid
    secret_id = u'xxxxxxxx'         # 替换为用户的secret_id
    secret_key = u'xxxxxxx'         # 替换为用户的secret_key
    region_info = "sh"             # 替换为用户的region，例如 sh 表示华东园区, gz 表示华南园区, tj 表示华北园区
    cos_client = CosClient(appid, secret_id, secret_key, region=region_info)
```



### 自定义接入点

如果需要使用自定义的接入域名，可以通过下面的方式设置
```python
	conf = CosConfig(hostname='', download_hostname='')
	cos_client.set_config(conf)
```

## 文件操作

### 上传文件

#### 方法原型

```python
def upload_file(self, request)
```

#### 参数说明

|   参数名   |        类型         | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | UploadFileRequest |  无   | 上传文件类型请求 |

|  request成员  |      类型      | 默认值  |    设置方法    |                    描述                    |
| :---------: | :----------: | :--: | :--------: | :--------------------------------------: |
| bucket_name |   unicode    |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   |   unicode    |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
| local_path  |   unicode    |  无   | 构造函数或set方法 |              要上传的本地文件的绝对路径               |
|  biz_attr   |   unicode    |  空   | 构造函数或set方法 |           文件的备注，主要用于对该文件用途的描述            |
| insert_only | int     (枚举) |  1   | 构造函数或set方法 | 是否直插入不覆盖已存在的文件, 1表示只直插入不覆盖, 当文件存在返回错误 0 表示允许覆盖 |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

#### 示例

```python
    request = UploadFileRequest(bucket, u'/sample_file.txt', u'local_file_1.txt')
    upload_file_ret = cos_client.upload_file(request)
```

### 获取文件属性

#### 方法原型

```python
def stat_file(self, request)
```

#### 参数说明

|   参数名   |      参数类型       | 默认值  |   参数描述   |
| :-----: | :-------------: | :--: | :------: |
| request | StatFileRequest |  无   | 获取文件属性请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

#### 示例

```python
    request = StatFileRequest(bucket, u'/sample_file.txt')
    stat_file_ret = cos_client.stat_file(request)
```

### 更新文件属性

#### 方法原型

```python
def update_file(self, request)
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | UpdateFileRequest |  无   | 更新文件属性请求 |

|      request成员      |      类型      | 默认值  |    设置方法    |                    描述                    |
| :-----------------: | :----------: | :--: | :--------: | :--------------------------------------: |
|     bucket_name     |   unicode    |  无   | 构造函数或set方法 |                 bucket名称                 |
|      cos_path       |   unicode    |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
|      biz_attr       |   unicode    |  无   |   set方法    |           文件的备注，主要用于对改文件用途的描述            |
|      authority      | unicode (枚举) |  无   |   set方法    | 文件权限，默认是继承bucket的权限合法取值: eInvalid(继承bucket), eWRPrivate(私有读写), eWPrivateRPublic(私有写, 公有读) |
|    cache_control    |   unicode    |  无   |   set方法    |           参见HTTP的Cache-Control           |
|    content_type     |   unicode    |  无   |   set方法    |           参见HTTP的Content-Type            |
|  content_language   |   unicode    |  无   |   set方法    |         参见HTTP的Content-Language          |
| content_disposition |   unicode    |  无   |   set方法    |        参见HTTP的Content-Disposition        |
|     x-cos-meta-     |   unicode    |  无   |   set方法    | 自定义HTTP 头，参数必须以x-cos-meta-开头，值由用户定义，可设置多个 |

**tips:** 用户可以在以上这些属性中选择几个进行更新。如果本次只更新HTTP头部cache_control，content_type, content_disposition和x-cos-meta-这四个中的某几个，其他的几个没有更新和设置，那么其他没有被设置的头部会被清除删除掉，不会出现，即这4个属性会出现整体一起更新变动。


#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = UpdateFileRequest(bucket, u'/sample_file.txt')

    request.set_biz_attr(u'这是个demo文件')            # 设置文件biz_attr属性
    request.set_authority(u'eWRPrivate')              # 设置文件的权限
    request.set_cache_control(u'cache_xxx')           # 设置Cache-Control
    request.set_content_type(u'application/text')     # 设置Content-Type
    request.set_content_disposition(u'ccccxxx.txt')   # 设置Content-Disposition
    request.set_content_language(u'english')          # 设置Content-Language
    request.set_x_cos_meta(u'x-cos-meta-xxx', u'xxx') # 设置自定义的x-cos-meta-属性
    request.set_x_cos_meta(u'x-cos-meta-yyy', u'yyy') # 设置自定义的x-cos-meta-属性

    update_file_ret = cos_client.update_file(request)
```

### 下载文件

#### 方法原型

```python
def download_file(self, request)
```

#### 参数说明

|   参数名   |      参数类型      | 默认值  |  参数描述  |
| :-----: | :------------: | :--: | :----: |
| request | DownloadFileRequest |  无   | 下载文件请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
|  local_filename | unicode | 无 | 构造函数 | 本地文件路径|


#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = DownloadFileRequest(bucket, u'/sample_file_move.txt', u'/tmp/a.txt')
    download_ret = cos_client.download_file(request)
```


### 删除文件

#### 方法原型

```python
def del_file(self, request)
```

#### 参数说明

|   参数名   |      参数类型      | 默认值  |  参数描述  |
| :-----: | :------------: | :--: | :----: |
| request | DelFileRequest |  无   | 删除文件请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = DelFileRequest(bucket, u'/sample_file_move.txt')
    del_ret = cos_client.del_file(request)
```

## 目录操作

### 创建目录

#### 方法原型

```python
def create_folder(self, request)
```

#### 参数说明

|   参数名   |        参数类型         | 默认值  |  参数描述  |
| :-----: | :-----------------: | :--: | :----: |
| request | CreateFolderRequest |  无   | 创建目录请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
|  biz_attr   | unicode |  空   |   set方法    |            目录的备注，主要用于对目录用途的描述            |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = CreateFolderRequest(bucket, u'/sample_folder/')
    create_folder_ret = cos_client.create_folder(request)
```

### 获取目录属性

#### 方法原型

```python
def stat_folder(self, request)
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | StatFolderRequest |  无   | 获取目录属性请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

#### 示例

```python
    request = StatFolderRequest(bucket, u'/sample_folder/')
    stat_folder_ret = cos_client.stat_folder(request)
```



### 更新目录属性

#### 方法原型

```python
def update_folder(self, request)
```

#### 参数说明

|   参数名   |        参数类型         | 默认值  |   参数描述   |
| :-----: | :-----------------: | :--: | :------: |
| request | UpdateFolderRequest |  无   | 更新目录属性请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
|  biz_attr   | unicode |  空   |   set方法    |            目录的备注，主要用于对目录用途的描述            |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = UpdateFolderRequest(bucket, u'/sample_folder/')
    request.set_biz_attr(u'这是一个测试目录')
    update_folder_ret = cos_client.update_folder(request)
```

### 获取目录列表

#### 方法原型

```python
def list_folder(self, request)
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | ListFolderRequest |  无   | 获取目录成员请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
|     num     |   int   | 199  | 构造函数或set方法 |             获取列表成员的数量，最大为199             |
|   prefix    | unicode |  空   | 构造函数或set方法 | 搜索成员的前缀, 例如prefix为test表示只搜索以test开头的文件或目录 |
|   context   | unicode |  空   | 构造函数或set方法 | 透传字段，从响应的返回内容中得到。若查看第一页，则将空字符串作为 context 传入。若需要翻页，需要将前一页返回内容中的 context 透传到参数中。 |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含成员列表, 详情请参见返回值模块 |

#### 示例

```python
    request = ListFolderRequest(bucket, u'/sample_folder/')
    list_folder_ret = cos_client.list_folder(request)
```

### 删除目录

#### 方法原型

```python
def del_folder(self, request)
```

#### 参数说明

|   参数名   |       参数类型       | 默认值  |  参数描述  |
| :-----: | :--------------: | :--: | :----: |
| request | DelFolderRequest |  无   | 删除目录请求 |

|  request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cos_path   | unicode |  无   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |

#### 返回值

| 返回值类型 |                  返回值描述                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```python
    request = DelFolderRequest(bucket, u'/sample_folder/')
    delete_folder_ret = cos_client.del_folder(request)
```

## 签名管理

签名模块提供了生成多次签名、单次签名和下载签名的接口，其中多次签名和单次签名在文件和目录操作的api内部使用，用户不用关心，下载签名用于方便用户生成下载私有bucket的文件签名。

### 多次签名

```python
def sign_more(self, bucket, cos_path, expired)
```

#### 使用场景

上传文件, 重命名文件, 创建目录, 获取文件目录属性, 拉取目录列表

#### 参数说明

| 参数名      |  参数类型   | 默认值  |      参数描述       |
| -------- | :-----: | :--: | :-------------: |
| bucket   | unicode |  无   |    bucket名称     |
| cos_path | unicode |  无   |    要签名的cos路径    |
| expired  |   int   |  无   | 签名过期时间, UNIX时间戳 |

#### 返回值

base64编码的字符串

#### 示例

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_more(u'mybucket', u'/pic/1.jpg',  int(time.time()) + 600)
```

### 单次签名

```python
def sign_once(self, bucket, cos_path)
```

#### 使用场景

删除和更新文件目录

#### 参数说明

|   参数名    |  参数类型   | 默认值  |   参数描述    |
| :------: | :-----: | :--: | :-------: |
|  bucket  | unicode |  无   | bucket名称  |
| cos_path | unicode |  无   | 要签名的cos路径 |

#### 返回值

base64编码的字符串

#### 示例

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_once(u'mybucket', u'/pic/1.jpg')
```

### 下载签名

```python
def sign_download(self, bucket, cos_path, expired)
```

#### 使用场景

生成文件的下载签名, 用于下载私有bucket的文件

#### 参数说明

|   参数名    |  参数类型   | 默认值  |      参数描述       |
| :------: | :-----: | :--: | :-------------: |
|  bucket  | unicode |  无   |    bucket名称     |
| cos_path | unicode |  无   |    要签名的cos路径    |
| expired  |   int   |  无   | 签名过期时间, UNIX时间戳 |

#### 返回值

base64编码的字符串

#### 示例

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_download(u'mybucket', u'/pic/1.jpg',  int(time.time()) + 600)
```

## 返回码

| code |                  含义                  |
| :--: | :----------------------------------: |
|  0   |                 操作成功                 |
|  -1  | 输入参数错误, 例如输入的本地文件路径不存在, cos文件路径不符合规范 |
|  -2  |             网络错误, 如404等              |
|  -3  |           连接cos时发生异常，如连接超时           |
| -71  |           操作频率过快，触发cos的攻击            |
