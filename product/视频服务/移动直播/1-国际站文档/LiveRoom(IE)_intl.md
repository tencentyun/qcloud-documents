# LVB+Joint Broadcasting (LiveRoom) APIs (js)

**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/2ea169fa766f84576b3055ea97e3c26b.jpg" />

Tencent Cloud implements "LVB+Joint Broadcasting" by using the component [**LiveRoom**](https://cloud.tencent.com/document/product/454/14606), which involves Client and Server (available at an open-source basis on both). For more information on how to interface with the Client and Server, please see [DOC](https://cloud.tencent.com/document/product/454/14606). This document describes the APIs for Client:

> [Download](https://cloud.tencent.com/document/product/454/7873#Windows) the SDK package from Tencent Cloud's official website and download ActiveX plug-in. The zip package contains JavaScript files related to LiveRoom.

<h2 id = "LiveRoom">LiveRoom APIs</h2>

| Member Function | Description |
| --------------------------------------------- |----------------------------------------- |
| [setLiveRoomListener(object)](#setLiveRoomListener) | Sets LiveRoom callback |
| [login(object)](#login) | Logs in to the RoomService backend |
| [logout(object)](#logout) | Logs out of the RoomService backend |
| [getRoomList(object)](#getRoomList) | Obtains the room list (Optional. You can select your room list) |
| [getAudienceList(object)](#getAudienceList) | Obtains the list of viewers in a room (A maximum of 30 viewers who entered the room most recently are returned) |
| [createRoom(object)](#createRoom) | VJ: Creates a room |
| [enterRoom(object)](#enterRoom) | Viewer: Enters a room |
| [exitRoom(object)](#exitRoom) | VJ or viewer: Exits a room |
| [joinPusher(object)](#joinPusher) | Viewer: Joins joint broadcasting |
| [quitPusher(object)](#quitPusher) | Viewer: Quits joint broadcasting |
| [requestJoinPusher(object)](#requestJoinPusher) | Viewer: Initiates a joint broadcasting request |
| [acceptJoinPusher(object)](#acceptJoinPusher) | VJ: Accepts the joint broadcasting request from a viewer |
| [rejectJoinPusher(object)](#rejectJoinPusher) | VJ: Rejects the joint broadcasting request from a viewer |
| [kickoutSubPusher(object)](#kickoutSubPusher) | VJ: Kicks a viewer out of joint broadcasting |
| [startLocalPreview(object)](#startLocalPreview) | Enables local camera preview |
| [stopLocalPreview(object)](#stopLocalPreview) | Disables local camera preview |
| [switchCamera(object)](#switchCamera) | Switches between camera |
| [getCameras(object)](#getCameras) | Obtains all cameras |
| [addRemoteView(object)](#addRemoteView) | VJ/Viewer: Plays the remote video stream of a viewer in joint broadcasting |
| [deleteRemoteView(object)](#deleteRemoteView) | VJ/Viewer: Removes the remote video stream of a viewer in joint broadcasting |
| [sendRoomTextMsg(object)](#sendRoomTextMsg) | Sends a text message (on-screen comment) |
| [sendRoomCustomMsg(object)](#sendRoomCustomMsg) | Sends a custom message (gives "like" or "flower") |
| [setBeautyFilter(object)](#setBeautyFilter) | Sets beauty filter |
| [setVideoQuality(object)](#setVideoQuality) | Sets the LVB video quality |


<h2 id = "LiveRoomListener">LiveRoomListener APIs</h2>

LiveRoom's callback APIs are listed as follows, which are set via the [setLiveRoomListener](#setLiveRoomListener) method:

| API | Description |
| ---------------------------------------- | ------------------- |
| onGetPusherList(object) | Notification: The list of existing pushers in the room (the number of remote video streams) |
| onPusherJoin(object) | Notification: A new pusher joined the room (notifies you of addition of a remote video stream) |
| onPusherQuit(object) | Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
| onRoomClosed(object) | Notification: The room is closed |
| onRecvRoomTextMsg(object) | Receives a text message in the room |
| onRecvRoomCustomMsg(object) | Receives a custom message in the room |
| onRecvJoinPusherRequest(object) | VJ receives a joint broadcasting request from a viewer |
| onKickOut(object) | Viewer gets notified of being kicked out by VJ |
| onError(object) | Error callback |

## Details of LiveRoom APIs
<h3 id="setLiveRoomListener">setLiveRoomListener</h3>

- API definition: setLiveRoomListener(object):void
- API description: Sets LiveRoom callback
- Parameter description:

```object
{
	onGetPusherList(object)			    function    Notification: The list of existing pushers in the room (the number of remote video streams).
	onPusherJoin(object)				function    Notification: A new pusher joined the room (notifies you of addition of a remote video stream)
	onPusherQuit(object)				function    Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
	onRoomClosed(object)				function    Notification: Room is closed
	onRecvJoinPusherRequest(object)		function    VJ receives a joint broadcasting request from a viewer.
	onRecvRoomTextMsg(object)			function    Receives a text message in the room
	onRecvRoomCustomMsg(object)			function    Receives a custom message in the room
	onKickOut(object)					function    Viewer gets notified of being kicked out by VJ
	onError(object)						function    Error callback
}
```
- Returned result: None
- Sample code:

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

- API definition: login(object):void
- API description: Logs in to RoomService backend. You can specify whether to use the Tencent Cloud RoomService or the user-deployed RoomService (for more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)) via parameter serverDomain.
- Parameter description:

```
{  
	data: {  
		serverDomain  String   Request's backend address   
		userID        String    User ID
		userName      String    User name
		sdkAppID      String    IM login credential
		accType       Int       Account integration type
		userSig       String    IM signature
	}
	success       	function  Callback successful
	fail          	function  Callback failed
}
```
- Returned result: None
- Sample code:

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
        console.log('LiveRoom.login Login successful, userID=', res);
    },
    fail: function(){
        console.log('LiveRoom.login Login failed);
    }
});
```

<h3 id="logout">logout</h3>

- API definition: logout(object):void
- API description: Logs out of the RoomService backend
- Parameter description:

```object
{
	success       	function  Callback successful
	fail          	function  Callback failed
}
```
- Returned result: None
- Sample code:

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

- API definition: getRoomList(object):void
- API description: Pulls the list of rooms (If you already have your own room list service module, you can continue to use it).
- Parameter description:

```object
{
	{
		index		Int		The index of the room from which pull starts
		count		Int		Number of rooms to be returned via RoomService
	}
	success       	function  Callback successful
	fail          	function  Callback failed
}
```
- Returned result: None
- Sample code:

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
        console.warn('Failed to get room list', JSON.stringify(res))
    }
});
```

<h3 id="getAudienceList"> getAudienceList </h3>

- API definition: getAudienceList(object):void
- API description: Gets the list of viewers in a room. Only the last 30 viewers who entered the room are returned.
- Parameter description:

```object
{
	data: {
		roomID      String      Room number
	}
	success      function  Callback successful
	fail         function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.getAudienceList({
    data: {
        roomID: roomID
    },
    success: function(res){
        console.log('getAudienceList.success', JSON.stringify(res.data));
    },
    fail: function(res) {
        console.warn('Failed to get viewer list', JSON.stringify(res))
    }
});
```

<h3 id="createRoom"> createRoom </h3>

- API definition: createRoom(object):void
- API description: Creates a room at RoomService backend. This method can be called only after [startLocalPreview](#startLocalPreview) is called to enable local camera preview.
- Parameter description:

```object
{
	data: {
		roomInfo	String  User-defined data, which is returned as room information in the getRoomList function. 
	}
	success       	function  Callback successful
	fail          	function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.createRoom({
    data: {
        roomInfo: roomInfo
    },
    success: function(res){
        console.log('Room created successfully. Room number: ', res.roomID);
    },
    fail: function(res) {
        console.warn('Failed to create room', JSON.stringify(res))
    }
});
```

<h3 id="enterRoom"> enterRoom </h3>

- API definition: enterRoom(object):void
- API description: Viewer enters a room.
- Parameter description:

```object
{
	data: {
		roomID     String	Room number
		divId      String  div where the played video stream is located
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

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
  		console.log("Joined the room successfully");
	},
	fail: function(res) {
		alert("Failed to join the room");
	}
});
```

<h3 id="exitRoom"> exitRoom </h3>

- API definition: exitRoom(object):void
- API description: VJ (or viewer) exits a room.
- Parameter description:

```object
{
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.exitRoom({
	success: function(res) {
  		console.log("Exited the room successfully");
	},
	fail: function(res) {
		alert("Failed to exit the room");
	}
});
```

<h3 id="joinPusher"> joinPusher </h3>

- API definition: joinPusher(object):void
- API description: (Viewer) starts push and joins joint broadcasting. This method can be called only after [startLocalPreview](#startLocalPreview) is called to enable local camera preview.
- Parameter description:

```object
{
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.joinPusher({
	success: function(res) {
  		console.log("Joint broadcasting successful");
	},
	fail: function(res) {
		alert("Joint broadcasting failed:", JSON.stringify(res));
	}
});
```

<h3 id="quitPusher"> quitPusher </h3>

- API definition: quitPusher(object):void
- API description: (Viewer) quits joint broadcasting.
- Parameter description:

```object
{
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.joinPusher({
	success: function() {
  		console.log("Quit joint broadcasting successfully");
	},
	fail: function(res) {
		alert("Failed to quit joint broadcasting:", JSON.stringify(res));
	}
});
```

<h3 id="requestJoinPusher"> requestJoinPusher </h3>

- API definition: requestJoinPusher(object):void
- API description: (Viewer) sends a request to join the joint broadcasting with the VJ.
- Parameter description:

```object
{
	data: {
		timeout    Int     Timeout (ms)
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.requestJoinPusher({
	data: {
		timeout: 30000
	},
	success: function(res) {
  		console.log("VJ accepts the request");
  		LiveRoom.joinPusher({});
	},
	fail: function(res) {
		alert("Request for joining joint broadcasting failed:", JSON.stringify(res));
	}
});
```

<h3 id="acceptJoinPusher"> acceptJoinPusher </h3>

- API definition: acceptJoinPusher(object):void
- API description: (VJ) accepts viewer's request for joining joint broadcasting.
- Parameter description:

```object
{
	data: {
   		userID    String   ID of the viewer who sends a request for joining joint broadcasting
	}
}
```
- Returned result: None
- Sample code:

```
LiveRoom.acceptJoinPusher({
	data: {
		userID: userID
	}
});
```

<h3 id="rejectJoinPusher"> rejectJoinPusher </h3>

- API definition: rejectJoinPusher(object):void
- API description: (VJ) rejects viewer's request for joining joint broadcasting.
- Parameter description:

```object
{
	data: {
   		userID		String   ID of the viewer who sends a request for joining joint broadcasting
   		reason		String  Reason for rejection
	}
}
```
- Returned result: None
- Sample code:

```
LiveRoom.rejectJoinPusher({
	data: {
		userID: userID,
		reason: ''
	}
});
```

<h3 id="kickoutSubPusher"> kickoutSubPusher </h3>

- API definition: kickoutSubPusher(object):void
- API description: VJ kicks a viewer out of joint broadcasting.
- Parameter description:

```object
{
	data: {
		userID    String   ID of the viewer to be kicked out of the joint broadcasting
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.kickoutSubPusher({
	data: {
		userID: userID
	},
	success: function(res) {
  		console.log("Kicked out successfully");
	},
	fail: function(res) {
		alert("Failed to kick out:", JSON.stringify(res));
	}
});
```

<h3 id="startLocalPreview"> startLocalPreview </h3>

- API definition: startLocalPreview(object):void
- API description: VJ (or Viewer) enables camera preview.
- Parameter description:

```
{
	data: {
		divId      String  div where the pushed preview stream is located
		cameraId   String  Camera ID (you can obtain the IDs of all cameras via getCameras)
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```

- Returned result: None
- Sample code:

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
  		console.log("Preview successful");
	},
	fail: function(res) {
		alert("Failed to enable camera:", JSON.stringify(res));
	}
});
```

<h3 id="stopLocalPreview"> stopLocalPreview </h3>

- API definition: stopLocalPreview(object):void
- API description: VJ (or viewer) disables camera preview.
- Parameter description: None
- Returned result: None
- Sample code:

```
LiveRoom.stopLocalPreview();
```

<h3 id="switchCamera"> switchCamera </h3>

- API definition: switchCamera(object):void
- API description: Switches between cameras.
- Parameter description:

```object
{
	data: {
		cameraId      String  Camera ID (you can obtain the IDs of all cameras via getCameras)
	}
}
```
- Returned result: None
- Sample code:

```
LiveRoom.switchCamera({
	data: {
		cameraId: cameraId
	}
});
```

<h3 id="getCameras"> getCameras </h3>

- API definition: getCameras(object):object
- API description: Gets all cameras.
- Parameter description:

```object
{
	data: {
		divId      String  div where the pushed preview stream is located
	}
}
```
- Returned result:

```
{
	camera_cnt				Int			Number of cameras obtained
	cameralist: [
		{
			camera_name		String		Camera name
			id				String		Camera ID
		},
		...
	]
}
```
- Sample code:

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
var cameras = LiveRoom.getCameras({
	data: {
		divId: 'videoview'
	}
});
console.log('Cameras obtained: ', JSON.stringify(cameras));
```

<h3 id="addRemoteView"> addRemoteView </h3>

- API definition: addRemoteView(object):void
- API description: Plays the remote video stream of a viewer in joint broadcasting. This API is called when VJ and viewer receive onPusherJoin (notification of new viewer joining joint broadcasting).
- Parameter description:

```object
{
	data: {
		divId      String  ID of the div where the played video stream is located
		userID     String  ID of the member whose video stream is to be played
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

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
  		console.log("Playback of the remote video stream of the viewer in joint broadcasting was successful");
	},
	fail: function(res) {
		alert("Playback of the remote video stream of the viewer in joint broadcasting failed:", JSON.stringify(res));
	}
});
```

<h3 id="deleteRemoteView"> deleteRemoteView </h3>

- API definition: deleteRemoteView(object):void
- API description: Stops pushing the video stream of a viewer in joint broadcasting. This API is called when onPusherQuit (a viewer quits the joint broadcasting) is received.
- Parameter description:

```object
{
	data: {
		userID     String  ID of the member whose video image playback is to be stopped
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.deleteRemoteView({
	data: {
		userID: userID
	},
	success: function() {
  		console.log("Playback of the remote video stream of the viewer in joint broadcasting stopped successfully");
	},
	fail: function(res) {
		alert("Failed to stop the playback of the remote video stream of the viewer in joint broadcasting:", JSON.stringify(res));
	}
});
```

<h3 id="sendRoomTextMsg"> sendRoomTextMsg </h3>

- API definition: sendRoomTextMsg(object):void
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Parameter description:

```object
{
	data: {
		message     String    The text message sent
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.sendRoomTextMsg({
	data: {
		message: ''
	},
	success: function() {
		console.log("Text message sent successfully");
	},
	fail: function(res) {
		alert("Failed to send text message:", JSON.stringify(res));
	}
});
```

<h3 id="sendRoomCustomMsg"> sendRoomCustomMsg </h3>

- API definition: sendRoomCustomMsg(object):void
- API description: Sends a custom message. Other members in the room will receive a notification via onRecvRoomCustomMsg.
- Parameter description:

```object
{
	data: {
		cmd			String		Custom command
		message     String     	The custom message sent
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
LiveRoom.sendRoomCustomMsg({
	data: {
		cmd: 'like',
		message: ''
	},
	success: function() {
		console.log("Custom text message sent successfully");
	},
	fail: function(res) {
		alert("Failed to send custom text message:", JSON.stringify(res));
	}
});
```

<h3 id="setBeautyFilter"> setBeautyFilter </h3>

- API definition: setBeautyFilter(object):void
- API description: Sets beauty filter
- Parameter description:

```object
{
	data: {
		style              Int         Beauty filter style. Three styles are available: 0: Smooth; 1: Natural; 2: Hazy.
		beautyLevel        Int         Beauty filter level ranges from 1 to 9. Default is 0, which means disabling beauty filter. A higher value means a bigger effect. 
		whiteningLevel     Int         Whiteness level ranges from 1 to 9. Default is 0, which means disabling whitening. A higher value means a bigger effect.
	}
}
```
- Returned result: None
- Sample code:

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

- API definition: setVideoQuality(object):void
- API description: Sets LVB video quality
- Parameter description:

```object
{
	data: {
		quality          Int        The value ranges from 0 to 2 (indicating low, medium and high resolutions respectively). Low: 480x360/272x480; Medium: 640x480/360x640; High: 960x720/540x960. Default is 1.
		ratioType        Int        Value: 0 or 1. 0: Aspect ratio is 4:3; 1: Aspect ratio is 9:16. Default is 0.
	}
}
```
- Returned result: None
- Sample code:

```
LiveRoom.setVideoQuality({
	data: {
		quality: 1,
		ratioType: 0
	}
});
```
