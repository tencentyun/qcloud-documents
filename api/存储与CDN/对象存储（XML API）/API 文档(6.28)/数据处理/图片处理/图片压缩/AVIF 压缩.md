## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

对象存储（Cloud Object Storage，COS）基于 [数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 AVIF 压缩功能，可将图片转换为 avif 格式，avif 是基于 av1 的一种全新图片格式，在2020年2月由 Netflix 首次公布于众，目前已支持 Chrome、Firefox 等浏览器。

## 限制说明

- 支持格式：支持将 jpg、png、bmp、gif、webp、tpg、heif 等格式图片转换为 avif 格式。
- 体积限制：处理图片原图大小不超过32MB、宽高不超过30000像素且总像素不超过2.5亿像素，处理结果图宽高设置不超过9999像素；针对动图，原图宽 x 高 x 帧数不超过2.5亿像素。
- 动图帧数限制：gif 帧数限300帧。


## 前提条件

- 目前 AVIF 压缩属于内测功能，仅支持北京、上海、广州地域的存储桶，使用前请先 [申请开通 AVIF 功能内测](https://cloud.tencent.com/apply/p/igpvms3gjcn)。
- 使用 AVIF 压缩，需要先开通存储桶的图片高级压缩功能，您需要在相应的存储桶配置页中通过开关按钮开启功能，详情请参见 [设置图片高级压缩](https://cloud.tencent.com/document/product/436/48981)。

## 使用方式

COS 通过数据万象 imageMogr2 接口提供 avif 压缩功能。

该功能支持以下的处理方式：

- 下载时处理
- 上传时处理
- 云上数据处理

>? AVIF 压缩为付费服务，计费项为图片高级压缩费用，由数据万象收取，具体费用请参见数据万象 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。
>

## 接口示例

#### 1. 下载时处理

```plaintext
download_url?imageMogr2/format/avif
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
    "rule": "imageMogr2/format/avif"
}]
}
```

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
    "rule": "imageMogr2/format/avif"
}]
}
```

>? 本篇文档中的实际案例仅包含**下载时处理**，该类处理不会保存处理后的图片至存储桶。如有保存需求，请使用**上传时处理**或**云上数据处理**方式。
>

## 处理参数说明

| 参数             | 含义                                                         |
| :--------------- | :----------------------------------------------------------- |
| download_url     | 文件的访问链接，具体构成为&lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com/&lt;picture name>， 例如`examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg`。 |
| /format/&lt;Format> | 压缩格式，此处为 avif。                                       |

## 实际案例

假设原图格式为 png，图片大小为1335.2KB，如下图所示：
![img](https://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png)

将原图转换为 avif 格式，请求 URL 如下：

```plaintext
http://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageMogr2/format/avif
```

**压缩率对比**

| 格式        | 图片大小              |
| :---------- | :-------------------- |
| png（原图） | 1335.2KB              |
| avif        | 62.8KB（压缩率95.3%） |

