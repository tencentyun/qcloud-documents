## 操作场景

腾讯云全站加速网络（Enterprise Content Delivery Network，ECDN）将静态边缘缓存与动态回源路径优化相融合，通过腾讯在全球部署的节点优势，基于 QQ 平台上累计超过十年的技术实践，提供高可靠、低延时一站式加速服务体验。
将 API 网关与 ECDN 结合可为您解决使用 API 过程中遇到的因跨运营商、跨国、网络不稳定等因素导致的响应慢、丢包、服务不稳定等问题。

## 相关产品

- [API 网关](https://console.cloud.tencent.com/apigateway/service)
- [全站加速网络 ECDN](https://console.cloud.tencent.com/cdn/domains)

<img src="https://qcloudimg.tencent-cloud.cn/raw/faf36b8f087259248b5746efeb69ca2b.png" width="450px">   

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) 创建 API 网关服务，生成默认访问地址。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/0a1caac37827585f33f4d78ccb6b1494.png" width=700> 
2. 在 [CDN控制台](https://console.cloud.tencent.com/cdn/domains) 接入自定义域名，在菜单中选择**域名管理**，点击**添加域名**。
<ul>
<li>加速域名，填写需要接入的自定义域名</li>
<li>加速类型，选择 ECDN动态加速</li>
<li>源站类型，选择“自有源”</li>
<li>回源协议，加速区域根据自己的需求选择</li>
<li>源站地址，填写第一步生成的 API 网关默认域名</li>
<li>回源HOST，在源站访问的站点域名</li>
</ul>
单击保存完成配置，需要等待一段时间，在 CDN 控制台上会生成一个 CNAME 域名。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/40eb9c3bc70e829a5e27480e74b404a8.png" width=700> 

3. 修改源站 Host。
在 CDN 控制台域名列表里，选择刚刚配置好的域名，单击进入详情页。
修改回源配置中的源站 Host 为第一步中生成的默认公网域名。

 <img src = "https://qcloudimg.tencent-cloud.cn/raw/06e3944504dee4a777cc706ccddc4687.png" width=700> 
4. 配置 cname。
为本次接入的自定义域名配置 CNAME 到 CDN 生成的 CNAME 域名。详细方式参考指引 [配置CNAME](https://cloud.tencent.com/document/product/228/3121) 。
5. 发起调用，可以看到已经连通。
