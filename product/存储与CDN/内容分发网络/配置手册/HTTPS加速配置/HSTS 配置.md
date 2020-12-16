

## 配置场景

HSTS 即 HTTP Strict Transport Security，是国际互联网工程组织 IETE 推行的 Web 安全协议，通过强制客户端（浏览器等）使用 HTTPS 与服务器创建链接，帮助网站进行全局加密。

## 配置约束

- expireTime 约束为0 - 365天，配置时单位为秒。
- 可通过勾选是否包含子域名，来控制 includeSubDomain 参数。
- 开启 HSTS 配置需要先完成 HTTPS 加速配置。

## 配置指南

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面，【Https 配置】中可看到 HSTS 配置模块，默认情况下为关闭状态：
![](https://main.qcloudimg.com/raw/f9c2e5d2796fc254ae316bd560bcf2c3.png)
单击开启，可进行相关配置：
![](https://main.qcloudimg.com/raw/cdcc8afd16cb9fe284eb307db8022fa7.png)
单击【确定】后，根据所配置的内容决定响应头值，可单击【编辑】进行修改：
![](https://main.qcloudimg.com/raw/4c6fbedf2f0f7b40cccc8a094af5bca3.png)

## 配置示例

假设域名`cloud.tencent.com`的 HSTS 配置如下：
![](https://main.qcloudimg.com/raw/4c6fbedf2f0f7b40cccc8a094af5bca3.png)
访问时其 Response Header 为：
![](https://main.qcloudimg.com/raw/910e57e5abdedba4a33b4e4748a81318.png)

