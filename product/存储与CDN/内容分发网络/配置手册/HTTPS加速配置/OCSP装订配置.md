
## 配置场景
启用 OCSP 装订（TLS 证书状态查询扩展）后， 服务器在 TLS 握手时会发送事先缓存的在线证书状态协议（OCSP）响应，供用户验证，无需用户再向数字证书认证机构（CA）发送查询请求。OCSP 装订极大地提高了 TLS 握手效率，节省了用户验证时间。

腾讯云 CDN 支持自助开启或关闭 OCSP 装订配置。


## 配置指南
### 查看配置
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面【Https 配置】中，可看到【OCSP 装订配置】，默认情况下为关闭状态：
![](https://main.qcloudimg.com/raw/063f1f4f85850f9faafdea14a2507711.png)

###  修改配置
配置了 HTTPS 加速的域名，可直接通过单击开关，对 OCSP 装订配置进行开启或关闭操作，删除证书配置后，OCSP 装订配置会同步失效：
![](https://main.qcloudimg.com/raw/73f0f5763dfc99956272f846aed079a4.png)

> !若域名的服务区域为全球，则配置的 OCSP 装订会全球生效，暂不支持境内、境外分别配置。

