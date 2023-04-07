本文主要介绍如何快速运行腾讯云即时通信 IM Demo（Electron）并了解集成 Electron SDK 的方法。

## 环境要求

| 平台     | 版本                |
| -------- | ------------------- |
| Electron | 13.1.5 及以上版本。 |
| Node.js  | v14.2.0             |

## 支持平台

目前支持 Macos 和 Windows 两个平台。

## 体验 DEMO

在开始接入前，您可以体验我们的 [DEMO](https://cloud.tencent.com/document/product/269/36852) ，快速了解腾讯云 IM Electron SDK。

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)

### 步骤1：创建应用

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
  > ?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
  > 同一个腾讯云账号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)
3. 请保存 SDKAppID 信息。可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、标签、创建时间以及到期时间。
   ![](https://main.qcloudimg.com/raw/ed34d9294a485d8d06b3bb7e0cc5ae59.png)
4. 单击创建后的应用，左侧导航栏单击**辅助工具** > **UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，后续登录使用。
  ![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:step2)

### 步骤2：选择适合的方法集成 Electron SDK

IM 提供了两种方式来即成，您可以选择最合适的方案来即成：

| 继承方式  | 适用场景                                                                                                                                                                |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 使用 DEMO | IM Demo包含完整的聊天功能，代码已开源，如果您需要实现聊天类似场景，可以使用 Demo进行二次开发。可立即体验 [Demo](https://cloud.tencent.com/document/product/269/36852)。 |
| 自实现    | 如果 Demo 不能满足您应用的功能界面需求，可以使用该方法。                                                                                                                |

为帮助您更好的理解 IM SDK 的各 API，我们还提供了 [API 文档](https://comm.qq.com/im/doc/electron/zh/)。

[](id:step3)

### 步骤3：使用 Demo

1. 克隆即时通信 IM Electron Demo 源码到本地。
  ```javascript
  git clone https://github.com/TencentCloud/tc-chat-demo-electron.git
  ```
2. 安装项目依赖。
  ```javascript
  // 项目根目录
  npm install

  // 渲染进程目录
  cd src/client
  npm install
  ```
3. 项目运行。
```javascript
// 项目根目录
npm start
```
4. 项目打包。
  ```javascript
  // mac打包
  npm run build:mac
  // windows打包
  npm run build:windows
  ```

>? demo 中主进程的目录为`src/app/main.js`，渲染进程目录为`src/client`。如运行过程出现问题，可优先通过常见问题查找解决。

[](id:step4)

### 步骤4：自实现

**安装 Electron SDK**
使用如下命令，安装 Electron SDK最新版本
在命令行执行：

```
npm install im_electron_sdk
```

**完成 SDK 初始化**

1. 在`TimMain`中传入您的`sdkAppID`。
```javascript
// 主进程
const TimMain = require('im_electron_sdk/dist/main')

const sdkappid = 0;// 可以去腾讯云即时通信IM控制台申请
const tim = new TimMain({
  sdkappid:sdkappid
})
```
2. 调用`TIMInit`，完成 SDK 初始化。
```javascript
//渲染进程
const TimRender = require('im_electron_sdk/dist/render')
const timRender = new TimRender();
// 初始化
timRender.TIMInit()
```
3. 登录测试用户。
此时，您可以使用最开始的时候，在控制台申城的测试账户，完成登录验证。
调用`timRender.TIMLogin`方法，登录一个测试用户。
当返回值 `code`为0时，登录成功。
```javascript
const TimRender = require('im_electron_sdk/dist/render')
const timRender = new TimRender();
let {code} = await timRender.TIMLogin({
  userID:"userID",
  userSig:"userSig" // 参考userSig生成
})
```

>? 该账户仅限开发测试使用，应用上线前，正确的`UserSig` 签发方式是将`UserSig`的计算代码集成到您的服务端，并提供面向 APP的接口。在需要 `UserSig`时由您的 APP 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

**发送信息**
此处以发送文本消息距离，`code`返回 0 则为消息发送成功。
代码示例：

```javascript
const TimRender = require('im_electron_sdk/dist/render')
const timRender = new TimRender();
let param:MsgSendMessageParamsV2 = {    // param of TIMMsgSendMessage
    conv_id: "conv_id",
    conv_type: 1,
    params: {
        message_elem_array: [{
            elem_type: 1,
            text_elem_content:'Hello Tencent!',

        }],
        message_sender: "senderID",
    },
    callback: (data) => {}
  }
let {code} = await timRender.TIMMsgSendMessageV2(param);
```

>? 如果发送失败，可能是由于您的 sdkAppID 不支持陌生人发送消息，您可至控制台开启，用于测试。[请点击此链接](https://console.cloud.tencent.com/im/login-message)，关闭好友关系链检查。

**获取会话列表**
在上一个步骤中，完成发送测试消息，现在可登录另一个测试账户，拉取会话列表。
常见应用场景为：
在启动应用程序后立即获取会话列表，然后监听长链接以实时更新会话列表的变化。

```javascript
let param:getConvList = {
            userData:userData,
        }
let data:commonResult<convInfo[]> = await timRenderInstance.TIMConvGetConvList(param)
```

此时，您可以看到您在上一步中，使用另一个测试账号发来的消息的会话。

**接收消息**
常见应用场景为：

1. 界面进入新的会话后，首先一次性请求一定数量的历史消息，用于展示历史消息列表。
2. 监听长链接，实时接收新的消息，将其添加进历史消息列表中。

一次性请求历史消息列表

```javascript
let param:MsgGetMsgListParams = {
        conv_id: conv_id,
        conv_type: conv_type,
        params: {
            msg_getmsglist_param_last_msg: msg,
            msg_getmsglist_param_count: 20,
            msg_getmsglist_param_is_remble: true,
        },
        user_data: user_data
    }
    let msgList:commonResult<Json_value_msg[]> = await timRenderInstance.TIMMsgGetMsgList(param);
```

监听实时获取新消息
绑定 callback 示例代码如下：

```javascript
let param : TIMRecvNewMsgCallbackParams = {
            callback: (...args)=>{},
            user_data: user_data
        }
timRenderInstance.TIMAddRecvNewMsgCallback(param);
```

此时，您已基本完成 IM 模块开发，可以发送接收消息，也可以进入不同的会话。
您可以继续完成 群组，用户资料，关系链，离线推送，本地搜索 等相关功能开发。
详情可查看 [API 文档](https://comm.qq.com/im/doc/electron/zh/Callback/readme.html)。

### 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。



## 常见问题

#### 支持哪些平台？

目前支持 Macos 和 Windows 两个平台。

#### 错误码如何查询？

IM SDK 的 API 层面错误码，请查看 [错误码](https://cloud.tencent.com/document/product/269/1671)。

#### 安装开发环境问题，出现 `npm ERR! gyp ERR! stack TypeError: Cannot assign to read only property 'cflags' of object '#<Object>'` 错误如何解决？

请降低 node 版本，建议使用16.18.1。

#### 安装开发环境问题，出现 `gypgyp ERR!ERR` 错误如何解决？

请参见 [gypgyp ERR!ERR!](https://stackoverflow.com/questions/57879150/how-can-i-solve-error-gypgyp-errerr-find-vsfind-vs-msvs-version-not-set-from-c)。

#### 执行 `npm install` 出现错误 `npm ERR! Fix the upstream dependency conflict, or retry`，如何解决？

npmV7之前的版本遇到依赖冲突会忽视依赖冲突，继续进行安装
npmV7版本开始不会自动进行忽略，需要用户手动输入命令
请执行以下命令：
<dx-codeblock>
:::  sh
npm install --force
:::
</dx-codeblock>


#### 执行 `npm run start` 出现错误 `Error: error:0308010C:digital envelope routines::unsupported`，如何解决？

请降低node版本，建议使用16.18.1。

#### Mac 端 Demo 执行 `npm run start` 会出现白屏，如何解决？

Mac 端执行`npm run start` 会出现白屏，原因是渲染进程的代码还没有 build 完成，主进程打开的3000端口为空页面，当渲染进程代码 build 完成重新刷新窗口后即可解决问题。或者执行`cd src/client && npm run dev:react`, `npm run dev:electron`, 分开启动渲染进程和主进程。

#### `vue-cli-plugin-electron-builder` 构建的项目如何使用 `native modules`?

使用`vue-cli-plugin-electron-builder` 构建的项目使用`native modules` 请参见 [No native build was found for platform = xxx](https://github.com/nklayman/vue-cli-plugin-electron-builder/issues/1492)。

#### 用 `webpack` 构建的项目如何使用 `native modules`?

自己使用webpack 构建的项目使用native modules 请参见 [Windows 下常见问题](https://blog.csdn.net/Yoryky/article/details/106780254)。

#### 出现 `Dynamic Linking Error`?

Dynamic Linking Error. electron-builder 配置

``` javascript
   extraFiles:[
    {
      "from": "./node_modules/im_electron_sdk/lib/",
      "to": "./Resources",
      "filter": [
        "**/*"
      ]
    }
  ]
```

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：753897823 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/dbf4d02c6229db536d9ad018c91f8bf0.png)
