## 功能

腾讯云点播VOD和腾讯云对象存储COS提供了一组REST API，让用户的APP服务器将文件上传到COS，并由VOD完成对上传视频的转码、拼接等后续操作。

通过这些REST API，APP服务器单独上传一个视频，也可以同时上传一个视频文件和封面文件（封面文件为该视频的封面）。

## 点播发起上传

### REST API

[点播发起上传]()

### 请求参数

如果仅上传视频，则至少需要填写**videoType**字段。

如果再上传视频的同时还需要上传封面，则至少需要同时填写**videoType**和**coverType**两个字段。

### 返回结果

返回的结果包括**storageAppId**，**storageBucket**，**storageRegion**和**vodSessionKey**。

如果仅上传视频，返回的结果有**video**结构（包含**video.storageSignature**和**video.storagePath**字段）；如果同时上传视频和封面，返回的结果除了**video**结构，还有**cover**结构（包含**cover.storageSignature**和**cover.storagePath**字段）

返回的结果中，vodSessionKey用于VOD的[点播确认上传]()，而其他以storage为前缀的结果均用于[COS上传相关]()的REST API。


## COS上传相关

### REST API

1. [初始化分片上传](/document/api/436/6067)
2. [逐个上传分片](/document/api/436/6068)
3. [结束上传分片](/document/api/436/6074)
4. [查询上传分片](/document/api/436/6070)

以上REST API的语法为：
```
POST /files/v2/<appid>/<bucket_name>[/dir_name]/<file_name>  HTTP/1.1
Host: <Region>.file.myqcloud.com
Content-Type: multipart/form-data
Authorization: <multi_effect_signature>
```

语法中的变量均采用[点播发起上传的返回结果]()：
```<appid>```为**storageAppId**，```<bucket_name>```为**storageBucket**，```<Region>```为**storageRegion**，```/<bucket_name>[/dir_name]/<file_name>```为**video.storagePath**(对于封面文件为**cover.storagePath**)，```<multi_effect_signature>```为**video.storageSignature**(对于封面文件为**cover.storageSignature**)

### 流程

向COS上传文件时，需要按照以下顺序：

初始化分片上传（调用一次）->查询上传分片->逐个上传分片（调用多次，次数为分片数）->结束上传分片（调用一次）

## 点播确认上传

### REST API

[点播确认上传]()

### 请求参数

请求参数为**vodSessionKey**，该参数的值与[点播发起上传的返回结果]()中的**vodSessionKey**保持一致。

### 返回结果
