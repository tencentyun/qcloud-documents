## 功能描述
EXIF（Exchangeable Image File）全称为可交换图像文件，可记录数码照片的拍摄参数、缩略图及其他属性信息。对象存储通过数据万象的 **exif** 接口获取 EXIF 信息。处理图片原图大小不超过32MB、宽高不超过30000像素且总像素不超过1亿像素，处理结果图宽高设置不超过9999像素；针对动图，原图宽 x 高 x 帧数不超过1亿像素。

>!
> - 图片处理功能为收费项，由数据万象收取，详细的计费说明请参见数据万象 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。
> - 如图片无 exif 信息，将返回`{"error" : "no exif data"}`。
> 

## 接口示例

```plaintext
download_url?exif
```

## 参数说明

**操作名称**：exif

| 参数         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| download_url | 文件的访问链接，具体构成为&lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com/&lt;picture name>，<br>例如 `examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg` |


## 实际案例
#### 请求1：公有读
```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?exif
```

#### 请求2：私有读、携带签名

获取方式同上，仅增加签名部分，并与获取参数以“&”连接，示例如下：

```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=<signature>&exif
```

 >? `<signature>` 为签名部分，获取方式请参考 [请求签名](https://cloud.tencent.com/document/product/436/7778)。
 >
