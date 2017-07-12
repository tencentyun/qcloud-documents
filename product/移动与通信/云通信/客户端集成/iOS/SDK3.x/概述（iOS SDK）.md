## 1. ImSDK集成

本节主要介绍如何创建一个应用，并集成ImSDK。

### 1.1 支持版本

ImSDK.framework 支持iOS 7.0 及以上系统。

### 1.2 下载ImSDK

从 [官网](https://www.qcloud.com/product/im.html#sdk) 下载ImSDK开发包，主要包括：ImSDK.framework、IMMessageExt.framework、IMGroupExt.framework、IMFriendshipExt.framework、TLSSDK.framework、QALSDK.framework。各个包的说明如下：

必选SDK：**必须是一个版本成套使用，不同版本不可混用**

* ImSDK.framework 		IM基础功能包
* QALSDK.framework		网络SDK
* TLSSDK.framework		登录SDK

可选SDK：

* IMMessageExt.framework		IM全量消息能力扩展包
  * 包含消息本地存储、会话列表、最近联系人、拉取漫游消息等功能
  * 增加消息的未读计数、已读回执、草稿等功能
* IMGroupExt.framework   IM全量群组能力扩展包
  * 包含全量的群组类型和群组资料
  * 包含全量的群成员能力
  * 包含全量的群组管理能力
* IMFriendshipExt.framework    IM全量关系链资料能力扩展包
  * 包含全量的关系链能力
* IMSDKBugly.framework	  Crash上报功能
 * 如无特殊需要，推荐使用，在控制台页面可以查看Crash率等信息
 * 如果不加入此SDK，需要调用 [TIMManager sharedInstance] disableCrashReport]; 禁用功能
* IMUGCExt.framework		IM小视频UGC消息能力扩展包
  * 发送小视频消息 TIMUGCElem 功能
  * 上传小视频功能
* TXRTMPSDK.framework   小视频录制、编辑能力扩展包
  * 包含小视频录制功能
  * 包含小视频编辑功能
  * 其他能力请参见[移动直播SDK文档](https://www.qcloud.com/document/product/454/7876)

其他SDK：

* QALHttpSDK.framework		网络透传SDK
 * 只有用到网络透传功能时使用

### 1.3 创建应用

创建一个新工程，填入工程名，这里以IMDemo为例：

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013356_56054.jpg)
![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013638_56711.jpg)

### 1.4 集成ImSDK

选中IMDemo的Target，在General面板中的Linked Frameworks and Libraries添加依赖库。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928013833_31715.jpg)

需要添加的依赖库有：

```
CoreTelephony.framework
SystemConfiguration.framework
libstdc++.6.dylib
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

其中 ImSDK.framework、IMMessageExt.framework、IMGroupExt.framework、IMFriendshipExt.framework、TLSSDK.framework、QALSDK.framework 为步骤1.1.1下载的SDK，其余均为系统内置库。另外**需要在Build Setting中Other Linker Flags添加-ObjC**。

### 1.5 功能开发

在调用代码中引入头文件ImSDK.h、IMMessageExt.h、IMGroupExt.h、IMFriendshipExt.h，根据后续章节的开发指引进行功能的开发。

## 2. ImSDK 基本概念

会话：ImSDK中会话(Conversation)分为两种，一种是C2C会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成；另一种是群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。

如下图所示，一个会话表示与一个好友的对话：

![](//mccdn.qcloud.com/static/img/6a12c1ea947e7b36a7abe25e55c33608/image.jpg)

消息：ImSDK中消息(Message)表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等；一条消息由若干Elem组合而成，每种Elem可以是文本、图片、表情等等，消息支持多种Elem组合发送。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928014948_11392.png)

群组Id：群组Id唯一标识一个群，由后台生成，创建群组时返回。

### 2.1 ImSDK对象简介

iOS ImSDK 对象主要分为通讯管理器，会话、消息，群管理，具体的含义参见下表：

对象 | 介绍 | 功能
---|---|---
TIMManager | 管理器类，负责基本的SDK操作 | 初始化登录、注销、创建会话等
TIMConversation | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等
TIMMessage | 消息 | 包括文本、图片等不同类型消息
TIMGroupManager | 群管理器 | 负责创建群，增删成员，以及修改群资料等
TIMFriendshipManager | 资料关系链管理 | 负责获取、修改好友资料和关系链信息


### 2.2 调用顺序介绍

ImSDK调用API需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

步骤 | 对应函数 | 说明
---|---|---
初始化 | TIMManager : initSdk | 设置SDK配置信息
初始化 | TIMManager : setUserConfig | 设置用户的配置信息
登录 | TIMManager : login | 登录
消息收发 | TIMManager : getConversation | 获取会话
消息收发 | TIMConversation : sendMessage | 发送消息
群组管理 | TIMGroupManager | 群组管理
资料关系链 | TIMFriendshipManager | 资料关系链管理
注销 | TIMManager : logout | 注销（用户可选）

## 3. ImSDK2.x升级到ImSDK3.x

ImSDK3.x版本优化了SDK的初始化流程和较多的模块接口，接口逻辑不变。
具体接口变更请参考如下表格：

模块 | 2.0接口 | 3.0接口
---|---|---
<b>初始化 TIMManager</b> | initSdk:<br>disableCrashReport<br>initLogSettings:<br>setLogLevel:<br>setLogListener:<br>setLogListenerLevel:<br>setDBPath:<br>setConnListener: | initSdk:
<b>初始化 TIMManager</b> | disableStorage<br>disableAutoReport<br>enableReadReceipt<br>disableRecentContact<br>disableRecentContactNotify<br>enableFriendshipProxy<br>enableGroupAssistant<br>initFriendshipSetting:<br>initGroupSetting:<br>setUserStatusListener:<br>setRefreshListener:<br>setReceiptListener:<br>setMessageUpdateListener:<br>setUploadProgressListener:<br>setFriendProxyListener:<br>setGroupAssistantListener: | setUserConfig:
<b>TIMFriendshipManager</b> | 接口名首字母大写 | 接口名首字母小写
<b>TIMFriendshipManager</b> | SetNickname:succ:fail:<br>SetAllowType:succ:fail:<br>SetAllowType:succ:fail:<br>SetFaceURL:succ:fail:<br>SetSelfSignature:succ:fail:<br>SetGender:succ:fail:<br>SetBirthday:succ:fail:<br>SetLocation:succ:fail:<br>SetLanguage:succ:fail:<br>SetCustom:succ:fail:<br> | modifySelfProfile:profile:succ:fail:
<b>TIMFriendshipManager</b> | GetFriendListV2:custom:meta:succ:fail: | setUserConfig:配置需要拉取的资料字段<br>getFriendList:succ:fail:
<b>TIMFriendshipProxy</b> | GetFriendList<br>GetFriendsProfile:<br>GetFriendGroupList<br>GetFriendGroup: | <b>TIMFriendshipManager</b><br> getFriendsProfile:<br>getFriendGroup:
<b>TIMGroupManager</b> | 接口名首字母大写 | 接口名首字母小写
<b>TIMGroupManager</b> | GetGroupPublicInfoV2:flags:custom:succ:fail: | setUserConfig:配置需要拉取的资料字段<br>getGroupPublicInfo:succ:fail:
<b>TIMGroupManager</b> | GetGroupMemberV2:flags:custom:nextSeq:succ:fail: | getGroupMembers:ByFilter:flags:custom:nextSeq:succ:fail:
<b>消息</b> | <b>TIMSoundElem、TIMFileElem</b> | 仅保留指定文件路径方式上传和下载资源
<b>消息</b> | <b> TIMImageElem</b> | 仅保留指定文件路径方式下载资源
<b>消息</b> | <b> TIMMessage delFromStorage</b> | <b>TIMMessage remove</b>
<b>回调</b> | <b>TIMGroupAssistantListener</b> | <b>TIMGroupListener</b>
<b>回调</b> | <b>TIMGroupMemberListener</b> | <b>TIMGroupEventListener</b>注意首字母小写
<b>回调</b> | <b>TIMFriendshipProxyListener</b> | <b>TIMFriendshipListener</b>注意首字母小写
