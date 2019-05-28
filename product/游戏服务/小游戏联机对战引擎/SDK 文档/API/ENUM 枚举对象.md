该对象记录了 SDK 常用的几种枚举数据，且均由枚举名称（key）和值（value）组成的 object。ENUM 对象全部属性如下：

|属性名|类型|描述|
|:---|---|---|
|CreateType|MGOBE.types.CreateType|创建房间方式枚举|
|JoinType|MGOBE.types.JoinType|加入房间方式枚举|
|MatchType|MGOBE.types.MatchType|匹配类型枚举|
|NetworkState|MGOBE.types.NetworkState|网络状态枚举|
|FrameStatusType|MGOBE.types.FrameStatusType|房间帧同步状态|
|RecvRange|MGOBE.types.RecvRange|消息接收者范围枚举|

MGOBE.types.CreateType 定义如下：

|名称|值|描述|
|:---|---|---|
|COMMONCREATE|0|普通创建|
|MATCHCREATE|1|匹配创建|

MGOBE.types.JoinType 定义如下：

|名称|值|描述|
|:---|---|---|
|COMMONJOIN|0|普通加入|
|MATCHJOIN|1|匹配加入|

MGOBE.types.MatchType 定义如下：

|名称|值|描述|
|:---|---|---|
|ROOMMATCH|1|房间匹配|
|MATCH_PLAYER_COMPLEX|2|玩家匹配|

MGOBE.types.NetworkState 定义如下：

|名称|值|描述|
|:---|---|---|
|ROOM_OFFLINE|0|房间中玩家掉线|
|ROOM_ONLINE|1|房间中玩家在线|
|RELAY_OFFLINE|2|帧同步中玩家掉线|
|RELAY_ONLINE|3|帧同步中玩家在线|

MGOBE.types.FrameStatusType 定义如下：

|名称|值|描述|
|:---|---|---|
|STOP|0|未开始帧同步|
|START|1|已开始帧同步|

MGOBE.types.RecvRange 定义如下：

|名称|值|描述|
|:---|---|---|
|ROOM_ALL|1|全部玩家|
|ROOM_OTHERS|2|除自己外的其他玩家|
|ROOM_SOME|3|房间中部分玩家|
