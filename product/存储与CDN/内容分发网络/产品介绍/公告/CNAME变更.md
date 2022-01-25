## 背景

腾讯云内容分发网络（CDN）预计于2022年1月25日进行技术升级，调整 CNAME，涉及以下变更：

- 中国境内/全球加速域名，在已生效 `.com` 结尾的 CNAME 基础上新增 `.cn` 结尾的 CNAME。
如：原来为 `example.com.dsa.dnsv1.com`  -->  更改为 `example.com.dsa.dnsv1.com.cn`。
- 加速区域从中国境内/全球切换到中国境外时，CNAME 会从 `.cn` 后缀切换成 `.com` 后缀。
如：原来为 `example.com.dsa.dnsv1.com.cn`  -->  自动切换为 `example.com.dsa.dnsv1.com`。

## 注意事项

技术升级后，若您的域名有两条不同的 CNAME，请关注确认新增的 CNAME，并配置新的 CNAME 解析。

1. 新增 CNAME
   CNAME 变更发布后，对于中国境内/全球域名，会出现两条 CNAME 解析。**原来已生效 CNAME 解析可正常使用，但仍建议您尽快配置新的 CNAME 解析**，即 `.com.cn` 后缀的 CNAME。配置成功后，CDN 将不再展示原来的 CNAME。
![](https://qcloudimg.tencent-cloud.cn/raw/062465982361ae2d543edffc207a1199.jpg)
>? 域名若添加腾讯云dnspod解析，支持[一键解析](https://cloud.tencent.com/document/product/228/59152)。
2. 加速区域变更
   中国境内/全球域名的 CNAME 将统一采用最新的后缀：`cdn.dnsv1.com.cn`；中国境外域名的 CNAME 将统一采用后缀：`.cdn.dnsv1.com`。若您需要进行加速区域变更，相应 CNAME 后缀也会发生变更，请注意确认和修改您的 CNAME 解析。
>? 切换前，旧的 CNAME 保持有效，不影响现网业务。建议您尽早切换为新的 CNAME，后期将为您集中切换为新的CNAME ，届时请您关注消息通知。

