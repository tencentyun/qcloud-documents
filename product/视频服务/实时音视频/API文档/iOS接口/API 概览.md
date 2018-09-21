实时音视频 IOS API 中包括了主动调用类的功能接口和事件通知回调类接口，其中功能接口有基础功能接口和高级功能接口，事件通知有基础事件通知和高级事件通知。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。高级开发人员可以通过高级功能接口和高级事件通知的开发，体验实时音视频更高级功能。

### 基础功能接口

#### ILiveSDK类
| API                   |  描述            |
| -------------------- | -------- |
| [- initSdk:](https://cloud.tencent.com/document/product/647/20037#ilivesdk.E7.B1.BB)     | ILiveSDK初始化(必调) |
| [- setChannelMode:withHost:](https://cloud.tencent.com/document/product/647/20037#ilivesdk.E7.B1.BB) | 设置SDK环境(自研环境还是云上环境) |
| [ilveEventListener](https://cloud.tencent.com/document/product/647/20037#ilivesdk.E7.B1.BB) | 设置统一事件回调监听 |

#### ILiveLoginManager类
| API                   |  描述            |
| -------------------- | -------- |
| [– iLiveLogin:sig:succ:failed:](https://cloud.tencent.com/document/product/647/20037#iliveloginmanager.E7.B1.BB录)     | 登录 |
| [– iLiveLogout:failed:](https://cloud.tencent.com/document/product/647/20037#iliveloginmanager.E7.B1.BB)     | 登出 |

#### ILiveRoomManager类
| API                   |  描述            |
| -------------------- | -------- |
| [– createRoom:option:succ:failed:](https://cloud.tencent.com/document/product/647/20037#iliveroommanager.E7.B1.BB)     | 创建房间 |
| [– joinRoom:option:succ:failed:](https://cloud.tencent.com/document/product/647/20037#iliveroommanager.E7.B1.BB)     | 加入房间 |
| [- switchRoom:option:succ:failed:](https://cloud.tencent.com/document/product/647/20037#iliveroommanager.E7.B1.BB)     | 切换房间 |
| [– quitRoom:failed:](https://cloud.tencent.com/document/product/647/20037#iliveroommanager.E7.B1.BB)     | 退出房间 |
| [– addRenderAt:forIdentifier:srcType:](https://cloud.tencent.com/document/product/647/20037#iliveroommanager.E7.B1.BB)     | 创建渲染图层|


### 事件通知接口

#### 登录事件

| 事件                   |  描述            |
| -------------------- | -------- |
| [- onLoginSuccess:](https://cloud.tencent.com/document/product/647/20036)     | 登录成功事件 |
| [- onLoginFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036)     | 登录失败事件 |
| [- onLogoutSuccess:](https://cloud.tencent.com/document/product/647/20036)     | 注销成功事件 |
| [- onLogoutFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036)     |  注销失败事件 |
| [- onForceOffline:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036)     | 账号下线事件 |

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
