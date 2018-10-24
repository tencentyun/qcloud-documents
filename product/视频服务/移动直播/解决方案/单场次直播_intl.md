Single-session LVB is to broadcast one or several LVB streams related to official PGCs simultaneously. It is often used for live broadcasting of events and leader speeches. A typical example is a popular livestreaming quiz App Chongding Dahui prevailing at the end of 2017.

Single-session LVB is easy to integrate. As VJ (push) ends are provided with mature solutions to PGC resources, your R&D resources are used to play live audio/video streams on terminals:

<h2 id="URL">Push and playback URLs</h2>

Because only a few LVB streams are broadcasted in single-session LVB, you can manually generate push and playback URLs via [**LVB Console** -> **Access Management** -> **LVB Code Access** -> **URL Generator**](https://console.cloud.tencent.com/live/livecodemanage) . For more information, please see [DOC](https://cloud.tencent.com/document/product/454/7915).

Tencent Cloud customers frequently asked a question: <font color='red'>Why can't I push streams?</font> This is caused by two factors:
- The expiration time is too short. URLs are considered invalid after the set expiration time.
![](https://mc.qcloudimg.com/static/img/da82219b2d8068dc1aa1fe1d00abb6a3/image.png)
- One push URL cannot be used by two persons at the same time. Otherwise a conflict occurs.

<h2 id="PUSH">How to push</h2>

<h3 id="CASE1">Case 1: Push by a mobile video studio</h3>

![](https://mc.qcloudimg.com/static/img/4fd30f06ca5c20050c1fc588ef9b5ef1/image.jpg)
Suitable for formal live broadcasting scenarios. Use a professional mobile video studio to interface with a PC, and then push via [Obs Studio](https://obsproject.com/zh-cn)  on the PC.

- **Advantage**: A mobile video studio makes it easy to switch to ads or play other videos during in-show time. The popular livestreaming quiz App Chongding Dahui prevailing at the end of 2017 uses this solution.
- **Reference**: For more information on push by Obs, please see [DOC](https://cloud.tencent.com/document/product/267/13460) .

<h3 id="CASE2">Case 2: Push by cameras</h3>

![](https://mc.qcloudimg.com/static/img/fa7f85b62138f0ac1b0a4568e98e34da/image.jpg)
Suitable for LVB scenarios unable to be implemented in studios, such as **live broadcasting for events** and **live shows**. Connect cameras to a PC via HDMI and push by [Obs Studio](https://obsproject.com/zh-cn), or connect cameras to a video encoder and push by the video encoder.
- **Advantage**: Location-insensitive for LVB.
- **Reference**: For more information on push by Obs, please see [DOC](https://cloud.tencent.com/document/product/267/13460).
- **Note**: LVB requires high network quality. As networks vary depending on locations for event LVB or live show, be sure to test networks in advance and get both WiFi network and 4G mobile data ready. In addition, wired network is preferred.

<h3 id="CASE3">Case 3: Push by mobile</h3>

![](https://mc.qcloudimg.com/static/img/a4aa40a617b44213552a3810b97ceced/image.jpg)
With improved mobile performance, LVB on mobile is as good as the above two solutions. You can install the [Video Cloud Toolkit](https://cloud.tencent.com/document/product/454/6555#DE) on a mobile with good performance and start pushing by using the **RTMP push**.
- **Advantages**: Easy to use and get started, low costs.
- **Reference**: If you want to add your watermark in LVB streams, download a proper SDK and replace the demo watermark with yours. For more information on the push SDK, please see ([iOS](https://cloud.tencent.com/document/product/454/7879) | [Android](https://cloud.tencent.com/document/product/454/7885)).
- **Note**: Videos pushed to Tencent Cloud are smoother than those pushed to other clouds. That is because UDP protocol with strong anti-packet loss and bandwidth occupation capabilities is used by Tencent Video Cloud toolkit to push videos to Tencent Cloud while RTMP protocol is used to other clouds.

<h2 id="PLAY">How to play</h2>

### iOS player
- **Step 1**: Download Tencent Cloud [SDK](https://cloud.tencent.com/document/product/454/7873#iOS)  SDK. If push is not required, download an independent player version.

- **Step 2**: Integrate the SDK into your SDK according to the documentation [TXLivePlayer](https://cloud.tencent.com/document/product/454/7880) .

### Android player
- **Step1**: Download Tencent Cloud [SDK](https://cloud.tencent.com/document/product/454/7873#Android) SDK. If push is not required, download an independent player version.

- **Step 2**: Integrate the SDK into your SDK according to the documentation [TXLivePlayer](https://cloud.tencent.com/document/product/454/7886) .

### Web player
- **Interfacing guide**: Because javascript components can be directly used in Web pages, you only need to interface with the Web player according to the documentation [TCPlayer](https://cloud.tencent.com/document/product/454/7503) .

- **High latency**: URLs with HLS (m3u8) protocol can be played by Web players on various terminals with a latency of over 20 seconds, which is greater than the latency of 2 to 5 seconds when URLs with FLV protocol are played.

### Mini Program Player
- **Specific category**: If the category of your Mini Program meets [category requirements](https://cloud.tencent.com/document/product/454/12519#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6), you can use the tag &lt;live-player&gt (generated from the simplified version of the built-in Tencent Cloud SDK) to implement LVB on iOS and Android with low latency according to [DOC](https://cloud.tencent.com/document/product/454/12520#.E7.9B.B4.E6.92.AD.E6.92.AD.E6.94.BE.EF.BC.88flv.E3.80.81rtmp.EF.BC.89).

- **Other categories**: If your Mini Program belongs to any other categories, you can only implement LVB with high latency by using the tag &lt;video&gt; plus HLS (m3u8) protocol.


