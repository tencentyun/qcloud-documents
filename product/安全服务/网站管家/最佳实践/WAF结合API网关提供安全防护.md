
本文档将介绍如何配置 Web 应用防火墙（WAF），为 API 网关上的 API 提供安全防护。

## 前提条件

- 已开通 [Web 应用防火墙](https://buy.cloud.tencent.com/buy/waf)。
- 已在 API 网关上发布了 API，详情请参见 [快速入门](https://cloud.tencent.com/document/product/628/41654)。

## 操作步骤

### 步骤1：在 API 网关控制台绑定自定义域名
参考 [配置自定义域名](https://cloud.tencent.com/document/product/628/11791) 文档，在 API 网关控制台绑定自定义域名。
>!API 网关绑定自定义域名时，会校验自定义域名是否解析（通过 CNAME）到该服务的子域名。因此，您必须先将自定义域名解析（通过 CNAME）到 API 网关服务的子域名并配置绑定成功，再修改 DNS 记录，将自定义域名指向 WAF 的 CNAME 域名。
>
<img src="https://main.qcloudimg.com/raw/d9602adbae069b353545476d4c7ee146.png">



### 步骤2：配置 WAF
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，在左侧导航中，选择**接入管理**。
2. 在域名接入页面，单击**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/12126e9b3bad0a7ea4af4fc6b59c8ea8.png)
3. 在添加域名页面，配置相关参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/199a82d8ee104da13e017b8be8d75e64.png)
5. 完成配置后，此时域名接入状态为“未配置 CNAME 记录”。
![](https://qcloudimg.tencent-cloud.cn/raw/ec2c0b54b458d2c4dca57f66f45d9737.png)


### 步骤3：修改 CNAME 记录
1. 在 DNS 提供商中修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。
2. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，选择**接入管理**，进入域名接入页面，即可看到正常防护的界面。
![](https://qcloudimg.tencent-cloud.cn/raw/81517b46e9a9591e808f5cb67fefb90b.png)
