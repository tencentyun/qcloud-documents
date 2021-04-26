### Why do &lt;live-pusher&gt; and &lt;live-player&gt; not work?
For policy and compliance considerations, &lt;live-pusher&gt; and &lt;live-player&gt; are not supported by all WeChat mini programs:

- Mini Programs of personal and enterprise accounts only support the categories in the following table:
- For Mini Programs meeting requirements of categories, you need to enable the component permissions in <font color='red'>"Settings" -> "API Settings"</font> of the Mini Program management backend.

<table>
  <tr align="center">
    <th width="200px">Primary Category</th>
    <th width="700px">Sub-category</th>
  </tr>
  <tr align="center">
    <td>"Social"</td>
		<td>LVB</td>
  </tr>
	<tr align="center">
    <td>"Education"</td>
		<td>Online education</td>
  </tr>
	<tr align="center">
    <td>"Healthcare"</td>
		<td>Internet hospital and public hospital</td>
  </tr>
	<tr align="center">
    <td>"Government Affairs and Livelihood"</td>
		<td>All secondary categories</td>
  </tr>
	<tr align="center">
    <td>"Finance"</td>
		<td>Funds, trusts, insurance, banking, securities/futures, micro-credit of non-financial institutions, credit investigation, and consumer finance</td>
  </tr>
</table>

Note: If your Mini Program still does not work after the settings are correctly made, that may be because the cache within the WeChat is not updated. Delete the mini program, restart WeChat, and try again.

### How do I choose the right resolution ratio?
The resolution ratio is set by aspect. Available resolution ratios include 3:4 and 9:16, which are set according to the display area ratio of the current push and the playback view on the mobile phone. The mobile phone screen is usually in a resolution ratio of 9:16 when it is in portrait screen mode. If a person pushes through the full screen, 9:16 is set. If two persons are displayed side by side, one for push and the other for playback, and the display area is in a resolution ratio of 3:4, and then 3:4 is set.

### How do I choose from SD, HD, FHD, and RTC modes for various applications, and how do I set the minimum and maximum bit rates?
Please see the [&lt;live-pusher&gt;](https://cloud.tencent.com/document/product/454/12518) Tag Parameter Setting section for how to select the right mode and make bitrate settings.

### How do I listen to key push and playback events?
See [&lt;live-pusher&gt;](https://cloud.tencent.com/document/product/454/12518) Tag Internal Events section for how to listen to push events.
See the [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) Tag Internal Events section for how to listen to playback events.

### The &lt;live-push&gt; tag cannot be inserted to certain mobile phones, is that true?
This problem has been identified and will be fixed in the next version. There is no way to capture this anomaly and prompt the user to allow access to the microphone and camera.
If you see a log message that says "insertLivePusher:fail:system permission denied", that means that no access to the microphone and camera is allowed. Check the microphone and camera permissions in the settings to ensure access to the microphone and camera is allowed.


### Why does the Mini Program &lt;live-play&gt; tag occasionally turn black or fail to play?
You need to first understand the Page Lifecycle of WeChat Mini Programs by viewing [Mini Program Page Life Cycle](https://mp.weixin.qq.com/debug/wxadoc/dev/framework/app-service/page.html#生命周期函数).

For the page lifecycle of mini programs, onLoad only loads data but not renders page, at which time the &lt;live-push&gt; and &lt;liveplay&gt; tags have not been created. Therefore, the method of obtaining or calling livepushercontext and liveplayercontext is uncertain. onReady indicates that the page has been loaded and rendered for the first time. Operations related to &lt;live-pusher&gt; and &lt;live-player&gt; must be implemented in onReady.
Examples:
``` javascript
  onReady: function () {
    var self = this;
    this.data.videoContext = wx.createLivePlayerContext("video-livePlayer");
    this.setData({
      playUrl: "rtmp://live.hkstv.hk.lxdns.com/live/hks",
    }, function () {
      self.data.videoContext.stop();
      self.data.videoContext.play();
    })
  },
```

### How do I solve the log overlay problem when setting style="display:block" for tag &lt;live-player&gt;?
This is an identified problem. If you want to control the showing/hiding of tag &lt;live-player&gt; using the "display" attribute of "style", it is recommended that the hiding setting be style="display:none". For showing, the default value is used for "display" without making any changes.

### 8. The same &lt;live-player&gt; tag is used to playback different URLs, but it does not work. How can I solve this?
When in autoplay mode, playUrl changes are not automatically played back. When not in autoplay mode, call the play function after changing playUrl. Therefore, no matter in which mode, when playUrl is changed to play another URL, you are recommended to do the following:

``` javascript
  onPlay: function () {
    var self = this;
    this.data.videoContext = wx.createLivePlayerContext("video-livePlayer");
    this.setData({
      playUrl: "rtmp://live.hkstv.hk.lxdns.com/live/hks",
    }, function () {
      self.data.videoContext.stop();
      self.data.videoContext.play();
    })
  },
```
Make sure that videoContext is called in setData's callback, and stop must be called before start.

### The mode attribute is dynamically set for the &lt;live-player&gt; tag, but it does not work. How can I solve this?
The dynamically set mode does not become effective dynamically and you need to stop and start again. Please see the following for how to use it:
``` javascript
  onChangeMode: function () {
    var self = this;
    this.data.videoContext = wx.createLivePlayerContext("video-livePlayer");
      if (this.data.mode == "live") {
      this.setData({ mode: "RTC"}, function () {
          self.data.videoContext.stop();
          self.data.videoContext.play();
        });
    }
    else {
      this.setData({ mode: "live"}, function () {
        self.data.videoContext.stop();
        self.data.videoContext.play();
      });
    }
  },
```
### Why does the muted attribute fail to function for some mobile phones when the &lt;live-player&gt; tag of Android Mini Program is in RTC mode?
This is an identified bug. We will fix it in the SDK as soon as possible and make it ready for the next release of WeChat.

### The enable-camera attribute is dynamically set for the &lt;live-pusher&gt; tag, but it does not work. How can I solve this?
The enable-camera attribute does not become effective dynamically and needs to be set in advance. That is, dynamic enabling/disabling of the camera in the push process is not supported. This attribute must be set before push. To make it effective dynamically, you are recommended to do the following:
``` javascript
  onEnableCamera: function () {
    var self = this;
    this.data.videoContext = wx.createLivePusherContext("video-livePusher");
    this.setData({
        enable-camera: "true"
    },function () {
        self.data.videoContext.stop();
        self.data.videoContext.start();
    });
  },
```

### Clean the &lt;live-pusher&gt; and &lt;live-player&gt; on the onUnload page.
Please see the following for details:
``` javascript
  onUnload: function () {
    self.data.pusherContext && self.data.pusherContext.stop();
    self.data.playerContext && self.data.playerContext.stop();
  },
```

### When cover-view is overlaid on top of the &lt;live-pusher&gt; or &lt;live-player&gt; tag, it is not recommended to change the size of the tag.

When the size of &lt;live-pusher&gt; or &lt;live-player&gt; changes, iOS Mini Program cannot change the cover-view overlaid on it, and the interface display is unpredictable. Therefore, when cover-view is overlaid on the &lt;live-pusher&gt; or &lt;live-player&gt; tag, do not dynamically change the size of the tag.

### What is &lt;cameraview&gt; in the Demo source code used for?

Because only the &lt;live-pusher&gt; and &lt;live-player&gt; tags are used to support real-time audio/video chats (especially multi-person video chats), substantial development effort is required. Therefore, based on the native **custom component** capability of WeChat Mini Program, we have encapsulated complex status management and business logics in the custom tag called &lt;cameraview&gt;. You can learn about how to use &lt;cameraview&gt; and &lt;live-player&gt; to quickly build a two-person audio/video chat feature by viewing the codes in `doubleroom\room\room.js` from the source code package.

