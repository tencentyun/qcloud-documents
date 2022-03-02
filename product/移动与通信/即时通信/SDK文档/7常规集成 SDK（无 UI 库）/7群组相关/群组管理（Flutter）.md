[](id:type)
## 群类型介绍
即时通信 IM 群组分为以下类型：
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
>- 群组类型有**好友工作群（Work）**、**陌生人社交群（Public）**、**临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom）**五个群组类型。旧版群组类型（Public、Private、ChatRoom、AVChatRoom）中的 Private 类型对应新群组类型 Work（好友工作群），ChatRoom 类型对应新群组类型 Meeting（临时会议群）。
>- 专业版或旗舰版 SDKAppID 下，所有群类型日净增群组数上限为1万个。免费峰值群组数为10万个/月，超出免费量将产生 <a href="https://cloud.tencent.com/document/product/269/11673#jc">套餐外超量费用</a>。
>- 社群（Community）功能仅SDK5.8.1668增强版及以上版本支持，需购买旗舰版套餐包并 [申请开通](https://cloud.tencent.com/document/product/269/3916) 后方可使用。
>- 好友工作群（Work）、陌生人社交群（Public）默认不支持查看入群前消息记录。如需使用此功能，请参见 [配置变更需求工单](https://cloud.tencent.com/document/product/269/3916) 指引提交变更申请。


## 群组管理
[](id:create)
### 创建群组
#### 简化版接口（3.6.0后已弃用）
 [createGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/createGroup.html) （简单创建群组自3.6.0开始弃用，请使用 groupManager 下的高级创建群组）。

#### 高级版接口
如果您想在创建群组的同时初始化群的信息，例如群简介、群头像、以及最初的几个群成员等，可以调用 `V2TIMGroupManager` 管理类中的 [createGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html) 接口实现，其中 `V2TIMGroupManager` 管理类可以通过 `TencentImSDKPlugin.v2TIMManager.getGroupManager()` 获取。


```dart
// 示例代码：使用高级版 createGroup 创建一个工作群 
   List<V2TimGroupMember> list = [];
    for (String userID in memberList) {
      list.add(V2TimGroupMember(userID: userID, role: 200));
    }
    V2TimValueCallback<String> res =
        await TencentImSDKPlugin.v2TIMManager.getGroupManager().createGroup(
              groupType: "Work", // 工作群
              groupName: "groupName",
              groupID: groupID, 
              notification: "notification", // 群通告
              introduction: introduction, // 群介绍
              isAllMuted: false, // 是否全员禁言
              faceUrl: "...",
              addOpt: GroupAddOptTypeEnum.V2TIM_GROUP_ADD_ANY, // 加群权限
              memberList: list, // 创建时加入的成员
            );
```


- 参数 `groupType` 是字符串类型，可以选择 “Work”、“Public”、“Meeting” 、“Community”和 “AVChatRoom” 中的任何一个，各种不同类型之间的差异请参见 [群类型介绍](#type)。
- 参数 `groupID` 用于指定群组 ID，它用于唯一标识一个群，请勿在同一个 SDKAppID 下创建相同 `groupID`  的群。如果您指定 `groupID` 为 null，系统会为您默认分配一个群 ID。
- 参数 `groupName` 用于指定群的描述信息，最长支持30个字节。

[](id:join)
### 加入群组
不同类型的群，加群的方法不同，下面根据加群流程从简单到复杂进行逐一介绍：

| 类型         | 好友工作群（Work）| 陌生人社交群（Public）| 临时会议群（Meeting）| 社群（Community）|直播群（AVChatRoom）|
|---------|---------|---------|---------|---------|---------|
| 加群方法 | 必须由其他群成员邀请 | 用户申请，群主或管理员审批 | 用户可随意加入 |用户可随意加入 | 用户可随意加入 |

#### 场景一：用户可以自由进出群
临时会议群（Meeting）和直播群（AVChatRoom）主要用于满足成员进进出出的交互场景，例如在线会议，秀场直播等。因此，这两种类型群的入群流程最为简单。

用户调用 [joinGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html) 即可加入该群，加群成功后，全体群成员（包括加群者）都会收到 [onMemberEnter](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberEnter.html) 回调。 

#### 场景二：需被邀请才能进入群
好友工作群（Work）类似微信群和企业微信群，适用于工作交流，在交互设计上限制用户主动加入，只能由现有的群成员邀请才能加群。

现有的群成员调用 [inviteUserToGroup](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/inviteUserToGroup.html) 邀请另一个用户入群，全体群成员（包括邀请者自己）会收到 [onMemberInvited](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberInvited.html) 回调。

#### 场景三：需要审批才能进入群
陌生人社交群（Public）类似 QQ 中的各种兴趣群和部落区，任何人都可以申请入群，但需要经过群主或管理员审批才能真正入群。陌生人社交群默认需要群主或管理员进行审批才能加群的，但群主或管理员也可以通过 [setGroupInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/setSelfInfo.html) 接口调整加群选项（`GroupAddOptType`），可以设置为更严格的“禁止任何人加群”，也可以设置为更宽松的“放开审批流程”。
- GroupAddOptTypeEnum.V2TIM_GROUP_ADD_FORBID ：禁止任何人加群。
- GroupAddOptTypeEnum.V2TIM_GROUP_ADD_AUTH ：需要群主或管理员审批才能加入（默认值）。
- GroupAddOptTypeEnum.V2TIM_GROUP_ADD_ANY ：取消审批流程，任何用户都可以加入。

需要审批才能进入群的流程如下：
![](https://main.qcloudimg.com/raw/8b0de43bea607a6a75571c1885ca75aa.svg)

1. **申请者提出加群申请**
申请者调用 [joinGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html) 申请加群。
2. **群主或管理员处理加群申请**
群主或管理员在收到加群申请的回调 [onReceiveJoinApplication](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onReceiveJoinApplication.html) 后调用接口 [getGroupApplicationList](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/getGroupApplicationList.html) 获取加群申请列表，然后通过 [acceptGroupApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/acceptGroupApplication.html) 或者 [refuseGroupApplication](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/refuseGroupApplication.html) 来同意或者拒绝某一条加群请求。
3. **申请者收到处理结果**
 请求加群被同意或者拒绝后，请求者会收到  [V2TimGroupListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener-class.html) 中的 [onApplicationProcessed](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onApplicationProcessed.html) 回调，其中 `isAgreeJoin` 为 `true` 表示同意加群，反之被拒绝。同意加群后，全员（包括请求者）收到 [onMemberEnter](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberEnter.html) 回调。



[](id:quit)
### 退出群组
调用 [quitGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/quitGroup.html) 可以退出群组，退群者会收到 [onQuitFromGroup](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onQuitFromGroup.html) 回调，群其他成员会收到 [onMemberLeave](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberLeave.html) 回调。
>?对于陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom），群主不可以退群的，群主只能 [解散群组](#dismiss)。

[](id:dismiss)
### 解散群组
调用 [dismissGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/dismissGroup.html) 可以解散群组，全员会收到  [onGroupDismissed](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupDismissed.html) 回调。

>?
>- 对于陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）和直播群（AVChatRoom），群主随时可以解散群。
>- 好友工作群（Work）的解散最为严格，即使群主也不能随意解散，只能由您的业务服务器调用 [解散群组 REST API](https://cloud.tencent.com/document/product/269/1624) 解散。


### 获取已加入的群组
调用 [getJoinedGroupList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedGroupList.html) 可以获取已加入的好友工作群（Work）、陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）列表，但直播群（AVChatRoom）不包含在此列表中。

## 群资料和群设置
### 获取群资料
调用 [getGroupsInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getJoinedGroupList.html) 可以获取群资料，该接口支持批量获取。您可以一次传入多个 `groupID` 获取多个群的群资料。

### 修改群资料
调用 [setGroupInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupInfo.html) 可以修改群资料。群资料被修改后，全员会收到 [onGroupInfoChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupInfoChanged.html) 回调。
>?
> - 好友工作群（Work）所有群成员都可以修改群基础资料。
> - 陌生人社交群（Public）、临时会议群（Meeting）、社群（Community）只有群主或管理员可以修改群基础资料。
> - 直播群（AVChatRoom）只有群主可以修改群基础资料。

```dart
// 示例代码：修改群资料
 V2TimCallback res =
        await TencentImSDKPlugin.v2TIMManager.getGroupManager().setGroupInfo(
              info: V2TimGroupInfo.fromJson(  // 传入V2TimGroupInfo类型
                {
                  "groupID": : "需要修改的ID",
                  "groupName": "需要修改的的名字",
                  "groupType": "Work",
                  "notification": "notification",
                  "introduction": "introduction",
                  "faceUrl": faceUrl,
                  "isAllMuted": false,
                  "addOpt": GroupAddOptType.V2TIM_GROUP_ADD_ANY,
                  "customInfo": Map(),
                },
              ),
            );
```

### 设置群消息的接收选项
任何群成员都可以调用 [setGroupReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/setGroupReceiveMessageOpt.html) 接口修改群消息接收选项。群消息接收选项包括：
- ReceiveMsgOptEnum.V2TIM_RECEIVE_MESSAGE：在线正常接收消息，离线时会有厂商的离线推送通知。
- ReceiveMsgOptEnum.V2TIM_NOT_RECEIVE_MESSAGE：不会接收到群消息。
- ReceiveMsgOptEnum.V2TIM_RECEIVE_NOT_NOTIFY_MESSAGE：在线正常接收消息，离线不会有推送通知。

根据群消息接收选择可以实现群消息免打扰：
- **完全不接收群内消息**
群消息接收选项设置为 `ReceiveMsgOptEnum.V2TIM_NOT_RECEIVE_MESSAGE` 后，群内的任何消息都收不到，会话列表也不会更新。
- **接收群内消息但不提醒，在会话列表界面显示小圆点，而不显示未读数**
>?此方式需使用未读计数功能，因此仅适用于好友工作群（Work）和陌生人社交群（Public）。
>
群消息接收选项设置为 `ReceiveMsgOptEnum.V2TIM_RECEIVE_MESSAGE`，当群内收到新消息，会话列表需要更新时，可以通过会话中的  [unreadCount](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_conversation/V2TimConversation/unreadCount.html) 获取到消息未读数。根据 [recvOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_info/V2TimGroupInfo/recvOpt.html) 判断获取到的群消息接收选项为 `ReceiveMsgOptEnum.V2TIM_RECEIVE_MESSAGE` 时显示小红点而非消息未读数。

## 群属性（群自定义字段）
我们设计了全新的群自定义字段，我们称之为 "群属性"，其特性如下：
1. 不再需要控制台配置，客户端可以直接增删改查群属性。
2. 最多支持16个群属性，每个群属性的大小最大支持4k，所有群属性的大小最大支持16k。
3. 目前仅支持直播群（AVChatRoom）。
4. initGroupAttributes、setGroupAttributes、deleteGroupAttributes 接口合并计算， SDK 限制为5秒10次，超过后回调8511错误码；后台限制1秒5次，超过后返回10049错误码。
5. getGroupAttributes 接口 SDK 限制5秒20次。

基于群属性，我们可以做语聊房的麦位管理，当有人上麦的时候，可以设置一个群属性管理上麦人信息，当有人下麦的时候，可以删除对应群属性，其他成员可以通过获取群属性列表来展示麦位列表。

### 初始化群属性
调用 [initGroupAttributes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/initGroupAttributes.html) 接口可以初始化群属性，如果该群之前有群属性，会先清空原来的群属性。

### 设置群属性

调用 [setGroupAttributes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupAttributes.html) 接口可以设置群属性，如果设置的群属性不存在，会自动添加该群属性。

### 删除群属性
调用 [deleteGroupAttributes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/deleteGroupAttributes.html) 接口可以删除指定群属性，如果 `keys` 字段填 `null` ，则会清空所有的群属性。

### 获取群属性
调用 [getGroupAttributes](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupAttributes.html) 接口可以获取指定群属性，如果 `keys` 字段填 `null` ，则会获取所有的群属性。

### 群属性更新
群属性有任何的更新变化，都会通过 [onGroupAttributeChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupAttributeChanged.html) 回调出来所有的群属性字段。

##  群成员管理
### 获取群成员列表
调用 [getGroupMemberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) 可以获取某个群的群成员列表，该列表中包含了各个群成员的资料信息，例如用户ID（`userID`）、群名片（`nameCard`）、头像（`faceUrl`）、昵称（`nickName`）、进群时间（`joinTime`）等信息。
一个群中的成员人数可能很多（例如5000+），群成员列表的拉取接口支持过滤器（`filter`）和分页拉取（`nextSeq`）两个高级特性。

#### 过滤器（filter）
在调用  [getGroupMemberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) 接口时，您可以指定 `filter` 确定是否仅拉取特定角色的信息列表。

| 过滤器 | 过滤类型 |
|---------|---------|
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ALL | 拉取所有群成员的信息列表 |
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_OWNER | 仅拉取群主的信息列表|
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ADMIN | 仅拉取群管理员的信息列表|
| GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_COMMON | 仅拉取普通群成员的信息列表|

```dart
//示例代码：通过 filter 参数指定只拉取群主的资料
 await TencentImSDKPlugin.v2TIMManager
            .getGroupManager()
            .getGroupMemberList(
              groupID: "你要传的groupId",
              filter: GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_OWNER,
              nextSeq: "0",
            );
```

#### 分页拉取（nextSeq）
很多情况下，用户界面上并不需要展示全部的群成员信息，只需展示群成员列表的第一页即可，等用户单击**下一页**或在列表页下拉刷新时，才需要拉取更多的群成员。针对此类场景，您可以使用分页拉取。

在调用 [getGroupMemberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) 接口时，一次最多返回50个成员，您可以通过 `nextSeq` 参数分页拉取成员列表，`nextSeq`参数为分页拉取标志，第一次拉取时请填0。当首次拉取群成员信息成功后，`getGroupMemberList` 的回调结果 [V2TIMGroupMemberInfoResult](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_info_result/V2TimGroupMemberInfoResult-class.html) 中会包含 [nextSeq](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_info_result/V2TimGroupMemberInfoResult/nextSeq.html) 接口。
- 如果 [nextSeq](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_info_result/V2TimGroupMemberInfoResult/nextSeq.html) 返回0，表示已经拉取全部的群成员列表。
- 如果 [nextSeq](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_info_result/V2TimGroupMemberInfoResult/nextSeq.html)  返回 >0 的数值，表示还有更多的群成员信息可以拉取。您可以根据用户在 UI 上的操作，选择是否进行第二次接口调用以拉取更多的群成员信息。当您进行第二次拉取时，需要将上一次拉取返回的 `V2TIMGroupMemberInfoResult` 中的  [nextSeq](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_info_result/V2TimGroupMemberInfoResult-class.html)  作为参数，传入  [getGroupMemberList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMemberList.html) 接口。

```dart
//示例代码：通过 nextSeq 参数进行分页拉取
  String nextSeq = "0";
  getGroupMemberList(String nextSeq) async {
    V2TimValueCallback<V2TimGroupMemberInfoResult> res =
        await TencentImSDKPlugin.v2TIMManager
            .getGroupManager()
            .getGroupMemberList(
              groupID: "你要传的groupId",
              filter: GroupMemberFilterTypeEnum.V2TIM_GROUP_MEMBER_FILTER_ALL,
              nextSeq: nextSeq,
            );
    setState(() {
      resData = res.toJson();
      if (res.data != null) {
        nextSeq = res.data!.nextSeq!;
		// ...
      }
    });
  }
```


### 获取群成员资料
调用 [getGroupMembersInfo](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/getGroupMembersInfo.html) 可以获取群成员资料，该接口支持批量获取，您可以一次传入多个 `userID` 获取多个群成员的资料，从而提升网络传输效率。

### 修改群成员资料
群主或管理员可以调用 [setGroupMemberInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/setGroupMemberInfo.html) 接口修改群成员的群名片（`nameCard`）、 群成员角色（`role`）、禁言时间（`muteUntil`）以及自定义字段等与群成员相关的资料。

[](id:mute)
### 禁言
群主或管理员可以通过 [muteGroupMember](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/muteGroupMember.html) 禁言某一个群成员并设置禁言时间，禁言时间单位为秒，禁言信息存储于群成员的 [muteUtil](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_full_info/V2TimGroupMemberFullInfo/muteUntil.html) 属性字段中。群成员被禁言后，全员（包括被禁言的群成员）都会收到 [onMemberInfoChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberInfoChanged.html) 事件回调。
群主或管理员也可以通过 [setGroupInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/setGroupInfo.html) 接口对整个群进行禁言，将 [isAllMuted](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_info/V2TimGroupInfo/isAllMuted.html) 属性字段设置为 `true` 即可。全群禁言没有时间限制，需通过将群资料 `setAllMuted(false)` 解除禁言。


[](id:kick)
### 踢人
群主或管理员调用 [kickGroupMember](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/kickGroupMember.html) 接口可以实现踢人。由于直播群（AVChatRoom）对进群没有限制，因此直播群（AVChatRoom）没有支持踢人的接口，您可以使用 [muteGroupMember](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/method_channel_im_flutter/MethodChannelIm/muteGroupMember.html) 达到同样的目的。
成员被踢后，全员（包括被踢人）会收到 [onMemberKicked](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onMemberKicked.html) 回调。

### 切换群成员角色
群主调用 [setGroupMemberRole](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/setGroupMemberRole.html) 可以对陌生人社交群（Public）或临时会议群（Meeting）中的群成员进行角色切换，可切换角色包括普通成员、管理员。
- 被设置为管理员后，全员（包括被设置的成员）会收到 [onGrantAdministrator](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onGrantAdministrator.html)  回调。
- 被取消管理员后，全员（包括被设置的成员）会收到 [onRevokeAdministrator](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onRevokeAdministrator.html) 回调。

[](id:transfer)
### 转让群主
群主可以调用 [transferGroupOwner](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/transferGroupOwner.html) 把群主转让给其他群成员。
群主转让后，全员会收到 [onGroupInfoChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimGroupListener/V2TimGroupListener/onGroupInfoChanged.html) 回调，其中 `V2TIMGroupChangeInfo` 的 type 为 `GroupChangeInfoType.V2TIM_GROUP_INFO_CHANGE_TYPE_OWNER`，value 值为新群主的 UserID。

## 常见问题

### 1. 直播群（AVChatRoom）中途掉线又连接上后，能否继续接收消息？
可以继续接收消息，但是直播群（AVChatRoom）中的消息不支持云端存储，因此无法拉取到掉线期间的消息。

### 2. 为什么群成员进群和退群收不到通知？
请确认群组类型：
- 临时会议群（Meeting）不支持群成员变更通知。
- 直播群（AVChatRoom）消息限制40条/秒，会优先保证高优先级消息的收发，超过限制后会优先丢弃低优先级的消息。

### 3. 为什么会议群（Meeting） 中的未读数一直为零?
临时会议群（Meeting）和直播群（AVChatRoom）分别配合会议和直播的音视频场景，因此这两类群组均不支持未读消息计数。
