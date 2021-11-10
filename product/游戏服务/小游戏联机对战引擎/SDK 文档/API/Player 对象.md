Player 对象为 MGOBE 的子属性，用于访问玩家的基本信息，例如玩家 ID、openId 等。


### 对象描述
玩家信息。

### 参数描述

|属性名|类型|描述|
|:---|---|---|
|id|string|玩家 ID|
|openId|string|玩家 openId|
|name|string|玩家昵称|
|teamId|string|队伍 ID|
|customPlayerStatus|number|自定义玩家状态|
|customProfile|string|自定义玩家属性|
|commonNetworkState|[MGOBE.types.NetworkState](https://cloud.tencent.com/document/product/1038/35534#networkstate)|房间网络状态|
|relayNetworkState|[MGOBE.types.NetworkState](https://cloud.tencent.com/document/product/1038/35534#networkstate)|帧同步网络状态|



<dx-alert infotype="explain" title="">
- 该对象记录了玩家的基本信息，默认全部为空。成功初始化 Listener 后，ID、openId 属性将生效。
- 玩家进入房间后，该对象的属性与 roomInfo.playerList 中当前玩家信息保持一致。
- 玩家 ID 是 MGOBE 后台生成的 ID，openId 是您初始化时候使用的 ID。openId 只有初始化 Listener 的时候使用，其它接口的“玩家 ID”均指 MGOBE 后台生成的 ID。
</dx-alert>







