## 群组综述

即时通信 IM 有多种群组类型，其特点以及限制因素可参考 [群组系统](https://cloud.tencent.com/doc/product/269/群组系统)。群组使用唯一 ID 标识，通过群组 ID 可以进行不同操作。

## 群组管理

### 获取加入的群组列表
需要渲染或刷新【我的群组列表】时，调用该接口获取群组列表，更多详情请参见 [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)。

**接口名**

```js
tim.getGroupList();
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称                    | 类型           | 属性 | 描述                                                         |
| :---------------------- | :------------- | :--- | :----------------------------------------------------------- |
| `groupProfileFilter` | `Array<String>` |`<optional>`  | 群资料过滤器。除默认拉取的群资料外，指定需要额外拉取的群资料，支持的值如下：<br/>TIM.TYPES.GRP_PROFILE_OWNER_ID：群主 ID<br/>TIM.TYPES.GRP_PROFILE_CREATE_TIME：群创建时间<br/>TIM.TYPES.GRP_PROFILE_LAST_INFO_TIME：最后一次群资料变更时间<br/>TIM.TYPES.GRP_PROFILE_MEMBER_NUM：群成员数量<br/>TIM.TYPES.GRP_PROFILE_MAX_MEMBER_NUM：最大群成员数量<br/>TIM.TYPES.GRP_PROFILE_JOIN_OPTION：申请加群选项<br/>TIM.TYPES.GRP_PROFILE_INTRODUCTION：群介绍<br/>TIM.TYPES.GRP_PROFILE_NOTIFICATION：群公告 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**
- 默认拉取：
```js
// 该接口默认只拉取这些资料：群类型、群名称、群头像以及最后一条消息的时间。
let promise = tim.getGroupList();
promise.then(function(imResponse) {
  console.log(imResponse.data.groupList); // 群组列表
}).catch(function(imError) {
  console.warn('getGroupList error:', imError); // 获取群组列表失败的相关信息
});
```
- 拉取其他资料：
```js
// 若默认拉取的字段不满足需求，可以参考下述代码，拉取额外的资料字段。
let promise = tim.getGroupList({
   groupProfileFilter: [TIM.TYPES.GRP_PROFILE_OWNER_ID],
});
promise.then(function(imResponse) {
  console.log(imResponse.data.groupList); // 群组列表
}).catch(function(imError) {
  console.warn('getGroupList error:', imError); // 获取群组列表失败的相关信息
});
```

### 获取群详细资料

更多详情请参见 [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)。

**接口名**

```js
tim.getGroupProfile(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称                    | 类型           | 属性 | 描述                                                         |
| :---------------------- | :------------- | :--- | :----------------------------------------------------------- |
| `groupID  `               | `String`         |-  | 群组 ID                                                       |
| `groupCustomFieldFilter`  | `Array<String>` | `<optional>` | 群组的自定义字段过滤器，指定需要获取的群组的自定义字段，详情请参见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中获取群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getGroupProfile({
  groupID: 'group1',
  groupCustomFieldFilter: ['key1','key2']
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group);
}).catch(function(imError) {
  console.warn('getGroupProfile error:', imError); // 获取群详细资料失败的相关信息
});
```



### 创建群组

更多详情请参见 [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)。

>!该接口创建 TIM.TYPES.GRP_AVCHATROOM（音视频聊天室） 后，需调用 [joinGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#joinGroup) 接口加入群组后，才能进行消息收发流程。

**接口名**

```js
tim.createGroup(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称             | 类型           | 属性       | 默认值                               | 描述                                                         |
| :--------------- | :------------- | :--------- | :----------------------------------- | :----------------------------------------------------------- |
| `name`           | `String`         |       -     |                        -              | 必填，群组名称，最长30字节                                   |
| `type`             | `String`         | `<optional>` | `TIM.TYPES.GRP_PRIVATE`              | 群组类型，包括： <li>TIM.TYPES.GRP_PRIVATE：私有群，默认</li><li>TIM.TYPES.GRP_PUBLIC：公开群</li><li>TIM.TYPES.GRP_CHATROOM：聊天室</li><li>TIM.TYPES.GRP_AVCHATROOM：互动直播聊天室</li> |
| `groupID`          | `String`         | `<optional>` |                      -                | 群组 ID。不填该字段时，会自动为群组创建一个唯一的群 ID        |
| `introduction`     | `String`         | `<optional>` |                  -                    | 群简介，最长240字节                                          |
| `notification`    | `String`         | `<optional>` |                      -                | 群公告，最长300字节                                          |
| `avatar`           | `String`         | `<optional>` |                 -                     | 群头像 URL，最长100字节                                      |
| `maxMemberNum`     | `Number`         | `<optional>` |                      -                | 最大群成员数量，默认值：私有群为200，公开群为2000，聊天室为6000，音视频聊天室无限制 |
| `joinOption`       | `String`         | `<optional>` | `TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS` | 申请加群处理方式。**创建私有群/聊天室/音视频聊天室时不能填写该字段。**私有群该字段固定为：禁止申请加群，聊天室和音视频聊天室该字段固定为：自由加入<br><li>TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS：自由加入</li><li>TIM.TYPES.JOIN_OPTIONS_NEED_PERMISSION：需要验证</li><li>TIM.TYPES.JOIN_OPTIONS_DISABLE_APPLY：禁止加群</li> |
| `memberList`       | `Array<Object>` | `<optional>`|                            -          | 初始群成员列表，最多500个。创建音视频聊天室时不能添加成员。详情请参见下方 [memberList 参数说明](#memberList) |
| `groupCustomField` | `Array<Object>` | `<optional>` |                     -                 | 群组维度的自定义字段，默认没有自定义字段，如需开通请参见 [群成员资料](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

<span id="memberList"></span>
`memberList` 参数说明

| 名称                | 类型           | 属性 | 描述                                                  |
| :------------------ | :------------- | :--------- | :----------------------------------------------------------- |
| `userID    `        | `String`         |      -      | 必填，群成员的 UserID                                        |
| `role  `            | `String`         | `<optional>` | 成员身份，可选值只有 Admin，表示添加该成员并设置为管理员      |
| `memberCustomField` | `Array<Object>` | `<optional>` | 群成员维度的自定义字段，默认没有自定义字段，如需开通请参见 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中获取群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
// 创建私有群
let promise = tim.createGroup({
  type: TIM.TYPES.GRP_PRIVATE,
  name: 'WebSDK',
  memberList: [{userID: 'user1'}, {userID: 'user2'}] // 如果填写了 memberList，则必须填写 userID
});
promise.then(function(imResponse) { // 创建成功
  console.log(imResponse.data.group); // 创建的群的资料
}).catch(function(imError) {
  console.warn('createGroup error:', imError); // 创建群组失败的相关信息
});
```

### 解散群组

群主可调用该接口解散群组。
>!群主不能解散私有群。

**接口名**

```js
tim.dismissGroup(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回`Promise`对象：
- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupID`中获取被解散的群组 ID。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.dismissGroup('group1');
promise.then(function(imResponse) { // 解散成功
  console.log(imResponse.data.groupID); // 被解散的群组 ID
}).catch(function(imError) {
  console.warn('dismissGroup error:', imError); // 解散群组失败的相关信息
});
```

### 更新群组资料

**接口名**

```js
tim.updateGroupProfile(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称               | 类型           | 属性       | Default                              | 描述                                                         |
| :----------------- | :------------- | :--------- | :----------------------------------- | :----------------------------------------------------------- |
| `groupID`          | `Object`         |       -     |                    -                  |   群组 ID                                                      |
| `name`             | `Object`         | `<optional>` |                -                      | 群名称，最长30字节                                           |
| `avatar`           | `Object`         | `<optional>` |                -                      | 群头像 URL，最长100字节                                       |
| `introduction`     | `Object`         | `<optional>` |                       -               | 群简介，最长240字节                                          |
| `notification`     | `Object`         | `<optional>` |                    -                  | 群公告，最长300字节                                          |
| `maxMemberNum`     | `Number`         | `<optional>` |                      -                | 最大群成员数量，最大为6000                                   |
| `joinOption`       | `String`         | `<optional>` | `TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS` | 申请加群处理方式<br>**修改私有群/聊天室/音视频聊天室的群资料时不能设置该字段**，私有群该字段固定为：禁止申请加群，聊天室和音视频聊天室该字段固定为：自由加入<li>TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS：自由加入</li><li>TIM.TYPES.JOIN_OPTIONS_NEED_PERMISSION：需要验证</li><li>TIM.TYPES.JOIN_OPTIONS_DISABLE_APPLY：禁止加群</li> |
| `groupCustomField` | `Array<Object>` | `<optional>` |                 -                     | 群自定义字段，详情请参见下方[`groupCustomField`参数说明](#groupCustomField)<br>默认没有自定义字段，如需开通请参见  [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

<span id="groupCustomField"></span>
`groupCustomField`参数说明

| 名称    | 类型   | 描述              |
| :------ | :----- | :---------------- |
| `key`   | `String` | 自定义字段的 Key   |
| `value` | `String` | 自定义字段的 Value |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中获取修改后的群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.updateGroupProfile({
  groupID: 'group1',
  name: 'new name', // 修改群名称
  introduction: 'this is introduction.', // 修改群公告
  // v2.6.0 起，群成员能收到群自定义字段变更的群提示消息，且能获取到相关的内容，详见 Message.payload.newGroupProfile.groupCustomField
  groupCustomField: [{ key: 'group_level', value: 'high'}] // 修改群组维度自定义字段
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group) // 修改成功后的群组详细资料
}).catch(function(imError) {
  console.warn('updateGroupProfile error:', imError); // 修改群组资料失败的相关信息
});
```

### 申请加群

私有群不能申请加入，只能由群成员邀请加入。

**接口名**

```js
tim.joinGroup(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称           | 类型   | 属性       | 描述                                                         |
| :------------- | :----- | :--------- | :----------------------------------------------------------- |
| `groupID`      | `String` |     -       |                       -                                       |
| `applyMessage` | `String` |    -        | 附言                                                         |
| `type`         | `String` | `<optional>` | 待加入的群组的类型，加入音视频聊天室时该字段必填。可选值：<br/><li>TIM.TYPES.GRP_PUBLIC：公开群</li><li>TIM.TYPES.GRP_CHATROOM：聊天室</li><li>TIM.TYPES.GRP_AVCHATROOM：音视频聊天室</li> |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`中包括的属性值如下表所示：
	<table>
     <tr>
         <th>名称</th>  
         <th>含义</th>
     </tr>
	 <tr>
	     <td>status</td>   
	     <td>加群的状态。包括：<ul><li>TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL：等待管理员审核</li><li>TIM.TYPES.JOIN_STATUS_SUCCESS：加群成功</li><li>TIM.TYPES.JOIN_STATUS_ALREADY_IN_GROUP：已在群中</li></ul></td>
     </tr> 
	 <tr>
	     <td>group</td>   
	     <td>加群成功后的群组资料</td>   
     </tr> 
</table>

- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.joinGroup({ groupID: 'group1', type: TIM.TYPES.GRP_AVCHATROOM });
promise.then(function(imResponse) {
  switch (imResponse.data.status) {
    case TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL: break; // 等待管理员同意
    case TIM.TYPES.JOIN_STATUS_SUCCESS: // 加群成功
      console.log(imResponse.data.group); // 加入的群组资料
      break;
    default: break;
  }
}).catch(function(imError){
  console.warn('joinGroup error:', imError); // 申请加群失败的相关信息
});
```

### 退出群组

群主只能退出私有群，退出后该私有群无群主。

**接口名**

```js
tim.quitGroup(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.groupID`为退出的群组 ID。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.quitGroup('group1');
promise.then(function(imResponse) {
  console.log(imResponse.data.groupID); // 退出成功的群 ID
}).catch(function(imError){
  console.warn('quitGroup error:', imError); // 退出群组失败的相关信息
});
```

### 根据群 ID 搜索群组

私有群不能被搜索。

**接口名**

```js
tim.searchGroupByID(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.searchGroupByID('group1');
promise.then(function(imResponse) {
  const group = imResponse.data.group; // 群组信息
}).catch(function(imError) {
  console.warn('searchGroupByID error:', imError); // 搜素群组失败的相关信息
});
```

### 转让群组
只有群主拥有转让的权限，音视频聊天室不能转让。

**接口名**

```js
tim.changeGroupOwner(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称         | 类型   | 描述            |
| :----------- | :----- | :-------------- |
| `groupID`    | `String` | 待转让的群组 ID |
| `newOwnerID` | `String` | 新群主的 ID     |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.changeGroupOwner({
  groupID: 'group1',
  newOwnerID: 'user2'
});
promise.then(function(imResponse) { // 转让成功
  console.log(imResponse.data.group); // 群组资料
}).catch(function(imError) { // 转让失败
  console.warn('changeGroupOwner error:', imError); // 转让群组失败的相关信息
});
```

### 处理加群申请

当用户申请加入一个需要管理员同意的群组时，管理员/群主会收到申请加群的【群系统通知消息】，详情请参见 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。

**接口名**

```js
tim.handleGroupApplication(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称            | 类型                                             | 属性       | 描述                                                         |
| :-------------- | :--------------------- | :--------- | :----------------------------------------------- |
| `handleAction`  | `String `               |       -     | 处理结果 Agree（同意） / Reject（拒绝）                          |
| `handleMessage` | `String`                       | `<optional>` | 附言                                                         |
| `message`       | [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) |      -      | 申请加群的【群系统通知消息】的消息实例。该实例可通过以下方式获取：<li><a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECERIVED">收到新的群系统通知事件</a> 的回调参数中获取</li><li>系统类型会话的消息列表中获取</li> |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.handleGroupApplication({
  handleAction: 'Agree',
  handleMessage: '欢迎欢迎',
  message: message // 申请加群群系统通知的消息实例
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 群组资料
}).catch(function(imError){
  console.warn('handleGroupApplication error:', imError); // 错误信息
});
```

### 设置群消息提示类型

**接口名**

```js
tim.setMessageRemindType(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称                | 类型   | 描述                                                         |
| :------------------ | :----- | :----------------------------------------------------------- |
| `groupID`           | `String` | 群组 ID                                                      |
| `messageRemindType` | `String` | 群消息提示类型。详细如下：<li>TIM.TYPES.MSG_REMIND_ACPT_AND_NOTE：SDK 接收消息并抛出 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED">收到消息事件</a> 通知接入侧，接入侧做提示</li><li>TIM.TYPES.MSG_REMIND_ACPT_NOT_NOTE：SDK 接收消息并抛出 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED">收到消息事件</a> 通知接入侧，接入侧不做提示</li><li>TIM.TYPES.MSG_REMIND_DISCARD：SDK 拒收消息，不会抛出 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED">收到新消息事件</a></li>|

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setMessageRemindType({ groupID: 'group1', messageRemindType: TIM.TYPES.MSG_REMIND_DISCARD }); // 拒收消息
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
}).catch(function(imError) {
  console.warn('setMessageRemindType error:', imError);
});
```

## 群成员管理

### 获取群成员列表

>!
>- 从v2.6.2版本开始，该接口支持拉取群成员禁言截止时间戳（muteUntil），接入侧可根据此值判断群成员是否被禁言，以及禁言的剩余时间。
>- 低于v2.6.2版本时，该接口获取的群成员列表中的资料仅包括头像、昵称等，能够满足群成员列表的渲染需求。如需查询群成员禁言截止时间戳（muteUntil）等详细资料，请使用 [getGroupMemberProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupMemberProfile)。
>- 该接口是分页拉取群成员，不能直接用于获取群的总人数。获取群的总人数（memberNum）请使用 [getGroupProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupProfile) 。

**接口名**

```js
tim.getGroupMemberList(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称      | 类型     | 属性          | 默认值 | 描述                                                         |
| :-------- | :------- | :------------ | :----- | :--------------------------- |
| `groupID` | `String` |      -         |   -     | 群组的 ID                                                    |
| `count`   | `Number` | `<optional> ` | `15`   | 需要拉取的数量。最大值为100，避免回包过大导致请求失败。若传入超过100，则只拉取前100个 |
| `offset`  | `Number` | `<optional> ` | `0`    | 偏移量，默认从0开始拉取                                      |

**返回值**

该接口返回`Promise`对象：

- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.memberList`为群成员列表，请参考 [GroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/GroupMember.html)。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```javascript
let promise = tim.getGroupMemberList({ groupID: 'group1', count: 30, offset:0 }); // 从0开始拉取30个群成员
promise.then(function(imResponse) {
  console.log(imResponse.data.memberList); // 群成员列表
}).catch(function(imError) {
  console.warn('getGroupMemberList error:', imError);
});
// 从v2.6.2 起，该接口支持拉取群成员禁言截止时间戳。
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

### 获取群成员资料

>!
>- 使用该接口前，需要将 SDK 版本升级至v2.2.0或以上。
>- 每次查询的用户数上限为50。如果传入的数组长度大于50，则只取前50个用户进行查询，其余丢弃。 

**接口名**

```js
tim.getGroupMemberProfile(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称                      | 类型             | 属性          | 描述                                                         |
| :------------------------ | :--------------- | :------------ | :----------------------------------------------------------- |
| `groupID`                 | `String`         |         -     | 群组的 ID                                                    |
| `userIDList`              | `Array.<String>` |         -     | 要查询的群成员用户 ID 列表                                   |
| `memberCustomFieldFilter` | `Array.<String>` | `<optional> ` | 群成员自定义字段筛选。可选，若不填，则默认查询所有群成员自定义字段 |

**返回值**

该接口返回`Promise`对象：

- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.memberList`为查询成功的群成员列表，请参考 [GroupMember](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/GroupMember.html)。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

### 添加群成员

详细规则如下：
-  TIM.TYPES.GRP_PRIVATE 私有群：任何群成员都可邀请他人加群，且无需被邀请人同意，直接将其拉入群组中。
-  TIM.TYPES.GRP_PUBLIC 公开群/ TIM.TYPES.GRP_CHATROOM 聊天室：只有 App 管理员可以邀请他人入群，且无需被邀请人同意，直接将其拉入群组中。
-  TIM.TYPES.GRP_AVCHATROOM 音视频聊天室：不允许任何人邀请他人入群（包括 App 管理员）。

**接口名**

```js
tim.addGroupMember(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称         | 类型           | 描述                                          |
| :----------- | :------------- | :-------------------------------------------- |
| `groupID`    | `String`         | 群组 ID                                       |
| `userIDList` | `Array<String>` | 待添加的群成员 ID 数组。单次最多添加500个成员 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`属性值如下表所示：
	<table>
     <tr>
         <th nowrap="nowrap">名称</th>  
         <th>类型</th>  
         <th  nowrap="nowrap">含义</th>  
     </tr>
	 <tr>      
         <td>successUserIDList</td>   
	     <td>Array&#60;String&#62;</td>   
	     <td>添加成功的 userID 列表</td>   
     </tr> 
	 <tr>      
         <td>failureUserIDList</td>   
	     <td>Array&#60;String&#62;</td>   
	     <td>添加失败的 userID 列表</td>   
     </tr> 
	 <tr>      
         <td>existedUserIDList</td>   
	     <td>Array&#60;String&#62;</td>   
	     <td>已在群中的 userID 列表</td>   
     </tr> 
	 <tr>      
         <td>group</td>   
	     <td><a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html">Group</a></td>   
	     <td>接口调用后的群组资料</td>   
     </tr> 
</table>

- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.addGroupMember({
  groupID: 'group1',
  userIDList: ['user1','user2','user3']
});
promise.then(function(imResponse) {
  console.log(imResponse.data.successUserIDList); // 添加成功的群成员 userIDList
  console.log(imResponse.data.failureUserIDList); // 添加失败的群成员 userIDList
  console.log(imResponse.data.existedUserIDList); // 已在群中的群成员 userIDList
  console.log(imResponse.data.group); // 添加后的群组信息
}).catch(function(imError) {
  console.warn('addGroupMember error:', imError); // 错误信息
});
```



### 删除群成员

删除群成员。群主可移除群成员。

**接口名**

```js
tim.deleteGroupMember(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称         | 类型           | 描述                     |
| :----------- | :------------- | :----------------------- |
| `groupID`    | `String`         | 群组 ID                  |
| `userIDList` | `Array<String>` | 待删除的群成员的 ID 列表 |
| `reason`     | `String`         | 踢人的原因，可选参数         |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为更新后的群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.deleteGroupMember({groupID: 'group1', userIDList:['user1'], reason: '你违规了，我要踢你！'});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 删除后的群组信息
  console.log(imResponse.data.userIDList); // 被删除的群成员的 userID 列表
}).catch(function(imError) {
  console.warn('deleteGroupMember error:', imError); // 错误信息
});
```



### 禁言或取消禁言

设置群成员的禁言时间，可以禁言群成员，也可取消禁言。TIM.TYPES.GRP_PRIVATE 类型的群组（即私有群）不能禁言。
>?只有群主和管理员拥有该操作权限：
>- 群主可以禁言/取消禁言管理员和普通群成员。
>- 管理员可以禁言/取消禁言普通群成员。

**接口名**

```js
tim.setGroupMemberMuteTime(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称       | 类型   | 描述                                                         |
| :--------- | :----- | :----------------------------------------------------------- |
| `groupID`  | `String` | 群组 ID                                                      |
| `userID`   | `String` | 群成员 ID                                                    |
| `muteTime` | `Number` | 禁言时长，单位秒<br>例如，设置该值为1000，则表示即刻起禁言该用户1000秒，设置为0，则表示取消禁言 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberMuteTime({
  groupID: 'group1',
  userID: 'user1',
  muteTime: 600 // 禁言10分钟；设为0，则表示取消禁言
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 修改后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberMuteTime error:', imError); // 禁言失败的相关信息
});
```



### 设为管理员或撤销管理员

修改群成员角色，只有群主拥有操作权限。

**接口名**

```js
tim.setGroupMemberRole(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称      | 类型   | 描述                                                         |
| :-------- | :----- | :----------------------------------------------------------- |
| `groupID` | `String` | 群组 ID                                                      |
| `userID`  | `String` | 群成员 ID                                                    |
| `role`    | `String` | 可选值：`TIM.TYPES.GRP_MBR_ROLE_ADMIN`（群管理员）或 `TIM.TYPES.GRP_MBR_ROLE_MEMBER`（群普通成员） |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberRole({
  groupID: 'group1',
  userID: 'user1',
  role: TIM.TYPES.GRP_MBR_ROLE_ADMIN // 将群 ID: group1 中的用户：user1 设为管理员
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 修改后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberRole error:', imError); // 错误信息
});
```



### 修改群名片

设置群成员名片。
- 群主：可设置所有群成员的名片。
- 管理员：可设置自身和其他普通群成员的群名片。
- 普通群成员：只能设置自身群名片。

**接口名**

```js
tim.setGroupMemberNameCard(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称       | 类型             | 描述                       |
| :--------- | :--------------- | :------------------------- |
| `groupID`  | `String`           | 群组 ID                    |
| `userID`   | `String<optional>` | 可选，默认修改自身的群名片 |
| `nameCard` | `String`           |       -                     |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberNameCard({ groupID: 'group1', userID: 'user1', nameCard: '用户名片' });
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberNameCard error:', imError); // 设置群成员名片失败的相关信息
});
```


### 修改自定义字段

设置群成员自定义字段。
>!普通群成员只能设置自己的自定义字段。

**接口名**

```js
tim.setGroupMemberCustomField(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称                | 类型               | 描述      |
| :------------------ | :----------------- | :-------- |
| `groupID`           | `String`           | 群组 ID   |
| `userID`            | `String<optional>` | 群成员 ID，可选，不填则修改自己的群成员自定义字段 |
| `memberCustomField` | `Array<Object>`    | 群成员自定义字段 |

`memberCustomField`包含的属性值如下表所示：

| 名称    | 类型               |  描述 |
| :------ | :----------------- | :------ |
| `key`   | `String`      | 自定义字段的 Key |
| `value` | `String<optional>`| 自定义字段的 Value |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberCustomField({ groupID: 'group1', memberCustomField: [{key: 'group_member_test', value: 'test'}]});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberCustomField error:', imError); // 设置群成员自定义字段失败的相关信息
});
```

## 群提示消息

当有用户被邀请加入群组或有用户被移出群组等事件发生时，群内会产生提示消息，接入侧可以根据需要展示给群组用户，或者忽略。
群提示消息有多种类型，详细描述请参见 [Message.GroupTipPayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload)。

| 名称              | 类型             | 描述                                   |
| :---------------- | :--------------- | :------------------------------------- |
| `operatorID`      | `String`         | 执行该操作的用户 ID                    |
| `operationType`   | `Number`         | 操作类型                               |
| `userIDList`      | `Array<String>` | 相关的 userID 列表                     |
| `newGroupProfile` | `Object`         | 若是群资料变更，该字段存放变更的群资料 |

群提示消息的 content 结构。系统会在恰当的时机，向全体群成员发出群提示消息。例如：有群成员退群/进群，系统会给所有群成员发对应的群提示消息。

## 群系统通知

当有用户申请加群等事件发生时，管理员会收到申请加群等系统消息。管理员同意或拒绝加群申请，IM SDK 会将相应的消息通过群系统通知消息发送给接入侧，由接入侧展示给用户。
群系统通知消息有多种类型，详细描述请参见 [群系统通知类型常量及含义](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload)。

<pre>
let onGroupSystemNoticeReceived = function(event) {
  const type = event.data.type; // 群系统通知的类型，详情请参见 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload">Message.GroupSystemNoticePayload</a> 
  const message = event.data.message; // 群系统通知的消息实例，详情请参见 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html">Message</a>
  console.log(message.payload); // 消息内容. 群系统通知 payload 结构描述
};
tim.on(TIM.EVENT.GROUP_SYSTEM_NOTICE_RECEIVED, onGroupSystemNoticeReceived);
</pre>



| 名称            | 类型     | 描述                                                         |
| :-------------- | :------- | :----------------------------------------------------------- |
| `operatorID`    | `String` | 执行该操作的用户 ID                                          |
| `operationType` | `Number` | 操作类型                                                     |
| `groupProfile`  | `Object` | 相关的群组资料                                               |
| `handleMessage` | `Object` | 处理的附言<br>例如，user1 申请加入进群需要验证的 group1 时，若 user1 填写了申请加群的附言，则 group1 的管理员会在相应群系统通知中看到该字段 |

`operationType`描述

| 名称 | 描述                               |接收对象|
| :--- | :--------------------------------- | :---|
| 1    | 有用户申请加群|群管理员/群主接收  |
| 2    | 申请加群被同意|申请加群的用户接收 |
| 3    | 申请加群被拒绝|申请加群的用户接收 |
| 4    | 被踢出群组|被踢出的用户接收       |
| 5    | 群组被解散|全体群成员接收         |
| 6    | 创建群组|创建者接收               |
| 7    | 邀请加群|被邀请者接收             |
| 8    | 退群|退群者接收                   |
| 9    | 设置管理员|被设置方接收           |
| 10   | 取消管理员|被取消方接收           |
| 255  | 用户自定义通知|默认全员接收       |

群系统通知的 content 结构。系统会在恰当的时机，向特定用户发出群系统通知。例如，user1 被踢出群组，系统会给 user1 发送对应的群系统消息。
