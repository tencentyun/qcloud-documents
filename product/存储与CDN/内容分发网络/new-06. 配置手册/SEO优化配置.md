## 功能介绍
SEO优化配置是为解决域名接入CDN后，因CDN频繁变更IP而影响域名搜索结果权重问题的功能；通过识别访问IP是否属于搜索引擎，用户可选择直接回源访问资源，来保证搜索引擎权重的稳定性。
开启SEO优化配置功能，来自搜索引擎的请求将直接回源，其他请求将正常访问CDN节点。


## 配置说明

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

您可以在 【高级配置】 中找到 **SEO 优化配置** 配置项：

![](https://mccdn.qcloud.com/static/img/d9643dcd9a8d747fc79642cdaf059499/SEO.png)

+ SEO 优化配置功能只能在**“自有源”**方式接入下可使用，开启SEO优化配置功能后，**若域名有多个源站地址，则默认回源地址为添加的第一个源站地址**；
+ 若当前域名的 CNAME 为旧 CNAME，如下图所示，还需更新为新 CNMAE 后才可使用 SEO 优化配置功能。

![](https://mccdn.qcloud.com/static/img/80afb8cf5a858e91d596f5a3be86f70d/seo.png)

CNAME 更新的具体操作步骤如下：
+ 提交工单变更相应域名的 CNAME 为新版；
+ 在您的域名解析服务商处将对应域名的 CNAME 解析切换为新版 CNAME；

注：由于搜索引擎 IP 更新较为频繁，腾讯云 CDN 仅能确保能识别绝大多数的搜索引擎 IP。