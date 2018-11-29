
## 预备知识
### H5 支持的平台

| 操作系统平台 | 浏览器/webview  | 版本要求 | 备注          |
| ------------ | --------------- | -------- | ------------- |
| iOS          | Safari ( Only ) | 11.1.2   |               |
| Android      | Chrome          | 60+      | 需要支持 H264 |
| Mac          | Chrome          | 47+      |               |
| Mac          | Safari          | 11+      |               |
| Windows(PC)  | Chrome          | 52+      |               |

## 基本名词
腾讯云账户信息

| 名词        | 含义                                                         |
| ----------- | ------------------------------------------------------------ |
| appid       | 商户在腾讯云注册后，会产生一个在腾讯云的唯一标示，称为 appid |
| sdkappid    | 商户可以在实时音视频控制台创建多个应用，以对应自己不同的 App。每个应用都会有一个 sdkappid 来标示 |
| accounttype | 每个sdkappid在账户体系页面都会有一个accounttype参数，登录的时候会用到 |

appid 是 125xxxxxxx 的数字，可以在 实时音视频控制台 的顶部获取。
sdkappid 是 14000xxxxx 的数字 ， 实时音视频控制台 创建应用，在【App 基础设置】下可查看。
accounttype 需要您在 实时音视频控制台 创建应用后，查看 【App 基础设置】-【帐号集成体系】中找到（ 如果没有，编辑保存即可 ）

用户信息

| 名词    | 含义                                                         |
| ------- | ------------------------------------------------------------ |
| userId  | 在 App 中标示用户的身份,一般大家都把他叫做用户名             |
| userSig | 身份签名，相当于登录密码的作用。每个 userId 都有一个有一定期限的签名，在请求的时候带上，以便腾讯云鉴别用户的身份。 |

视频通话信息

| 名词          | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| spear 角色    | 一个视频用户的分辨率、码率、帧率等信息的配置信息集合名，可以在应用的 Spear 引擎页面维护 |
| roomId        | 用来标识一个视频通话房间。roomId 相同的用户才能相互看到      |
| privateMapKey | 房间权限key，相当于进入指定房间roomId的钥匙                  |
下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 userSig 和 privateMapKey 的计算代码（生成 userSig 和 privateMapKey 的签名算法是 ECDSA-SHA256）。

## 接入准备工作
1. 注册腾讯云帐号，联系销售申请开通实时音视频业务；
2. 在实时音视频页面，新建应用。得到 sdkappid 和 accounttype；
3. 参考 [usersig 计算文档](https://intl.cloud.tencent.com/document/product/268/7656) ，计算出测试用户名的 usersig；
4. 如果所在网络有防火墙，请确定有开放以下端口：

| 协议 | 端口号              |
| ---- | ------------------- |
| TCP  | 8687                |
| UDP  | 8000 、 8800 、 443 |

使用 CDN 引入SDK。
### 在页面中引入 WebRTCAPI.min.js

`<script src="https://sqimg.qq.com/expert_qq/webrtc/2.6/WebRTCAPI.min.js"></script>`
### Update Log
2.6
新增SoundMeter接口
新增日志上报的字段
调整初始化接口
