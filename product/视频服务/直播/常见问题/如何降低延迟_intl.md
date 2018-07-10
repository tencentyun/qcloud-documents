Generally, the delay of RTMP push+FLV playback is about 2-3 seconds. An extra-long delay indicates an exception. In case of an extra-long delay, perform the troubleshooting by following steps below:

### Step 1. Check the playback protocol
It is quite normal that many customers using HLS (m3u8) as the playback protocol experience a longer delay. Apple's HLS is a streaming protocol based on a total of 3-4 large-granular TS fragments, with each fragment featuring a time period of more than 5 seconds. Therefore, it is not unusual that the total delay may reach about 20-30 seconds.
To solve the problem, use the FLV protocol instead. Please note that only HLS (m3u8) playback protocol can be selected if you want to watch LVB on mobile browsers. Other LVB protocols are not supported on Apple's Safari browser.

### Step 2. Check the player settings
Tencent Cloud RTMP SDK's player supports Speedy, Smooth and Auto modes. For more information about the settings, please see [adjusting delay](https://cloud.tencent.com/document/product/454/7886#Delay).
- **Speedy**: With a delay within 2-3 seconds in most scenarios, this mode is suitable for Beauty Show LVB.
- **Smooth**: With a delay within 5 seconds in most scenarios, this mode is suitable for scenarios that are insensitive to delay but have a high requirement for smoothness (such as Game LVB).
![](//mc.qcloudimg.com/static/img/9e958f11e25eb2d2ca21c5935ae094e1/image.png)

### Step 3. Disable watermarking in background
Tencent Cloud supports watermarking in background to cater for the customers who cannot use Tencent Cloud RTMP SDK's pusher (supporting watermarking for live streaming) but have a need for watermarking. However, this solution will introduce an extra three second delay. If you are using the Tencent Cloud RTMP SDK to push streams, disable the watermarking in background and then perform watermarking on the App of VJ.

### Step 4. Third-party pusher
The desired effect can be ensured only when Tencent Cloud integrated solution is used. Many third-party pushers deal with insufficient upstream bandwidth through unbounded buffer. If you're using a third-party pusher, you're recommended to use Tencent Cloud RTMP SDK's push Demo to make a comparison to eliminate the possibility that the third-party pusher causes an extra-long delay due to the encoding buffer.

### Step 5. Check OBS settings
 Many customers who use OBS for push report a long delay at viewer end. It is recommended to configure parameters as described in [push on PC](https://cloud.tencent.com/document/product/267/7962). Be sure to set the key frame interval to 1 or 2.


