
TUIKit 组件具备单人视频通话和语音通话功能，并且实现了小程序端和 Web 端、App 端全平台的互通。

## 环境准备
- 建议使用最新的 HBuilderX 编辑器 。
- iOS 9.0 或以上版本且支持音视频的 iOS 设备，暂不支持模拟器。
- Android 版本不低于 4.1 且支持音视频的 Android 设备，暂不支持模拟器。如果为真机，请开启**允许调试**选项。最低兼容 Android 4.1（SDK API Level 16），建议使用 Android 5.0 （SDK API Level 21）及以上版本。
- iOS/Android 设备已经连接到 Internet。

> ?
> - **2022年8月以后，TUIKit 组件升级了音视频通话功能，采用了全新的 TUICallKit，新版本音视频通话功能需要加购专属的 IM 音视频通话能力包后解锁**，具体购买方法请参考 [**步骤1：开通音视频服务**](#step1)，如已开通，则可忽略该步骤。

音视频通话界面如下图所示：

<table style="text-align:center;vertical-align:middle;width:1000px">
  <tr>
	  <th style="text-align:center;" width="500px">语音通话<br></th>
    <th style="text-align:center;" width="500px">视频通话<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b412c178178c0052254f4f800559d7d4.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6b2b6878e714e77e578e3c962659e36b.jpg" />     </td>
	 </tr>
</table>


## 操作步骤
### 步骤1：开通音视频通话能力

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 在页面的右下角找到**开通腾讯实时音视频服务**功能区。
   1. 若您需要体验音视频通话功能，可单击卡片内的 **免费体验** 开通 TUICallKit 的 7 天免费试用服务。
      ![image](https://qcloudimg.tencent-cloud.cn/raw/a7caebe5a773c93fb23d00b4488003b1.png)
   2. 您可参见 [音视频通话能力版本说明](https://cloud.tencent.com/document/product/269/84296#step2) 确认所需要使用的版本，单击 **[购买正式版](https://buy.cloud.tencent.com/avc)** 以购买正式的音视频通话能力。在购买页内的增值服务中勾选“音视频通话能力”，并选择所需版本即可。![](https://qcloudimg.tencent-cloud.cn/raw/c0d6f96d96a1d10a6422f143b620c94b.png)
      ![](https://qcloudimg.tencent-cloud.cn/raw/79e1c65b1cc44442b9f83ea2f62e7683.png)

[](id:step2)
### 步骤2：导入插件 
1. **购买 uni-app 原生插件**
登录 [uni 原生插件市场](https://ext.dcloud.net.cn/)，在  [TencentCloud-TUICallKit 插件](https://ext.dcloud.net.cn/plugin?id=9035) 详情页中购买（免费插件也可以在插件市场0元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
![](https://qcloudimg.tencent-cloud.cn/raw/d270d9298975ee829ae9c8c405530765.png)
2. 使用自定义基座打包 uni 原生插件 （**请使用真机运行自定义基座**）
使用 uni 原生插件必须先提交云端打包才能生效，购买插件后在应用的 `manifest.json` 页面的 **App原生插件配置** 项下单击**选择云端插件**，选择**腾讯云原生音视频插件**。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/TencentCloud-TUICallKit.png)
直接云端打包后无法打 log，无法排查问题，需要自定义基座调试原生插件。
>! 
>- 自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK。
>- 请尽量不要使用本地插件，插件包超过自定义基座的限制，可能导致调试收费。


[](id:step3)
### 步骤3：引入原生插件并登录
1. 在 App.vue 文件注册原生插件。
使用 uni.requireNativePlugin 在 App.vue 注册原生插件，参数为腾讯云原生音视频插件ID: `TencentCloud-TUICallKit`
```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
console.warn(TUICallKit, "TUICallKit ｜ ok"); // 本地日志
uni.$TUICallKit = TUICallKit; // 全局引入
```
2. App.vue 文件中， IM SDK 初始化之后完成登录。
```javascript
// sdk ready 以后可调用 API
handleSDKReady(event) {
 uni.$chat_isSDKReady = true;
 uni.hideLoading();
 // #ifdef APP-PLUS
 // TUICallKit login
 uni.$TUICallKit.login({
  SDKAppID: uni.$chat_SDKAppID, // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: uni.$chat_userID,     // 用户 ID，可以由您的帐号系统指定
  userSig: uni.$chat_userSig,   // 身份签名，相当于登录密码的作用
 }, (res) => {
  if (res.code === 0) {
  uni.showToast({
   title: "TUICallKit login",
  });
  uni.$TUICallKit.enableFloatWindow(true); // 开启小浮窗
  } else {
  console.error(`login failed, error message = ${res.msg}`);
  }
 });
 // #endif
},
```

> ?
> - 更多 TUICallKit API详情可参考文档 [TUICallKit-API](https://cloud.tencent.com/document/product/647/78732)。
> - TUIKit 组件目前仅支持 1v1 通话，如果您需要集成群通话功能，可参见   [TUICallKit-API](https://cloud.tencent.com/document/product/647/78732) 实现。

### 步骤4：本地调试和发布
 使用自定义基座开发调试 [TencentCloud-TUICallKit 插件](https://ext.dcloud.net.cn/plugin?id=9035) 后，不可直接将自定义基座 APK 作为正式版发布。
 需要重新提交云端打包（不能勾选“**自定义基座**”）生成正式版本。
 
### 步骤5：发起您的第一次通话
发起通话：
<img width="1015" src="https://qcloudimg.tencent-cloud.cn/raw/8ca0ca09d7ca8c06c23d3dda2a510abf.png"/>
收到通话：
<img width="1015" src="https://qcloudimg.tencent-cloud.cn/raw/ba26abfe4ba1c5f82303b2390dd197ab.png"/>

### 步骤6：离线推送
如果您需要集成离线推送，[uni-app 离线推送集成](https://cloud.tencent.com/document/product/269/79124) 文档。
配置完成后，当单击接收到的**音视频通话离线推送通知**时， TUICallKit 会自动拉起**音视频通话邀请界面**。


## 相关文档
- [TUICallkit  API（客户端） 文档](https://cloud.tencent.com/document/product/647/78732)
- [TUICallkit  API（小程序） 文档](https://cloud.tencent.com/document/product/647/78912)
- [TUIKit (uni-app)](https://cloud.tencent.com/document/product/269/64506)
- [小程序离线推送](https://cloud.tencent.com/document/product/269/79588)

## 交流与反馈
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">309869925</dx-tag-link>

<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-app-qq.png" width = "300"/>
