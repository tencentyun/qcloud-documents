## 操作场景
腾讯云 Web 应用防火墙（Web Application Firewall，WAF）是一款应对Web 攻击、入侵、漏洞利用、挂马、篡改、后门、爬虫等网站及 Web 业务安全防护的方案。
本任务将介绍如何配置 WAF，对 API 网关上的 API 提供安全防护。

## 前提条件

- 已开通 [Web 应用防火墙](https://console.cloud.tencent.com/guanjia/tea-welcome)
- 已在 API 网关上发布了 API

## 操作步骤

### 步骤1：在 API 网关控制台绑定自定义域名

参考 [配置自定义域名](https://cloud.tencent.com/document/product/628/11791) 文档，在 API 网关控制台绑定自定义域名。
<img src="https://qcloudimg.tencent-cloud.cn/raw/898113b638d556124893d00d6604dbee.png" width=700>

>!API 网关绑定自定义域名时，会校验自定义域名是否 CNAME 到服务的子域名。因此，您必须先将自定义域名 CNAME 到 API 网关服务的子域名并配置绑定成功后，再修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。

### 步骤2：配置 WAF

1. 登录 [WAF 控制台](https://console.cloud.tencent.com/guanjia/tea-welcome)。
2. 在左侧导航栏中单击 **Web 应用防火墙** ,选择 **资产中心 > 接入管理**。
3. 单击域名列表上方的**添加域名**，进入添加域名页面。
4. 填写添加域名表单。
 -    域名，填写需要防护的域名，也即自定义域名。
 - 	 	源站地址选择**域名**；填写 API 网关服务的默认子域名。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/7e141d1f78a566a2674cd0956fcf8dd6.png" width=600>
5. 单击**保存**，完成配置，此时域名接入状态为“未配置 CNAME 记录”。


### 步骤3：修改 CNAME 记录
详细参考指引 [域名添加](https://cloud.tencent.com/document/product/627/18631) 和 [修改DNS解析](https://cloud.tencent.com/document/product/627/18633)。
1. 修改 CNAME 记录，将自定义域名指向 WAF 的 CNAME 域名。
2. 登录 WAF 控制台，在左侧导航栏中单击 **Web 应用防火墙** > **防护设置**，进入防护设置页面。
3. 单击域名列表中接入状态后面的刷新按钮，可以看到接入状态变为**正常防护**，至此接入配置完成。
