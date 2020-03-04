## 配置场景
腾讯云 CDN 支持配置 HTTPS 强制跳转，已经配置了证书进行 HTTPS 加速的域名，可指定301/302跳转方式，将所有到达 CDN 节点的 HTTP 请求强制跳转为 HTTPS。
## 配置指南
### 查看配置
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面最后一栏【高级配置】中，已配置 HTTPS 证书的域名，可看到【强制跳转】开关，默认情况下强制跳转为关闭状态：
![](https://main.qcloudimg.com/raw/3a60e71f17f830bf4ae4d00d4efd1124.png)
### 修改配置
可单击右侧【编辑】，进行301/302跳转切换，也可直接通过开关进行配置关闭：
![](https://main.qcloudimg.com/raw/f0b2fab0919635c6ba3c4784083cf942.png)
![](https://main.qcloudimg.com/raw/ba7f5a597ae182e019cb13704fbad9ef.png)

> !若域名的服务区域为全球，则配置的 HTTPS 强制跳转会全球生效，暂不支持境内、境外分别配置。
