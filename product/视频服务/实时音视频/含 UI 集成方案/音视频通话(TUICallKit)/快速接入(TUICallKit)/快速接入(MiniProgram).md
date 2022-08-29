本文将介绍如何用最短的时间完成 TUICallKit 组件的接入，跟随本文档，您将在一个小时的时间内完成如下几个关键步骤，并最终得到一个包含完备 UI 界面的视频通话功能。


## 环境准备
- 微信 App iOS 最低版本要求：7.0.9
- 微信 App Android 最低版本要求：7.0.8
- 小程序基础库最低版本要求：2.10.0
- 由于小程序测试号不具备 &lt;live-pusher> 和 &lt;live-player> 的使用权限，请使用企业小程序账号申请相关权限进行开发
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher> 和 &lt;live-player> 标签），需要在真机上进行运行体验
- 不支持 uniapp 等开发框架，请使用原生小程序开发环境


[](id:step1)
## 步骤一：开通小程序权限
由于 TUICallKit 所使用的小程序标签有更苛刻的权限要求，因此集成 TUICallKit 的第一步就是要开通小程序的类目和标签使用权限，**否则无法使用**，这包括如下步骤：

- 小程序推拉流标签不支持个人小程序，只支持企业类小程序。需要在 [注册](https://developers.weixin.qq.com/community/business/doc/000200772f81508894e94ec965180d) 时填写主体类型为企业，如下图所示：
  ![img](https://qcloudimg.tencent-cloud.cn/raw/a30f04a8983066fb9fdf179229d3ee31.png)
- 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 符合类目要求的小程序，需要在 **[微信公众平台](https://mp.weixin.qq.com/)** > **开发** > **开发管理** > **接口设置**中自助开通该组件权限，如下图所示：
  ![img](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)


[](id:step2)
## 步骤二：在小程序控制台配置域名
在 **[微信公众平台](https://mp.weixin.qq.com/)** > **开发** > **开发管理** > **开发设置** > **服务器域名**中设置 **request 合法域名** 和 **socket 合法域名**，如下图所示：
- **request 合法域名**：
```javascript
https://official.opensso.tencent-cloud.com
https://yun.tim.qq.com
https://cloud.tencent.com
https://webim.tim.qq.com
https://query.tencent-cloud.com
https://web.sdk.qcloud.com
```
- **socket 合法域名**：
```javascript
wss://wss.im.qcloud.com
wss://wss.tim.qq.com
```
![](https://qcloudimg.tencent-cloud.cn/raw/a79ca9726309bb1fdabb9ef8961ce147.png)


[](id:step3)
## 步骤三：开通服务

TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务：

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png">
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。如果需要正式应用上线，可以单击 [**前往加购**](https://buy.cloud.tencent.com/avc) 即可进入购买页面。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/99a6a70e64f6877bad9406705cbf7be1.png">
>? IM 音视频通话能力针对不同的业务需求提供了差异化的付费版本供您选择，您可以在 [IM 购买页](https://buy.cloud.tencent.com/avc) 了解包含功能并选购您适合的版本。

3. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续的 [步骤五：填写 SDKAPPID 和 SECRETKEY](#step5)  中被用到。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png">

    - **SDKAppID**：IM 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话彼此不能互通。
    - **Secretkey**：IM 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 IM 服务的鉴权用票据 UserSig，我们会在接下来的步骤五中用到这个 Key。

<dx-alert infotype="notice" title="<b>音视频通话能力活动特惠</b>：">
即日起至2022年10月01日0点前，购买音视频通话能力包基础版可获赠解锁相同有效期的小程序端通话功能授权。在活动结束前购买的音视频通话能力包在有效期内不受活动结束影响仍可使用小程序通话功能，活动结束后的新购或续期需选择体验版、进阶版、尊享版来获取小程序通话功能授权，基础版亦可单独加购小程序功能授权进行解锁。
</dx-alert> 

<dx-alert infotype="alarm" title="<b>友情提示：</b>">
单击**免费体验**以后，部分之前使用过 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 服务的用户会提示：
```
[-100013]:TRTC service is  suspended. Please check if the package balance is 0 or the Tencent Cloud accountis in arrears
```
因为新的 IM 音视频通话能力是整合了腾讯云[实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础的 PaaS 服务，所以当 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 的免费额度（10000分钟）已经过期或者耗尽，就会导致开通此项服务失败，这里您可以单击 [TRTC 控制台](https://console.cloud.tencent.com/trtc/app)，找到对应 SDKAppID 的应用管理页，示例如图，开通后付费功能后，再次**启用应用**即可正常体验音视频通话能力。
<img width=800px src="https://qcloudimg.tencent-cloud.cn/raw/f74a13a7170cf8894195a1cae6c2f153.png" />
</dx-alert>

[](id:step4)
## 步骤四：下载并导入 TUICallKit 组件
单击进入 [Github](https://github.com/tencentyun/TUICalling)，选择克隆/下载代码，然后拷贝 MiniProgram 下的 debug 目录，lib 目录以及 TUICallKit 和 TUICallEngine 目录到您的工程中。
<img width="350" src="https://qcloudimg.tencent-cloud.cn/raw/02c1c681bf400de5ce55e8e5eb7efa3a.png">

	
[](id:step5)
## 步骤五：填写 SDKAPPID 和 SECRETKEY
打开 debug 文件夹下的 `GenerateTestUserSig.js` 文件。
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
 * 注意：该方案仅适用于调试Demo，正式上线前请将 UserSig 计算代码和密钥迁移到您的后台服务器上，以避免加密密钥泄露导致的流量盗用。
 * 文档：https://cloud.tencent.com/document/product/647/17275#Server
 *  */
const SECRETKEY = '';
```

[](id:step6)
## 步骤六：创建并初始化 TUI 组件库
1. **添加组件到需要使用 TUICallKit 的页面**，例如示例代码中的 `MiniProgram/pages/videoCall/videoCall.json`：
```javascript
// 可参考 MiniProgram/pages/videoCall/videoCall.json 或 MiniProgram/pages/audioCall/audioCall.json
{
    "usingComponents": {
        "TUICallKit": "/TUICallKit/TUICallKit"
    }
}
```
2. **在 WXML 模板 中添加一个 TUICallKit 组件**，例如示例代码中的 `MiniProgram/pages/videoCall/videoCall.wxml`：
```javascript
// 可参考 MiniProgram/pages/videoCall/videoCall.wxml 或 MiniProgram/pages/audioCall/audioCall.wxml
  <TUICallKit
    id="TUICallKit-component"
    config="{{config}}"
  ></TUICallKit>
```
3. **用 JS 代码动态设置 config 参数**
在 JS 逻辑交互例如 `pages/index/index.js` 中填写如下代码，用于设置 wxml 文件中的 {{config}} 变量。这部分工作可参考 `MiniProgram/pages/videoCall/videoCall.js` 或 `MiniProgram/pages/audioCall/audioCall.js` 中的示例代码，如下所示：
```javascript
// 引入 userSig 生成函数
import { genTestUserSig } from '../../debug/GenerateTestUserSig';
const userID = 'your userId';
const Signature = genTestUserSig(userID);
Page({
    /**
     * 页面的初始数据
     */
    data: {
        config: {
            sdkAppID: Signature.sdkAppID, // 替换为您自己账号下的 SDKAppId
            userID: userID,   // 填写当前用的 userID
            userSig: genTestUserSig(userID).userSig, // 通过 genTestUserSig(userID) 生成
            tim: null,   //  tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
        }
    }
})
```
这里详细介绍一下 config 中的几个参数：
	- **sdkAppID**：在步骤三中您已经获取到，这里不再赘述。
	- **userId**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。
	- **userSig**：使用步骤三中获取的 SecretKey 对 sdkAppID、userId 等信息进行加密，就可以得到 UserSig，它是一个鉴权用的票据，用于腾讯云识别当前用户是否能够使用 TRTC 的服务，更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。
4. **在生命周期函数中初始化 TUICallKit**
```javascript
onLoad() {
	const userID = 'your userId';
	const Signature = genTestUserSig(userID);
	const config = {
	sdkAppID: Signature.sdkAppID,
	userID: userID,
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
5. **生命周期函数中监听页面卸载**
```javascript
onUnload() {
	this.TUICallKit.destroyed();
},
```

[](id:step7)
## 步骤七：发起视频通话请求
在 JS 逻辑交互例如 `pages/index/index.js` 中填写如下代码，就可以实现一对一视频通话。
```javascript
// 发起1对1视频通话，假设被邀请人的userId为: 1111, type 1：语音通话，2：视频通话。
this.TUICallKit.call({ userID: '1111', type: 2 });
```


[](id:step8)
## 步骤八：更多特性
### 设置昵称&头像
如果您需要自定义昵称或头像，可以使用如下接口进行更新：
```javascript
this.TUICallKit.setSelfInfo("昵称", "头像 URL");
```
