## 1	开发准备
万象优图服务的java sdk的下载地址： https://github.com/tencentyun/java-sdk.git
### 1.1	前期准备
1.	sdk采用1.8版本的jdk开发， 推荐使用相同的版本。如果使用其他版本，建议不要直接导入jar包，自行编译为佳；
2.	获取appid，secret_id和secret_key；
3.	Sdk开发采用netbeans，本文档以netbeans为例，其他IDE请适当调整。
### 1.2	导入SDK
1.	下载java sdk
如果安装了git命令行，执行git clone https://github.com/tencentyun/java-sdk.git
或者直接在github下载zip包。
2.	导入项目
在IDE中导入jar包（如果代码不支持，可以直接复制代码文件）
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/jieruwanxiang-22.jpg)
4.	3.	参照api说明和sdk中提供的demo，开发代码。
## 2	相关数据结构定义
### 2.1 UploadResult

名称|	类型|	含义
---------|---------|---------
url|	String	|图片的资源url
download_url|	String	|图片的下载url
fileid	|String|	图片资源的唯一标识
width	|int|	图片宽度
height	|int	|图片高度


### 2.2 PicInfo

名称	|类型|	含义
---------|---------|---------
url	|String|	图片的资源url
fileid|	String|	图片资源的唯一标识
upload_time	|String|	图片上传时间，unix时间戳
download_url	|int|	图片的下载url
size	|int|	图片大小，单位byte
md5	|String|	图片md5
width|	int	|图片宽度
height|	int	|图片高度


## 3	API详细说明
### 3.1	生成签名
1．	接口说明
签名生成方法，可以在服务端生成签名，供移动端app使用。
签名分为2种：
多次有效签名（有一定的有效时间）
单次有效签名（绑定资源url，只能生效一次）
签名的详细描述及使用场景参见[鉴权服务技术方案](/doc/product/275/签名与鉴权文档-V1)
2．	方法
多次有效签名

```
int appSign(String appId, String secret_id, String secret_key, long expired, String userid, StringBuffer mySign)
```
单次有效签名

```
int appSignOnce(String appId, String secret_id, String secret_key, String userid, String url, StringBuffer mySign)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须	|默认值|	参数描述
---------|---------|---------|---------|---------
appId	|String	|是	|无|	开发者的授权appid
secret_id|	String	|是|	无	|开发者的授权secret_id
secret_key	|String|	是	|无	|开发者的授权secret_key
expired|	long|	否	|无	|过期时间，Unix时间戳
userid	|String	|是|	无	|开发者的账号体系的userid, 如果没有，请填0
url	|String|	否|	无	|图片资源的下载url
mySign|	String	|是	|无	|返回值，返回的生成的签名串


返回值：

正确返回值|	返回码	|结果说明
---------|---------|---------
 |0	|成功

错误返回值|	返回码	|结果说明
---------|---------|---------
 |-1	|传入参数错误
 |-2|	userid非法
 |-3|	url非法


示例代码：

```
long expired = System.currentTimeMillis() / 1000 + 2592000;
if( FileCloudSign.appSign(Integer.toString(m_appid), m_secret_id, m_secret_key, expired, userid, sign) != 0)
{
    return SetError(-1, "create app sign failed");
}
```
### 3.2	图片上传
1．	接口说明
用于图片的上传，调用者可以通过此接口上传图片并获得图片的url和唯一标识fileid（用于调用其他api）。
2．	方法
int Upload(String userid, String fileName, UploadResult result) 
3．	参数和返回值
参数说明：

参数名	类型|	必须	|默认值	|参数描述
---------|---------|---------|---------|---------
userid|	String|	是	|无|	开发者的账号体系的userid, 如果没有，请填0
fileName|	String|	是|	无	|需要上传的图片的路径名
result|	UploadResult|	是|	无|	返回参数，上传图片的信息，具体属性参见数据结构定义部分


返回值：

正确返回值	|返回码|	结果说明
---------|---------|---------
 |0	|成功

错误返回值	|返回码	|结果说明
---------|---------|---------
 |-1|	错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
UploadResult result = new UploadResult();
int ret = pc.Upload(userid, "pic_path", result);
```


### 3.3	图片复制
1．	接口说明
用于图片的复制，调用者可以通过此接口复制已经上传的图片并获得新图片的url和唯一标识fileid（用于调用其他api）。
2．	方法

```
int Copy(String userid, String fileid, UploadResult result)
```
3．	参数和返回值
参数说明：

参数名|	类型|	必须|	默认值	|参数描述
---------|---------|---------|---------|---------
userid	|String	|是	|无	|开发者的账号体系的userid, 如果没有，请填0
fileid	|String	|是	|无	|图片资源的唯一标识
result	|UploadResult|	是|	无	|返回参数，复制的新图片的信息，具体属性参见数据结构定义部分


返回值：

正确返回值	|返回码	|结果说明
---------|---------|---------
 |0	|成功

错误返回值|	返回码|	结果说明
---------|---------|---------
 |-1	|错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
UploadResult result = new UploadResult();
int ret = pc.Copy(userid, fileid, result);
```


### 3.4	图片查询
1．	接口说明
用于图片的查询，调用者可以通过此接口查询已经上传的图片并获得图片的各种参数信息。
2．	方法
int Stat(String userid, String fileid, PicInfo info) 
3．	参数和返回值
参数说明：

参数名	|类型	|必须	|默认值	|参数描述
---------|---------|---------|---------|---------
userid|	String	|是	|无	|开发者的账号体系的userid, 如果没有，请填0
fileid	|String|是	|无|	图片资源的唯一标识
info|	PicInfo	|是|	无	|返回参数，图片的各种属性，具体属性参见数据结构定义部分


返回值：

正确返回值|	返回码|	结果说明
---------|---------|---------
 |0	|成功

错误返回值	|返回码|	结果说明
---------|---------|---------
 |-1	|错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
PicInfo info = new PicInfo(); 
int ret = pc.Stat(userid, fileid, info);
```


### 3.5	图片删除
1．	接口说明
用于图片的删除，调用者可以通过此接口删除已经上传的图片。
2．	方法
int Delete(String userid, String fileid) 
3．	参数和返回值
参数说明：

参数名	|类型	|必须|	默认值|	参数描述
---------|---------|---------|---------|---------
userid|	String	|是	|无	|开发者的账号体系的userid, 如果没有，请填0
fileid	|String|	是	|无	|图片资源的唯一标识


返回值：

正确返回值|	返回码	|结果说明
---------|---------|---------
 |0	|成功

错误返回值|	返回码|	结果说明
---------|---------|---------
 |-1|	错误描述可以通过GetError方法获得


示例代码：

```
PicCloud pc = new PicCloud(APP_ID, SECRET_ID, SECRET_KEY);	
int ret = pc.Delete(userid,  fileid);
```