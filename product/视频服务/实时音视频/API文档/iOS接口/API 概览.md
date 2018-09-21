实时音视频 IOS API 中包括了主动调用类的功能接口和事件通知回调类接口，其中功能接口有基础功能接口和高级功能接口，事件通知有基础事件通知和高级事件通知。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。高级开发人员可以通过高级功能接口和高级事件通知的开发，体验实时音视频更高级功能。

### 基础功能接口

#### ILiveSDK类
| API                   |  描述            |
| -------------------- | -------- |
| [- initSdk:](./基础功能接口.md#初始化)     | ILiveSDK初始化(必调) |
| [- setChannelMode:withHost:](./基础功能接口.md#设置SDK环境) | 设置SDK环境(自研环境还是云上环境) |
| [ilveEventListener](./基础功能接口.md#设置事件回调监听) | 设置统一事件回调监听 |

#### ILiveLoginManager类
| API                   |  描述            |
| -------------------- | -------- |
| [– iLiveLogin:sig:succ:failed:](./基础功能接口.md#登录)     | 登录 |
| [– iLiveLogout:failed:](./基础功能接口.md#登出)     | 登出 |

#### ILiveRoomManager类
| API                   |  描述            |
| -------------------- | -------- |
| [– createRoom:option:succ:failed:](./基础功能接口.md#创建房间)     | 创建房间 |
| [– joinRoom:option:succ:failed:](./基础功能接口.md#加入房间)     | 加入房间 |
| [- switchRoom:option:succ:failed:](./基础功能接口.md#切换房间)     | 切换房间 |
| [– quitRoom:failed:](./基础功能接口.md#退出房间)     | 退出房间 |
| [– addRenderAt:forIdentifier:srcType:](./基础功能接口.md#创建渲染图层)     | 创建渲染图层|


### 事件通知接口

#### 登录事件

| 事件                   |  描述            |
| -------------------- | -------- |
| [- onLoginSuccess:](./事件通知接口.md#登录成功事件onloginsuccess)     | 登录成功事件 |
| [- onLoginFailed:module:errCode:errMsg:](./事件通知接口.md#登录失败事件onloginfailed)     | 登录失败事件 |
| [- onLogoutSuccess:](./事件通知接口.md#注销成功事件onlogoutsuccess)     | 注销成功事件 |
| [- onLogoutFailed:module:errCode:errMsg:](./事件通知接口.md#注销失败事件onlogoutfailed)     |  注销失败事件 |
| [- onForceOffline:module:errCode:errMsg:](./事件通知接口.md#帐号下线事件onforceoffline)     | 账号下线事件 |

#### 房间事件
| 事件                   |  描述            |
| -------------------- | -------- |
| [- onCreateRoomSuccess:groupId:](./事件通知接口.md#创建房间成功事件oncreateroomsuccess)     | 创建房间成功事件 |
| [- onCreateRoomFailed:module:errCode:errMsg:](./事件通知接口.md#创建房间失败事件oncreateroomfailed)     | 创建房间失败事件 |
| [- onJoinRoomSuccess:groupId:](./事件通知接口.md#加入房间成功事件onjoinroomsuccess)     | 加入房间成功事件 |
| [- onJoinRoomFailed:module:errCode:errMsg:](./事件通知接口.md#加入房间失败事件onjoinroomfailed)     | 加入房间失败事件 |
| [- onQuitRoomSuccess:groupId:](./事件通知接口.md#退出房间成功事件onquitroomsuccess)     | 退出房间成功事件 |
| [- onQuitRoomFailed:module:errCode:errMsg:](./事件通知接口.md#退出房间失败事件onquitroomfailed)     | 退出房间失败事件 |
| [- onRoomDisconnected:module:errCode:errMsg:](./事件通知接口.md#房间断开连接事件onroomdisconnected)     | 房间断开连接事件 |
| [- onGroupDisband:groupId:](./事件通知接口.md#聊天群组解散事件ongroupdisband)     | 聊天群组解散事件 |

#### 状态事件
| 事件                   |  描述            |
| -------------------- | -------- |
| [- onRoomMemberIn:groupId:userId:](./事件通知接口.md#成员进入房间回调onroommemberin)     | 成员进入房间事件 |
| [- onRoomMemberOut:groupId:userId:](./事件通知接口.md#成员离开房间事件onroommemberout)     | 成员离开房间事件 |
| [- onCameraUpdate:enable:](./事件通知接口.md#摄像头状态变更事件oncameraupdate)     | 摄像头状态变更事件 |
| [- onCameraFailed:errCode:errMsg:](./事件通知接口.md#摄像头操作失败oncamerafailed)     | 摄像头操作失败事件 |
| [- onRoomHasVideo:videoType:userId:](./事件通知接口.md#视频上行开始事件onroomhasvideo)     | 视频上行开始事件 |
| [- onRoomNoVideo:videoType:userId:](./事件通知接口.md#视频上行结束事件onroomnovideo)     | 视频上行结束事件 |
| [- onRoomHasAudio:userId:](./事件通知接口.md#音频上行开始事件onroomhasaudios)     | 音频上行开始事件 |
| [- onRoomNoAudio:userId:](./事件通知接口.md#音频上行结束事件onroomnoaudio)     | 音频下行结束事件 |
| [- onRecvVideoEvent:userId:](./事件通知接口.md#视频数据到达事件onrecvvideoevent)     | 视频数据到达事件 |

### 进阶功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [– enableCamera:enable:succ:failed:](./高级功能接口.md#开关相机)     | 开关相机|
| [– enableMic:succ:failed:](./高级功能接口.md#开关麦克风)     | 开关麦克风|
| [– enableSpeaker:succ:failed:](./高级功能接口.md#开关扬声器)     | 开关扬声器|
| [– switchCamera:failed:](./高级功能接口.md#切换相机方向)     | 切换相机方向|
| [- enableCameraPreview:enable:succ:failed:](./高级功能接口.md#打开相机预览)   | 打开相机预览 |
| [- changeRole:succ:failed:](./高级功能接口.md#开始推流)   | 切换音视频角色 |
| [- sendGroupMessage:succ:failed:](./高级功能接口.md#停止录制)     | 发送群组消息 |

