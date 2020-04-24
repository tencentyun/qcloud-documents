您可以对群内某一成员或全体成员禁言并配置禁言时长，在禁言期间被禁言成员不能在当前群内发送消息，该操作只针对当前群有效。禁言期间，被禁言成员退群后重新加入该群禁言依旧有效，直至禁言时间结束或被取消禁言。
本文主要介绍 Web 和小程序端 SDK 中如何对群成员禁言/取消禁言。

## 使用限制

- 群组形态限制
 <table>
<tr>
<th width="25%">私有群</th>
<th width="25%">公开群</th>
<th width="25%">聊天室</th>
<th width="25%">音视频聊天室</th>
</tr>
<tr>
<td><strong>不支持</strong></td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr>
</table>
- 成员角色限制
<table>
<tr>
<th width="25%">成员角色</th>
<th>权限</th>
</tr>
<tr>
<td>App 管理员</td>
<td>支持对当前 SDKAppID 下所有群内的所有成员进行禁言/取消禁言操作</td>
</tr>
<tr>
<td>群主</td>
<td>支持对当前群内的管理员和普通成员进行禁言/取消禁言操作</td>
</tr>
<tr>
<td>群管理员</td>
<td>支持对当前群内的普通成员进行禁言/取消禁言操作</td>
</tr>
<tr>
<td>普通成员</td>
<td>无禁言权限</td>
</tr>
</table>

## 操作步骤

### 步骤1：确认操作权限
1. 调用 [getGroupProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupProfile) 接口查看所在群的类型，确认是否支持禁言/取消禁言操作。
 >!若为 Private（私有群）则不支持禁言。
 >
2. 调用 [getGroupMemberProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberProfile) 接口查看指定的 userID 在当前群的成员角色，确认是否有权限进行禁言/取消禁言操作。

### 步骤2：禁言/取消禁言群成员
#### 禁言/取消禁言单个用户
App 管理员、群主或群管理员调用接口 [setGroupMemberMuteTime](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#setGroupMemberMuteTime) 可禁言/取消禁言指定群组内的指定成员，单次调用仅支持禁言/取消禁言单个群成员。
请求参数如下表所示。

| 名称      | 类型     | 描述    |
| --------- | ------- | --------|
| groupID  | String | 群 ID|
| userID  | String | 群成员 ID|
| muteTime | Number | 禁言时长，单位为秒。设置为0，表示取消禁言|

请求示例如下：
```javascript
let promise = tim.setGroupMemberMuteTime({
  groupID: 'group1',
  userID: 'user1',
  muteTime: 1000
});
```

#### 禁言/取消禁言全体成员
>!使用该功能需将 SDK 升级至2.6.2及以上版本。全体禁言或取消全体禁言，暂无相关的群提示消息下发。
 
App 管理员或群主调用 [updateGroupProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateGroupProfile) 接口可禁言/取消禁言指定群的全体管理员和普通成员。
请求参数如下表所示。

| 名称      | 类型     | 描述    |
| --------- | ------- | --------|
| groupID  | String | 群 ID|
| muteAllMembers | Boolean | 设置禁言，true 表示全体禁言，false 表示取消全体禁言|

请求示例如下：
```javascript
let promise = tim.updateGroupProfile({
  groupID: 'group1',
  muteAllMembers：true, // true 全体禁言，false 取消全体禁言
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group) // 修改成功后的群组详细资料
}).catch(function(imError) {
  console.warn('updateGroupProfile error:', imError); // 修改群组资料失败的相关信息
});
```



### 步骤3：监听处理 TIM.EVENT.MESSAGE_RECEIVED 事件
禁言后，该群成员收到的被禁言 [群提示消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload)，可通过遍历 event.data 获取相关数据并渲染到页面。
>?在收到禁言/取消禁言的相关通知时，建议您自行实现 disable/enable 输入框或输入区域的状态。

<pre>
tim.on(TIM.EVENT.MESSAGE_RECEIVED, function(event) {
  // 收到推送的单聊、群聊、群提示、群系统通知的新消息，可通过遍历 event.data 获取消息列表数据并渲染到页面
  // event.name - TIM.EVENT.MESSAGE_RECEIVED
  // event.data - 存储 Message 对象的数组 - [Message]
  const length = event.data.length;
  let message;
  for (let i = 0; i < length; i++) {
    message = event.data[i];
    switch (message.type) {
      // 禁言用户 A，用户 A 会收到被禁言的群提示消息
      case TIM.TYPES.MSG_GRP_TIP:
        this._handleGroupTip(message);
        break;
      case TIM.TYPES.MSG_TEXT: // 文本消息，更多消息类型请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html">Message</a>
        break;
      default:
        break;
    }
  }
});

_handleGroupTip(message) {
  switch (message.payload.operationType) {
    case TIM.TYPES.GRP_TIP_MBR_PROFILE_UPDATED: // 群成员资料变更，例如：群成员被禁言
      const memberList = message.payload.memberList;
      for (let member of memberList) {
        console.log(`${member.userID} 被禁言${member.muteTime}秒`);
      }
      break;
    case TIM.TYPES.GRP_TIP_MBR_JOIN: // 有成员加群
      break;
    case TIM.TYPES.GRP_TIP_MBR_QUIT: // 有群成员退群
      break;
    case TIM.TYPES.GRP_TIP_MBR_KICKED_OUT: // 有群成员被踢出群
      break;
    case TIM.TYPES.GRP_TIP_GRP_PROFILE_UPDATED: // 群组资料变更
      break;
	default:
	  break;
  }
}
</pre>

### 步骤4：判断禁言状态

- 2.6.2及以上版本 SDK，调用 [getGroupMemberList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberList) 接口可以拉取群成员禁言截止时间戳（muteUntil），您根据该值即可判断群成员是否被禁言，以及禁言的剩余时间。取消禁言后，该群成员的 GroupMember.muteUntil * 1000 <= Date.now()。
```javascript
// 从v2.6.2 起，getGroupMemberList 接口支持拉取群成员禁言截止时间戳。
let promise = tim.getGroupMemberList({ groupID: 'group1', count: 30, offset:0 }); // 从0开始拉取30个群成员
promise.then(function(imResponse) {
  console.log(imResponse.data.memberList); // 群成员列表
  for (let groupMember of imResponse.data.memberList) {
    if (groupMember.muteUntil * 1000  > Date.now()) {
      console.log(`${groupMember.userID} 禁言中`);
    } else {
      console.log(`${groupMember.userID} 未被禁言`);
    }
  }
}).catch(function(imError) {
  console.warn('getGroupMemberProfile error:', imError);
});
```
- 2.6.2以下版本 SDK， 调用 [getGroupMemberProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberProfile) 接口可以查询群成员禁言截止时间戳（muteUntil）等详细资料。
