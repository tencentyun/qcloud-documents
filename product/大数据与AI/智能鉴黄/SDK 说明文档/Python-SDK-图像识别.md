


## 开发准备
### SDK 获取

智能图像的 Python SDK 下载地址：[Python-SDK-V2.0](https://github.com/tencentyun/image-python-sdk-v2.0) 。

### 开发准备
**使用 pip**
Python 2：
pip install qcloud_image
Python 3：
pip3 install qcloud_image
## 快速入门
### 在腾讯云申请业务的授权

授权包括： APPID 、SecretId 、 SecretKey ，目前只支持主账号及密钥进行调用。
>!BUCKET 为历史遗留字段, 无需修改。

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
创建完对象后，您可以根据实际需求调用对应的操作方法。

图片识别包括：图片鉴黄、图像分析、OCR - 身份证识别及 OCR - 名片识别。
#### 图片鉴黄
```
//单个或多个图片 Url
print (client.porn_detect(CIUrls(['http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg','http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg'])))
//单个或多个图片 File
print (client.porn_detect(CIFiles(['./test.jpg',])))
```
#### 图像分析
```
//单个图片 Url
print (client.tag_detect(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
//单个图片 File
print (client.tag_detect(CIFile('./hot2.jpg')))
```

#### OCR - 身份证识别

```
//单个或多个图片 Url,识别身份证正面
print (client.idcard_detect(CIUrls(['http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg']), 0))
//单个或多个图片 File,识别身份证正面
print (client.idcard_detect(CIFiles(['./id4zheng.jpg','./id1zheng.jpg']), 0))
//单个或多个图片 Url,识别身份证反面
print (client.idcard_detect(CIUrls(['http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg', 'http://www.4009951551.com/upload/image/20151026/1445831136187479.png']), 1))
//单个或多个图片 File,识别身份证反面
print (client.idcard_detect(CIFiles(['./id5_fan.jpg']), 1))
```
#### OCR - 名片识别
```
//单个或多个图片 Url
print (client.namecard_detect(CIUrls(['http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg', 'http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg'])))
//单个或多个图片 File
print (client.namecard_detect(CIFiles(['./name1.jpg'])))
```


