实时音视频 Android API 中包括了主动调用类的功能接口、触发设置的事件通知类接口，其中功能接口有基础功能接口和进阶功能接口。初级开发人员可以通过基础功能接口和基础事件通知完成基础开发接入，即可体验实时音视频主要功能。进阶开发人员可以通过进阶功能接口通知的开发，体验实时音视频进阶功能。

### 基础功能接口

#### ILiveSDK类

| API | 描述 |
| -- | -- |
| [getInstance](./基础功能接口.md#获取实例) | 获取ILiveSDK单实例 |
| [initSdk](./基础功能接口.md#初始化) | 初始化ILiveSDK(必调) |
| [setChannelMode](./基础功能接口.md#设置音视频环境) | 设置SDK环境(自研环境还是云上环境) |
| [addEventHandler](./基础功能接口.md#添加事件回调) | 设置统一事件回调 |
| [clearEventHandler](./基础功能接口.md#移除所有事件回调) | 移除所有事件回调 |

#### ILiveLoginManager类

| API | 描述 |
| -- | -- |
| [getInstance](./基础功能接口.md#获取实例) | 获取ILiveLoginManager单实例 |
| [iLiveLogin](./基础功能接口.md#登录) | 登录iLiveSDK |
| [iLiveLogout](./基础功能接口.md#注销) | 注销iLiveSDK |


#### ILiveRoomManager类

| API | 描述 |
| -- | -- |
| [getInstance](./基础功能接口.md#获取实例) | 获取ILiveRoomManager单实例 |
| [init](./基础功能接口.md#初始化房间模块) | 初始化房间模块(必调) |
| [createRoom](./基础功能接口.md#创建房间) | 创建音视频房间 |
| [joinRoom](./基础功能接口.md#加入房间) | 加入音视频房间 |
| [switchRoom](./基础功能接口.md#切换房间) | 切换音视频房间 |
| [quitRoom](./基础功能接口.md#退出房间) | 退出音视频房间 |
| [initAvRootView](./基础功能接口.md#设置渲染控件) | 设置渲染控件 |



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

#### ILiveRoomManager类

| API | 描述 |
| -- | -- |
| [enableCamera](./进阶功能接口.md/#开关摄像头) | 打开或关闭摄像头 |
| [switchCamera](./进阶功能接口.md/#切换摄像头) | 切换前后置摄像头 |
| [enableMic](./进阶功能接口.md/#开关麦克风) | 打开或关闭麦克风 |
| [enableSpeaker](./进阶功能接口.md/#开关扬声器) | 打开或关闭扬声器 |
| [changeRole](./进阶功能接口.md/#切换角色) | 切换音视频角色 |
| [enableScreen](./进阶功能接口.md/#打开屏幕分享) | 打开屏幕分享 |
| [disableScreen](./进阶功能接口.md/#关闭屏幕分享) | 关闭屏幕分享 |
| [sendGroupMessage](./进阶功能接口.md/#发送群组消息) | 发送群组消息 |
| [sendGroupOnlineMessage](./进阶功能接口.md/#发送在线群组消息) | 发送在线群组消息(仅当前在线成员能收到) |

#### AVRootView类
| API | 描述 |
| -- | -- |
| [setSubCreatedListener](./进阶功能接口.md/#监听布局回调) | AVVideoView初始化回调(尺寸变更时也会上抛)，推荐用于布局 |
| [bindIdAndView](./进阶功能接口.md/#绑定视频渲染) | 指定用户画面渲染在指定AVVideoView(需要视频渲染前调用) |
| [swapVideoView](./进阶功能接口.md/#交换两路视频) | 交换两路视频(需要视频开始渲染后调用) |
| [setGravity](./进阶功能接口.md/#设置小屏初始位置) | 设置小屏初始位置 |
| [setSubMarginX](./进阶功能接口.md/#设置小屏横向边距) | 设置小屏初始化x轴边距 |
| [setSubMarginY](./进阶功能接口.md/#设置小屏纵向边距) | 设置小屏初始化y轴边距 |
| [setSubPadding](./进阶功能接口.md/#设置小屏间距) | 设置小屏间距 |
| [setSubWidth](./进阶功能接口.md/#设置小屏初始宽度) | 设置小屏初始宽度(默认为大屏的1/4) |
| [setSubHeight](./进阶功能接口.md/#设置小屏初始高度) | 设置小屏初始高度(默认为大屏的1/4) |

## 联系我们

关注公众号"腾讯云视频"，给公众号发关键字"技术支持"，会有专人联系。

![](https://main.qcloudimg.com/raw/769293c3dbc0df8fbfb7d6a7cc904692.jpg)
