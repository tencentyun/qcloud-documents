实时音视频 PC API 中包括了主动调用类的功能接口、触发设置的事件通知类接口，其中功能接口有基础功能接口和进阶功能接口。初级开发人员可以通过基础功能接口和基础事件通知接口完成基础开发接入，即可体验实时音视频主要功能。进阶开发人员可以通过进阶功能接口的接入开发，体验实时音视频进阶功能。

### 基础功能接口

#### 全局函数

| API | 描述 |
| -- | -- |
| [GetILive](https://cloud.tencent.com/document/product/647/30018#.E8.8E.B7.E5.8F.96.E5.AE.9E.E4.BE.8B) | 获取 iLiveSDK 单实例 |

#### iLive类

| API | 描述 |
| -- | -- |
| [init](https://cloud.tencent.com/document/product/647/30018#.E5.88.9D.E5.A7.8B.E5.8C.96) | 初始化 iLiveSDK(必调) |
| [setChannelMode](https://cloud.tencent.com/document/product/647/30018#.E8.AE.BE.E7.BD.AE.E9.9F.B3.E8.A7.86.E9.A2.91.E7.8E.AF.E5.A2.83) | 设置 SDK 环境(自研环境还是云上环境) |
| [addEventHandler](https://cloud.tencent.com/document/product/647/30018#.E6.B7.BB.E5.8A.A0.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83) | 设置统一事件回调 |
| [clearEventHandler](https://cloud.tencent.com/document/product/647/30018#.E7.A7.BB.E9.99.A4.E6.89.80.E6.9C.89.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83) | 移除所有事件回调 |
| [login](https://cloud.tencent.com/document/product/647/30018#.E7.99.BB.E5.BD.95) | 登录 iLiveSDK |
| [logout](https://cloud.tencent.com/document/product/647/30018#.E6.B3.A8.E9.94.80) | 注销 iLiveSDK |
| [createRoom](https://cloud.tencent.com/document/product/647/30018#.E5.88.9B.E5.BB.BA.E6.88.BF.E9.97.B4) | 创建音视频房间 |
| [joinRoom](https://cloud.tencent.com/document/product/647/30018#.E5.8A.A0.E5.85.A5.E6.88.BF.E9.97.B4) | 加入音视频房间 |
| [switchRoom](https://cloud.tencent.com/document/product/647/30018#.E5.88.87.E6.8D.A2.E6.88.BF.E9.97.B4) | 切换音视频房间 |
| [quitRoom](https://cloud.tencent.com/document/product/647/30018#.E9.80.80.E5.87.BA.E6.88.BF.E9.97.B4) | 退出音视频房间 |

### 事件通知接口

*这里仅包含通过 addEventHandler 设置的回调上抛的事件通知*。

#### 登录事件

| 事件 | 描述 |
| -------- | ------- |
| [onLoginSuccess](https://cloud.tencent.com/document/product/647/30017#.E7.99.BB.E5.BD.95.E6.88.90.E5.8A.9F.E4.BA.8B.E4.BB.B6) | 登录成功事件 |
| [onLoginFailed](https://cloud.tencent.com/document/product/647/30017#.E7.99.BB.E5.BD.95.E5.A4.B1.E8.B4.A5.E4.BA.8B.E4.BB.B6) | 登录失败事件 |
| [onLogoutSuccess](https://cloud.tencent.com/document/product/647/30017#.E6.B3.A8.E9.94.80.E6.88.90.E5.8A.9F.E4.BA.8B.E4.BB.B6) | 注销成功事件 |
| [onLogoutFailed](https://cloud.tencent.com/document/product/647/30017#.E6.B3.A8.E9.94.80.E5.A4.B1.E8.B4.A5.E4.BA.8B.E4.BB.B6) | 注销失败事件 |
| [onForceOffline](https://cloud.tencent.com/document/product/647/30017#.E5.B8.90.E5.8F.B7.E4.B8.8B.E7.BA.BF.E4.BA.8B.E4.BB.B6) | 帐号下线事件 |


#### 房间事件

| 事件 | 描述 |
| -- | -- |
| [onCreateRoomSuccess](https://cloud.tencent.com/document/product/647/30017#.E5.88.9B.E5.BB.BA.E6.88.BF.E9.97.B4.E6.88.90.E5.8A.9F.E4.BA.8B.E4.BB.B6) | 创建房间成功事件 |
| [onCreateRoomFailed](https://cloud.tencent.com/document/product/647/30017#.E5.88.9B.E5.BB.BA.E6.88.BF.E9.97.B4.E5.A4.B1.E8.B4.A5.E4.BA.8B.E4.BB.B6) | 创建房间失败事件 |
| [onJoinRoomSuccess](https://cloud.tencent.com/document/product/647/30017#.E5.8A.A0.E5.85.A5.E6.88.BF.E9.97.B4.E6.88.90.E5.8A.9F.E4.BA.8B.E4.BB.B6) | 加入房间成功事件 |
| [onJoinRoomFailed](https://cloud.tencent.com/document/product/647/30017#.E5.8A.A0.E5.85.A5.E6.88.BF.E9.97.B4.E5.A4.B1.E8.B4.A5.E4.BA.8B.E4.BB.B6) | 加入房间失败事件 |
| [onQuitRoomSuccess](https://cloud.tencent.com/document/product/647/30017#.E9.80.80.E5.87.BA.E6.88.BF.E9.97.B4.E6.88.90.E5.8A.9F.E4.BA.8B.E4.BB.B6) | 退出房间成功事件 |
| [onQuitRoomFailed](https://cloud.tencent.com/document/product/647/30017#.E9.80.80.E5.87.BA.E6.88.BF.E9.97.B4.E5.A4.B1.E8.B4.A5.E4.BA.8B.E4.BB.B6) | 退出房间失败事件 |
| [onRoomDisconnected](https://cloud.tencent.com/document/product/647/30017#.E6.88.BF.E9.97.B4.E6.96.AD.E5.BC.80.E8.BF.9E.E6.8E.A5.E4.BA.8B.E4.BB.B6) | 房间断开连接事件 |
| [onGroupDisband](https://cloud.tencent.com/document/product/647/30017#.E8.81.8A.E5.A4.A9.E7.BE.A4.E7.BB.84.E8.A7.A3.E6.95.A3.E4.BA.8B.E4.BB.B6) | 聊天群组解散事件 |

#### 状态事件

| 事件 | 描述 |
| -- | -- |
| [onRoomMemberIn](https://cloud.tencent.com/document/product/647/30017#.E6.88.90.E5.91.98.E8.BF.9B.E5.85.A5.E6.88.BF.E9.97.B4.E5.9B.9E.E8.B0.83) | 成员进入房间回调 |
| [onRoomMemberOut](https://cloud.tencent.com/document/product/647/30017#.E6.88.90.E5.91.98.E7.A6.BB.E5.BC.80.E6.88.BF.E9.97.B4.E4.BA.8B.E4.BB.B6) | 成员离开房间事件 |
| [onCameraUpdate](https://cloud.tencent.com/document/product/647/30017#.E6.91.84.E5.83.8F.E5.A4.B4.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4.E4.BA.8B.E4.BB.B6) | 摄像头状态变更事件 |
| [onCameraFailed](https://cloud.tencent.com/document/product/647/30017#.E6.91.84.E5.83.8F.E5.A4.B4.E6.93.8D.E4.BD.9C.E5.A4.B1.E8.B4.A5) | 摄像头操作失败 |
| [onRoomHasVideo](https://cloud.tencent.com/document/product/647/30017#.E8.A7.86.E9.A2.91.E4.B8.8A.E8.A1.8C.E5.BC.80.E5.A7.8B.E4.BA.8B.E4.BB.B6) | 视频上行开始事件 |
| [onRoomNoVideo](https://cloud.tencent.com/document/product/647/30017#.E8.A7.86.E9.A2.91.E4.B8.8A.E8.A1.8C.E7.BB.93.E6.9D.9F.E4.BA.8B.E4.BB.B6) | 视频上行结束事件 |
| [onRoomHasAudio](https://cloud.tencent.com/document/product/647/30017#.E9.9F.B3.E9.A2.91.E4.B8.8A.E8.A1.8C.E5.BC.80.E5.A7.8B.E4.BA.8B.E4.BB.B6) | 音频上行开始事件 |
| [onRoomNoAudio](https://cloud.tencent.com/document/product/647/30017#.E9.9F.B3.E9.A2.91.E4.B8.8A.E8.A1.8C.E7.BB.93.E6.9D.9F.E4.BA.8B.E4.BB.B6) | 音频上行结束事件 |
| [onRecvVideoEvent](https://cloud.tencent.com/document/product/647/30017#.E8.A7.86.E9.A2.91.E6.95.B0.E6.8D.AE.E5.88.B0.E8.BE.BE.E4.BA.8B.E4.BB.B6) | 视频数据到达事件 |


### 进阶功能接口

| API | 描述 |
| -- | -- |
| [openCamera](https://cloud.tencent.com/document/product/647/30019#.E6.89.93.E5.BC.80.E6.91.84.E5.83.8F.E5.A4.B4) | 打开摄像头 |
| [closeCamera](https://cloud.tencent.com/document/product/647/30019#.E5.85.B3.E9.97.AD.E6.91.84.E5.83.8F.E5.A4.B4) | 关闭摄像头 |
| [openMic](https://cloud.tencent.com/document/product/647/30019#.E6.89.93.E5.BC.80.E9.BA.A6.E5.85.8B.E9.A3.8E) | 打开麦克风 |
| [closeMic](https://cloud.tencent.com/document/product/647/30019#.E5.85.B3.E9.97.AD.E9.BA.A6.E5.85.8B.E9.A3.8E) | 关闭麦克风 |
| [openPlayer](https://cloud.tencent.com/document/product/647/30019#.E6.89.93.E5.BC.80.E6.89.AC.E5.A3.B0.E5.99.A8) | 打开扬声器 |
| [closePlayer](https://cloud.tencent.com/document/product/647/30019#.E5.85.B3.E9.97.AD.E6.89.AC.E5.A3.B0.E5.99.A8) | 关闭扬声器 |
| [openScreenShare](https://cloud.tencent.com/document/product/647/30019#.E6.89.93.E5.BC.80.E5.B1.8F.E5.B9.95.E5.88.86.E4.BA.AB) | 打开屏幕分享 |
| [closeScreenShare](https://cloud.tencent.com/document/product/647/30019#.E5.85.B3.E9.97.AD.E5.B1.8F.E5.B9.95.E5.88.86.E4.BA.AB) | 关闭屏幕分享 |
| [changeRole](https://cloud.tencent.com/document/product/647/30019#.E5.88.87.E6.8D.A2.E8.A7.92.E8.89.B2) | 切换音视频角色 |
| [sendGroupMessage](https://cloud.tencent.com/document/product/647/30019#.E5.8F.91.E9.80.81.E7.BE.A4.E7.BB.84.E6.B6.88.E6.81.AF) | 发送群组消息 |

## 联系我们

关注公众号"腾讯云视频"，给公众号发关键字"技术支持"，会有专人联系。

![](https://main.qcloudimg.com/raw/769293c3dbc0df8fbfb7d6a7cc904692.jpg)
