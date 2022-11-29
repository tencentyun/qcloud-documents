## 功能简介
重写 Host 头字段。若您的回源 Host 与 [负载均衡](https://cloud.tencent.com/document/product/1552/70905) 任务中接入的加速域名不同，可使用此功能重写 Host 至实际回源 Host。

## 操作步骤

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**源站配置** > **规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![img](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需配置 Host Header 重写规则。
3. 在规则引擎页面，匹配类型 **Host**，操作选择 **Host Header 重写**，并按需配置其他参数，单击**保存发布**或**仅保存**。
>?目前支持的匹配类型为 Host。
>
   

