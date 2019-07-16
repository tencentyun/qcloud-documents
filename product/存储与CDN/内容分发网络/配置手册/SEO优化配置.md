 SEO 优化配置是解决域名接入 CDN 后，因 CDN 频繁变更 IP 而影响域名搜索结果权重问题的功能。通过识别访问 IP 是否属于搜索引擎，用户可选择直接回源访问资源，来保证搜索引擎权重的稳定性。

>!由于搜索引擎 IP 更新较为频繁，腾讯云 CDN 仅能确保能识别绝大多数的搜索引擎 IP。

## 配置指引
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://main.qcloudimg.com/raw/b6d8bae9b2ed90c37d4555f627d42ca4/HTTP%20Header1.png)
单击【高级配置】，您可以看到**SEO 优化配置**模块。默认情况下，搜索引擎自动回源为关闭状态。
>!SEO 优化配置功能只在域名接入方式为**自有源**时可使用。开启 SEO 优化配置功能后，若域名有多个源站地址，则默认回源地址为添加的第一个源站地址。

![](https://main.qcloudimg.com/raw/ba17c127b09456c142340b303567741e/SEO2.png)

若当前域名的 CNAME 为旧版 CNAME，还需更新为新版 CNAME 后才可使用 SEO 优化配置功能。

CNAME 更新的具体操作步骤如下：

1. 提交工单变更相应域名的 CNAME 为新版 CNAME。

2. 在您的域名解析服务商处将对应域名的 CNAME 解析切换为新版 CNAME。

  ![](https://main.qcloudimg.com/raw/271a2ea8a13c7e9e6a02bf998497739b/seo3.png)
