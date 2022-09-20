## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

[数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 WebP 压缩功能，可将图片转换为 webp 压缩图片格式，其在压缩方面相比 jpg 格式更优越。在相同图片质量的情况下，webp 格式图片要比 jpg 格式图片减小25%以上，可以适配多终端使用场景。

## 限制说明

- 支持格式：支持将 jpg、png、bmp、gif、tpg、heif、avif 等格式图片转换为 webp 格式。
- 体积限制：处理图片原图大小不超过32MB、宽高不超过30000像素且总像素不超过2.5亿像素，处理结果图宽高设置不超过9999像素；针对动图，原图宽 x 高 x 帧数不超过2.5亿像素。
- 动图帧数限制：gif 帧数限300帧。

## 使用方式

数据万象通过 imageMogr2 接口提供 WebP 压缩功能。

该功能支持以下的处理方式：

- 下载时处理
- 上传时处理
- 云上数据处理

>? 
>- WebP 压缩为付费服务，费用同基础图片处理，具体费用请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。
>- 图片转换为 WebP 格式后，部分浏览器无法读取 WebP 图片的 exif 信息，导致没有旋转。您可参见 [旋转](https://cloud.tencent.com/document/product/460/36542) 文档，增加 auto-orient 参数，对原图旋转后再进行压缩。
>- WebP 压缩默认继承原始图片的质量参数。您可参见 [质量变换](https://cloud.tencent.com/document/product/460/36544) 文档，通过修改图片质量来调节压缩率。
>


## 接口示例

#### 1. 下载时处理

```plaintext
GET /<ObjectKey>?imageMogr2/format/webp HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

#### 2. 上传时处理

```http
PUT /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Pic-Operations: 
{
"is_pic_info": 1,
"rules": [{
    "fileid": "exampleobject",
    "rule": "imageMogr2/format/webp"
}]
}
```

>? Pic-Operations 为 json 格式的字符串，具体参数信息可参考 [图片持久化处理](https://cloud.tencent.com/document/product/460/18147)。
>

#### 3. 云上数据处理

```http
POST /<ObjectKey>?image_process HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-length: Size
Authorization: Auth String
Pic-Operations: 
{
"is_pic_info": 1,
"rules": [{
    "fileid": "exampleobject",
    "rule": "imageMogr2/format/webp"
}]
}
```

>? 
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 

## 处理参数说明

| 参数             | 含义                                                         |
| :--------------- | :----------------------------------------------------------- |
| ObjectKey  | 对象文件名，例如 folder/sample.jpg。                           | 
| /format/&lt;Format> | 压缩格式，此处为 webp。                                       |

## 实际案例

>? 本篇文档中的实际案例仅包含**下载时处理**，该类处理不会保存处理后的图片至存储桶。如有保存需求，请使用**上传时处理**或**云上数据处理**方式。
>

假设原图格式为 png，图片大小为1335.2KB，如下图所示：
![img](https://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png)

将原图转换为 webp 格式，请求 URL 如下：

```plaintext
http://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageMogr2/format/webp
```

效果如下：
![img](https://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageMogr2/format/webp)

**压缩率对比**

| 格式        | 图片大小             |
| :---------- | :------------------- |
| png（原图） | 1335.2KB             |
| webp        | 65KB（压缩率95.13%） |
