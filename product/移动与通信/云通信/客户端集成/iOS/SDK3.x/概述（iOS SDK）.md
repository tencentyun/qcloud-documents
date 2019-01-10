## ImSDK 集成

本节主要介绍如何创建一个应用，并集成 ImSDK。

> **注意：**
> 使用互动直播业务的开发者，请集成 ImSDKv2 版本。

### 支持版本

`ImSDK.framework` 支持 iOS 7.0 及以上系统。

### 下载 ImSDK

从 [官网](https://cloud.tencent.com/product/im/developer) 下载 ImSDK 开发包，主要包括**必选 SDK** 、**可选 SDK** 和**其他 SDK** 。

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
| IMMessageExt.framework | IM 全量消息能力扩展包 | 包含消息本地存储、会话列表、最近联系人、拉取漫游消息、消息的未读计数、已读回执、草稿等功能
| IMGroupExt.framework | IM 全量群组能力扩展包 | 包含全量的群组类型和群组资料、全量的群成员能力、全量的群组管理能力 |
| IMFriendshipExt.framework | IM 全量关系链资料能力扩展包 | 包含全量的关系链能力 |
| IMSDKBugly.framework | Crash 上报功能 | 推荐使用，可以在控制台页面查看 Crash 率等信息。如果不加入此 SDK，需要设置 `TIMSdkConfig ` 中的 `disableCrashReport = true ` 禁用此功能 |
| IMUGCExt.framework | IM 小视频 UGC 消息能力扩展包 | 发送小视频消息 TIMUGCElem 功能、上传小视频功能 |
| TXRTMPSDK.framework | 小视频录制、编辑能力扩展包 | 包含小视频录制功能、小视频编辑功能，其他能力请参见 [移动直播 SDK 文档](https://cloud.tencent.com/document/product/454/7876) |

**其他 SDK：**

| 包名 | 介绍 | 功能 |
| --- | --- | --- |
| QALHttpSDK.framework | 网络透传 SDK | 只有用到网络透传功能时使用 |

使用小视频存储功能需要在控制台开通点播服务。**开通方式如下：**

![](https://mc.qcloudimg.com/static/img/7830ff8639567e4a9d60923349bf5a58/image.png)

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
>- `ImSDK.framework`、`IMMessageExt.framework`、`IMGroupExt.framework`、`IMFriendshipExt.framework`、`TLSSDK.framework`、`QALSDK.framework` 为下载的 ImSDK，其余均为系统内置库。
>- 需要在【Build Setting】-【Other Linker Flags】添加 `-ObjC`。

```
CoreTelephony.framework
SystemConfiguration.framework
libc++.dylib
libz.dylib
libsqlite3.dylib
ImSDK.framework
IMMessageExt.framework
IMGroupExt.framework
IMFriendshipExt.framework
TLSSDK.framework
QALSDK.framework
IMSDKBugly.framework
```

### 功能开发

在调用代码中引入头文件 `ImSDK.h`、`IMMessageExt.h`、`IMGroupExt.h`、`IMFriendshipExt.h`，并根据后续章节的开发指引进行功能的开发。

## ImSDK 基本概念

**会话：**ImSDK 中会话（Conversation）分为两种，一种是 **C2C 会话**，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成。另一种是**群会话**，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。如下图所示，一个会话表示与一个好友的对话。

![](//mccdn.qcloud.com/static/img/6a12c1ea947e7b36a7abe25e55c33608/image.jpg)

**消息：**ImSDK 中消息（Message）表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等。一条消息由若干 `Elem` 组合而成，每种 `Elem` 可以是文本、图片、表情等等，消息支持多种 `Elem` 组合发送。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928014948_11392.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。

### ImSDK 对象简介

iOS ImSDK 对象主要分为通讯管理器、会话、消息、群管理，具体的含义参见下表。

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| TIMManager | 管理器类 | 负责基本的 SDK 操作，包含初始化登录、注销、创建会话等 |
| TIMConversation | 会话 | 负责会话相关操作，包含发送消息、获取会话消息缓存、获取未读计数等 |
| TIMMessage | 消息 | 包含文本、图片等不同类型消息 |
| TIMGroupManager | 群管理器 | 负责创建群、增删成员、以及修改群资料等 |
| TIMFriendshipManager | 资料关系链管理 | 负责获取、修改好友资料和关系链信息 |


### 调用顺序介绍

ImSDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

| 步骤 | 对应函数 | 说明 |
| --- | --- |  --- |
| 初始化 | TIMManager:initSdk | 设置 SDK 配置信息 |
| 初始化 | TIMManager:setUserConfig | 设置用户的配置信息 |
| 登录 | TIMManager:login | 登录 |
| 消息收发 | TIMManager:getConversation | 获取会话 |
| 消息收发 | TIMConversation:sendMessage | 发送消息 |
| 群组管理 | TIMGroupManager | 群组管理 |
| 资料关系链 | TIMFriendshipManager | 资料关系链管理 |
| 注销 | TIMManager:logout | 注销（用户可选） |

## ImSDK2.x 升级到 ImSDK3.x

ImSDK3.x 版本优化了 SDK 的初始化流程和较多的模块接口，接口逻辑不变。具体接口变更请参考如下表格。

| 模块 | 2.0 接口 | 3.0 接口 |
| ---|---|--- |
| 初始化 TIMManager | initSdk:<br>disableCrashReport<br>initLogSettings:<br>setLogLevel:<br>setLogListener:<br>setLogListenerLevel:<br>setDBPath:<br>setConnListener: | initSdk: |
| 初始化 TIMManager | disableStorage<br>disableAutoReport<br>enableReadReceipt<br>disableRecentContact<br>disableRecentContactNotify<br>enableFriendshipProxy<br>enableGroupAssistant<br>initFriendshipSetting:<br>initGroupSetting:<br>setUserStatusListener:<br>setRefreshListener:<br>setReceiptListener:<br>setMessageUpdateListener:<br>setUploadProgressListener:<br>setFriendProxyListener:<br>setGroupAssistantListener: | setUserConfig: |
| TIMFriendshipManager | 接口名首字母大写 | 接口名首字母小写
| TIMFriendshipManager | SetNickname:succ:fail:<br>SetAllowType:succ:fail:<br>SetAllowType:succ:fail:<br>SetFaceURL:succ:fail:<br>SetSelfSignature:succ:fail:<br>SetGender:succ:fail:<br>SetBirthday:succ:fail:<br>SetLocation:succ:fail:<br>SetLanguage:succ:fail:<br>SetCustom:succ:fail:<br> | modifySelfProfile:profile:succ:fail: |
| TIMFriendshipManager | GetFriendListV2:custom:meta:succ:fail: | setUserConfig:配置需要拉取的资料字段<br>getFriendList:succ:fail: |
| TIMFriendshipProxy | GetFriendList<br>GetFriendsProfile:<br>GetFriendGroupList<br>GetFriendGroup: | TIMFriendshipManager<br>getFriendsProfile:<br>getFriendGroup: |
| TIMGroupManager | 接口名首字母大写 | 接口名首字母小写 |
| TIMGroupManager | GetGroupPublicInfoV2:flags:<br>custom:succ:fail: | setUserConfig:配置需要拉取的资料字段<br>getGroupPublicInfo:succ:fail: |
| TIMGroupManager | GetGroupMemberV2:flags:<br>custom:nextSeq:succ:fail: | getGroupMembers:ByFilter:flags:<br>custom:nextSeq:succ:fail: |
| 消息 | TIMSoundElem、TIMFileElem<br>TIMImageElem<br>TIMMessage delFromStorage | 仅保留指定文件路径方式上传和下载资源<br>仅保留指定文件路径方式下载资源<br>TIMMessage remove |
| 回调 | TIMGroupAssistantListener<br>TIMGroupMemberListener<br>TIMFriendshipProxyListener | TIMGroupListener<br>TIMGroupEventListener 接口名首字母小写<br>TIMFriendshipListener  接口名首字母小写 |
