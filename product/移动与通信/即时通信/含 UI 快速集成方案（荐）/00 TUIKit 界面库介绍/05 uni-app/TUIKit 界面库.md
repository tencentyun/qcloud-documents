
## TUIKit 介绍
TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或个性化扩展即可。

## 支持平台
- APP 端（Android、iOS）
- 微信小程序端
- H5 端

界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/06ccb31cb4dd0ae0d93a15794f63bb81.png)
## TUIKit 主要功能介绍
TUIKit 主要分为 TUIConversation、TUIChat、TUICallKit、和TUIGroup 几个 UI 子组件，每个 UI 组件负责展示不同的内容。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b65ac3e2fdac99228dcaf0a2b909a156.png" style="zoom:50%;"/>

### TUIChat 重点功能介绍
TUIChat 主要负责消息界面的展示。您还可以利用它直接发送不同类型的消息、对消息长按删除/复制/撤回等。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">消息界面</th>
    <th style="text-align:center;" width="500px">消息操作</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/c4841f05abb3d956fbf2ca6e62815bda.png"/></td>
		<td><img style="width:450px" src="https://qcloudimg.tencent-cloud.cn/raw/29aa0c54d00b03e82bbcb0a1a8445373.png"/></td>
	 </tr>
</table>

### TUIConversation 重点功能介绍
TUIConversation 主要负责会话列表的展示和操作。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/bd41cd6ec99cb8c6e1ef0fef39002db1.png" style="zoom:60%;"/>

### TUIGroup 重点功能介绍
TUIGroup 主要负责群资料、群成员的管理。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/31f6f3e42b5a78e844b1f9ce1bf46417.png" style="zoom:60%;"/>

### 更多高级特性

#### TUICallKit 重点功能介绍
TUICallKit 主要负责语音、视频通话。
单聊通话示意图：
<table style="text-align:center;vertical-align:middle;width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">视频通话<br></th>
    <th style="text-align:center;" width="500px">语音通话<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b412c178178c0052254f4f800559d7d4.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6b2b6878e714e77e578e3c962659e36b.jpg" />     </td>
	 </tr>
</table>

群聊通话示意图：
<table style="text-align:center;vertical-align:middle;width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">视频通话<br></th>
    <th style="text-align:center;" width="500px">语音通话<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/5ca955c288c0c45b74e4fcfcb0ec6ebb.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/068a66d2a99a910d516e645ffb06a23a.png" />     </td>
	 </tr>
</table>


集成请参考官网文档 [TUICallKit 集成方案](https://cloud.tencent.com/document/product/647/78742)

#### TUIOfflinePush 离线推送插件介绍
TUIOfflinePush 是腾讯云即时通信 IM Push 插件。目前离线推送支持 Android 和 iOS 平台，设备有：华为、小米、OPPO、vivo、魅族 和 苹果手机。
效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/02e095b0f832c73caf5382495d7fc8d9.png" style="zoom:50%;"/>

在 APP 中集成离线推送能力，请参考官网文档 [uni-app 离线推送](https://cloud.tencent.com/document/product/269/79124)

[](id:feedback)
## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。 QQ 咨询：309869925技术交流群
