## 背景

腾讯云内容分发网络（CDN）预计于2022年1月25日进行技术升级，新增 CNAME 域名，不影响现网业务。变更详情如下：
- 中国境内/全球加速域名，在已生效 `.com` 结尾的 CNAME 基础上会新增一条 `.cn` 结尾的 CNAME。
如：原来为 `example.com.dsa.dnsv1.com` -->  新增 `example.com.dsa.dnsv1.com.cn`。
- 新添加的加速域名从中国境内/全球切换到中国境外时，会在 `.cn` 结尾的 CNAME 基础上新增一条 `.com` 后缀的 CNAME 。
如：原来为 `example.com.dsa.dnsv1.com.cn`  -->  新增 `example.com.dsa.dnsv1.com`。

>? 新增的 CNAME 域名与原 CNAME 域名解析一致，对业务无影响，并都会长期提供服务。您当前无需调整解析配置。

## 注意事项

技术升级后，CDN 域名体验将会有如下变更：

1. 现有加速域名的 CNAME
CNAME 变更发布后，对于中国境内/全球域名，会出现两条 CNAME 解析。**原来已生效 CNAME 解析仍正常提供服务**。新增的 `.com.cn` CNAME 域名与原 CNAME 域名解析一致，并都会长期保持服务，您未来可以在业务合适的时间自主调整解析配置。若域名解析配置更新为 `.com.cn` 后缀的 CNAME，在配置成功后，CDN 将不再展示原来的 CNAME（但原后缀的 CNAME 仍在后台保留并可正常解析）。
![](https://qcloudimg.tencent-cloud.cn/raw/55251a59a965b2f45f090f52e6be1a1b.jpg)
2. 新增加速域名的 CNAME
加速区域为中国境内/全球域名的新增加速域名的 CNAME 将统一采用新的后缀：`cdn.dnsv1.com.cn`；中国境外域名的 CNAME 将统一采用后缀：`.cdn.dnsv1.com`。若您需要进行加速区域变更，域名列表下的 CNAME 后缀也会发生变更。但 `.com` 和 `.com.cn` 后缀的两条 CNAME 域名仍都在后台保留并可正常解析，并长期保持服务。您可以根据加速区域选择合适的 CNAME 解析。

