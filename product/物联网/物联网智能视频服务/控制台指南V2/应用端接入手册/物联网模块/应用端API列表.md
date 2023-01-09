<style> table th:nth-of-type(1) {width:30%; } table th:nth-of-type(2){ width:70%; }  </style>

## 简介

本文档为您介绍应用端 API 相关使用内容。

## 用户管理

### 相关接口

| 接口名称                                                     | 备注                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [微信号注册登录](https://cloud.tencent.com/document/product/1081/40781) | 用于微信用户注册登录，获取开发平台的用户访问 AccessToken，首次调用时，自动为该微信号注册对应账号。 |
| [手机号注册用户](https://cloud.tencent.com/document/product/1081/40783) | 提供手机号码方式的用户注册。                                 |
| [随机发送手机短信](https://cloud.tencent.com/document/product/1081/40785) | 用于手机号注册、绑定、重置密码时，发送验证码。               |
| [邮箱账号注册用户](https://cloud.tencent.com/document/product/1081/40784) | 提供邮箱账号方式注册用户。                                   |
| [随机发送邮箱验证码](https://cloud.tencent.com/document/product/1081/56316) | 用于邮箱注册、绑定、重置密码和登录时，发送验证码。           |
| [手机号、邮箱账号登录](https://cloud.tencent.com/document/product/1081/40786) | 用于手机号码、邮箱账号登录，获取用户访问 AccessToken         |
| [使用手机号重置密码](https://cloud.tencent.com/document/product/1081/47613) | 用于使用手机号重置密码。                                     |
| [使用邮箱重置密码](https://cloud.tencent.com/document/product/1081/56317) | 用于使用邮箱重置密码。                                       |
| [用户注销](https://cloud.tencent.com/document/product/1081/40787) | 用于用户退出登录态。                                         |
| [修改用户信息](https://cloud.tencent.com/document/product/1081/40788) | 用于修改用户信息。                                           |

## 配网管理

### 相关接口

| 接口名称                                                     | 备注                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) | 用于生成 Wi-Fi 配网任务的随机 Token。    |
| [查询配网 Token 状态](https://cloud.tencent.com/document/product/1081/44045) | 用于查询配网 Token 的当前状态。          |
| [用户绑定 Wi-Fi 设备](https://cloud.tencent.com/document/product/1081/44046) | 用于小程序或 App 用户绑定 Wi-Fi 类设备。 |


## 设备管理

### 相关接口

| 接口名称                                                     | 备注                                                       |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| [获取产品信息](https://cloud.tencent.com/document/product/1081/48764) | 获取产品信息                                               |
| [用户删除设备](https://cloud.tencent.com/document/product/1081/40802) | 为用户提供删除设备的功能，删除后用户需要重新配网进行绑定。 |
| [获取用户绑定设备列表](https://cloud.tencent.com/document/product/1081/40803) | 用于获取用户已绑定设备列表。                               |
| [获取设备当前状态](https://cloud.tencent.com/document/product/1081/40804) | 用于查询设备状态。                                         |
| [修改设备名称](https://cloud.tencent.com/document/product/1081/40806) | 用于修改设备名称。                                         |
| [获取设备详情](https://cloud.tencent.com/document/product/1081/40807) | 用于查询设备详情。                                         |
| [设备更换房间](https://cloud.tencent.com/document/product/1081/43201) | 设备更换房间。                                             |
| [配网绑定设备](https://cloud.tencent.com/document/product/1081/50205) | 用于小程序或 App进行 Wi-Fi 设备配网绑定操作。              |


## 设备控制

### 相关接口

| 接口名称                                                     | 备注                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [用户控制设备](https://cloud.tencent.com/document/product/1081/40805) | 用于用户对绑定的设备下发属性物模型数据，实现设备远程控制。   |
| [同步调用设备行为](https://cloud.tencent.com/document/product/1081/61347) | 用于用户向已成功绑定的设备同步下发行为物模型请求，实现设备远程控制。 |
| [异步调用设备行为](https://cloud.tencent.com/document/product/1081/61348) | 用于向用户所绑定的设备异步下发行为物模型请求，实现设备远程控制。 |

## 数据查询

### 相关接口

| 接口名称                                                     | 备注                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [获取设备物模型数据](https://cloud.tencent.com/document/product/1081/48492) | 用于获取设备物模型数据，可用于【_sys_xp2p_info】的获取。 |
| [获取设备物模型历史数据](https://cloud.tencent.com/document/product/1081/43119) | 用于获取设备物模型历史数据。                             |
| [获取设备的历史事件](https://cloud.tencent.com/document/product/1081/60783) | 用于获取设备的历史事件。                                 |

## 云存服务

| 接口名称                                                     | 备注                         |
| ------------------------------------------------------------ | ---------------------------- |
| [拉取云存事件列表](https://cloud.tencent.com/document/product/1081/80183#.E6.8B.89.E5.8F.96.E4.BA.91.E5.AD.98.E4.BA.8B.E4.BB.B6.E5.88.97.E8.A1.A8) | 用于获取云存时间列表         |
| [拉取云存事件缩略图](https://cloud.tencent.com/document/product/1081/80183#.E6.8B.89.E5.8F.96.E4.BA.91.E5.AD.98.E4.BA.8B.E4.BB.B6.E7.BC.A9.E7.95.A5.E5.9B.BE) | 用于拉取云存事件缩略图地址。 |
| [获取具有云存的日期](https://cloud.tencent.com/document/product/1081/80183#.E8.8E.B7.E5.8F.96.E5.85.B7.E6.9C.89.E4.BA.91.E5.AD.98.E7.9A.84.E6.97.A5.E6.9C.9F) | 用于获取具有云存的日期。     |
| [获取某一天云存时间轴](https://cloud.tencent.com/document/product/1081/80183#.E8.8E.B7.E5.8F.96.E5.85.B7.E6.9C.89.E4.BA.91.E5.AD.98.E7.9A.84.E6.97.A5.E6.9C.9F) | 用于获取某一天云存时间轴。   |
| [获取视频防盗链播放 URL](https://cloud.tencent.com/document/product/1081/80183#.E8.8E.B7.E5.8F.96.E6.9F.90.E4.B8.80.E5.A4.A9.E4.BA.91.E5.AD.98.E6.97.B6.E9.97.B4.E8.BD.B4) | 用于获取视频防盗链播放 URL。 |
| [拉取图片流数据](https://cloud.tencent.com/document/product/1081/80183#.E6.8B.89.E5.8F.96.E5.9B.BE.E7.89.87.E6.B5.81.E6.95.B0.E6.8D.AE) | 用于拉取图片流数据。         |


## 设备分享

| 接口名称                                                     | 备注                          |
| ------------------------------------------------------------ | ----------------------------- |
| [App 端发送设备分享](https://cloud.tencent.com/document/product/1081/43156) | 用于发送设备分享邀请。        |
| [获取设备分享 Token](https://cloud.tencent.com/document/product/1081/48183) | 用于获取设备分享 Token。      |
| [获取设备分享 Token 信息](https://cloud.tencent.com/document/product/1081/48187) | 用于获取设备分享 Token 信息。 |
| [绑定用户分享的设备](https://cloud.tencent.com/document/product/1081/48188) | 用于绑定用户分享的设备。      |
| [查询用户分享设备列表](https://cloud.tencent.com/document/product/1081/48189) | 用于查询用户分享的设备列表。  |
| [删除用户分享的设备](https://cloud.tencent.com/document/product/1081/48190) | 用于删除用户分享的设备。      |
| [查询设备的用户列表](https://cloud.tencent.com/document/product/1081/48191) | 用于查询设备用户列表。        |
| [删除设备分享的用户](https://cloud.tencent.com/document/product/1081/48192) | 用于删除设备分享的用户。      |


## 家庭管理

| 接口名称                                                     | 备注                                 |
| ------------------------------------------------------------ | ------------------------------------ |
| [创建家庭](https://cloud.tencent.com/document/product/1081/40808) | 用于创建家庭。                       |
| [删除家庭](https://cloud.tencent.com/document/product/1081/40809) | 用于删除家庭。                       |
| [修改家庭](https://cloud.tencent.com/document/product/1081/40810) | 用于修改家庭                         |
| [获取家庭列表](https://cloud.tencent.com/document/product/1081/40811) | 用于获取家庭列表。                   |
| [获取家庭详情](https://cloud.tencent.com/document/product/1081/40812) | 用于获取家庭详情。                   |
| [新建房间](https://cloud.tencent.com/document/product/1081/40813) | 用于新建房间。                       |
| [修改房间](https://cloud.tencent.com/document/product/1081/40814) | 用于修改房间。                       |
| [删除房间](https://cloud.tencent.com/document/product/1081/40815) | 用于删除房间。                       |
| [获取房间列表](https://cloud.tencent.com/document/product/1081/40816) | 用于获取房间列表。                   |
| [邀请家庭成员](https://cloud.tencent.com/document/product/1081/40817) | 用于向微信好友发送邀请加入家庭请求。 |
| [成员加入家庭](https://cloud.tencent.com/document/product/1081/40818) | 用于成员加入家庭。                   |
| [删除家庭成员](https://cloud.tencent.com/document/product/1081/40819) | 用于管理员删除家庭成员。             |
| [成员退出家庭](https://cloud.tencent.com/document/product/1081/40820) | 用于成员主动退出某个家庭。           |
| [获取家庭成员列表](https://cloud.tencent.com/document/product/1081/40821) | 用于获取家庭成员列表。               |
| [App 端邀请家庭成员](https://cloud.tencent.com/document/product/1081/43157) | 用于发送家庭分享邀请。               |


## 固件升级

| 接口名称                                                     | 备注                                             |
| ------------------------------------------------------------ | ------------------------------------------------ |
| [查询设备固件是否升级](https://cloud.tencent.com/document/product/1081/47129) | 用于查询设备固件升级信息。                       |
| [确认固件升级任务](https://cloud.tencent.com/document/product/1081/47131) | 用于用户确认升级后，云端向设备发起固件升级请求。 |
| [查询设备固件升级状态](https://cloud.tencent.com/document/product/1081/47128) | 用于查询设备固件升级状态及进度。                 |


## 长连接通信

| 接口名称                                                     | 备注                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [注册监听](https://cloud.tencent.com/document/product/1081/40792) | 用于向 WS 服务端进行订阅，订阅成功后可以通过ws.onmessage的监听获取到 WS 服务端实时推送设备上下线状态及属性数据。 |
| [心跳](https://cloud.tencent.com/document/product/1081/40791) | 设备保活，通过该接口更新设备时间戳，保持设备监听状态，同时保持 WebSocket 连接。可以多次调用，推荐每60s调用一次。 |
| [设备状态推送](https://cloud.tencent.com/document/product/1081/40793) | 设备状态推送用于在小程序或 App 实时获取用户绑定设备的上下线状态、设备上报的属性与事件以及设备行为执行结果。需要成功调用注册设备监听接口，通过监听 WebSocket 的 OnMessage 获取设备状态与属性值的实时推送，若获取到的 event.data.push 为 true，则代表该条消息为设备状态变更的主动推送。 |

