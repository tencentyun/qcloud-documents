
本文档将介绍如何配置 Web 应用防火墙（WAF），使其对 API 网关上的 API 提供安全防护。

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

1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航中，选择选择【实例管理】>【实例列表】，进入实例列表页面。
2. 在实例列表页面，选择需要添加域名的实例，在右侧单击所属实例的【域名接入】。
![](https://main.qcloudimg.com/raw/26e509138e71dd1d3e1d6a6a88fb5a09.png)
3. 在域名接入页面 ，单击【添加域名】，进入添加域名页面。
4. 在“域名配置”页面，根据实际情况填写相关字段，其中源站地址选择【域名】，并填写 API 网关服务的子域名，单击【保存】。
![](https://main.qcloudimg.com/raw/8c83fbec08742ede0ddb19f762eaf90b.png)
5. 完成配置后，此时域名接入状态为“未配置 CNAME 记录”。
<img src="https://main.qcloudimg.com/raw/46bf4804349321a264c8b0715c92a4b5.png">


### 步骤3：修改 CNAME 记录

1. 在 DNS 提供商中修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。
2. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/config)，选择 【实例管理】>【域名接入】，进入域名接入页面。
3. 在实例列表页面，选择需要添加域名的实例，在右侧单击所属实例的【域名接入】。
![](https://main.qcloudimg.com/raw/26e509138e71dd1d3e1d6a6a88fb5a09.png)
4. 在域名列表中，单击接入状态后面的刷新按钮，可以看到接入状态变为“正常防护”，至此接入配置完成。
![](https://main.qcloudimg.com/raw/e26f4a5c7f9e21f6b2d57be2e6867480.png)
