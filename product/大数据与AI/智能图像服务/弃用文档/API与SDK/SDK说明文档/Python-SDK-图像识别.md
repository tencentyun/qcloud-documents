## 开发准备
### SDK 获取

万象优图的 Python SDK 下载地址：[Python-SDK-V2.0](https://github.com/tencentyun/image-python-sdk-v2.0) 。

### 开发准备
**使用pip**
Python 2:
pip install qcloud_image
Python 3:
pip3 install qcloud_image
## 快速入门
### 在腾讯云申请业务的授权

授权包括： APPID 、SecretId 、 SecretKey 及存储桶名（可参考 [域名管理](https://cloud.tencent.com/document/product/460/6937) ）。

### 创建对应操作类的对象
如果要使用图片，需要创建图片操作类对象：
```
from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers
appid = 'APP_ID'
secret_id = 'SECRET_ID'
secret_key = 'SECRET_KEY'
bucket = 'BUCKET'
client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)
```

### 调用对应的方法
在创建完对象后，根据实际需求，调用对应的操作方法就可以了。sdk 提供的方法包括：图片识别、人脸识别及人脸核身等。
### 图片识别
图片识别包括：图片鉴黄、图片标签、OCR - 身份证识别及 OCR - 名片识别。
#### 图片鉴黄
```
//单个或多个图片Url
print (client.porn_detect(CIUrls(['http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg','http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg'])))
//单个或多个图片File
print (client.porn_detect(CIFiles(['./test.jpg',])))
```
#### 图片标签
```
//单个图片url
print (client.tag_detect(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
//单个图片file
print (client.tag_detect(CIFile('./hot2.jpg')))
```

#### OCR - 身份证识别

```
//单个或多个图片Url,识别身份证正面
print (client.idcard_detect(CIUrls(['http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg']), 0))
//单个或多个图片file,识别身份证正面
print (client.idcard_detect(CIFiles(['./id4zheng.jpg','./id1zheng.jpg']), 0))
//单个或多个图片Url,识别身份证反面
print (client.idcard_detect(CIUrls(['http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg', 'http://www.4009951551.com/upload/image/20151026/1445831136187479.png']), 1))
//单个或多个图片file,识别身份证反面
print (client.idcard_detect(CIFiles(['./id5_fan.jpg']), 1))
```
#### OCR - 名片识别
```
//单个或多个图片Url
print (client.namecard_detect(CIUrls(['http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg', 'http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg'])))
//单个或多个图片file
print (client.namecard_detect(CIFiles(['./name1.jpg'])))
```
### 人脸识别
人脸识别包括：人脸检测、五官定位、个体信息管理、人脸验证、人脸对比及人脸检索。
#### 人脸检测
```
//单个图片Url, mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_detect(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
//单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_detect(CIFile('./hot2.jpg')))
```
#### 五官定位
```
//单个图片Url,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_shape(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png'),1))
//单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_shape(CIFile('./hot2.jpg'),1))
```
#### 个体信息管理
```
//个体创建,创建一个Person，并将Person放置到group_ids指定的组当中，不存在的group_id会自动创建。
//创建一个Person, 使用图片url
print (client.face_newperson('person111', ['group2',], CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png'), 'xiaoxin'))
//创建一个Person, 使用图片file
print (client.face_newperson('person211', ['group2',], CIFile('./hot2.jpg')))
//增加人脸,将一组Face加入到一个Person中。注意，一个Face只能被加入到一个Person中。 
//将单个或者多个Face的url加入到一个Person中
print (client.face_addface('person111', CIUrls(['http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg','http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg'])))
//将单个或者多个Face的file加入到一个Person中
print (client.face_addface('person211', CIFiles(['./test.jpg',])))
//删除人脸,删除一个person下的face
print (client.face_delface('person111', ['person111',]))
//设置信息
print (client.face_setinfo('person111', 'hello'))
//获取信息
print (client.face_getinfo('person111'))
//获取组列表
print (client.face_getgroupids())
//获取人列表
print (client.face_getpersonids('group2'))
//获取人脸列表
print (client.face_getfaceids('person211'))
//获取人脸信息
print (client.face_getfaceinfo('1820307972625034938'))
//删除个人
print (client.face_delperson('person11'))
```
#### 人脸验证
给定一个 Face 和一个 Person ，返回是否是同一个人的判断以及置信度。
```
//人脸验证,单个图片Url
print (client.face_verify('person111', CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
//人脸验证,单个图片file
print (client.face_verify('person111', CIFile('./test.jpg')))
```
#### 人脸对比
```
//两个对比图片的文件url
print (client.face_compare(CIFile('./zhao1.jpg'), CIFile('./zhao2.jpg')))
//两个对比图片的文件file
print (client.face_compare(CIUrl('http://www.miexue.com/d/file/junshiyingshi/2016-12-05/60bce03aac7a57e4fc600ecee1591e1d.jpg'), CIUrl('http://img.mp.itc.cn/upload/20161118/ee6be67ec6fb4135b5d579ab05acd715_th.jpg')))
//一个是图片的文件url， 一个是对比图片的文件file
print (client.face_compare(CIFile('./zhao1.jpg'), CIUrl('http://www.miexue.com/d/file/junshiyingshi/2016-12-05/60bce03aac7a57e4fc600ecee1591e1d.jpg')))
```
#### 人脸检索
对于一个待识别的人脸图片，在一个 Group 中识别出最相似的 Top5 Person 作为其身份返回，返回的Top5中按照相似度从大到小排列。
```
//人脸检索,单个文件url
print (client.face_identify('group1', CIUrl('http://www.5djiaren.com/uploads/2016-07/22-141354_227.jpg')))
//人脸检索,单个文件file
print (client.face_identify('group2', CIFile('./test.jpg')))
```
### 人脸核身   

#### 身份证识别对比
```python
	#身份证url
	print (client.face_idcardcompare('420822198804266119', '李时杰', CIUrl('http://docs.ebdoor.com/Image/CompanyCertificate/1/16844.jpg')))
	#身份证文件file
	print (client.face_idcardcompare('420822198804266119', '李时杰', CIFile('./id4_zheng.jpg')))
```
#### 活体检测 - 获取唇语验证码
```python
	obj = client.face_livegetfour()
	print (obj)
	#验证码
	validate_data = obj['data']['validate_data']
```
#### 活体检测 - 视频身份信息核验

```python	
	print (client.face_livedetectfour(validate_data, CIFile('../dn.qlv'), False, CIFile('../wxb.jpg')))
```
#### 活体检测 - 视频与用户照片的比对	

```python	
	print (client.face_idcardlivedetectfour(validate_data, CIFile('../dnn.qlv'), '330782198802084329', '李时杰'))
```

