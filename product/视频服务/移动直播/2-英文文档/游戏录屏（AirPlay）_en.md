## About AirPlay

AirPlay is a wireless technology developed by Apple Inc. that allows you to stream the screen content (including the system UI) from iPhone to other devices as the AirPlay mirror.

AirPlay's advantage over [ReplayKit](https://cloud.tencent.com/document/product/454/7883) is that it does not need the support from the target App since it can obtain the current screen content in any case, whether it is a game or system interface.

Such a powerful feature inevitably comes with Apple Inc.'s restriction on its use. An App adopting this solution may not be approved by AppStore. In case of a failure to get your APP listed in the AppStore, you can consider issuing an IPA installation package by using a signed enterprise certificate.

## Version Requirement
iOS **9.0** or above
	
## Notes

| Package Name    | Function   | Description | Download |
|--------|-------|---------|---------|
| TXAirPlayService.framework | Airplay core module | / | Download is currently unavailable |
| CocoaAsyncSocket.framework ( >= 1.0)  | Third-party open source library |[Visit Github](https://github.com/robbiehanson/CocoaAsyncSocket) | [Click to download](https://mc.qcloudimg.com/static/archive/b286354677e2b74cef7cc6d7fbb75b88/CocoaAsyncSocket-master.zip) |
| TXRTMPSDK.framework ( >= 1.8.1)  | RTMP SDK | [View the document](https://cloud.tencent.com/document/product/454/7873) |[Check the download link](https://cloud.tencent.com/document/product/454/7873#.E4.B8.8B.E8.BD.BD.E5.9C.B0.E5.9D.806)|

Due to company's requirement for product exclusive usage, TXAirPlayService SDK is currently unavailable for download this month. We'll make it available as soon as possible.

## Access Procedure
### 1. Configure Parameters
LAAirPlayManager is AirPlay's management class and can be used without configuration.

LAAirPlayManager is used to set AirPlay's resolution, service name (the name displayed on AirPlay menu), TXLivePushConfig, etc. Typical configuration code is as follows: 

```objective-c
TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
// TODO: set fps bitrate
[LAAirPlayManager manager].config = config;
[LAAirPlayManager manager].qualityWidth = 720;
[LAAirPlayManager manager].qualityHeight = 1280;
```
You can specify FPS, bitrate, landscape and other parameters in TXLivePushConfig; if you want to modify these default settings based on your experiences, please see [Advanced Operations](https://cloud.tencent.com/document/product/454/7884).

### 2. Start Screencap
```
[LAAirPlayManager manager].rtmpUrl = @"rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
[[LAAirPlayManager manager] runServer];
```

After starting AirPlay, wait for user connection. During the connection, SDK will throw notifications and modify the `airplayConState` status. App can listen to these notifications to adjust UI display: 

| Status | Description | 
|---------|---------|
| LAAirPlayServerPublished | AirPlay service has been enabled. You can choose this device in system's AirPlay interface | 
| LAAirPlayServerConnected | AirPlay service is already connected, and screencap has begun | 
| LAAirPlayServerConnectFailed | If you have selected AirPlay service but failed to connect to it within 30 seconds, you will receive this notification | 

It takes approximately **2-5** seconds from the time AirPlay is enabled until it is connected successfully. After successful connection, a blue bar will appear on your mobile phone's status bar, which means the screen content has been mirrored by AirPlay.

### 3. Event Handling

Listen to RTMP SDK push events just by calling `-[LAirPlayManager setDelegate:]` to set up a callback. For the list of push events, please see [RTMP Push-Event Handling](https://cloud.tencent.com/document/product/454/7879#.E4.BA.8B.E4.BB.B6.E5.A4.84.E7.90.86)

### 4. Finish Screencap
```
[[LAAirPlayManager manager] stopServer];
```

## FAQs

### 1. Get listed in AppStore

AirPlay is Apple's proprietary protocol. If your request is rejected by AppStore, any attempt to distribute your App on the AppStore can put you at a risk. SDK doesn't contain any proprietary API. You can use it without any worry.

### 2. I haven't receive any notification about successful connection since enabling the service

Please check for any network exception, or suggest user selecting AirPlay device manually. Auto-connection may change with the system update. Please refer to the latest Mini LVB code.

### 3. Bitrate selection

Screencap features a larger image instability than camera. With the same resolution and frame rate, Screencap needs a higher bitrate to achieve the same definition as camera. For more information about bitrate selection, please see [How to get a good image quality](https://cloud.tencent.com/document/product/454/7955).

### 4. Frame rate decreases during LVB

SDK screencap mostly runs at the background. iOS can limit the CPU utilization for running App at the background to ensure the smoothness of App at the frontground.

If a large game is running on a low-configuration phone, the smoothness of push may be affected. You can listen to the NET_STATUS_CODEC_CACHE value of status callback of `[TXLivePushDelegate onNetStatus:]`. The ideal CACHE value is 0, and if it's greater than 100, it's necessary to suggest the user returning to the App temporarily and resume the game after the Cache value decreases.

