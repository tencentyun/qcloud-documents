## Plugin Introduction

- Tencent Video Cloud OBS 265 push plug-in allows OBS-studio (version 20.0.0 or above) to push H.265 video streams to Tencent Video Cloud for LVB.
- Pushing using H.265 can save more traffic than H.264, or get the better video quality for the same traffic.
- This plug-in supports hardware acceleration for **Intel** and **Nvidia** platforms.
- Tencent Video Cloud automatically converts H.265 video streams to H.264 video streams. If the default playback address is of H.264 video stream, contact us to enable H.265 playback configuration to obtain the H.265 video stream playback address.
- Push address does not need to be set specially.


## Instructions

### Step 1: Download and install OBS-Studio 
Download obs studio **20.0.0** or above on OBS Studio [Official Website](https://obsproject.com/) and install it.

### Step 2: Download and install 265 encoding plug-in
Click [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/OBS_Plugins/tx265-plugin-setup.exe) to download and install H.265 plug-in, which can only be installed on OBS Studio of **20.0.0** or above. 

![](https://main.qcloudimg.com/raw/98f69bbefe4e5efee58e609446a5ba6a.png)

> The plug-in installation package automatically detects the installation directory of OBS Studio. If the detection fails, you need to manually select the installation directory of OBS Studio.


### Step 3: Set OBS push parameters

#### 3.1 OBS Settings - Stream:
Go to OBS Settings -> Stream -> Stream Type, select **Tencent Stream (H.265) Service**, and enter the push address.

 After [activating](https://console.cloud.tencent.com/live) the LVB service, use [LVB Console -> LVB Code Access -> Push Generator](https://console.cloud.tencent.com/live/livecodemanage) to generate the push address. For more information, please see [Acquiring Push Playback URL](https://cloud.tencent.com/document/product/454/7915).
![](https://main.qcloudimg.com/raw/81b7aaa96e7beb2744550360d3c1e1dd.png)


#### 3.2 OBS Settings - Output:
Go to OBS Settings -> Output -> Output Mode, and select **Advanced**
Go to OBS Settings -> Output -> Stream -> Encoder, select **Encoder beginning with TX265**, and set encoding parameters as needed
![](https://main.qcloudimg.com/raw/da8c892c2c0cc5ac12c033d40163a2dd.png)

Encoder name | Description
-|-
TX265-Intel QuickSync HEVC Encoder | Intel platform 265 hardware encoding
TX265-NVENC HEVC Encoder | NVIDIA 265 hardware encoding
TX265-QQ265 HEVC Encoder | Tencent Audio/Video Lab self-developed 265 software encoding
TX265-x265 HEVC Encoder | 265 software encoding implemented by X265

If you cannot find the hardware encoder in the encoder list, follow these steps to enable it:

**How do I enable nvdia 265 hardware encoding:**
1. Windows version requirement: Windows 7/8/10
2. [Check if the graphics card supports NVENC H.265 (HEVC)](https://developer.nvidia.com/video-encode-decode-gpu-support-matrix)
Desktop GPU: Graphics card of Geforce GTX 950 series or above
Laptop GPU: Graphics card of GTX 965M, 970M, 980M series or above
3. The driver version is higher than 378.66. [Download the latest driver](http://www.nvidia.com/drivers)

**How do I enable Intel 265 hardware encoding:**

1. Windows version requirement: Windows 7/8/10
2. [Check if your CPU model supports "Intel(r) Quick Sync video"](https://ark.intel.com/zh-cn/)
Skylake or more advanced architecture supports "Intel(r) Quick Sync video"
3. [Download/Install the latest "Intel(r) HD Graphics" driver](https://downloadcenter.intel.com/zh-cn/)
4. ***For dual-graphics card users, to enable Intel 265 hardware encoding, they need to enable "Internal Graphics" in the BIOS/CMOS settings, and connect the onboard VGA or DVI interface (integrated graphics) to the monitor.***

### Step 4: Contact us to activate 265 playback

Tencent Video Cloud automatically converts 265 streams to 264 streams. To play 265 streams, contact us by submitting a ticket or calling the number starting with 400 to enable 265 stream playback configuration. The 264 playback address is still valid and is suitable for clients that cannot play 265 streams.

