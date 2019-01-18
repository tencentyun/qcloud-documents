### Which browsers are supported by TcPlayer?
TcPlayer has been tested on and supports the following browsers: PC: IE 10+, Edge, Chrome, Firefox, QQ Browser, MAC Safari. Mobile: Android 4.4+, iOS 8.0+, WeChat, Mobile QQ, QQ Browser, Chrome, Safari.
To support IE 8 and IE 9, you must introduce the Polyfill script before introducing the player script, as shown below:
```
    <!--[if lt IE 9]>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-shim.js" charset="utf-8"></script>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-sham.js" charset="utf-8"></script>
    <![endif]-->
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.1.js" charset="utf-8"></script>;
```
		
### On mobile devices, the video does not go into full screen when TcPlayer is switched to full screen mode, and browser interface is still displayed. Why is that?
First, you should know that the full screen solution provided by TcPlayer is to use Fullscreen API + pseudo-full screen. If the browser supports Fullscreen API, the video container will fill up the entire screen when the player goes into full screen mode, and the control bar is provided by TcPlayer, as shown in the figure:
![](//mc.qcloudimg.com/static/img/df40b2b49390f8fc314fd040ba026156/image.png)
(Android Chrome)

If the browser does not support Fullscreen API, then pseudo-full screen mode will be used, as shown in the figure:
![](//mc.qcloudimg.com/static/img/d5746d9bef48b411c3bac576fe6925b1/image.png)![](//mc.qcloudimg.com/static/img/1e20288d6f69a5cf7a886f95edd40ec3/image.png)
(Left: WeChat on Android. Right: WeChat on iOS)
The control bars displayed in these two full screen modes are all provided by TcPlayer, and you enter these modes by tapping on the full screen button on the control bar or by using the method provided by TcPlayer. However, the control bar provided by TcPlayer may not always be displayed on mobile devices, as their webview hijacks the video playback in most situations and uses the control bar provided by webview. In this case, the TcPlayer control bar will not be displayed, and you cannot use the full screen solution provided by TcPlayer, as shown in the figure:
![](//mc.qcloudimg.com/static/img/d027ca6fce35059e05428128b9823d70/image.png)![](//mc.qcloudimg.com/static/img/b28d69f15a60321d1a6e2b3a93b53038/image.png)
(Left: WeChat on Android, where video playback is hijacked by TBS. Right: iOS, where video playback is hijacked by QQ Browser)
Upon entering full screen mode:
 ![](//mc.qcloudimg.com/static/img/0ab29e27c7aa89587cec96d7530ab4f7/image.png)![](//mc.qcloudimg.com/static/img/a260a96ed73d2a4d7d0260c4584a128a/image.png)
(Left: WeChat on Android. Right: QQ Browser on iOS)
As you can see, the control bar is different from the TcPlayer one. No APIs are provided for JS in this full screen mode, so TcPlayer cannot realize this mode. We usually refer to the full screen mode where the video covers the whole screen as System Full Screen, and the mode where the video covers the whole browser page area as Pseudo-Full Screen. Therefore, if you can see the browser interface after going into full screen mode, then it is pseudo-full screen. You can only use the control bar provided by the system if you want to go into system full screen mode on mobile devices. You may choose the control bar type by using the "controls" attribute of TcPlayer.

### Why is the screen stretched when the video is played in H5?
Video stretching is not supported when playing video in H5. Check if the player container width/height configuration is correct.

### Why can't I cover my own div on top of the video?
Different browsers implement the `<video>` tag in different ways. For example, if you open a web page in QQ or WeChat (on Android system), then it's very likely that X5 browser kernel is used (the kernel which is bound with QQ or WeChat, i.e. the QQ Browser kernel). For certain reasons, the QQ Browser team implemented such a solution that "the video `<video>` must be placed in the top layer" (for more information, please see [QQ Browser Documentation](http://x5.tencent.com/guide?id=2009)). However, with recent coordination among teams within the company, the QQ Browser Team is gradually changing this policy. This issue may have already been solved in the latest X5 browser kernel as you read this document.

### Why is the configured cover image not working?
This is the same problem with the previous one ("cannot cover div on top of the video"). The cover image cannot be displayed as long as the browser does not allow elements to cover up the `<video>` tag.

### Why is video displayed in full screen mode by default in certain mobile browsers?
If the video is played through inline playback inside the application (that is, your own application encapsulates an iOS webview control which is used to display web pages. In this mode, you can customize the details of webview, which may have different performance from standard Safari browser), you can configure the "webkit-playsinline" attribute for the `<video>` tag in HTML (or configure the "playsinline" attribute if you're using iOS 10), and then configure "allowsInlineMediaPlayback" for webview. In this way, videos are played in non-full screen mode (inline playback) when you open pages in the application.
If you open the page in Safari on iOS 10, you can realize non-full screen playback (inline playback) by using the method above (configure "playsinline" attribute for the `<video>` tag). You cannot disable auto full screen playback for Safari on systems below iOS 10. This attribute is already added for our browser. It only needs to be supported by the devices.
For Android devices, it is known that there are many different customized versions for Android systems, and each system realizes the `<video>` tag in a different way, without a universal standard. For this reason, video playback capabilities on Android have much lower consistency compared to iOS. The "webkit-playsinline playsinline" attribute is already added for the player according to current universal method. It only needs to be supported by the devices.

### Why can't I realize auto video playback in mobile browsers?
There are only two ways to realize auto video playback on mobile web: by configuring the "autoplay" attribute for the `<video>` tag, or by calling the "play()" method provided by the `<video>` tag. However, auto video playback has always been prohibited on mobile web, thus the universal method now is to trigger video playback by users actions. For example, monitor ontap events of users and call the "play()" method. It is possible that certain customized webviews support the "autoplay" attribute of the `<video>` tag, or can realize auto video playback by calling other special functions. Videos can be played automatically when you open the pages in these webviews. Our player will add the "autoplay" attribute for the `<video>` tag if "autoplay" is configured as "true". Now we only need the devices to support this attribute.

### Why does the Flash player have two play buttons in Chrome on PC?
Flash is no longer be automatically played starting from Chrome 42 (Google has purchased WebRTC and made it open-source for a reason). Chrome only plays major Flash contents automatically, while other Flash contents are paused, unless users enable them manually.

### Why can the LVB video be played in browsers on PC but cannot on mobile devices?
Only hls (m3u8) protocol is supported for playing LVB videos in mobile browsers. Thus, you need to confirm whether the LVB stream pulling addresses contain URL for pulling hls (m3u8) stream. The video cannot be played on mobile phones if you only provide an flv or rtmp address for our player.

