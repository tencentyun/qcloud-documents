## TUIKit 介绍
TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或个性化扩展即可。


## TUIKit 主要功能介绍
TUIKit 主要分为 TUIConversation、TUIChat、TUICallKit、和TUIGroup 几个 UI 子组件，每个 UI 组件负责展示不同的内容。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d3976ece9cd5e206db47426b1f3a1690.png" style="zoom:50%;"/>

### TUIChat 重点功能介绍
TUIChat 主要负责消息界面的展示。您还可以利用它直接发送不同类型的消息、对消息长按删除/复制/撤回等。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">消息界面</th>
    <th style="text-align:center;" width="500px">发送多种类型消息</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/7f5c50d28d05db67e33dc043805a536b.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/0bbea7850f3b2d77cfcf5c7dfa4c520e.png"/></td>
	 </tr>
</table>
<table style="text-align:center; vertical-align:middle; width:500px">
		<tr>
		<th style="text-align:center;" width="500px">消息删除/撤回/复制</th>
		</tr>
		<td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/2aa099a7b362d33c246cab1418dcf90b.png" /></td>
</table>


### TUIConversation 重点功能介绍
TUIConversation 主要负责会话列表的展示和编辑。
界面效果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/c1512c52aae32e993baeb037d340fb17.png" style="zoom:40%;"/>


### TUIGroup 重点功能介绍
TUIGroup 主要负责群资料、群成员的管理。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:1000px">
  <tr>
    <th style="text-align:center;" width="500px">群操作</th>
    <th style="text-align:center;" width="500px">群成员及资料展示</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/f0aa1a5f2ab7c7c863173c31a979ad32.png"/></td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/112ed337c655c1a8c1e3f81372b3772b.png"/></td>
	 </tr>
</table>


### TUICallKit 重点功能介绍
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

如果您集成了 TUIChat 及 TUICalllKit，您可以在 TUIChat 消息页启动语音、视频通话。
界面效果如下图所示：
<table style="text-align:center; vertical-align:middle; width:500px">
  <tr>
    <th style="text-align:center;" width="300px">消息页启动</th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/324094be2e0b6891354ea6d074a81831.png" /></td>
	 </tr>
</table>


[](id:feedback)
## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ca5f8724cd5a9002abc454f80bf3df12.png" style="zoom:50%;"/>
