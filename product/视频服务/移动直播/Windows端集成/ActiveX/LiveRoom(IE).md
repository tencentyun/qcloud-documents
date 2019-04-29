# 直播+连麦（LiveRoom ）接口（js）

**直播+连麦** 是在 **秀场直播** 和 **在线教育** 场景中经常使用的直播模式，它既能支持高并发和低成本的在线直播，又能通过连麦实现主播和观众之间的视频通话互动，具有极强的场景适用性。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/2ea169fa766f84576b3055ea97e3c26b.jpg" />

腾讯云基于 [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606) 组件实现“直播 + 连麦”功能，它分成 Client 和 Server 两个部分（都是开源的），对接攻略请参考 [DOC](https://cloud.tencent.com/document/product/454/14606)，本文档主要是详细列出了 Client 端的 API 列表：

> 在腾讯云官网 [下载](https://cloud.tencent.com/document/product/454/7873#Windows) SDK 开发包，并下载 ActiveX 插件版本，zip 包中包含 LiveRoom 相关的 javascript 文件。

<h2 id = "LiveRoom">LiveRoom接口列表</h2>

| 成员函数                                       | 功能说明                                                     |
| --------------------------------------------- |----------------------------------------- |
| [setLiveRoomListener(object)](#setLiveRoomListener)          | 设置LiveRoom回调 |
| [login(object)](#login)                                      | 登录到RoomService后台 |
| [logout(object)](#logout)                                    | 从RoomService后台登出 |
| [getRoomList(object)](#getRoomList)                          | 获取房间列表（非必须，可选择使用您自己的房间列表）|
| [getAudienceList(object)](#getAudienceList)                  | 获取某个房间里的观众列表（最多返回最近加入的 30 个观众）|
| [createRoom(object)](#createRoom)                            | 主播：创建房间|
| [enterRoom(object)](#enterRoom)                              | 观众：进入房间 |
| [exitRoom(object)](#exitRoom)                                | 主播/观众：退出房间 |
| [joinPusher(object)](#joinPusher)                            | 观众：进入连麦状态 |
| [quitPusher(object)](#quitPusher)                            | 观众：退出连麦状态 |
| [requestJoinPusher(object)](#requestJoinPusher)              | 观众：发起连麦请求 |
| [acceptJoinPusher(object)](#acceptJoinPusher)                | 主播：接受观众的连麦请求 |
| [rejectJoinPusher(object)](#rejectJoinPusher)                | 主播：拒绝观众的连麦请求 |
| [kickoutSubPusher(object)](#kickoutSubPusher)                | 主播：踢掉连麦中的某个观众 |
| [startLocalPreview(object)](#startLocalPreview)              | 开启本地摄像头预览 |
| [stopLocalPreview(object)](#stopLocalPreview)                | 停止本地摄像头预览 |
| [switchCamera(object)](#switchCamera)                        | 切换摄像头 |
| [getCameras(object)](#getCameras)                            | 获取所有摄像头 |
| [addRemoteView(object)](#addRemoteView)                      | 主播/连麦观众：播放连麦观众的远程视频画面 |
| [deleteRemoteView(object)](#deleteRemoteView)                | 主播/连麦观众：移除连麦观众的远程视频画面 |
| [sendRoomTextMsg(object)](#sendRoomTextMsg)                  | 发送文本（弹幕）消息 |
| [sendRoomCustomMsg(object)](#sendRoomCustomMsg)              | 发送自定义消息（点赞，送花） |
| [setBeautyFilter(object)](#setBeautyFilter)                  | 设置美颜 |
| [setVideoQuality(object)](#setVideoQuality)                  | 设置直播的视频质量 |


<h2 id = "LiveRoomListener">LiveRoomListener接口列表</h2>

LiveRoom的回调接口通过[setLiveRoomListener](#setLiveRoomListener)方法设置，其中包括有：

| 接口定义                                     | 功能说明                |
| ---------------------------------------- | ------------------- |
| onGetPusherList(object) 					   | 通知：房间里已有的推流者列表（也就是当前有几路远程画面） |
| onPusherJoin(object)                     | 通知：新的推流者加入进来（也就是通知您多了一路远程画面） |
| onPusherQuit(object) 						   | 通知：有推流者离开房间 （也就是通知您少了一路远程画面） |
| onRoomClosed(object)                     | 通知：房间解散 |
| onRecvRoomTextMsg(object)                | 收到房间文本消息 |
| onRecvRoomCustomMsg(object)              | 收到房间自定义消息 |
| onRecvJoinPusherRequest(object)          | 主播收到观众的连麦请求 |
| onKickOut(object)                        | 连麦观众收到被主播踢开的消息 |
| onError(object)                          | 错误回调 |

## LiveRoom接口详情
<h3 id="setLiveRoomListener">setLiveRoomListener</h3>

- 接口定义：setLiveRoomListener(object):void
- 接口说明：设置LiveRoom的回调
- 参数说明：

```object
{
	onGetPusherList(object)			    function    通知：房间里已有的推流者列表（也就是当前有几路远程画面）
	onPusherJoin(object)				function    通知：新的推流者加入进来（也就是通知您多了一路远程画面）
	onPusherQuit(object)				function    通知：有推流者离开房间 （也就是通知您少了一路远程画面）
	onRoomClosed(object)				function    通知：房间解散
	onRecvJoinPusherRequest(object)		function    主播收到观众的连麦请求
	onRecvRoomTextMsg(object)			function    收到房间文本消息
	onRecvRoomCustomMsg(object)			function    收到房间自定义消息
	onKickOut(object)					function    连麦观众收到被主播踢开的消息
	onError(object)						function    错误回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.setLiveRoomListener({
	onGetPusherList: function(object) {
		//...
	},
	onPusherJoin: function(object) {
		//...
	},
	
	......
});
```

<h3 id="login"> login </h3>

- 接口定义：login(object):void
- 接口说明：登录到 RoomService 后台，通过参数 serverDomain 可以指定是使用腾讯云的 RoomService 还是使用自建的 RoomService（具体可以参考 [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)）。
- 参数说明：

```
{  
	data: {  
		serverDomain  String   请求的后台地址   
		userID        String    用户ID
		userName      String    用户昵称
		sdkAppID      String    IM登录凭证
		accType       Int       账号集成类型
		userSig       String    IM签名
	}
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.login({
    data: {
        serverDomain: 'https://room.qcloud.com/weapp/live_room/',
        userID: info.userID,
        sdkAppID: info.sdkAppID,
        accType: info.accType,
        userSig: info.userSig
    },
    success: function(res){
        console.log('LiveRoom.login 登录成功, userID=', res);
    },
    fail: function(){
        console.log('LiveRoom.login 登录失败');
    }
});
```

<h3 id="logout"> logout </h3>

- 接口定义：logout(object):void
- 接口说明：从 RoomService 后台注销
- 参数说明：

```object
{
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.logout({
	success: function(ret) {
		//...
	},
	fail: function(ret) {
		//...
	}
});
```

<h3 id="getRoomList"> getRoomList </h3>

- 接口定义：getRoomList(object):void
- 接口说明：拉取房间列表（如果您已经有自己的房间列表服务模块，可以继续使用）。
- 参数说明：

```object
{
	{
		index		Int		从第几个房间开始拉取
		count		Int		希望 RoomService 返回的房间个数
	}
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.getRoomList({
    data: {
        index: 0,
        count: 10
    },
    success: function(res){
        console.log('getRoomList.success', JSON.stringify(res.data.rooms));
    },
    fail: function(res) {
        console.warn('获取房间列表失败', JSON.stringify(res))
    }
});
```

<h3 id="getAudienceList"> getAudienceList </h3>

- 接口定义：getAudienceList(object):void
- 接口说明：获取某个房间里的观众列表，只返回最近进入房间的 30 位观众。
- 参数说明：

```object
{
	data: {
		roomID      String      房间号
	}
	success      function  成功回调
	fail         function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.getAudienceList({
    data: {
        roomID: roomID
    },
    success: function(res){
        console.log('getAudienceList.success', JSON.stringify(res.data));
    },
    fail: function(res) {
        console.warn('获取观众列表失败', JSON.stringify(res))
    }
});
```

<h3 id="createRoom"> createRoom </h3>

- 接口定义：createRoom(object):void
- 接口说明：在 RoomService 后台创建一个直播房间。调用此方法前，必须先调用[startLocalPreview](#startLocalPreview)开启本地摄像头预览。
- 参数说明：

```object
{
	data: {
		roomInfo	String  用户自定义数据，作为房间信息会在getRoomList函数返回 
	}
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.createRoom({
    data: {
        roomInfo: roomInfo
    },
    success: function(res){
        console.log('创建房间成功，房间号为：', res.roomID);
    },
    fail: function(res) {
        console.warn('创建房间失败', JSON.stringify(res))
    }
});
```

<h3 id="enterRoom"> enterRoom </h3>

- 接口定义：enterRoom(object):void
- 接口说明：观众进入直播房间。
- 参数说明：

```object
{
	data: {
		roomID     String	房间号
		divId      String  播放画面所在div
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
LiveRoom.enterRoom({
	data: {
		roomID: roomID,
		divId: 'videoview'
	},
	success: function(res) {
  		console.log("进入房间成功");
	},
	fail: function(res) {
		alert("进入房间失败");
	}
});
```

<h3 id="exitRoom"> exitRoom </h3>

- 接口定义：exitRoom(object):void
- 接口说明：（主播 OR 观众）退出房间。
- 参数说明：

```object
{
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.exitRoom({
	success: function(res) {
  		console.log("进出房间成功");
	},
	fail: function(res) {
		alert("进出房间失败");
	}
});
```

<h3 id="joinPusher"> joinPusher </h3>

- 接口定义：joinPusher(object):void
- 接口说明：（观众）开始推流，并进入连麦状态。调用此方法前，必须先调用[startLocalPreview](#startLocalPreview)开启本地摄像头预览。
- 参数说明：

```object
{
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.joinPusher({
	success: function(res) {
  		console.log("连麦成功");
	},
	fail: function(res) {
		alert("连麦失败:", JSON.stringify(res));
	}
});
```

<h3 id="quitPusher"> quitPusher </h3>

- 接口定义：quitPusher(object):void
- 接口说明：（观众）主动退出连麦状态。
- 参数说明：

```object
{
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.joinPusher({
	success: function() {
  		console.log("退出连麦成功");
	},
	fail: function(res) {
		alert("退出连麦失败:", JSON.stringify(res));
	}
});
```

<h3 id="requestJoinPusher"> requestJoinPusher </h3>

- 接口定义：requestJoinPusher(object):void
- 接口说明：（观众）请求和主播连麦。
- 参数说明：

```object
{
	data: {
		timeout    Int     超时时间（MS）
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.requestJoinPusher({
	data: {
		timeout: 30000
	},
	success: function(res) {
  		console.log("主播同意连麦");
  		LiveRoom.joinPusher({});
	},
	fail: function(res) {
		alert("连麦请求失败:", JSON.stringify(res));
	}
});
```

<h3 id="acceptJoinPusher"> acceptJoinPusher </h3>

- 接口定义：acceptJoinPusher(object):void
- 接口说明：（主播）同意观众的连麦请求。
- 参数说明：

```object
{
	data: {
   		userID    String   申请连麦的观众ID
	}
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.acceptJoinPusher({
	data: {
		userID: userID
	}
});
```

<h3 id="rejectJoinPusher"> rejectJoinPusher </h3>

- 接口定义：rejectJoinPusher(object):void
- 接口说明：（主播）拒绝观众的连麦请求。
- 参数说明：

```object
{
	data: {
   		userID		String   申请连麦的观众ID
   		reason		String  拒绝理由
	}
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.rejectJoinPusher({
	data: {
		userID: userID,
		reason: ''
	}
});
```

<h3 id="kickoutSubPusher"> kickoutSubPusher </h3>

- 接口定义：kickoutSubPusher(object):void
- 接口说明：主播踢掉连麦中的某个观众。
- 参数说明：

```object
{
	data: {
		userID    String   要踢掉的连麦观众ID
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.kickoutSubPusher({
	data: {
		userID: userID
	},
	success: function(res) {
  		console.log("剔除成功");
	},
	fail: function(res) {
		alert("剔除失败:", JSON.stringify(res));
	}
});
```

<h3 id="startLocalPreview"> startLocalPreview </h3>

- 接口定义：startLocalPreview(object):void
- 接口说明：（主播 OR 连麦观众）启动摄像头预览。
- 参数说明：

```
{
	data: {
		divId      String  推流预览画面所在div
		cameraId   String  摄像头ID（通过getCameras可以获取所有摄像头）
	}
	success       function  成功回调
	fail          function  失败回调
}
```

- 返回值说明：无
- 示例代码：

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
var cameraId = 0;
var cameras = getCameras({
    data: {
        previewDivId: object.data.divId
    }
});
if (cameras.camera_cnt > 0) {
    cameraId = cameras.cameralist[0].id;
}

LiveRoom.startLocalPreview({
	data: {
		divId: 'videoview',
		cameraId: cameraId
	},
	success: function() {
  		console.log("预览成功");
	},
	fail: function(res) {
		alert("打开摄像头失败:", JSON.stringify(res));
	}
});
```

<h3 id="stopLocalPreview"> stopLocalPreview </h3>

- 接口定义：stopLocalPreview(object):void
- 接口说明：（主播 OR 连麦观众）关闭摄像头预览。
- 参数说明：无
- 返回值说明：无
- 示例代码：

```
LiveRoom.stopLocalPreview();
```

<h3 id="switchCamera"> switchCamera </h3>

- 接口定义：switchCamera(object):void
- 接口说明：切换摄像头。
- 参数说明：

```object
{
	data: {
		cameraId      String  摄像头ID（通过getCameras可以获取所有摄像头）
	}
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.switchCamera({
	data: {
		cameraId: cameraId
	}
});
```

<h3 id="getCameras"> getCameras </h3>

- 接口定义：getCameras(object):object
- 接口说明：获取所有摄像头。
- 参数说明：

```object
{
	data: {
		divId      String  推流预览画面所在div
	}
}
```
- 返回值说明：

```
{
	camera_cnt				Int			获取到的摄像头个数
	cameralist: [
		{
			camera_name		String		摄像头名称
			id				String		摄像头ID
		},
		...
	]
}
```
- 示例代码：

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
var cameras = LiveRoom.getCameras({
	data: {
		divId: 'videoview'
	}
});
console.log('获取到cameras: ', JSON.stringify(cameras));
```

<h3 id="addRemoteView"> addRemoteView </h3>

- 接口定义：addRemoteView(object):void
- 接口说明：播放连麦观众的远程视频画面 ，主播和连麦观众在收到 onPusherJoin（新进连麦通知）时调用。
- 参数说明：

```object
{
	data: {
		divId      String  播放画面所在的divId
		userID     String  要播放的成员ID
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
LiveRoom.addRemoteView({
	data: {
		divId: 'videoview',
		userID: userID
	},
	success: function() {
  		console.log("播放远端连麦观众画面成功");
	},
	fail: function(res) {
		alert("播放远端连麦观众画面失败:", JSON.stringify(res));
	}
});
```

<h3 id="deleteRemoteView"> deleteRemoteView </h3>

- 接口定义：deleteRemoteView(object):void
- 接口说明：停止播放某个连麦观众视频，一般在收到 onPusherQuit （连麦者离开）时调用。
- 参数说明：

```object
{
	data: {
		userID     String  要停止播放的成员ID
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.deleteRemoteView({
	data: {
		userID: userID
	},
	success: function() {
  		console.log("停止播放远端连麦观众画面成功");
	},
	fail: function(res) {
		alert("停止播放远端连麦观众画面失败:", JSON.stringify(res));
	}
});
```

<h3 id="sendRoomTextMsg"> sendRoomTextMsg </h3>

- 接口定义：sendRoomTextMsg(object):void
- 接口说明：发送文本消息，直播间里的其他人会收到 onRecvRoomTextMsg 通知。
- 参数说明：

```object
{
	data: {
		message     String     发送的文本消息
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.sendRoomTextMsg({
	data: {
		message: ''
	},
	success: function() {
		console.log("发送文本消息成功");
	},
	fail: function(res) {
		alert("发送文本消息失败:", JSON.stringify(res));
	}
});
```

<h3 id="sendRoomCustomMsg"> sendRoomCustomMsg </h3>

- 接口定义：sendRoomCustomMsg(object):void
- 接口说明：发送自定义消息。直播间其他人会收到 onRecvRoomCustomMsg 通知。
- 参数说明：

```object
{
	data: {
		cmd			String		自定义命令
		message     String     	发送的自定义消息内容
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.sendRoomCustomMsg({
	data: {
		cmd: 'like',
		message: ''
	},
	success: function() {
		console.log("发送自定义文本消息成功");
	},
	fail: function(res) {
		alert("发送自定义文本消息失败:", JSON.stringify(res));
	}
});
```

<h3 id="setBeautyFilter"> setBeautyFilter </h3>

- 接口定义：setBeautyFilter(object):void
- 接口说明：设置美颜
- 参数说明：

```object
{
	data: {
		style              Int         美颜风格.三种美颜风格：0 ：光滑  1：自然  2：朦胧
		beautyLevel        Int         美颜级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显，默认为0
		whiteningLevel     Int         美白级别取值范围 1 ~ 9； 0 表示关闭，1 ~ 9值越大，效果越明显，默认为0
	}
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.setBeautyFilter({
	data: {
		style: 0,
		beautyLevel: 5,
		whiteningLevel: 5
	}
});
```

<h3 id="setVideoQuality"> setVideoQuality </h3>

- 接口定义：setVideoQuality(object):void
- 接口说明：设置直播的视频质量
- 参数说明：

```object
{
	data: {
		quality          Int        取值0~2，分别对应低中高三种分辨率。低:480x360/272x480；中:640x480/360x640；；高:960x720/540x960。默认为1
		ratioType        Int        取值0~1。0：屏幕宽高比为4:3；1:屏幕宽高比为9:16。默认为0
	}
}
```
- 返回值说明：无
- 示例代码：

```
LiveRoom.setVideoQuality({
	data: {
		quality: 1,
		ratioType: 0
	}
});
```