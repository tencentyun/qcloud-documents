## 操作场景
腾讯云 Web 应用防火墙（Web Application Firewall，WAF）是一款基于 AI 的一站式 Web 业务运营风险防护方案。
本任务将介绍如何配置 WAF，对 API 网关上的 API 提供安全防护。

## 前提条件

- 已开通 [Web 应用防火墙](https://cloud.tencent.com/product/waf)
- 已在 API 网关上发布了 API

## 操作步骤

### 步骤1：在 API 网关控制台绑定自定义域名

参考 [配置自定义域名](https://cloud.tencent.com/document/product/628/11791) 文档，在 API 网关控制台绑定自定义域名。
<img src="https://main.qcloudimg.com/raw/d9602adbae069b353545476d4c7ee146.png">

>!API 网关绑定自定义域名时，会校验自定义域名是否 CNAME 到服务的子域名。因此，您必须先将自定义域名 CNAME 到 API 网关服务的子域名并配置绑定成功后，再修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。

### 步骤2：配置 WAF

1. 登录 [WAF 控制台](https://console.cloud.tencent.com/guanjia/waf/config)。
2. 在左侧导航栏中单击【WEB应用防火墙】>【防护设置】，进入防护设置页面。
3. 单击域名列表上方的【添加域名】，进入添加域名页面。
4. 填写添加域名表单。源站地址选择【域名】，填写 API 网关服务的子域名。
<img src="https://main.qcloudimg.com/raw/820dfd300d05f8fa8da30c6290c5a1b3.png">
5. 单击【保存】，完成配置，此时域名接入状态为“未配置 CNAME 记录”。
<img src="https://main.qcloudimg.com/raw/46bf4804349321a264c8b0715c92a4b5.png">


### 步骤3：修改 CNAME 记录

1. 修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。
2. 登录 WAF 控制台，在左侧导航栏中点击【WEB应用防火墙 - 防护设置】，进入防护设置页面。
3. 单击域名列表中接入状态后面的刷新按钮，可以看到接入状态变为【正常防护】，至此接入配置完成。
