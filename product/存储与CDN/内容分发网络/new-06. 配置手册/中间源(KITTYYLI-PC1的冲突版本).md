## 功能介绍

中间源可以理解为二级缓存节点，当用户发起请求时，请求会先到达边缘节点，若节点无所需资源，则会向中间源发起资源请求，若仍未在中间源命中，中间源会向源站发起请求。

开启了中间源后，用户的请求回源行为会在中间源进行收敛，由中间源统一回源获取数据，有效缓解源站压力。

<font color="red">为提升您的CDN加速效果，有效降低回源带宽，推荐您开启中间源</font>

## 配置说明

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

在 【回源配置】中找到 **中间源配置** 模块，开启中间源配置：

![](https://mc.qcloudimg.com/static/img/ebf26011eb4c08eec66dae276b935bbf/middle.png)

默认情况下中间源配置为开启状态。




