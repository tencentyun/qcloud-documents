## 群组综述

即时通信 IM 有多种群组类型，其特点以及限制因素可参考 [群组系统](https://cloud.tencent.com/doc/product/269/群组系统)。群组使用唯一 ID 标识，通过群组 ID 可以进行不同操作。

## 群组管理

### 获取加入的群组列表

> 参考：[Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)

需要渲染或刷新【我的群组列表】时，调用该接口获取群组列表

**接口名**

```js
tim.getGroupList();
```

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中拿到群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getGroupList();
promise.then(function(imResponse) {
  console.log(imResponse.data.groupList); // 群组列表
}).catch(function(imError) {
  console.warn('getGroupList error:', imError); // 获取群组列表失败的相关信息
});
```

### 获取群详细资料

> 参考：[Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)

**接口名**

```js
tim.getGroupProfile(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称                    | 类型           | 属性 | 描述                                                         |
| :---------------------- | :------------- | :--- | :----------------------------------------------------------- |
| `groupID  `               | `String`         |  | 群组ID                                                       |
| `groupCustomFieldFilter`  | `Array<String>` | `<optional>` | 群组的自定义字段过滤器，指定需要获取的群组的自定义字段，详情请参阅 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |
| `memberCustomFieldFilter` | `Array<String>` | `<optional>` | 群成员的自定义字段过滤器，指定需要获取的群成员的自定义字段，详情请参阅 [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中拿到群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getGroupProfile({
  groupID: 'group1',
  groupCustomFieldFilter: ['key1','key2'],
  memberCustomFieldFilter: ['key1', 'key2']
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group);
}).catch(function(imError) {
  console.warn('getGroupProfile error:', imError); // 获取群详细资料失败的相关信息
});
```



### 创建群组

> 参考：[Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html)

**接口名**

```js
tim.createGroup(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称             | 类型           | 属性       | 默认值                               | 描述                                                         |
| :--------------- | :------------- | :--------- | :----------------------------------- | :----------------------------------------------------------- |
| `name`           | `String`         |            |                                      | 必填，群组名称，最长30字节                                   |
| `type`             | `String`         | `<optional>` | `TIM.TYPES.GRP_PRIVATE`              | 群组类型，包括： <br/>TIM.TYPES.GRP_PRIVATE(私有群，默认) <br/>TIM.TYPES.GRP_PUBLIC(公开群)<br/>TIM.TYPES.GRP_CHATROOM(聊天室)<br/>TIM.TYPES.GRP_AVCHATROOM(互动直播聊天室) |
| `groupID`          | `String`         | `<optional>` |                                      | 群组ID。不填该字段时，会自动为群组创建一个唯一的群 ID        |
| `introduction`     | `String`         | `<optional>` |                                      | 群简介，最长240字节                                          |
| `notification`    | `String`         | `<optional>` |                                      | 群公告，最长300字节                                          |
| `avatar`           | `String`         | `<optional>` |                                      | 群头像 URL，最长100字节                                      |
| `maxMemberNum`     | `Number`         | `<optional>` |                                      | 最大群成员数量，缺省时的默认值：私有群是200，公开群是2000，聊天室是10000，音视频聊天室和在线成员广播大群无限制 |
| `joinOption`       | `String`         | `<optional>` | `TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS` | 申请加群处理方式。注意：创建私有群和音视频聊天室不能填写该字段。<br/>TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS (自由加入)<br/>TIM.TYPES.JOIN_OPTIONS_NEED_PERMISSION (需要验证)<br/>TIM.TYPES.JOIN_OPTIONS_DISABLE_APPLY (禁止加群) |
| `memberList`       | `Array<Object>` | `<optional>`|                                      | 初始群成员列表，最多500个。创建音视频聊天室时不能添加成员。参考下方：memberList 参数说明 |
| `groupCustomField` | `Array<Object>` | `<optional>` |                                      | 群组维度的自定义字段，默认情况是没有的，需要开通，详情请参阅[群成员资料](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

`memberList` 参数说明

| 名称                | 类型           | 属性 | 描述                                                  |
| :------------------ | :------------- | :--------- | :----------------------------------------------------------- |
| `userID    `        | `String`         |            | 必填，群成员的 userID                                        |
| `role  `            | `String`         | `<optional>` | 成员身份，可选值只有Admin，表示添加该成员并设其为管理员      |
| `memberCustomField` | `Array<Object>` | `<optional>` | 群成员维度的自定义字段，默认情况是没有的，需要开通，详情请参阅[自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中拿到群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
// 创建私有群
let promise = tim.createGroup({
  type: TIM.TYPES.GRP_PRIVATE,
  name: 'WebSDK',
  memberList: [{userID: 'user1'}, {userID: 'user2'}] // 如果填写了memberList，则必须填写 userID
});
promise.then(function(imResponse) { // 创建成功
  console.log(imResponse.data.group); // 创建的群的资料
}).catch(function(imError) {
  console.warn('createGroup error:', imError); // 创建群组失败的相关信息
});
```

### 解散群组

群主调用该接口解散群组，注意：群主不能解散私有群。

**接口名**

```js
tim.dismissGroup(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupID`中拿到被解散的群组ID。
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

参数`options`为`Object`类型，包含的属性值如下：

| 名称               | 类型           | 属性       | Default                              | 描述                                                         |
| :----------------- | :------------- | :--------- | :----------------------------------- | :----------------------------------------------------------- |
| `groupID`          | `Object`         |            |                                      |                                                              |
| `name`             | `Object`         | `<optional>` |                                      | 群名称，最长30字节                                           |
| `avatar`           | `Object`         | `<optional>` |                                      | 群头像URL，最长100字节                                       |
| `introduction`     | `Object`         | `<optional>` |                                      | 群简介，最长240字节                                          |
| `notification`     | `Object`         | `<optional>` |                                      | 群公告，最长300字节                                          |
| `maxMemberNum`     | `Number`         | `<optional>` |                                      | 最大群成员数量，最大为6000                                   |
| `joinOption`       | `String`         | `<optional>` | `TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS` | 申请加群处理方式。注意：TIM.TYPES.GRP_PRIVATE 和 TIM.TYPES.GRP_AVCHATROOM 类型的群组不能设置该字段TIM.TYPES.JOIN_OPTIONS_FREE_ACCESS (自由加入)TIM.TYPES.JOIN_OPTIONS_NEED_PERMISSION (需要验证)TIM.TYPES.JOIN_OPTIONS_DISABLE_APPLY (禁止加群) |
| `groupCustomField` | `Array<Object>` | `<optional>` |                                      | 群自定义字段，参考下方：`groupCustomField`参数说明。默认情况是没有的，开通请参见： [自定义字段](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) |

`groupCustomField`参数说明

| 名称    | 类型   | 描述              |
| :------ | :----- | :---------------- |
| `key`   | `String` | 自定义字段的Key   |
| `value` | `String` | 自定义字段的Value |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.group`中拿到修改后的群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.updateGroupProfile({
  groupID: 'group1',
  name: 'new name', // 修改群名称
  introduction: 'this is introduction.', // 修改群公告
  groupCustomField: [{ key: 'group_level', value: 'high'}] // 修改群组维度自定义字段
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group) // 修改成功后的群组详细资料
}).catch(function(imError) {
  console.warn('updateGroupProfile error:', imError); // 修改群组资料失败的相关信息
});
```

### 申请加群

注意：私有群不能申请加入，只能由群成员邀请加入。

**接口名**

```js
tim.joinGroup(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称           | 类型   | 属性       | 描述                                                         |
| :------------- | :----- | :--------- | :----------------------------------------------------------- |
| `groupID`      | `String` |            |                                                              |
| `applyMessage` | `String` |            | 附言                                                         |
| `type`         | `String` | `<optional>` | 要加入群组的类型，加入音视频聊天室时该字段必填。可选值：<br/>TIM.TYPES.GRP_PUBLIC (公开群)<br/>TIM.TYPES.GRP_CHATROOM (聊天室)<br/>TIM.TYPES.GRP_AVCHATROOM (音视频聊天室) |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`中包括的属性值如下：

  | 名称   | 含义                                                         |
  | ------ | ------------------------------------------------------------ |
  | status | 加群的状态。包括:<br/>TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL (等待管理员审核)<br/>TIM.TYPES.JOIN_STATUS_SUCCESS (加群成功) |
  | group  | 加群成功后的群组资料                                         |

- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.joinGroup({ groupID: 'group1', type: TIM.TYPES.GRP_AVCHATROOM });
promise.then(function(imResponse) {
  switch(imResponse.data.status){
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

注意：群主只能退出私有群，退出后该私有群无群主。

**接口名**

```js
tim.quitGroup(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.groupID`为退出的群组 ID。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.quitGroup('group1');
promise.then(function(imResponse) {
  console.log(imResponse.data.groupID); // 退出成功的群ID
}).catch(function(imError){
  console.warn('quitGroup error:', imError); // 退出群组失败的相关信息
});
```

### 根据群 ID 搜索群组

注意：私有群不能被搜索。

**接口名**

```js
tim.searchGroupByID(groupID);
```

**请求参数**

| 名称      | 类型   | 描述    |
| :-------- | :----- | :------ |
| `groupID` | `String` | 群组 ID |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
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

注意：只有群主拥有转让的权限，音视频聊天室不能转让。

**接口名**

```js
tim.changeGroupOwner(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型   | 描述            |
| :----------- | :----- | :-------------- |
| `groupID`    | `String` | 待转让的群组 ID |
| `newOwnerID` | `String` | 新群主的 ID     |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
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

当用户申请加入一个需要管理员同意的群组时，管理员/群主会收到申请加群的【群系统通知消息】，参考：[Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)

**接口名**

```js
tim.handleGroupApplication(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称            | 类型                                                         | 属性       | 描述                                                         |
| :-------------- | :----------------------------------------------------------- | :--------- | :----------------------------------------------------------- |
| `handleAction`  | `String `                                                      |            | 处理结果 Agree(同意) / Reject(拒绝)                          |
| `handleMessage` | `String`                                                       | `<optional>` | 附言                                                         |
| `message`       | [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html) |            | 申请加群的【群系统通知消息】的消息实例。该实例可在以下两种方式中取得:<br/>1. [收到新的群系统通知事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.GROUP_SYSTEM_NOTICE_RECERIVED)的回调参数中<br/>2. 系统类型会话的消息列表中 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
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
| `messageRemindType` | `String` | 群消息提示类型。详细如下：<br/>TIM.TYPES.MSG_REMIND_ACPT_AND_NOTE(SDK 接收消息并通知接入侧(抛出 [收到消息事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED))，接入侧做提示)<br/>TIM.TYPES.MSG_REMIND_ACPT_NOT_NOTE(SDK 接收消息并通知接入侧(抛出 [收到消息事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED))，接入侧不做提示)<br/>TIM.TYPES.MSG_REMIND_DISCARD(SDK 拒收消息，不会抛出[收到新消息事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED)) |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为群组资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setMessageRemindType({ groupID: 'group1', messageRemindType: TIM.TYPES.MSG_REMIND_DISCARD }); // 拒收消息
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料。
}).catch(function(imError) {
  console.warn('setMessageRemindType error:', imError);
});
```

## 群成员管理

### 添加群成员

详细规则如下：

- 私有群：任何群成员都可邀请他人加群，且无需被邀请人同意，直接将其拉入群组中。
- 公开群/聊天室：只有 App 管理员可以邀请他人入群，且无需被邀请人同意，直接将其拉入群组中。
- 音视频聊天室：不允许任何人邀请他人入群（包括 App 管理员）。

**接口名**

```js
tim.addGroupMember(options);
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型           | 描述                                          |
| :----------- | :------------- | :-------------------------------------------- |
| `groupID`    | `String`         | 群组 ID                                       |
| `userIDList` | `Array<String>` | 待添加的群成员 ID 数组。一次最多添加500个成员 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`属性值如下：

  | 名称              | 类型                                                         | 含义                   |
  | ----------------- | ------------------------------------------------------------ | ---------------------- |
  | `successUserIDList` | `Array<String> `                                              | 添加成功的 userID 列表 |
  | `failureUserIDList` | `Array<String> `                                              | 添加失败的 userID 列表 |
  | `existedUserIDList` | `Array<String> `                                              | 已在群中的 userID 列表 |
  | `group`             | [Group](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Group.html) | 接口调用后的群组资料   |

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

删除群成员。群主可移除群成员

**接口名**

```js
tim.deleteGroupMember(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型           | 描述                     |
| :----------- | :------------- | :----------------------- |
| `groupID`    | `String`         | 群组 ID                  |
| `userIDList` | `Array<String>` | 待删除的群成员的 ID 列表 |
| `reason`     | `String`         | 踢人的原因(可选)         |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`为更新后的群组资料
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

设置群成员的禁言时间，可以禁言群成员，也可取消禁言
注意：只有群主和管理员拥有操作的权限，群主可以 禁言/取消禁言 管理员和普通群成员，管理员可以 禁言/取消禁言 普通群成员。TIM.TYPES.GRP_PRIVATE类型的群组(私有群)不能禁言

**接口名**

```js
tim.setGroupMemberMuteTime(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称       | 类型   | 描述                                                         |
| :--------- | :----- | :----------------------------------------------------------- |
| `groupID`  | `String` | 群组 ID                                                      |
| `userID`   | `String` | 群成员 ID                                                    |
| `muteTime` | `Number` | 禁言时长，单位秒。如设为1000，则表示从现在起禁言该用户1000秒；设为`0`，则表示`取消禁言`。 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料
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
}).catch(function(imError) {
  console.warn('setGroupMemberMuteTime error:', imError); // 禁言失败的相关信息
});
```



### 设为管理员或撤销管理员

修改群成员角色。只有群主拥有操作的权限

**接口名**

```js
tim.setGroupMemberRole(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称      | 类型   | 描述                                                         |
| :-------- | :----- | :----------------------------------------------------------- |
| `groupID` | `String` | 群组 ID                                                      |
| `userID`  | `String` | 群成员 ID                                                    |
| `role`    | `String` | 可选值：`TIM.TYPES.GRP_MBR_ROLE_ADMIN`(群管理员) 或 `TIM.TYPES.GRP_MBR_ROLE_MEMBER`(群普通成员) |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberRole({
  groupID: 'group1',
  userID: 'user1',
  role: TIM.TYPES.GRP_MBR_ROLE_ADMIN // 将群ID: group1 中的用户：user1 设为管理员
});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 修改后的群资料
}).catch(function(imError) {
  console.warn('setGroupMemberRole error:', imError); // 错误信息
});
```



### 修改群名片

设置群成员名片。
群主：可设置所有群成员的名片
管理员：可设置自身和其他普通群成员的群名片 
普通群成员：只能设置自身群名片

**接口名**

```js
tim.setGroupMemberNameCard(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称       | 类型             | 描述                       |
| :--------- | :--------------- | :------------------------- |
| `groupID`  | `String`           | 群组 ID                    |
| `userID`   | `String<optional>` | 可选，默认修改自身的群名片 |
| `nameCard` | `String`           |                            |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.setGroupMemberNameCard({ groupID: 'group1', userID: 'user1', nameCard: '用户名片' });
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
}).catch(function(imError) {
  console.warn('setGroupMemberNameCard error:', imError); // 设置群成员名片失败的相关信息
});
```



### 修改自定义字段

设置群成员自定义字段
注意：普通群成员只能设置自己的自定义字段

**接口名**

```js
tim.setGroupMemberCustomField(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称                | 类型               | 描述      |
| :------------------ | :----------------- | :-------- |
| `groupID`           | `String`           | 群组 ID   |
| `userID`            | `String<optional>` | 群成员 ID |
| `memberCustomField` | `Array<Object>`    |           |

- `memberCustomField`描述

| 名称    | 类型               | 描述 |
| :------ | :----------------- | :--- |
| `key`   | `String`           |      |
| `value` | `String<optional>` |      |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data.group`是修改后的群资料
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = setMemberCustomField({ groupID: 'group1', memberCustomField: [{key: 'group_member_test', value: 'test'}]});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
}).catch(function(imError) {
  console.warn('setMemberCustomField error:', imError); // 设置群成员自定义字段失败的相关信息
});
```

## 群提示消息

当有用户被邀请加入群组，或者有用户被移出群组等事件发生时，群内会产生提示消息，接入侧可以根据需要展示给群组用户，或者忽略。
群提示消息有多种类型，详细描述见 [Message.GroupTipPayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload)

| 名称              | 类型             | 描述                                   |
| :---------------- | :--------------- | :------------------------------------- |
| `operatorID`      | `String`         | 执行该操作的用户 ID                    |
| `operationType`   | `Number`         | 操作类型                               |
| `userIDList`      | `Array<String>` | 相关的 userID 列表                     |
| `newGroupProfile` | `Object`         | 若是群资料变更，该字段存放变更的群资料 |

群提示消息的 content 结构。系统会在恰当的时机，向全体群成员发出群提示消息。例如：有群成员退群/进群，系统会给所有群成员发对应的群提示消息。

## 群系统通知

当有用户申请加群等事件发生时，管理员会收到申请加群等系统消息。管理员同意或拒绝加群申请，相应的消息 IM SDK 会通过群系统通知消息发送给接入侧，由接入侧展示给用户。
群系统通知消息有多种类型，详细描述见 [Message.GroupSystemNoticePayload](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload)



```javascript
let onGroupSystemNoticeReceived = function(event) {
  const type = event.data.type; // 群系统通知的类型，详见 群系统通知类型常量及含义 
  const message = event.data.message; // 群系统通知的消息实例，详见 Message
  console.log(message.payload); // 消息内容. 群系统通知 payload 结构描述
};
tim.on(TIM.EVENT.GROUP_SYSTEM_NOTICE_RECERIVED, onGroupSystemNoticeReceived);
```



| 名称            | 类型     | 描述                                                         |
| :-------------- | :------- | :----------------------------------------------------------- |
| `operatorID`    | `String` | 执行该操作的用户 ID                                          |
| `operationType` | `Number` | 操作类型                                                     |
| `groupProfile`  | `Object` | 相关的群组资料                                               |
| `handleMessage` | `Object` | 处理的附言。例如：user1 申请加入 group1 时，若进群需要验证，且 user1 填写了申请加群的附言。则 group1 的管理员会在相应群系统通知中看到该字段。 |

- `operationType`描述

| 名称 | 描述                               |
| :--- | :--------------------------------- |
| 1    | 有用户申请加群。群管理员/群主接收  |
| 2    | 申请加群被同意。申请加群的用户接收 |
| 3    | 申请加群被拒绝。申请加群的用户接收 |
| 4    | 被踢出群组。被踢出的用户接收       |
| 5    | 群组被解散。全体群成员接收         |
| 6    | 创建群组。创建者接收               |
| 7    | 邀请加群。被邀请者接收             |
| 8    | 退群。退群者接收                   |
| 9    | 设置管理员。被设置方接收           |
| 10   | 取消管理员。被取消方接收           |
| 255  | 用户自定义通知。默认全员接收       |

群系统通知的 content 。系统会在恰当的时机，向特定用户发出群系统通知。例如：user1 被踢出群组，系统就会给 user1 发对应的群系统消息。