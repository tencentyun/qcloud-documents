
**The current definition and size of videos published in Tencent Video Cloud **

Tencent Cloud provides extensive transcoding features available for use when publishing. Users can refer to the following definition classification to transcode and publish videos for viewers in different network environments to enjoy better experience:
Fluent (mobile phone): Bit rate: 256 kbps; graphic size: approx. 320 ** * ** 240; 
SD: Bit rate: 512 kbps; graphic size: approx. 640 ** * ** 480;
HD: Bit rate: 1024 kbps; graphic size: approx. 1280 ** * ** 720;
UHD: Bit rate: 2500 kbps; graphic size: approx. 1920 ** * ** 1080;

After transcoding, the detailed specification and technical parameters of videos are as follows:
![](//mccdn.qcloud.com/img56caab27ef9c8.png)

If the resolution of a video uploaded by a user is different from either one of the above sizes, the video file will be outputted by aligning the width with the above standard sizes and scaling the height during transcoding output.

If the resolution of a video uploaded by a user is lower than the configured transcoding format (for example, uploading a video with a resolution of 640** * ** 480 while selecting HD when configuring transcoding format), the system will still transcode the video according to the configured HD format. In this case, however, the low video definition will lead to a poor user experience and more traffic/bandwidth consumption.


**Are there any differences in the published videos if I upload them at different time/regions?**

Theoretically no, our system supports the access from any regions on a 24/7 basis. For the quality of system service, please refer to the information about Tencent Cloud service quality. It should be noted that, user's viewing experience is mostly determined by the network quality from user client to the video server and user's local hardware configuration. Thus during the peak hours of network service, there may be a difference in user experience due to potential changes in user's network or low user hardware configuration.

**Is there any limit on the number of users to watch online videos at the same time?**

There is no such limit. Currently our system does not have such restriction and can support unlimited number of users to watch online videos at the same time.

**The video won't play automatically when published.**

If you don't make any configuration, the video will use default configuration after being published, that is, auto playback is disabled. You can modify the configuration by checking "auto playback" when publishing.

**The video is not as clear as before.**

The definition during video playback depends on two aspects:
1) The definition provided by CVM after the video is transcoded when publishing;
2) The network environment under which users watch the video. If you feel the video is played in a lower definition, one possibility is that a low definition, instead of a high-definition video is stored in the CVM; the other possibility is poor network environment, in which case the player will adapt to a low-definition video to play.

**Lagging occur during video playback**

If the video itself dose not have any problems, the stutters may be caused by low configuration of the computer on which the video is played or poor local network condition (including bandwidth and latency). You can analyze the problem by using another device to play the video or changing the network environment. If the problem still remains, please contact our after-sales department.

**In the "Video Management" menu, what are "Adaptive HTML", "FLASH" and "IFRAME" displayed in "Publish Video" used for?**

These are three methods for publishing custom codes. Their usages are as follows:

**Adaptive HTML** is HTML code used to embed a video player when editing a web page. The player can be displayed and used to play videos when a user visits the web page. This code may need a few custom modifications, thus it is suitable for users who have an understanding of HTML language. This code can automatically adapt itself to both mobile and PC clients. It supports WEB SDK feature for highly flexible redevelopment. Refer to [WEB SDK Development Guide](http://video.qcloud.com/download/docs/QVOD_Player_Web_SDK_Developer_Guide.pdf) for details about how to use it .

**Flash address** is a URL address, usually with a format of `http://****.swf` (there may be a parameter string following behind). It can be opened using the browser address bar, or referenced in a web page. Flash can be opened in most browsers, but may not be supported by the default browser Safari in iOS or MAC X systems.

**IFRAME code** is used to quickly publish the player code directly without any modifications. You simply need to copy and paste the code to the proper location in HTML page, without the need to understand the code itself
. With excellent compatibility, IFRAME tag can currently support major browsers including Chrome, IE, Safari, Firefox and so on.

The order for all the codes to be adapted to different terminals is as follows:

If a user accesses using a mobile client (including iOS and Android systems), the video will only be played using HTML5; if a user accesses from PC client, flash will be used in priority, and then HTML5 if the browser does not support flash. If HTML5 is not supported, the user will be prompted to download a new version of the browser at the player's original location. In both of the above two methods, the video file relevant to the specific player configuration will be displayed.

**What is the difference between "Source file URL" and "Video with Web player code" displayed in "Publish Video" in "Video Management"?**

Source file URL corresponds to the video with specific bit rate, and contains no player information itself. The video can be opened in the browser directly, and played using browser or player built in the operating system.

Web player code corresponds to the codes used to edit web, including Flash address, adaptive HTML code and IFRAME code. Currently, the code can contain player configuration information (e.g. definition, video ads, social-sharing, etc.) and security password (optional). This code can be embedded into a web page edited by user.

**Is Web player code supported by mobile devices?**

This code can be used to play videos on various mobile devices. Refer to "Adaptive HTML" displayed in "Publish Video" in the "Video Management" for details.

**In "Video Management", if I modify player configuration after the "Web player code" has been published, do I need to re-publish the HTML code?**

No, the system will automatically maintain and update the code. The published player code will take effect immediately when the player configuration is modified.

In "Web Player Management", what will happen if I delete a certain custom player?
In this case, since the custom player is deleted, the video files will be automatically associated to "default player configuration", which will be applied to the video files. The code that is already published can still be used. If you need to change the configuration, please redefine and select a player, then re-publish the code.

**What is a playback password?**

Playback password is a security mechanism used to ensure that the video is only viewed by authorized users. Users need to enter an 8-digit alphanumeric password when playing the video. The password is case-sensitive (space and special characters are not supported). The video can be played once the correct password is provided. You can configure playback password individually for each video file when publishing them. This password is suitable for scenarios where the videos require basic protection.

**What are Blacklist & Whitelist?**

You can use Blacklist/Whitelist to allow or restrict requests from accessing a video from a player code of a specific web page. This list is effective to videos published by a player code. Users can enable this feature globally, and specify whether to use blacklist or whitelist. Each list can contain 10 URLs. Blacklist & Whitelist function by checking the source referer of access requests. To protect the video file URL, refer to [URL Hotlink Protection Feature](http://cloud.tencent.com/doc/product/266/URL%E9%98%B2%E7%9B%97%E9%93%BE).

**What is the difference between watermark and Logo?**

A watermark is a fixed identifier completely embedded into a video during transcoding, and cannot be canceled once transcoding is finished. A Logo is displayed on top of a video and inside the player when the video is played using a player. It can be repositioned or canceled at any time.

**Is dynamic watermark supported for the Web player?**

It's not supported for the moment. When this feature becomes available, you can upload the viewer's ID using API and make it appear in the video screen in a dynamic and random pattern, to protect video content.

**Are video ads supported by the Web player?**

Currently, you can add static video ads at the start of videos.

**What is the relationship between Web player and video files? How many Web players can I create?**

A Web player contains the playback parameter configurations when a video is played using the web player code. The configurations include the appearance of the player, video ads, etc. The player parameter configurations in the management screen will not have any effect if the file is not played through player. For example, accessing the video file URL directly via browser, or playing the file by using a third-party player or a self-developed player. Currently you can create up to 10 players in the system.

**Can I customize the appearance of the player?**

Currently, users can customize Logo, appearance and size of the player from the management page. Users can also customize the size of the player on iOS/Android mobile devices by using SDK.


