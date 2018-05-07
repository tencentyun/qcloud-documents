## 功能描述
**EXEStarter.js**  主要用于唤起 TXCloudRoom.exe 桌面程序，并跟 TXCloudRoom.exe 进行双向通讯，您的 Web 页面只需要 include EXEStarter.js 就可以调用其接口函数，音视频相关的复杂功能，则交给 TXCloudRoom.exe 去完成。

<h2 id = "API">接口列表</h2>

| 成员函数                                    | 功能说明                                                  |
| ------------------------------------------- | --------------------------------------------------------- |
| [setListener(object)](#setListener)         | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [createExeAsRoom(object)](#createExeAsRoom) | 通知 TXCloudRoom.exe 创建或者进入指定的房间               |
| [closeExeAsRoom(object)](#closeExeAsRoom)   | 通知 TXCloudRoom.exe 离开指定的房间                       |
| [unload()](#unload)                         | 页面在 unload 时，调用此接口，清除相关资源                |

<h2 id = "EnumDef">枚举定义</h2>

```object
var StyleType = {
    LiveRoom: 'LiveRoom',  //视频连麦模式 [支持模板Template: 1V2 | 1V3 | 1V4]
    RTCRoom: 'RTCRoom',    //视频通话模式 [支持模板Template: 1V1 | 1V2 | 1V3 | 1V4]
}
var RoomAction = {
    CreateRoom: 'createRoom',  //创建房间
    EnterRoom: 'enterRoom',   //视频通话模式
}
var Template = {
    Template1V1: '1v1',   //1推流 & 1拉流的模板
    Template1V2: '1v2',   //1推流 & 2拉流的模板
    Template1V3: '1v3',	  //1推流 & 3拉流的模板
    Template1V4: '1v4',   //1推流 & 4拉流的模板
}
```

<h2 id = "setListener">事件列表</h2>

EXEStarter.js 的事件回调和事件通知，您可以通过 **setListener**  方法设置，目前支持的事件有：

| 接口定义                                     | 功能说明                |
| ---------------------------------------- | ------------------- |
| onRoomClose(object) | 通知：EXE通知关闭 |
| onMemberChange(object) | 通知：用户列表变更通知 |
| onRecvRoomIMMsg(object) | 通知：收到 IM 消息 |
| onRecvData(object) | 通知：其他消息通知，如流状态信息等。 |

<h2 id="setListener">setListener</h2>

- 接口定义：setListener(object):void
- 接口说明：设置事件回调
- 参数说明：

```object
{
	onRoomClose(object)			function    通知：房间被动关闭，EXE出错引起
	onMemberChange(object)		function    通知：房间用户列表变更（进房、退房），全量数据
	onRecvRoomIMMsg(object)		function    通知：房间IM消息
	onRecvData(object)			function    通知：透传流状态通知
}
```
- 返回值说明：无
- 示例代码：

```
EXEStarter.setListener({
	onMemberChange: function(object) {
		//...
	},
	onRoomClose: function(object) {
		//...
	},
	
	......
});
```

<h2 id="createExeAsRoom"> createExeAsRoom</h2>

- 接口定义：createExeAsRoom(object):void
- 接口说明：通过您的账户信息和房间信息，打开本地EXE应用程序。
- 参数说明：

```
{  
  userdata: {
      userID        String    用户ID
      userName      String    用户昵称
      sdkAppID      String    IM登录凭证
      accType       Int       账号集成类型
      userSig       String    IM签名
  },
  roomdata: {
    serverDomain String  roomserver域，eg:https://room.qcloud.com/
    roomAction:  String  支持：createRoom | enterRoom
    roomId:      Int     房间号
    roomName:    String  房间名称
    roomTitle:   String  房间Title
    roomLogo:    String  图标URL
    type:        String  默认RTCRoom。更多参考StyleType定义
    template:    String  视频窗口摆放样式，默认1V1。更多参考Template定义
  },
  custom: {   //可选参数
     userList:    bool    用户列表模块，可以不设置，默认true
     IMList :     bool    IM聊天模块，可以不设置，默认true
     whiteboard:  bool    白板模块，可以不设置，默认true
     screenShare: bool    本地屏幕采集作为视频源，可以不设置，默认true
     record:      bool    后台录制当前视频流，可以不设置，默认false
     exeUrl:      String  指定自定义EXE的下载URL
     proxy_ip:    String  代理IP，可以不设置，默认不开启代理
     proxy_port:  Int     代理端口，可以不设置，默认不开启代理
  },
  success       function  成功回调
  fail          function  失败回调  errCode == -1时,检测本地未安装EXE，需要处理未安装逻辑。
}
```
- 返回值说明：无
- 示例代码：

```
EXEStarter.createExeAsRoom({
            userdata: {
                userID: accountInfo.userID,
                userName: accountInfo.userName,
                sdkAppID: accountInfo.sdkAppID,
                accType: accountInfo.accountType,
                userSig: accountInfo.userSig,
            },
            roomdata: {
                serverDomain: "https://room.qcloud.com/",
                roomAction: object.data.roomAction,
                roomID: object.data.roomID,
                roomName: object.data.roomName,
                roomTitle: object.data.roomTitle,
                roomLogo: "http://liteav.myqcloud.com/windows/logo/liveroom_logo.png",
                type: EXEStarter.StyleType.LiveRoom,
                template: EXEStarter.Template.Template1V3,
            },
            success: function (ret) {
               console.log('EXEStarter.openExeRoom 打开本地应用成功');
            },
            fail: function (ret) {
               console.log('EXEStarter.openExeRoom 打开本地应用失败');
               if (ret.errCode == -1) {
                  //本地应用未安装
               }
            },
        })
```

<h2 id="closeExeAsRoom"> closeExeAsRoom </h2>

- 接口定义：closeExeAsRoom(object):void
- 接口说明：关闭指定房间ID的EXE进程。
- 参数说明：

```object
{
    data: {
        roomID:     String  房间号
    }
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
EXEStarter.closeExeAsRoom({
	success: function(ret) {
		//...
	},
	fail: function(ret) {
		//...
	}
});
```

<h2 id="unload"> unload </h2>

- 接口定义：unload():void
- 接口说明：页面docment-unload时调用，SDK释放所有资源。
- 参数说明：无


- 返回值说明：无
- 示例代码：

```
EXEStarter.unload();
```
