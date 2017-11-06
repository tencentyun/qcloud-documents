
## Scenario 1: Beauty LVB

### Step 1: Update SDK to Latest Version 
We improve the beauty filter feature in every new version of the SDK. For example:
- In 1.9.1, we updated the beauty filter engine and made great improvements to certain aspects such as foreground focus, algorithm, exposure and the filter feature's performance.
- In 1.9.2, we optimized noise reduction effect, reducing picture noise while increasing character clearness in nocturnal environment
- In 2.0.0, we increased more filters to iOS in order to solve problems where user's skin appears too yellowish
- ... ...
  
### Step 2: Configure Picture Quality
Note that the picture viewed from the VJ's end is different from what is seen on viewer's end:

- **VJ vs Viewer**:  
The picture seen by the VJ is the collected video which is directly rendered onto the mobile phone screen, thus it retains the best quality. Whereas the picture needs to go through **Video Encoding -> Network Transmission -> Video Decoding** before it reaches the user's phone screen, the viewers will see degraded picture compared to VJ's end due to loss of picture quality caused by the encoding process.
  
 Incorrect parameter configurations will lead to more picture quality loss. A typical mistake is to configure a high resolution with a low bit rate, which will cause a blurred display and serious mosaic. How should we configure?
	 
- **setVideoQuality**
In 1.9.1, we introduced the setVideoQuality function into TXlivePusher with several configuration levels. You can simply choose **High Definition** mode to achieve best quality in beauty LVB. For more information, please see [iOS Platform](https://cloud.tencent.com/document/product/454/7879#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6) and [Android Platform](https://cloud.tencent.com/document/product/454/7885#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6).

### Step 3: Add Manual Focus to Android
The same beauty filter algorithm may yield different result on different Android phones. The main reason is that the difference between the exposure effects on various devices may cause completely different visual experiences.

On iOS platform, we use the auto-exposure feature of the system. While considering that Android models can be greatly different from each other and most inexpensive phones may have poor exposure mechanisms, we recommend that you add an auto-exposure slider on the UI to allow VJs to adjust exposure value on their own in order to meet their demands.

For Android version, the TXLivePush::**setExposureCompensation** API in RTMP SDK can be used to adjust exposure. The parameter value is a floating-point value between -1 and 1:  0 means no adjustment; -1 means lowest exposure and 1 means highest exposure.

![](//mc.qcloudimg.com/static/img/b4c3fcc20a580347bb1360c5b59fd08c/image.png)

### Step 4: Add Color Filter
Filter is also an important aspect, as different color filters create different atmosphere. The VJ may choose a proper filter based on clothes coloration or room light to create a better overall atmosphere for the picture.

![](//mc.qcloudimg.com/static/img/ad0711f3c35f2087d3520677bfd64391/image.png)

Color filter became supported by the RTMP SDK since 1.9.1, we introduced setFilter into TXLivePusher for you to configure filter effect. Our designer group provided 8 materials which are packaged inside the Demo by default. You can use them as you like, without considering about copyright issues.

### Step 5: Serious Mosaic on Android Phones
Some customers find out that pictures pushed by the Android RTMP SDK have serious mosaics, especially when the picture is moving. This is a common performance brought by Android hardware encoding, and there are two solutions:

- **If power consumption is your main concern**
If you're concerned about the App's power consumption, you can consider increasing the bit rate of the pushed stream or use **High Definition** level in setVideoQuality (if you configure a low bit rate, the Android hardware encoding module will ensure a stable bit rate by greatly lowering picture quality)

- **If bandwidth is your main concern**
 Increasing bit rate may not satisfy your demand properly if you're concerned about bandwidth cost. In this case, you can solve the problem by disabling hardware acceleration. Refer to [setHardwareAcceleration](https://cloud.tencent.com/document/product/454/7885#step-7.3A-.E7.A1.AC.E4.BB.B6.E7.BC.96.E7.A0.81) for instructions.

### Step 6: Disable Network Adaption
The **AutoAdjustBitrate** option in **TXLivePushConfig** is the switch for network adaption. If it is enabled, when the VJ's network condition declines, the video quality will be lowered to ensure the smoothness. But this feature is not suitable for Beauty Show LVB.

Network adaption technology is suitable for game LVB scenarios, where viewers consider picture fluency as more important than quality. If the VJ's network becomes unstable during a battle, it's ok to have a degraded picture quality but stuttering is totally unacceptable, which means ensuring fluency (frame rate) by lowing picture quality is a mandatory option.

However, picture quality is more critical in beauty show scenarios. A number of customers report that picture quality varies greatly in different LVB rooms, and enabling network adaption is a possible reason for this.

We recommend that you disable network adaption in these scenarios and use [Active Notification](https://cloud.tencent.com/document/product/454/7946#4.2-.E9.92.88.E5.AF.B9.E6.80.A7.E4.BC.98.E5.8C.96.E6.96.B9.E6.A1.888) to deal with network fluctuations, as this is the fundamental solution.


## Scenario 2: Game LVB
### Option 1: Simple Approach
There are three definition options on the LVB starting screen: Standard Definition, High Definition and Ultra High Definition, **for VJs to choose on their own**. As professionals, a gaming VJ will know which level is suitable for the current game. The configurations for the three definition levels are listed below:
![](//mc.qcloudimg.com/static/img/adff3641312721649a1e0d101fdd981f/image.png)

| Level   | Resolution | FPS | Bit Rate |
|---------|---------|---------|---------|
| SD | VIDEO_RESOLUTION_TYPE_360_640 | 20 | 800 kbps |
| HD | VIDEO_RESOLUTION_TYPE_540_960 | 20 | 1000 kbps | 
| UHD | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1800 kbps |

> Note: The minimum FPS for game LVB scenarios is 20. Viewers will see serious stuttering if the FPS is configured any lower.

### Option 2: Professional Approach
It takes effort and time to configure different resolutions and bit rates for different games. For example:
- **Clash Royale** - For such games where there are no great changes in display, it is recommended to choose the **960 * 540** resolution. A good performance can be achieved with a bit rate of 800 kbps-1000 kbps.

-  **Fishlord** - For such games where there are big changes in display, it is recommended to choose the **960 * 540** resolution, and the bit rate should be relatively higher, such as 1200 kbps - 1500 kbps.

-  **Temple Run** - For such games where there are huge changes in display, it is recommended to choose the **640 * 360** resolution, and the bit rate should be high, such as 2000 kbps. Otherwise there will be mosaic all over the screen.

## Tips on Audio/Video

### Point 1: Is 720p Always Clearer?
If the bit rate is fixed, for example, 800 kbps, **a higher resolution will put more strain on the encoder**.

You can consider the encoder's work as "robbing Peter to pay Paul" - it supports more pixels by offering "bogus", such as decreasing coloration information or introducing mosaic. Similarly, for the same movie file with a size of 2 GB, the 1080p resolution may look worse than the 720p resolution.

Meanwhile, if the viewers watch videos on small mobile phone screens, they won't see much difference between **960 * 540 1000 kbps** and **1280 * 720 1800 kbps**. For instance, the two pictures below are from iOS screencap LVB based on the airplay technology. Can you notice the clearness difference between them?

![](//mc.qcloudimg.com/static/img/98135b33c574c1c70373df982d6ba179/image.png)
> You will see the difference if the pictures are viewed on a 32-inch LCD screen.

### Point 2: Keep FPS Within 24!
If the bit rate is fixed, for example, 800 kbps, then a higher FPS means the encoder must increase the compression ratio for each frame, which means to lower picture quality in order to support enough frames. If the video source comes from camera, then 24 FPS is the highest frame rate for naked eyes. Therefore, an FPS of 20 is already enough to create a good user experience.

Some 3D game players may ask: "Will the game become more fluent with a higher frame rate? Such as 60 FPS, or 120 FPS?" 

Do not confuse the scenarios: Games pursue a high **render frame rate**. The goal is to make the motion effects rendered with 3D models more similar to realistic motion tracks, thus a higher frame rate is always better. 

But such frame rate is not necessary when capturing pictures. For example, mobile phone cameras capture objects in reality. Instead of being simulated by multiple sets of pictures, these objects originally move continuously, so 20 FPS is enough to capture them.

For game LVB, an FPS of 24 is ideal, but you also need to consider system encoding cost, phone temperature, CPU utilization and so on. The VJ will be playing the game on the same phone after all.
 





