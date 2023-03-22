
## TUIKit 介绍

TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、关系链、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit  时只需关注自身业务或个性化扩展即可。
基于 React 开发的 TUIKit 界面风格更契合境外客户的使用习惯，而且支持国际化，如果您的业务有出海的需求，欢迎接入。

## Example App
我们构建了可供体验的在线 [demo](https://web.sdk.qcloud.com/im/demo/intl/index.html)，并将代码开源到了 github， [chat-uikit-react](https://github.com/TencentCloud/chat-uikit-react)。

Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/631e3dbdef2579c48d87e722a3a2e9ee.png)

## 开发环境要求
- React ≥ v18.0
- TypeScript
- node（12.13.0 ≤ node 版本 ≤ 17.0.0, 推荐使用 Node.js 官方 LTS 版本 16.17.0）
- npm（版本请与 node 版本匹配）

## 跑通demo

### 步骤1：下载源码
```
# Run the code in CLI
$ git clone https://github.com/TencentCloud/chat-uikit-react
# Go to the project  
$ cd chat-uikit-react
# Install dependencies of the demo and build chat-uikit-react
$ npm install && npm run build
$ cd examples/sample-chat && npm install
```

>! 项目 `examples/sample-chat` 下依赖的 `@tencentcloud/chat-uikit-react` 为本地包，因此需要在 `chat-uikit-react` 根目录下执行 `npm run build` 或者 `npm run start`，后者会启动 `npm run rollup -c -w` ， `examples/sample-chat` 项目会实时加载修改后的组件库，建议在需要自己开发修改组件库时使用。


### 步骤2：配置 demo
1. 打开 `examples/sample-chat` 项目，通过路径 `./examples/sample-chat/src/debug/GenerateTestUserSig.js` 找到 `GenerateTestUserSig.js` 文件。
2. 在 `GenerateTestUserSig.js` 文件中设置 `SDKAPPID` 和 `SECRETKEY` ，其值可以在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 中获取。 点击目标应用卡片，进入应用的基础配置页面，例如：
   <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/480455e5b4a2a1d4d67ffb2e445452a6.png"/>
3. 在 **图中所示** 区域，点击  **复制**，替换 `GenerateTestUserSig.js` 文件原有的 `SDKAPPID` 和 `SECRETKEY`。
>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试。**
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。
   [](id:2-4)
4. 进入应用的账号管理页面，创建账号并获取 userID，用于当作后续发送消息的测试用户。
   <img style="width:870px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c6e76f750f11023d13b01ba8c2279a0e.png"/>

### 步骤3：启动项目
```
# Launch the project
$ cd examples/sample-chat
$ npm run start
```

### 步骤4：发送您的第一条消息
1. 项目启动成功后，点击“+”图标，创建会话。
2. 在输入框中搜索另一个用户的 userID（参考：[步骤2.4](#2-4)）。
3. 点击用户头像发起会话。
4. 在输入框输入消息，按下"enter"键发送。
   ![](https://web.sdk.qcloud.com/im/demo/TUIkit/react-static/images/chat-English.gif)

### 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 常见问题

#### 什么是 UserSig？

UserSig 是用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文。

#### 如何生成 UserSig？

UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向项目的接口，在需要 UserSig 时由您的项目向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

> !本文示例代码采用的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通功能调试**。 正确的 UserSig 签发方式请参见上文。

## 相关文档

- [SDK API 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
