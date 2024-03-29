## 配置场景
HTTP2.0 作为最新的 HTTP 协议，大幅提升了 Web 性能，进一步减少了网络延迟。已配置证书启用 HTTPS 加速的域名，可自助开启 HTTP2.0 协议支持。
> !目前仅支持 HTTP2.0 访问，暂不支持 HTTP2.0 协议回源。


## 配置指南
### 查看配置
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面【Https 配置】中，可看到【HTTP2.0 配置】：
![](https://qcloudimg.tencent-cloud.cn/raw/d4e585fb2ba9be3797c2efdff73a94a5.png)




###  修改配置
通过单击开关，可对 HTTP2.0 配置进行开启或关闭操作，删除证书配置后，HTTP2.0 配置会同步失效：
![](https://qcloudimg.tencent-cloud.cn/raw/c68120025d7ef21127df3cad14e82314.png)

> !若域名的服务区域为全球，则配置的 HTTP2.0 会全球生效，暂不支持境内、境外分别配置。

