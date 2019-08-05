## ImSDK 集成

本节主要介绍如何创建一个应用，并集成 ImSDK。

### 支持版本

`ImSDK.framework` 支持 iOS 7.0 及以上系统。

### 下载 ImSDK

从 [官网](https://cloud.tencent.com/product/im/developer) 下载 ImSDK 开发包，主要包括：**必选 SDK** 、**可选 SDK** 和**其他 SDK**。

> **注意：**
> SDK 包必须是一个版本成套使用，不同版本不可混用。

**必选 SDK：**

| 包名 | 介绍 |
| --- | --- |
| ImSDK.framework | IM 基础功能包 |
| QALSDK.framework | 网络 SDK |
| TLSSDK.framework | 登录 SDK |

**可选 SDK：**

| 包名 | 介绍 | 功能 |
| --- | --- | --- |
| IMCore.framework | IM 核心功能 | 如果使用 IM 聊天必须加入，如果只用登录功能（如只使用音视频的情况，可不加入）<br>如果不加入 IMCore.framework，使用时需 `#import "ImSDK/ImSDKSimple.h"`，不要包含其他头文件，否则可能会引起编译错误 |
| IMSDKBugly.framework | Crash 上报功能 | 如无特殊需要，推荐使用，在控制台页面可以查看 Crash 率等信息<br>如果不加入此 SDK，需要调用 `[TIMManager sharedInstance] disableCrashReport]; ` 禁用功能 |

**其他 SDK：**

| 包名 | 介绍 | 功能 |
| --- | --- | --- |
| QALHttpSDK.framework | 网络透传 SDK | 只有用到网络透传功能时使用 |

### 创建应用

**创建一个新工程：**

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013356_56054.jpg)

**填入工程名（例如：IMDemo）：**

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013638_56711.jpg)

### 集成 ImSDK

**添加依赖库：**选中 IMDemo 的【Target】，在【General】面板中的【Linked Frameworks and Libraries】添加依赖库。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013833_31715.jpg)

**添加以下依赖库：**

> **注意：**
>- `ImSDK.framework`、`IMCore.framework`、`TLSSDK.framework`、`QALSDK.framework` 为下载的 ImSDK，其余均为系统内置库。
>- 需要在【Build Setting】-【Other Linker Flags】添加 `-ObjC`。

```
CoreTelephony.framework
SystemConfiguration.framework
libc++.dylib
libz.dylib
libsqlite3.dylib
ImSDK.framework
IMCore.framework
TLSSDK.framework
QALSDK.framework
IMSDKBugly.framework
```

### 功能开发

在调用代码中引入 `ImSDK.framework` 头文件 `ImSDK.h`，根据后续章节的开发指引进行功能的开发。其中函数调用顺序可参见 [调用顺序介绍](#.E8.B0.83.E7.94.A8.E9.A1.BA.E5.BA.8F.E4.BB.8B.E7.BB.8D)。

## ImSDK 基本概念

**会话：**ImSDK 中会话（Conversation）分为两种，一种是 **C2C 会话**，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成。另一种是**群会话**，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。如下图所示，一个会话表示与一个好友的对话。

![](//mccdn.qcloud.com/static/img/6a12c1ea947e7b36a7abe25e55c33608/image.jpg)

**消息：**ImSDK 中消息（Message）表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等。一条消息由若干 `Elem` 组合而成，每种 `Elem` 可以是文本、图片、表情等等，消息支持多种 `Elem` 组合发送。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928014948_11392.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。

### ImSDK 对象简介

iOS ImSDK 对象主要分为通讯管理器，会话、消息，群管理，具体的含义参见下表。

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| TIMManager | 管理器类，负责基本的 SDK 操作 | 初始化登录、注销、创建会话等 |
| TIMConversation | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等 |
| TIMMessage | 消息 | 包括文本、图片等不同类型消息 |
| TIMGroupManager | 群管理器 | 负责创建群，增删成员，以及修改群资料等 |
| TIMFriendshipManager | 资料关系链管理 | 负责获取、修改好友资料和关系链信息 |

### 调用顺序介绍

ImSDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

| 步骤 | 对应函数 | 说明 |
| --- | --- | --- |
| 初始化 | TIMManager : setMessageListener | 设置消息回调 |
| 初始化 | TIMManager : setConnListener | 设置链接通知回调 |
| 初始化 | TIMManager : initSdk | 初始化 SDK |
| 登录 | TIMManager : login | 登录 |
| 消息收发 | TIMManager : getConversation | 获取会话 |
| 消息收发 | TIMConversation : sendMessage | 发送消息 |
| 群组管理 | TIMGroupManager | 群组管理 |
| 资料关系链 | TIMFriendshipManager | 资料关系链管理 |
| 注销 | TIMManager : logout | 注销（用户可选） |

