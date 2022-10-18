## 功能简介

支持自定义回源 HTTP 请求头部，携带真实客户端 IP 信息回源。

## 操作步骤

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **网络优化**。
3. 在网络优化页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/8d3e9bac718473e40a340843b4cc7fb8.png)，开启“真实客户端 IP 头部”功能。
![](https://qcloudimg.tencent-cloud.cn/raw/06efe399aaf0413f24205d42b21253d1.png)
3. 在弹窗中，自定义设置该头部的名称，例如 Tencent-Client-IP，单击**保存**。
>?此页面配置均对当前所选站点的全部请求生效，为全局配置。如果子域名或请求路径需自定义配置，请在左侧菜单栏中前往 [规则引擎](https://cloud.tencent.com/document/product/1552/70901) 创建更细粒度的自定义配置。

