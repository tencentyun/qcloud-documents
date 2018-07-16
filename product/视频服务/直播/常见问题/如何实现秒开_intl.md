## What is "Instant Broadcasting"?

**Instant Broadcasting** is to make the time length between the start of video playback and the moment the first frame is displayed as short as possible (in hundreds of milliseconds) to prevent viewers from waiting long.
![](//mc.qcloudimg.com/static/img/9a1541e3d8f6796e8025b571d5267c7c/image.png)
This depends on optimized cloud services and player. In an LVB, a combination of Tencent Cloud Audio/Video SDK and video cloud service allows you to open the first frame at a speed as high as about **200ms**, and even open it instantly if you have sufficient downstream bandwidth.

## How to Achieve Instant Broadcasting?
### Apps
Use [Tencent Cloud Audio/Video SDK](https://cloud.tencent.com/document/product/454/7873) and the FLV playback protocol to achieve instant broadcasting:
- **HTTP + FLV playback protocol**
The HTTP + FLV playback protocol is the most widely used protocol in the LVB industry. Thanks to its simple data format, it allows immediate access to Audio/Video data once the server is connected. In contrast, the RTMP protocol provides a slightly lower first frame rate than the FLV protocol due to the several negotiation handshakes required to establish a connection.
- **Tencent Cloud Audio/Video SDK**
The way instant broadcasting works on cloud is quite simple. With a group of GOP pictures (containing at least a key frame for decoding) always cached on a server, the player can obtain a key frame (I frame) once it is connected to the server, and then proceed with decoding and playing. Such caching on cloud, however, has some side effects: the player is often suddenly stuffed with several seconds of audio/video data after it is connected to a server, which will cause a major delay on the player end. We call it "side effect of instant broadcasting".
Besides instant broadcasting, a good player should also have excellent **delay correction** ability that automatically corrects player end delay to a proper level (such as less than 1 second) without affecting the viewing experience. Tencent Cloud Audio/Video SDK is a great way to achieve this, even allowing you to specify a delay correction mode for a player ([iOS](https://cloud.tencent.com/document/product/454/7880#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F)/[Android](https://cloud.tencent.com/document/product/454/7886#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F)).

### PC browsers
The video playback kernels on PC browsers usually use the Flash control (Chrome also supports MSE, but it has no obvious advantage over Flash). Flash players adopt a rigid **forced buffering** strategy, providing little room for optimization of video loading speed, which is unlikely to be kept within 1 second. This fact can be found on many video websites and LVB platforms when you're using a PC browser.

### Mobile browsers
- **iPhone**
Safari works perfectly with HLS (m3u8) and even allows using iPhone's hardware decoding chip to facilitate video playback. Usually, you do not have to worry about the video loading speed as long as DNS caches are available, but this is limited to the iOS platform.
- **Android**
Due to the severe fragmentation, the performance on the Android platform varies greatly with the system browsers that come along with the various OS versions and devices. The browsers within QQ and WeChat even have Tencent's X5 kernel installed, which would result in large performance variations.
