## TUICallKit 说明 
TUICalling 小程序平台音视频通话组件支持如下两种接入方式：

- TUICallKit：含 UI 交互版本，交互体验”类微信“，适用于大部分通话场景
- TUICallEngine：无 UI 交互版本，仅包含通话业务相关的逻辑 API，适用于 UI 定制性较高的场景

本文以`TUICallKit`的接入为主，如果您需要使用`TUICallEngine`进行接入，可以参考 [TUICallEngine API]()。

## 接入TUICallKit
通过集成TUICallKit，您可以通过对方 UserId 直接拨打一个 1v1 通话。

### 步骤一：购买说明
主要介绍如何快速开通音视频通话能力，以及音视频通话套餐购买的流程

IM 音视频通话能力，是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两个基础的通信 PaaS 服务构建出的增值能力，需要您购买额外的套餐，同时我们也提供有 7 天的免费体验环节，欢迎您的使用~


###  步骤二：开通 IM 服务
本章节主要针对尚未开通过 IM 服务的新用户，如果您已经有IM 应用，可以跳过此章节，可以点击 [这里](https://console.cloud.tencent.com/im) 进行查询；

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)

3. 创建完成后，可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间、标签以及到期时间。请记录 SDKAppID 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/dafcf805e22c15f6c0096bfb4e960528.png)

[](id:step2)
4. 单击目标应用卡片，进入应用的基础配置页面。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)
5. 在**基本信息**区域，单击**显示密钥**，复制并保存密钥信息。

>!这里请您妥善保管密钥信息，谨防泄露。


### 步骤三：开通音视频通话能力
1. 在创建 IM 应用成功后，如果您希望先体验音视频通话能力，可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 的如下区域开通免费体验服务，在弹窗中点击领取7天试用即可免费领取7天音视频通话体验版。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9f72ed668b8a82b9301d9a5dbf24db12.png" width="900">


>!每个SDKAppId仅有一次领取体验版的机会。

2. 在体验完成后，如果您确认购买，可以点击腾讯实时音视频服务区域的前往加购，可以进入IM套餐包购买页选购对应的音视频通话能力包，购买完成后会自动开通实时音视频服务。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9f9d4cac0ee9c88bb28e35c45c506b0c.png" width="900">



3、购买完成后，您可以在腾讯实时音视频服务区域点击详情按钮查看并管理当前音视频通话能力的版本。
<img src="https://qcloudimg.tencent-cloud.cn/raw/441d8ac3b6e5c4bb70884c002d85de05.png" width="900">


### 步骤四：下载并导入 TUICallKit 组件
单击进入 Github ，选择克隆/下载代码，然后拷贝MiniProgram 下的debug目录，lib目录以及 TUICallKit 和 TUICallEngine 目录到您的工程中。

### 步骤五：配置app.js
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


### 步骤六：填写SDKAppId和SECRETkey
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

### 步骤七：创建并初始化 TUI 组件库
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



### 步骤八：发起视频通话请求
实现1对1视频通话
在 JS 逻辑交互例如 pages/index/index.js 中填写如下代码，就可以实现一对一视频通话。
```javascript
// 发起1对1视频通话，假设被邀请人的userId为: 1111, type 1：语音通话，2：视频通话。
this.TUICallKit.call({ userID: '1111', type: 2 });
```


