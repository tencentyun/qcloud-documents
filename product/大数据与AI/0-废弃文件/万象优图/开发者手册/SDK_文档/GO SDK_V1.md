## 1	开发准备
万象优图服务的Go sdk的下载地址：https://github.com/tencentyun/go-sdk.git
### 1.1	前期准备
1. 获取appid，secret_id和secret_key。

### 1.2	导入SDK
1. 导入go-sdk包
在开发环境命令行直接执行下面的命令导入go-sdk包。
```
　　Go get github.com/tencentyun/go-sdk
```
2. 参考api说明和sdk中提供的demo，开发代码。

## 2	相关数据结构定义
### 2.1 PicCloud
图片sdk的类，所有api通过该类的对象调用。
初始化需要三个参数，appid，secret_id和secret_key，也就是万象服务的授权。
### 2.2 PicUrlInfo
图片的上传url信息，该类包含下面的属性：

名称|	类型	|含义
---------|---------|---------
Url|	string	|图片的资源url
DownloadUrl|	string	|图片的下载url
Fileid	|string|	图片资源的唯一标识
Width	|uint	|图片宽度
Height	|uint	|图片高度

### 2.3 PicInfo
图片本身的属性信息，该类包含下面的属性：

名称|	类型	|含义
---------|---------|---------
Url	|string	|图片的资源url
Fileid	|string	|图片资源的唯一标识
UploadTime|	uint	|图片上传时间，unix时间戳
Size|	uint	|图片大小，单位byte
Md5|	string|	图片md5
Width|	uint|	图片宽度
Height|	uint|	图片高度

## 3	API详细说明
### 3.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[签名适用场景](/doc/product/275/签名与鉴权文档-V1#1.3-.E7.AD.BE.E5.90.8D.E9.80.82.E7.94.A8.E5.9C.BA.E6.99.AF)
2．	方法
多次有效签名

```
　　func (pc *PicCloud) Sign(userid string, expire uint) (string, error)
```
单次有效签名

```
　　func (pc *PicCloud) SignOnceWithUrl(userid string, downloadUrl string) (string, error)
　　func (pc *PicCloud) SignOnce(userid string, fileid string) (string, error)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值|	参数描述
---------|---------|---------|---------|---------
expire|	uint	|否	|无	|过期时间，Unix时间戳
userid	|string|	是	|无	|开发者的账号体系的userid, 如果没有，请填0
downloadUrl	|string|	否|	无	|图片资源的下载url
fileid|	string|	否	|无	|图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
 |string	|签名串
 |error|	错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　sign, err := cloud.Sign(userid, expire)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.2	图片上传
1．接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
方法

```
　　func (pc *PicCloud) Upload(userid string, filename string) (info PicUrlInfo, err error)
```
3．	参数和返回值
参数说明：

参数名|	类型|必须	|默认值|	参数描述
---------|---------|---------|---------|---------
userid	|string	|是	|无|	开发者的账号体系的userid, 如果没有，请填0
fileName	|string	|是	|无	|需要上传的图片的路径名

返回值：

参数名	|类型	|参数描述
---------|---------|---------
info	|PicUrlInfo	|返回的图片的url信息
err	|error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　info, err := cloud.Upload(123456, "./test.jpg")
　　if nil != err {
　　	//错误处理
　　}
```
### 3.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
　　func (pc *PicCloud) Copy(userid string, fileid string) (info UrlInfo, err error) 
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
userid	|string	|是|	无	|开发者的账号体系的userid, 如果没有，请填0
fileid|	string|	是	|无|	图片资源的唯一标识

返回值：

参数名|	类型	|参数描述
---------|---------|---------
info|	UrlInfo	|返回的图片的url信息
err	|error|	错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　info, err := cloud.Copy(123456, fileid)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
    func (pc *PicCloud) Stat(userid string, fileid string) (info PicInfo, err error)
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
userid	|string|	是|	无	|开发者的账号体系的userid, 如果没有，请填0
fileid|	string|	是	|无|	图片资源的唯一标识

返回值：
参数名	|类型|	参数描述
---------|---------|---------
info	|PicInfo	|返回的图片的属性信息
err	|error|	错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　picInfo, err = cloud.Stat(123456, fileid)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
　　func (pc *PicCloud) Delete(userid string, fileid string) error
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值|	参数描述
---------|---------|---------|---------|---------
userid|	string|	是	|无|	开发者的账号体系的userid, 如果没有，请填0
fileid	|string|	是	|无|	图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
err	|error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　err = cloud.Delete(123456, fileid)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.6	图片下载
1．	接口说明
用于图片的下载，调用者可以通过此接口下载已经上传的图片到本地。下载分为2种：开启防盗链和不开启防盗链。开发者需要根据实际情况调用不同的api方法。
方法
不开启防盗链

```
　　func (pc *PicCloud) Download(userid string, fileid string, filename string) error
```
开启防盗链

```
　　func (pc *PicCloud) DownloadWithSign(userid string, fileid string, filename string) error
```
自己提供下载url（如果必要，需要自己处理防盗链的签名）

```
　　func (pc *PicCloud) DownloadByUrl(url string, filename string) error
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值|	参数描述
---------|---------|---------|---------|---------
userid	|string	|是	|无|	开发者的账号体系的userid, 如果没有，请填0
fileid	|string|	是|	无|	图片资源的唯一标识
filename	|string|	是|	无	|图片文件的保存路径

返回值：

参数名	|类型	|参数描述
---------|---------|---------
err|	error|	错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　err = cloud.Download(123456, fileid, "./test2.jpg")
　　if nil != err {
　　	//错误处理
　　}
```