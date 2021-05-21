
## 现象描述

如果您使用腾讯云 CDN 后，网页访问速度依然很慢。

## 可能原因

- 原因一：您接入域名的 CDN 加速服务未生效，可能原因是您没有在域名 DNS 服务商处配置 CNAME 记录。请执行 [检查域名解析](#step1)。
- 原因二：节点缓存过期时间配置错误。请执行 [检查节点缓存过期时间配置](#step2)。
- 原因三：首次访问资源，且之前未对该资源做过预热处理。请执行 [进行 URL 预热](#step3)。
- 原因四：网页架构模式本身存在缺陷请执行 [优化网页架构模式](#step4)。



## 解决思路

[](id:step1)
### 检查域名解析
以下是一个用 nslookup 命令查询 CDN 加速域名 DNS 解析示例：
```
nslookup 加速域名
```
![](https://main.qcloudimg.com/raw/25766483a81d51e0ba240d7e3bd5db81.png)
如果查询出的域名解析中没有如上图红框中所示，是后缀为 dnsv1.com 的 CNAME 解析记录，则说明您接入域名的 CDN 加速服务未生效，可能原因是您没有在域名 DNS 服务商处配置 CNAME 记录，可以根据 [配置 CNAME](https://cloud.tencent.com/document/product/228/3121) 文档前往您的域名 DNS 服务商处配置 CNAME 记录。

[](id:step2)
###  检查节点缓存过期时间配置

- 检查所访问的资源对应的节点缓存规则，是否存在配置的节点缓存过期时间为0、节点缓存过期时间过短或不缓存的情况。
  如果 CDN 节点没有缓存，访问请求会回源，起不到加速效果。建议用户根据需要配置节点的缓存时间，
- 检查您的源站是否设置了缓存头部 Cache-Control为 no-store/no-cache/private。
  如果源站设置了缓存头部 Cache-Control为 no-store/no-cache/private，此时需同时开启“强制缓存”， CDN 节点才会按照所配置的缓存时间缓存资源。
  若未开启“强制缓存”且源站的 Cache-Control 字段为 no-cache/no-store/private，则即使配置了缓存时间，CDN 节点也不会缓存资源。

更多配置规则请前往 [节点缓存过期时间配置](https://cloud.tencent.com/document/product/228/47672)。

[](id:step3)
### 进行 URL 预热

如果您是首次访问资源，且之前未对该资源做过预热处理，CDN 节点会回源拉取资源，首次访问速度慢属于正常。建议可以先在控制台进行 [URL 预热](https://cloud.tencent.com/document/product/228/40273)。


[](id:step4)
### 优化网页架构模式

网页动态资源较多，每次访问都会回源拉取最新资源，影响访问速度。若网页动态资源占比多，建议优化源站，将动态资源与静态资源分开，静态资源使用 CDN 分发加速。
