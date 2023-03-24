本文主要介绍如何快速运行腾讯云即时通信 IM Demo（React Native）。

## 环境要求

|              | 版本                                                                 |
| ------------ | -------------------------------------------------------------------- |
| React Native | 0.63.4 版本以上                                                      |
| Android      | Android Studio 3.5 及以上版本，App 要求 Android 4.1 及以上版本设备。 |
| iOS          | Xcode 11.0 及以上版本，请确保您的项目已设置有效的开发者签名。        |

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 第一部分：创建测试用户

在 [IM 控制台](https://console.cloud.tencent.com/im) 选择您的应用，在左侧导航栏依次点击 **辅助工具**->**UserSig 生成&校验** ，创建两个 UserID 及其对应的 UserSig，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。

> ? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:part2)

## 第二部分：集成 React Native SDK

### 前提条件

您已经完成创建 React Native 项目，或有可以基于的 React Native 项目。

### 接入步骤

#### 安装 IM SDK
使用如下命令，安装 React Naitve IM SDK 最新版本。在命令行执行：
```shell
// npm
npm install react-native-tim-js

// yarn
yarn add react-native-tim-js
```

#### 完成 SDK 初始化
调用`initSDK`，完成 SDK 初始化。将您的 `sdkAppID` 传入。
```javascript
import { TencentImSDKPlugin, LogLevelEnum } from 'react-native-tim-js';

TencentImSDKPlugin.v2TIMManager.initSDK(
    sdkAppID: 0, // Replace 0 with the SDKAppID of your IM application when integrating
    loglevel: LogLevelEnum.V2TIM_LOG_DEBUG, // Log
    listener: V2TimSDKListener(),
);
```

在本步骤，您可以针对 IM SDK 挂载一些监听，主要包括网络状态及用户信息变更等，详情可参见 [该文档](https://comm.qq.com/im/doc/RN/zh/Interface/Listener/V2TimSDKListener.html)。

#### 登录测试账户
1. 此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证。
2. 调用`TencentImSDKPlugin.v2TIMManager.login`方法，登录一个测试账户。当返回值`res.code`为 0 时，登录成功。
```javascript
import { TencentImSDKPlugin } from 'react-native-tim-js';
 const res = await TencentImSDKPlugin.v2TIMManager.login(
    userID: userID,
    userSig: userSig,
  );
```
> ? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是将 `UserSig` 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 `UserSig` 时由您的 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

#### 发送消息

此处以发送文本消息举例，其流程为：
1. 调用 `createTextMessage(String)`创建一个文本消息。
2. 根据其返回值，拿到消息 ID。
3. 调用 `sendMessage()` 发送该 ID 的消息。`receiver`可填入您此前创建的另一个测试账户 ID。发送单聊消息无需填入`groupID`。

代码示例：

```javascript
import { TencentImSDKPlugin } from 'react-native-tim-js';

const createMessage =
      await TencentImSDKPlugin.v2TIMManager
          .getMessageManager()
          .createTextMessage("The text to create");

const id = createMessage.data!.id!; // The message creation ID

const res = await TencentImSDKPlugin.v2TIMManager
      .getMessageManager()
      .sendMessage(
          id: id, // Pass in the message creation ID to
          receiver: "The userID of the destination user",
          groupID: "The groupID of the destination group",
          );
```

> ?如果发送失败，可能是由于您的 sdkAppID 不支持陌生人发送消息，您可至控制台开启，用于测试。
>
> [请单击此链接](https://console.cloud.tencent.com/im/login-message)，关闭好友关系链检查。

#### 获取会话列表

在上一个步骤中，完成发送测试消息，现在可登录另一个测试账户，拉取会话列表。

<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e2fdd7632ebc0c5cde68c91afa914201.jpg" />

获取会话列表的方式有两种：

1. 监听长连接回调，实时更新会话列表。
2. 请求 API，根据分页一次性获取会话列表。

常见应用场景为：

在启动应用程序后立即获取会话列表，然后监听长连接以实时更新会话列表的变化。

##### 一次性请求会话列表

为了获取会话列表，需要维护`nextSeq`，记录当前位置。

```typescript
import { useState } from "react";
import { TencentImSDKPlugin } from "react-native-tim-js";

const [nextSeq, setNextSeq] = useState<string>("0");

const getConversationList = async () => {
  const count = 10;
  const res = await TencentImSDKPlugin.v2TIMManager
    .getConversationManager()
    .getConversationList(count, nextSeq);
  setNextSeq(res.data?.nextSeq ?? "0");
};
```

此时，您可以看到您在上一步中，使用另一个测试账号，发来消息的会话。

##### 监听长链接实时获取会话列表

您在此步骤中，需要先在 SDK 上挂载监听，然后处理回调事件，更新 UI。

1. 挂载监听。
```javascript
import { TencentImSDKPlugin } from "react-native-tim-js";

const addConversationListener = () => {
  TencentImSDKPlugin.v2TIMManager
    .getConversationManager()
    .addConversationListener({
      onNewConversation: (conversationList) => {
        // new conversation created callback
        _onConversationListChanged(conversationList);
      },
      onConversationChanged: (conversationList) => {
        // conversation changed callback
        _onConversationListChanged(conversationList);
      },
    });
};
```

2. 处理回调事件，将最新的会话列表展示在界面上。
```javascript
const _onConversationListChanged = (list) => {
  // you can use conversation list to update UI
};
```

#### 接收消息

通过腾讯云 IM React Native SDK 接收消息有两种方式：

1. 监听长连接回调，实时获取消息变化，更新渲染历史消息列表。
2. 请求 API，根据分页一次性获取历史消息。

常见应用场景为：

1. 界面进入新的会话后，首先一次性请求一定数量的历史消息，用于展示历史消息列表。
2. 监听长链接，实时接收新的消息，将其添加进历史消息列表中。

##### 一次性请求历史消息列表

每页拉取的消息数量不能太大，否则会影响拉取速度。建议此处设置为 20 左右。

您应该动态记录当前页数，用于下一轮请求。

示例代码如下：

```javascript
import { TencentImSDKPlugin } from "react-native-tim-js";

const getGroupHistoryMessageList = async () => {
  const groupID = "";
  const count = 20;
  const lastMsgID = "";
  const res = await TencentImSDKPlugin.v2TIMManager
    .getMessageManager()
    .getGroupHistoryMessageList(groupID, count, lastMsgID);
  const msgList = res.data ?? [];
  // here you can use msgList to render your message list
};
```

##### 监听长链接实时获取新消息

历史消息列表初始化后，新消息来自长链接 `V2TimAdvancedMsgListener.onRecvNewMessage`。

`onRecvNewMessage`回调被触发后，您可以按需将新消息添加进历史消息列表中。

绑定监听器示例代码如下：

```javascript
import { TencentImSDKPlugin } from "react-native-tim-js";

const adVancesMsgListener = {
  onRecvNewMessage: (newMsg) => {
    _onReceiveNewMsg(newMsg);
    /// ... other listeners related to message
  },
};

const addAdvancedMsgListener = () => {
  TencentImSDKPlugin.v2TIMManager
    .getMessageManager()
    .addAdvancedMsgListener(adVancesMsgListener);
};
```

此时，您已基本完成 IM 模块开发，可以发送接收消息，也可以进入不同的会话。
您可以继续完成群组，用户资料，关系链，离线推送，本地搜索等相关功能开发，详情可参见 [SDK API 文档](https://comm.qq.com/im/doc/RN/zh/)。

### 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 常见问题

#### 运行 demo 时出现 `Undefined symbols for architecture x86_64 [duplicate]` 如何解决？

请参见 [文档](https://stackoverflow.com/questions/71933392/react-native-ios-undefined-symbols-for-architecture-x86-64)。

#### 运行 demo 时出现 `Failed to resolve: react-native-0.71.0-rc.0-debug` 如何解决？

请参见 [文档](https://blog.csdn.net/weixin_44132277/article/details/127731985)。

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：437955475 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/095e39d0943d3670585659251c5a3b6d.png)

