## 什么是 CC 防护？
- CC 防护是指针对 CC 攻击的防护。

## CC 防护的原理是什么？
-  CC 防护的原理是对全站进行 QPS 进行监控，当达到设置的 QPS 值时，则会触发针对 CC 攻击的清洗。

##  http 请求阈值应设置为多少比较合适？
- 推荐您将 http 请求阈值 （QPS） 设置为业务量 1.2 倍。

## CC防护的生效时间
- 当您选择开启或者修改CC防护的配置后，配置将实时生效。

## 如何开启CC防护(根据自身业务情况选择开启)
1. 登录控制台BGP高防包配置页面
登录 “ [大禹网络安全](https://cloud.tencent.com/document/product/297) ” 控制台，在  “ BGP 高防包 ”  控制页中找到您所购买的 BGP 高防包实例。
2. 选择所要开启 CC 防护的 BGP 高防包实际，点击实例名称进入 BGP 高防服务包详情页面。
  ![](https://main.qcloudimg.com/raw/7b49887a3ade760ed476ab5e3c1ae721.png)
	
3. 在 CC 防护一栏开启 CC 防护开关，根据自身业务需要设置 http 请求阈值即可，推荐您将 http 请求阈值设置为业务量 1.2 倍。
  ![](https://main.qcloudimg.com/raw/1df583bf4739d7a568bb9cc4859f2fa5.png)
	