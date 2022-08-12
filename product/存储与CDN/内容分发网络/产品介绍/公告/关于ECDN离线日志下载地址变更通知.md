## 调整说明

为符合国家相关法律法规要求，ECDN 将对离线日志的生成及投递规则进行调整，将区分中国境内、中国境外生成不同的离线日志包，若用户在全球范围内均有加速服务，为了能下载到完整的日志内容，需分别使用境内、境外地址下载对应的离线日志包。


## 调整时间

2022年7月4日正式上线。

## 影响范围
本次调整主要影响正在使用 ECDN 离线日志下载接口的用户。

>!当前 ECDN 与 CDN 产品已融合控制台，请统一使用 [DescribeCdnDomainLogs](https://cloud.tencent.com/document/product/228/39232) 接口查询及下载离线日志，如果您仍然在使用 ECDN 旧的离线日志下载接口 [DescribeEcdnDomainLogs](https://cloud.tencent.com/document/product/570/42464)，请注意将接口地址切换至 [DescribeCdnDomainLogs](https://cloud.tencent.com/document/product/228/39232)。

1. 本次调整过后，如果使用 API 接口 [DescribeCdnDomainLogs](https://cloud.tencent.com/document/product/228/39232) 查询离线ECDN域名的离线下载日志，如果您的加速范围为全球加速，将区分中国境内、中国境外生成不同的离线日志包，接口将返回中国境内、中国境外响应的离线日志包下载链接；
2. 如果您使用控制台手动下载 ECDN 离线日志，本次调整后，如果您的加速范围为全球加速，将区分中国境内、中国境外区域查询到两条不同的离线日志记录，您可以分别下载对应的离线日志。
3. 如果您在本次调整后，发现有日志丢失，可以在30天内重新调用接口请求对应的离线日志进行补全，超过30天未补全，可能造成日志永久丢失。

