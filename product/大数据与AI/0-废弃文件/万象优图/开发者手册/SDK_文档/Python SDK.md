本文档为万象优图V2版本和V2加强版的Python SDK文档，V1版本的Python SDK文档参见 万象优图[Python SDK说明文档-V1](/doc/product/275/Python SDK_V1)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。
## 1	开发准备
万象优图服务的python sdk的下载地址： https://github.com/tencentyun/python-sdk
### 1.1	前期准备
获取项目ID(appid)，bucket，secret_id和secret_key。
### 1.2	获取SDK
1. pip获取：
在开发环境命令行直接执行下面的命令即可导入python-sdk包。

```
pip install tencentyun
```
然后，参考api说明和sdk中提供的sample，开发代码即可。sample对应v1版本的restful api, samplev2对应v2版本的restful api。
2. 直接下载源码集成:
您也可以直接下载github上提供的源代码，集成到您的开发环境即可（依赖requests）。

## 2	API详细说明
### 2.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
V1版本的api和V2版本的api的签名并不相同。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[鉴权服务技术方案](/doc/product/275/签名与鉴权文档)
2．	方法
签名函数会自动根据传入的URL，进行不同方式的签名，这里对使用者是透明的。
V2加强版的签名:

```
  def get_app_sign_v2(bucket, fileid, expired)
```
V2版本的签名:

```
  def app_sign_v2(self, url, expired=0)
```
V1版本的签名:

```
  def app_sign(self, url, expired=0)
```
## 3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
url	|String	|是	|无|	需要操作的url
expired	|Int|	是	|无	|签名过期时间戳

返回值：

参数名|	类型|	参数描述
---------|---------|---------
httpcode|	Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String	|API错误信息
data|	Array|	API 返回数据
data.sign	|String	|签名串


示例代码：

```
    # 生成私密下载url
    auth = tencentyun.Auth(secret_id,secret_key)
    expired = int(time.time()) + 999
    sign = auth.get_app_sign_v2(bucket, fileid, expired)
    download_url = statRet['data']['download_url']
    print 'download_url:', download_url + '?sign=' + sign

    # 生成上传签名
    fileid = 'sample'+str(int(time.time()))
    expired = int(time.time()) + 999
    sign = auth.get_app_sign_v2(bucket, fileid, expired)
    print fileid, sign
```

### 2.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
def upload(self, filepath, bucket, fileid='', userid='0', magic_context='', params={})
def upload_binary(self, file_binary, bucket, fileid = '', userid = '0', magic_context = '', params = {})
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
filePath	|String|	是|	无|	本地图片文件路径
file_binary|	String|	是	|无	|base64编码后的字符串数据
bucket|	String|	是	|无	|空间名称
fileid	|String	|否|	空	|用户自定义文件名
userid|	String|	否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0
magicContext	|String|	否	|空	|上传成功后，用户自定义的回调参数
params	|array|	否	|空数组|	可选处理项，目前支持params[‘get’] => array() 用于指定上传是url中携带的get请求参数

返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int|	http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String	|API错误信息
data	|Dict|	API 返回数据
data.url|	String|	图片的管理URL
data.downloadUrl	|String|	图片的下载和访问URL
data.fileid|	String	|图片的唯一ID
data.info.0.0.width	|int|	图片宽度
data.info.0.0.height|	int	|图片高度

示例代码：

```
  image = tencentyun.ImageV2(appid,secret_id,secret_key)
  obj = image.upload('/tmp/amazon.jpg', bucket, fileid);
  print obj
```

### 2.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
def copy(self, bucket, fileid, userid='0') 
```
3．	参数和返回值
参数说明：

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
bucket	|String	|是	|无	|空间名称
fileid	|String|	是	|无|	图片唯一ID
userid	|String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int|	http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String	|API错误信息
data	|Dict|	API 返回数据
data.downloadUrl	|String|	图片的下载和访问URL
data.url	|String	|管理url


示例代码：

```
  // 复制
  copyRet = image.copy(bucket, fileid)
  download_url = copyRet['data']['download_url']
  print copyRet
```
### 2.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法
def stat(self, bucket, fileid, userid='0') 
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
bucket|	String|	是	|无|	空间名称
fileid	|String	|是|	无|	图片唯一ID
userid	|String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message	|String	|API错误信息
data	|Dict	|API 返回数据
data.downloadUrl	|String	|图片的下载和访问URL
data.url	|String|	管理url
data.fileid	|String	|图片的唯一ID
data.upload_time	|String	|图片的上传时间
data.size|	String|	图片的大小（Bytes）
data.md5	|String	|图片的md5值
data.width|	String|	图片的宽度（pixels）
data.height|	String|	图片的高度（pixels）

示例代码：

```
  // 查询管理信息
  statRet = image.stat(bucket, fileid)
```

### 2.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
def delete(self, bucket, fileid, userid='0') 
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值	|参数描述
---------|---------|---------|---------|---------
bucket|	String	|是|	无|	空间名称
fileid|	String	|是	|无|	图片唯一ID
userid|	String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名|	类型|	参数描述
---------|---------|---------
httpcode|	Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String|	API错误信息
data|	Dict|	空字典

示例代码：

```
  print image.delete(bucket, fileid)
```

### 2.6	图片下载
图片的下载直接使用图片下载url进行下载，具体参见Restful API[图片下载](/doc/product/275/RESTful API#7-.E5.9B.BE.E7.89.87.E4.B8.8B.E8.BD.BD)。
## 3 错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。