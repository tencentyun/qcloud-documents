
<h2 id = "API">功能导读</h2>

**EXEStarter.js**  主要用于唤起 TXCloudRoom.exe 桌面程序，并跟 TXCloudRoom.exe 进行双向通讯，您的 Web 页面只需要 include EXEStarter.js 就可以调用其接口函数。音视频相关的复杂功能，则交给 TXCloudRoom.exe 去完成。

EXEStarter 目前支持 **LiveRoom**、**RtcRoom** 和 **PushPlay** 三个标签对象，[LiveRoom](https://cloud.tencent.com/document/product/454/14606) 用于直播连麦（在线教育中的大班课）功能，[RtcRoom](https://cloud.tencent.com/document/product/454/14617) 用于视频通话（双人视频通话或者多人视频会议）功能，PushPlay 用于实现基础的推拉流功能。

- **直播连麦（LiveRoom）和视频通话（RtcRoom）场景**
直播连麦可以用于在线教育场景，尤其是典型的大班课场景，视频通话则可以用于多人实时音视频场景。在使用 [LiveRoom](#LiveRoom) 或者 [RTCRoom](#RtcRoom) 时，您的后台需要帮忙分配房间号和用户id。

![](https://main.qcloudimg.com/raw/c89609dcfa5388a7a3d4d00d5d7f94cc.png)

- **双人视频通话（PushPlay）场景**
对于双人音视频通话的场景，由于本身原理上非常简单（通话双方各分配一个推流地址和一个低延时加速地址），很多客户会选择使用简单的推拉（[PushPlay](#PushPlay) ）解决方案，在使用该方案时，您的后台需要帮忙分配推流地址和低延时加速地址。

![](https://main.qcloudimg.com/raw/3f4ecfc1f4614b26adbcaff3e2e69b8f.png)


<h2 id = "EnumDef">枚举定义</h2>

```object
EnumDef = (function () {
	var RoomAction = {
        CreateRoom: 'createRoom',  //创建房间
        EnterRoom: 'enterRoom',    //视频通话模式
    }
    var Template = {
        Template1V1: '1v1',		   //1v1视频模板
        Template1V2: '1v2',		   //1v2视频模板
        Template1V3: '1v3',		   //1v3视频模板
        Template1V4: '1v4',         //1v4视频模板
    };
    var ScreenRecordType = {
        RecordNone : 0,  		   //无录制状态
        RecordScreenToServer: 1,    //录制视频窗口数据到后台
        RecordScreenToClient: 2,    //录制视频窗口数据到本地
        RecordScreenToBoth: 3,      //录制视频窗口数据到本地
    };
})()
```



<h2 id = "LiveRoom">LiveRoom</h2>

<h3 id = "LiveRoom.API">接口列表</h3>

| 成员函数                                     | 功能说明                                                  |
| -------------------------------------------- | --------------------------------------------------------- |
| [setListener(object)](#LiveRoom.setListener) | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [startEXE(object)](#LiveRoom.startEXE)       | 通知 TXCloudRoom.exe 创建或者进入指定的房间               |
| [stopEXE(object)](#LiveRoom.stopEXE)         | 通知 TXCloudRoom.exe 离开指定的房间                       |
| [unload()](#LiveRoom.unload)                 | 页面在 unload 时，调用此接口，清除相关资源                |

<h3 id = "LiveRoom.EventList">事件列表</h3>

LiveRoom 的事件回调和事件通知，您可以通过 **setListener**  方法设置，目前支持的事件有：

| 接口定义                                     | 功能说明                |
| ---------------------------------------- | ------------------- |
| onRoomClose(object) | 通知：EXE通知关闭 |
| onMemberChange(object) | 通知：用户列表变更通知 |
| onRecvRoomIMMsg(object) | 通知：收到 IM 消息 |
| onRecvEvent(object) | 通知：其他消息通知，如流状态信息等。 |

<h3 id="LiveRoom.setListener">LiveRoom.setListener</h3>

- 接口定义：setListener(object):void
- 接口说明：设置事件回调
- 参数说明：

```object
{
	onRoomClose(object)			function    通知：房间被动关闭，EXE出错引起
	onMemberChange(object)		function    通知：房间用户列表变更（进房、退房），全量数据
	onRecvRoomIMMsg(object)		function    通知：房间IM消息
	onRecvEvent(object)			function    通知：透传流状态通知
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.setListener({
	onMemberChange: function(object) {
		//...
	},
	onRoomClose: function(object) {
		//...
	},
	
	......
});
```

<h3 id="LiveRoom.startEXE">LiveRoom.startEXE</h3>

- 接口定义：startEXE(object):void
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
    template:    String  视频窗口摆放样式，默认1V1。更多参考Template定义
  },
  custom: {   //可选参数
     userList:    bool    用户列表模块，可以不设置，默认true
     IMList :     bool    IM聊天模块，可以不设置，默认true
     whiteboard:  bool    白板模块，可以不设置，默认true
     screenShare: bool    屏幕分享模块，可以不设置，默认true
     exeUrl:      String  指定自定义EXE的下载URL
     proxy_ip:    String  代理IP，可以不设置，默认不开启代理
     proxy_port:  Int     代理端口，可以不设置，默认不开启代理
     singleton:   bool    exe是否设置单例模式，可以不设置，默认开启。
     mixRecord:   bool    云端混流录制，开通点播服务才能起效。可以不设置，默认关闭。
     screenRecord:  Int   录屏模式，参考EnumDef.ScreenRecordType定义
     cloudRecordUrl:String 录屏模式地址 screenRecord == EnumDef.ScreenRecordType.RecordScreenToServer需要用到。
  },
  success       function  成功回调
  fail          function  失败回调  errCode == -1时,检测本地未安装EXE，需要处理未安装逻辑。
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.startEXE({
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
                template: EnumDef.Template.Template1V3,
            },
            success: function (ret) {
               console.log('LiveRoom.startEXE 打开本地应用成功');
            },
            fail: function (ret) {
               console.log('LiveRoom.startEXE 打开本地应用失败');
               if (ret.errCode == -1) {
                  //本地应用未安装
               }
            },
        })
```

<h3 id="LiveRoom.stopEXE">LiveRoom.stopEXE</h3>

- 接口定义：stopEXE(object):void
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
LiveRoom.stopEXE({
	success: function(ret) {
		//...
	},
	fail: function(ret) {
		//...
	}
});
```

<h3 id="LiveRoom.unload">LiveRoom.unload</h3>

- 接口定义：unload():void
- 接口说明：页面docment-unload时调用，SDK释放所有资源。
- 参数说明：无


- 返回值说明：无
- 示例代码：

```
LiveRoom.unload();
```


<h3 id="LiveRoom.Code">示例代码 </h3>

如下示例代码展示了如何使用 EXEStarter.js中的LiveRoom对象启动 TXCloudRoom.exe

```html
<HTML>
<HEAD>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
    <TITLE>web+exe解决方案test | LiveRoom示例</TITLE>
    <script type="text/javascript" src="./js/EXEStarter.js" charset="utf-8"></script>
</HEAD>
<BODY>
    <input type=submit value="开课" onClick="opencourse()">
    <input type=submit value="下载EXE"  id="download" style="display:none" onClick="downloadExe()">
    <div id="text_div"></div>
    <script>
        function downloadExe() {
            window.open(EnumDef.EXEUrl);
        }
        function opencourse()
		{
            var userID = 'user_1212312', roomID = 'room_123123'; //您业务中的userid和roomid
            var roomserverInfo;
            var roomServerDomain = "https://room.qcloud.com/";
            var ListServerDoMain = "http://xzb.qcloud.com/roomlist/weapp/webexe_room/";
            //第一步：通过您的账号userid，获取您的业务服务器的 usersig
            getSDKLoginInfo({
                data: {  userID: userID, 
                         loginServerDoMain: ListServerDoMain + "get_login_info",
                         method : "GET",time: 24 * 60 * 60 * 7
                },
                success: function (res) {
                    if (res.status && res.status === 200) {
                        roomserverInfo = res.data;

                        //第二步：设置事件监听
                        LiveRoom.setListener({
                            onRoomClose: function (ret) { 
                                //监控返回的事件，具体参考SDK接口。
                                alert("【errMsg:" + ret.data.msg + "】");
                            }
                        });

                        document.getElementById('text_div').innerHTML = '正在打开EXE，请稍后.....';
                        //第三步：通过usersig和您的房间信息，拉起本地应用程序。
                        LiveRoom.startEXE({
                            userdata: {
                                userID: roomserverInfo.userID,
                                userName: "雷锋",
                                sdkAppID: roomserverInfo.sdkAppID,
                                accType: roomserverInfo.accountType,
                                userSig: roomserverInfo.userSig,
                            },
                            roomdata: {
                                serverDomain: roomServerDomain,
                                roomAction: EnumDef.RoomAction.CreateRoom,
                                roomID: roomID,
                                roomName: "雷锋的房间",
                                roomTitle: "LiveRoom视频直播间",
                                roomLogo: "",
                                template: EnumDef.Template.Template1V3,
                            },
                            success: function (ret) { },
                            fail: function (ret) {
                                /////////////////////////////////////////////////
							    // ATTENTION
				    			// ret.errCode == -1 代表网页检测到用户并没有安装 TXCloudRoom.exe。
							    // 需要在网页上弹出一个下载提示框，提示用户进行下载安装。
                                //
                                if (ret.errCode == -1) {
                                    // 这段代码用于显示 “请下载并安装房间服务” 的提示语。
                                    document.getElementById('download').style.display = 'block';
                                }
                            },
                        })
                    }
                },
            });
           
        }
    </script>
</BODY>
</HTML>
```




<h2 id = "RtcRoom API">RtcRoom</h2>

<h3 id = "RtcRoom.API">接口列表</h3>

| 成员函数                                    | 功能说明                                                  |
| ------------------------------------------- | --------------------------------------------------------- |
| [setListener(object)](#RtcRoom.setListener) | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [startEXE(object)](#RtcRoom.startEXE)       | 通知 TXCloudRoom.exe 创建或者进入指定的房间               |
| [stopEXE(object)](#RtcRoom.stopEXE)         | 通知 TXCloudRoom.exe 离开指定的房间                       |
| [unload()](#RtcRoom.unload)                 | 页面在 unload 时，调用此接口，清除相关资源                |

<h3 id = "RtcRoom.setListener">事件列表</h3>

RtcRoom 的事件回调和事件通知，您可以通过 **setListener**  方法设置，目前支持的事件有：

| 接口定义                | 功能说明                             |
| ----------------------- | ------------------------------------ |
| onRoomClose(object)     | 通知：EXE通知关闭                    |
| onMemberChange(object)  | 通知：用户列表变更通知               |
| onRecvRoomIMMsg(object) | 通知：收到 IM 消息                   |
| onRecvEvent(object)     | 通知：其他消息通知，如流状态信息等。 |

<h3 id="RtcRoom.setListener">RtcRoom.setListener</h3>

- 接口定义：setListener(object):void
- 接口说明：设置事件回调
- 参数说明：

```object
{
	onRoomClose(object)			function    通知：房间被动关闭，EXE出错引起
	onMemberChange(object)		function    通知：房间用户列表变更（进房、退房），全量数据
	onRecvRoomIMMsg(object)		function    通知：房间IM消息
	onRecvEvent(object)			function    通知：透传流状态通知
}
```

- 返回值说明：无
- 示例代码：

```
RtcRoom.setListener({
	onMemberChange: function(object) {
		//...
	},
	onRoomClose: function(object) {
		//...
	},
	
	......
});
```

<h3 id="RtcRoom.startEXE">RtcRoom.startEXE</h3>

- 接口定义：startEXE(object):void
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
    template:    String  视频窗口摆放样式，默认1V1。更多参考Template定义
  },
  custom: {   //可选参数
     userList:    bool    用户列表模块，可以不设置，默认true
     IMList :     bool    IM聊天模块，可以不设置，默认true
     whiteboard:  bool    白板模块，可以不设置，默认true
     screenShare: bool    屏幕分享模块，可以不设置，默认true
     exeUrl:      String  指定自定义EXE的下载URL
     proxy_ip:    String  代理IP，可以不设置，默认不开启代理
     proxy_port:  Int     代理端口，可以不设置，默认不开启代理
     singleton:   bool    exe是否设置单例模式，可以不设置，默认开启。
     mixRecord:   bool    云端混流录制，开通点播服务才能起效。可以不设置，默认关闭。
     screenRecord:  Int   录屏模式，参考EnumDef.ScreenRecordType定义
     cloudRecordUrl:String 录屏模式地址 screenRecord == EnumDef.ScreenRecordType.RecordScreenToServer需要用到。
  },
  success       function  成功回调
  fail          function  失败回调  errCode == -1时,检测本地未安装EXE，需要处理未安装逻辑。
}
```

- 返回值说明：无
- 示例代码：

```
RtcRoom.startEXE({
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
                template: EnumDef.Template.Template1V3,
            },
            success: function (ret) {
               console.log('RtcRoom.startEXE 打开本地应用成功');
            },
            fail: function (ret) {
               console.log('RtcRoom.startEXE 打开本地应用失败');
               if (ret.errCode == -1) {
                  //本地应用未安装
               }
            },
        })
```

<h3 id="RtcRoom.stopEXE">RtcRoom.stopEXE</h3>

- 接口定义：stopEXE(object):void
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
RtcRoom.stopEXE({
	success: function(ret) {
		//...
	},
	fail: function(ret) {
		//...
	}
});
```

<h3 id="RtcRoom.unload">RtcRoom.unload</h3>

- 接口定义：unload():void
- 接口说明：页面docment-unload时调用，SDK释放所有资源。
- 参数说明：无

- 返回值说明：无
- 示例代码：

```
RtcRoom.unload();
```



<h2 id = "PushPlay">PushPlay</h2>

<h3 id = "PushPlay.API">接口列表</h3>

| 成员函数                                     | 功能说明                                                  |
| -------------------------------------------- | --------------------------------------------------------- |
| [setListener(object)](#PushPlay.setListener) | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [startEXE(object)](#PushPlay.startEXE)       | 通知 TXCloudRoom.exe 以推拉流模式创建                     |
| [stopEXE()](#PushPlay.stopEXE)               | 通知 TXCloudRoom.exe 退出推拉流模式                       |
| [unload()](#PushPlay.unload)                 | 页面在 unload 时，调用此接口，清除相关资源                |
| [videoSnapshot()](#PushPlay.videoSnapshot)   | 截图接口                                                  |

<h3 id = "PushPlay.EventList">事件列表</h3>

PushPlay 的事件回调和事件通知，您可以通过 **setListener**  方法设置，目前支持的事件有：

| 接口定义            | 功能说明                             |
| ------------------- | ------------------------------------ |
| onRecvEvent(object) | 通知：其他消息通知，如流状态信息等。 |

<h3 id="PushPlay.setListener">PushPlay.setListener</h3>

- 接口定义：setListener(object):void
- 接口说明：设置事件回调
- 参数说明：

```object
{
	onRecvEvent(object)			function    通知：透传流状态通知
}
```

- 返回值说明：无
- 示例代码：

```
PushPlay.setListener({
	onRecvEvent: function(object) {
		//...
	}
});
```

<h3 id="PushPlay.startEXE">PushPlay.startEXE</h3>

- 接口定义：startEXE(object):void
- 接口说明：通过您的流地址信息，打开本地EXE应用程序。
- 参数说明：

```
{  
  data: {
      pushURL       String    推流地址
      playURL       String    拉流地址
      title         String    Title
      logoUrl       String    logo图片地址
  },
  custom: {   //可选参数
     top_window   Bool    默认false,是否置顶窗口。可以不设置，默认不开启
     proxy_ip:    String  代理IP，可以不设置，默认不开启
     proxy_port:  Int     代理端口，可以不设置，默认不开启
     singleton:   bool    exe是否设置单例模式，可以不设置，默认开启。
  },
  success       function  成功回调
  fail          function  失败回调  errCode == -1时,检测本地未安装EXE，需要处理未安装逻辑。
}
```

- 返回值说明：无
- 示例代码：

```
  PushPlay.startEXE({
                data: {
                    type: "CustomServiceLive",
                    pushURL: pushUrl,
                    playURL: playUrl,
                    title: "CS Demo",
                    logoUrl: "http://liteavsdk/logo/doubleroom_logo.png",
                },
                success: function (ret) {
                },
                fail: function (ret) {
                    if (ret.errCode == -1) {
                        alert("exe未安装");
                    }
                },
            });
```

<h3 id="PushPlay.stopEXE">PushPlay.stopEXE</h3>

- 接口定义：stopEXE():void
- 接口说明：关闭推拉流模式的EXE进程。
- 参数说明：无
- 返回值说明：无

- 示例代码：

```
PushPlay.stopEXE();
```

<h3 id="PushPlay.unload">PushPlay.unload </h3>

- 接口定义：unload():void
- 接口说明：页面docment-unload时调用，SDK释放所有资源。
- 参数说明：无

- 返回值说明：无
- 示例代码：

```
PushPlay.unload();
```

<h3 id="PushPlay.videoSnapshot">PushPlay.videoSnapshot</h3>

- 接口定义：videoSnapshot(object):void
- 接口说明：截图接口，图片数据从事件回调:onRecvEvent中获取，eg：{"event":"snapshot", "base64Img:"xxxxx", "id":"xxx"}。
- 参数说明：

```
{
   data: {
       userRole:  String   取值[pusher-截图推流端]\[player-截图拉流端]
   },
}
```

- 返回值说明：无
- 示例代码：

```
  PushPlay.videoSnapshot({ data: { userRole: "player" } });
```
