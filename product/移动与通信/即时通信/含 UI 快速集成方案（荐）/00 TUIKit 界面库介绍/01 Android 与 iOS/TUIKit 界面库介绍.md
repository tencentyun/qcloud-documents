## TUIKit 介绍
TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、搜索、关系链、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或个性化扩展即可。


## TUIKit 主要功能介绍
TUIKit 主要分为 TUISearch、TUIConversation、TUIChat、TUICallKit、TUIContact、TUIGroup 和 TUIOfflinePush 几个 UI 子组件，每个 UI 组件负责展示不同的内容。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ed580d8967b9d205e894f36d8e634369.png" style="zoom:50%;"/>

## TUIChat 重点功能介绍
TUIChat 主要负责消息界面的展示。您还可以利用它直接发送不同类型的消息、对消息长按点赞/回复/引用、查询消息已读回执详情等。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">消息界面</th>
    <th style="text-align:center;" width="500px">发送多种类型消息</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/1ac02de0a788fe0d1f0d20493fbfd081.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/512d34e2e5bdf256129b6207e46e79e1.png"/></td>
	 </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">消息点赞/回复/引用</th>
    <th style="text-align:center;" width="300px">消息回复详情</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/f87f569a7b90164d3ab44ed16089d8cd.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6d011c026f7b4d58413032da2e18b090.png" /></td>
	 </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">消息已读回执</th>
    <th style="text-align:center;" width="300px">已读回执详情</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/223da735715f8d1563ff2dab2a9c19fe.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b18dd054ac62d844ccbda50c1a7e0e9b.png" /></td>
	 </tr>
</table>

## TUIContact 重点功能介绍
TUIContact 主要负责联系人的展示、权限设置等。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">关系链列表</th>
    <th style="text-align:center;" width="500px">联系人资料及管理</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6c84a8e9dd793c52d3cff3ca6ebee80a.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/16965a64aab5e9987ac6e002fa479830.png"/></td>
	 </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">参与的群聊列表</th>
    <th style="text-align:center;" width="300px">黑名单列表</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/6f8d0873f28ae18673106edfac334366.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/0c1cf41c8924a72221299d938952ef38.png" /></td>
	 </tr>
</table>


## TUIConversation 重点功能介绍
TUIConversation 主要负责会话列表的展示和编辑。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b90b81ddce0bee584fb3d7e9470e95b8.png" style="zoom:40%;"/>


## TUIGroup 重点功能介绍
TUIGroup 主要负责群资料、群成员、群组权限的管理。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">群资料及管理</th>
    <th style="text-align:center;" width="500px">群成员管理</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/fb9c2ff73c31ecb349926b22ba0e4ac2.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/ca958eb233e5ede07b03a81b25ee9975.png"/></td>
	 </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">加群方式管理</th>
    <th style="text-align:center;" width="300px">权限管理</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/dc3f86d8140d9c40de674f6b5bc820db.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/dd2bb957639ea1606f15f4c73420bb5c.png" /></td>
	 </tr>
</table>


## TUISearch 重点功能介绍
TUISearch 主要负责本地搜索，支持搜索联系人、群聊、聊天记录。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/1e94c5b2c50102c7d3d0c79de9343c07.png" style="zoom:40%;"/>


## TUICallKit 重点功能介绍
TUICallKit 主要负责语音、视频通话。
单聊语音通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/2f037d7de8270c0edef68c0b829465ec.png" style="zoom:40%;"/>
单聊视频通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b9f362503d25179db6f75fc91cfd000a.jpg" style="zoom:40%;"/>
群聊视频通话示意图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/71d343787ce1c2a4b5ea0671f7d2192e.png" style="zoom:40%;"/>

如果您集成了 TUIChat、TUIContact 及 TUICalllKit，您可以在 TUIChat 消息页、TUIContact 个人资料页启动语音、视频通话。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="300px">消息页启动</th>
    <th style="text-align:center;" width="300px">资料页启动</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/b7b6aca5e1f3f3e5d775cfa3316e30f4.png" /></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/31fd1d8fb263e953825cf5531a24ffca.png" /></td>
	 </tr>
</table>


## TUIOfflinePush 重点功能介绍
TUIOfflinePush 主要负责离线推送消息展示。
离线推送效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/991f4499b52103dc5495ca1b7188a9ad.png" style="zoom:40%;"/>

[](id:feedback)
## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ca5f8724cd5a9002abc454f80bf3df12.png" style="zoom:50%;"/>
