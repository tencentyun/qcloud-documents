### COS 如何开通 CDN？

详情请参见 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636) 和 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

### COS 是否支持 CDN HTTPS 回源 COS？

支持。具体操作方法请参见 [设置回源](https://cloud.tencent.com/document/product/436/13310) 文档。

### COS 和 CDN 有什么区别？

COS 和 CDN 是两个不同的产品。

 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/document/product/436/6222) 是腾讯云提供的一种存储海量文件的分布式存储服务，可进行多格式文件的上传、下载和管理，实现海量数据存储和管理。
[内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/document/product/228) 是由遍布全球的高性能加速节点构成。这些高性能的服务节点都会按照一定的缓存策略存储您的业务内容，当您的用户向您的某一业务内容发起请求时，请求会被调度至最接近用户的服务节点，直接由服务节点快速响应，有效降低用户访问延迟，提升可用性。

使用 COS 服务可以不开启 CDN 功能，COS 中的 CDN 适用于以下场景：
- 对响应延时和下载速度有较高要求的场景。
- 需跨地区、国家、大洲传输数 GB 至数 TB 数据的场景。
- 需高密集地反复下载相同内容的场景。

更多介绍请参见 [CDN 加速概述](https://cloud.tencent.com/document/product/436/18669)。

### 前端业务能否通过 CDN 和临时密钥的方式来访问 COS 的内容？

不支持 CDN 和临时密钥的方式访问 COS。如果您希望在 COS 私有读写的情况下实现 CDN 访问，请参见 [CDN 回源鉴权](https://cloud.tencent.com/document/product/436/18670#.E9.85.8D.E7.BD.AE.E9.89.B4.E6.9D.832)。

### 私有读存储桶能否通过 CDN 加速访问？

可以，但是需要进行授权相关配置。具体配置请参见 CDN 加速概述文档的 [私有读存储桶](https://cloud.tencent.com/document/product/436/18669#.E7.A7.81.E6.9C.89.E8.AF.BB.E5.AD.98.E5.82.A8.E6.A1.B6) 部分。


### COS 文件更新（重新上传或删除）时，CDN 仍然保存缓存内容，造成与源站不一致。能否在 COS 更新时自动刷新 CDN 的缓存？

COS 本身不支持自动刷新 CDN 缓存，但可以借助云函数 SCF 来设置自动刷新 CDN 缓存，详情请参见 [设置 CDN 缓存刷新](https://cloud.tencent.com/document/product/436/45597) 文档。

### COS 可以使用 CDN 加速域名上传文件吗？

如果使用 CDN 的加速域名作为自定义域名，在文件上传场景使用的话，这种场景不建议使用，因为本身 CDN 不是做加速上传使用的。推荐使用 COS 的全球加速功能，可以实现数据上传加速和下载加速，请参见 [全球加速概述](https://cloud.tencent.com/document/product/436/38866)。

### COS 自带 CDN 功能吗？

COS 本身不带有 CDN 功能，需要用户自行配置，详情请参见 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636) 和 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

