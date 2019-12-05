## 接口名称

### 上传小文件（小于20MB）使用的 API
1. [简单上传文件](/document/api/436/6066)

### 上传大文件（大于20MB）使用的 API
1. [初始化分片上传](/document/api/436/6067)
2. [逐个上传分片](/document/api/436/6068)
3. [结束上传分片](/document/api/436/6074)

## 功能说明
1. 将视频（和封面）文件。
2. API 在服务端上传位于哪个步骤请参考[服务端上传综述](/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B)。

## SDK
建议使用[基于 JSON API 封装的 SDK](/document/product/436/6474) 进行 API 的调用。

## 使用方式

使用方式可以参考以上各 API 链接中的文档，各 API 的语法为：
```
POST /files/v2/<appid>/<bucket_name>[/dir_name]/<file_name>  HTTP/1.1
Host: <Region>.file.myqcloud.com
Content-Type: multipart/form-data
Authorization: <multi_effect_signature>
```

语法中的以下变量取值 [VOD发起上传的返回结果](/document/product/266/9756#.E6.8E.A5.E5.8F.A3.E5.BA.94.E7.AD.94)：
```<bucket_name>```为**storageBucket**，```<Region>```为**storageRegion**，```/<bucket_name>[/dir_name]/<file_name>```为**video.storagePath**(对于封面文件为**cover.storagePath**)。
其他的变量取值：
```<appid>```为10022853，```<multi_effect_signature>```按照API的要求生成签名。