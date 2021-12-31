## 操作场景

腾讯云全站加速网络（Enterprise Content Delivery Network，ECDN）将静态边缘缓存与动态回源路径优化相融合，通过腾讯在全球部署的节点优势，基于 QQ 平台上累计超过十年的技术实践，提供高可靠、低延时一站式加速服务体验。

将 API 网关与 ECDN 结合可为您解决使用 API 过程中遇到的因跨运营商、跨国、网络不稳定等因素导致的响应慢、丢包、服务不稳定等问题。

## 相关产品

- [API 网关](https://console.cloud.tencent.com/apigateway/service)
- [全站加速网络 ECDN](https://console.cloud.tencent.com/ecdn)

<img src="https://qcloudimg.tencent-cloud.cn/raw/faf36b8f087259248b5746efeb69ca2b.png" width="450px">   

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) 创建 API 网关服务，生成默认访问地址。
![](https://qcloudimg.tencent-cloud.cn/raw/a57d11d46cb8dff3426616e702def406.png)
2. 在 ECDN 控制台接入自定义域名。
<img src="https://qcloudimg.tencent-cloud.cn/raw/91371935d7c1b73598c49229214e96f5.png" width="500px">

	- 加速域名填写需要接入的自定义域名
	- 源站类型选择“源站域名”
	- 回源策略选择“择优回源”
	- 回源地址填写第一步生成的 API 网关默认域名，不带协议和端口号
	- 回源协议、加速区域根据自己的需求选择
	
单击**保存**完成配置，需要等待一段时间，在 CDN 控制台上会生成一个 CNAME 域名。
![](https://qcloudimg.tencent-cloud.cn/raw/bcfe7a1c9b0e5317aa84bfdc8cba622e.png)
                
3. 修改源站 Host。
![](https://qcloudimg.tencent-cloud.cn/raw/085b738d32e6b5b9db4d1aabd0b0aebb.png)                         
在 ECDN 控制台域名列表里，选择刚刚配置好的域名，点击进入详情页。
修改回源配置中的源站 Host 为第一步中生成的默认公网域名。

4. 配置 cname。
为本次接入的域名配置 CNAME 到 ECDN 生成的 CNAME 域名。
![](https://qcloudimg.tencent-cloud.cn/raw/4ce80b56098ea1d99503078675f4c86a.png)

5. 发起调用，可以看到已经连通。

