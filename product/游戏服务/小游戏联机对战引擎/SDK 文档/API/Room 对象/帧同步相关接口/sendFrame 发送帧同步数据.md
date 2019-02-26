### sendFrame 发送帧同步数据
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|data|object|帧数据|
|callback|```ReqCallback<lagame.FrameInputRsp>```|发送帧同步数据回调|

lagame.FrameInputRsp 暂未定义任何字段。

帧数据内容 data 类型为普通 object， 由开发者自定义，目前支持最大长度不超过 1k。后台将集合全部玩家的帧数据，并以一定时间间隔（由创建房间时的帧率定义）通过 frameBroadcast 广播给各客户端。

调用结果将在 callback 中异步返回。

注意：只有房间处于”已开始帧同步“状态才能调用该接口。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const frame = {x: 100, y: 100, dir: 30, id: "xxxxxxxx"};
let seq = room.sendFrame(frame, event => console.log(event));
```

