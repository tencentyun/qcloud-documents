### startGameBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<RelayRoom>```|回调参数|

RelayRoom 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomId|number|房间ID|

startGameBroadcast 广播表示房间开始帧同步。收到该广播后将持续收到 frameBroadcast 广播。

**返回值说明**

无

**使用示例**

```
room.startGameBroadcast = event => console.log("开始帧同步");
```

