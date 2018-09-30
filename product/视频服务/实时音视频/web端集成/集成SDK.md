## 预备知识
###  H5 支持的平台

| 操作系统平台  | 浏览器/webview  | 版本要求  |  备注|
| ------------------------- | -------- | ---------------------- |------- |
| iOS          | Safari ( 只支持Safari ) | 11.1.2 | 由于苹果 Safari 仍有偶现的 bug，产品化方案建议先规避，待苹果解决后再使用<br > 对于iOS可以考虑使用我们的[小程序解决方案](/document/product/647/17000) |
| Android      | TBS （微信和手机QQ的默认Webview） | 43600                | 微信和手机QQ默认内置的浏览器内核为TBS。 [TBS 介绍](http://x5.tencent.com/) |
| Android      | Chrome | 60+               | 需要支持 H264  |
| Mac          | Chrome | 47+                |      |
| Mac          | Safari | 11+                |      |
| Windows(PC)  | Chrome | 52+                |      |
| Windows(PC)  | [QQ浏览器](https://browser.qq.com/) | 10.2 | &nbsp;     |


> 基于 TBS 内核的 webview，需满足版本 >= 43600，我们的[ 能力检测 ](/document/product/647/17251#webrtcapi.fn.detectrtc) 中有获取 TBS 版本的方法。

## 基本名词

* 腾讯云账户信息

| 名词          | 含义                                       |
| ----------- | ---------------------------------------- |
| appid       | 商户在腾讯云注册后，会产生一个在腾讯云的唯一标示，称为 appid         |
| sdkappid    | 商户可以在实时音视频控制台创建多个应用，以对应自己不同的 App。每个应用都会有一个 sdkappid 来标示 |
| accounttype | 每个sdkappid在账户体系页面都会有一个accounttype参数，登录的时候会用到 |

> appid 是 125xxxxxxx 的数字，可以在[ 实时音视频控制台 ](https://console.cloud.tencent.com/rav)的顶部获取。
> sdkappid 是  14000xxxxx 的数字 ，[ 实时音视频控制台 ](https://console.cloud.tencent.com/rav)创建应用，在【App 基础设置】下可查看。
> accounttype 需要您在 [ 实时音视频控制台 ](https://console.cloud.tencent.com/rav)创建应用后，查看 【App 基础设置】-【账号集成体系】中找到（ 如果没有，编辑保存即可 ）


* 用户信息

| 名词      | 含义                                       |
| ------- | ---------------------------------------- |
| userId  | 在 App 中标示用户的身份,一般大家都把他叫做用户名    |
| userSig | 身份签名，相当于登录密码的作用。每个 userId 都有一个有一定期限的签名，在请求的时候带上，以便腾讯云鉴别用户的身份。 |


* 视频通话信息

| 名词      | 含义                                       |
| ------- | ---------------------------------------- |
| spear 角色 | 一个视频用户的分辨率、码率、帧率等信息的配置信息集合名，可以在应用的 Spear 引擎页面维护 |
| roomId  | 用来标识一个视频通话房间。roomId 相同的用户才能相互看到             |
| privateMapKey  | 房间权限key（密文），相当于进入指定房间roomId的钥匙             |

> privateMapKey 并不影响业务开发，如果暂时不用考虑对用户的权限控制，您可以忽略这部分内容

下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 userSig 和 privateMapKey 的计算代码（生成 userSig 和 privateMapKey 的签名算法是 **ECDSA-SHA256**）。

## 如何配置是是否使用房间权限key进行权限校验呢？


进入[实时音视频控制台](https://console.cloud.tencent.com/rav/app/1400128798)->选择应用->账号信息->启用权限密钥
** 特别注意，这里的策略修改后，需要2小时后才能全量生效 **

![启用权限密钥](https://main.qcloudimg.com/raw/c60b5cf33ea2c0bc291a7700f252b8c1.png)


## 接入准备工作

1. 请务必参考[开通服务](https://cloud.tencent.com/document/product/647/17195)的指引，注册腾讯云账号，申请开通实时音视频业务并**提交白名单申请**；
2. 在实时音视频页面，新建应用。得到 sdkappid 和 accounttype；
3. 参考[ usersig 计算文档 ](https://cloud.tencent.com/document/product/268/7656)，计算出测试用户名的 usersig；
4. 如果所在网络有防火墙，请确定有开放以下端口：

| 协议      | 端口号                                       |
| ------- | ---------------------------------------- |
| TCP | 8687 |
| UDP  | 8000 、 8800 、 443 |

使用 CDN 引入SDK。
### 在页面中引入 WebRTCAPI.min.js

```html
<script src="https://sqimg.qq.com/expert_qq/webrtc/3.0/WebRTCAPI.min.js"></script>
```



### 更新日志

- 3.0（ 2018-09-11 ）

  - 初始化接口 [WebRTCAPI](/document/product/647/17251#webrtcapi) 
      弃用字段 accountType 
      弃用字段 closeLocalMedia 默认不再推流
      弃用字段 video 不再支持配置是否进行音视频推流 
      弃用字段 audio 不再支持配置是否进行音视频推流
      弃用成功和失败回调
      ```javascript
      new WebRTCAPI({...});
      ```
    
- 2.6.1（ 2018-08-16 ）

  - 增加接口 getSpeakerDevices

    枚举音频输出设备

  - 增加接口chooseSpeakerDevice

    选择音频输出设备

    

- 2.6 （ 2018-08-10）

  - 新增SoundMeter接口

  - 新增日志上报的字段

  - createRoom 名称改为 enterRoom 

## 联系我们

关注公众号"腾讯云视频"，给公众号发关键字"技术支持"，会有专人联系。

![](https://main.qcloudimg.com/raw/769293c3dbc0df8fbfb7d6a7cc904692.jpg)
