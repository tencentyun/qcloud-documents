
### Suggested steps for troubleshooting
- Identify the error code to troubleshoot the issue
- Check if the current browser supports this feature

### How can I determine if the current browser supports WebRTC
Use WebRTCAPI.fn.detectRTC to check if WebRTC is supported. If false is returned, the business end will provide an error message page to guide you to use the supported environment. In special cases, you can seek help by creating a ticket.

### Howling (feedback)
Note that we have set a muted attribute to the local video/audio, which means to mute the local video stream when it is played. Otherwise, there will be a loop where the sound of the local video stream is once again used as an audio input source, causing a problem of "howling" or "feedback".
```
<video muted autoplay playsinline></video>
　　　
 <audio muted autoplay playsinline></audio>
```

### It takes a long time to hear the audio
In an audio-only scenario, be sure to use the audio instead of the video tag to load the audio stream.

### on set remote sdp failed (as shown below)
![](https://main.qcloudimg.com/raw/0edefde27bea9f4a44b4a6d0c273c315.png)
There is a parameter closeLocalMedia in the webrtcapi instantiation method.
It indicates whether the auto push is disabled. If it is set to false (the default value), but startWebRTC is called, this problem will occur.

### Power consumption of your mobile phone
Videos need to be encoded/decoded, which is quite power-consuming. However, no push/playback on the page still consumes a lot of power. You must check if the video's srcObject is not reset during the callback for non-push.

`videoElement.srcObject = null`

### SecurityError [Security error]
The audio/video cannot be obtained correctly.
WebRTC must be enabled in the page of HTTPS or localhost, otherwise the audio/video device cannot be obtained.

### NotAllowedError [Rejection error]
The user rejected the request to obtain the audio/video device

### OverConstrainedError [Error: The device does not meet the requirements]
The specified requirements cannot be met by the device. This exception is an object of OverconstrainedError type and has a constraint attribute that contains constraint pairs that cannot be satisfied. If multiple tabs are enabled for push at a time, make sure the resolution to be collected is consistent.

### NotFoundError [Error: Not found]
The media type that meets the request parameter was not found.

### NotReadableError [Error: Unable to read]
Even if the user has been authorized to use an appropriate device, it cannot be accessed due to a hardware, browser or web page error on the operating system.

### AbortError [Termination error]
Even if both the user and the operating system have been granted the access to the device hardware and no problem such as NotReadableErro caused by hardware occurs, the device still cannot be used due to some problems.

### TypeError [Type error]
The constraints objects are not set or set to false.

### No sound
The browser uses the default sound output device. In this case, adjust the sound output device and disable other devices than the amplifier to determine if it works.

### Unable to make a video call in the Electron development environment
If you are using Electron and are unable to make a video call after submitting it to the Mac App Store, please add com.apple.securite.network.server to the entitlements.plist file.

### Be careful with the black screen caused by dom tree redrawing
If you are using react/vue/angular, pay special attention to the relationship between video and stream, which is controlled by JS. If data changes cause page changes, you need to rebind video with stream, otherwise a black screen will occur.

### Black screen on iOS
If you are using react/vue/angular, note that a video created dynamically is not automatically played in a browser.
In the viewer mode (non-push), iOS does not allow auto playback of videos with sound and remote video streams cannot be played automatically. You need to bind the remote streams to the video tag and add video.play() in the onRemoteStreamUpdate event handling function.

