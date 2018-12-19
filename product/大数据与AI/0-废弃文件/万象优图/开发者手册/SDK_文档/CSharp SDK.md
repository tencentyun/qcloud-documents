本文档为万象优图V2加强版的C# SDK文档
## 1 开发准备
万象优图的C# SDK的下载地址： https://github.com/tencentyun/pic-donet-sdk
前期准备
1.	sdk依赖C# 4.0版本及以上， 推荐使用相同的版本。
2.	获取项目ID(appid)，bucket，secret_id和secret_key；
获取SDK
直接下载github上提供的源代码，集成到您的开发环境。 
## 2 API详细说明
### 2.1 生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[鉴权技术服务方案](/doc/product/275/签名与鉴权文档)
2．	方法
多次有效签名

```
 public static string Signature(int appId, string secretId, string secretKey, long expired, string bucketName)
```
单次有效签名

```
 public static string SignatureOnce(int appId, string secretId, string secretKey, string bucketName, string fileId)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
appId|	int|	是|	无|	AppId
secretId|	string|	是|	无|	Secret Id
secretKey|	string|	是|	无|	Secret Key
expired|	long|	否|	无|	过期时间，Unix时间戳
bucketName|	string|	否|	无|	bucket名称，bucket创建参见创建Bucket
fileId|	string|	是|	无|	资源存储的唯一标识

返回值：签名字符串
示例代码：

```
var sign = Sign.Signature(appId, secretId, secretKey, expired, bucketName); //多次有效签名调用例子
var sign = Sign.SignatureOnce(appId, secretId, secretKey, bucketName, fileId); //单次有效签名调用例子
```
### 2.2 图片上传
1．	接口说明
直接上传单张图片, 目前只支持20M以内的图片。
2．	方法

```
 public string Upload(string bucketName, string localPath, string fileId = null)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucketName|	string|	是|	无|	bucket名称
localPath|	string|	是|	无|	本地图片地址
fileId|	string|	否|	空字符串|	资源存储的唯一标识


返回值,json格式字符串：

参数名|	类型|	参数描述
---------|---------|---------
code|	int|	服务器错误码, 0为成功
message|	string|	服务器返回的信息
data|	Array|	具体查询数据. 内容见下表

data里面字段描述:

参数名|	类型|	参数描述
---------|---------|---------
url|	string|	资源url(用于restful api交互, 如查询,复制,删除资源)
download_url|	string|	生成的下载资源url(用于下载)
fileid|	string|	生成的资源唯一标识符

示例代码：

```
result = pic.Upload(bucketName, @"d:\Tulips.jpg");
```
### 2.3 图片复制
1．	接口说明
将图片复制一份(保留原有图片)。
2．	方法

```
 public string Copy(string bucketName, string fileId)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucketName|	string|	是|	无|	bucket名称
fileId|	string|	是|	无|	生成的资源唯一标识符


返回值,json格式字符串：

参数名|	类型|	参数描述
---------|---------|---------
code|	int|	服务器错误码, 0为成功
message|	string|	服务器返回的信息
data|	Array|	具体查询数据. 内容见下表

data里面字段描述:

参数名|	类型|	参数描述
---------|---------|---------
url|	string|	资源url(用于restful api交互, 如查询,复制,删除资源)
download_url|	string|	生成的下载资源url(用于下载)

示例代码：

```
result = pic.Copy(bucketName, fileId);
```
### 2.4 图片查询
1．	接口说明
查看文件的属性信息，包含：文件哈希值、文件大小、上传时间等，图片和视频返回的信息会有所不同。
2．	方法

```
 public string Query(string bucketName, string fileId)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucketName|	string|	是|	无|	bucket名称
fileId|	string|	是|	无|	生成的资源唯一标识符

返回值,json格式字符串：

参数名|	类型|	参数描述
---------|---------|---------
code|	int|	服务器错误码, 0为成功
message|	string|	服务器返回的信息
data|	Array|	具体查询数据. 内容见下表

data里面字段描述:

参数名|	类型|	参数描述
---------|---------|---------
file_url|	string|	图片资源的下载url
file_fileid|	string|	图片资源的唯一id
file_upload_time|	string|	图片上传时间
file_size|	int|	图片的大小|
file_md5|	string|	图片的MD5值|
photo_width|	int|	图片的宽度|
photo_height|	int|	图片的高度

示例代码：

```
result = pic.Query(bucketName, fileId);
```
### 2.5 图片删除
1．	接口说明
删除一个图片。
2．	方法

```
 public string Delete(string bucketName, string fileId)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucketName|	string|	是|	无|	bucket名称
fileId|	string|	是|	无|	生成的资源唯一标识符

返回值,json格式字符串：

参数名|	类型|	参数描述
---------|---------|---------
code|	int|	服务器错误码, 0为成功
message|	string|	服务器返回的信息

示例代码：

```
result = pic.Delete(bucketName, fileId);
```
### 2.6 图片鉴黄

```
result = pic.Delete(bucketName, fileId);
```
1．	接口说明
鉴定url的图片是否为黄色图片。
2．	方法

```
 public string Detection(string bucketName, string url)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucketName|	string|	是|	无|	bucket名称
url|	string|	是|	无|	需要鉴黄图片地址


返回值,json格式字符串

参数名|	类型|	必然返回|	参数描述
---------|---------|---------|---------
code|	int|	是|	服务器错误码, 0为成功
message|	string|	是|	服务器返回的信息
data|	Array|	是|	具体查询数据，内容见下表

data里面字段描述:

参数名|	类型|	参数描述
---------|---------|---------
result|	int|	供参考的识别结果，0正常，1黄图，2需要自行判断
confidence|	double|	识别为黄图的置信度，范围0-100。
hot_score|	double|	性感分值，范围0-100
normal_score|	double|	正常分值，范围0-100
porn_score|	double|	图片的MD5值

示例代码：

```
result = pic.Detection(bucketName, downloadUrl);
```