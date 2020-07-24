## 功能简介
防篡改功能可用于防止发生指定页面被篡改而显示异常的问题。
>!指定页面仅限于`.html`、`.shtml`、`.txt`、`.js`、`.css`、`.jpg`、`.png`等静态资源。
## 配置示例 
### 保护网站主页不被篡改
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia)，在左侧导航栏中，选择【Web 应用防火墙】>【防护设置】，在域名列表中，选择需要防护的站点域名（如`www.qcloudwaf.com`），在右侧操作栏中，单击【防护配置】。
![](https://main.qcloudimg.com/raw/5c5c6538e7f4f79f114af7db2d62c1d8.png)
2. 进入防护设置页面，如果有需要可以在上方更换需要防护的站点域名，单击【防篡改】，进入防篡改配置界面，单击 【添加规则】。
 ![](https://main.qcloudimg.com/raw/59d44caef924f1743621b6dae93cb02a.png)
3. 在添加防篡改规则弹窗内，输入规则名称（如主页），输入规则（如主页）完整的 URL 路径（如`http://www.qcloudwaf.com/index.html`），输入完成后单击【添加】，保存规则。
 ![](https://main.qcloudimg.com/raw/7843d55aaec679d5bf83b6f42f29c54c.png)
4. 此时规则将会生效，如果规则更新，在右侧操作栏，单击【刷新缓存】，可更新缓存内容。
 ![](https://main.qcloudimg.com/raw/f76edde165f01f5e332268505330a763.png)
