## Handling LVB Interruptions
An LVB could be interrupted by many events. Following are some common interruptive events and their handling methods for developers' reference:
>* Incoming call
>* Audio interruption
>* Switching to background
>* Locking screen
>* Network interruption
>* Crash
>* Being kicked

### 1. Incoming Call
No special action is needed.

When there is an incoming call, the ringing interface would cover the current LVB interface. Refer to the handling of being switched to background.

### 2. Audio Interruption
No special action is needed.

When there is an audio interruption (such as an alarm), there may be two cases:

>* No new interface appears. The current video and audio playback (recording) is not influenced.
>* There is a new interface appearing. Refer to the handling of being switched to background.

### 3. Switching to Background
#### Android
iLiveSDK provides three modes for users to handle the App's being switched to background.

Mode | Description
:--|:--:
VIDEOMODE_BSUPPORT | Background support mode. The App would continue video and audio playback (recording) after being switched to background.
VIDEOMODE_NORMAL | Normal mode (*default*). The App would pause video and audio playback (recording) after being switched to background, and resume after it's in foreground again.
VIDEOMODE_BMUTE | Background mute mode. The App would stop transmitting all upstream and downstream video and audio data after being switched to background, and resume after it's in foreground again.

#### iOS
There may be two cases for iOS:
>* Interface is covered. In this case, the App would pause video and audio playback (recording), and resume after it's in the front again.
>* Being switched to background. The App would only pause for a short interruption (as described above), but could be reclaimed after a long interruption (system mechanism).

*PS: In a live room, if no upstream data is received in 90s, the room would be reclaimed by the backend.*

### 4. Locking Screen
#### Android
Similar to background switching. Users can set the FLAG_KEEP_SCREEN_ON flag in the application to prevent automatic lock screen.
#### iOS
iLiveSDK keeps the application alive internally and prevents automatic lock screen. (This is enabled after users join the room and disabled after users exit the room.)

### 5. Network Interruption
When the network is interrupted, the SDK would retry connection internally. Users can monitor the system's network status themselves.

To monitor the internal network status of the SDK, refer to [iLiveQualityData](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos/blob/master/doc/ILiveSDK/quality.md).

If a room doesn't generate any upstream data in 90s, the room would be reclaimed and an onRoomDisconnect event is fired.

### 6. App Crash
iLiveSDK embeds [bugly Report](https://bugly.qq.com/v2/) to help users pinpoint bugs quickly.

Users only need to record the current live room (roomid) and its LVB status to return to the room after the App restarts to resume LVB. If the interruption is short (*less than 90 seconds*), the viewers would only experience lag and stutter. (*when this happens, you can prompt the users based on related events*)

Users can listen for camera disabling events in onEndpointsUpdateInfo and prompt accordingly.


### 7. Being Kicked
When a user is logged in on multiply clients, a kick event would be fired. In this case, it's recommended to ask the user to re-login. (Users have to restore their status on their own to resume.)

#### Android
You can call setUserStatusListener method of ILiveLoginManager class to listen for forced offline events.

```java
public interface TILVBStatusListener {
    void onForceOffline(int error, String message);
}
```

#### iOS

#### 1. Set User Status Listener
```
//Set user status listener
[[ILiveSDK getInstance] setUserStatusListener:[[LiveUserStatusListener alloc] init]];
```

```
//User status listener class
@interface LiveUserStatusListener : NSObject <TIMUserStatusListener>
@end

@implementation LiveUserStatusListener
//Being kicked
- (void)onForceOffline{
}
//Session expiration
- (void)onUserSigExpired{
}
```
##### 2. Handle Application Logics in Callbacks
```
- (void)onForceOffline{
    //Forced offline (you can use the following logics as a reference. Customize your logics based on your applications.)
    //1. If not in a live room, redirect to login interface.
    //2. If in a live room
    //(1) Store LVB status, such as room ID and title, then exit the room.
    //(2) After re-login, restore the room based on the recorded status and resume.
}
```
