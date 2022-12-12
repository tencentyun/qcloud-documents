


## TUIKit 介绍
TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，它提供了一些通用的 UI 组件，包含会话、聊天、关系链、群组、音视频通话等功能。
基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
TUIKit 中的组件在实现 UI 功能的同时，会调用 IM SDK 相应的接口实现 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit  时只需关注自身业务或个性化扩展即可。
基于 React 开发的 TUIKit 界面风格更契合境外客户的使用习惯，而且支持国际化，如果您的业务有出海的需求，欢迎接入。

## TUIKit 组成
TUIKit 主要分为 TUIChat、TUIConversation、TUIProfile、TUIManage 等模块，每个模块负责不同的内容，具体可参见 [开源代码](https://github.com/TencentCloud/chat-uikit-react)。TUIKit Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/14ed827eecc218306abc82d46c57252d.png)


## TUIChat 重点功能介绍
TUIChat 主要负责消息界面的展示。您可以利用它直接发送不同类型的消息，支持文字/表情/图片/视频/文件/自定义等消息类型，同时支持消息转发/撤回/引用、查询、已读回执等功能。
TUIChat Web 端界面效果如下图所示：

<table style="text-align:center;vertical-align:middle;width:1000px">
  <tr>
	  <th style="text-align:center;" width="500px">消息界面/引用/撤回/转发<br></th>
    <th style="text-align:center;" width="500px">消息导航/已读显示<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/650406b1aa19b2a28d6edaf5e9640600.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/a6aa711af90ed63109c921e2d92ac1c8.png" />     </td>
	 </tr>
</table>

## TUIConversation 功能介绍
TUIConversation 主要负责会话列表的展示和编辑，包含会话置顶、会话删除等功能。TUIConversation Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1edcd75599d64d138218ff5607fd91b1.png)


## TUIManage 功能介绍
TUIManage 主要负责会话相关信息展示、会话置顶、会话删除以及群组相关操作。TUIManage Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0cf2909353296b154ba4f61197624f55.png)

## TUIContact 重点功能介绍
TUIContact 主要负责关系链展示以及创建会话等操作。TUIContact Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6ff9f0f4704c9e1664d27f673789de9c.png)

## TUIProfile 重点功能介绍
TUIProfile 主要负责用户资料的管理。TUIProfile Web 端界面效果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/34985aaa1c4e4371bc1e517984427137.png)
