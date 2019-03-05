Java-SDK说明文档-2.0.4
本文档为万象优图新版本（V2加强版本）的Java SDK文档，旧版本（V1和V2版本）的Java SDK文档分别参见 万象优图[Java SDK说明文档-V1](/doc/product/275/Java SDK_V1)和 万象优图[Java SDK说明文档-V2](/doc/product/275/Java SDK_V2)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。

## 1	开发准备
万象优图服务的java sdk的下载地址： https://github.com/tencentyun/java-sdk.git
注意：本文档适用于2.0.4版本，不适用于2.1.0（版本号可参考github）
### 1.1	前期准备
1.	请先申请万象的接入授权，才能正常使用java api sdk。万象的接入授权包括appid（项目ID），bucket，secret_id和secret_key，请先确保已经拿到这四项；
2.	sdk开发采用netbeans，本文档以netbeans为例，其他IDE请适当调整。
1.2	导入SDK
1.	下载java sdk
如果安装了git命令行，执行git clone https://github.com/tencentyun/java-sdk.git
或者直接在github下载zip包。
2.	导入项目
在IDE中导入jar包（如果代码不支持，可以直接复制代码文件）
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/jieruwanxiang-22.jpg)

3.	参照api说明和sdk中提供的demo，开发代码。

## 2	相关数据结构定义
### 2.1 PicCloud
图片sdk的类，所有api通过该类的对象调用。根据使用的restful api的版本，需要采用不同的初始化方式。
对2.0版本的api, 使用下面的方法初始化：
 PicCloud(int appid, String secret_id, String secret_key, String bucket)
对1.0版本的api，使用下面的方法初始化：
 PicCloud(int appid, String secret_id, String secret_key)

### 2.2 UploadResult

名称|	类型|	含义
---------|---------|---------
url	|String	|图片的资源url
download_url|	String|	图片的下载url
fileid|	String|	图片资源的唯一标识
width	|int|	图片宽度
height|	int	|图片高度


### 2.3 PicInfo

名称|	类型|	含义
---------|---------|---------
url|	String|	图片的资源url
fileid|	String|	图片资源的唯一标识
upload_time|	String|	图片上传时间，unix时间戳
size|	int|	图片大小，单位byte
md5|	String|	图片md5
width|	int|	图片宽度
height|	int|	图片高度

## 3	API详细说明
### 3.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供终端使用。
V1版本的api和V2版本的api的签名并不相同。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[鉴权服务技术方案](/doc/product/275/签名与鉴权文档)
2．	方法
多次有效签名

```
int appSignV2(String appId, String secret_id, String secret_key, String bucket, long expired, 
              StringBuffer mySign)
```

单次有效签名

```
int appSignOnceV2(String appId, String secret_id, String secret_key, String url, StringBuffer mySign)
```

3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|---------|---------|---------
appId|	String|	是|	无|	开发者创建图片空间时，系统返回的项目ID
secret_id|	String|	是|	无|	开发者的授权secret_id
secret_key|	String|	是|	无|	开发者的授权secret_key
secret_id|	String|	是|	无|	开发者的授权secret_id
bucket|	String|	|	无|	V2版本签名需要的空间名
expired|	long|	否|	无|	过期时间，Unix时间戳
url|	String|	否|	无|	图片资源的下载url
mySign|	String|	是|	无|	返回值，返回的生成的签名串

返回值：

正确返回值|	返回码|	结果说明
---------|---------|---------
 |0|	成功

错误返回值|	返回码|	结果说明
---------|---------|---------
 |-1	|传入参数错误
 |-3|	url非法


示例代码：

```
long expired = System.currentTimeMillis() / 1000 + 2592000;
if( FileCloudSign.appSign(
  Integer.toString(m_appid), 
  m_secret_id, 
  m_secret_key, 
  expired, 
  sign) 
!= 0){
        return SetError(-1, "create app sign failed");
   }
```
### 3.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法
//最简单的上传方法
int Upload(String fileName, UploadResult result)
//可以自定义fileid的上传方法
int Upload(String fileName, String fileid, UploadResult result)
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|--------|---------|--------
fileName|	String|	是	|无|	需要上传的图片的路径名
fileid|	String|	否|	无|	用户自定义的fileid
result|	UploadResult|	是|	无|	返回参数，上传图片的信息，具体属性参见数据结构定义部分


返回值：

正确返回值|	返回码	|结果说明
---------|---------|--------
 |0	|成功

错误返回值|	返回码	|结果说明
---------|---------|--------
 |-1|	错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
  UploadResult result = new UploadResult(); 
  int ret = pc.Upload(pic, result);
```


### 3.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法
int Copy(String fileid, UploadResult result) 
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值|	参数描述
---------|---------|---------|--------|---------
fileid|	String	|是	|无|	图片资源的唯一标识
result|	UploadResult|	是	|无	|返回参数，复制的新图片的信息，具体属性参见数据结构定义部分


返回值：

正确返回值|	返回码|	结果说明
---------|---------|--------
 |0	|成功

错误返回值	|返回码	|结果说明
---------|---------|--------
 |-1|	错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
UploadResult result = new UploadResult();
int ret = pc.Copy(fileid, result);
```


### 3.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法

```
int Stat(String fileid, PicInfo info) 
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值	|参数描述
---------|---------|--------|---------|--------
fileid|	String|	是	|无|	图片资源的唯一标识
info	|PicInfo|	是|	无	|返回参数，图片的各种属性，具体属性参见数据结构定义部分


返回值：

正确返回值|	返回码|	结果说明
---------|---------|--------
 |0	|成功

错误返回值	|返回码	|结果说明
---------|---------|--------
 |-1|	错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
PicInfo info = new PicInfo(); 
int ret = pc.Stat(fileid, info);
```
3.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法
int Delete(String fileid) 
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值|	参数描述
---------|---------|--------|---------|--------
fileid|	String|	是|	无|	图片资源的唯一标识


返回值：

正确返回值|	返回码	|结果说明
---------|---------|--------
 |0|	成功

错误返回值|	返回码|	结果说明
---------|---------|--------
 |-1	|错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
int ret = pc.Delete(fileid);
```
3.6	图片下载
图片下载可以直接使用下载url直接下载，开发者可自行下载，具体可参考[图片下载](/doc/product/275/RESTful API#7-.E5.9B.BE.E7.89.87.E4.B8.8B.E8.BD.BD)。腾讯云·万象优图在Java-SDK中也提供了下载功能，具体见下：
1．	接口说明
用于图片的下载，调用者可以通过此接口下载已经上传的图片到本地。
下载分为2种：开启防盗链和不开启防盗链。
需要根据实际情况调用不同的api方法。
2．	方法
不开启防盗链
int Download(String fileid, String fileName)
开启防盗链
int DownloadEx(String fileid, String fileName)
自己提供下载url（如果必要，需要自己处理防盗链的签名）
int Download(String download_url, String fileName)
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值|	参数描述
---------|---------|--------|---------|--------
fileid|	String|	是	|无|	图片资源的唯一标识
fileName|	String|	是|	无|	图片文件的保存路径


返回值：

正确返回值	|返回码	|结果说明
---------|---------|--------
 |0	|成功

错误返回值	|返回码	|结果说明
---------|---------|--------
 |-1	|错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);
//不开启防盗链
int ret = pc.Download(result.fileid, "./download.jpg");
//开启防盗链
int ret = pc.DownloadEx(result.fileid, "./download.jpg");
```
3 错误码说明
服务端SDK封装了Restful API，Restful API错误码参见[Restful API错误码](/doc/product/275/RESTful API#9-.E8.BF.94.E5.9B.9E.E7.A0.81.E5.AE.9A.E4.B9.89)；
其他错误码参见[错误码说明](/doc/product/275/返回码说明)。