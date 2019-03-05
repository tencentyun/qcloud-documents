## Audio/Video Room Introduction
Definition: Audio/Video room represents an enclosed space. Users can enter this space by logging in and participate in audio/video chat with other users who joined the same space. Each audio/video room has a room number (roomID). Members in different rooms do not affect each other. The room class provides a number of methods for room members to acquire room information and member information.
## Join/Exit a Room
### 1. Join a room
To join a room, following the three steps below:
(1) Configure AVMultiParam to configure parameters such as room number and audio/video scenario policy (for example, VJ scenario), to achieve customized audio/video effects.
   ![](//mccdn.qcloud.com/static/img/f20213fc76026ab7aa2f407eeb92dfa9/image.png)
	 
The enumerated values for all room parameters are listed below:
   ![](//mccdn.qcloud.com/static/img/0383ddf61f7477d11b8bc100daca4af4/image.png) 
	 ![](//mccdn.qcloud.com/static/img/923b8ddb63523817a265eae6b5edee03/image.png)
	 
(2) Implement callback function defined by the room delegate. The delegate for multiplayer room inherits its features from the delegate class of the room class AVRoom. You need to create a AVRoomMulti.Delegate object and realize callback API OnEnterRoomComplete() in this object.
   ![](//mccdn.qcloud.com/static/img/a5fbf9b759be82267c7fe72f3c413f1c/image.png)
	 
(3) Call enterRoom to join the room according to room parameters and proxy.   
**API Description:**
   ![](//mccdn.qcloud.com/static/img/ccec380f63155ba6262511fc8816da69/image.png)
	 ![](//mccdn.qcloud.com/static/img/923b8ddb63523817a265eae6b5edee03/image.png)
	 
**Sample Code:**
   ![](//mccdn.qcloud.com/static/img/13e608b48c0bfd42234f992fb45148c1/image.png)
	 ![](//mccdn.qcloud.com/static/img/a76fb417bd48d9f5fa2bc3829bc57fc3/image.png)
 
### 2. Exit the Room 
(1) The exitRoom() method internally and asynchronously executes process for exiting a room. You can only create new room once the asynchronous room exit process is completed.

(2) The result of the asynchronous process is returned by onExitRoomComplete(). This method is defined in roomDelegate, which is passed when calling the enterRoom() method.

(3) The room on the server is not terminated immediately after a user exits it. It is terminated by the server only after all the members exit it. Currently, the SDK does not provide method for terminating server rooms explicitly.

**API Description:**
   ![](//mccdn.qcloud.com/static/img/01920c5f5517c13495773597a1d118eb/image.png)
	 
**Sample Code:**
   ![](//mccdn.qcloud.com/static/img/99a145f4fb98ef6a709356f12e51a118/image.png)
## Room Listening Callback 
Apart from callback for joining and exiting rooms, the room delegation protocol AVRoomDelegate also defines 3 notification callback APIs.
### 1. Room member status update notification
After users join the room, all member updates (someone joins or exits the room) or video status changes of a certain user (someone enables or disables camera) are all notified to this method via callback.
### 2. Notification about illegal operation by room member
Different roles in a room have different permissions. For example, during LVB, the VJ should have most permissions such as sending voices and videos. An ordinary viewer should be granted permissions such as accepting voices and videos, but not sending them. Permissions for room members are specified by the authBit field and authBuffer field in the configuration parameter EnterRoomParam which is used when entering the room. If a member performs an operation without owning the corresponding permission, the SDK will call back this notification.
### 3. Callback notification about list of members who semi-automatically receive videos
The EnterRoomParam parameter configured for joining rooms includes field for configuring video receiving method (as mentioned in 2.1). When the receiving method is specified as auto, members will automatically receive existing camera video uplink data when entering a room (data for screen sharing does not follow this logic). Furthermore, members cannot receive newly added uplink camera data automatically upon entering a room, they must manually apply for the data and call the requestview() method to acquire such data. In this case, the SDK uses the callback API OnSemiAutoRecvCameraVideo() to notify App about the list of members who currently own uplink data in the room, for the App to perform rendering configuration.
    ![](//mccdn.qcloud.com/static/img/076e1a77c35b07caee4eb03b712135d3/image.png)
		
**API Description:**
    ![](//mccdn.qcloud.com/static/img/83ee3d1ac00f21fa07a770634a0da001/image.png)
		
**Sample Code:**
    ![](//mccdn.qcloud.com/static/img/4070db894c4d9bc99b6ff3e0763adfde/image.png)
## Room Members
First, use the room attribute of the AVContext instance to acquire room and force convert it into AVMultiRoom, then use the getEndpointCount and getEndPointbyId methods of AVMultiRoom to acquire all member objects of the current room.
			
**API Description:**
		![](//mccdn.qcloud.com/static/img/cac69699ca13610d8190278bee335a8f/image.png)
		
**Sample Code**:
    ![](//mccdn.qcloud.com/static/img/2ffa7d872ea9a7011f14c9debc520bd5/image.png)
## Member Permissions
We already explained about room member permissions. Apart from managing permissions by configuring authBit or authBuffer in the EnterRoomParam for joining rooms, you can also modify permissions for members in the room dynamically. All permission definitions are located in QAVCommon.h.
To modify an individual's permissions, follow the steps below:

(1) Call the ChangeAuthority() method to modify permissions for room members. Pass plaintext permission bit for the first parameter, pass ciphertext permission bit for the second parameter. Permissions are determined by the permission bit you entered (the ciphertext prevails if you enter both). Plaintext permission bit types are explained in detail in 2.1. Ciphertext permission bit strings are provided by Tencent Cloud.
(2) The result of permission modification operations is returned through callback ChangeAuthorityCallback.

**API Description:**
    ![](//mccdn.qcloud.com/static/img/b025bf0b6c79b0306394014a7beafe6b/image.png)
		
**Sample Code:**
    ![](//mccdn.qcloud.com/static/img/59742460d425b1976c532f7c54ce4287/image.png)

