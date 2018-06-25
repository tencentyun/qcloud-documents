本文档为万象优图V2版本和V2加强版的PHP SDK文档，旧版本（V1版本）的PHP SDK文档参见 万象优图[PHP SDK说明文档-V1](/doc/product/275/PHP SDK_V1)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。
## 1	开发准备
万象优图服务的php sdk的下载地址： https://github.com/tencentyun/php-sdk
### 1.1	前期准备
前期准备
1.	sdk依赖php 5.3.0版本及以上， 推荐使用相同的版本。
2.	获取项目ID(appid)，bucket，secret_id和secret_key；
### 1.2	获取SDK
获取SDK的方式有两种：
1. composer获取
在开发环境命令行直接执行下面的命令即可导入php-sdk包.
 php composer.phar require tencentyun/php-sdk
然后，参考api说明和sdk中提供的sample，开发代码即可。sample.php对应v1版本的restful api, samplev2.php对应v2版本的restful api。
2. 下载源码获取
您也可以直接下载github上提供的源代码，集成到您的开发环境即可。

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
V2加强版的签名：

```
 public static function getAppSignV2($bucket, $fileid, $expired)
```
V2版本的签名:

```
 public static function appSignV2($url, $expired=0, $options=array())
```
V1版本的签名:

```
 public static function appSign($url, $expired)
```
3．	参数和返回值
参数说明：

---------|---------|---------|---------|---------
参数名|	类型|	必须	|默认值|	参数描述
url	|String	|是	|无	|需要操作的url
expired	|Int|	否	|0	|签名过期时间戳


返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode|	Int|	http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message|	String	|API错误信息
data	|Array|	API 返回数据
data.sign	|String|	签名串


示例代码：

```
// 生成私密下载url
    $expired = time() + 999;
    $sign = Auth::getAppSignV2($bucket, $fileid, $expired);
    $signedUrl = $downloadUrl . '?sign=' . $sign;
    var_dump($signedUrl);

    //生成新的单次签名, 必须绑定资源fileid，复制和删除必须使用，其他不能使用
    $fileid = $fileid.time().rand();  // 自定义文件名
    $expired = 0;
    $sign = Auth::getAppSignV2($bucket, $fileid, $expired);
    var_dump($sign);
```
### 2.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
   public static function upload($filePath, $bucket, $fileid='', $userid=0, 
                                     $magicContext = '', $params = array())

   public static function upload_binary($fileContent, $bucket, $fileid = '', 
                                     $userid = 0, $magicContext = '', $params = array())

```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileContent|	String	|是	|无|	base64编码后的字符串数据
filePath	|String	|是	|无	|本地图片文件路径
bucket	|String	|是|	无	|空间名称
fileid	|String	|否|	空	|用户自定义文件名
userid|	String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0
magicContext	|String|	否	|空	|上传成功后，用户自定义的回调参数
params	|array|	否	|空数组|	可选处理项，目前支持params[‘get’] => array() 用于指定上传是url中携带的get请求参数


返回值：

参数名	|类型|	参数描述
---------|---------|---------
httpcode	|Int|	http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message|	String|	API错误信息
data|	Array	|API 返回数据
data.url|	String|	图片的管理URL
data.downloadUrl	|String	|图片的下载和访问URL
data.fileid	|String|	图片的唯一ID
data.info.0.0.width|	int|	图片宽度
data.info.0.0.height	|int|	图片高度


示例代码：

```
 $bucket = 'test1'; // 自定义空间名称，在http://console.cloud.tencent.com/image/bucket创建
 $fileid = 'sample'.time();  // 自定义文件名
 $uploadRet = ImageV2::upload('/tmp/tencentyun.jpg', $bucket, $fileid);
 var_dump($uploadRet);
```



### 2.3	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
public static function stat($bucket, $fileid, $userid=0)
```
3．	参数和返回值
参数说明：

参数名|	类型	|必须	|默认值|	参数描述
---------|---------|---------|---------|---------
bucket|	String	|是	|无	|空间名称
fileid	|String|	是	|无	|图片唯一ID
userid	|String	|否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0


返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message	|String|	API错误信息
data	|Array	|API 返回数据
data.downloadUrl	|String|	图片的下载和访问URL
data.url	|String	|管理url
data.fileid	|String|	图片的唯一ID
data.uploadTime	|String	|图片的上传时间
data.size	|String	|图片的大小（Bytes）
data.md5	|String	|图片的md5值
data.width	|String	|图片的宽度（pixels）
data.height	|String	|图片的高度（pixels）


示例代码：

```
 // 查询管理信息
    $statRet = ImageV2::stat($bucket, $fileid);
    var_dump('stat',$statRet);
```


### 2.4	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
public static function del($bucket, $fileid, $userid=0)
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
bucket|	String	|是	|无	|空间名称
fileid|	String	|是|	无	|图片唯一ID
userid|	String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0


返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code	|Int	|API 错误码，成功时为0
message|	String|	API错误信息
data|	Array	|空数组


示例代码：

```
$delRet = ImageV2::del($bucket, $fileid);
var_dump($delRet);
```



### 2.5 图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
public static function copy($bucket, $fileid, $userid=0)
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值|	参数描述
---------|---------|---------|---------|---------
bucket	|String	|是|	无	|空间名称
fileid	|String|	是	|无|	图片唯一ID
userid|	String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0


返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode|	Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String|	API错误信息
data	|Array	|API 返回数据
data.downloadUrl	|String|	图片的下载和访问URL
data.url|	String	|管理url


示例代码：

```
 // 复制
 $copyRet = ImageV2::copy($bucket, $fileid);
```


3 错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。