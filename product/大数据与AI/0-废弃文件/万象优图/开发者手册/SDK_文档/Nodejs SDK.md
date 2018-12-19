本文档为万象优图V2版本和V2加强版的Nodejs SDK文档，旧版本（V1版本）的Nodejs SDK文档参见 万象优图[Nodejs SDK说明文档-V1](/doc/product/275/Nodejs SDK_V1)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。
## 1	开发准备
万象优图服务的nodejs sdk的下载地址： https://github.com/tencentyun/nodejs-sdk
### 1.1	前期准备
1.	sdk依赖node 0.4.7版本及以上。
2.	获取项目ID(appid)，bucket，secret_id和secret_key；
### 1.2	获取SDK
1. npm获取:
在开发环境命令行直接执行下面的命令即可导入nodejs-sdk包

```
npm install tencentyun
```
然后，参考api说明和sdk中提供的sample，开发代码即可。sample对应v1版本的restful api, samplev2对应v2版本的restful api。
2. 直接下载源码集成:
您也可以直接下载github上提供的源代码，集成到您的开发环境即可（依赖formstream）。

## 2	API详细说明
### 2.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
V1版本的api和V2版本的api的签名并不相同。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见鉴权服务技术方案
2．	方法
签名函数会自动根据传入的URL，进行不同方式的签名，这里对使用者是透明的。
V2加强版的签名：

```
 // 生成新的上传签名
  exports.getAppSignV2(bucket, fileid, expired)
```
V2版本的签名：

```
  // 生成新的上传签名
  exports.appSignV2 = function(url, expired)
```
V1版本的签名：

```
  // 生成新的上传签名
  exports.appSign = function(url, expired)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
url	|String|	是	|无|	需要操作的url
expired	|Int|	是	|无|	签名过期时间戳

返回值：

参数名|	类型|	参数描述
---------|---------|---------
sign	|String	|签名串

示例代码：

```
        // 生成私密下载url
        var expired = parseInt(Date.now() / 1000) + 60;
        var sign = tencentyun.auth.getAppSignV2(bucket, fileid, expired);
        console.log('downloadUrl is : ' + ret.data.downloadUrl + '?sign=' + sign);

        // 生成新的上传签名
        var expired = parseInt(Date.now() / 1000) + 60;
        var sign = tencentyun.auth.getAppSignV2(bucket, fileid, expired);
        console.log('sign is :'+sign);
```

### 2.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法
 
```
exports.upload = function(fileObj, bucket, fileid, callback, userid, magicContext) 
```
3．	参数和返回值

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileObj|	String|	是|	无|	图片本地路径或保存有二进制图片数据的Buffer(如果是二进制图片数据，需要进行Base64编码)
bucket|	String|	是	|无|	空间名称
fileid	|String	|否	|空	|用户自定义文件名
callback|	Function	|是	|无|	回调函数，返回执行结果
userid	|String	|否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0
magicContext	|String	|否|	空	|上传成功后，用户自定义的回调参数

返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode|	Int	|http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message	||String	|API错误信息
data	|Object	|API 返回数据
data.url|	String	|图片的管理URL
data.downloadUrl	|String	|图片的下载和访问URL
data.fileid|	String	|图片的唯一ID
data.info.0.0.width	|int	|图片宽度
data.info.0.0.height|	int|	图片高度

示例代码：

```
  tencentyun.imagev2.upload('/tmp/amazon.jpg', bucket, fileid, 
                                   function(ret){……})

```

### 2.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
exports.copy = function(bucket, fileid, callback, userid) 
```
3．	参数和返回值

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
bucket|	String|	是	|无	|空间名称
fileid	|String	|否	|空	|用户自定义文件名
callback	|Function	|是	|无	|回调函数，返回执行结果
userid	|String|	否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String	|API错误信息
data|	Object	|API 返回数据
data.url|	String|	图片的管理URL
data.downloadUrl	|String	|图片的下载和访问URL

示例代码：

```
    // 复制
    tencentyun.imagev2.copy(bucket, fileid, function(ret) {
         console.log(ret);
    });
```
### 2.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
exports.stat = function(bucket, fileid, callback, userid)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值	|参数描述
---------|---------|---------|---------|---------
bucket|	String	|是	|无	|空间名称
fileid	|String	|否|	空	|用户自定义文件名
callback	|Function	|是	|无	|回调函数，返回执行结果
userid	|String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode|	Int	|http响应码，请求正常时为200
code|	Int|	API 错误码，成功时为0
message	|String|	API错误信息
data|	Object	|API 返回数据
data.downloadUrl	|String	|图片的下载和访问URL
data.url	|String	|图片管理url
data.fileid	|String|	图片的唯一ID
data.uploadTime	|String|	图片的上传时间
data.size	|String|	图片的大小（Bytes）
data.md5	|String|	图片的md5值
data.width	|String|	图片的宽度（pixels）
data.height	|String|	图片的高度（pixels）

示例代码：

```
  // 查询
  tencentyun.imagev2.stat(bucket, fileid, function(ret) {
       console.log(ret);
  });
```
### 2.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
exports.delete = function(bucket, fileid, callback, userid) 
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
bucket	|String|	是|	无	|空间名称
fileid	|String	|是	|无	|图片唯一ID
callback|	Function|	是|	无|	回调函数，返回执行结果
userid|	String|	否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode|	Int|	http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message|	String	|API错误信息
data	|Object|	空对象

示例代码：

```
 tencentyun.imagev2.delete(bucket, fileid, function(ret) {
           console.log(ret);
  });
```
## 3 错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。