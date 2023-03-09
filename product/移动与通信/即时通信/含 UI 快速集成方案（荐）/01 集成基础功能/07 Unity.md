


## 简介

`Tencent Cloud IM Unity UIKit` 是基于 [Tencent Cloud IM Chat SDK](https://github.com/TencentCloud/chat-sdk-unity) 实现的游戏场景业务 UI 组件库。目前包含了`会话 (Conversation)`和`聊天 (Chat)`组件，收发文字消息、收发表情包消息、自定义表情包等功能。
![](https://qcloudimg.tencent-cloud.cn/raw/16b6b41518e46ca431e7384014810980.png)

## 快速开始

### 前置条件

- 已 [注册](https://www.tencentcloud.com/zh/document/product/378/17985) 腾讯云账号并完成 [身份验证](https://www.tencentcloud.com/zh/document/product/378/3629)。
- 参见 [创建并升级应用](https://www.tencentcloud.com/zh/document/product/1047/34577) 创建应用，并记录好 `SDKAppID`。
- 在 [IM 控制台](https://console.tencentcloud.com/im) 选择您的应用，在左侧导航栏依次点击 辅助工具 > UserSig 生成&校验 ，创建 UserID 及其对应的 `UserSig`，复制`UserID`、`签名（Key）`、`UserSig` 这三个，后续登录时会用到。

### 导入 Package

- 创建/启动已存在的 Unity 项目。
- 在 `Packages/manifest.json` 文件中的 dependencies 下添加：
    ```json
      {
        "dependencies":{
          "com.tencent.imsdk.unity":"https://github.com/TencentCloud/chat-sdk-unity.git#unity"
        }
      }
    ```
- 下载 [项目](https://github.com/TencentCloud/chat-uikit-unity) 目录下的 `chat-uikit-unity.unitypackage`，并导入资源包。

### 步骤1：初始化并登录 IM

初始化并登录 IM 有两种方式:

- **组件外部**: 整个应用初始化并登录一次即可。
- **组件内部**: 通过配置的方式将参数传入组件内部。建议您使用内部登录，UIKit 已帮您绑定了相应的事件回调，包括接收新消息的事件以及会话列表更新的事件。

#### 组件外部

在您创建的 Unity 项目中初始化 IM, 注意 IM 应用只需初始化一次即可。如若在现有 IM 项目中集成可跳过该步骤。

```c#
public static void Init() {
        int sdkappid = 0; // 从即时通信 IM 控制台获取应用 SDKAppID。
        SdkConfig sdkConfig = new SdkConfig();

        sdkConfig.sdk_config_config_file_path = Application.persistentDataPath + "/TIM-Config";

        sdkConfig.sdk_config_log_file_path = Application.persistentDataPath + "/TIM-Log"; // 设置本地日志地址

        TIMResult res = TencentIMSDK.Init(long.Parse(sdkappid), sdkConfig);
}

public static void Login() {
  if (userid == "" || user_sig == "")
  {
      return;
  }
  TIMResult res = TencentIMSDK.Login(userid, user_sig, (int code, string desc, string json_param, string user_data)=>{
    // 处理登录回调逻辑
  });
```

##### 组件内部(推荐)

您也可将`SDKAppID`、`UserSig`、`UserID`通过配置的方式传入组件内部进行 IM 的初始化和登录。

```c#
using com.tencent.imsdk.unity.uikit;

public static void Init() {
  Core.SetConfig(sdkappid, userId, sdkUserSig);
  Core.Init();
  Core.Login();
}
```

### 步骤2：导入表情包(可选)

Tencent Cloud IM Unity UIKit 目前提供文字和表情包的发送和渲染。您需要提前导入使用到的表情包。

1. 在 `Assets/Resources` 文件夹内导入所用的表情包图片
    <p align="center">
      <img src="https://qcloudimg.tencent-cloud.cn/raw/ea516e9b19793282a49c81570d17c559.png">
    </p>
2. 更改图片的 `Texture Type` 为 `Sprite (2D and UI)`，并根据图片尺寸修改 `Pixels Per Unit`
    <p align="center">
      <img src="https://qcloudimg.tencent-cloud.cn/raw/d5cad0548b08be9413a7e3a92ed0c956.png">
    </p>
3. 定义相应的表情包数据
   ```c#
      // 生成表情包列表，StickerPackage 为一组表情包
      List<StickerPackage> stickers = new List<StickerPackage> {
      new StickerPackage {
        name = "4350",
        baseUrl = "custom_sticker_resource/4350", //Resource 文件夹内相对路径
        menuItem = new StickerItem { // 表情栏表情项目
          name = "menu@2x",
          index = 0,
        },
        stickerList = new List<StickerItem> { // 表情包项目组
          new StickerItem { // 具体表情包数据
          name = "menu@2x",
          index = 0 // 表情包顺序
        },
        }
      }
    };
   ```
4. 注册表情包给 UIKit
   ```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetStickerPackageList(Config.stickers);
   ```


### 步骤3：使用 Conversation 和 Chat 预制件

在场景内引用预制件 `ChatPanel` 和 `ConversationPanel` 并调整相应 layout
    <p align="center">
      <img src="https://qcloudimg.tencent-cloud.cn/raw/99991ae822e1855ee65d4beb1058b502.png">
    </p>

在 Script 里执行 `SetConfig`, `Init` 以及 `Login`

```c#
    using com.tencent.imsdk.unity.uikit;

      Core.SetConfig(sdkappid, userid, sdkusersig); // 设置sdk账号信息
      Core.Init();
      Core.Login((params string[] args) => {
        // 处理Login回调
      });
```


## 预制件说明

您可以通过修改预制件的样式来改造自己项目的样式，目前提供以下预制件：

1. ChatPanel: 包含消息展示区 `MessageContent`, 输入操作区 `ActionPanel` 以及表情包区 `OverlayPanel`
    <p align="center">
      <img src="https://qcloudimg.tencent-cloud.cn/raw/adcb0192f03a88689addb13e9bebadbf.png">
    </p>
2. ConversationPanel: 包含会话列表头区 `ConversationHeaderPanel` 以及会话列表展示区 `ConversationListPanel`
    <p align="center">
      <img src="https://qcloudimg.tencent-cloud.cn/raw/e10e0c9d36293dcdaab80674d5756faf.png">
    </p>
3. MessageItem, MessageItemSelf, StickerMessageItem, StickerMessageItemSelf, TimeStamp 为消息组件，分别代表：他人发送文本消息类型，自己发送文本消息类型，他人发送表情消息类型，自己发送表情消息类型和时间戳消息类型
4. ConversationItem 为会话列表项
5. MenuItem, StickerItem 代表表情栏表情项目和表情项目

## API 文档

### SetConfig

在 Init 前传入 Config 信息，包括 `sdkappid`, `userid` 以及 `usersig`。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetConfig(sdkappid, userid, usersig);
```

### Init

采用 UIKit 提供的 Init 方法来初始化 SDK，会自动绑定 `AddRecvNewMsgCallback` 和 `SetConvEventCallback` 回调。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.Init();
```

### SetStickerPackageList

通过 `SetStickerPackageList` 设定表情包列表。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetStickerPackageList(Config.stickers);
```

### Login

通过 `Login` 登录账号，登录完成后执行绑定的回调函数。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.Login((params string[] args) => {
        // 处理Login回调
      });
```

### SetMessageList

添加某个会话的消息列表，处理后合并到当前会话消息字典里，并触发 `OnMsgListChanged` 事件。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetMessageList(currentConvID, newMsgList, isFinished);
```

### SetCurrentConv

设置当前选中的会话，并触发 `OnCurrentConvChanged` 事件。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetMessageList(convID, convType);
```

### SetCurrentStickerIndex

设置当前选中的表情包组，并触发 `OnCurrentStickerIndexChanged` 事件。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.SetMessageList(stickerIndex);
```

### Logout

登出，并清空数据。

```c#
   using com.tencent.imsdk.unity.uikit;

      Core.Logout((string[] parameters) => {
        // 处理Logout回调
      });
```

## TencentIMSDK

[Unity TencentIMSDK](https://cloud.tencent.com/document/product/269/54106) 提供了基于 Unity 平台的全面的即时通信能力。您可以使用 `TencentIMSDK` 来获取其他即时通信的相关功能。例如通过 `TencentIMSDK` 来获取用户资料

```c#
using com.tencent.imsdk.unity;

    // 获取个人资料
    FriendShipGetProfileListParam param = new FriendShipGetProfileListParam
    {
      friendship_getprofilelist_param_identifier_array = new List<string>
      {
        "self_userid"
      }
    };

    TIMResult res = TencentIMSDK.ProfileGetUserProfileList(param, (int code, string desc, List<UserProfile> profile, string user_data)=>{
      // 处理异步逻辑
    });
```

## 交流与反馈

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：764231117 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/26c9444af94d60e1c606f94cda7cff9d.png)
