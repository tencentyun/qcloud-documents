## TUIKit 介绍

TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、搜索、关系链、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或个性化扩展即可。

## 支持平台

| 平台  | 支持状态 |
|---------|---------|
| iOS  | 支持 |
| Android  | 支持 |
| [Web](#web)  | 支持，0.1.5版本起 |
| macOS  | 支持，2.0.0 版本起 |
| Windows  | 支持，2.0.0 版本起 |
| [混合开发](https://cloud.tencent.com/document/product/269/83153) （将 Flutter SDK 添加至现有原生应用） | 1.0.0版本起支持 |

>? 我们致力于打造一套支持 Flutter 全平台的即时通信 IM SDK 及 TUIKit，帮助您一套代码，全平台运行。

## 体验 DEMO[](id:demo)

您可以通过我们的 DEMO，快速在线体验 TUIKit 各项能力。

**以下各版本 DEMO，均由同一 Flutter 项目引入TUIKit 制作打包而成。**

<table style="text-align:center; vertical-align:middle; max-width: 800px">
  <tr>
    <th style="text-align:center;">移动端 APP</th>
    <th style="text-align:center;">WEB - H5</th>
  </tr>
  <tr>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">iOS/Android APP，自动判断平台下载<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/ca2aaff551410c74fce48008c771b9f6.png"/></div></td>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">手机扫码体验在线 Web 版 DEMO<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/3c79e8bb16dd0eeab35e894a690e0444.png"/></div></td>
  </tr>
</table>

## TUIKit 主要功能介绍

TUIKit 按照功能主要分为**聊天**、**关系链**、**用户或群组资料**、**搜索**、**语音**几个类型的 UI 组件，每个类型的 UI 组件负责展示不同的内容。具体的 UI 组件描述如下表所示：

| 组件名               | 组件功能           |
| -------------------- | ------------------ |
| [TIMUIKitConversation](#TIMUIKitConversation) | 会话列表组件       |
| [TIMUIKitChat](#TIMUIKitChat)         | 核心聊天组件           |
| [TIMUIKitAddFriend](#add) / [TIMUIKitAddGroup](#add)    | 添加好友 及 添加群组 组件       |
| [TIMUIKitBlackList](#contacts) / [TIMUIKitNewContact](#contacts)     | 黑名单列表 及 新的联系人申请列表 组件     |
| [TIMUIKitContact](#contacts) / [TIMUIKitGroup](#contacts)      | 好友列表 及 群组列表 组件       |
| [TIMUIKitProfile](#TIMUIKitProfile) / [TIMUIKitGroupProfile](#TIMUIKitGroupProfile) | 用户信息 及 群组信息 组件       |
| [TIMUIKitSearch / TIMUIKitSearchMsgDetail](#search)      | 全局搜索/会话内搜索组件           |
| [音视频通话插件](#calling)      | 单聊or群聊 的 语音通话&视频通话       |
| [消息推送插件](#push)      | 接入厂商的离线推送 & 本地在线推送       |

界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/29ae8ebd00b201bcf60f031c7dc763a8.png" style="zoom:50%;"/>

<img src="https://qcloudimg.tencent-cloud.cn/raw/51e1a447ea02808f6b6fdea8bd8824d1.png" style="zoom:50%;"/>

### TIMUIKitChat 重点功能介绍[](id:TIMUIKitChat)

TIMUIKitChat 主要负责消息界面的展示。您可以利用它直接发送不同类型的消息，进行消息表情回应/回复/引用、查询消息已读回执详情等。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">消息界面</th>
    <th style="text-align:center;" width="500px">发送多种类型消息</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/c64b7ca7083f6858c6bb67f27fafce66.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/8b3d14018072db74145ce4bc24b91e89.png"/></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">表情回应/回复/引用</th>
    <th style="text-align:center;" width="300px">文件自动匹配icon</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/9728707f05092a8ef8945b9b611a1fb9.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/1d9f794578306b39e39a8fee3647a57b.png" /></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">消息已读回执</th>
    <th style="text-align:center;" width="300px">已读回执详情</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/91de492b091ed713f3249f31f9bd502b.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/4fe4d1d57c9ba945d19a6993c290016f.png" /></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">群tips消息</th>
    <th style="text-align:center;" width="300px">入群申请审批</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/280aacf5b254fe263ec47cc712435c8e.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/26d87e8f2e54cac8de224735a39e6158.png" /></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">链接解析</th>
    <th style="text-align:center;" width="300px">地理位置消息</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6f9b523937e482c7aa86d30f02cd1739.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b012b5a54c59748cb964782e37340495.png" /></td>
  </tr>
</table>

### 关系链 重点功能介绍[](id:contacts)

关系链主要负责当前用户的联系人、群聊、黑名单的信息展示。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">联系人列表(TIMUIKitContact)</th>
    <th style="text-align:center;" width="500px">新的联系人列表(TIMUIKitNewContact)</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/aed62aba0272da2900a5db8c9c0fcc8f.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/ed169aaccead28dfa2fc6ef6192b64f3.png"/></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">参与的群聊列表(TIMUIKitGroup)</th>
    <th style="text-align:center;" width="300px">黑名单列表(TIMUIKitBlackList)</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/c6bc53492ba9c620680396e687bda3a9.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/5eaaa4aa89d5c7a549813b1b3ab054b5.png" /></td>
  </tr>
</table>

### TIMUIKitConversation 重点功能介绍[](id:TIMUIKitConversation)

TIMUIKitConversation 主要负责会话列表的展示和编辑。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/214007feb3be18519c4ad3947ef0e266.png" style="zoom:40%;"/>

### TIMUIKitProfile 重点功能介绍[](id:TIMUIKitProfile)

TIMUIKitProfile 主要负责联系人的资料展示与管理。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e3831ff35e1571c8dbd6b26517cac819.png" style="zoom:40%;"/>

### 添加用户与群组 功能介绍[](id:add)

TIMUIKitAddFriend 为添加好友页面。
TIMUIKitAddGroup 为添加群组页面。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">添加好友页面(TIMUIKitAddFriend)</th>
    <th style="text-align:center;" width="500px">添加群组页面(TIMUIKitAddGroup)</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/cf0eaf557c607a139d8c4afd7da8bb21.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/398e1fa730ffe17acdaffaa252c3de3c.png"/></td>
  </tr>
</table>

### TIMUIKitGroupProfile 重点功能介绍[](id:TIMUIKitGroupProfile)

TIMUIKitGroupProfile 主要负责群资料、群成员、群组权限的展示与管理。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">群资料及管理</th>
    <th style="text-align:center;" width="500px">群成员管理</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/3424c3e391c321bf607fcd807ef70afe.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/e35200ce0b9653a98205ad135caa2b45.png"/></td>
  </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">加群方式管理</th>
    <th style="text-align:center;" width="300px">群操作</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/2af746e239e4f43d142dc634a114a680.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/d39a4b2c84e3b62bcd1a770cf26dc209.png" /></td>
  </tr>
</table>

### 本地搜索 重点功能介绍[](id:search)

TIMUIKitSearch 为本地全局搜索，支持搜索联系人、群聊、聊天记录。
TIMUIKitSearchMsgDetail 为会话内聊天历史记录搜索。
详情 [可查看此文档](https://cloud.tencent.com/document/product/269/79121)，界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/199a69d9da6126690a34c7bb01552081.png" style="zoom:40%;"/>

### 音视频通话 重点功能介绍[](id:calling)

[TUICalling插件](https://cloud.tencent.com/document/product/269/72485) 主要负责语音、视频通话。
单聊语音通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/1ee168e84c31bcac54e1d5ffb98b4491.png" style="zoom:40%;"/>
单聊视频通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e4a376e5d6895059214ccc7412cc6be2.jpg" style="zoom:60%;"/>
群聊语音与视频通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/f00f69d432ce4599b7be643dbf410370.png" style="zoom:40%;"/>

您可以在 TIMUIKitChat 消息页、TIMUIKitProfile 个人资料页等页面启动语音、视频通话。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">消息页启动</th>
    <th style="text-align:center;" width="300px">资料页启动</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/a54e097733331db4593589959ab52a82.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/4f9ecb8c9c585271e1c9a527876e6efc.png" /></td>
  </tr>
</table>

### 消息推送重点功能介绍[](id:push)

您可通过我们的 [Flutter 推送插件](https://cloud.tencent.com/document/product/269/74605) 集成消息推送能力，涵盖离线推送与在线推送。
消息推送效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b2717640d161ea0cea66d509311dc6a7.png" style="zoom:40%;"/>

[](id:feedback)

## 联系我们[](id:contact)

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
