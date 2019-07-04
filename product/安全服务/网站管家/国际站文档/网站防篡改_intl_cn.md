## 功能简介
防篡改功能可用于防止指定的页面由于被篡改而显示异常的问题。
## 注意事项 
指定的页面仅限于`.html`、`.js`、`.txt`等静态资源。
## 配置示例 
### 保护网站主页不被篡改
1. 登录 [网站管家控制台](https://console.cloud.tencent.com/guanjia)，单击【网站应用防火墙】>【防护设置】，选择需要防护的站点域名（如`www.qcloudwaf.com`），单击【防篡改】进入防篡改配置界面。
![](https://main.qcloudimg.com/raw/21643cd78783fac306ae8aade064aab0.png)
2. 单击【添加规则】，输入规则名称（如主页），输入主页完整的 URL 路径（如`http://www.qcloudwaf.com/index.html`）。
![](https://main.qcloudimg.com/raw/f64f52177854f67b2dfb57086105cb9c.png)
3. 单击【添加】保存规则，此时规则将会生效。如果主页有更新，则可单击【刷新缓存】来更新缓存内容。
![](https://main.qcloudimg.com/raw/0292f8dd8b035478811e881e1e61a55b.png)

[上一步：CC 防护设置](/document/product/627/11709)
[下一步：自定义策略](/document/product/627/11711)
