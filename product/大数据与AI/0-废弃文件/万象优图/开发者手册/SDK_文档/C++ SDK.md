## 1	开发准备
万象优图服务的C++ SDK的下载地址： https://github.com/tencentyun/cpp_sdk
### 1.1	前期准备
前期准备
1.	安装openssl的库和头文件 http://www.openssl.org/source/ 
2.	安装curl的库和头文件 `http://curl.haxx.se/download/curl-7.43.0.tar.gz` 
3.	安装jsoncpp的库和头文件 https://github.com/open-source-parsers/jsoncpp 
4.	安装cmake工具 http://www.cmake.org/download/ 
注意：
1. sdk中提供了curl和jsoncpp的库以及头文件，以上库编译好后替换掉sdk中相应的库和头文件即可，如果以上库已经安装到系统里，也可删除sdk中相应的库和头文件。
2. curl默认不支持多线程环境，如果项目使用多线程，在编译curl执行 configure 时需指定 --enable-ares 参数来开启异步DNS解析，依赖 c-ares库，如果系统没有，可到http://c-ares.haxx.se/ 下载安装。
3. jsoncpp的1.y.x版本需要c++11的支持，如果编译器不支持，可以换成 0.y.x版本。
### 1.2	集成SDK
直接下载github上提供的源代码，集成到您的开发环境。 
执行下面的命令 

```
cd ${cpp-sdk} 
mkdir -p build 
cd build 
cmake .. 
make 
```
需要将sample.cpp里的appid、secretId、secretKey、bucket等信息换成您自己的。
生成的sample就可以直接运行，试用，生成的静态库，名称为:libimagesdk.a。 
生成的libimagesdk.a放到您自己的工程里lib路径下， 
include目录下的 Auth.h Imageapi.h curl json都放到您自己的工程的include路径下。 
例如我的项目里只有一个sample.cpp,项目目录和sdk在同级目录， 
copy libimagesdk.a 到项目所在目录那么编译命令为：

```
g++ -o sample sample.cpp -I ./include/ -L. -L../cpp-sdk/lib/ -limagesdk -lcurl -lcrypto -lssl -lrt -ljsoncpp
```
## 2	API详细说明
### 2.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供终端使用。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[鉴权服务技术方案](/doc/product/275/签名与鉴权文档)
2．	方法
多次有效签名

```
//v1版本时，bucketName为空
string Auth::appSign(const uint64_t appId,const string &secretId,const string &secretKey,const uint64_t expired,const string &bucketName,const string &fileId)
```
单次有效签名

```
//v1版本时，bucketName为空
string Auth::appSignOnce(const uint64_t appId,const string &secretId,const string &secretKey,const string &bucketName,const string &fileId)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
appId|	String|	是|	无|	开发者创建图片空间时，系统返回的项目ID
secretId|	String|	是|	无|	开发者的授权Secret ID
secretKey|	String|	是|	无|	开发者的授权Secret Key
bucketName|	String|	否|	无|	V2版本签名需要的空间名
expired|	expired|	否|	无|	过期时间，Unix时间戳
fileId|	String|	否|	无|	资源ID

返回值：签名字符串

示例代码：

```
uint64_t expired = time(NULL) + 60;
string sign = Auth::appSign(APP_ID,SECRET_ID,SECRET_KEY,expired,BUCKET,fileId);
cout << "sign:" << sign << endl;
```
### 2.2	图片上传
1．	接口说明
用于较小图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileId（用于调用其他api）。
2．	方法

```
   int upload(const string &srcPath,const string &fileId,const string &magicContext);
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
srcPath|	String|	是|	无|	本地图片文件路径
fileId|	String|	否|	空|	用户自定义文件名
magicContext|	String|	否|	空|	上传成功后，用户自定义的回调参数

返回值：通过类的成员变量Json::Value retJson返回请求结果：

参数名|	类型|	参数描述
code|	Int|	错误码，成功时为0
message|	String|	错误信息
data|	Array|	返回数据
data.url|	String|	图片的管理URL
data.download_url|	String|	图片的下载和访问URL
data.fileid|	String|	图片的唯一ID
data.info.0.0.width|	Int|	图片宽度
data.info.0.0.height|	Int|	图片高度

示例代码：

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
string srcPath = "/myFolder/test.jpg";
api.upload(srcPath);
api.dump_res();
```
### 2.3	图片分片上传
1．	接口说明
用于较大图片的上传，调用者可以通过此接口分片上传图片，获得图片的url和唯一标识fileId（用于调用其他api）。
2．	方法

```
int uploadSlice(const string &srcPath,const string &fileId,const uint64_t sliceSize,const string &session,const string &magicContext);
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
srcPath|	String|	是|	无|	本地图片文件路径
fileId|	String|	否|	空|	用户自定义文件名
magicContext|	String|	否|	空|	上传成功后，用户自定义的回调参数
sliceSize|	uint64_t|	否|	512*1024字节|	用户自定义的分片大小
session|	String|	否|	空|	如果是断点续传, 则带上(唯一标识此文件传输过程的id, 由后台下发, 调用方透传)


返回值：通过类的成员变量Json::Value retJson返回请求结果：

参数名|	类型|	参数描述
---------|---------|---------
code|	Int|	错误码，成功时为0
message|	String|	错误信息
data|	Array|	返回数据
data.url|	String|	图片的管理URL
data.download_url|	String|	图片的下载和访问URL
data.fileid|	String|	图片的唯一ID
data.info.0.0.width|	int|	图片宽度
data.info.0.0.height|	int|	图片高度

示例代码：

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
string srcPath = "/myFolder/test.jpg";
api.uploadSlice(srcPath);
api.dump_res();
```
### 2.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
int Imageapi::stat(const string &fileId,const uint64_t userId)
```
3．	参数和返回值
参数说明：

参数名	|类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
fileid	|String|	是|	无|	图片唯一ID
userid	|uint64_t	|否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：通过类的成员变量Json::Value retJson返回请求结果：

参数名|	类型|	参数描述
---------|---------|---------
code|	Int|	API 错误码，成功时为0
message|	String|	API错误信息
data|	Array|	API 返回数据
data.downloadUrl|	String|	图片的下载和访问URL
data.url|	String|	管理url
data.fileid|	String|	图片的唯一ID
data.uploadTime|	String|	图片的上传时间
data.size|	Int|	图片的大小（Bytes）
data.md5|	String|	图片的md5值
data.width|	Int|	图片的宽度（pixels）
data.height|	Int|	图片的高度（pixels）

示例代码：
### 2.5	图片删除

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
api.stat(fileId);
api.dump_res();
```
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法

```
int del(const string &fileId,const uint64_t userId=0);
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值|	参数描述
---------|---------|---------|---------|---------
fileid|	String|	是	|无	|图片唯一ID
userid|	uint64_t	|否	|0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：通过类的成员变量Json::Value retJson返回请求结果：

参数名	|类型	|参数描述
---------|---------|---------
code|	Int|	API 错误码，成功时为0
message|	String	|API错误信息

示例代码：

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
api.del(fileId);
api.dump_res();
```
### 2.6 图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片，获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
int copy(const string &fileId,const uint64_t userId=0);
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
fileid	|String|	是	|无	|图片唯一ID
userid	|uint64_t|	否|	0	|开发者的账号体系的userid, 如果没有，请使用默认值0

返回值：通过类的成员变量Json::Value retJson返回请求结果

参数名|	类型|	参数描述
---------|---------|---------
code	|Int|	API 错误码，成功时为0
message	|String	|API错误信息
data	|Array	|API返回数据
data.downloadUrl	|String	|图片的下载和访问URL
data.url	|String	|管理url

示例代码：

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
api.copy(fileId);
api.dump_res();
```
### 2.7 黄图识别
1．	接口说明
用于黄图的鉴别， 调用者可以通过此接口，输入图片的url，获取智能鉴黄的结果。
2．	方法

```
int pornDetect(const string &url);
```
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值|	参数描述
---------|---------|---------|---------|---------
url	|String	|是	|无	|需要鉴别的图片url，必须是公网可以访问的url

返回值：通过类的成员变量Json::Value retJson返回请求结果

参数名|	类型|	参数描述
---------|---------|---------
code|	Int	|API 错误码，成功时为0
message|	String	|API错误信息
data	|Array	|API返回数据
data.result|	Int	|供参考的识别结果，0正常，1黄图，2疑似图片
data.confidence	|double	|识别为黄图的置信度，范围0-100；是normal_score, hot_score, porn_score的总和评分
data.normal_score	|double|	图片为正常图片的评分
data.hot_score	|double|	图片为性感图片的评分
data.porn_score	|double|	图片为色情图片的评分

示例代码：

```
Imageapi api(APP_ID,SECRET_ID,SECRET_KEY,BUCKET,30);
api.pornDetect(url);
api.dump_res();
```
## 3	错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。
