## 什么是 CC 攻击？
CC 攻击即 ChallengeCollapsar 攻击，指攻击者借助代理服务器生成指向受害主机的合法请求，拥塞被攻击方的网络和服务器性能，实现攻击目的。

## 什么是 CC 防护？
CC 防护即指针对 CC 攻击的防护。

## 如何开启 CC 防护？
**特别提醒：**
CC 防护可根据您自身业务情况选择开启。
1. 登录 [DDoS 防护（大禹）](https://console.cloud.tencent.com/dayu/overview) 控制台，在 “BGP 高防包” 控制页中找到您所购买的 BGP 高防包实例；
 ![](https://main.qcloudimg.com/raw/78dff8603cf7b5b09dd9580f50d305d7.png)
2. 选择所要开启 CC 防护的 BGP 高防包实例，单击实例名称进入 BGP 高防服务包详情页面。
 ![](https://main.qcloudimg.com/raw/7b49887a3ade760ed476ab5e3c1ae721.png)	
3. 在 CC 防护一栏开启 CC 防护开关，根据自身业务需要设置 HTTP 请求阈值即可，推荐您将 HTTP 请求阈值设置为业务量的 1.2 倍。
 ![](https://main.qcloudimg.com/raw/1df583bf4739d7a568bb9cc4859f2fa5.png)
