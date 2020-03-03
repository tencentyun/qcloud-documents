SEO 优化配置是解决域名接入 CDN 后，因 CDN 频繁变更 IP 而影响域名搜索结果权重问题的功能。通过识别访问 IP 是否属于搜索引擎，用户可选择直接回源访问资源，来保证搜索引擎权重的稳定性。

> **注**：由于搜索引擎 IP 更新较为频繁，腾讯云 CDN 仅能确保能识别绝大多数的搜索引擎 IP。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【高级配置】，您可以看到 **SEO 优化配置** 模块。默认情况下，搜索引擎自动回源为关闭状态。
> **注意**：SEO 优化配置功能只在域名接入方式为 **自有源** 时可使用。开启 SEO 优化配置功能后，若域名有多个源站地址，则默认回源地址为添加的第一个源站地址。

![](https://mc.qcloudimg.com/static/img/ba53dad1df9c481d35552040b8cb538c/seo.png)
若当前域名的 CNAME 为旧版 CNAME，还需更新为新版 CNMAE 后才可使用 SEO 优化配置功能。CNAME 更新的具体操作步骤如下：
1. 提交工单变更相应域名的 CNAME 为新版 CNAME。
2. 在您的域名解析服务商处将对应域名的 CNAME 解析切换为新版 CNAME。
![](https://mccdn.qcloud.com/static/img/80afb8cf5a858e91d596f5a3be86f70d/seo.png)
