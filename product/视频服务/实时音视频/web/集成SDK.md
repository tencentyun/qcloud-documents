## 集成SDK

### 导语
欢迎来到集成SDK教程!

### 预备知识

####  H5支持的平台

| 操作系统平台  | 浏览器/webview  | 版本要求  |  备注|
| ------------------------- | -------- | ---------------------- |------- |
| iOS          | Safari (Only) | 11.1.2 | 由于Safari的实现仍然bug，产品化方案建议先规避，待苹果解决后再使用 |
| Android      | TBS | 43600                |   [什么是TBS?](http://x5.tencent.com/)   |
| Android      | Chrome | 60+               | 需要支持 H264  |
| Mac          | Chrome | 47+                |      |
| Windows(PC)  | Chrome | 52+                |    &nbsp;  |

> 基于TBS内核的webview，需满足版本>=43600，我们的[示例代码](./示例代码.md#检测是否支持WebRTC)中有获取TBS版本的方法


### 了解基本名词

* 腾讯云账户信息

| 名词          | 含义                                       |
| ----------- | ---------------------------------------- |
| appid       | 商户在腾讯云注册后，会产生一个在腾讯云的唯一标示，称为appid         |
| sdkappid    | 商户可以在互动直播控制台创建多个应用，以对应自己不同的app。每个应用都会有一个sdkappid来标示 |
| accounttype | 每个sdkappid在账户体系页面都会有一个accounttype参数，登录的时候会用到 |

> appid 是 125xxxxxxx 的数字，可以在 https://console.qcloud.com/ilvb 的顶部找到

> sdkappid 是  14000xxxxx 的数字 ，https://console.qcloud.com/ilvb 先创建应用，就会看到

> accounttype 需要你在 https://console.qcloud.com/ilvb 创建应用后，查看 【APP基础设置】 - 【帐号集成体系】中找到（如果没有，编辑保存即可）


* 用户信息

| 名词      | 含义                                       |
| ------- | ---------------------------------------- |
| OpenID  | 也叫identifier，在app中标示用户的身份,一般大家都把他叫做用户名   |
| TinyID  | 每个OpenID在腾讯云那边都会有一个对应的身份信息标示，称为TinyID    |
| UserSig | 每个OpenID都有一个对应的签名，在请求的时候带上，以便腾讯云鉴别用户的身份。这个签名称为usersig |



* 视频通话信息

| 名词      | 含义                                       |
| ------- | ---------------------------------------- |
| spear角色 | 一个视频用户的分辨率、码率、帧率等信息的配置信息集合名，可以在应用的Spear引擎页面维护 |
| roomid  | 用来标示一个视频通话。roomid相同的用户才能相互看到             |



### 接入准备工作

1. 注册腾讯云帐号，申请开通互动直播业务
2. 在互动直播页面，新建应用。得到sdkappid和accounttype
3. 参考[usersig的计算文档](https://cloud.tencent.com/document/product/268/7656)，计算出测试用户名的usersig
4. 如果所在网络有防火墙，请确定有开放以下端口：

| 协议      | 端口号                                       |
| ------- | ---------------------------------------- |
| TCP | 8687 、443 |
| UDP  | 8000 、 8800 <br/>42000 - 42200 <br/>42201 - 42800 <br/>52000 - 52200 |

使用CDN引入SDK

#### 在页面中引入 WebRTCAPI.min.js

```html
<script src="https://sqimg.qq.com/expert_qq/webrtc/2.1/WebRTCAPI.min.js"></script>
```


[下一课 三步完成进房连麦](三步完成进房连麦.md)