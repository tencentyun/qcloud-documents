## Audio/Video Permission Management

The user's audio/video permission is a set of switches that determine whether the user can perform an operation in a room. The operations are **`creating rooms`**, **`entering rooms`**, **`receiving/sending camera audio/video data`** and **`receiving/sending shared audio/video data from screen`**.

The audio/video permission of a user is passed to the SDK by parameter **`AVRoomMulti.EnterRoomParam`** when calling **`AVContext.enterRoom(int roomType, AVRoom.Delegate roomDelegate, AVRoom.EnterRoomParam enterRoomParam)`** to enter a room. The values are as follows:

Permission Field Name | Description
----		| ----
AUTH\_BITS\_CREATE\_ROOM 	| Permission to create a room
AUTH\_BITS\_JOIN_ROOM 		| Permission to join a room
AUTH\_BITS\_RECV_AUDIO		| Permission to "receive" audio data
AUTH\_BITS\_RECV_VIDEO		| Permission to "receive" camera video data
AUTH\_BITS\_RECV_SUB		| Permission to "receive" shared video data from screen (no effect in Mass LVB)
AUTH\_BITS\_SEND_AUDIO		| Permission to "send" audio data
AUTH\_BITS\_SEND_VIDEO		| Permission to "send" camera video data
AUTH\_BITS\_SEND_SUB		| Permission to "send" shared video data from screen (no effect in Mass LVB)
AUTH\_BITS\_DEFUALT			| Default value. With all permissions

Mass LVB usually has two roles, the VJ and the viewer.

+ VJ: should have all permissions, i.e. **`AUTH_BITS_DEFUALT`**.
+ Viewer
	+ Viewers should not have sending permissions when **`AVContext.enterRoom()`** is called. We recommend
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
	+ Note: When a viewer joins the broadcast, the **`AVRoomMulti.changeAuthority()`** API described in the next section should be called to add the sending permission of audio/video to implement a formal joint broadcasting. After modification, the viewer's permissions become
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
		+ **`AUTH_BITS_SEND_AUDIO`**
		+ **`AUTH_BITS_SEND_VIDEO`**
		+ **`AUTH_BITS_SEND_SUB`**
	+ Note: When a viewer quits the joint broadcast, the **`AVRoomMulti.changeAuthority()`** API should be called again to cancel the viewer's audio/video data sending permissions. After modification, the viewer's permissions become
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**

Proper management of user audio/video permissions could prevent users not in a joint broadcast from using expensive [core nodes](ttps://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/oddc.md) to save bandwidth fee effectively. Implementation details about changing user audio/video permissions are in the next section.
	
## Dynamic Change of User Audio/Video Permissions

As mentioned previously, accessing of Tencent Cloud ILVB's backend can use [Core Nodes and Outer Nodes](ttps://github.com/zhaoyang21cn/suixinbo_doc/blob/master/doc2/oddc.md). Core nodes are more expensive than outer nodes in terms of bandwidth fee, and are mainly used for user roles that need uplink audio/video data or real-time interactions (VJs and users for joint broadcasting can be specified in Mass LVB business); outer nodes have cheaper bandwidth fee and are mainly used for user roles that only watch the LVB and don't need uplink audio/video data(roles other than the VJ and the users for joint broadcasting can be specified in Mass LVB business)

For businesses that need joint broadcasting, if all users set `AUTH_BITS_DEFUALT` when they enter a room, they would all be connected to core nodes and a ***_high fee_*** may be incurred. Therefore, the most economical approach is that only the VJ has all audio/video permissions (`AUTH_BITS_DEFUALT `), and all other users only have the permissions to enter the room and to watch/listen to the LVBs (`AUTH_BITS_JOIN_ROOM` | `AUTH_BITS_RECV_AUDIO` | `AUTH_BITS_RECV_VIDEO` | `AUTH_BITS_RECV_SUB`) when entering a room (`AVContext.enterRoom(`)

When a user needs to join a broadcast, the user's uplink audio/video permission (`AUTH_BITS_SEND_AUDIO` | `AUTH_BITS_SEND_VIDEO` |  `AUTH_BITS_SEND_SUB`) is granted by the SDK's **`AVRoomMulti.changeAuthority()`** API. Now, the user would be redirected from outer nodes to core nodes. The redirection is completed within the SDK and is transparent to the App. After the redirection has been completed, the callback `OnChangeAuthority()` is performed.

When quitting a broadcasting, the user's permissions for uplink audio/video is revoked by calling **`AVRoomMulti.changeAuthority()`** API (only keeps `AUTH_BITS_RECV_XXX`). At this point, the user is redirected from core nodes to outer nodes to save bandwidth fee

### Detailed Procedure for Joining a Broadcast

+ Call `boolean AVRoomMulti.changeAuthority()` API to give the joint broadcaster permissions for uplink audio/video (`AUTH_BITS_SEND_XXX`). If the returned value is True,
+ wait for callback `OnChangeAuthority:(int retCode)`, and check if `retCode` equals `av_ok`. If yes, then
+ enable microphones and cameras and start joint broadcasting (detailed example code coming soon...)

### Detailed Procedure for Quitting a Joint Broadcasting

+ Disable microphones and cameras (detailed example code coming soon...)
+ Call `boolean AVRoomMulti.changeAuthority()` API to revoke the joining user's permissions for uplink audio/video (`AUTH_BITS_SEND_XXX`). If the returned value is True, then
+ wait for callback `OnChangeAuthority:(int retCode)`, and check if `retCode` equals `av_ok`. If yes, the process is completed; otherwise, throw an exception or retry.
