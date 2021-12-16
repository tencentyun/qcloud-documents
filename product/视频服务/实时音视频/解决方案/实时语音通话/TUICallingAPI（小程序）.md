## 组件介绍
TUICalling 小程序组件是基于腾讯云实时音视频（TRTC）和腾讯云信令 SDK（TSignalling）组合而成，支持1V1，多人场景下的语音通话。TUICalling 是一个开源组件，依赖闭源的信令 SDK（TSignalling）进行状态管理，通过 C2C 通信，完成信令传递。组件可快速服务线上客服，咨询，医疗问诊，跨端实时通话等应用场景。您可前往 [ **Github** ](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini/TRTCScenesDemo)或单击 [ **ZIP** ](https://web.sdk.qcloud.com/component/trtccalling/download/trtc-calling-miniapp.zip)，下载相关 SDK 及配套的 Demo 源码。
![](https://web.sdk.qcloud.com/component/trtccalling/doc/miniapp/6b1368e2186abcd5126fc1c165f2fb78.png)

## 环境要求
- 微信 App iOS 最低版本要求：7.0.9。
- 微信 App Android 最低版本要求：7.0.8。
- 小程序基础库最低版本要求：2.10.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，需要申请常规小程序账号进行开发。
- 不支持 uniapp 开发环境，请使用原生小程序开发环境。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在 **[微信公众平台](https://mp.weixin.qq.com)** > **开发** > **开发管理** > **接口设置** 中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)
 - **配置推流域名及 IM 域名**到小程序控制台 request 合法域名。

  因 TUICalling 使用 TSignalling（IM） 进行信令交互，涉及使用 [IM 的受信域名](https://web.sdk.qcloud.com/im/doc/zh-cn/tutorial-02-upgradeguideline.html)。

  ```js
  https://official.opensso.tencent-cloud.com
  https://yun.tim.qq.com
  https://cloud.tencent.com
  https://webim.tim.qq.com
  https://query.tencent-cloud.com
  wss://wss.im.qcloud.com
  wss://wss.tim.qq.com
  https://web.sdk.qcloud.com
  ```

 - 不支持 uniapp、taro 开发环境，请使用原生小程序开发环境。

## 支持平台

| 微信小程序 | QQ小程序 |
| ---------- | -------- |
| ✓          | ✓        |

## 支持框架

TUICalling 为原生小程序组件。支持原生开发或支持嵌入原生组件的框架。

## 支持场景

TUICalling是基于腾讯云实时音视频（TRTC）和腾讯云信令 SDK（TSignalling）组合而成。**支持1V1，多人场景下的音视频通话**。如：线上客服，咨询，医疗问诊，跨端实时通话等应用场景。不支持涉及屏幕分享的业务。如：直播、会议等。

## 目录结构

```
TUICalling
├─ component        // UI 组件
    ├─ calling      // 呼叫中 UI 组件
    └─ connected    // 通话中 UI 组件
├─ static         // UI icon 图片
├─ TRTCCalling    // TRTCCalling 逻辑文件
```

## TUICalling API 概览
### 邀请方函数

| API | 描述 |
|---------|---------|
|[call({userID, type})](#call)|发出 C2C 通话邀请。|
|[groupCall({userIDList, type, groupID})](#groupCall)|群组邀请通话（请先 [创建 IM 群组](https://cloud.tencent.com/document/product/269/37459)）。|

### 通用功能函数
| API | 描述 |
|---------|---------|
|[init()](#init) | 初始化TUICalling，初始化完成后可以进行通讯。 |
|[destroyed()](#destroyed)|销毁 TUICalling。|

## 属性表

### &lt;TUICalling&gt; 属性

| 属性                 | 类型    | 默认值 | 必填 | 说明                                                         |
| -------------------- | ------- | ------ | ---- | ------------------------------------------------------------ |
| id                   | String  |        | 是   | 绑定 TUICalling 的 dom ID，可通过 this.selectComponent(ID) 获取实例。 |
| config               | Object  |        | 是   | TUICalling 初始化配置。                                        |

#### config 参数

| 参数     | 类型   | 必填 | 说明                                                         |
| -------- | ------ | ---- | ------------------------------------------------------------ |
| sdkAppID | Number | 是   | 开通实时音视频服务创建应用后分配的 [SDKAppID](https://console.cloud.tencent.com/trtc/app)。 |
| userID   | String | 是   | 用户 ID，可以由您的帐号体系指定。                            |
| userSig  | String | 是   | 身份签名（即相当于登录密码），由 userID 计算得出，具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| type     | Number | 是   | 指定通话类型。1：语音通话，2：视频通话。                     |
| tim     | Object | 否   | tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性。                     |

**示例代码：**

```html
// index.wxml
<TUICalling id="TUICalling-room" config="{{tuiConfig}}"></TUICalling>
```

```javascript
tuiConfig = {
  sdkAppID: 0, // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: 'test_user_001', // 用户 ID，可以由您的帐号系统指定
  userSig: 'xxxxxxxxxxxx', // 身份签名，相当于登录密码的作用
  type: 1, // 通话模式
  tim: null, // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
}
```

### 组件方法
[](id:selectComponent)
#### selectComponent()
您可以通过小程序提供的 `this.selectComponent()` 方法获取组件实例。
```javascript
let TUICallingContext = this.selectComponent('#TUICalling-room')
```

[](id:init)
#### init()
初始化 TUICalling，会建议在页面 onLoad 阶段调用。

```javascript
TUICallingContext.init()
```

[](id:destroyed)
#### destroyed()
销毁 TUICalling，会建议在页面 onUnload 阶段调用。
```javascript
TUICallingContext.destroyed()
```

[](id:call)
#### call({userID, type})
进行某个 user 进行呼叫。

| 参数 | 含义 | 
|---------|---------|
| userID | 希望呼叫用户的 userID。 | 
| type | 通话类型，type = 1：语音通话，type =2：视频通话。 | 

```javascript
let userID = 'test'
let type = 1
TUICallingContext.call({userID, type})
```

[](id:groupCall)
#### groupCall({userIDList, type, groupID})

在调用该接口前需要使用 IM [创建群组](https://cloud.tencent.com/document/product/269/37459)，并将 groupID 作为参数传入。

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIDList | Arrary | 拨打的用户列表 |
|type|Number|type 为通话类型，1：语音通话，2：视频通话。|
|groupID|String| IM 群组的 groupID。|

```javascript
TUICallingContext.groupCall({userIDList, type, groupID})
```
[](id:accept)


## 常见问题
#### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认账号登入的唯一性。

- 多实例：一个 userID 重复登入，或在不同端登入，将会引起信令的混乱。 
- 离线推送：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。即，小程序在后台与离线状态下，无法收到呼入提醒或来电提醒。

更多常见问题，请参见 [小程序端相关问题](https://cloud.tencent.com/document/product/647/45532)。

### 技术咨询

了解更多详情您可以 QQ 咨询：646165204 技术支持

### 参考文档
[TUICalling 组件源码](https://github.com/tencentyun/TUICalling/tree/main/MiniProgram)
[TUICalling demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini/TRTCScenesDemo/trtc-calling-miniapp)
[小程序端相关问题](https://cloud.tencent.com/document/product/647/45532)