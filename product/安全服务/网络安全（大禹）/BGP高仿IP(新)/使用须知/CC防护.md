 ##  什么是 CC 防护？
CC 防护是指针对 CC 攻击的防护。

## CC 防护的原理是什么？
CC 防护的原理是对全站进行 QPS 进行监控，当达到设置的 QPS 值时，则会触发针对 CC 攻击的清洗。

## HTTP 请求阈值应设置多少？
推荐您将 HTTP 请求阈值（QPS）设置为业务量的 1.2 倍。

## CC 防护的生效时间
当您选择开启或者修改 CC 防护的配置后，配置将实时生效。

## 如何开启 CC 防护 ( 根据自身业务情况选择开启 ) ？
1. 登录 [大禹网络安全](https://console.cloud.tencent.com/dayu/basic)  控制台，在 “ BGP  高防  IP  ”控制页中找到您所购买的 BGP 高防 IP 实例；
![](https://main.qcloudimg.com/raw/d9d8a9d3bca8ba7ec791065be15358c0.png)
2. 选择所要开启 CC 防护的 BGP 高防 IP 实例，点击实例名称进入 BGP 高防 IP 详情页面；
![](https://main.qcloudimg.com/raw/89fa28959d6409a918ce1a7c6e65bc70.png)
3. 在 CC 防护一栏开启 CC 防护开关，根据自身业务需要设置 HTTP 请求阈值即可，推荐您将 HTTP 请求阈值设置为业务量的 1.2 倍。
![](https://main.qcloudimg.com/raw/8bf9c80734b737a0e5d6347f8cd69a57.png)
