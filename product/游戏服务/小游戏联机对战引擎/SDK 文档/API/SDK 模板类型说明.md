>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。

SDK 在使用过程中会收到两类消息，即响应消息和广播消息。
- 响应消息指由客户端主动发起请求后，服务器返回的响应，消息类型为 ResponseEvent。
- 广播消息指服务器主动向客户端发起的消息，消息类型为 BroadcastEvent。

每种响应、广播的数据由下文“[响应消息](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E6.B6.88.E6.81.AF-mgobe.types.responseevent)”、“[广播消息](https://cloud.tencent.com/document/product/1038/33331#.E5.B9.BF.E6.92.AD.E6.B6.88.E6.81.AF-mgobe.types.broadcastevent)”定义。
客户端向服务器发起请求后，可以设置响应回调函数，回调函数类型由下文“[响应回调函数](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)”定义。

### 响应消息 MGOBE.types.ResponseEvent
#### MGOBE.types.ResponseEvent 的 TypeScript  定义如下：
```
interface ResponseEvent<T> {
    code: number;
    msg: string;
    seq: string;
    data?: T;
}
```
#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|code|number|消息错误码|
|msg|string|错误信息|
|seq|string|请求序列号|
|data|object|消息数据，由各消息回调接口定义|

SDK 使用 TypeScript 的模板类型定义了 data 字段，具体的 data 结构由 API 各接口定义。
- 如```MGOBE.types.ResponseEvent<MGOBE.types.CreateRoomRsp>```定义了创建房间的响应消息，其中 data 的类型为```MGOBE.types.CreateRoomRsp```。
- 由于有些响应消息没有 data 内容，API 将使用```MGOBE.types.ResponseEvent<null>```来表示这类响应消息。

### 广播消息 MGOBE.types.BroadcastEvent
#### MGOBE.types.BroadcastEvent 的 TypeScript  定义如下：
```
interface BroadcastEvent<T> {
    data?: T;
}
```
#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|data|object|消息数据，由各消息回调接口定义|

广播消息是由服务端主动发起，只含有 data 一个字段。Room 对象各个广播接口中有具体 data 定义。
如 ```MGOBE.types.BroadcastEvent<MGOBE.types.DismissRoomBst>``` 定义了解散房间广播消息，其中 data 的类型为```MGOBE.types.DismissRoomBst```。

### 响应回调函数 MGOBE.types.ReqCallback

#### MGOBE.types.ReqCallback 的 TypeScript  定义如下：
```
ReqCallback<T> = (event: MGOBE.types.ResponseEvent<T>) => any;
```
响应函数是使用 SDK 接口向后台发起请求后，后台返回消息时的回调函数。上述定义表明该函数的入参是响应消息 MGOBE.types.ResponseEvent，函数体由您自定义。
