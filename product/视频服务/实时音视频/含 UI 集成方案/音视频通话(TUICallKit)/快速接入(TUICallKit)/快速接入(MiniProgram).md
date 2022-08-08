## TUICallKit 说明 
TUICalling 小程序平台音视频通话组件支持如下两种接入方式：

- TUICallKit：含 UI 交互版本，交互体验”类微信“，适用于大部分通话场景
- TUICallEngine：无 UI 交互版本，仅包含通话业务相关的逻辑 API，适用于 UI 定制性较高的场景

本文以`TUICallKit`的接入为主，如果您需要使用`TUICallEngine`进行接入，可以参考 [TUICallEngine API](https://tcloud-doc.isd.com/document/product/647/78761?!preview)。

## 接入TUICallKit
通过集成TUICallKit，您可以通过对方 UserId 直接拨打一个 1v1 通话。

### 步骤一：开通服务
TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务：

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png)
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。
![](https://qcloudimg.tencent-cloud.cn/raw/667633f7addfd0c589bb086b1fc17d30.png)
3. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续的[步骤四：登录 TUI 组件](#step4)中被用到。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)


### 步骤二：下载并导入 TUICallKit 组件
单击进入 Github ，选择克隆/下载代码，然后拷贝MiniProgram下的debug目录，lib目录以及 TUICallKit 和 TUICallEngine 目录到您的工程中。

### 步骤三：配置app.js
打开根目录的app.js文件
```javascript
import { genTestUserSig } from './debug/GenerateTestUserSig';
import Aegis from './lib/aegis';

const Signature = genTestUserSig('');
App({
  onLaunch() {
    wx.$globalData = {
      userInfo: null,
      headerHeight: 0,
      statusBarHeight: 0,
      sdkAppID: Signature.sdkAppID,
      userID: '',
      userSig: '',
      token: '',
      expiresIn: '',
      phone: '',
      sessionID: '',
    };
    this.aegisInit();
    this.aegisReportEvent('onLaunch', 'onLaunch-success');
  },
  aegisInit() {
    wx.aegis = new Aegis({
      id: 'iHWefAYqxqlqtLQVcA', // 项目key
      reportApiSpeed: true, // 接口测速
      reportAssetSpeed: true, // 静态资源测速
      pagePerformance: true, // 开启页面测速
    });
  },
  aegisReportEvent(name, ext1) {
    if (!this.aegisReportEvent[name] || !this.aegisReportEvent[name][ext1]) {
      wx.aegis.reportEvent({
        name,
        ext1,
        ext2: 'wxTUICallingExternal',
        ext3: genTestUserSig('').sdkAppID,
      });
      if (typeof this.aegisReportEvent[name] !== 'object') {
        this.aegisReportEvent[name] = {};
      }
      this.aegisReportEvent[name][ext1] = true;
    }
  },
});
```


### 步骤四：填写SDKAppId和SECRETkey
打开debug文件夹下的GenerateTestUserSig.js文件
```javascript
/**
 * 腾讯云 SDKAppId，需要替换为您自己账号下的 SDKAppId。
 *
 * 进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav ) 创建应用，即可看到 SDKAppId，
 * 它是腾讯云用于区分客户的唯一标识。
 */
const SDKAPPID = '';

/**
 * 计算签名用的加密密钥，获取步骤如下：
 *
 * step1. 进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav )，如果还没有应用就创建一个，
 * step2. 单击“应用配置”进入基础配置页面，并进一步找到“帐号体系集成”部分。
 * step3. 点击“查看密钥”按钮，就可以看到计算 UserSig 使用的加密的密钥了，请将其拷贝并复制到如下的变量中
 *  */
const SECRETKEY = '';
```

### 步骤五：创建并初始化 TUI 组件库
1.添加组件到对应页面的 页面配置，例如 pages/index/index.json：
```javascript
// 可参考 MiniProgram/pages/videoCall/videoCall.json 或 MiniProgram/pages/audioCall/audioCall.json
{
    "usingComponents": {
        "TUICallKit": "/TUICallKit/TUICallKit"
    }
}
```

2.在 WXML 模板 中添加一个 TUICallKit 组件，例如示例代码中的 pages/index/index.wxml：
```javascript
// 可参考 MiniProgram/pages/videoCall/videoCall.wxml 或 MiniProgram/pages/audioCall/audioCall.wxml
  <TUICallKit
    id="TUICallKit-component"
    config="{{config}}"
  ></TUICallKit>
```

3.用 JS 代码动态设置 Config 参数
在 JS 逻辑交互例如 pages/index/index.js 中填写如下代码，用于设置 wxml 文件中的 {{config}} 变量。这部分工作可参考 MiniProgram/pages/videoCall/videoCall.js 或 MiniProgram/pages/audioCall/audioCall.js中的示例代码，如下所示：
```javascript
// 引入 userSig 生成函数
import { genTestUserSig } from '../../debug/GenerateTestUserSig';
Page({
    /**
     * 页面的初始数据
     */
    data: {
        config: {
            sdkAppID: 0, // 替换为步骤三中获取的 SDKAppID
            userID: userID,   // 填写当前用的 userID
            userSig: genTestUserSig(userID), // 通过 genTestUserSig(userID) 生成
            tim: null,   // 如果您的项目中未集成。
        }
    }
})
```
这里详细介绍一下 config 中的几个参数：
sdkAppID：在步骤三中您已经获取到，这里不再赘述。
userId：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。
userSig：使用步骤三中获取的 SecretKey 对 sdkAppID、userId 等信息进行加密，就可以得到 UserSig，它是一个鉴权用的票据，用于腾讯云识别当前用户是否能够使用 TRTC 的服务，更多信息请参见 如何计算及使用 UserSig。


4.在生命周期函数中初始化TUICallKit
```javascript
  onLoad() {
      const Signature = genTestUserSig(userID);
      const config = {
      sdkAppID: wx.$globalData.sdkAppID,
      userID: wx.$globalData.userID,
      userSig: Signature.userSig,
      };
      this.setData(
        {
          config: { ...this.data.config, ...config },
        },
        () => {
          this.TUICallKit = this.selectComponent('#TUICallKit-component');
          this.TUICallKit.init();
        },
      );
    },

```



### 步骤六：发起视频通话请求
实现1对1视频通话
在 JS 逻辑交互例如 pages/index/index.js 中填写如下代码，就可以实现一对一视频通话。
```javascript
// 发起1对1视频通话，假设被邀请人的userId为: 1111, type 1：语音通话，2：视频通话。
this.TUICallKit.call({ userID: '1111', type: 2 });
```


