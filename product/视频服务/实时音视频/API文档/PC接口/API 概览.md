实时音视频 PC API 中包括了主动调用类的功能接口、触发设置的事件通知类接口，其中功能接口有基础功能接口和进阶功能接口。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。进阶开发人员可以通过进阶功能接口通知的开发，体验实时音视频进阶功能。

### 基础功能接口

#### 全局函数

| API | 描述 |
| -- | -- |
| [GetILive](./基础功能接口.md#获取实例) | 获取iLiveSDK单实例 |

#### iLive类

| API | 描述 |
| -- | -- |
| [init](./基础功能接口.md#初始化) | 初始化iLiveSDK(必调) |
| [setChannelMode](./基础功能接口.md#设置音视频环境) | 设置SDK环境(自研环境还是云上环境) |
| [addEventHandler](./基础功能接口.md#添加事件回调) | 设置统一事件回调 |
| [clearEventHandler](./基础功能接口.md#移除所有事件回调) | 移除所有事件回调 |
| [login](./基础功能接口.md#登录) | 登录iLiveSDK |
| [logout](./基础功能接口.md#注销) | 注销iLiveSDK |
| [createRoom](./基础功能接口.md#创建房间) | 创建音视频房间 |
| [joinRoom](./基础功能接口.md#加入房间) | 加入音视频房间 |
| [switchRoom](./基础功能接口.md#切换房间) | 切换音视频房间 |
| [quitRoom](./基础功能接口.md#退出房间) | 退出音视频房间 |

### 事件通知接口

*这里仅包含通过addEventHandler设置的回调上抛的事件通知*

#### 登录事件

| 事件 | 描述 |
| -- | -- |
| [onLoginSuccess](./事件通知接口.md#登录成功事件) | 登录成功事件 |
| [onLoginFailed](./事件通知接口.md#登录失败事件) | 登录失败事件 |
| [onLogoutSuccess](./事件通知接口.md#注销成功事件) | 注销成功事件 |
| [onLogoutFailed](./事件通知接口.md#注销失败事件) | 注销失败事件 |
| [onForceOffline](./事件通知接口.md#帐号下线事件) | 帐号下线事件 |


#### 房间事件

| 事件 | 描述 |
| -- | -- |
| [onCreateRoomSuccess](./事件通知接口.md#创建房间成功事件) | 创建房间成功事件 |
| [onCreateRoomFailed](./事件通知接口.md#创建房间失败事件) | 创建房间失败事件 |
| [onJoinRoomSuccess](./事件通知接口.md#加入房间成功事件) | 加入房间成功事件 |
| [onJoinRoomFailed](./事件通知接口.md#加入房间失败事件) | 加入房间失败事件 |
| [onQuitRoomSuccess](./事件通知接口.md#退出房间成功事件) | 退出房间成功事件 |
| [onQuitRoomFailed](./事件通知接口.md#退出房间失败事件) | 退出房间失败事件 |
| [onRoomDisconnected](./事件通知接口.md#房间断开连接事件) | 房间断开连接事件 |
| [onGroupDisband](./事件通知接口.md#聊天群组解散事件) | 聊天群组解散事件 |

#### 状态事件

| 事件 | 描述 |
| -- | -- |
| [onRoomMemberIn](./事件通知接口.md#成员进入房间回调) | 成员进入房间回调 |
| [onRoomMemberOut](./事件通知接口.md#成员离开房间事件) | 成员离开房间事件 |
| [onCameraUpdate](./事件通知接口.md#摄像头状态变更事件) | 摄像头状态变更事件 |
| [onCameraFailed](./事件通知接口.md#摄像头操作失败) | 摄像头操作失败 |
| [onRoomHasVideo](./事件通知接口.md#视频上行开始事件) | 视频上行开始事件 |
| [onRoomNoVideo](./事件通知接口.md#视频上行结束事件) | 视频上行结束事件 |
| [onRoomHasAudio](./事件通知接口.md#音频上行开始事件) | 音频上行开始事件 |
| [onRoomNoAudio](./事件通知接口.md#音频上行结束事件) | 音频上行结束事件 |
| [onRecvVideoEvent](./事件通知接口.md#视频数据到达事件) | 视频数据到达事件 |


### 进阶功能接口

| API | 描述 |
| -- | -- |
| [openCamera](./进阶功能接口.md/#打开摄像头) | 打开摄像头 |
| [closeCamera](./进阶功能接口.md/#关闭摄像头) | 关闭摄像头 |
| [openMic](./进阶功能接口.md/#打开麦克风) | 打开麦克风 |
| [closeMic](./进阶功能接口.md/#关闭麦克风) | 关闭麦克风 |
| [openPlayer](./进阶功能接口.md/#打开扬声器) | 打开扬声器 |
| [closePlayer](./进阶功能接口.md/#关闭扬声器) | 关闭扬声器 |
| [openScreenShare](./进阶功能接口.md/#打开屏幕分享) | 打开屏幕分享 |
| [closeScreenShare](./进阶功能接口.md/#关闭屏幕分享) | 关闭屏幕分享 |
| [changeRole](./进阶功能接口.md/#切换角色) | 切换音视频角色 |
| [sendGroupMessage](./进阶功能接口.md/#发送群组消息) | 发送群组消息 |

## 联系我们

关注公众号"腾讯云视频"，给公众号发关键字"技术支持"，会有专人联系。

![](https://main.qcloudimg.com/raw/769293c3dbc0df8fbfb7d6a7cc904692.jpg)
