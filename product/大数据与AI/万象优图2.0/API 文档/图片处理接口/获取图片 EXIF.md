## 功能概述
EXIF（Exchangeable Image File）全称为可交换图像文件，可记录数码照片的拍摄参数、缩略图及其他属性信息。腾讯云数据万象通过 **exif** 接口获取 EXIF 信息。处理图片原图大小不超过20MB、宽高不超过30000像素且总像素不超过1亿像素，处理结果图宽高设置不超过9999像素；针对动图，原图宽 x 高 x 帧数不超过1亿像素。


>!如图片无 exif 信息，将返回`{"error" : "no exif data"}`。

## 接口形式

```
download_url?exif
```

## 参数说明

**操作名称**：exif。

| 参数         | 含义                                                         |
| ------------ | ------------------------------------------------------------ |
| download_url | 文件的访问链接，具体构成为`<BucketName-APPID>.cos.<picture region>.<domain>.com/<picture name>`，<br>例如`examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg`。 |


## 示例
```
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?exif
```

