## 音视频权限管理

用户音视频权限，是指一组开关，每个开关对应用户能否在房间内执行某项动作，即**`能否创建房间`**、**`能否加入房间`**、**`能否接收/发送摄像头音视频数据`**和**`能否发送/接收屏幕分享音视频数据`**。

用户音视频权限，是作为进入房间**`AVContext.enterRoom(int roomType, AVRoom.Delegate roomDelegate, AVRoom.EnterRoomParam enterRoomParam)`** 的参数**`AVRoomMulti.EnterRoomParam`**传递给SDK的。具体取值如下：

权限字段名称| 字段含义
----		| ----
AUTH\_BITS\_CREATE\_ROOM 	|创建房间权限
AUTH\_BITS\_JOIN_ROOM 		|加入房间的权限
AUTH\_BITS\_RECV_AUDIO		|【接收】语音的权限
AUTH\_BITS\_RECV_VIDEO		|【接收】摄像头视频数据的权限
AUTH\_BITS\_RECV_SUB		|【接收】屏幕分享视频数据的权限（全民直播用不到）
AUTH\_BITS\_SEND_AUDIO		|【发送】语音的权限
AUTH\_BITS\_SEND_VIDEO		|【发送】摄像头视频数据的权限
AUTH\_BITS\_SEND_SUB		|【发送】屏幕分享视频数据的权限（全民直播用不到）
AUTH\_BITS\_DEFUALT			|缺省值。拥有所有权限

对应到全民直播领域，通常有两个角色，即主播和观众。

+ 主播：毫无疑问应该拥有所有权限，即**`AUTH_BITS_DEFUALT`**
+ 观众
	+ 观众角色**`AVContext.enterRoom()`**时都应该设置成没有“发送”相关的权限，建议
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
	+ 【注意】当观众连麦时，需要调用下一节介绍的**`AVRoomMulti.changeAuthority()`**接口来添加音视频发送权限，才能真正实现连麦，修改完成后观众权限变成
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
		+ **`AUTH_BITS_SEND_AUDIO`**
		+ **`AUTH_BITS_SEND_VIDEO`**
		+ **`AUTH_BITS_SEND_SUB`**
	+ 【注意】观众连麦结束后，需要再次调用的**`AVRoomMulti.changeAuthority()`**接口来取消观众的音视频发送权限，修改完成后观众权限变成
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**

用户音视频权限的合理控制，可以避免不连麦用户使用资费较贵的[核心节点](ttps://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/oddc.md)，大幅度节省带宽费用。关于用户音视频权限变更的具体实施细节在下一节详细介绍。
	
## 用户音视频权限动态变更

如前所述，腾讯云互动直播的后台接入分为[核心节点和边缘节点](ttps://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/oddc.md)，其中核心节点带宽资费较贵，主要用于需要上行音视频数据或实时交互的用户角色（在全民直播业务中可以特指主播和连麦用户）；而边缘节点带宽资费较便宜，主要用于不需要上行音视频数据、仅观看的用户角色（在全民直播业务中可以特指除主播和连麦用户之外的所有其他用户）

对于需要连麦功能的业务来说，如果所有用户进房间时都设置为`AUTH_BITS_DEFUALT`，那么所有用户都会接入核心节点，从而产生***_较贵的资费_***。所以，最经济的做法是，在进房间（`AVContext.enterRoom(）`）的时候，只有主播拥有全部音视频权限（`AUTH_BITS_DEFUALT `），而所有其他用户则只有进入房间和收听/收看权限（`AUTH_BITS_JOIN_ROOM` | `AUTH_BITS_RECV_AUDIO` | `AUTH_BITS_RECV_VIDEO` | `AUTH_BITS_RECV_SUB`）

当某个用户要连麦的时候，通过SDK的**`AVRoomMulti.changeAuthority()`**接口为该用户赋予上行音视频的权限（`AUTH_BITS_SEND_AUDIO` | `AUTH_BITS_SEND_VIDEO` |  `AUTH_BITS_SEND_SUB`）。此时，该用户会从边缘节点重定向到核心节点，其中重定向动作在SDK内部完成，对App透明，完成后会有回调`OnChangeAuthority()`

当连麦用户结束下麦的时候，同样需要调用**`AVRoomMulti.changeAuthority()`**接口收回该用户的音视频上行权限（只保留`AUTH_BITS_RECV_XXX`）。此时，该用户会从核心节点重定向到边缘节点，从而达到节省带宽资费的目的

### 连麦用户上麦的具体步骤如下：

+ 调用`boolean AVRoomMulti.changeAuthority()`接口为连麦用户增加音视频上行权限（`AUTH_BITS_SEND_XXX`），如果返回值为True，那么
+ 等待`OnChangeAuthority:(int retCode)`回调，判断`retCode`是否等于`av_ok`，如果是，那么
+ 打开麦克风和摄像头（具体客户端代码示例待补充...），开始连麦

### 连麦用户退出连麦的具体步骤如下：

+ 关闭麦克风和摄像头（具体客户端代码示例待补充...）
+ 调用`boolean AVRoomMulti.changeAuthority()`接口为连麦用户去除音视频上行权限，如果返回值为True，那么
+ 等待`OnChangeAuthority:(int retCode)`回调，判断`retCode`是否等于`av_ok`，如果是，那么步骤完成，否则报错或重试