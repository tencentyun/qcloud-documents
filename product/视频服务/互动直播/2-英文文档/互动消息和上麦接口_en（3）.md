# Interactive Message and Joining Broadcasting

## Preparations
Whether you want to send messages or join the broadcasting, you need to set event and message listening before creating and joining a room. Example:
```
//Add IM message listening
//The listening object added with addMessageListener must call removeMessageListener when the object is terminated, or it will add multiple message listening objects, resulting in the receipt of multiple messages.
[[[ILiveSDK getInstance] getTIMManager] addMessageListener:self];
```

## Send a message

| API | Description |
|---|---|
| sendC2CMessage:message:succ:fail: | Send C2C messages |
| sendOnlineC2CMessage: succ: failed: | Send C2C online messages |
| sendGroupMessage: succ: failed: | Send group messages |
| sendOnlineGroupMessage: succ: failed: | Send group online messages |

**Differences between ordinary messages and online messages:**

1. When sending ordinary messages, the receiver will certainly receive them (If the receiver is not online, he/she will receive them again at the next login).

2. When sending online messages, if the receiver is online, he/she will receive the messages; if not online, he/she will not receive them, even at the next login.

The calling methods of above APIs are similar. The sample codes for sending "group online messages" are shown as follows:

```
//1. Send a message
TIMTextElem *elem = [[TIMTextElem alloc] init];
elem.text = @"msg text";

TIMMessage *msg = [[TIMMessage alloc] init];
[msg addElem:elem];

__weak typeof(self) ws = self;
[[ILiveRoomManager getInstance] sendOnlineGroupMessage:msg succ:^{
    NSLog(@"send msg  succ");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"send msg fail.M=%@,errId=%d,errMsg=%@",module,errId,errMsg);
}];
```

```
// 2. Receive a message (All IM messages are called back in onNewMessage:)
- (void)onNewMessage:(NSArray *)msgs
{
    //If addMessageListener has not added the listening object, then you will not receive the onNewMessage callback
    NSLog (@"Receive messages, and resolve the messages here. For detailed resolution steps, please see the demo program");
}
```

## Join broadcasting
### Flowchart of invitation from VJ to viewer for joint broadcasting
![](http://mc.qcloudimg.com/static/img/ccbafe376da2e175ff41bd681856581e/image.png)

### Flowchart of viewer's request for joining the broadcasting
![](http://mc.qcloudimg.com/static/img/4d21a6ce428740fa16ebc58a0675b3e7/image.png)


### APIs

>**Note: **
>The control signaling is implemented by sending custom messages.

#### Invite to join broadcasting

```
//Message assembly
NSString *dataStr = @"";
NSError *error;
//The data of custom messages is a set of key-value pairs. In demo, kMsgCmdKey is taken as the key of command field, and kMsgDataKey is taken as the key of other parameters
//The command field is defined by the user, which must be unified in the used app
NSDictionary *sendDic = [NSDictionary dictionaryWithObjectsAndKeys:@(AVIMCMD_Multi_Host_Invite), kMsgCmdKey, dataStr, kMsgDataKey,nil];
NSData *sendData = [NSJSONSerialization dataWithJSONObject:sendDic options:NSJSONWritingPrettyPrinted error:&error];
if(error != nil){
    NSLog(@"serialization msg fail");
    return;
}
TIMCustomElem *imCustomElem = [[TIMCustomElem alloc] init];
[imCustomElem setData:sendData];
TIMMessage *imMessage = [[TIMMessage alloc] init];
[imMessage addElem:imCustomElem];
__weak typeof(self) ws = self;

[[ILiveRoomManager getInstance] sendOnlineC2CMessage:recvId message:imMessage succ:^{
    NSLog(@"Sent the joint broadcasting invitation message successfully");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"Failed to send the joint broadcasting invitation, M=%@,code=%d,Msg=%@",module,errId,errMsg);
}];
```
#### API for joining broadcasting

```
- (void)onNewMessage:(NSArray *)msgs
{
    //Receive the message, resolve it, and determine whether it is a joining broadcasting invitation message. If yes, perform the joining broadcasting operation, see demo for the detailed resolution method
    ...
    //Joining broadcasting steps: Modify the role -> Enable the camera -> Enable the Mic
    __weak typeof(self) ws = self;
    ILiveRoomManager *manager = [ILiveRoomManager getInstance];
    //kSxbRole_InteractHD is the role name of demo, developers need to change it to the role name configured in the console by their appids
    [manager changeRole:kSxbRole_InteractHD succ:^ {
        NSLog(@"Join broadcasting: Changed the role successfully");
        [manager enableCamera:CameraPosFront enable:YES succ:^{
            NSLog(@"Join broadcasting: Enabled the camera successfully");
            [manager enableMic:YES succ:^{
                NSLog(@"Join broadcasting: Enabled the microphone successfully");
                NSLog(@"Join broadcasting: Joined the broadcasting successfully");
            } failed:^(NSString *module, int errId, NSString *errMsg) {
                NSLog(@"Join broadcasting: Failed to enable the microphone, M=%@,code=%d,Msg=%@",module,errId,errMsg);
            }];
         } failed:^(NSString *module, int errId, NSString *errMsg) {
             NSLog(@"Join broadcasting: Failed to enable the camera, M=%@,code=%d,Msg=%@",module,errId,errMsg);
         }];
    } failed:^(NSString *module, int errId, NSString *errMsg) {
       NSLog(@"Join broadcasting: Failed to change the role, M=%@,code=%d,Msg=%@",module,errId,errMsg);
    }];
}
```
#### API for setting the area for rendering for joining broadcasting

| API | Description |
|---|---|
| addRenderAt:forIdentifier:srcType: | Add the area for rendering and set the key for the rendered view (generally, the user ID for the rendered view is used). |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| CGRect | rect | View rendering area. |
| NSString | forIdentifier | View key, which is used as business logic (generally, the user ID for the view is used). |
| avVideoSrcType | srcType | Video source type. |

```
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints
{
    TILLiveManager *manager = [TILLiveManager getInstance];
    switch (event) 
    {
        case ILVLIVE_AVEVENT_CAMERA_ON:
        {
           for (NSString *user in users) 
            {
                //user: The user id corresponding to the event
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderViewForMac *view = [frameDispatcher addRenderAt:NSMakeRect(0, 0, 640, 480) forIdentifier:user    srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [self.window.contentView addSubview:view];
            }	
        }
        break;
    }
    return YES;
}
```
If the above steps are correctly performed, the VJ can successfully invite the viewer to the broadcasting. When the viewer joins the broadcasting, multi-stream views appear in the room to show the interactions between VJ and viewers.

