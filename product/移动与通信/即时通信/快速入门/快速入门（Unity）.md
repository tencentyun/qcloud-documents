[](id:toc)
通过阅读本文，您可以了解集成 Unity SDK 的方法。

## 环境要求

| 环境  | 版本 |
|---------|---------|
| Unity | 2019.4.15f1 及以上版本。|
|Android| Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS| Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 支持平台

我们致力于打造一套支持 Unity 全平台的即时通信 IM SDK ，帮助您一套代码，全平台运行。

| 平台 | IM SDK |
|---------|---------|
| iOS | 支持 |
| Android | 支持 |
| macOS | 支持 |
| Windows | 支持 |
| [Web](#web) | 支持，1.8.1+版本起 |

>? Web 平台需要简单的几步额外引入，详情请查看本文 [第五部分](#web)。

## 前提条件

1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参照 [创建并升级应用](https://cloud.tencent.com/document/product/269/32577) 创建应用，并记录好 `SDKAppID`。

[](id:part1)

## 第一部分：创建测试用户

在 [IM 控制台](https://console.cloud.tencent.com/im) 选择您的应用，在左侧导航栏依次单击 **辅助工具** > **UserSig 生成&校验** ，创建两个 UserID 及其对应的 UserSig，复制`UserID`、`签名（Key）`、`UserSig`这三个，后续登录时会用到。

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是由服务器端生成，并提供面向 App 的接口，在需要 `UserSig` 时由 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:part2)

## 第二部分：集成 IM SDK 进您的 Unity 项目

1. 通过 Unity，创建一个 Unity 项目，并记住项目所在的位置。
![](https://qcloudimg.tencent-cloud.cn/raw/f07ae1bb4db4ca5f43f6acc563aafa8c.png)
或打开一个已有 Unity 项目。
2. 通过 IDE（如：Visual Studio Code）打开项目：
![](https://qcloudimg.tencent-cloud.cn/raw/881d625bf3ee2e736db22762e8763c18.png)
3. 根据目录，找到 Packages/manifest.json，并修改依赖如下：
```json
   {
     "dependencies":{
       "com.tencent.imsdk.unity":"https://github.com/TencentCloud/chat-sdk-unity.git#unity"
     }
   }
```

为帮助您更好的理解 IM SDK 的各 API，我们还提供了 [API Example](https://github.com/TencentCloud/tc-chat-sdk-unity/tree/main/Assets/IM_Api_Example)，演示各 API 的调用及监听的触发。

[](id:part3)

## 第三部分：加载依赖

在 Unity Editor 中打开项目，等候依赖加载完毕，确认Tencent Cloud IM 已经加载完成。
![](https://qcloudimg.tencent-cloud.cn/raw/d98dfb17bbee6c0319e370de6f2ba9dd.jpg)

[](id:part4)

## 第四部分：自实现 UI 集成

### 前提条件

您已经完成创建 Unity 项目，或有可以基于的 Unity 项目，并加载了 Tencent Cloud IM SDK。

### 完成 SDK 初始化

[本节详细文档](https://cloud.tencent.com/document/product/269/76653)

调用`TencentIMSDK.Init`，完成 SDK 初始化。

将您的 `SDKAppID` 传入。

```c#
public static void Init() {
  int SDKAppID = 0; // 从即时通信 IM 控制台获取应用 SDKAppID。
  SdkConfig sdkConfig = new SdkConfig();

  sdkConfig.sdk_config_config_file_path = Application.persistentDataPath + "/TIM-Config";

  sdkConfig.sdk_config_log_file_path = Application.persistentDataPath + "/TIM-Log";

  TIMResult res = TencentIMSDK.Init(long.Parse(SDKAppID), sdkConfig);
}
```

在`Init`后，您可以针对 IM SDK 挂载一些监听，主要包括网络状态及用户信息变更等，详情可参见 [该文档](https://cloud.tencent.com/document/product/269/76653)。

### 登录测试账户

[本节详细文档](https://cloud.tencent.com/document/product/269/76654)

此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证。

调用`TencentIMSDK.Login`方法，登录一个测试账户。

当返回值`res.code`为0时，登录成功。

```c#
public static void Login() {
  if (userid == "" || user_sig == "")
  {
      return;
  }
  TIMResult res = TencentIMSDK.Login(userid, user_sig, (int code, string desc, string json_param, string user_data)=>{
    // 处理登陆回调逻辑
  });
}
```

>? 该账户仅限开发测试使用。应用上线前，正确的 `UserSig` 签发方式是将 `UserSig` 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 `UserSig` 时由您的 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

### 发送消息

[本节详细文档](https://cloud.tencent.com/document/product/269/76656)

此处以发送文本消息举例

代码示例：

```c#
public static void MsgSendMessage() {
        string conv_id = ""; // c2c 消息会话 ID 为 userID，群消息会话 ID 为 groupID
        Message message = new Message
        {
          message_conv_id = conv_id,
          message_conv_type = TIMConvType.kTIMConv_C2C, // 群消息为TIMConvType.kTIMConv_Group
          message_elem_array = new List<Elem>
          {
            new Elem
            {
              elem_type = TIMElemType.kTIMElem_Text,
              text_elem_content =  "这是一个普通文本消息"
            }
          }
        };
        StringBuilder messageId = new StringBuilder(128);

        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc,                         string json_param, string user_data)=>{
          // 消息发送异步结果
        });
              // 消息发送同步返回的消息ID messageId
}
```

>?如果发送失败，可能是由于您的 SDKAppID 不支持陌生人发送消息，您可至控制台开启，用于测试。
>
> [请单击此链接](https://console.cloud.tencent.com/im/login-message)，关闭好友关系链检查。

### 获取会话列表

[本节详细文档](https://cloud.tencent.com/document/product/269/76673)

在上一个步骤中，完成发送测试消息，现在可登录另一个测试账户，拉取会话列表。

获取会话列表的方式有两种：

1. 监听长连接回调，实时更新会话列表。
2. 请求 API，根据分页一次性获取会话列表。

常见应用场景为：

在启动应用程序后立即获取会话列表，然后监听长连接以实时更新会话列表的变化。

#### 一次性请求会话列表

```c#
TIMResult res = TencentIMSDK.ConvGetConvList((int code, string desc, List<ConvInfo> info_list, string user_data)=>{
 // 处理异步逻辑
});
```

此时，您可以看到您在上一步中，使用另一个测试账号，发来消息的会话。

#### 监听长链接实时获取会话列表

您在此步骤中，需要先在 SDK 上挂载监听，然后处理回调事件，更新 UI。

1. 挂载监听。
```c#
TencentIMSDK.SetConvEventCallback((TIMConvEvent conv_event, List<ConvInfo> conv_list, string user_data)=>{
 // 处理回调逻辑
});
```
2. 处理回调事件，将最新的会话列表展示在界面上。

### 接收消息

[本节详细文档](https://cloud.tencent.com/document/product/269/76657)

通过腾讯云 IM SDK 接收消息有两种方式：

1. 监听长连接回调，实时获取消息变化，更新渲染历史消息列表。
2. 请求 API，根据分页一次性获取历史消息。

常见应用场景为：

1. 界面进入新的会话后，首先一次性请求一定数量的历史消息，用于展示历史消息列表。
2. 监听长链接，实时接收新的消息，将其添加进历史消息列表中。

#### 一次性请求历史消息列表

每页拉取的消息数量不能太大，否则会影响拉取速度。建议此处设置为20左右。

您应该动态记录当前页数，用于下一轮请求。

示例代码如下：

```c#
// 拉取单聊历史消息
// 首次拉取，msg_getmsglist_param_last_msg 设置为 null
// 再次拉取时，msg_getmsglist_param_last_msg 可以使用返回的消息列表中的最后一条消息
var get_message_list_param = new MsgGetMsgListParam
    {
      msg_getmsglist_param_last_msg = LastMessage
    };
TIMResult res = TencentIMSDK.MsgGetMsgList(conv_id, TIMConvType.kTIMConv_C2C, get_message_list_param, (int code, string desc, string user_data) => {
  // 处理回调逻辑
});
```

```c#
// 拉取群聊历史消息
// 首次拉取，msg_getmsglist_param_last_msg 设置为 null
// 再次拉取时，msg_getmsglist_param_last_msg 可以使用返回的消息列表中的最后一条消息
var get_message_list_param = new MsgGetMsgListParam
    {
      msg_getmsglist_param_last_msg = LastMessage
    };
TIMResult res = TencentIMSDK.MsgGetMsgList(conv_id, TIMConvType.kTIMConv_Group, get_message_list_param, (int code, string desc, string user_data) => {
  // 处理回调逻辑
});
```

#### 监听长链接实时获取新消息

历史消息列表初始化后，新消息来自长链接 `TencentIMSDK.AddRecvNewMsgCallback`。

`AddRecvNewMsgCallback`回调被触发后，您可以按需将新消息添加进历史消息列表中。

绑定监听器示例代码如下：

```c#
TencentIMSDK.AddRecvNewMsgCallback((List<Message> message, string user_data) => {
  // 处理新消息
});
```

此时，您已基本完成 IM 模块开发，可以发送接收消息，也可以进入不同的会话。

您可以继续完成 [群组](https://cloud.tencent.com/document/product/269/75697)，[用户资料](https://cloud.tencent.com/document/product/269/76686)，[关系链](https://cloud.tencent.com/document/product/269/76687)，[本地搜索](https://cloud.tencent.com/document/product/269/76690) 等相关功能开发。

详情可查看 [自实现 UI 集成 SDK 文档](https://cloud.tencent.com/document/product/269/75260)。

[](id:part5)

## 第五部分：#Unity for WebGL 支持[](id:web)

Tencent Cloud IM SDK (Unity 版本) 自 `1.8.1` 版本起支持构建 WebGL。

相比 Android 和 iOS 端，需要一些额外步骤。如下：

### 引入 JS

从 GitHub 下载下方三个JS文件，放置于项目构建 WebGL 产物的文件夹内。

- [tim-js](https://github.com/TencentCloud/TIMSDK/blob/master/Web/IMSDK/tim-js.js)
- [tim-js-friendship.js](https://github.com/TencentCloud/TIMSDK/blob/master/Web/IMSDK/tim-js-friendship.js)
- [将此文件重命名成 tim-upload-plugin.js](https://github.com/TencentCloud/TIMSDK/blob/master/Web/IMSDK/tim-upload-plugin/index.js)
打开 `index.html` ，并引入这三个JS文件。如下：

```html
<script src="./tim-js.js"></script>
<script src="./tim-js-friendship.js"></script>
<script src="./tim-upload-plugin.js"></script>
```

## 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 常见问题

#### 支持哪些平台？

目前支持 iOS、Android、Windows Mac 和 WebGL。

#### Android 单击 Build And Run 报错找不到可用设备？

确保设备没被其他资源占用，或单击 Build 生成 apk 包，再拖动进模拟器里运行。

#### iOS 第一次运行报错？

按照上面的 Demo 运行配置后，如果报错，可以单击**Product**>**Clean**，清除产物后重新 Build，或者关闭 Xcode 重新打开再次 Build。

#### 2019.04版 Unity，iOS 平台报错？

Library/PackageCache/com.unity.collab-proxy@1.3.9/Editor/UserInterface/Bootstrap.cs(23,20): error CS0117: 'Collab' does not contain a definition for 'ShowChangesWindow'
在 Editor 工具栏单击**Window**>**Package Manager**，将 Unity Collaborate 降级到1.2.16。

#### 2019.04版 Unity，iOS 平台报错？

Library/PackageCache/com.unity.textmeshpro@3.0.1/Scripts/Editor/TMP_PackageUtilities.cs(453,84): error CS0103: The name 'VersionControlSettings' does not exist in the current context
打开源码，把`|| VersionControlSettings.mode != "Visible Meta Files"`这部分代码删除即可。

#### 错误码如何查询？

- IM SDK 的 API 层面错误码，请查看 [该文档](https://cloud.tencent.com/document/product/269/1671)。

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：764231117 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/26c9444af94d60e1c606f94cda7cff9d.png)
