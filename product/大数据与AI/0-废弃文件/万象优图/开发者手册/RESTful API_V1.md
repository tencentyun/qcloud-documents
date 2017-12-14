## 1	基本概念
概念|解释
---------|---------
appid|	接入万象优图时,生成为唯一id, 用于唯一标识接入业务
userid|	接入业务自行定义的用户id, 为了灵活,我们一致认为是字符串形式. 如果有业务没有用户id或者不想要使用用户id,那么可以填”0”.
fileid|	资源存储的唯一标识

## 2	鉴权
腾讯云•万象优图通过签名来验证请求的合法性。开发者通过将签名授权给客户端，使其具备上传下载及管理指定资源的能力。
签名分为单次签名和多次签名, 区别为: 如果针对资源进行写操作(资源删除和资源复制), 那么这个签名必须是单次有效的.重复使用该签名则会返回签名失败.如果是上传一个新的资源,那么这个签名可以是多次有效的.有效时长最多为三个月. 下载时,签名既可以是多次有效（不绑定资源URL）,也可以是单次有效的（绑定资源URL，即只能对固定资源使用一次）。
开发者可以通过[服务器SDK文档(V1版本)](/doc/product/275/SDK文档#3.-.E6.9C.8D.E5.8A.A1.E5.99.A8sdk.E6.96.87.E6.A1.A3)生成签名，也可以参考我们的签名函数自行生成签名，，具体生成方式详见[鉴权签名方法](/doc/product/275/签名与鉴权文档-V1)。
## 3	图片上传
功能: 直接上传单张图片, 只支持POST表单(multipart/form-data)方式, 目前只支持20M以内的图片。
接口: `http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]` 
注：</b>fileid为可选参数，fileid为空表示由后台自动生成fileid；不为空表示自定义fileid，fileid不可重复。
方法: POST
请求参数HTTP头部信息:

参数名称|	必选|	类型|	描述
---------|---------|---------|---------
Host|	是|	String|	图片云服务器域名，固定为web.image.myqcloud.com
Content-Length|	是|	Int|	整个multipart/form-data内容的总长度，单位：字节（Byte）。
Content-Type|	是|	String|	标准的multipart/form-data 格式，参见[rfc1867](http://www.ietf.org/rfc/rfc1867.txt)
Authorization|	是|	String|	多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法（不绑定资源多次签名）](/doc/product/275/签名与鉴权文档-V1)


HTTP包头

参数名称|	必选|	类型|	描述
---------|---------|---------|---------
MagicContext|	否|	String|	业务附加信息,当配置回调时，腾讯云•万象优图会透传给开发者的服务器.
FileContent|	是|	Binary|	文件内容
Md5|	否|	String|	图片的Md5值,如果提供,服务会对上传的文件做Md5校验及秒传


返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400
返回内容(json):

字段名称|	描述
---------|---------
code|	服务器错误码, 0为成功	
message|	服务器返回的信息	
data|	具体查询数据. 内容见下表	


data里面字段描述:

字段名称|	描述|	格式
---------|---------|---------
url|	资源url(用于restful api交互, 如查询,复制,删除资源)|	`http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]`
download_url|	生成的下载资源url(用于下载)|	`http://[appid].image.myqcloud.com/[appid]/[userid]/[fileid]/original`
fileid|	生成的资源唯一标识符|
info|	图片的具体信息，见下表|	


info里面字段描述：

数组名称|	字段名称|	描述
---------|---------|---------
0|	height|	图片高度
|width|	图片宽度


请求示例:
```
POST /photos/v1/201561/123456 HTTP/1.1
Host: web.image.myqcloud.com
Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468
Authorization: gZIdzEk4HZuOhQzscBv2hvZTlQphPTIwMTU2MSZrPUFLSURraHIzRjY2cEQ3ZEVidlFRakpEWlFjR3VLVGo4dWFBSSZ
lPTE0MzcwMzk4MzQmdD0xNDM0NDQ3ODM0JnI9MTExNjcwMDMyNSZ1PTEyMzQ1NiZmPQ==
Content-Length: 576924

---------------------------acebdf13572468
Content-Disposition: form-data; name=&quot;filecontent&quot;; filename=&quot;tencentyun.jpg&quot;
Content-Type: image/jpeg

&lt;@INCLUDE *E:\photos\tencentyun.jpg*@&gt;
---------------------------acebdf13572468--
```
## 4	图片复制
功能: 将图片复制一份(保留原有图片)。
接口: `http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]/copy`
方法: POST
请求参数HTTP头部信息:

参数名称|	必选|	类型|	描述
---------|---------|---------|---------
Host|	是|	String|	图片云服务器域名，固定为web.image.myqcloud.com
Authorization|	是|	String|	单次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](/doc/product/275/签名与鉴权文档-V1)
返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400
返回内容(json):

字段名称|	描述
---------|---------
code|	服务器错误码, 0为成功	
message|	服务器返回的信息	
data|	具体查询数据. 内容见下表	

data里面字段描述:

字段名称|	描述|	格式
---------|---------|---------
url|	资源url(用于restful api交互, 如查询,复制,删除资源)|	`http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]`
download_url|	生成的下载资源url(用于下载)|	`http://[appid].image.myqcloud.com/[appid]/[userid]/[fileid]`
请求示例:
```
POST /photos/v1/201561/123456/4affadae-9e94-4cdc-82cc-ac86e9f4f4b7/copy HTTP/1.1
Host: `web.image.myqcloud.com`
Authorization: 3J0EpeWAU3Xm3miaputSLAkj21JhPTIwMTU2MSZrPUFLSURraHIzRjY2cEQ3ZEVidlFRakpEWlFjR3VLVGo4dWFBSSZ
lPTAmdD0xNDM0NDQ4Njg3JnI9MTQyNzU2MDEzMyZ1PTEyMzQ1NiZmPTRhZmZhZGFlLTllOTQtNGNkYy04MmNjLWFjODZlOWY0ZjRiNw==
Content-Length: 0
```
## 5	图片查询
功能: 查看文件的属性信息，包含：文件哈希值、文件大小、上传时间等，图片和视频返回的信息会有所不同。
接口: `http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]/`
方法: GET
请求参数HTTP头部信息:

参数名称|	必选|	类型|	描述
---------|---------|---------|---------
Host|	是|	String|	图片云服务器域名，固定为web.image.myqcloud.com

返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400
返回内容(json):

字段名称|	描述
---------|---------
code|	服务器错误码, 0为成功	
message|	服务器返回的信息	
data|	具体查询数据. 内容见下表	

data里面字段描述:

字段名称|	描述|	格式
---------|---------|---------
file_url|	图片资源的下载url|	`http://[appid].image.myqcloud.com/[appid]/[userid]/[fileid]`
file_fileid|	图片资源的唯一id	|
file_upload_time|	图片上传时间|	Unix timestamp
file_size|	图片的大小|	单位: Byte
file_md5|	图片的MD5值|	16进制的MD5值
photo_width|	图片的宽度|	
photo_height|	图片的长度|

请求示例:
```
GET /photos/v1/201561/123456/4affadae-9e94-4cdc-82cc-ac86e9f4f4b7 HTTP/1.1
Host: web.image.myqcloud.com
```
## 6	图片删除
功能: 删除一个图片。
接口: `http://web.image.myqcloud.com/photos/v1/[appid]/[userid]/[fileid]/del`
方法: POST
请求参数HTTP头部信息:

参数名称|	必选|	类型|	描述
---------|---------|---------|---------
Host|	是|	String|	图片云服务器域名，固定为web.image.myqcloud.com
Authorization|	是|	String|	单次有效签名,用于鉴权，具体生成方式详见[鉴权签名方法](/doc/product/275/签名与鉴权文档-V1)

返回的HTTPP 状态码: 
- 成功: 200
- 失败: 400
返回内容(json):

字段名称|	描述
---------|---------
code|	服务器错误码, 0为成功	
message|	服务器返回的信息
请求示例:
```
POST /photos/v1/201561/123456/4affadae-9e94-4cdc-82cc-ac86e9f4f4b7/del HTTP/1.1
Host: web.image.myqcloud.com
Authorization: ay75r43erVJekjk8ZmHjpNq9rp1hPTIwMTU2MSZrPUFLSURraHIzRjY2cEQ3ZEVidlFRakpEWlFjR3VLVGo4dWFBSSZ
lPTAmdD0xNDM0NDQ5NTc1JnI9Mjk0ODk5OTQ4JnU9MTIzNDU2JmY9NGFmZmFkYWUtOWU5NC00Y2RjLTgyY2MtYWM4NmU5ZjRmNGI3
Content-Length: 0
```
##  7	图片下载
图片下载可以是公开下载，即使用图片的download_url 直接访问即可。
请求示例：
```
GET /201561/123456/4affadae-9e94-4cdc-82cc-ac86e9f4f4b7/original HTTP/1.1
Host: 201561.image.myqcloud.com
```
若开启了token防盗链，图片下载只能是私密下载，即必须download_url +?sign=[签名]。
请求示例:
```
GET /201561/123456/4affadae-9e94-4cdc-82cc-ac86e9f4f4b7/original?sign=bXiSDdRNtjxlm7ayaH3L1QXoDbdhPTIwMTU2
MSZrPUFLSURraHIzRjY2cEQ3ZEVidlFRakpEWlFjR3VLVGo4dWFBSSZlPTE0MzcwNDA2ODcmdD0xNDM0NDQ4Njg3JnI9Njk1OTc2MjUzJn
U9MTIzNDU2JmY9 HTTP/1.1
Host: 201561.image.myqcloud.com
```
图片下载支持实时压缩等动态处理，详见以下 8.图像处理

## 8	图像处理
### 8.1	基本格式
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]`
domain&nbsp;:[appid].image.myqcloud.com
其中[appid]为用户app的接入id。

参数名称|	参数含义|	说明
---------|---------|---------
appid|	为用户app分配的接入id|	
userid|	同个id下每个用户的唯一编号|	开发者用户体系同的userid 若没有可填0
fileid|	上传图片后返回的文件id|	开发者用户体系同的userid 若没有可填0
pattern|	用户针对每个缩略图样式定义的名字|	取代一些以数字标记规格的方式，增强灵活性和解决相同规格不同压缩方式的冲突；当pattern为original表示原图，其他为用户自定义的样式名

示例:
```
//myPattern样式图，myPattern为开发者自定义样式
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/myPattern
//原图
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/original
```
### 8.2	普通缩放功能
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?ss=1&amp;w=100&amp;h=80`

参数名称|	参数值|	说明
---------|---------|---------
w|	图片宽	|取值范围10-16383
h|	图片高|	取值范围10-16383
ss|	1: 限定长边，短边自适应缩放;0：限定短边，长边自适应缩放;默认为0	|缩放方式
domain, appid, userid, fileid, pattern等参数参见[基本格式参数说明](#8-.E5.9B.BE.E5.83.8F.E5.A4.84.E7.90.86)。
注：假如样式[parttern]图大小（wh）为200400，将其缩放为10080，按照等比缩放，采用不同的缩放方式可以缩放为100200或者4080两种，具体如下：
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?ss=0&amp;w=100&amp;h=80`
限定短边的缩放方式，返回的缩略图大小为4080（等比缩放，缩略后的图片宽最多100，高最多80）
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?ss=1&amp;w=100&amp;h=80`
限定长边的缩放方式，返回的缩略图大小为100200（等比缩放，缩略后的图片宽最少100，高最少80）
示例:
```
//myPattern为开发者自定义样式
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/myPattern?
ss=1&amp;w=100&amp;h=80
```
### 8.3	水印功能
 url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?`
    watermark=1&amp;wpos=north&amp;wpx=10&amp;wpy=10&amp;wlw=200&amp;wlh=200
    &amp;ww=water_test&amp;font=&lt;encodedFontName&gt;&amp;fontsize=&lt;fontSize&gt;
    &amp;fill=&lt;encodedTextColor&gt;&amp;dissolve=&lt;dissolve&gt;<


参数名称|	参数值|	说明|	默认值
---------|---------|---------|---------
watermark|	1，开启；0，不开启|	是否开启水印功能，只有开启水印功能，下面的参数设置才会生效。|	0
ww|	水印文字|	需要打在图片上的水印文字，需要经过安全的URL编码|	不填默认不打文字水印
wpos|	九宫格形式：northwest；north; northeast; west；middle；east；southwest；south；southeast|	水印位置|middle
wpx|	文字在宽方向上的偏移量	根据参数wp的位置确定的九宫格的某个位置后，wpx的值为原点开始偏移后，进行打水印操作|	0，不大于原图宽|
wpy|	文字在高方向上的偏移量	根据参数wp的位置确定的九宫格的某个位置后，wpy的值为原点开始偏移后，进行打水印操作|	0，不大于原图高|
wlw|	打水印最小宽|	原图小于参数中传入的宽或者高，这张图不会打水印|	0
wlh|	打水印最小高|	原图小于参数中传入的宽或者高，这张图不会打水印|	0
font|	encodedFontName, 水印字体，需要经过URL安全的Base64编码。|	水印字体列表参考[支持字体列表](/doc/product/275/万象优图支持字体列表)|	tahoma.ttf
fontsize|	fontSize|水印文字字体大小，单位是: 磅	|13
fill|	encodedTextColor|字体颜色，缺省为白色，RGB格式，可以是颜色名称（如blue）或者十六进制（如#FF0000），参考RGB编码表，需经过URL安全的Base64编码|	#3D3D3D
dissolve|	dissolve|文字透明度，取值1-100|	100（完全不透明）
domain, appid, userid, fileid, pattern等参数参见[基本格式参数说明](#8-.E5.9B.BE.E5.83.8F.E5.A4.84.E7.90.86)。
九宫格图如下：
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/apicankao-3.jpg" alt="apicankao-3.jpg" /><br /><br />
示例:
```
//myPattern为开发者自定义样式
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/myPattern?
watermark=1&amp;wpos=north&amp;wpx=10&amp;wpy=10&amp;wlw=200&amp;wlh=200&amp;ww=water_test
```
### 8.4	裁剪功能
一般裁剪功能：
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?crop=1&amp;cpx=0&amp;cpy=0&amp;cpos=north&amp;w=300&amp;h=300`
一般裁剪功能：
url=`http://[domain]/[appid]/[userid]/[fileid]/[pattern]?scrop=1&amp;w=300&amp;h=300`

参数名称|	参数值|	说明|	默认值
---------|---------|---------|---------
crop|	1，开启；0，不开启|	是否开启裁剪功能，只有开启裁剪功能，下面的参数设置才会生效|	0
scrop|	1，开启；0，不开启|	基于人脸识别执行智能裁剪功能。裁剪区域根据人的头像位置自动确定。 输出的裁剪后图片大小需要结合宽高参数指定。|	0
ww|	水印文字|	需要打在图片上的水印文字|	不填默认不打文字水印
cpos|	九宫格形式：northwest，north，northeast，west，middle，east，southwest，south，southeast	|裁剪方位|	middle
cpx|	裁剪位置在宽方向的偏移量|裁剪动作在宽方向上的偏移量，根据参数cpos的位置确定的九宫格的某个位置后，cpx的值为原点开始偏移后，进行裁剪操作|	0
cpy|	裁剪位置在高方向的偏移量	|裁剪动作在高方向上的偏移量，根据参数cpos的位置确定的九宫格的某个位置后，cpx的值为原点开始偏移后，进行裁剪操作|	0
w	|图片裁剪后的宽度|	取值范围10-16383|	原图
h|	图片裁剪后的高度|	取值范围10-16383|	原图

domain, appid, userid, fileid, pattern等参数参见[基本格式参数说明](#8-.E5.9B.BE.E5.83.8F.E5.A4.84.E7.90.86)。


scrop 参数与 crop 参数同时使用，当智能裁剪没有识别到人脸时，会执行普通的裁剪。 
`http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/original?scrop=1&amp;crop=1&amp;w=300&amp;h=300`
示例:
```
//myPattern为开发者自定义样式
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/myPattern?
crop=1&amp;cpx=0&amp;cpy=0&amp;cpos=north&amp;w=300&amp;h=300
http://201405.image.myqcloud.com/201405/123456/8d72f95e-f8cc-4962-b787-cc1d218475e0/original?scrop=1&amp;w=300&amp;h=300
```
### 8.5	更多功能

参数名称|	参数值|	说明|	默认值
---------|---------|---------|---------
strip|	1，开启；0，不开启|	除不安全代码包括exif信息|	1
cgif|	1，开启；0，不开启|	压缩gif图片的颜色数，降低gif图片大小|	99
sharp|	1，开启；0，不开启|	锐化|	0
srotate|	1，开启；0，不开启|	根据exif信息自动把图片旋转回正	|0
composite|	1，开启；0，不开启|	图片加边框，背景框大小按用户填的宽高|	0
### 8.6	特别参数 

参数名称|	参数值|	说明|	默认值
---------|---------|---------|---------
qa|	0-100|	图片质量只针对jpg和webp有效，其他格式的图无图片质量概念。若jpg输入值比原图大，会使用原图值。|	原图质量
pqa|	0-100|	强制提升图片质量，同上面的qa参数，只是若输入值比原图大，依旧使用输入值|	原图质量
t|	1转为jpg；2转为gif；3转为png；4转为bmp；5转为webp|	格式转换|	不转换格式
degree|	0-360|	图片旋转角度，取值范围0-360，使用智能旋转后，该参数会被忽略|	0
interlace|	1，开启；0，不开启	|输出为渐进式jpg格式。该参数仅在输出图片格式为jpg格式时有效。如果输出非jpg图片格式，会忽略该参数|	0


## 9 返回码定义

错误码|	含义
---------|---------
-5999|	参数错误
-5998|	签名格式错误
-5997|	后端网络错误
-5996|	HTTP请求方法错误
-5995|	文件大小错误
-5994|	url参数解析不匹配
-5993|	multipart/formdata参数错误
-5992|	请求参数错误
-5991|	分片过大
-5990|	找不到filecontent
-5989|	上传失败
-5988|	cgi初始化错误
-5987|	wup编码失败
-5986|	wup解码失败
-5985|	获取路由失败
-5984|	sha1不匹配
-5983|	错误的session
-5982|	建立连接错误
-5981|	建立连接错误
其他返回码参见[返回码说明](/doc/product/275/返回码说明)。
