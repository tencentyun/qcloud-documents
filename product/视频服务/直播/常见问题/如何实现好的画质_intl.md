## Scenario 1: Beauty LVB

### Step 1: Update SDK to the latest version 
The beauty filter effects are optimized with each release of new version of SDK. For example:
- In 1.9.1, the beauty filter engine was updated, and many improvements were made to the foreground focus, algorithm, exposure and performance.
- In 1.9.2, the noise reduction effect was optimized to greatly reduce the noises at night and improve the clarity of person images in videos.
- In 2.0.0, more filters were provided for iOS to improve the visual effect of yellowish skin tone.
- ... ...
  
### Step 2: Configure image quality
The video image quality displayed to VJs is different from that displayed to viewers:
- **VJ vs Viewer**:  
The video images seen by a VJ are produced from the captured videos that are directly rendered on the phone screen and thus have the best clarity. The images need to go through **Video Encoding** > **Network Transmission** > **Video Decoding** before being rendered on the phone screen of viewers. The video encoding can affect the image quality, so the images displayed to viewers are not as clear as the ones displayed to the VJ. Inappropriately configured parameters can greatly reduce the image quality. A typical example is "high resolution plus low bitrate", which can cause blurred display and serious mosaics. 
- **setVideoQuality**
In 1.9.1, the function setVideoQuality was added in TXLivePusher with a range of levels available. You can have the best image quality in beauty LVB by simply choosing **HD** mode. For more information, please see [iOS Platform](https://cloud.tencent.com/document/product/454/7879#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6) and [Android Platform](https://cloud.tencent.com/document/product/454/7885#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6).

### Step 3: Add manual exposure on Android
The same beauty filter algorithm may yield different effects on different Android phones. This is because the difference between various devices in terms of exposure performance leads to different visual effects.
On iOS devices, auto-exposure is adopted. But Android devices are significantly different from iOS ones, and some low-end Android phones have an unsatisfactory auto-exposure effect. Therefore, it is recommended to provide a slider on the page for VJs to adjust exposure value manually as needed.
The API TXLivePush::**setExposureCompensation** in the Android RTMP SDK can be used to adjust exposure, with the parameter value being a float value between -1 and 1: 0 - no adjustment; -1 - minimum exposure; 1 - maximum exposure.
![](//mc.qcloudimg.com/static/img/b4c3fcc20a580347bb1360c5b59fd08c/image.png)

### Step 4: Add color filters
Filters are also important because different color filters create different atmosphere. A VJ can choose a filter to match his/her clothes or room light to create a better visual effect.
![](//mc.qcloudimg.com/static/img/ad0711f3c35f2087d3520677bfd64391/image.png)
Color filters have been supported as of RTMP SDK 1.9.1. The setFilter added in TXLivePusher can be used to set filter effect. Eight sets of color filter materials are made available in the Demo. You can use them on a royalty-free basis.

### Step 5: Serious mosaics on Android
Some customers find that the images pushed by the Android RTMP SDK have serious mosaics, especially for dynamic images. This is a common problem created by Android hardware encoding, and you can solve it in two ways:
- **For a lower battery drain**
If you care more about the App's battery drain, increase the bitrate of the pushed streams or use **HD** in setVideoQuality (if you set a low bitrate, the Android's hardware encoding module ensures a consistent bitrate by greatly reducing the image quality).
- **For a lower bandwidth cost**
 If you care more about the bandwidth cost, increasing bitrate may not be a good solution. Instead, you can solve this problem by disabling hardware acceleration. For more information, please see [setHardwareAcceleration](https://cloud.tencent.com/document/product/454/7885#step-7.3A-.E7.A1.AC.E4.BB.B6.E7.BC.96.E7.A0.81).

### Step 6: Disable network adaption
The **AutoAdjustBitrate** in **TXLivePushConfig** is used to enable/disable network adaption. If it is enabled, the image quality is reduced to ensure smoothness in case of a poor network of VJ. But this feature is **not suitable** for beauty shows. Network adaption is suitable for game LVB scenarios, where viewers attach more importance to smoothness than image quality. If the VJ's network becomes unstable during a battle, it's ok to have a degraded image quality but stutters are totally unacceptable, so it is necessary to trade off image quality for smoothness (frame rate). However, image quality is more important in beauty show scenarios. Many customers report that the image quality varies greatly with different rooms. This is likely caused by the enabling of network adaption.
We recommend that you disable network adaption and deal with network fluctuations by using [system alerts](https://cloud.tencent.com/document/product/454/7946#4.2-.E9.92.88.E5.AF.B9.E6.80.A7.E4.BC.98.E5.8C.96.E6.96.B9.E6.A1.888) to solve the problem more fundamentally.

## Scenario 2: Game LVB
### Option 1: Simple approach
Provide three definition options on the LVB starting page - SD, HD and UHD - **for VJs to select from**. A VJ in game LVB can find out which option is suitable for the game he/she is playing. The configurations for the three options are as follows:
![](//mc.qcloudimg.com/static/img/adff3641312721649a1e0d101fdd981f/image.png)

| Option | Resolution | FPS | Bitrate |
|---------|---------|---------|---------|
| SD | VIDEO_RESOLUTION_TYPE_360_640 | 20 | 800 kbps |
| HD | VIDEO_RESOLUTION_TYPE_540_960 | 20 | 1000 kbps | 
| UHD | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1800 kbps |

> **Note:**
> The minimum FPS in game LVB scenarios is 20. Serious stutters can occur at viewer end in case of an FPS less than 20.

### Option 2: Professional approach
Configure different resolutions and bitrates for different games. For example:
- **Clash Royale** - For such a game that features less dynamic images, the combination of a resolution of **960 * 540** and a bitrate between 800 kbps and 1000 kbps can produce a good effect.
- **Fishlord** - For such a game that features more dynamic images, the combination of a resolution of **960 * 540** and a higher bitrate between 1200 kbps and 1500 kbps is recommended.
- **Temple Run** - For such a game that features highly dynamic images, it is recommended to choose a resolution of **640 * 360** and a very high bitrate, for example, 2000 kbps, to avoid serious mosaics.

## Tips on Audio/Video

### 1: A resolution of 720p does not necessarily mean a higher clarity
For a given bitrate, for example, 800 kbps, **a higher resolution will make it harder for an encoder to deliver a good image quality**. The encoder can support sufficient pixels only by decreasing color elements or introducing mosaics. For the same movie file sized at 2 GB, a 1080p resolution may render less clear images than a 720p resolution.
If the viewers watch videos on small phone screens, they won't see much difference between **960 * 540 1000 kbps** and **1280 * 720 1800 kbps**. For instance, the two images below are captured from screencap LVB on iOS using the airplay technology:
![](//mc.qcloudimg.com/static/img/98135b33c574c1c70373df982d6ba179/image.png)
>**Note:**
> You will see the difference if the images are displayed in full-screen mode on a 32-inch LCD screen.

### 2: Keep the FPS within 24
For a given bitrate, for example, 800 kbps, a higher FPS makes it necessary for the encoder to increase the compression ratio for each frame, which means reducing the image quality to support enough frames. If the video source is camera, then 24 FPS is the maximum frame rate for naked eyes. Therefore, an FPS of 20 is already enough to offer a good user experience. Some 3D game players may ask: "Does a higher frame rate, such as 60 or 120 FPS, mean a higher smoothness? " 
It depends on the scenarios: In a game scenario, a higher **rendering frame rate** is recommended to make the motion effects rendered with 3D models more similar to the motion trajectories in the real world. But a high frame rate is not needed for capturing. For example, what are captured by a phone camera are the objects in reality, which are in motion continuously and are not simulated through refreshes of images, so 20 FPS is enough.
For game LVB, an FPS of 24 is ideal, but you also need to consider such factors as system encoding cost, phone temperature, and CPU utilization.


