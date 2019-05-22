## Audio/Video Room Introduction
  Definition: A room represents an enclosed space. Users can enter this space and participate in audio/video chat with other users who joined the same space. Each audio/video room has a room number (roomID). Members in different rooms do not affect each other. The room class provides a number of methods for room members to acquire room information and member information.

## Join/Exit a Room
### 1. Join a room
To join a room (or create a room if no user exists in the room), follow the four steps below:

- (1) Add room delegation protocol QAVRoomDelegate in .h file on the page of joining room.

- (2) Configure QAVMultiParam to configure parameters such as room number and audio/video scenario policy (for example, VJ scenario), to achieve perfect audio/video effects.

- (3) Join the room according to the configured parameters in .m file on the page of joining room, and set delegate to self.

- (4) The result indicating whether you successfully join the room will be called back to the following method, so you need to implement the method of protocol in .m file.


```
-(void)OnEnterRoomComplete:(int)result;      

```

API Description:

```
-(QAVResult)enterRoom:(QAVRoomParam*)param delegate:(id<QAVRoomDelegate>)dlg;

```
 Sample code:
 

```
    QAVMultiParam *info = [[QAVMultiParam alloc]init];
    info.roomID = 201678;  
    info.authBitMap = QAV_AUTH_BITS_DEFAULT;          //With all the audio/video permissions

    QAVResult temp = [[AVUtil sharedContext] enterRoom:info delegate:self];
```


```
-(void)OnEnterRoomComplete:(int)result
{
    if(result)
    {
        NSLog(@"Joined the room successfully");
    }
}

```

### 2.Exit the room 
The method for exiting a room is the same with that for joining a room. API Description:

```
-(QAVResult)exitRoom;
```

Asynchronous callback indicating whether you have successfully exited the room:


```
-(void)OnExitRoomComplete:(int)result;

```
 Sample code:
 

```
[[AVUtil sharedContext]exitRoom];

```

```
-(void)OnExitRoomComplete:(int)result
{
    if(result)
    {
        NSLog(@"Exited the room successfully");
    }
}
```

## Room Listening Callback 
Apart from callback for joining and exiting rooms, the room delegation protocol QAVRoomDelegate also defines three notification callback APIs:

### 1. Room member status update notification

When users join the room, all member updates (someone joins or exits the room) or video status changes of a certain user (someone enables or disables camera) are all notified to this method via callback (on condition that the room delegation protocol QAVRoomDelegate is used):

API Description:

```
-(void)OnEndpointsUpdateInfo:(QAVUpdateEvent)eventID endpointlist:(NSArray*)endpoints;

```

 Sample code:
 

```

- (void)OnEndpointsUpdateInfo:(QAVUpdateEvent)eventID endpointlist:(NSArray *)endpoints
{
    for(int i = 0; i < [endpoints count];i++)
    {
        //Obtain the information of users in the room
        QAVEndpoint *endpoint = [endpoints objectAtIndex:i];
        NSLog(@"%d %@ whether to enable camera: %@",i,endpoint.identifier,endpoint.isCameraVideo?@"YES":@"No");
    }
}

```
### 2. Notification about illegal opeartion by room member

Different roles in the room have different permissions. For example, during LVB, the VJ should have most permissions such as sending voices and videos. An ordinary viewer should be granted permissions such as accepting instead of sending voices and videos. If a member performs an operation without owning the corresponding permission, the SDK will call back this notification. Permissions for room members are specified by the authBit field and authBuffer field in the configuration parameter EnterRoomParam which is used when joining the room.

API Description:

```
The chatting permission value of the room member recorded at the SDK end currently
-(void)OnPrivilegeDiffNotify:(int)privilege;
```

 Sample code:
 

```
- (void)OnPrivilegeDiffNotify:(int)privilege
{
    NSLog(@"illegal operation!Your privilege is %d",privilege);
}
```
### 3. Notification about list of members who semi-automatically receive room videos

The EnterRoomParam parameter configured for joining rooms includes field for configuring video receiving method. When the receiving method is specified as auto, members will automatically receive existing camera video uplink data when joining a room without the need for application (except data for screen sharing). However, if any new camera video uplink data are generated, members must manually apply for the data and call the requestview() method to acquire such data upon joining a room. The SDK uses the callback API OnSemiAutoRecvCameraVideo() to notify App about the list of members who own uplink data in the room, for the App to perform rendering configuration.

API Description:

```
List of IDs of members corresponding to the camera video data automatically received by @param identifierList
-(void)OnSemiAutoRecvCameraVideo:(NSArray*)identifierList;
```
 Sample code:

```
- (void)OnSemiAutoRecvCameraVideo:(NSArray*)identifyList
{

    if(identifierList != NULL && [identifierList count] > 0)
    {
       for(NSString* identifier in identifierList)
       {
          NSLog(@"%@ has video upload",identifier);
       }
    }
}
```
## Room Members
First, use the room attribute of the QAVContext instance to acquire room and forcibly convert it into QAVMultiRoom, and then use the GetEndPointList method of QAVMultiRoom to acquire all member objects of all rooms.

API Description:

```
-(NSArray*)GetEndpointList; 
```
Sample code:

```
QAVMultiRoom *multiRoom = (QAVMultiRoom *)[AVUtil sharedContext].room;
NSArray *endpointArray = [NSArray arrayWithArray:[multiRoom GetEndpointList]];
//     Work with the user array endpointArray
```

## Member Permissions
Different roles in rooms have different permissions. For example, in during LVB, the VJ should have most permissions such as sending voices and videos. An ordinary viewer should be granted permissions such as accepting voices and videos, but not sending them.

All permissions are defined in QAVCommon.h:

```
QAV_AUTH_BITS_DEFAULT          // Default values. With all permissions.
QAV_AUTH_BITS_OPEN             // Enable all permissions.
QAV_AUTH_BITS_CLOSE            // Disable all permissions.
QAV_AUTH_BITS_CREATE_ROOM      // Permission for creating room.
QAV_AUTH_BITS_JOIN_ROOM        // Permission for joining room.
QAV_AUTH_BITS_SEND_AUDIO       // Permission for sending voices.
QAV_AUTH_BITS_RECV_AUDIO       // Permission for receiving voices.
QAV_AUTH_BITS_SEND_VIDEO       // Permission for sending videos.
QAV_AUTH_BITS_RECV_VIDEO       // Permission for receiving videos.
QAV_AUTH_BITS_SEND_SUB         // Permission for sending side-channel videos.
QAV_AUTH_BITS_RECV_SUB         // Permission for receiving side-channel videos.
```

To modify an individual's permissions, follow the steps below:

1. Add permission changing protocol QAVChangeDelegate in corresponding ViewController.h file.

2. By calling the API for changing personal permissions, specify the first parameter with new permission, and leave the second parameter empty. The result will be returned using callback function. API declaration is as follows:

```
-(QAVResult)ChangeAuthoritybyBit:(uint64)auth_Bit orstring:(NSData *)buff delegate:(id<QAVChangeDelegate>)dlg;
```
 The sample code is as follows:

```
//Grant permissions for creating room and joining room
authBitMap = QAV_AUTH_BITS_CREATE_ROOM | QAV_AUTH_BITS_JOIN_ROOM;   
QAVMultiRoom*multiRoom = (QAVMultiRoom*)[AVUtil sharedContext].room;
[multiRoom ChangeAuthoritybyBit: authBitMap orstring:nil delegate:self];
```
3. The result indicating whether the permission is modified successfully will be called back to the following method, so you need to implement the method of protocol in corresponding ViewController.m file.

```
-(void)OnChangeAuthority:(int)ret{
    if (ret == QAV_OK)
{
      //Permission modified successfully
}
}

```
