## 功能概述

TPG 压缩是腾讯云数据万象提供的高级图片压缩功能。通过该功能，您可将 JPG/PNG/GIF/WEBP 等图片格式转码为 TPG 格式，大幅减小图片大小，从而显著降低图片流量，提升页面加载速度。

>!
>- TPG 压缩为付费服务，具体费用可参见 [计费与定价](https://cloud.tencent.com/doc/product/460/6970)。
>- 如需使用该功能，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们，我们将为您开通服务。

## 接口形式

```plaintext
download_url?imageMogr2/format/<Format>
```

## 参数说明

| 参数                | 含义                                                         |
| ------------------- | ------------------------------------------------------------ |
| download_url        | 文件的访问链接，具体构成为`<BucketName-APPID>.cos.<picture region>.<domain>.com/<picture name>`<br>例如`examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg` |
| /format/&lt;Format> | 压缩格式。目标缩略图的图片格式为 tpg                       |

## 示例

假设原图格式为 JPG，图片大小为160KB，如下图所示。
![](https://main.qcloudimg.com/raw/8539c13ce879348e19f51704b753af60.jpg)

然后将原图转换为 TPG 格式，URL 地址如下。

```http
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?imageMogr2/format/tpg
```

转换为 TPG 格式后，图片大小为97KB，减少39%。

