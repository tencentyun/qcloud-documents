## 功能概述

图片处理服务由腾讯云 [数据万象](https://cloud.tencent.com/document/product/460) 提供。TPG 压缩是腾讯云数据万象提供的高级图片压缩功能。通过该功能，您可将 JPG、PNG、GIF、WEBP 等格式图片转码为 TPG 格式，大幅减小图片大小，从而显著降低图片流量，提升页面加载速度。

>!
- TPG 压缩为付费服务，具体费用可查看 [计费项](https://cloud.tencent.com/document/product/1246/45274)。
- 使用 TPG 压缩时，需在相应存储桶配置页中开通服务，具体操作请参见 [开启 TPG 压缩](https://cloud.tencent.com/document/product/1246/45278)。
- TPG 是腾讯自研的图片格式，如需使用，请确认图片加载环境支持 TPG 解码，腾讯云音视频实验室提供集成 TPG 解码器的 iOS、Android、Windows 终端 SDK，可帮助您快速接入和使用 TPG，详见 [SDK 下载](https://cloud.tencent.com/document/product/875/18366)。


## 接口形式

```plaintext
download_url?imageMogr2/format/<Format>
```

## 参数说明

| 参数                 | 含义                                                         |
| -------------------- | ------------------------------------------------------------ |
| download_url | 文件的访问链接，具体构成为`<BucketName-APPID>.cos.<picture region>.<domain>.com/<picture name>`，<br>例如`examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg`。 |
| /format/&lt;Format>  | 压缩格式，目标缩略图的图片格式为 tpg。 |


## 示例

假设原图格式为 JPG，图片大小为160KB，如下图所示。
![](https://main.qcloudimg.com/raw/8539c13ce879348e19f51704b753af60.jpg)

然后将原图转换为 TPG 格式，URL 地址如下。

```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?imageMogr2/format/tpg
```

转换为 TPG 格式后，图片大小为97KB，减少39%。
