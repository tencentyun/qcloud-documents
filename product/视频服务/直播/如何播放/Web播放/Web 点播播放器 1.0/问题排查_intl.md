### Error Codes

The table contains error codes that may occur when using the SDK. In case of any error code that is not listed in this table, contact customer service. Our engineers can help you solve the problem.

| Code  | Description |
|-------|---------------------|
| 1003  | Incorrect password |
| 10000 | Request timeout (timeout when pulling player configuration and video information. Check your network and try again. Timeout is 10 seconds) |
| 10001 | Failed to parse data (Failed to parse the data obtained by pulling player configuration and video information. It may be caused by a network problem or server exception) |
| 10002 | Connection timeout. Try again later | (Failed to pull player configuration and video information. It may be caused by a network problem or server exception) |
| 10008 | Incorrect APPID or File ID |
| 11044 | APPID missing |
| 11045 | File ID missing |
| 11046 | Password missing |


### FAQs

* **Why is the screen distortedly stretched when the video is played in H5?**
Video stretching is not supported when playing video in H5. Check if the player container has right width/height configuration.

* **My QQ browser is downloading the video. How to stop it?**
JS cannot intervene such actions due to the restrictions of the QQ mobile browser kernel. Similarly, the kernels of some browsers, such as UC, also provide auto video detection/download feature. Contact your browser developer to disable this feature.

* **The video cannot be hidden on the QQ browser.**
QQ browser takes over the video playback feature from H5, and the X5 kernel uses self-developed player to play videos. QQ browsers use a unified playback interface to ensure a good user experience. For more information, please see [QQ Browser Documentation](https://x5.tencent.com/tbs/guide.html).
		
* **I didn't get the correct status information when calling relevant methods such as isPlaying().**
In some mobile browsers and webviews, video playback will be taken over by the browser's kernel, which means the SDK will not be able to acquire the correct playback status.

* **Video cannot be automatically played on mobile device after auto playback is set.**
Most mobile browsers cannot automatically load media files due to reasons like data traffic. Users need to trigger this action manually when playing videos.
	
* **Video is automatically played in full screen mode on iOS.**
By default, video is played in full screen mode on iOS system due to the webkit setting. To achieve inline playback within an App, you can set the webkit-playsinline attribute. Any Safari browser on iOS below 10 is unable to disable the automatic use of full screen mode.

* **Why does the Flash player have two play buttons in Chrome on PC?**
Flash is no longer automatically played starting from Chrome 42. Chrome only plays major Flash contents automatically, while other Flash contents are paused, unless users enable them manually.

