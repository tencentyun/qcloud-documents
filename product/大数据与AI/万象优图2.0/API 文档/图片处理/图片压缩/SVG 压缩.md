## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

[数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 SVG 压缩功能，可以在不影响显示效果的情况下，通过一定的优化算法删除 SVG 文件中的冗余信息，最终达到减少 SVG 文件体积的目的。

## 限制说明

- 支持格式：仅支持将 svg 格式图片作为输入。
- 体积限制：处理图片原图大小不超过32MB。

## 使用方式

数据万象通过 imageMogr2 接口提供 SVG 压缩功能。

该功能支持以下的处理方式：

- 下载时处理
- 上传时处理
- 云上数据处理

>?  SVG 压缩为付费服务，计费项为图片高级压缩费用，具体费用请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。
>


## 接口示例

#### 1. 下载时处理

```plaintext
GET /<ObjectKey>?imageMogr2/format/svgc HTTP/1.1
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
    "rule": "imageMogr2/format/svgc"
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
    "rule": "imageMogr2/format/svgc"
}]
}
```

>? 
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
>

## 处理参数说明

| 参数                | 含义                                                         |
| :------------------ | :----------------------------------------------------------- |
| ObjectKey  | 对象文件名，例如 folder/sample.jpg。                           | 
| /format/&lt;Format> | 压缩格式，此处为svgc。                                       |
