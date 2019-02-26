### stopFrameSync 停止帧同步
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|para|object|预留参数，传{}即可|
|callback|```ReqCallback<lagame.StopRsp>```|停止帧同步回调|

lagame.StopRsp 暂未定义任何字段。

调用结果将在 callback 中异步返回。调用成功后房间内全部成员将收到 stopGameBroadcast 广播。该接口会修改房间状态为”已停止帧同步“。

注意：房间内任意一个玩家成功调用该接口将导致全部玩家**停止接收**帧广播。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const seq = room.stopFrameSync({}, event => console.log(event));
```

