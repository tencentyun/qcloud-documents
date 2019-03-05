本文档为万象优图新版本（V2加强版本）的GO SDK文档，旧版本（V1和V2版本）的GO SDK文档分别参见 万象优图[GO SDK说明文档-V1](/doc/product/275/GO SDK_V1)和 万象优图[GO SDK说明文档-V2](/doc/product/275/GO SDK_V2)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。
## 1	开发准备
万象优图服务的Go sdk的下载地址：https://github.com/tencentyun/go-sdk.git
### 1.1	前期准备
 通过图片空间获取appid（项目ID），secret_id和secret_key。

### 1.2	导入SDK
 1. 导入go-sdk包
在开发环境命令行直接执行下面的命令导入go-sdk包。
```
go get github.com/tencentyun/go-sdk
```
 2. 参考api说明和sdk中提供的demo，开发代码。demo.go对应v1版本的restful api, demoV2.go对应v2版本的restful api。

## 2	相关数据结构定义
### 2.1 icCloud
图片sdk的类，所有api通过该类的对象调用。根据使用的restful api的版本，需要采用不同的初始化方式。
对1.0版本的api，初始化bucket不用赋值：

```
 cloud := qcloud.PicCloud{appid, sid, skey, ""}
```
对2.0版本的api，初始化bucket必须赋值：

```
 cloud := qcloud.PicCloud{appid, sid, skey, bucket}
```
### 2.2 PicUrlInfo
图片的上传url信息，该类包含下面的属性：

名称	类型	含义
---------|---------|---------
Url	|string	|图片的资源url
DownloadUrl|string	|图片的下载url
Fileid	|string	|图片资源的唯一标识
Width	|uint	|图片宽度
Height	|uint	|图片高度

### 2.3 PicInfo
图片本身的属性信息，该类包含下面的属性：

名称	|类型	|含义
---------|---------|---------
Url	|string|	图片的资源url
Fileid	|string	|图片资源的唯一标识
UploadTime|	uint	|图片上传时间，unix时间戳
Size	|uint	|图片大小，单位byte
Md5	|string|	图片md5
Width	|uint	|图片宽度
Height|	uint	|图片高度

## 3	API详细说明
### 3.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
V1版本的api和V2版本的api的签名并不相同。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见签名适用场景
2．	方法
签名函数会自动根据PicCloud的设置，选择v1和v2版本的签名算法.
多次有效签名

```
　　func (pc *PicCloud) Sign(expire uint) (string, error)
```
单次有效签名

```
　　func (pc *PicCloud) SignOnce(fileid string) (string, error)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值|	参数描述
---------|---------|---------|---------|---------
expire	|uint|	否|	无	|过期时间，Unix时间戳
fileid|	string|	否	|无	|图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
 |string	|签名串
 |error|	错误信息

示例代码：

```
　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
  sign, err := cloud.Sign(expire)
  if nil != err {
     	//错误处理
  }
```
### 3.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
方法

```
  //最简单的上传方法
　func (pc *PicCloud) Upload(filename string) (UrlInfo, error)
  //可以自定义fileid的上传方法
  func (pc *PicCloud) UploadWithFileid(filename string, fileid string) (UrlInfo, error)
```
2．	参数和返回值
参数说明：

参数名|	类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
fileName	|string|	是	|无	|需要上传的图片的路径名

返回值：

参数名	|类型	|参数描述
---------|---------|---------
info|	UrlInfo	|返回的图片的url信息
err	|error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　info, err := cloud.Upload("./test.jpg")
　　if nil != err {
　　	//错误处理
　　}
```
### 3.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
  func (pc *PicCloud) Copy(fileid string) (info UrlInfo, err error) 
```
3．	参数和返回值
参数说明：

参数名	|类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
fileid	|string	|是	|无	|图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
info|	UrlInfo	|返回的图片的url信息
err|	error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　info, err := cloud.Copy(fileid)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
    func (pc *PicCloud) Stat(fileid string) (info PicInfo, err error)
```
3．	参数和返回值
参数说明：

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileid	|string|	是|	无|	图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
info	|PicInfo	|返回的图片的属性信息
err	|error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　picInfo, err = cloud.Stat(fileid)
　　if nil != err {
　　	//错误处理
　　}
```
### 3.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
　　func (pc *PicCloud) Delete(fileid string) error
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
fileid|	string|	是	|无	|图片资源的唯一标识

返回值：

参数名	|类型	|参数描述
---------|---------|---------
err|	error	|错误信息

示例代码：

```
　　cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
　　err = cloud.Delete(fileid)
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
  func (pc *PicCloud) Download(fileid string, filename string) error
```
开启防盗链

```
  func (pc *PicCloud) DownloadWithSign(fileid string, filename string) error
```
自己提供下载url（如果必要，需要自己处理防盗链的签名）

```
  func (pc *PicCloud) DownloadByUrl(url string, filename string) error
```
3．	参数和返回值
参数说明：

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileid	|string|	是	|无|	图片资源的唯一标识
filename|	string	|是|	无	|图片文件的保存路径

返回值：

参数名|	类型|	参数描述
---------|---------|---------
err	|error	|错误信息

示例代码：

```
  cloud := PicCloud{APPID, SECRET_ID, SECRET_KEY}
  err = cloud.Download(fileid, "./test2.jpg")
　if nil != err {
　　//错误处理
　}
```
## 3 错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。