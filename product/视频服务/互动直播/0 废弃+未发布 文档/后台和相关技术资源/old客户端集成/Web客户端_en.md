**1. Login**

Log in to IM cloud service. Before initiating an audio/video session, the App needs to log in to the service.

```
Login(sdk_app_id, account_type, app_id_at3rd, identifier, user_sig);
```

**Parameter**

```
sdk_app_id: App ID.
account_type: Account type.
app_id_at3rd: appid of the third-party App.
identifier: User account.
user_sig: User identity authentication information.
```

**Returned Value**
None

>Note
Before initiating an audio/video session, the App needs to call the API Login to log in to IM service. Only after the callback indicating the success of login is returned can the audio/video session be initiated. 

**2. StartContext**

Start the SDK and create a context.

```
StartContext(sdk_app_id, account_type, app_id_at3rd, identifier, user_sig);
```

**Parameter**

```
sdk_app_id: App ID.
account_type: Account type.
app_id_at3rd: appid of the third-party App.
identifier: User account.
user_sig: User identity authentication information.
```

**Returned Value**
None

>Note
StartContext cannot be called until the callback indicating the success of Login is returned. Only after the callback indicating the success of execution of StartContext is returned can other APIs be called.

**3. StopContext**

Stop the SDK and release the context.

```
StopContext()
```

**Returned Value**

S_OK: API call is successful. 
None

>Note
Call StopContext when terminating an audio/video session to release context resources.

**4. EnterRoom**

Join a room.

```
EnterRoom(room_type, relation_type, relation_id, mode, auther);
```

**Parameter**

```
room_type: Room type. It should always be 2, which means a multi-people room.
relation_type: Relation type. It should always be 6.
relation_id: Relation ID (room number).
mode: Audio or video calls. It should always be 1 (video call).
auther: Audio/video permission bitmap. It is not used currently, and should always be 0.
```

**Returned Value**

None

>Note
Only after the SDK has been started successfully can the user join the room. If the room number (relation_id) of the room the user wants to join by calling EnterRoom doesn't exist, a new room is created. The execution result of EnterRoom is sent to the application layer via callback API.

**5. ExitRoom**

Exit the room.

```
ExitRoom();
```

**Returned Value**

None

>Note
The execution result of ExitRoom is sent to the application layer via callback API.

**6. GetEndpointAVMode**

Obtain the audio/video statuses of room members.

```
GetEndpointAVMode(identifier);
```

**Parameter**

identifier: ID of room member.

**Returned Value**

The audio/video statuses of users. 1: Video is available (camera is enabled); 2: Audio is available (microphone is enabled); 3: Both video and audio are available (both camera and microphone are enabled).

**7. SetVideoWinPos**

Set the size and position for the video windows of other members.

```
SetVideoWinPos(identifier, ulPosx, ulPosy, ulWidth, ulHeight)
```

**Parameter**

```
identifier: ID of room member
ulPosX: X coordinate of the video window position
ulPosy: Y coordinate of the video window position
ulWidth: Width of video window
ulHeight: Height of video window
```

**Returned Value**

None

**8. MuteAudio**

Mute or unmute the audio of room members.

```
MuteAudio(identifier, is_mute);
```

**Parameter**

```
identifier: ID of room member.
is_mute: Whether to mute. 1: Yes, 0: No.
```

**Returned Value**

None

**9. RequestViewList**

Request the video views from multiple room members.


```
RequestViewList(identifier_list);
```

**Parameter**

```
Identifier_list: An array of room member IDs.
```

**Returned Value**

None

>Note 
The execution result of RequestViewList is sent to the application layer via callback API.

**10. CancelAllView**

Cancel the video views of all the members

```
CancelAllView();
```

**Parameter**

None

**Returned Value**

None

>Note 
The execution result of CancelAllView is sent to the application layer via callback API.

**11. GetCameraList**

Obtain the camera list.

```
GetCameraList(list);
```

**Parameter**

list: Camera list.

**Returned Value**

If the call is successful, the parameter "list" is the camera list.

**12. GetSelectedCameraId**

Obtain the ID of selected camera.

```
GetSelectedMicId();
```

**Returned Value**

Return the ID of selected camera

**13. SetSelectedCameraIndex**

Set the index for the camera used by the App.

```
SetSelectedCameraIndex(index);
```

**Parameter**

index: Camera index in the camera list returned by GetCameraList.

**Returned Value**

None

**14. OpenCamera**

Enable the camera.


```
OpenCamera();
```

**Returned Value**

None

>Note 
The execution result of OpenCamera is sent to the application layer via callback API.

**15. CloseCamera**

Disable the camera.

```
CloseCamera();
```

**Returned Value**
None

>Note 
The execution result of CloseCamera is sent to the application layer by callback API.

**16. GetMicList**

Obtain the list of microphones installed on the system.


```
GetMicList(list);
```

**Parameter**
list: Microphone list.

**Returned Value**

If the call is successful, the parameter "list" is the microphone list.

**17. SetSelectedMicIndex**

Set the index for the microphone used.

```
SetSelectedMicIndex(index);
```

**Parameter**

index: Microphone index in the microphone list returned by GetMicList.

**Returned Value**

None

**18. GetSelectedMicId**

Obtain the ID of selected microphone.

```
GetSelectedMicId();
```

**Parameter**

None

**Returned Value**

ID of selected microphone

**19. OpenMic**

Enable the microphone.

```
OpenMic();
```

**Returned Value**

None

>Note 
The execution result of OpenMic is sent to the application layer via callback API.

**20. CloseMic**

Disable the microphone.

```
CloseMic();
```

**Returned Value**

None

>Note 
The execution result of CloseMic is sent to the application layer via callback API.

**21. SetMicVolumn**

Set microphone volume.

```
SetMicVolumn(value);
```

**Parameter**

value: Microphone volume, with a value range of 0-100. 0: Minimum volume; 100: Maximum volume.

**Returned Value**

None

**22. GetMicVolumn**

Obtain the microphone volume.

```
GetMicVolumn();
```

**Parameter**

None

**Returned Value**

Return the microphone volume.

**23. GetPlayerList**

Obtain the speaker list.

```
GetPlayerList(list);
```

**Parameter**

list: Speaker list.

**Returned Value**

If the call is successful, the parameter "list" is the speaker list.

**24. SetSelectedPlayerIndex**

Set the index for the speaker used by App.

```
SetSelectedPlayerIndex(index)
```

**Parameter**

index: Speaker index in the speaker list returned by GetPlayerList.

**Returned Value**

None

**25. OpenPlayer**

Enable the speaker.

```
OpenPlayer(void)
```

**Returned Value**
None

**Note**

The execution result of OpenPlayer is sent to the application layer via callback API.

**26. ClosePlayer**

Disable the speaker.

```
ClosePlayer();
```

**Returned Value**

None

> Note 
The execution result of ClosePlayer is sent to the application layer via callback API.

**27. GetPlayerVolumn**

Obtain the speaker volume.

```
GetPlayerVolumn();
```

**Parameter**

None

**Returned Value**

Return the speaker volume.

**28. SetPlayerVolumn**

Set speaker volume.

```
SetPlayerVolumn(value);
```

**Parameter**

value: Speaker volume with a value range of 0-100.

**Returned Value**
None

**29. qavsdk_eventcallback**

js callback function. Function qavsdk_eventcallback must be defined on the HTML page to receive ActiveX callbacks and event notifications.

```
function qavsdk_eventcallback(evt,result,oper,vcnt,vusers)
```

**Parameter**

```
evt: Event type. Please see the definitions below.
result: Result. 0: Success; other values: Failure.
oper: Operation type, which is valid when evt=3155/3156/3158.
vcnt: Number of room members, which is valid when evt=3150.
vusers: List of room members, which is valid when evt=3150.
```

**Event Type:**

```
3144: Login. The notification of execution result of API Login.
3146: Start the SDK. The notification of execution result of StartContext.
3147: Stop the SDK. The notification of execution result of StopContext.
3148: Join the room. The notification of execution result of EnterRoom.
3149: Exit the room. The notification of execution result of ExitRoom.
3150: Notification of change of room members. The list of current room members is returned along with the callback.
3153: Request the video views of multiple members. The notification of execution result of RequestViewList.
3154: Cancel the video views of all the members . The notification of execution result of CancelAllView.
3155: The notification of the result of enabling/disabling the microphone.
      Oper 1: Microphone is enabled; 2: Microphone is disabled.
3156: The notification of the result of enabling/disabling the speaker.
      Oper 1: Speaker is enabled; 2: Speaker is disabled.
3158: The notification of the result of enabling/disabling the camera.
      Oper 1: Camera is enabled; 2: Camera is disabled.
```

      


