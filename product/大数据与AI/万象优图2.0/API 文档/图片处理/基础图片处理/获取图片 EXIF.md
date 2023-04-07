## 功能概述
EXIF（Exchangeable Image File）全称为可交换图像文件，可记录数码照片的拍摄参数、缩略图及其他属性信息。腾讯云数据万象通过 **exif** 接口获取 EXIF 信息。


## 限制说明

- 支持格式：支持处理 JPG、BMP、GIF、PNG、WebP 格式，并且支持 HEIF 格式的解码和处理操作。
- 静图体积限制：处理图片原图大小不超过32MB、宽高不超过50000像素且总像素不超过2.5亿像素，处理结果图宽高设置不超过50000像素。
- WebP图片限制：处理图片原图大小不超过32MB、宽高不超过16383像素且总像素不超过2.5亿像素，处理结果图宽高设置不超过16383像素。
- 动图体积限制：原图及处理图宽 x 高 x 帧数不超过2.5亿像素。
- 动图帧数限制：gif 帧数限300帧。



>! 如图片无 exif 信息，将返回`{"error" : "no exif data"}`。
>

## 接口示例

```plaintext
GET /<ObjectKey>?exif HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

## 处理参数说明

**操作名称**：exif。

| 参数         | 含义                                                         |
| ------------ | ------------------------------------------------------------ |
| ObjectKey  | 对象文件名，例如 folder/sample.jpg。                           | 


## 实际案例

#### 案例一：公有读
```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?exif
```

#### 案例二：私有读、携带签名

获取方式同上，仅增加签名部分，并与获取参数以“&”连接，示例如下：

```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=<signature>&exif
```

>? `<signature>` 为签名部分，获取方式请参考 [请求签名](https://cloud.tencent.com/document/product/436/7778)。
>


## 注意事项

为了避免未授权人员通过访问不携带处理参数的链接实现访问和下载原图的情况，您可同时将处理参数签入到请求签名中，处理参数整体是参数的 key，value 为空，如下是简单的示例（仅做样式参考，可能已经过期无法直接访问），详细计算方法请参见 [请求签名](https://cloud.tencent.com/document/product/436/14114)。


```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=sha1&q-ak=AKID********************&q-sign-time=1593342360;1593342720&q-key-time=1593342360;1593342720&q-header-list=&q-url-param-list=watermark%252f1%252fimage%252fahr0cdovl2v4yw1wbgvzlteyntewmdawmdqucgljc2gubxlxy2xvdwquy29tl3nodwl5aw4uanbn%252fgravity%252fsoutheast&q-signature=26a429871963375c88081ef60247c5746e834a98&watermark/1/image/aHR0cDovL2V4YW1wbGVzLTEyNTEwMDAwMDQucGljc2gubXlxY2xvdWQuY29tL3NodWl5aW4uanBn/gravity/southeast
```
