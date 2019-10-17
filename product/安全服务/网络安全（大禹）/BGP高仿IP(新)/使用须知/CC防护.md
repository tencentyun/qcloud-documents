## 什么是 CC 攻击？
CC 攻击即 ChallengeCollapsar 攻击，指攻击者借助代理服务器生成指向受害主机的合法请求，拥塞被攻击方的网络和服务器性能，实现攻击目的。

## 什么是 CC 防护？
CC 防护即指针对 CC 攻击的防护。

## 如何开启 CC 防护？
**特别提醒：**
CC 防护可根据您自身业务情况选择开启。
1. 登录 [DDoS 防护（大禹）](https://console.cloud.tencent.com/dayu/overview) 控制台，在 “BGP 高防 IP” 控制页中找到您所购买的 BGP 高防 IP 实例；
 ![](https://main.qcloudimg.com/raw/d9d8a9d3bca8ba7ec791065be15358c0.png)
2. 选择所要开启 CC 防护的 BGP 高防 IP 实例，单击实例名称进入 BGP 高防 IP 详情页面；
 ![](https://main.qcloudimg.com/raw/89fa28959d6409a918ce1a7c6e65bc70.png)
3. 在 CC 防护一栏开启 CC 防护开关，根据自身业务需要设置 HTTP 请求阈值即可，推荐您将 HTTP 请求阈值设置为业务量的 1.2 倍。
 ![](https://main.qcloudimg.com/raw/8bf9c80734b737a0e5d6347f8cd69a57.png)
