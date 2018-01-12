## 1	开发准备
万象优图服务的python sdk的下载地址： https://github.com/tencentyun/python-sdk
### 1.1	前期准备
获取appid，secret_id和secret_key。
### 1.2	获取SDK
1.	下载源码
如果安装了git命令行，执行git clone https://github.com/tencentyun/python-sdk
或者直接在github下载zip包。
2.	使用pip管理包

```
pip install tencentyun
```
3.	参照api说明和sdk中提供的demo，开发代码。
## 2	API详细说明
### 2.1	生成签名
1．	接口说明
可以使用该函数在服务端生成签名，供移动端app使用。签名的详细描述和适用场景参见[鉴权服务技术方案](/doc/product/275/签名与鉴权文档-V1)。
2．	方法

```
def app_sign(self, url, expired=0) 
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值	|参数描述
---------|---------|---------|---------|---------
url|	String	|是	|无	|需要操作的url
expired	|Int	|是|	无	|签名过期时间戳

返回值：

参数名|	类型|	参数描述
---------|---------|---------
sign	|String|	签名串
code	|Int|	API 错误码，成功时为0

示例代码：

```
    # 生成单次有效签名
    auth = tencentyun.Auth(secret_id,secret_key)
    sign = auth.app_sign(download_url)
    print download_url + '?sign=' + sign

    # 生成多次有效签名
    expired = int(time.time()) + 999
    sign = auth.app_sign('http://web.image.myqcloud.com/photos/v1/0/', expired)
    print sign
```
### 2.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
def upload(self, filepath, userid=0, magic_context=) 
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值	|参数描述
---------|---------|---------|---------|---------
filePath|	String	|是|	无	|本地图片文件路径
userid|	String	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0
magicContext	|String	|否|	空	|上传成功后，用户自定义的回调参数

返回值：

参数名	|类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message	|String	|API错误信息
data	|Dict|	API 返回数据
data.url|	String|	图片的管理URL
data.download_url	|String|	图片的下载和访问URL
data.fileid	|String	|图片的唯一ID
data.info.0.0.width|	int	|图片宽度
data.info.0.0.height	|int	|图片高度


示例代码：

```
import tencentyun

image = tencentyun.Image('200679','AKIDoleG4e6U0j6EVQcjWXxzSO2Vv7Hqlgp2','ROlw3XYdNXNnII18ATs6zd7m5mivnApa')
obj = image.upload('/tmp/tencentyun.jpg');
print obj

```
### 2.3	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
def stat(self, fileid, userid=0) 
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileid	|String|	是|	无|	图片唯一ID
userid|	String	|否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode|	Int|	http响应码，请求正常时为200
code|	Int|	API 错误码，成功时为0
message|	String|	API错误信息
data	|Dict|	API 返回数据
data.download_url	|String	|图片的下载和访问URL
data.fileid	|String	|图片的唯一ID
data.upload_time	|String|	图片的上传时间
data.size	|String	|图片的大小（Bytes）
data.md5	|String|	图片的md5值
data.width	|String|	图片的宽度（pixels）
data.height	|String	|图片的高度（pixels）

示例代码：

```
import tencentyun

image = tencentyun.Image('200679','AKIDoleG4e6U0j6EVQcjWXxzSO2Vv7Hqlgp2','ROlw3XYdNXNnII18ATs6zd7m5mivnApa')
obj = image.upload('/tmp/tencentyun.jpg');
print obj

fileid = obj['data']['fileid']
print image.stat(fileid)
```
### 2.4	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
def delete(self, fileid, userid=0) 
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileid|	String	|是	|无	|图片唯一ID
userid|	String|	否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：

参数名|	类型	|参数描述
---------|---------|---------
httpcode	|Int	|http响应码，请求正常时为200
code|	Int	|API 错误码，成功时为0
message|	String|	API错误信息
data	|Dict|	空字典

示例代码：

```
import tencentyun

image = tencentyun.Image('200679','AKIDoleG4e6U0j6EVQcjWXxzSO2Vv7Hqlgp2','ROlw3XYdNXNnII18ATs6zd7m5mivnApa')
obj = image.upload('/tmp/tencentyun.jpg');
print obj

fileid = obj['data']['fileid']
print image.delete(fileid)
```