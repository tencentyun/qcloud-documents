
## 配置场景

腾讯云 CDN 支持配置 HTTPS/HTTP 强制跳转：

- 已经配置了证书进行 HTTPS 加速的域名，可指定301/302跳转方式，将所有到达 CDN 节点的 HTTP 请求强制跳转为 HTTPS。
- 也可指定301/302跳转方式，将所有到达 CDN 节点的 HTTPS 请求强制跳转为 HTTP 请求。
- 跳转时默认不携带 Response header，可变更。

## 配置指南

### 配置约束

配置 HTTPS 强制跳转，需要先在 CDN 启用 HTTPS 加速。

### 配置说明

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可在【Https 配置】中可看到【强制跳转】配置开关，默认情况下为关闭状态，默认不进行任何跳转：
<img src="https://main.qcloudimg.com/raw/db35eccbcc86efb8041acd7d2e62ace7.png" style="width:700px"/>
单击开启，可配置跳转类型、跳转方式及是否携带头部：
<img src="https://main.qcloudimg.com/raw/bb68d629d2015e79ef492ee8e00ae69a.png" style="width:450px"/>
单击确认后，即可直接发布配置至现网：
<img src="https://main.qcloudimg.com/raw/bd1a62d0b49fb4f2e189512e30b8b9ff.png" style="width:700px"/>

