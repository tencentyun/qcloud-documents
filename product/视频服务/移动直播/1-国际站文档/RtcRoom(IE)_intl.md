# Real-time Video Chat (RTCRoom) APIs (js)

## RTCRoom

| Member Function | Description |
| ---------------------------------------- | ------------------------- |
|  [setRTCRoomListener(object)](#setRTCRoomListener) | Sets RTCRoom callback |
|  [login(object)](#login) | Logs in to RoomService backend |
| [logout(object)](#logout) | Logs out of RoomService backend |
| [getRoomList(object)](#getRoomList) | Obtains the room list (Optional. You can select your room list) |
|[createRoom(object)](#createRoom) | Meeting initiator: Creates a room (roomID is optional) |
| [enterRoom(object)](#enterRoom) | Meeting participant: Enters a room |
| [exitRoom(object)](#exitRoom) | Meeting initiator/participant: Exits a room |
|[getCameras(object)](#getCameras) | Obtains all cameras |
| [switchCamera(object)](#switchCamera) | Switches between cameras |
| [startLocalPreview(object)](#startLocalPreview) | Meeting initiator/participant: Enables camera preview |
| [stopLocalPreview()](#stopLocalPreview) | Stops camera preview |
| [addRemoteView(object)](#addRemoteView) | Plays the remote video stream of a meeting participant |
| [deleteRemoteView(object)](#deleteRemoteView) | Stops playing the remote video stream of a meeting participant |
| [sendRoomTextMsg(object)](#sendRoomTextMsg) | Sends a text message (on-screen comment) |
| [sendRoomCustomMsg(object)](#sendRoomCustomMsg) | Sends a custom message (gives a "Like" or flower) |
| [setBeautyFilter(object)](#setBeautyFilter)  | Sets beauty filter |
|  [setVideoQuality(object)](#setVideoQuality) | Sets LVB video quality |



## Callback APIs

RTCRoom's callback APIs are listed as follows, which are set via the method [setRTCRoomListener](#setRTCRoomListener):

| API Definition | Description |
| --------------------------- | ---------------------------- |
| onGetPusherList(object) | Notification: The list of existing pushers in the room (the number of remote video streams).
| onPusherJoin(object) | Notification: A new pusher joined the room (notifies you of addition of a remote video stream)
| onPusherQuit(object) | Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
| onRecvRoomTextMsg(object) | Receives a text message in the room |
| onRecvRoomCustomMsg(object)  | Receives a custom message in the room |
| onRoomClosed(object) | Notification: Room is closed |
| onError(object) | Error callback |

## Details of RTCRoom APIs
### <h3 id="setRTCRoomListener">setRTCRoomListener</h3>
- API definition: setRTCRoomListener(object):void
- API description: Sets RTCRoom callback
- Parameter description:

```object
{
	onGetPusherList(object)			    function    Notification: The list of existing pushers in the room (the number of remote video streams).
	onPusherJoin(object)				function    Notification: A new pusher joined the room (notifies you of addition of a remote video stream)
	onPusherQuit(object)				function    Notification: A pusher left the room (notifies you of subtraction of a remote video stream) |
	onRecvRoomTextMsg(object)			function    Receives a text message in the room
	onRecvRoomCustomMsg(object)			function    Receives a custom message in the room
	onRoomClosed(object)				function    Notification: Room is closed
	onError(object)						function    Error callback
}
```
- Returned result: None
- Sample code:

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
- API definition:login(object):void
- API description: Logs in to the RoomService backend. You can specify whether to use the Tencent Cloud RoomService or the user-deployed RoomService via parameter serverDomain (For more information, please see [DOC](https://cloud.tencent.com/document/product/454/14606#ClientFLOW)).
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
RTCRoom.login({
    data: {
        serverDomain: 'https://room.qcloud.com/weapp/rtc_room/',
        userID: info.userID,
        sdkAppID: info.sdkAppID,
        accType: info.accType,
        userSig: info.userSig
    },
    success: function(res){
        console.log('RTCRoom.login Login successful, userID=', res);
    },
    fail: function(){
        console.log('RTCRoom.login Login failed');
    }
});
```

### <h3 id="logout"> logout </h3>

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
- API definition: getRoomList(object):void
- API description: Pulls the room list. The parameters index and count are used for paging, which means you can pull "count" rooms starting from the room numbered "index". Call of this API is not required. If you already have your own room list, you can continue to use it.
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
RTCRoom.getRoomList({
    data: {
        index: 0,
        count: 10
    },
    success: function(res){
        console.log('getRoomList.success', JSON.stringify(res.data.rooms));
    },
    fail: function(res) {
        console.warn('Failed to get room list ', JSON.stringify(res))
    }
});
```

### <h3 id="createRoom"> createRoom </h3>
- API definition: createRoom(object):void
- API description: Creates a room at RoomService backend.
- Parameter description:

```object
{
	data: {
		roomID       String  You can specify an ID for a new room with the parameter roomID, or leave it unspecified. If you do not specify an ID for the room, RoomService will automatically create a new roomID and return it to you through CreateRoomCallback.
   		roomInfo     String  Defined by creator. This information is returned via getRoomList. 
	}
	success       	function  Callback successful
	fail          	function  Callback failed
}
```
- Returned result: None
- Sample code:

```
//html
<div id="videoview" class="edu-main-video-play" width="960" height="720" style="border: 1px solid #eee; width: 960px; height: 720px;" />

//js
RTCRoom.createRoom({
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

### <h3 id="enterRoom"> enterRoom </h3>
- API definition: enterRoom(object):void
- API description: (A meeting participant) enters a room.
- Parameter description:

```object
{
	data: {
		roomID     StringRoom number
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
RTCRoom.enterRoom({
	data: {
		roomID: roomID
	},
	success: function(res) {
  		console.log("Joined the room successfully");
	},
	fail: function(res) {
		alert("Failed to join the room");
	}
});
```

### <h3 id="exitRoom"> exitRoom </h3>
- API definition: exitRoom(object):void
- API description: (A meeting initiator/participant) exits a room.
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
RTCRoom.exitRoom({
	success: function(res) {
  		console.log("Exited room successfully");
	},
	fail: function(res) {
		alert("Failed to exit the room");
	}
});
```

### <h3 id="getCameras"> getCameras </h3>

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
var cameras = RTCRoom.getCameras({
	data: {
		divId: 'videoview'
	}
});
console.log('Obtained cameras: ', JSON.stringify(cameras));
```

### <h3 id="switchCamera"> switchCamera </h3>

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
RTCRoom.switchCamera({
	data: {
		cameraId: cameraId
	}
});
```

### <h3 id="startLocalPreview"> startLocalPreview </h3>

- API definition: startLocalPreview(object):void
- API description: (A meeting initiator/participant) enables camera preview.
- Parameter description:

```object
{
	data: {
		divId      String  ID of the div where the played video stream is located
		cameraId   String Camera ID
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

RTCRoom.startLocalPreview({
   data: {
		divId: 'videoview',
        cameraId: cameraId,
   }
 });
```

### <h3 id="stopLocalPreview"> stopLocalPreview </h3>

- API definition: stopLocalPreview():void
- API description: (A meeting initiator/participant) disables camera preview.


- Returned result: None
- Sample code:

```
RTCRoom.stopLocalPreview();
```

### 

### <h3 id="addRemoteView"> addRemoteView </h3>

- API definition: addRemoteView(object):void
- API description: (A meeting initiator/participant) plays the remote video stream of a meeting participant. This API is called when onPusherJoin (notification of new meeting participant entering the room) is received.
- Parameter description:

```object
{
	data: {
		divId      String  divId where the played stream is located
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
RTCRoom.addRemoteView({
	data: {
		divId: 'videoview',
		userID: userID
	},
	success: function() {
  		console.log("Playback of meeting participant's video stream was successful");
	},
	fail: function(res) {
		alert("Playback of meeting participant's video stream failed", JSON.stringify(res));
	}
});
```

### <h3 id="deleteRemoteView"> deleteRemoteView </h3>
- API definition: deleteRemoteView(object):void
- API description: Stops playing the video of a meeting participant. This API is called when onPusherQuit (a meeting participant leaves) is received.
- Parameter description:

```object
{
	data: {
		userID     String  ID of the meeting participant whose video stream playback is to be stopped.
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
RTCRoom.deleteRemoteView({
	data: {
		userID: userID
	},
	success: function() {
  		console.log("Successfully stopped playing the meeting participant's video stream");
	},
	fail: function(res) {
		alert("Failed to stop playing the meeting participant's video stream: ", JSON.stringify(res));
	}
});
```

### <h3 id="sendRoomTextMsg"> sendRoomTextMsg </h3>
- API definition: sendRoomTextMsg(object):void
- API description: Sends a text message. Other members in the room will receive a notification via onRecvRoomTextMsg.
- Parameter description:

```object
{
	data: {
		message     String     The text message sent
	}
	success       function  Callback successful
	fail          function  Callback failed
}
```
- Returned result: None
- Sample code:

```
RTCRoom.sendRoomTextMsg({
	data: {
		message: ''
	},
	success: function() {
		console.log("Text message sent successfully");
	},
	fail: function(res) {
		alert("Failed to send text message :", JSON.stringify(res));
	}
});
```

### <h3 id="sendRoomCustomMsg"> sendRoomCustomMsg </h3>
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
RTCRoom.sendRoomCustomMsg({
	data: {
		cmd: 'like',
		message: ''
	},
	success: function() {
		console.log("Custom text message sent successfully");
	},
	fail: function(res) {
		alert("Failed to send custom text message :", JSON.stringify(res));
	}
});
```

### <h3 id="setBeautyFilter"> setBeautyFilter </h3>
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
RTCRoom.setBeautyFilter({
	data: {
		style: 0,
		beautyLevel: 5,
		whiteningLevel: 5
	}
});
```

### <h3 id="setVideoQuality"> setVideoQuality </h3>
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
RTCRoom.setVideoQuality({
	data: {
		quality: 1,
		ratioType: 0
	}
});
```
