**步骤预览**

![流程图](https://mc.qcloudimg.com/static/img/5a3583a665decdd4ffe2985dec6871ae/cdn-start.png)
## 第一步：开通 CDN 服务
在使用 CDN 服务前，您需要进行实名认证及 CDN 服务的开通，如果您的腾讯云账号已经开通 CDN，请直接跳到第二步。
### 1.完成实名认证
新用户登陆 [CDN 控制台](https://console.cloud.tencent.com/cdn) 可以看到实名认证指引，单击【前往认证】可进行实名认证。
![](https://mc.qcloudimg.com/static/img/1784f11f0b2ffcdda8872c50550804b5/identity.png)
您也可以通过进入 [帐号中心](https://console.cloud.tencent.com/developer) ，单击[【实名认证】](https://console.cloud.tencent.com/developer?to=auth)进行认证。
![](https://mc.qcloudimg.com/static/img/89cf6aefa8292bdc64662fcc8817a397/auth.png)
> 详细认证流程请查阅 [实名认证指引](https://cloud.tencent.com/doc/product/378/3629) 。个人认证会在提交审核后立即完成。企业认证约一个工作日完成，且认证成功后您将收到短信通知。您可以 [提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=1&level2_id=41&level1_name=%E5%85%AC%E5%85%B1%E5%9F%BA%E7%A1%80%E7%B1%BB%E9%97%AE%E9%A2%98&level2_name=%E8%B4%A6%E5%8F%B7%E7%B1%BB) 咨询实名认证进度。

### 2.补充服务信息
完成实名认证后，进入 [CDN 控制台](https://console.cloud.tencent.com/cdn)，确认您的实名认证信息及选择服务内容，完成后单击【下一步】。
![](https://mc.qcloudimg.com/static/img/7ddd56c73162b7ff908c70f52b3eb4e1/addinfo.png)
### 3.选择付费方式
补充服务信息后，进入 [CDN 控制台](https://console.cloud.tencent.com/cdn) ，可对计费方式进行选择。详细价格计算说明可查阅 [计费说明](https://cloud.tencent.com/doc/product/228/2949)。
![](https://mc.qcloudimg.com/static/img/b13dd5b1c61fc44a44824d7d45cd1a9c/paychoose.png)
确认付费方式，单击【开通 CDN 】即可开通 CDN 服务并跳转到 CDN 概览页，您可以通过概览页了解您的 CDN 整体情况。
![](https://mc.qcloudimg.com/static/img/eff4d520fb07998d741a95719d966937/cnddesc.png)

## 第二步：接入域名
1.进入 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧菜单中【域名管理】进入相应页面，单击【添加域名】。
![](https://mc.qcloudimg.com/static/img/b1c4623293ce5e4600bd905d5a795622/addhost.png)

2.填写域名相关配置及加速服务相关配置。
在**域名**位置填入需要加速的域名，该域名需要满足以下条件：
+ 已经在工信部进行过备案
+ 尚未被接入过腾讯云 CDN

**业务类型** 选择，决定了域名调度的资源平台，不同资源平台加速配置存在一定差异，请选择与您业务相匹配的业务类型：
-  静态加速：适用于电商类、网站类、游戏图片类静态资源加速场景。
-  下载加速：适用于游戏安装包、音视频原文件下载、手机固件分发等场景。
-  流媒体点播加速：适用于音视频点播加速等场景。
-  流媒体直播加速：适用于直播、互动直播下行加速等场景。
![](https://mc.qcloudimg.com/static/img/b2fdd0bef148d38e256aaf8b9648433f/addhost.png)

3.提交域名，添加完成，请耐心等待域名配置下发至全网节点，下发时间约 15 分钟。
![](https://mc.qcloudimg.com/static/img/c3ff6aae83f3b19b242f859df32ab7bd/addok.png)

## 第三步：配置 CNAME
1.域名配置完成后，系统会为您分配对应的 **CNAME** ，以 ```.cdn.dnsv1.com``` 为后缀。
![](https://mccdn.qcloud.com/static/img/93257fff3cdf7311a2108bfec8d9fab0/image.png)

2.您需要到接入域名的 DNS 服务商处完成 CNAME 配置，配置方法请查阅 [CNAME 配置](https://cloud.tencent.com/doc/product/228/3121)。

3.验证 CNAME 是否生效：不同的DNS服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过 PING 的方式来查询 CNAME 是否生效，如果 PING 到后缀为 ```.sp.spcdntip.com``` 的域名，表示域名 CNAME 已生效。
![](https://mc.qcloudimg.com/static/img/13b5d4cc294c6f11543553a4d0f61b09/ping.png)