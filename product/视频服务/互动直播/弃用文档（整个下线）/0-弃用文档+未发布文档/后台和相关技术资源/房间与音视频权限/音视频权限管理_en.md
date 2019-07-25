## Initial Settings of User Audio/Video Permissions

A user's audio/video permission is a set of switches that determine whether the user can perform one of the following operations in a room: **`create a room`**, **`join a room`**, **`receive/send camera audio/video data`** and **`receive/send audio/video data for screen sharing`**.

User's audio/video permission is passed to SDK by the parameter **`AVRoomMulti.EnterRoomParam`** of API **`AVContext.enterRoom (int roomType, AVRoom.Delegate roomDelegate, AVRoom.EnterRoomParam enterRoomParam)`** for joining a room. The values are as follows:

Permission Field Name | Description
----		| ----
AUTH\_BITS\_CREATE\_ROOM 	| Permission to create a room
AUTH\_BITS\_JOIN_ROOM 		| Permission to join a room
AUTH\_BITS\_RECV_AUDIO		| Permission to "receive" audio data
AUTH\_BITS\_RECV_VIDEO		| Permission to "receive" camera video data
AUTH\_BITS\_RECV_SUB		| Permission to "receive" video data for screen sharing (ignored in Masses LVB)
AUTH\_BITS\_SEND_AUDIO		| Permission to "send" audio data
AUTH\_BITS\_SEND_VIDEO		| Permission to "send" camera video data
AUTH\_BITS\_SEND_SUB		| Permission to "send" video data for screen sharing (ignored in Masses LVB)
AUTH\_BITS\_DEFUALT			| Default value. With all permissions

Masses LVB generally has two roles: VJ and viewer.

+ VJ has all the permissions, i.e. **`AUTH_BITS_DEFUALT`**.
+ Viewer
	+ When a viewer calls the API **`AVContext.enterRoom()`**, he or she does not have any "send"-related permissions. The following permissions should be added:
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
	+ "Note": When a viewer needs to join broadcasting, the API **`AVRoomMulti.changeAuthority()`** described in the next section should be called to add the permission of sending audio/video to actually join broadcasting. After modification, the viewer's permissions are changed to:
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**
		+ **`AUTH_BITS_SEND_AUDIO`**
		+ **`AUTH_BITS_SEND_VIDEO`**
		+ **`AUTH_BITS_SEND_SUB`**
	+ "Note": When a viewer quits the joint broadcasting, the API **`AVRoomMulti.changeAuthority()`** should be called again to cancel the viewer's audio/video data sending permission. After modification, the viewer's permissions are changed to:
		+ **`AUTH_BITS_JOIN_ROOM`**
		+ **`AUTH_BITS_RECV_AUDIO`**
		+ **`AUTH_BITS_RECV_VIDEO`**
		+ **`AUTH_BITS_RECV_SUB`**

Reasonable control of audio/video permissions can help users who don't join broadcasting avoid using more expensive [core nodes](http://cloud.tencent.com/doc/product/268/DC与OC的分配和切换) and significantly reduce the bandwidth costs. For more information on how to change users' audio/video permissions, please see details below.
	
## Dynamic Change of User's Audio/Video Permissions

As mentioned previously, Tencent Cloud ILVB's backend can access to [core node and outer node](http://cloud.tencent.com/doc/product/268/DC与OC的分配和切换). Core node is more expensive than outer node in terms of bandwidth fee, and is mainly used for user roles (specific to VJ and users who join broadcasting in Masses LVB business) that need to send uplink audio/video data or participate in real-time interaction. Outer node has cheaper bandwidth fee and is mainly used for user roles (specific to roles other than VJ and users who join broadcasting in Masses LVB business) that only watch the LVB without the need to send uplink audio/video data.

For businesses that need joint broadcasting feature, if all users are set as `AUTH_BITS_DEFUALT` when joining a room, they would all be connected to core node, and a ***_higher fee_*** may be incurred. Therefore, the most economical approach is that when API `AVContext.enterRoom()` for joining a room is called, only VJ has all audio/video permissions (`AUTH_BITS_DEFUALT`), and all other users only have the permissions to join the room and receive audio/video data (`AUTH_BITS_JOIN_ROOM` | `AUTH_BITS_RECV_AUDIO` | `AUTH_BITS_RECV_VIDEO` | `AUTH_BITS_RECV_SUB`).

When a user needs to join broadcasting, the user's permissions for sending uplink audio/video (`AUTH_BITS_SEND_AUDIO` | `AUTH_BITS_SEND_VIDEO` |  `AUTH_BITS_SEND_SUB`) are granted via SDK's API **`AVRoomMulti.changeAuthority()`**. Now, the user is redirected from outer node to core node. The redirection is completed within the SDK and is transparent to the App. After this, the callback API `OnChangeAuthority()` is called.

When user quits broadcasting, his or her permissions for sending uplink audio/video are revoked by calling API **`AVRoomMulti.changeAuthority()`** (only `AUTH_BITS_RECV_XXX` is remained). At this point, the user is redirected from core node to outer node to save bandwidth fee.

### Steps for Joining Broadcasting

+ Call API `boolean AVRoomMulti.changeAuthority()` to grant users who join broadcasting the permissions for sending uplink audio/video (`AUTH_BITS_SEND_XXX`). If True is returned:
+ Wait for the callback `OnChangeAuthority:(int retCode)`, and determine whether `retCode` equals `av_ok`. If yes, then
+ Enable microphone and camera (specific sample client code is available soon...), and start joining broadcasting

### Steps for Quitting Broadcasting

+ Disable microphone and camera (specific sample client code is available soon...)
+ Call API `boolean AVRoomMulti.changeAuthority()` to revoke the permissions for sending uplink audio/video (`AUTH_BITS_SEND_XXX`) of users who join broadcasting. If True is returned:
+ Wait for the callback `OnChangeAuthority:(int retCode)`, and determine whether `retCode` equals `av_ok`. If yes, the process is completed; otherwise, an error occurs and try again
