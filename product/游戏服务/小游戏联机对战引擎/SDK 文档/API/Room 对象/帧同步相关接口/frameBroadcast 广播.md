### frameBroadcast 广播

**参数说明**

|参数名|类型|描述|
|---|---|---|---|
|event|```ResponseEvent<RelayFrame>```|回调参数|

RelayFrame 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|frameId|number|帧ID|
|frameItems|lagame.FrameItem[]|帧内容|
|ext|lagame.FrameExtInfo|附加信息|
|time|number|该帧到达客户端时间|
|isReplay|boolean|是否为补帧|

lagame.FrameItem 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|openId|string|玩家ID|
|data|string|玩家帧内容|
|timestamp|number|时间戳，各玩家本地发送帧的时间|

lagame.FrameExtInfo 定义如下：
|字段名|类型|描述|
|:---|---|---|---|
|seed|number|随机数种子|

frameBroadcast 广播表示收到帧消息，帧内容由多个 lagame.FrameItem 组成，即一帧时间内房间内所有玩家向服务器发送帧消息的集合。每个 lagame.FrameItem 包含玩家ID、玩家帧内容、服务器收到该帧的时间戳。time 表示该 FrameItem 到达客户端的时间。

由于网络状态发生掉帧时，SDK 会进行自动补帧，使用 isReplay 区分补帧与正常帧。当 isReplay 为 true 时，该帧为补帧，此时 time 为 SDK 拟合的时间，即 SDK 利用正常帧推算出来该补帧按照正常广播中的顺序到达客户端的时间。一般来说，拟合出来的 time 值小于 补帧达到客户端的真正时间。

**返回值说明**

无

**使用示例**

```
room.frameBroadcast = event => {
	console.log("帧广播", event.data);
};
```

