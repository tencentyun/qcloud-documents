## 群组类型介绍

- **好友工作群（Work）**：类似普通微信群，创建后仅支持已在群内的好友邀请加群，且无需被邀请方同意或群主审批，同旧版本中的 Private。
- **陌生人社交群（Public）**：类似 QQ 群，创建后群主可以指定群管理员，用户搜索群 ID 发起加群申请后，需要群主或管理员审批通过才能入群。
- **临时会议群（Meeting）**：创建后可以随意进出，且支持查看入群前消息；适合用于音视频会议场景、在线教育场景等与实时音视频产品结合的场景，同旧版本中的 ChatRoom。
- **社群（Community）**：创建后可以随意进出，适合用于知识分享和游戏交流等超大社区群聊场景。
- **直播群（AVChatRoom）**：创建后可以随意进出，没有群成员数量上限，但不支持历史消息存储；适合与直播产品结合，用于弹幕聊天场景。



每种群类型的功能特性及限制如下表所示：

<table>
  <tr>
    <th width="20%">功能项</th>
    <th width="16%">好友工作群（Work）</th>
    <th width="16%">陌生人社交群（Public）</th>
    <th width="16%">临时会议群（Meeting）</th>
    <th width="16%">社群（Community）</th>
    <th>直播群（AVChatRoom）</th>
  </tr>
  <tr>
    <td>可用群成员角色</td>
    <td>群主、普通成员</td>
    <td>群主、管理员、普通成员</td>
    <td>群主、管理员、普通成员</td>
    <td>群主、管理员、普通成员</td>
    <td>群主、普通成员</td>
  </tr>
  <tr>
    <td>是否支持申请加群</td>
    <td>不支持</td>
    <td>支持，但需要群主或管理员审批</td>
    <td>支持，且无需审批</td>
    <td>支持，且无需审批</td>
    <td>支持，且无需审批</td>
  </tr>
  <tr>
    <td>是否支持成员邀请他人加群</td>
    <td>支持</td>
    <td>不支持</td>
    <td>不支持</td>
    <td>支持</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>是否支持群主退群</td>
    <td>支持</td>
    <td>不支持</td>
    <td>不支持</td>
    <td>不支持</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>群组资料修改权限</td>
    <td>任意群成员均可修改</td>
    <td>群主和管理员</td>
    <td>群主和管理员</td>
    <td>群主和管理员</td>
    <td>群主</td>
  </tr>
  <tr>
    <td>“踢人”权限</td>
    <td>群主可踢人</td>
    <td colspan="3">群主和管理员可踢人，但管理员仅支持踢普通群成员</td>
    <td>不支持踢人，可用“禁言”功能达到类似效果</td>
  </tr>
  <tr>
    <td>“禁言”权限</td>
    <td>不支持禁言</td>
    <td colspan="3">群主和管理员可禁言，
      但管理员仅支持禁言普通群成员</td>
    <td>群主可禁言</td>
  </tr>
  <tr>
    <td>是否支持未读消息计数</td>
    <td>支持</td>
    <td>支持</td>
    <td>不支持</td>
    <td>支持</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>是否支持查看入群前消息记录</td>
    <td>不支持</td>
    <td>不支持</td>
    <td>支持</td>
    <td>支持</td>
    <td>不支持</td>
  </tr>
  <tr>
  	<td>是否支持云端历史消息存储</td>
  	<td colspan="4"><ul style="margin:0;padding-left:10px" ><li>体验版：7天</li><li>专业版 ：默认7天，最高支持 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值</a> 延长至360天</li><li>旗舰版 ：默认30天，最高支持 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值</a> 延长至360天</li></ul></td>
  <td>不支持</td>
  </tr>
  <tr>
  <td>群组数量</td>
  <td colspan="3"><ul style="margin:0;padding-left:10px"><li>体验版：最多同时存在100个，已解散的群组不计数</li><li>专业版或旗舰版：无上限</li></ul></td>
  <td><ul style="margin:0;padding-left:10px"><li>体验版和专业版：不支持</li><li>旗舰版：10万个</li></ul></td>
  <td><ul style="margin:0;padding-left:10px"><li>体验版：最多同时存在10个，已解散的群组不计数</li><li>专业版：最多同时存在50个，已解散的群组不计数;<br>支持 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值</a> 扩展直播群创建数至无上限</li><li>旗舰版：无上限</li></ul></td>
  </tr>
  <tr>
  <td>群成员数量</td>
  <td colspan="3"><ul style="margin:0;padding-left:10px"><li>体验版：20人/群</li><li>专业版 ：默认为200人/群，最高支持 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值</a> 扩展至2000人/群</li><li>旗舰版 ：默认为2000人/群，最高支持 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值</a> 扩展至6000人/群</li></ul></td>
  <td>10万人</td>
  <td>群成员人数无上限</td>
  </tr>
</table>

>?
- 新版 SDK 已全面升级群组类型。新群组类型有**好友工作群（Work）**、**陌生人社交群（Public）**、**临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom）**五个群组类型。旧版群组类型（Public、Private、ChatRoom、AVChatRoom）中的 Private 类型对应新群组类型 Work（好友工作群），ChatRoom 类型对应新群组类型 Meeting（临时会议群）。
- 专业版或旗舰版 SDKAppID 下，所有群类型日净增群组数上限为1万个。免费峰值群组数为10万个/月，超出免费量将产生 [套餐外超量费用](https://cloud.tencent.com/document/product/269/11673#jc)。
- 社群（Community）功能仅SDK5.8.1668增强版及以上版本支持，需购买旗舰版套餐包并 [申请开通](https://cloud.tencent.com/document/product/269/3916) 后方可使用。
- 好友工作群（Work）、陌生人社交群（Public）默认不支持查看入群前消息记录。如需使用此功能，请参见 [配置变更需求工单](https://cloud.tencent.com/document/product/269/3916) 指引提交变更申请。

## 创建群组

如果您想在创建群组的同时初始化群的信息，例如群简介、群头像、以及最初的几个群成员等，可以调用 [GroupCreate](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupCreate_com_tencent_imsdk_unity_types_CreateGroupParam_com_tencent_imsdk_unity_callback_ValueCallback_) 接口实现。参数请参见 [CreateGroupParam](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.CreateGroupParam.html)。

```c#
TencentIMSDK.GroupCreate(CreateGroupParam,(int code, string desc, string json_param, string user_data)=>{

})
```

## 加入群组

不同类型的群，加群的方法不同，下面根据加群流程从简单到复杂进行逐一介绍：

| 类型     | 好友工作群（Work）   | 陌生人社交群（Public）     | 临时会议群（Meeting） | 社群（Community） | 直播群（AVChatRoom） |
| :------- | :------------------- | :------------------------- | :-------------------- | :---------------- | :------------------- |
| 加群方法 | 必须由其他群成员邀请 | 用户申请，群主或管理员审批 | 用户可随意加入        | 用户可随意加入    | 用户可随意加入       |

### 场景一：用户可以自由进出群

临时会议群（Meeting）和直播群（AVChatRoom）主要用于满足成员进进出出的交互场景，例如在线会议，秀场直播等。因此，这两种类型群的入群流程最为简单。

用户调用 [GroupJoin](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupJoin_System_String_System_String_com_tencent_imsdk_unity_callback_ValueCallback_) 即可加入该群，加群成功后，全体群成员（包括加群者）都会收到 [GroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.html#grouptipseventcallback) 回调。

### 场景二：需被邀请才能进入群

好友工作群（Work）类似微信群和企业微信群，适用于工作交流，在交互设计上限制用户主动加入，只能由现有的群成员邀请才能加群。

现有的群成员调用 [GroupInviteMember](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupInviteMember_com_tencent_imsdk_unity_types_GroupInviteMemberParam_com_tencent_imsdk_unity_callback_ValueCallback_) 邀请另一个用户入群，全体群成员（包括邀请者自己）会收到 [GroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.GroupTipsEventCallback.html) 回调。

### 场景三：需要审批才能进入群

陌生人社交群（Public）类似 QQ 中的各种兴趣群和部落区，任何人都可以申请入群，但需要经过群主或管理员审批才能真正入群。陌生人社交群默认需要群主或管理员进行审批才能加群的，但群主或管理员也可以通过[GroupModifyGroupInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupModifyGroupInfo_com_tencent_imsdk_unity_types_GroupModifyInfoParam_com_tencent_imsdk_unity_callback_ValueCallback_)接口调整加群选项（[TIMGroupAddOption](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.enums.TIMGroupAddOption.html)），可以设置为更严格的“禁止任何人加群”，也可以设置为更宽松的“放开审批流程”。

- kTIMGroupAddOpt_Forbid ：禁止任何人加群。
- kTIMGroupAddOpt_Auth ：需要群主或管理员审批才能加入（默认值）。
- kTIMGroupAddOpt_Any ：取消审批流程，任何用户都可以加入。

## 退出群组

调用 [GroupQuit](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupQuit_System_String_com_tencent_imsdk_unity_callback_ValueCallback_) 可以退出群组，群内成员可收到 [GroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.GroupTipsEventCallback.html)。

>!对于陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom），群主不可以退群的，群主只能解散群组。

## 解散群组

调用 [GroupDelete](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupDelete_System_String_com_tencent_imsdk_unity_callback_ValueCallback_) 可以解散群组，全员会收到 [GroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.GroupTipsEventCallback.html) 回调。

>!
- 对于陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom），群主随时可以解散群。
- 好友工作群（Work）的解散最为严格，即使群主也不能随意解散，只能由您的业务服务器调用 [解散群组 REST API](https://cloud.tencent.com/document/product/269/1624) 解散。

## 获取即加入的群组

调用 [GroupGetJoinedGroupList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupGetJoinedGroupList_com_tencent_imsdk_unity_callback_ValueCallback_) 可以获取已加入的好友工作群（Work）、陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）列表，但直播群（AVChatRoom）不包含在此列表中。

## 群资料和群设置

### 获取群资料

调用 [GroupGetGroupInfoList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupGetGroupInfoList_System_Collections_Generic_List_System_String__com_tencent_imsdk_unity_callback_ValueCallback_) 可以获取群资料，该接口支持批量获取。您可以一次传入多个 `groupID` 获取多个群的群资料。

### 修改群资料

调用 [GroupModifyGroupInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupModifyGroupInfo_com_tencent_imsdk_unity_types_GroupModifyInfoParam_com_tencent_imsdk_unity_callback_ValueCallback_) 可以修改群资料。群资料被修改后，全员会收到 [GroupTipsEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.GroupTipsEventCallback.html) 回调。

>?
- 好友工作群（Work）所有群成员都可以修改群基础资料。
- 陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）只有群主或管理员可以修改群基础资料。
- 直播群（AVChatRoom）只有群主可以修改群基础资料。

## 设置群消息的接收选项

任何群成员都可以调用 [MsgSetGroupReceiveMessageOpt](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_MsgSetGroupReceiveMessageOpt_System_String_com_tencent_imsdk_unity_enums_TIMReceiveMessageOpt_com_tencent_imsdk_unity_callback_ValueCallback_) 接口修改群消息接收选项。群消息接收选项包括：

- TIMReceiveMessageOpt.kTIMRecvMsgOpt_Receive：在线正常接收消息，离线时会有厂商的离线推送通知。
- TIMReceiveMessageOpt.kTIMRecvMsgOpt_Not_Receive：不会接收到群消息。
- TIMReceiveMessageOpt.kTIMRecvMsgOpt_Not_Notify：在线正常接收消息，离线不会有推送通知。

## 常见问题

### 1. 直播群（AVChatRoom）中途掉线又连接上后，能否继续接收消息？

可以继续接收消息，但是直播群（AVChatRoom）中的消息不支持云端存储，因此无法拉取到掉线期间的消息。

### 2. 为什么群成员进群和退群收不到通知？

请确认群组类型：
- 临时会议群（Meeting）不支持群成员变更通知。
- 直播群（AVChatRoom）消息限制40条/秒，会优先保证高优先级消息的收发，超过限制后会优先丢弃低优先级的消息。

### 3. 为什么会议群（Meeting） 中的未读数一直为零?

临时会议群（Meeting）和直播群（AVChatRoom）分别配合会议和直播的音视频场景，因此这两类群组均不支持未读消息计数。
