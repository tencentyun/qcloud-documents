Generally, the delay of RTMP push + FLV playback is about **2-3 seconds**. An extra-long delay indicates an exception. In case of an extra-long LVB delay, perform the troubleshooting by following steps below:

## Step1. Check the playback protocol
It is quite normal that many customers using HLS (m3u8) as the playback protocol experience a longer delay. Apple's HLS is a streaming protocol based on a total of 3-4 large-granular TS fragments, with each fragment featuring a time period of more than 5 seconds. Therefore, it is not unusual that the total delay may reach about 20-30 seconds.

To solve the problem, use the FLV protocol instead. Please note that only HLS (m3u8) playback protocol can be selected if you want to watch LVB on mobile browsers. Other LVB protocols are not supported on Apple's Safari browser.

## Step 2. Check the player settings
Tencent Cloud RTMP SDK's player supports the **Speedy**, **Smooth**, and **Auto** modes:
- **Speedy**: With a delay within 2-3 seconds in most scenarios, this mode is suitable for Beauty Show LVB.

- **Smooth**: With a delay of over 5 seconds in most scenarios, this mode is suitable for scenarios that are insensitive to delay but have a high requirement for smoothness (such as Game LVB).

- **Auto**: For a good network condition, the delay is kept within 2-3 seconds. In case of a greater network fluctuation, the delay is automatically adjusted to be longer than 5 seconds.


![](//mc.qcloudimg.com/static/img/9e958f11e25eb2d2ca21c5935ae094e1/image.png)

##- **Step 3. Disable watermarking at background**.
Tencent Cloud supports watermarking at background for customers who cannot use Tencent Cloud RTMP SDK pusher (that supports watermarking at the LVB end) but need watermarking. However, watermarking will bring about an extra 3 seconds of delay. For this reason, if you are using Tencent Cloud RTMP SDK to push, disable the watermarking at background and add watermarks on the App at the VJ end.


**Step 4. Third-party pusher
We can ensure the desired effect only when Tencent Cloud integrated solution is used. Many third-party pushers deal with insufficient upstream bandwidth through unbounded buffer. If you're using a third-party pusher, you're recommended to use Tencent Cloud RTMP SDK's push Demo first to make a comparison to eliminate the possibility that the third-party pusher causes an extra-long delay due to the encoding buffer.
 
