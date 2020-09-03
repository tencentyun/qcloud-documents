
## 开发准备
### SDK 获取
智能图像的 PHP SDK 下载地址：[PHP-SDK-V2.0](https://github.com/tencentyun/image-php-sdk-v2.0)。
## 快速入门

### 在腾讯云申请业务的授权
授权包括： APPID 、SecretId 、SecretKey ，目前只支持主账号及密钥进行调用。
>!BUCKET 为历史遗留字段，无需修改。

### 创建对应操作类的对象
如果要使用图片，需要创建图片操作类对象：
```
require_once DIR . '/index.php';
use QcloudImage\CIClient;
$client = new CIClient('APP_ID', 'SECRET_ID', 'SECRET_KEY', 'BUCKET');
$client->setTimeout(30);
```
### 调用对应的方法
创建完对象后，您可以根据实际需求调用对应的操作方法。
### 图片识别
图片识别包括：图片鉴黄、图像分析、OCR - 身份证识别及 OCR - 名片识别。
#### 图片鉴黄
```
//单个或多个图片 URL
var_dump ($client->pornDetect(array('urls'=>array('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png',
"http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg"))));
//单个或多个图片 file
var_dump ($client->pornDetect(array('files'=>array('F:\pic\您好.jpg','G:\pic\test2.jpg'))));
```
#### 图像分析
```
//单个图片 URL
var_dump ($client->tagDetect(array('url'=>'http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')));
//单个图片 file
var_dump ($client->tagDetect(array('file'=>'G:\pic\hot1.jpg')));
//单个图片内容
var_dump ($client->tagDetect(array('buffer'=>file_get_contents('G:\pic\hot1.jpg'))));
```
#### OCR - 身份证识别
```
//单个或多个图片 URL，识别身份证正面
var_dump ($client->idcardDetect(array('urls'=>array('http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg',                                       								        'http://img5.iqilu.com/c/u/2013/0530/1369896921237.jpg')), 0));
//单个或多个图片 file，识别身份证正面
var_dump ($client->idcardDetect(array('files'=>array('F:\pic\id6zheng.jpg', 'F:\pic\id2zheng.jpg')), 0));
//单个或多个图片内容，识别身份证正面
var_dump ($client->idcardDetect(array('buffers'=>array(file_get_contents('F:\pic\id6_zheng.jpg'),                                                                
												    file_get_contents('F:\pic\id2_zheng.jpg'))), 0));
//单个或多个图片 URL，识别身份证反面
var_dump ($client->idcardDetect(array('urls'=>array('http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg',
                                                    'http://www.4009951551.com/upload/image/20151026/1445831136187479.png')), 1));
//单个或多个图片 file，识别身份证反面
var_dump ($client->idcardDetect(array('files'=>array('F:\pic\id5fan.jpg', 'F:\pic\id7fan.png')), 1));
//单个或多个图片内容，识别身份证反面
var_dump ($client->idcardDetect(array('buffers'=>array(file_get_contents('F:\pic\id5_fan.jpg'),
                                                       file_get_contents('F:\pic\id7_fan.jpg'))), 1));
```
#### OCR - 名片识别  
```
//单个或多个图片 HRL
var_dump ($client->namecardV2Detect(array('urls'=>array('http://open.youtu.qq.com/app/img/experience/char_general/ocr_namecard_01.jpg'))));
//单个或多个图片 file
var_dump ($client->namecardV2Detect(array('files'=>array('assets/ocr_namecard_01.jpg'))));
//单个或多个图片内容
var_dump ($client->namecardV2Detect(array('buffers'=>array(file_get_contents('assets/ocr_namecard_01.jpg')))));
```
