>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。


## 操作场景
本文档指导您如何使用游戏联机对战引擎 C# SDK。

## 前提条件
已在 Unity Editor 中根据指引导入 MGOBE，详情请参见 [Unity 游戏项目](https://cloud.tencent.com/document/product/1038/45333)。

### 初始化监听器 Listener
在使用 MGOBE API 接口时，主要用到 Listener 对象和 Room 对象。导入 SDK 后，需要先初始化 Listener 对象。


```c#
// 初始化监听器 Listener
static void Listener () {
    var gameInfo = new GameInfoPara {
        GameId = "xxxxxxxxxxxx",// 替换为控制台上的“游戏 ID”
        OpenId = "xxxxxxxxxxxx", // 开发者定义的玩家唯一 ID
        SecretKey = "xxxxxxxxxxxxx" // 替换为控制台上的“游戏 key”
    };

    var config = new ConfigPara {
        Url = "xxx.wxlagame.com", // 替换为控制台上的“域名”
        ReconnectMaxTimes = 5,
        ReconnectInterval = 1000,
        ResendInterval = 1000,
        ResendTimeout = 10000,
    };

    Listener.Init (gameInfo, config, (ResponseEvent eve) => {
        if (eve.Code == ErrCode.EcOk) {
            // 初始化成功
            // 继续在此添加代码
            // ...
        }
    });
}
```

调用 Listener.Init 时，需要传入游戏信息 gameInfo 和游戏配置 config 两个参数。
- gameInfo.GameId、gameInfo.SecretKey 和 config.Url 都需要根据控制台上的信息传入。
- gameInfo.OpenId 为玩家唯一 ID，例如，微信小游戏平台上的 OpenID。
- 其它字段由您自定义。

每个字段的具体含义您可参考 [Listener 对象](https://cloud.tencent.com/document/product/1038/33323)。

初始化成功后才能继续调用其他接口。因此，下文的 API 调用代码都应该在初始化回调函数内调用。

### 实例化 Room 对象

在开发游戏过程中的大部分业务接口都位于 Room 对象中。由于每个玩家只能加入一个房间，在游戏生命周期中可以实例化一个 Room 对象进行接口调用：

```c#
var room = new Room (null);
```

实例化 Room 后，可以调用 getMyRoom 接口来检查玩家是否已经加房，适用于应用重启后需要恢复玩家状态的场景。

```c#
// 查询玩家自己的房间
Room.GetMyRoom (eve => {
	if (eve.Code == 0) {
		var data = (GetRoomByRoomIdRsp) eve.Data;
		// 设置房间信息到 room 实例
		room.InitRoom (data.RoomInfo);
		Debug.Log ("玩家已在房间内：" + data.RoomInfo.Name);
		return;
	}

	if (eve.Code == 20011) {
		Debug.Log ("玩家不在房间内");
		return;
	}

	Debug.Log ("调用失败");
});
```

后续的创建房间、加房、匹配等接口调用直接利用 room 实例即可。


<dx-alert infotype="explain" title="">
GetMyRoom、GetRoomList、GetRoomByRoomId 接口是 Room 对象的静态方法，您需要使用 Room.GetMyRoom、Room.GetRoomList、Room.GetRoomByRoomId 进行调用。Room 的实例无法直接访问 GetMyRoom、GetRoomList、GetRoomByRoomId。
</dx-alert>



### Room 接收广播

一个房间对象会有很多广播事件与其相关，例如该房间有新成员加入、房间属性变化、房间开始对战等广播。Room 实例需要在 Listener 中注册广播监听，并且实现广播的回调函数。

#### 注册广播监听

```c#
// 监听
Listener.Add(room);
```

#### 设置广播回调函数

```c#
// 广播：房间有新玩家加入
room.OnJoinRoom = eve => {
	var data = (JoinRoomBst) eve.Data;
	Debug.Log ("新玩家加入" + data.JoinPlayerId);
}; 

// 广播：房间有玩家退出
room.OnLeaveRoom = eve => {
	var data = (LeaveRoomBst) eve.Data;
	Debug.Log ("玩家退出" + data.LeavePlayerId);
}; 

// 广播：房间被解散
room.OnDismissRoom = eve => {
	var data = (JoinRoomBst) eve.Data;
	Debug.Log ("房间被解散");
};

// 其他广播
// ...
```

其他广播接口您可参考 [Room 对象](https://cloud.tencent.com/document/product/1038/33325)。

#### 移除监听
如果不想再接收该 Room 实例的广播，可以从 Listener 中移除：

```c#
// 移除监听
 Listener.Remove (room);
```

### 创建房间
可以通过创建房间、加入房间、匹配等方式进入房间，进入房间后可以继续通过房间消息、帧同步、实时服务器相关接口进行游戏。
创建房间示例代码如下：
```
PlayerInfoPara playerInfoPara = new PlayerInfoPara
{
	Name = "测试 Name",
	CustomProfile = "测试 CustomProfile",
	CustomPlayerStatus = 12345,
};

CreateRoomPara createRoomPara = new CreateRoomPara
{
	RoomName = "测试 RoomName",
	RoomType = "测试 RoomType",
	MaxPlayers = 10,
	IsPrivate = true,
	CustomProperties = "测试 CustomProperties",
	PlayerInfo = playerInfoPara,
};

room.CreateRoom(createRoomPara, eve =>
{
	if (eve.Code == 0)
	{
		// 创建成功
		Debug.LogFormat ("创建成功 {0}", eve.Data);

		// 使用 room 调用其他 API，如 room.StartFrameSync
		// ...

		return;
	}

	if (eve.Code == 20010) {
		Debug.Log ("玩家已在房间内");
		return;
	}

	Debug.Log ("调用失败");
});
                
```   

### 游戏对战
如果玩家已经加入房间，可以通过帧同步功能进行游戏对战。游戏过程中用到的接口有发送帧消息、帧广播，您可以利用这两个接口进行帧同步。帧广播的开始、结束需要使用房间的 startFrameSync、stopFrameSync 接口。

#### 开始帧同步
使用 room.startFrameSync 接口可以开启帧广播。房间内任意一个玩家成功调用该接口将导致全部玩家开始接收帧广播。

```c#
// 开始帧同步
static void startFrameSync () {
    room.StartFrameSync (eve => {
        if (eve.Code == ErrCode.EcOk) {
            Debug.Log ("请求成功");
        }
    });
    // 广播：开始帧同步
    room.OnStartFrameSync = eve => Debug.Log ("开始帧同步");
}

```

#### 发送帧消息
玩家收到帧同步开始广播后可以发送帧消息，后台会将每个玩家的帧消息组合后广播给每个玩家。

```c#
// 用户自定义 Frame 类
[Serializable]
internal class Frame {
    [SerializeField]
    public int x;
    [SerializeField]
    public int y;
    [SerializeField]
    public string id;
}

// 发送帧消息 
static void sendFrame () {
    var frame = new Frame {
        x = 1,
        y = 1,
        id = "xxxxxxxxx"
    };
    var para = new SendFramePara {
        Data = frame.ToString ()
    };
    room.SendFrame (para, eve => {
        if (eve.Code == ErrCode.EcOk) {
            Debug.Log ("发送成功");
        }
    });
}
```

#### 接收帧广播
您可设置 room.OnRecvFrame 广播回调函数获得帧广播数据。

```c#
// 广播：收到帧消息
room.OnRecvFrame = eve => {
    RecvFrameBst bst = (RecvFrameBst) eve.Data;
    Debug.LogFormat ("帧广播: {0}", eve.Data);
};
```

#### 停止帧同步
使用 room.stopFrameSync 接口可以停止帧广播。房间内任意一个玩家成功调用该接口将导致全部玩家停止接收帧广播。

```c#
room.StopFrameSync (eve => {
	if (eve.Code == ErrCode.EcOk) {
			Debug.Log ("请求成功");
	}
});

// 广播：停止帧同步
room.OnStopFrameSync = eve => {
	Debug.LogFormat ("停止帧同步: {0}", eve.Data);
};
```



<dx-alert infotype="notice" title="">
C# SDK 可正常使用但后续不再进行更新维护。
</dx-alert>


