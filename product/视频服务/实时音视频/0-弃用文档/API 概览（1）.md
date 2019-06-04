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
| [- onLoginSuccess:](https://cloud.tencent.com/document/product/647/20036#.E7.99.BB.E5.BD.95.E4.BA.8B.E4.BB.B6)     | 登录成功事件 |
| [- onLoginFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E7.99.BB.E5.BD.95.E4.BA.8B.E4.BB.B6)     | 登录失败事件 |
| [- onLogoutSuccess:](https://cloud.tencent.com/document/product/647/20036#.E7.99.BB.E5.BD.95.E4.BA.8B.E4.BB.B6)     | 注销成功事件 |
| [- onLogoutFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E7.99.BB.E5.BD.95.E4.BA.8B.E4.BB.B6)     |  注销失败事件 |
| [- onForceOffline:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E7.99.BB.E5.BD.95.E4.BA.8B.E4.BB.B6)     | 账号下线事件 |

#### 房间事件
| 事件                   |  描述            |
| -------------------- | -------- |
| [- onCreateRoomSuccess:groupId:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 创建房间成功事件 |
| [- onCreateRoomFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 创建房间失败事件 |
| [- onJoinRoomSuccess:groupId:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 加入房间成功事件 |
| [- onJoinRoomFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 加入房间失败事件 |
| [- onQuitRoomSuccess:groupId:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 退出房间成功事件 |
| [- onQuitRoomFailed:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 退出房间失败事件 |
| [- onRoomDisconnected:module:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 房间断开连接事件 |
| [- onGroupDisband:groupId:](https://cloud.tencent.com/document/product/647/20036#.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6)     | 聊天群组解散事件 |

#### 状态事件
| 事件                   |  描述            |
| -------------------- | -------- |
| [- onRoomMemberIn:groupId:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 成员进入房间事件 |
| [- onRoomMemberOut:groupId:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 成员离开房间事件 |
| [- onCameraUpdate:enable:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 摄像头状态变更事件 |
| [- onCameraFailed:errCode:errMsg:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 摄像头操作失败事件 |
| [- onRoomHasVideo:videoType:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 视频上行开始事件 |
| [- onRoomNoVideo:videoType:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 视频上行结束事件 |
| [- onRoomHasAudio:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 音频上行开始事件 |
| [- onRoomNoAudio:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 音频下行结束事件 |
| [- onRecvVideoEvent:userId:](https://cloud.tencent.com/document/product/647/20036#.E7.8A.B6.E6.80.81.E4.BA.8B.E4.BB.B6)     | 视频数据到达事件 |

### 进阶功能接口

| API                   |  描述            |
| -------------------- | -------- |
| [– enableCamera:enable:succ:failed:](https://cloud.tencent.com/document/product/647/20038#.E5.BC.80.E5.85.B3.E7.9B.B8.E6.9C.BA)     | 开关相机|
| [– enableMic:succ:failed:](https://cloud.tencent.com/document/product/647/20038#.E5.BC.80.E5.85.B3.E9.BA.A6.E5.85.8B.E9.A3.8E)     | 开关麦克风|
| [– enableSpeaker:succ:failed:](https://cloud.tencent.com/document/product/647/20038#.E5.BC.80.E5.85.B3.E6.89.AC.E5.A3.B0.E5.99.A8)     | 开关扬声器|
| [– switchCamera:failed:](https://cloud.tencent.com/document/product/647/20038#.E5.88.87.E6.8D.A2.E7.9B.B8.E6.9C.BA.E6.96.B9.E5.90.91)     | 切换相机方向|
| [- enableCameraPreview:enable:succ:failed:](https://cloud.tencent.com/document/product/647/20038#.E6.89.93.E5.BC.80.E7.9B.B8.E6.9C.BA.E9.A2.84.E8.A7.88)   | 打开相机预览 |
| [- sendGroupMessage:succ:failed:](https://cloud.tencent.com/document/product/647/20038#.E5.8F.91.E9.80.81.E7.BE.A4.E7.BB.84.E6.B6.88.E6.81.AF)     | 发送群组消息 |
