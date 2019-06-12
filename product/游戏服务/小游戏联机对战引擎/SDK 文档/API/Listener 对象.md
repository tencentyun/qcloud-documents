
Listener 对象方法全为静态方法，不需要实例化。该对象主要用于给 Room 对象的实例绑定广播事件监听。

### init 初始化

#### 接口描述
初始化 Listener 对象。


#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|gameInfo|MGOBE.types.GameInfoPara|游戏信息|
|config|MGOBE.types.ConfigPara|游戏配置|

MGOBE.types.GameInfoPara 定义如下：

|字段名|类型|描述|
|:---|---|---|
|version|string|游戏版本|
|gameId|number|游戏 ID|
|playerId|string|玩家 ID|
|wxAppid|string|小游戏 APPID|
|secretKey|string|游戏密钥|

MGOBE.types.ConfigPara 定义如下：

|字段名|类型|描述|默认值|
|:---|---|---|---|
|reconnectMaxTimes|number|重连接次数|15|
|reconnectInterval|number|重连时间间隔，毫秒|500|
|resendInterval|number|消息重发时间间隔，毫秒|1000|
|resendTimeout|number|消息重发超时时间，毫秒|20000|
|url|string|服务地址|无|
|autoRequestFrame|boolean|是否自动补帧|false|


>?
- 该方法为静态方法。初始化 Listener 时需要传入 gameInfo 和 config 两个参数。
- ConfigPara.url 代表服务端 WebSocket 地址，开发者可以在控制台上获取该信息。在建立连接失败时，SDK 会进行多次重连尝试，最大重连次数为 ConfigPara.reconnectMaxTimes。
- ConfigPara.reconnectInterval 则定义了两次建立连接的时间间隔。如果 socket 消息发送失败，SDK 也会继续尝试发送，如果重发时间超过 ConfigPara.resendTimeout，则会通过对应的消息回调接口进行报错，每次消息重发时间间隔为 ConfigPara.resendInterval。
- ConfigPara.autoRequestFrame 为 true 则开启自动补帧功能，SDK 会记录最新帧号，如果收到的帧广播帧号不连续，则自动调用 requestFrame 接口，并将补帧信息从 onFrame 广播中返回。


#### 返回值说明
无

#### 使用示例

```
const gameInfo = {
	version: 'v1.0',
	gameId: 1234567890,
	playerId: 'xxxxxx',
	wxAppid: 'xxxxxx',
	secretKey: 'xxxxxx',
};
const config = {
	url: 'xxxxxxx.com',
	reconnectMaxTimes: 5,
	reconnectInterval: 1000,
	resendInterval: 1000,
	resendTimeout: 10000,
};
Listener.init(gameInfo, config);
```



### add 添加监听

#### 接口描述
为 Room 实例添加广播监听。

#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|room|Room|需要监听的房间对象|


>?
- 该方法为静态方法。
- 实例化 Room 对象之后，需要通过该方法给 Room 注册广播事件监听。


#### 返回值说明
无



#### 使用示例

```
const room = new Room();
Listener.add(room);
```

### remove 移除监听

#### 接口描述
为 Room 实例移除广播监听。

#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|room|Room|需要移除监听的房间对象|


>?
- 该方法为静态方法。
- 如果不再需要监听某个 Room 对象的广播事件，可以通过该方法进行移除。


#### 返回值说明
无



#### 使用示例

```
const room = new Room();
// 监听
Listener.add(room);
// 移除监听
Listener.remove(room);
```

### clear 移除全部监听

#### 接口描述
移除全部 Room 对象的广播监听。

#### 参数说明
无


>?该方法为静态方法。

#### 返回值说明
无



#### 使用示例

```
Listener.clear();
```
