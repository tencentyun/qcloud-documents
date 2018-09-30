This document describes how a viewer enters a room and enables the camera and the microphone to interact with other users.

## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_join.zip)
## Entering a Room
The method for entering a room is in ILiveRoomManager.h, and is the same as that for creating a room. This method also requires passing in two parameters, room ID (roomId) and room configuration object (option) (the roomId of the room to be entered must be the same as the created roomId). When creating a configuration object, we should disable the auto start of the camera and the microphone.

```objc
- (IBAction)onJoinRoom:(id)sender {
    // 1. Create a live room page
    LiveRoomViewController *liveRoomVC = [[LiveRoomViewController alloc] init];
    
    // 2. Create a room configuration object
    ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
    // Configure a room ticket
    option.privateMapKey = privateMapKey;
    option.imOption.imSupport = NO;
    // Do not enable the camera automatically
    option.avOption.autoCamera = NO;
    // Do not enable the microphone automatically
    option.avOption.autoMic = NO;
    // Set audio/video listening in the room
    option.memberStatusListener = liveRoomVC;
    // Set room disconnection event listening
    option.roomDisconnectListener = liveRoomVC;
    
    // This parameter indicates the audio/video specification used after a user enters a room. The value of the parameter is the role name configured by the customer in Screen Setting on the Tencent Cloud TRTC console (for example, the default role name is user, and you can set controlRole = @"user")
    option.controlRole = #The role name configured on the Tencent Cloud console#;
    
    // 3. Call the API for creating a room with roomId and option passed
    [[ILiveRoomManager getInstance] joinRoom:[self.roomIDTF.text intValue] option:option succ:^{
        // Entered the room successfully. The user will be redirected to the room page
        [self.navigationController pushViewController:liveRoomVC animated:YES];animated:YES];
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        // Failed to enter the room
        NSLog(@"Failed to enter the room errId:%d errMsg:%@",errId, errMsg);
    }];
}
```
After successfully entering a room, the user will be directly redirected to the room page.

## Video Interaction
To start video interactions with other users in the room, enable the camera and the microphone:

```objc
/**
 Enable/disable the camera

 @param cameraPos Camera position cameraPos
 @param bEnable   YES: Enable NO: Disable
 @param succ      Callback is successful
 @param fail      Callback failed
 */
- (void)enableCamera:(cameraPos)cameraPos enable:(BOOL)bEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;

/**
 Enable/disable the microphone

 @param bEnable YES: Enable NO: Disable
 @param succ      Callback is successful
 @param fail      Callback failed
 */
- (void)enableMic:(BOOL)bEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;
```
After triggering an action, call the corresponding API.

## Audio/Video Event Listening
The audio/video event callback method handles events involving multiple users, mainly the camera enabling/disabling events.

> If QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO is detected, which indicates that a user enables the camera, add the rendered view of the user.
If QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO is detected, which indicates that a user disables the camera, remove the rendered view of the user.

The frame of a rendered view is not fixed and needs to be calculated according to the current number of rendered views and product demands. In the Demo provided in this document, we demonstrate a simple top-down equal-division layout for rendered views. You can also define your own layout logic according to your needs.

```objc
// Audio/video event callback
- (BOOL)onEndpointsUpdateInfo:(QAVUpdateEvent)event updateList:(NSArray *)endpoints {
    if (endpoints.count <= 0) {
        return NO;
    }
    for (QAVEndpoint *endpoint in endpoints) {
        switch (event) {
            case QAV_EVENT_ID_ENDPOINT_HAS_CAMERA_VIDEO:
            {
                /*
                 Create and add rendering views, pass userID and rendering image type. QAVVIDEO_SRC_TYPE_CAMERA (camera image) is entered here.
                 */
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher addRenderAt:CGRectZero foruserId:endpoint.userId srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [self.view addSubview:renderView];
                [self.view sendSubviewToBack:renderView];
                // The number of users enabling the camera in the room changes and the rendered views are laid out again
                [self onCameraNumChange];
            }
                break;
            case QAV_EVENT_ID_ENDPOINT_NO_CAMERA_VIDEO:
            {
                // Remove a rendered view
                ILiveFrameDispatcher *frameDispatcher = [[ILiveRoomManager getInstance] getFrameDispatcher];
                ILiveRenderView *renderView = [frameDispatcher removeRenderViewFor:endpoint.userId srcType:QAVVIDEO_SRC_TYPE_CAMERA];
                [renderView removeFromSuperview];
                 // The number of users enabling the camera in the room changes and the rendered views are laid out again
                 [self onCameraNumChange];
            }
                break;
            default:
                break;
        }
    }
    return YES;
}
```

```objc
// This is called when the number of users enabling the camera in the room changes to re-layout all the rendered views. Here we simply arrange the rendered views equally from top to bottom.
- (void)onCameraNumChange {
    // Obtain all rendered views
    NSArray *allRenderViews = [[TILLiveManager getInstance] getAllAVRenderViews];
    
    // Detect exceptions
    if (allRenderViews.count == 0) {
        return;
    }
    
    // Calculate and set the frame for each rendered view
    CGFloat renderViewHeight = [UIScreen mainScreen].bounds.size.height / allRenderViews.count;
    CGFloat renderViewWidth = [UIScreen mainScreen].bounds.size.width;
    __block CGFloat renderViewY = 0.f;
    CGFloat renderViewX = 0.f;
    
    [allRenderViews enumerateObjectsUsingBlock:^(ILiveRenderView *renderView, NSUInteger idx, BOOL * _Nonnull stop) {
        renderViewY = renderViewY + renderViewHeight * idx;
        CGRect frame = CGRectMake(renderViewX, renderViewY, renderViewWidth, renderViewHeight);
        renderView.frame = frame;
    }];
}
```
> Note:
> 1. When adding rendered views, you don't need to worry about duplication. The SDK only allows adding one rendered view of the same type of video source for the same user.
> 2. The SDK only allows a maximum of 10 rendered views in it.

## FAQ
#### Failed to enter a room, and was prompted for required permission
Make sure that the room ticket field (privateMapKey) is configured correctly.
> The privateMapKey field is required for new users, and existing users (do not need room tickets) need to configure [[ILiveSDK getInstance] setChannelMode:E_ChannelIMRestAPI withHost:@""]; at initialization
```
[[ILiveSDK getInstance] setChannelMode:E_ChannelIMSDK withHost:@""];
```

Failed to change the role. Error code is -1.
> This means that the configuration backend cannot find the role to be changed to. Check whether the role name is entered correctly (case-sensitive).


## Email
If you have any questions, send us an email to trtcfb@qq.com.

