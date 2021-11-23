## 操作场景

腾讯云全站加速网络（Enterprise Content Delivery Network，ECDN）将静态边缘缓存与动态回源路径优化相融合，通过腾讯在全球部署的节点优势，基于 QQ 平台上累计超过十年的技术实践，提供高可靠、低延时一站式加速服务体验。
将 API 网关与 ECDN 结合可为您解决使用 API 过程中遇到的因跨运营商、跨国、网络不稳定等因素导致的响应慢、丢包、服务不稳定等问题。

## 相关产品

- [API网关](https://console.cloud.tencent.com/apigateway/service)

- [全站加速网络ECDN](https://console.cloud.tencent.com/ecdn)

​                 ![img](https://docimg6.docs.qq.com/image/2Pa29wd0I7SRr0lSPQKGDg?w=2474&h=462)        

## 操作步骤

1. 创建 API 网关服务，生成默认访问地址。

   ![](https://qcloudimg.tencent-cloud.cn/raw/4f1b94be40b7a0d4894e0b7f34b36ebd.png)        

2. 在 ECDN 控制台接入自定义域名。

   ![](https://qcloudimg.tencent-cloud.cn/raw/4a8f77466e6be6d38f62c5efd80c4615.png)        

- 加速域名填写需要接入的自定义域名
- 源站类型选择“源站域名”
- 回源策略选择“择优回源”
- 回源地址填写第一步生成的API网关默认域名，不带协议和端口号
- 回源协议、加速区域根据自己的需求选择

点击【保存】按钮完成配置，需要等待一段时间，在CDN控制台上会生成一个CNAME域名。

![](https://qcloudimg.tencent-cloud.cn/raw/bcfe7a1c9b0e5317aa84bfdc8cba622e.png)

​                         



3. 修改源站 Host。

![](https://qcloudimg.tencent-cloud.cn/raw/085b738d32e6b5b9db4d1aabd0b0aebb.png)                         

在 ECDN 控制台域名列表里，选择刚刚配置好的域名，点击进入详情页。

修改回源配置中的源站Host为第一步中生成的默认公网域名。

4. 配置 cname。

为本次接入的域名配置 CNAME 到 ECDN 生成的 CNAME 域名。

![](https://qcloudimg.tencent-cloud.cn/raw/dd319421876fa6f71895808fe41bdba9.png)                   

5. 发起调用，可以看到已经连通。

