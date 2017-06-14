## 接口名称

### 上传小文件（小于20MB）使用的 API
1. [简单上传文件](/document/api/436/6066)

### 上传大文件（大于20MB）使用的 API
1. [初始化分片上传](/document/api/436/6067)
1. [逐个上传分片](/document/api/436/6068)
1. [结束上传分片](/document/api/436/6074)

## 使用方式

使用方式可以参考以上各 API 链接中的文档，各 API 的语法为：
```
POST /files/v2/<appid>/<bucket_name>[/dir_name]/<file_name>  HTTP/1.1
Host: <Region>.file.myqcloud.com
Content-Type: multipart/form-data
Authorization: <multi_effect_signature>
```

语法中的变量均采用[点播发起上传的返回结果]()：
```<appid>```为**storageAppId**，```<bucket_name>```为**storageBucket**，```<Region>```为**storageRegion**，```/<bucket_name>[/dir_name]/<file_name>```为**video.storagePath**(对于封面文件为**cover.storagePath**)，```<multi_effect_signature>```为**video.storageSignature**(对于封面文件为**cover.storageSignature**)