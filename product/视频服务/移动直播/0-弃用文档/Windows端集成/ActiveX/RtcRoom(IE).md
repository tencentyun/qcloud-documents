# 实时音视频（RTCRoom ）接口（js）

## RTCRoom

| 成员函数                                     | 功能说明                      |
| ---------------------------------------- | ------------------------- |
| [setRTCRoomListener(object)](#setRTCRoomListener) | 设置RTCRoom回调               |
| [login(object)](#login)                  | 登录到RoomService后台          |
| [logout(object)](#logout)                | 从RoomService后台登出          |
| [getRoomList(object)](#getRoomList)      | 获取房间列表（非必须，可选择使用您自己的房间列表） |
| [createRoom(object)](#createRoom)        | 会议创建者：创建房间 （roomID 可不填）   |
| [enterRoom(object)](#enterRoom)          | 会议参与者：进入房间                |
| [exitRoom(object)](#exitRoom)            | 会议创建者 OR 会议参与者：退出房间       |
| [getCameras(object)](#getCameras)        | 获取所有摄像头                   |
| [switchCamera(object)](#switchCamera)    | 切换摄像头                     |
| [startLocalPreview(object)](#startLocalPreview) | 会议创建者 OR 会议参与者：开启摄像头预览    |
| [stopLocalPreview()](#stopLocalPreview)  | 停止摄像头预览                   |
| [addRemoteView(object)](#addRemoteView)  | 播放会议参与者的远程视频画面            |
| [deleteRemoteView(object)](#deleteRemoteView) | 停止播放会议参与者的远程视频画面          |
| [sendRoomTextMsg(object)](#sendRoomTextMsg) | 发送文本（弹幕）消息                |
| [sendRoomCustomMsg(object)](#sendRoomCustomMsg) | 发送自定义格式消息（点赞，送花）          |
| [setBeautyFilter(object)](#setBeautyFilter) | 设置美颜                      |
| [setVideoQuality(object)](#setVideoQuality) | 设置直播的视频质量                 |



## 回调接口（interface）

RTCRoom的回调接口通过[setRTCRoomListener](#setRTCRoomListener)方法设置，其中包括有：

| 接口定义                        | 功能说明                         |
| --------------------------- | ---------------------------- |
| onGetPusherList(object)     | 通知：房间里已有的推流者列表（也就是当前有几路远程画面） |
| onPusherJoin(object)        | 通知：新的推流者加入进来（也就是通知您多了一路远程画面） |
| onPusherQuit(object)        | 通知：有推流者离开房间 （也就是通知您少了一路远程画面） |
| onRecvRoomTextMsg(object)   | 收到房间文本消息                     |
| onRecvRoomCustomMsg(object) | 收到房间自定义消息                    |
| onRoomClosed(object)        | 通知：房间解散                      |
| onError(object)             | 错误回调                         |

## RTCRoom接口详情
### <h3 id="setRTCRoomListener">setRTCRoomListener</h3>
- 接口定义：setRTCRoomListener(object):void
- 接口说明：设置RTCRoom的回调
- 参数说明：

```object
{
	onGetPusherList(object)			    function    通知：房间里已有的推流者列表（也就是当前有几路远程画面）
	onPusherJoin(object)				function    通知：新的推流者加入进来（也就是通知您多了一路远程画面）
	onPusherQuit(object)				function    通知：有推流者离开房间 （也就是通知您少了一路远程画面）
	onRecvRoomTextMsg(object)			function    收到房间文本消息
	onRecvRoomCustomMsg(object)			function    收到房间自定义消息
	onRoomClosed(object)				function    通知：房间解散
	onError(object)						function    错误回调
}
```
- 返回值说明：无
- 示例代码：

```
RTCRoom.setRTCRoomListener({
	onGetPusherList: function(object) {
		//...
	},
	onPusherJoin: function(object) {
		//...
	},
	
	......
});
```

### <h3 id="login"> login </h3>
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
RTCRoom.login({
    data: {
        serverDomain: 'https://room.qcloud.com/weapp/rtc_room/',
        userID: info.userID,
        sdkAppID: info.sdkAppID,
        accType: info.accType,
        userSig: info.userSig
    },
    success: function(res){
        console.log('RTCRoom.login 登录成功, userID=', res);
    },
    fail: function(){
        console.log('RTCRoom.login 登录失败');
    }
});
```

### <h3 id="logout"> logout </h3>

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
RTCRoom.logout({
	success: function(ret) {
		//...
	},
	fail: function(ret) {
		//...
	}
});
```

### <h3 id="getRoomList"> getRoomList </h3>
- 接口定义：getRoomList(object):void
- 接口说明：拉取房间列表，index 和 count 两个参数用于做分页处理，表示：从序号 index 的房间开始拉取 count 个房间。这并非一个必须调用的 API，如果您已经有自己的房间列表服务模块，可以继续使用。
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
RTCRoom.getRoomList({
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

### <h3 id="createRoom"> createRoom </h3>
- 接口定义：createRoom(object):void
- 接口说明：在 RoomService 后台创建一个直播房间。
- 参数说明：

```object
{
	data: {
		roomID       String  您可以通过 roomID 参数指定新房间的 ID，也可以不指定。如果您不指定房间 ID，RoomService 会自动生成一个新的 roomID 并通过 CreateRoomCallback 返回给你您。
   		roomInfo     String  由创建者自定义。在getRoomList中返回该信息 
	}
	success       	function  成功回调
	fail          	function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
RTCRoom.createRoom({
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

### <h3 id="enterRoom"> enterRoom </h3>
- 接口定义：enterRoom(object):void
- 接口说明：（会议参与者）进入直播间。
- 参数说明：

```object
{
	data: {
		roomID     String	房间号
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
RTCRoom.enterRoom({
	data: {
		roomID: roomID
	},
	success: function(res) {
  		console.log("进入房间成功");
	},
	fail: function(res) {
		alert("进入房间失败");
	}
});
```

### <h3 id="exitRoom"> exitRoom </h3>
- 接口定义：exitRoom(object):void
- 接口说明：（会议创建者 OR 会议参与者）退出房间。
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
RTCRoom.exitRoom({
	success: function(res) {
  		console.log("退出房间成功");
	},
	fail: function(res) {
		alert("退出房间失败");
	}
});
```

### <h3 id="getCameras"> getCameras </h3>

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
var cameras = RTCRoom.getCameras({
	data: {
		divId: 'videoview'
	}
});
console.log('获取到cameras: ', JSON.stringify(cameras));
```

### <h3 id="switchCamera"> switchCamera </h3>

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
RTCRoom.switchCamera({
	data: {
		cameraId: cameraId
	}
});
```

### <h3 id="startLocalPreview"> startLocalPreview </h3>

- 接口定义： startLocalPreview(object):void
- 接口说明：（会议创建者 OR 会议参与者）启动摄像头预览
- 参数说明：

```object
{
	data: {
		divId      String  播放画面所在的divId
		cameraId   String  摄像头Id
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

RTCRoom.startLocalPreview({
   data: {
		divId: 'videoview',
        cameraId: cameraId,
   }
 });
```

### <h3 id="stopLocalPreview"> stopLocalPreview </h3>

- 接口定义：stopLocalPreview():void
- 接口说明：（会议创建者 OR 会议参与者）关闭摄像头预览。


- 返回值说明：无
- 示例代码：

```
RTCRoom.stopLocalPreview();
```

### 

### <h3 id="addRemoteView"> addRemoteView </h3>

- 接口定义：addRemoteView(object):void
- 接口说明：（会议创建者 OR 会议参与者）播放会议参与者的远程视频画面 ，一般在收到 onPusherJoin（新会议参与者进入通知）时调用。
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
RTCRoom.addRemoteView({
	data: {
		divId: 'videoview',
		userID: userID
	},
	success: function() {
  		console.log("播放会议参与者画面成功");
	},
	fail: function(res) {
		alert("播放会议参与者画面失败:", JSON.stringify(res));
	}
});
```

### <h3 id="deleteRemoteView"> deleteRemoteView </h3>
- 接口定义：deleteRemoteView(object):void
- 接口说明：停止播放某个会议参与者视频，一般在收到 onPusherQuit （会议参与者离开）时调用。
- 参数说明：

```object
{
	data: {
		userID     String  要停止播放的会议参与者ID
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
RTCRoom.deleteRemoteView({
	data: {
		userID: userID
	},
	success: function() {
  		console.log("停止播放会议参与者画面成功");
	},
	fail: function(res) {
		alert("停止播放会议参与者画面失败:", JSON.stringify(res));
	}
});
```

### <h3 id="sendRoomTextMsg"> sendRoomTextMsg </h3>
- 接口定义：sendRoomTextMsg(object):void
- 接口说明：发送文本消息，房间里的其他人会收到 onRecvRoomTextMsg 通知。
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
RTCRoom.sendRoomTextMsg({
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

### <h3 id="sendRoomCustomMsg"> sendRoomCustomMsg </h3>
- 接口定义：sendRoomCustomMsg(object):void
- 接口说明：发送自定义消息，房间里的其他人会收到 onRecvRoomCustomMsg 通知。
- 参数说明：

```object
{
	data: {
		cmd			String		自定义命令
		message     String     	发送的文本消息
	}
	success       function  成功回调
	fail          function  失败回调
}
```
- 返回值说明：无
- 示例代码：

```
RTCRoom.sendRoomCustomMsg({
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

### <h3 id="setBeautyFilter"> setBeautyFilter </h3>
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
RTCRoom.setBeautyFilter({
	data: {
		style: 0,
		beautyLevel: 5,
		whiteningLevel: 5
	}
});
```

### <h3 id="setVideoQuality"> setVideoQuality </h3>
- 接口定义：setVideoQuality(object):void
- 接口说明：设置直播的视频质量
- 参数说明：

```object
{
	data: {
		quality          Int        取值0~2，分别对应低中高三种分辨率。低:480x360/272x480;中:640x480/360x640;高:960x720/540x960。默认为1
		ratioType        Int        取值0~1。0：屏幕宽高比为4:3;1:屏幕宽高比为9:16。默认为0
	}
}
```
- 返回值说明：无
- 示例代码：

```
RTCRoom.setVideoQuality({
	data: {
		quality: 1,
		ratioType: 0
	}
});
```