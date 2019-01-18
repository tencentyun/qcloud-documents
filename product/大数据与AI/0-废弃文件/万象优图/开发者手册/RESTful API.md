本页面为万象优图V2加强版的Restful API文档。

1. 旧版本（V1和V2版本）的Restful API参见[万象优图Restful API文档-V1](/doc/product/275/RESTful API_V1)和[万象优图Restful API文档-V2](/doc/product/275/RESTful API_V2)。
2. 如果您使用的是万象优图2.0，则APPID是以125为前三位的的，请查看[新版文档](https://cloud.tencent.com/doc/product/460/6818)。

注意：各版本只能使用属于其的CGI，请不要混用。具体版本说明请参照[版本说明](/doc/product/275/版本说明)。

## 1	基本概念

| 概念     | 解释                                       |
| ------ | ---------------------------------------- |
| appid  | 接入万象优图创建空间时,系统生成的唯一项目ID, 用于唯一标识接入项目, 申请链接: [图片空间](http://console.cloud.tencent.com/image/bucket) |
| bucket | 开发者添加的空间名称，参见[图片空间](http://console.cloud.tencent.com/image/bucket) |
| userid | 即将废弃字段，请使用默认值“0”                         |
| fileid | 资源存储的唯一标识                                |

## 2	鉴权
腾讯云•万象优图通过签名来验证请求的合法性。开发者通过将签名授权给客户端，使其具备上传下载及管理指定资源的能力。
签名分为单次签名和多次签名, 区别为（可参见[签名适用场景](/doc/product/275/签名与鉴权文档#4-.E7.AD.BE.E5.90.8D.E9.80.82.E7.94.A8.E5.9C.BA.E6.99.AF)）: 
如果针对资源进行写操作(资源删除和资源复制), 那么这个签名必须是单次有效的，重复使用该签名则会返回签名失败；
如果是上传一个新的资源，那么这个签名可以是多次有效的。有效时长最多为三个月。
开发者可以通过[服务器SDK文档](http://cloud.tencent.com/doc/product/275/SDK%E4%B8%8B%E8%BD%BD)生成签名，也可以参考我们的签名函数自行生成签名，具体生成方式详见[鉴权签名方法](/doc/product/275/3805)。

## 3	图片上传

<font color=red>说明</font>：如果您使用的是万象优图2.0，则APPID是以125为前三位的的，您需要使用COS的上传接口，请查看[新版文档](https://cloud.tencent.com/doc/api/264/6005)。

### 3.1 直接上传
功能: 直接上传单张图片, 只支持POST表单(multipart/form-data)方式, 目前只支持20M以内的图片。
接口:`http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` (自定义fileid)
接口:`http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/` (由后台自动生成fileid)
其中fileid为可选参数，可以包含除了'\0'外的任意字符，需要对fileid进行urlencode，utf8字符集，最大长度支持128字节，建议控制在64字节内。
注意：userid为即将废弃字段，请使用默认值“0”，不要依赖该字段进行业务判断。
方法: POST
请求参数HTTP头部信息:

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Host           | 是    | String | 图片云服务器域名，固定为web.image.myqcloud.com       |
| Content-Length | 是    | Int    | 整个multipart/form-data内容的总长度，单位：字节（Byte）。 |
| Content-Type   | 是    | String | 标准的multipart/form-data 格式，参见[rfc1867](http://www.ietf.org/rfc/rfc1867.txt) |
| Authorization  | 是    | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](/doc/product/275/3805) |


HTTP包头

| 参数名称         | 必选   | 类型     | 描述                                 |
| ------------ | ---- | ------ | ---------------------------------- |
| MagicContext | 否    | String | 业务附加信息,当配置回调时，腾讯云•万象优图会透传给开发者的服务器. |
| FileContent  | 是    | Binary | 文件内容                               |
| Md5          | 否    | String | 图片的Md5值,如果提供,服务会对上传的文件做Md5校验及秒传    |


返回的HTTP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述            |
| ------- | ------------- |
| code    | 服务器错误码, 0为成功  |
| message | 服务器返回的信息      |
| data    | 具体查询数据. 内容见下表 |


data里面字段描述:

| 字段名称         | 描述                                  | 格式                                       |
| ------------ | ----------------------------------- | ---------------------------------------- |
| url          | 资源url(用于restful api交互, 如查询,复制,删除资源) | `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` |
| download_url | 生成的下载资源url(用于下载)                    | `http://[bucket]-[appid].image.myqcloud.com/[fileid]` |
| fileid       | 生成的资源唯一标识符                          |                                          |
| info         | 图片的具体信息，见下表                         |                                          |


info里面字段描述：

| 数组名称 | 字段名称   | 描述   |
| ---- | ------ | ---- |
| 0    | height | 图片高度 |
|      | width  | 图片宽度 |



请求示例:

```
POST /photos/v2/10001290/tencentyun/0/tencentyunRestfulAPITest HTTP/1.1
Host: web.image.myqcloud.com
Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468
Authorization: 4Kt58pkZdWwBhm7B6DWcIwebQQJhPTEwMDAxMjkwJmI9dGVuY2VudHl1biZrPUFLSURnYW9PWWgya09tSmZXVmRINGx
wZnhTY0cyelBMUEdvSyZlPTE0Mzg2NzMxNjImdD0xNDM2MDgxMTYyJnI9MTk4MDgmdT0mZj0=
Content-Length: 576924

---------------------------acebdf13572468
Content-Disposition: form-data; name="filecontent"; filename="tencentyun.jpg"
Content-Type: image/jpeg

<@INCLUDE *C:\Users\faithzhou\Desktop\tencentyun.jpg*@>
---------------------------acebdf13572468--
```



### 3.2 分片上传

<font color=red>说明</font>：如果您使用的是万象优图2.0，则APPID是以125为前三位的的，您需要使用COS的上传接口，请查看[新版文档](https://cloud.tencent.com/doc/api/264/6006)。

功能: 将文件分成固定大小片段上传, 适用于图片文件偏大的情况(如大于5MB)。目前单张图片大小限制为20MB。
接口:`http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` (自定义fileid)
接口:`http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/` (由后台自动生成fileid)
其中fileid为可选参数，可以包含除了'\0'外的任意字符，需要对fileid进行urlencode，utf8字符集，最大长度支持128字节，建议控制在64字节内。
注意：userid为即将废弃字段，请使用默认值“0”，不要依赖该字段进行业务判断。
方法: POST
请求参数HTTP头部信息:

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Host           | 是    | String | 图片云服务器域名，固定为web.image.myqcloud.com       |
| Content-Length | 是    | Int    | 整个multipart/form-data内容的总长度，单位：字节（Byte）。 |
| Content-Type   | 是    | String | 标准的multipart/form-data 格式，参见[rfc1867](http://www.ietf.org/rfc/rfc1867.txt) |
| Authorization  | 是    | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](/doc/product/275/3805) |


HTTP包头（第一个分片，即控制包）

| 参数名称         | 必选   | 类型     | 描述                                       |
| ------------ | ---- | ------ | ---------------------------------------- |
| MagicContext | 否    | String | 业务附加信息,当配置回调时，腾讯云•万象优图会透传给开发者的服务器.       |
| Sha          | 是    | String | 图片的sha1值                                 |
| Op           | 是    | String | 固定填: upload_slice, 与普通上传区分               |
| FileSize     | 是    | Int    | 图片总大小                                    |
| Session      | 否    | String | 断点续传功能. 上一次未成功传输的session id              |
| Slice_size   | 是    | String | 单位:字节. 约定分片大小, 最大值为 3MB. 如果不设定, 自动设置为512KB |


返回的HTTP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述            |
| ------- | ------------- |
| code    | 服务器错误码, 0为成功  |
| message | 服务器返回的信息      |
| data    | 具体查询数据. 内容见下表 |


data里面字段描述:

| 字段名称         | 必选   | 类型     | 描述                                       |
| ------------ | ---- | ------ | ---------------------------------------- |
| session      | 否    | String | 唯一标识此文件传输过程的 id. (图片命中秒传则不返回此项)          |
| offset       | 否    | Int    | 开始传输的文件位移(图片命中秒传则不返回此项)                  |
| slice_size   | 否    | Int    | 分片大小(图片命中秒传则不返回此项)                       |
| url          | 否    | String | 图片命中秒传或上传完成则返回。`http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` |
| download_url | 否    | string | 图片命中秒传或上传完成则返回。`http://[bucket]-[appid].image.myqcloud.com/[fileid]` |
| fileid       | 否    | String | 图片命中秒传或上传完成则返回. 资源的唯一标识符                 |


| 参数名称         | 必选   | 类型     | 描述                                 |
| ------------ | ---- | ------ | ---------------------------------- |
| MagicContext | 否    | String | 业务附加信息,当配置回调时，腾讯云•万象优图会透传给开发者的服务器. |
| FileContent  | 是    | Binary | 文件内容                               |
| Md5          | 否    | String | 图片的Md5值,如果提供,服务会对上传的文件做Md5校验及秒传    |


返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述            |
| ------- | ------------- |
| code    | 服务器错误码, 0为成功  |
| message | 服务器返回的信息      |
| data    | 具体查询数据. 内容见下表 |


data里面字段描述:

| 字段名称         | 描述                                  | 格式                                       |
| ------------ | ----------------------------------- | ---------------------------------------- |
| url          | 资源url(用于restful api交互, 如查询,复制,删除资源) | `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` |
| download_url | 生成的下载资源url(用于下载)                    |` http://[bucket]-[appid].image.myqcloud.com/[fileid]` |
| fileid       | 生成的资源唯一标识符                          |                                          |
| info         | 图片的具体信息，见下表                         |                                          |

info里面字段描述：

| 数组名称 | 字段名称   | 描述   |
| ---- | ------ | ---- |
| 0    | height | 图片高度 |
|      | width  | 图片宽度 |

## 4	图片复制
功能: 将图片复制一份(保留原有图片)。
接口: `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]/copy`
方法: POST
请求参数HTTP头部信息:

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| Host          | 是    | String | 图片云服务器域名，固定为web.image.myqcloud.com       |
| Authorization | 是    | String | 单次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](/doc/product/275/3805) |


返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述            |
| ------- | ------------- |
| code    | 服务器错误码, 0为成功  |
| message | 服务器返回的信息      |
| data    | 具体查询数据. 内容见下表 |


data里面字段描述:

| 字段名称         | 描述                                  | 格式                                       |
| ------------ | ----------------------------------- | ---------------------------------------- |
| url          | 资源url(用于restful api交互, 如查询,复制,删除资源) | `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]` |
| download_url | 生成的下载资源url(用于下载)                    | `http://[bucket]-[appid].image.myqcloud.com/[bucket]-[appid]/[userid]/[fileid]/orignal` |


请求示例:

```
POST /photos/v2/10001290/tencentyun/0/tencentyunRestfulAPITest/copy HTTP/1.1
Host: web.image.myqcloud.com
Authorization: VRx9mELRjO7ptkovqjE797CTV2RhPTEwMDAxMjkwJmI9dGVuY2VudHl1biZrPUFLSURnYW9PWWgya09tSmZXVmRING
xwZnhTY0cyelBMUEdvSyZlPTAmdD0xNDM2MDgxNTAyJnI9MjI1MjImdT0mZj10ZW5jZW50eXVuUmVzdGZ1bEFQSVRlc3Q=
Content-Length: 0
```


## 5	图片查询
功能: 查看文件的属性信息，包含：文件哈希值、文件大小、上传时间等，图片和视频返回的信息会有所不同。
接口: `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]/`
方法: GET
请求参数HTTP头部信息:

| 参数名称 | 必选   | 类型     | 描述                                 |
| ---- | ---- | ------ | ---------------------------------- |
| Host | 是    | String | 图片云服务器域名，固定为web.image.myqcloud.com |


返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述            |
| ------- | ------------- |
| code    | 服务器错误码, 0为成功  |
| message | 服务器返回的信息      |
| data    | 具体查询数据. 内容见下表 |


data里面字段描述:

| 字段名称             | 描述         | 格式                                       |
| ---------------- | ---------- | ---------------------------------------- |
| file_url         | 图片资源的下载url | `http:// [bucket]-[appid].image.myqcloud.com/[bucket]-[appid]]/[userid]/[fileid]/original` |
| file_fileid      | 图片资源的唯一id  |                                          |
| file_upload_time | 图片上传时间     | Unix timestamp                           |
| file_size        | 图片的大小      | 单位: Byte                                 |
| file_md5         | 图片的MD5值    | 16进制的MD5值                                |
| photo_width      | 图片的宽度      |                                          |
| photo_height     | 图片的长度      |                                          |


请求示例:

```
GET /photos/v2/10001290/tencentyun/0/tencentyunRestfulAPITest HTTP/1.1
Host: web.image.myqcloud.com
```

## 6	图片删除
功能: 删除一个图片。
接口: `http://web.image.myqcloud.com/photos/v2/[appid]/[bucket]/[userid]/[fileid]/del`
方法: POST
请求参数HTTP头部信息:

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| Host          | 是    | String | 图片云服务器域名，固定为`web.image.myqcloud.com `      |
| Authorization | 是    | String | 单次有效签名,用于鉴权，具体生成方式详见[鉴权签名方法](/doc/product/275/3805) |


返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400

返回内容(json):

| 字段名称    | 描述           |
| ------- | ------------ |
| code    | 服务器错误码, 0为成功 |
| message | 服务器返回的信息     |


请求示例:

```
POST /photos/v2/10001290/tencentyun/0/tencentyunRestfulAPITest/del HTTP/1.1
Host: web.image.myqcloud.com
Authorization: CP+70pfzpNnldJoYn3K85DGNUBxhPTEwMDAxMjkwJmI9dGVuY2VudHl1biZrPUFLSURnYW9PWWgya09tSmZXVmRINGx
wZnhTY0cyelBMUEdvSyZlPTAmdD0xNDM2MDgyMzIzJnI9MjI0NzkmdT0mZj10ZW5jZW50eXVuUmVzdGZ1bEFQSVRlc3Q=
Content-Length: 0
```


## 7	图片下载
图片下载可以是公开下载，即使用图片的download_url 直接访问即可。
请求示例：

```
GET test0706-10000037.image.myqcloud.com/tencentyunRestfulAPITest HTTP/1.1
Host: test0706-10000037.image.myqcloud.com
```


如果在控制台上面设置了[空间样式](/doc/product/275/控制台使用说明#2.3-.E7.A9.BA.E9.97.B4.E6.A0.B7.E5.BC.8F)或者[样式下载别名](/doc/product/275/控制台使用说明#2.2-.E7.A9.BA.E9.97.B4.E7.AE.A1.E7.90.86)，并且设置了[样式分隔符](/doc/product/275/控制台使用说明#2.2-.E7.A9.BA.E9.97.B4.E7.AE.A1.E7.90.86)，则访问样式图片的方式如下：
download_url+样式分隔符+样式名。
注：空间样式和样式下载别名的名字统称样式名。
例如设置了样式名“160x160.jpeg”，样式分隔符“/”,则样式图片的访问方式如下：

```
GET v2test-10000812.image.myqcloud.com/tencentyunRestfulAPITest/160x160.jpeg HTTP/1.1
Host: v2test-10000812.image.myqcloud.com/
```


若开启了token防盗链，图片下载只能是私密下载，即必须download_url +?sign=[签名]。
请求示例:

```
GET http://test0706-10000037.image.myqcloud.com/951b0e3b-db35-40e2-8c31-ed38dab5ae69?sign=Ea5aPdBMeVm5O
T332nSYh1nqyJhhPTEwMDAwMDM3JmI9dGVzdDA3MDYmaz1BS0lEcG9LQmZNSzdhWWNZTmxxeG5FdFlBMWFqQXFqaTJQN1QmZT0xNDQy
MjE0NzMwJnQ9MTQ0MTg1NDczMCZyPTE0NDE4NTQ3MzAmdT0wJmY9 HTTP/1.1
Host: test0706-10000037.image.myqcloud.com
```


图片下载支持实时压缩等动态处理，详见以下 [8.图像处理](#8-.E5.9B.BE.E5.83.8F.E5.A4.84.E7.90.86)

注意：以下为V2加强版的Restful API实时处理接口，如果开发者使用的是V1和V2的接口请参考本文档头部的相应Restful API文档。
## 8	图像处理
### 8.1 基本图像处理（imageView2）
imageView2是腾讯云·万象优图提供的一种使用简单，但功能强大的图像处理接口。开发者根据业务需求，只需在下载url后面附加相应的参数，就可以生成相应的缩略图。
开发者还可以为一组处理参数指定一个别名，具体参考[样式下载别名](/doc/product/275/控制台使用说明#2.2-.E7.A9.BA.E9.97.B4.E7.AE.A1.E7.90.86)。
#### 8.1.1 接口形式
注意：请忽略下面代码中的回车。

```
download_url?imageView2/<mode>/w/<Width>/h/<Height>
                         /format/<Format>
                         /q/<Quality>
```
#### 8.1.2 参数说明

| 参数                                       | 含义                                       |
| ---------------------------------------- | ---------------------------------------- |
| /0/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比压缩；如果只指定一边，则另一边自适应 |
| /1/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最小值分别为Width和Height，进行等比压缩，居中裁剪；如果只指定一边，则表示宽高相等的正方形；缩放后的图片的大小为&lt;Width&gt;x&lt;Height&gt;（其中一边多余的部分会被裁剪掉） |
| /2/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最大值分别为Width和Height，进行等比压缩；如果只指定一边，则另一边自适应 |
| /3/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最小值分别为Width和Height，进行等比压缩；如果只指定一边，代表另外一边为同样的值 |
| /4/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最小值分别为LongEdge和ShortEdge，进行等比压缩；如果只指定一边，代表另外一边为同样的值 |
| /5/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比压缩，居中裁剪；如果只指定一边，则表示宽高相等的正方形；同模式1，缩放后其中一边多余的部分会被裁剪掉 |
| /format/&lt;Format&gt;                   | 目标缩略图的图片格式，Format可为：jpg, bmp, gif, png, webp,yjpeg等，其中yjpeg为万象优图针对jpeg格式进行的优化，本质为jpg格式；缺省为原图格式 |
| /q/&lt;Quality&gt;                              | 图片质量，取值范围0-100，默认值为原图质量；取原图质量和指定质量的最小值；&lt;Quality&gt; 后面加！，表示强制使用指定值 |

示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/0/w/400/h/300
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/1/w/400/h/600/q/85
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/2/w/400/h/600/q/85!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/3/w/400/format/png
```


### 8.2 高级图像处理（imageMogr2）
imageMogr2是腾讯云·万象优图为开发者提供的简单而功能强大的高级图像处理接口，包括旋转、裁剪等。
注：裁剪为缩放裁剪，即先将图片进行等比缩放，在进行裁剪。例如：原图为1500x1200，裁剪成600x600，会先将图片缩放为750x600，然后再裁剪成600x600。
#### 8.2.1 接口形式
请忽略一下接口中的回车。

```
  download_url?imageMogr2/auto-orient
                         /thumbnail/<imageSizeGeometry>
                         /strip
                         /gravity/<gravityType>
                         /crop/<imageSizeAndOffsetGeometry>
                         /scrop/<imageSizeAndOffsetGeometry>
                         /rotate/<rotateDegree>
                         /format/<Format>
                         /quality/<Quality>
                         /cgif/<FrameNumber>
                         /interlace/<Mode>
```


#### 8.2.2 参数说明

| 参数                                      | 含义                                       |
| --------------------------------------- | ---------------------------------------- |
| /auto-orient                            | 根据原图的exif信息自动把图片旋转回正。                    |
| /strip                                  | 去除不安全代码包括exif信息。                         |
| /gravity/&lt;gravityType&gt;                 | 图片处理位置，影响其后的裁剪偏移参数，参见下面九宫格方位，默认值为中间：Center。 |
| /thumbnail/&lt;imageSizeAndOffsetGeometry&gt; | 参考下面的缩放操作参数表。                            |
| /crop/&lt;imageSizeAndOffsetGeometry&gt;      | 请参考下面的裁剪参数表，缺省不裁剪。                       |
| /scrop/&lt;imageSizeAndOffsetGeometry&gt;     | 基于人脸识别执行智能裁剪功能。裁剪区域根据人的头像位置自动确定。 输出的裁剪后图片大小需要结合宽高参数指定。参考下面的智能裁剪参数表。 |
| /rotate/&lt;rotateDegree&gt;                  | 图片旋转角度，取值范围0-360，默认不旋转。                  |
| /format/&lt;Format&gt;                        | 目标缩略图的图片格式，Format可为：jpg, bmp, gif, png, webp,yjpeg等，其中yjpeg为万象优图针对jpeg格式进行的优化，本质为jpg格式；缺省为原图格式。 |
| /quality/&lt;Quality&gt;                      | 图片质量，取值范围0-100，默认值为原图质量；取原图质量和指定质量的最小值；&lt;Quality&gt;后面加！，表示强制使用指定值，如：90！。 |
| /cgif/&lt;FrameNumber&gt;                     | 只针对原图为gif格式，对gif图片格式进行的优化，降帧降颜色。分为以下两种情况：FrameNumber=1，则按照默认帧数30处理，如果图片帧数大于该帧数则截取；FrameNumber取值(1,100]，则将图片压缩到指定帧数FrameNumber。 |
| /interlace/&lt;Mode&gt;                       | 输出为渐进式jpg格式。Mode可为0或1,0表示不开启渐进式；1表示开启渐进式。该参数仅在输出图片格式为jpg格式时有效。如果输出非jpg图片格式，会忽略该参数，默认值0。 |

缩放操作表格：


| 参数                                  | 含义                                       |
| ----------------------------------- | ---------------------------------------- |
| /thumbnail/!&lt;Scale&gt;p                | 指定图片的宽高为原图的Scale%                        |
| /thumbnail/!&lt;Scale&gt;px               | 指定图片的宽为原图的Scale%，高度不变                    |
| /thumbnail/!x&lt;Scale&gt;p               | 指定图片的高为原图的Scale%，宽度不变                    |
| /thumbnail/&lt;Width&gt;x                 | 指定目标图片宽度为Width，高度等比压缩                    |
| /thumbnail/x&lt;Height&gt;                | 指定目标图片高度为Height，宽度等比压缩                   |
| /thumbnail/&lt;LongEdge&gt;x&lt;ShortEdge&gt;   | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比缩放 |
| /thumbnail/!&lt;LongEdge&gt;x&lt;ShortEdge&gt;r | 限定缩略图的长边和短边的最小值分别为LongEdge和ShortEdge，进行等比缩放 |
| /thumbnail/&lt;Width&gt;x&lt;Height&gt;!        | 忽略原图宽高比例，指定图片宽度为Width，高度为Height，强行缩放图片，可能导致目标图片变形 |
| /thumbnail/&lt;Area&gt;@                  | 等比缩放图片，缩放后的图像，总像素数量不超过Area                   |

示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!50p
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!50px
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!x50p
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/200x
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/200x400!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/35000@
```

九宫格方位图：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/apicankao-3.jpg)

裁剪操作表格（cropSize）：

| 参数                                 | 含义                                       |
| ---------------------------------- | ---------------------------------------- |
| /crop/&lt;Width&gt;x               | 指定目标图片宽度为Width，高度不变。Width取值范围为10-16383   |
| /crop/x&lt;Height&gt;              | 指定目标图片高度为Height，宽度不变。Height取值范围为10-16383 |
| /crop/&lt;Width&gt;x&lt;Height&gt; | 指定目标图片宽度为Width，高度为Height。Width和Height取值范围都为10-16383 |

裁剪操作表格（scropSize）：

| 参数                                  | 含义                                       |
| ----------------------------------- | ---------------------------------------- |
| /scrop/&lt;Width&gt;x               | 指定目标图片宽度为Width，高度不变。Width取值范围为10-16383   |
| /scrop/x&lt;Height&gt;              | 指定目标图片高度为Height，宽度不变。Height取值范围为10-16383 |
| /scrop/&lt;Width&gt;x&lt;Height&gt; | 指定目标图片宽度为Width，高度为Height。Width和Height取值范围都为10-16383 |

开发者可以指定裁剪的具体偏移位置，如下表所示：

| 参数                                      | 含义                                       |
| --------------------------------------- | ---------------------------------------- |
| /crop/!{cropSize}a&lt;dx&gt;a&lt;dy&gt; | 相对于偏移位置，水平向右偏移dx，同时垂直向下偏移dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}-&lt;dx&gt;a&lt;dy&gt; | 相对于偏移位置，从指定宽度中减去dx，同时垂直向下偏移dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}a&lt;dx&gt;-&lt;dy&gt; | 相对于偏移位置，水平向右偏移dx，同时从指定高度中减去dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}-&lt;dx&gt;-&lt;dy&gt; | 相对于偏移位置，从指定宽度中减去dx个像素，同时从指定高度中减去dy个像素。取值范围小于原图宽高即可 |

例如：
/crop/!600x600a20a20: 表示从原图的坐标（x,y）为（20,20）的位置裁剪600x600的缩略图。
/crop/!600x600-20a20: 表示从原图的坐标（x,y）为（0,20）的位置裁剪580x600的缩略图。
注意：scrop 参数与 crop 参数同时使用，当智能裁剪没有识别到人脸时，会执行普通的裁剪。 要求使用的宽高参数一致，否则输出图片宽高是两个宽高参数中的一个。
`http://v2enhance-10000812.image.myqcloud.com/tencentyunRestfulAPITest?imageMogr2/scrop/300x400/crop/300x400`
示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/crop/!600x600a20a20/quality/85
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/crop/!600x600-20a20/quality/85!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/format/jpg/interlace/1
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/scrop/300x400
```


### 8.3 图片水印（watermark）
腾讯云•万象优图支持实时图片水印处理功能，目前，水印图片必须指定为已存储于万象优图中的图片。
#### 8.3.1 接口形式
请忽略一下接口中的回车。

```
  download_url?watermark/1
                        /image/<encodedImageURL>
                        /gravity/<gravity>
                        /dx/<distanceX>
                        /dy/<distanceY>
```


#### 8.3.2 参数说明

| 参数                             | 含义                                       |
| ------------------------------ | ---------------------------------------- |
| /image/&lt;encodedImageURL&gt; | 水印源图片地址，需要经过URL安全的Base64编码。指定的水印图片必须存在于万象优图中。 |
| /gravity/&lt;gravity&gt;       | 文字水印位置，九宫格位置，参见8.2.2节的九宫格方位图，默认值SouthEast |
| /dx/&lt;distanceX&gt;          | 水平（横轴）边距，单位为像素，缺省值为0                     |
| /dy/&lt;distanceY&gt;          | 垂直（纵轴）边距，单位像素，默认值为0                      |

示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?watermark/1
       /image/aHR0cDovL3Rlbmd4dW55dW4tMTAwMDQ0ODYuaW1hZ2UubXlxY2xvdWQuY29tL3NodWl5aW5fMi5wbmc=/gravity/southwest
```


### 8.4 文字水印（watermark）
腾讯云·万象优图支持实时文字水印功能，即通过在图片URL后面附加参数为图片实时打文字水印。
#### 8.4.1 接口形式
请忽略一下接口中的回车。

```
  download_url?watermark/2
                        /text/<encodedText>
                        /font/<encodedFontName>
                        /fontsize/<fontSize>
                        /fill/<encodedTextColor>
                        /dissolve/<dissolve>
                        /gravity/<gravity>
                        /dx/<distanceX>
                        /dy/<distanceY>
```


#### 8.4.2 参数说明

| 参数                             | 含义                                       |
| ------------------------------ | ---------------------------------------- |
| /text/&lt;encodedText&gt;      | 水印内容，需要经过URL安全的Base64编码                  |
| /font/&lt;encodedFontName&gt;  | 水印字体，需要经过URL安全的Base64编码，默认值tahoma.ttf。水印字体列表参考[支持字体列表](/doc/product/275/万象优图支持字体列表) |
| /fontsize/&lt;fontSize&gt;     | 水印文字字体大小，单位是: 磅，缺省值13                    |
| /fill/&lt;encodedTextColor&gt; | 字体颜色，缺省为白色，RGB格式，可以是颜色名称（如blue）或者十六进制（如#FF0000），参考[RGB编码表](http://www.rapidtables.com/web/color/RGB_Color.htm)，需经过URL安全的Base64编码，默认值#3D3D3D |
| /dissolve/&lt;dissolve&gt;     | 文字透明度，取值1-100，默认100（完全不透明）               |
| /gravity/&lt;gravity&gt;       | 文字水印位置，九宫格位置，参见8.2.2节的九宫格方位图，默认值SouthEast |
| /dx/&lt;distanceX&gt;          | 水平（横轴）边距，单位为像素，缺省值为0                     |
| /dy/&lt;distanceY&gt;          | 垂直（纵轴）边距，单位像素，默认值为0                      |
示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestfulAPITest?watermark/2
       /text/6IW-6K6v5LqRwrfkuIfosaHkvJjlm74=/fill/d2hpdGU=/fontsize/100/dissolve/50/gravity/northeast/dx/20/dy/20
```


### 8.5 获取图片基本信息（imageInfo）
获取图片的基本信息，包括图片的格式、长、宽等。
接口形式：
 download_url?imageInfo
示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageInfo
```


### 8.6 获取图片exif（exif）
接口形式：
 download_url?imageInfo
示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?exif
```


### 8.7 获取图片主色调（imageAve）
接口形式：
 download_url?imageAve
示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageAve
```


## 9 返回码定义

| 错误码   | 含义                     |
| ----- | ---------------------- |
| -5999 | 参数错误                   |
| -5998 | 签名格式错误                 |
| -5997 | 后端网络错误                 |
| -5996 | HTTP请求方法错误             |
| -5995 | 文件大小错误                 |
| -5994 | url参数解析不匹配             |
| -5993 | multipart/formdata参数错误 |
| -5992 | 请求参数错误                 |
| -5991 | 分片过大                   |
| -5990 | 找不到filecontent         |
| -5989 | 上传失败                   |
| -5988 | cgi初始化错误               |
| -5987 | wup编码失败                |
| -5986 | wup解码失败                |
| -5985 | 获取路由失败                 |
| -5984 | sha1不匹配                |
| -5983 | 错误的session             |
| -5982 | 建立连接错误                 |
| -5981 | 建立连接错误                 |

其他返回码参见 [返回码说明](/doc/product/275/返回码说明)。
