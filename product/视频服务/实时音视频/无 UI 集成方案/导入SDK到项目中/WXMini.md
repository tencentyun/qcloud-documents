本文主要介绍如何快速地将腾讯云 TRTC Wechat SDK 集成到您的项目中。
![](https://qcloudimg.tencent-cloud.cn/raw/49940081e803fb4534019ad5cb03dff8.png)
## 准备工作
集成 TRTC Wechat SDK 之前需要了解的事项。

### 环境要求

- 微信 App iOS 最低版本要求：7.0.9
- 微信 App Android 最低版本要求：7.0.8
- 小程序基础库最低版本要求：2.10.0
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，请使用企业小程序账号申请相关权限进行开发。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 不支持 uniapp 等开发框架，请使用原生小程序开发环境。

### 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在 **[微信公众平台](https://mp.weixin.qq.com)** > **开发** > **开发管理** > **接口设置** 中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)

### 配置域名添加

在 **[微信公众平台](https://mp.weixin.qq.com)** > **开发** > **开发管理** > **开发设置** > **服务器域名**中设置 **request合法域名**和 **socket合法域名**，如下图所示：
- request 合法域名：
```
https://official.opensso.tencent-cloud.com
https://yun.tim.qq.com
https://cloud.tencent.com
https://webim.tim.qq.com
https://query.tencent-cloud.com
https://web.sdk.qcloud.com
```
- socket 合法域名：
```
wss://wss.im.qcloud.com
wss://wss.tim.qq.com
```

![](https://qcloudimg.tencent-cloud.cn/raw/a79ca9726309bb1fdabb9ef8961ce147.png)
## 开始集成
SDK 提供了 ES Module 类型的模块。
### NPM 集成
1. 您需要在项目中使用  [trtc-wx](https://www.npmjs.com/package/trtc-wx-sdk) 包。
```
npm i trtc-wx-sdk --save
```
2. 在项目脚本里引入模块。
```javascript
import TRTC from 'trtc-wx.js';
```


**资源下载**
- [单击下载 SDK 及示例](https://web.sdk.qcloud.com/trtc/miniapp/download/trtc-wx.zip)
- [GitHub 仓库地址](https://github.com/LiteAVSDK/Live_WXMini)

