
Group 类为 MGOBE 的子属性，用来实现玩家组成队组。

### constructor

#### 接口描述
构造器。

#### 参数描述

|参数名|类型/值|描述|可选|
|:---|---|---|---|
|groupInfo|[MGOBE.types.GroupInfo](https://cloud.tencent.com/document/product/1038/35534#groupinfo)|队组信息|是|



<dx-alert infotype="explain" title="">
- 实例化 Group 对象时可以传入一个 [MGOBE.types.GroupInfo](https://cloud.tencent.com/document/product/1038/35534#groupinfo) 对象 groupInfo，后续接口调用都将基于该 groupInfo，例如修改该队组的属性、接收该队组的广播。
- 如果不传 groupInfo 参数，您可以通过直接调用 initGroup、createGroup、joinGroup 等方法获取 groupInfo。
- Group 对象会自动维护内部的 groupInfo 属性保持最新，您可以直接通过访问该属性获得最新的队组信息。
</dx-alert>




#### 返回值说明
无


#### 使用示例
```
	// 示例1：不传 groupInfo 参数
	// 该 Group 实例没有队组信息
	const group1 = new MGOBE.Group();

	// 示例2：传 groupInfo 参数
	// 该 Group 实例代表 ID 为 xxx 的队组，group2.getGroupDetail 将查询 xxx 队组信息
	const groupInfo = {
			id: "xxx",
			// 其他字段
			// ...
	};
	const group2 = new MGOBE.Group(groupInfo);
```

### groupInfo

#### 对象描述
队组信息。

#### 参数描述

无



<dx-alert infotype="explain" title="">
groupInfo 为 Group 实例的属性，类型为 [MGOBE.types.GroupInfo](https://cloud.tencent.com/document/product/1038/35534#groupinfo)，调用 Group 相关的接口会导致该属性发生变化。

</dx-alert>





#### 使用示例
```
	// 打印 Group 实例的 groupInfo 属性
	// 如需刷新该属性，可以使用 getGroupDetail 方法
	console.log(group.groupInfo);
```

### initGroup

#### 接口描述
初始化 Group 实例的队组信息，即更新 groupInfo 属性。

#### 参数描述

|参数名|类型/值|描述|可选|
|:---|---|---|---|
|groupInfo|[MGOBE.types.GroupInfo](https://cloud.tencent.com/document/product/1038/35534#groupinfo) 或 { id: string }|初始化参数，id表示队组ID|是|



<dx-alert infotype="explain" title="">
- initGroup 会更新 Group 实例的 groupInfo，接受 [MGOBE.types.GroupInfo](https://cloud.tencent.com/document/product/1038/35534#groupinfo) 或 { id: string; } 类型的参数。
- 如果不传参数，该方法将清空 Group 实例的 groupInfo 属性。
- 当玩家要加入指定 ID 队组时，需要使用该接口初始化 Group 实例的 groupInfo 属性，然后才能通过调用 joinGroup 方法，加入该 Group 实例所代表的队组。
</dx-alert>





#### 返回值说明
无


#### 使用示例
```
	const group = new Group();

	// 示例1：不传 groupInfo 参数
	// 该 Group 实例队组信息被清除
	group.initGroup();

	// 示例2：指定队组 ID
	// 该 Group 实例代表 ID 为 xxx 的队组，group.getGroupDetail 将查询 xxx 队组信息
	const groupInfo = { id: "xxx" };
	group.initGroup(groupInfo);
```

### getGroupByGroupId

#### 接口描述
通过队组 ID 获取队组信息。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|getGroupByGroupIdPara|[MGOBE.types.GetGroupByGroupIdPara](https://cloud.tencent.com/document/product/1038/35534#getgroupbygroupidpara)|获取队组参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.GetGroupByGroupIdRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#getgroupbygroupidrsp)|响应回调函数|

<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。
- 该接口为 Group 的静态方法，只能通过 Group.getGroupByGroupId 方式调用，Group 实例无法直接访问该方法。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
// 查询指定队组ID的信息
const getGroupByGroupIdPara = {
		groupId: "xxx",
};

MGOBE.Group.getGroupByGroupId(getGroupByGroupIdPara, event => console.log(event));
```

### getMyGroups

#### 接口描述
获取当前玩家队组信息。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.GetMyGroupsRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#getmygroupsrsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。
- 该接口为 Group 的静态方法，只能通过 Group.getMyGroups 方式调用，Group 实例无法直接访问该方法。
</dx-alert>




#### 返回值说明
无


#### 使用示例
```
	MGOBE.Group.getMyGroups(event => {
			if (event.code === 0 && event.data.groupInfoList.length > 0) {
					console.log("玩家在队组数量=", event.data.groupInfoList.length);
					// 可以使用队组信息初始化 Group 实例
					const group = new MGOBE.Group(event.data.groupInfoList[0]);
			}
	});
```

### createGroup

#### 接口描述
创建队组。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|createGroupPara|[MGOBE.types.CreateGroupPara](https://cloud.tencent.com/document/product/1038/35534#creategrouppara)|创建队组参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.CreateGroupRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#creategrouprsp)|响应回调函数|

<dx-alert infotype="explain" title="">
调用结果将在 callback 中异步返回。操作成功后，groupInfo 属性将更新。
</dx-alert>




#### 返回值说明
无


#### 使用示例
```
const playerInfo = {
		name: "Tom",
		customGroupPlayerStatus: 1,
		customGroupPlayerProfile: "https://xxx.com/icon.png",
};

const createGroupPara = {
		groupName: "队组名",
		groupType: MGOBE.ENUM.GroupType.GROUP_MANY,
		maxPlayers: 4,
		isForbidJoin: false,
		isPersistent: false,
		customProperties: "自定义队组属性",
		playerInfo,
};

group.createGroup(createGroupPara, event => console.log(event));
```

### getGroupDetail

#### 接口描述
获取 Group 实例的队组信息。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.GetGroupByGroupIdRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#getgroupbygroupidrsp)|响应回调函数|



<dx-alert infotype="explain" title="">
调用结果将在 callback 中异步返回。操作成功后，groupInfo 属性将更新。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.getGroupDetail(event => {
			if (event.code === 0) {
					console.log("队组名", event.data.groupInfo.name);
			}
	});
```

### joinGroup

#### 接口描述
加入队组。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|joinGroupPara|[MGOBE.types.JoinGroupPara](https://cloud.tencent.com/document/product/1038/35534#joingrouppara)|加入队组参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.JoinGroupRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#joingrouprsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。
- 该接口加入的队组是 Group 实例所代表的队组，如果该 Group 实例的 groupInfo 不存在队组ID，则需要使用队组ID通过 initGroup 方法初始化 Group 实例。
- 加入队组成功后，队组内全部成员（不含调用者）都会收到一条玩家加入队组广播 onJoinGroup，groupInfo 属性将更新。
- 玩家可以加入多个 GROUP_MANY 类型队组（type 为 GroupType.GROUP_MANY），同时加入的数量上限为5个。
- 玩家最多只能加入1个 GROUP_LIMITED 类型队组（type 为 GroupType.GROUP_LIMITED）。
</dx-alert>





#### 返回值说明
无


#### 使用示例
```
	const playerInfo = {
			name: "Tom",
			customGroupPlayerStatus: 1,
			customGroupPlayerProfile: "https://xxx.com/icon.png",
	};

	const joinGroupPara = {
			playerInfo,
	};

	// 加入指定 ID 的队组
	const group = new MGOBE.Group();
	group.initGroup({ id: "xxx" });
	group.joinGroup(joinGroupPara, event => console.log(event));
```

### leaveGroup

#### 接口描述
离开队组。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|para|object|预留参数，传{}即可|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.LeaveGroupRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#leavegrouprsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。退出成功后，队组内剩余成员（不含调用者）都会收到一条玩家退出队组广播 onLeaveGroup，groupInfo 属性将更新，groupInfo.groupPlayerList 中将没有该玩家信息。
- 离开队组后，如果队组内还剩下其他玩家，则该 Group 实例仍然代表退房前的队组，可以继续调用 group.initGroup() 清除队组信息。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.leaveGroup({}, event => {
			if (event.code === 0) {
					console.log("退出队组成功", group.groupInfo.id);
					// 可以使用 initGroup 清除 groupInfo
					group.initGroup();
			}
	});
```

### dismissGroup

#### 接口描述
解散队组。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|para|object|预留参数，传{}即可|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.DismissGroupRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#dismissgrouprsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。解散成功后，队组内全部成员（不含调用者）都会收到一条解散队组广播 onDismissGroup，groupInfo 属性将更新。
- 只有队长有权限解散队组。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.dismissGroup({}, event => {
			if (event.code === 0) {
					console.log("解散成功");
			}
	});
```

### changeGroup

#### 接口描述
更新队组信息。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|changeGroupPara|[MGOBE.types.ChangeGroupPara](https://cloud.tencent.com/document/product/1038/35534#changegrouppara)|更新队组参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.ChangeGroupRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#changegrouprsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。调用成功后，队组内全部成员都会收到一条更新队组广播 onChangeGroup，groupInfo 属性将更新。
- 只有队长有权限修改队组。
</dx-alert>





#### 返回值说明
无


#### 使用示例
```
	const changeGroupPara = {
			groupName: "队组名",
			owner: "xxxxxx",
			isForbidJoin: false,
			customProperties: "xxxxxx",
	};

	group.changeGroup(changeGroupPara, event => {
			if (event.code === 0) {
					console.log("更新队组成功", event.data.groupInfo);
			}
	});
```

### removeGroupPlayer

#### 接口描述
移除队组内玩家。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|removeGroupPlayerPara|[MGOBE.types.RemoveGroupPlayerPara](https://cloud.tencent.com/document/product/1038/35534#removegroupplayerpara)|移除队组内玩家参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.RemoveGroupPlayerRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#removegroupplayerrsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。调用成功后，队组内全部成员都会收到一条队组内玩家被移除广播 onRemoveGroupPlayer，groupInfo 属性将更新。
- 只有队长有权限移除玩家。
</dx-alert>




#### 返回值说明
无


#### 使用示例
```
const removeGroupPlayerPara = {
		removePlayerId: "xxxxxx",
};

group.removeGroupPlayer(removeGroupPlayerPara, event => console.log(event)); 
```

### changeCustomGroupPlayerStatus

#### 接口描述
修改队组玩家自定义状态。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|changeCustomGroupPlayerStatusPara|[MGOBE.types.ChangeCustomGroupPlayerStatusPara](https://cloud.tencent.com/document/product/1038/35534#changecustomgroupplayerstatuspara)|修改队组玩家自定义状态参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.ChangeCustomGroupPlayerStatusRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#changecustomgroupplayerstatusrsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 修改玩家状态是修改 GroupPlayerInfo 中的 customGroupPlayerStatus 字段，玩家的状态由您自定义。
- 修改成功后，队组内全部成员都会收到一条修改队组玩家状态广播 onChangeCustomGroupPlayerStatus，groupInfo 属性将更新。
- 每个玩家只能修改自己的状态，调用结果将在 callback 中异步返回。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
const changeCustomGroupPlayerStatusPara = {
		customGroupPlayerStatus: 2,
};

group.changeCustomGroupPlayerStatus(changeCustomGroupPlayerStatusPara, event => console.log(event));
```


### changeGroupPlayerProfile

#### 接口描述

修改队组玩家自定义属性。

#### 参数描述

| 参数名                       | 类型/值                                                      | 描述                       |
| :--------------------------- | ------------------------------------------------------------ | -------------------------- |
| changeGroupPlayerProfilePara | [MGOBE.types.ChangeGroupPlayerProfilePara](https://cloud.tencent.com/document/product/1038/35534#changegroupplayerprofilepara) | 修改队组玩家自定义属性参数 |
| callback                     | [MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.ChangeGroupPlayerProfileRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#changegroupplayerprofilepara) | 响应回调函数               |



<dx-alert infotype="explain" title="">
- 修改玩家属性是修改 GroupPlayerInfo 中的 customGroupPlayerProfile 字段，玩家的属性由您自定义。
- 修改成功后，队组内全部成员都会收到一条修改玩家属性广播 onChangeGroupPlayerProfile，groupInfo 属性将更新。
- 每个玩家只能修改自己的属性，调用结果将在 callback 中异步返回。
</dx-alert>




#### 返回值说明

无


#### 使用示例

```
	const changeGroupPlayerProfilePara = {
			customProfile: "{name: 'name_example'}",
	};

	group.changeGroupPlayerProfile(changeGroupPlayerProfilePara, event => console.log(event));
```


### sendToGroupClient

#### 接口描述
发送队组内消息。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|sendToGroupClientPara|[MGOBE.types.SendToGroupClientPara](https://cloud.tencent.com/document/product/1038/35534#sendtogroupclientpara)|发送队组内消息参数|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)[&lt;MGOBE.types.SendToGroupClientRsp&gt;](https://cloud.tencent.com/document/product/1038/35534#sendtogroupclientrsp)|响应回调函数|



<dx-alert infotype="explain" title="">
- 调用结果将在 callback 中异步返回。调用成功后所指定接收消息的玩家将收到 onRecvFromGroupClient 广播。
- 当 recvType 值为 1（即 GROUP_ALL ） 时，队组内全部玩家将收到消息。
- 当 recvType 值为 2（即 GROUP_OTHERS ） 时，队组内除消息发送者外的其他玩家将收到消息。
- 当 recvType 值为 3（即 GROUP_SOME ） 时，接收消息玩家由 recvPlayerList 决定。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
const sendToGroupClientPara = {
		recvType: MGOBE.ENUM.GroupRecvType.GROUP_SOME,
		recvPlayerList: ["xxxxxxxx1", "xxxxxxxx2"],
		msg: "hello",
};

group.sendToGroupClient(sendToGroupClientPara, event => console.log(event));
```

### onUpdate

#### 接口描述
队组信息更新回调接口。

#### 参数描述

|参数名|类型/值|描述|可选|
|:---|---|---|---|
|group|Group|更新的 Group 实例|是|



<dx-alert infotype="explain" title="">
onUpdate 表明 Group 实例的 groupInfo 信息发生变化，这种变化原因包括各种队组操作、广播、本地网络状态变化等。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.onUpdate = (_) => {
			console.log(_ === group); // true, 参数 _ 等于 group
			console.log("队组信息更新", group.groupInfo);
	};
```

### onRecvFromGroupClient

#### 接口描述
收到队组内其他玩家消息广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.RecvFromGroupClientBst&gt;](https://cloud.tencent.com/document/product/1038/35534#recvfromgroupclientbst)|回调参数|



<dx-alert infotype="explain" title="">
onRecvFromGroupClient 广播表示在队组内收到来自 ID 为 sendPlayerId 的玩家消息。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
group.onRecvFromGroupClient = event => console.log("新消息", event.data.msg);
```

### onChangeCustomGroupPlayerStatus

#### 接口描述
玩家自定义状态变化广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.ChangeCustomGroupPlayerStatusBst&gt;](https://cloud.tencent.com/document/product/1038/35534#changecustomgroupplayerstatusbst)|回调参数|



<dx-alert infotype="explain" title="">
onChangeCustomGroupPlayerStatus 广播表示队组内 ID 为 changePlayerId 的玩家状态发生变化。玩家状态由您自定义。

</dx-alert>



#### 返回值说明

无


#### 使用示例
```
group.onChangeCustomGroupPlayerStatus = event => {
		console.log("玩家状态变化", event.data.changePlayerId);
};
```

### onChangeGroupPlayerProfile

#### 接口描述

玩家自定义属性变化广播回调接口。

#### 参数描述

| 参数名 | 类型/值                                                      | 描述     |
| :----- | ------------------------------------------------------------ | -------- |
| event  | [MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.ChangeGroupPlayerProfileBst&gt;](https://cloud.tencent.com/document/product/1038/35534#changegroupplayerprofilebst) | 回调参数 |



<dx-alert infotype="explain" title="">
onChangeGroupPlayerProfile 广播表示队组内 ID 为 changePlayerId 的玩家属性发生变化。玩家属性由您自定义。
</dx-alert>



#### 返回值说明

无


#### 使用示例

```
	group.onChangeGroupPlayerProfile = event => {
			console.log("玩家属性变化", event.data.changePlayerId);
	};
```



### onChangeGroupPlayerNetworkState

#### 接口描述
队组内玩家网络状态变化广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.ChangeGroupPlayerNetworkStateBst&gt;](https://cloud.tencent.com/document/product/1038/35534#changegroupplayernetworkstatebst)|回调参数|

<dx-alert infotype="explain" title="">
- onChangeGroupPlayerNetworkState 广播表示 ID 为 changePlayerId 的玩家网络状态发生变化。
- 玩家在队组中的网络变化都会触发该广播，因此 networkState 将有两种情况，分别表示队组中上线、队组中下线。
</dx-alert>





#### 返回值说明
无


#### 使用示例
```
	group.onChangeGroupPlayerNetworkState = event => {
			if (event.data.networkState === MGOBE.ENUM.NetworkState.COMMON_OFFLINE)
					console.log("玩家下线");
	};
```

### onRemoveGroupPlayer

#### 接口描述
队组内玩家被移除广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.RemoveGroupPlayerBst&gt;](https://cloud.tencent.com/document/product/1038/35534#removegroupplayerbst)|回调参数|



<dx-alert infotype="explain" title="">
onRemoveGroupPlayer 广播表示有玩家被队长移除，队组内全部成员都会收到该广播。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.onRemoveGroupPlayer = event => console.log("玩家被移除", event.data.removePlayerId);
```

### onChangeGroup

#### 接口描述
更新队组广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.ChangeGroupBst&gt;](https://cloud.tencent.com/document/product/1038/35534#changegroupbst)|回调参数|



<dx-alert infotype="explain" title="">
onChangeGroup 广播表示修改了该队组属性，队组内全部成员都会收到该广播。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.onChangeGroup = event => console.log("队组属性变更", event.data.groupInfo);
```

### onDismissGroup

#### 接口描述
队组被解散广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.DismissGroupBst&gt;](https://cloud.tencent.com/document/product/1038/35534#dismissgroupbst)|回调参数|



<dx-alert infotype="explain" title="">
onDismissGroup 广播表示队长解散了该队组，队组内全部成员都会收到该广播。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.onDismissGroup = event => console.log("队组解散");
```

### onLeaveGroup

#### 接口描述
玩家退出队组广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.LeaveGroupBst&gt;](https://cloud.tencent.com/document/product/1038/35534#leavegroupbst)|回调参数|




<dx-alert infotype="explain" title="">
onLeaveGroup 广播表示该队组有玩家退出，队组内全部成员都会收到该广播。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
	group.onLeaveGroup = event => console.log("玩家退出", event.data.leavePlayerId);
```

### onJoinGroup

#### 接口描述
新玩家加入队组广播回调接口。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|event|[MGOBE.types.BroadcastEvent](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)[&lt;MGOBE.types.JoinGroupBst&gt;](https://cloud.tencent.com/document/product/1038/35534#joingroupbst)|回调参数|

<dx-alert infotype="explain" title="">
onJoinGroup 广播表示该队组有新玩家加入，队组内全部成员都会收到该广播。
</dx-alert>



#### 返回值说明
无


#### 使用示例
```
	group.onJoinGroup = event => console.log("新玩家加入", event.data.joinPlayerId);
```


