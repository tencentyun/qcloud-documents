该对象记录了 SDK 常用的几种枚举数据，且均由枚举名称（key）和值（value）组成的 object。ENUM 对象全部属性如下：

|属性名|类型|描述|
|:---|---|---|
|CreateType|lagame.CreateType|创建房间方式枚举|
|JoinType|lagame.JoinType|加入房间方式枚举|
|MatchType|lagame.MatchType|匹配类型枚举|
|NetworkState|lagame.NetworkState|网络状态枚举|
|UserLocate|lagame.UserLocate|用户位置枚举|
|RoomStatusType|lagame.RoomStatusType|房间状态|

lagame.CreateType 定义如下：

|名称|值|描述|
|:---|---|---|
|COMMONCREATE|0|普通创建|
|MATCHCREATE|1|匹配创建|

lagame.JoinType 定义如下：

|名称|值|描述|
|:---|---|---|
|COMMONJOIN|0|普通加入|
|MATCHJOIN|1|匹配加入|

lagame.MatchType 定义如下：

|名称|值|描述|
|:---|---|---|
|ONLINEMATCH|0|在线匹配|
|ROOMMATCH|1|房间匹配|

lagame.NetworkState 定义如下：

|名称|值|描述|
|:---|---|---|
|ROOM_OFFLINE|0|房间中玩家掉线|
|ROOM_ONLINE|1|房间中玩家在线|
|RELAY_OFFLINE|2|游戏中玩家掉线|
|RELAY_ONLINE|3|游戏中玩家在线|

lagame.UserLocate 定义如下：

|名称|值|描述|
|:---|---|---|
|INHALL|0|在大厅|
|INROOM|1|在房间|

lagame.RoomStatusType 定义如下：

|名称|值|描述|
|:---|---|---|
|STOP|0|未开始帧同步|
|START|1|已开始帧同步|
