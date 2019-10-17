**Does the publishing result vary with time and region?**

Theoretically not. Our system is now allowed to be accessed from anywhere at any time, and Tencent Cloud service quality information is available for your reference. Please note that, users' viewing experience is largely determined by the quality of the network from user terminal to video server and their local hardware configuration. Therefore, during peak hours of network services, experience may vary due to the change of network conditions or low hardware configuration.

**Is there a limit to the number of online viewers who watch video at the same time?**

Theoretically no. As our system does not set any limits, it allows an unlimited number of online viewers to watch video at the same time.

**Why can't a published video be played automatically?**

If no configuration is made, the default configuration is used when the video is uploaded and published, that is, the auto playback feature is disabled. You can modify this configuration by selecting "Auto Playback" when publishing videos.

**Why is the video not as clear as before?**

The definition of a video during playback depends on two aspects:
1. The definition provided by the CVM when the video is transcoded and published.
2. The network environment where users are watching video. Decrease in definition during video playback may be caused by two factors. One is that a low-definition instead of high-definition video is stored in the CVM. Another is that the player may adapt to a low-definition video for playback due to poor network environment.

**Why does stutters occur during video playback?**

If the stutter is not caused by the video file itself, it may be caused by the low computer configuration or poor local network condition (including bandwidth and latency). This problem can be solved by changing the hardware for playback or the network environment. If the problem still exists, contact our after-sales service.

**In "Video Management" menu, what are "Adaptive HTML", "FLASH"and "IFRAME" displayed in "Publish Video" used for?**

These three options are methods for publishing custom codes. Their uses are as follows:

**Adaptive HTML** is HTML code used to embed a video player into a web page, so that the player is displayed and video is played when users browse the webpage. This code may require minor modifications for customization and is therefore suitable for customers who have an understanding of the HTML language. The code can automatically adapt to mobile devices and PCs, and also supports WEB SDK feature for highly flexible secondary development. For more information, please see [Development Guide for WEB SDK](http://video.qcloud.com/download/docs/QVOD_Player_Web_SDK_Developer_Guide.pdf).

**FLASH Address** is an URL address, generally in the format of `http://****.swf` (possibly followed by a string of parameters). It can be opened in the browser's address bar or referenced in a web page. Flash can be opened in most browsers, but may not be supported by Safari, the default browser in iOS or MAC X systems.

** IFRAME Code ** allows you to quickly and directly publish the player code without any modifications. You can simply copy the code and paste it to the corresponding position of the HTML page without the need to know the contents of the code.
IFRAME tags are highly compatible and supported in many mainstream browsers including Chrome, IE, Safari, Firefox.

All codes adapts to different terminals in the following order:

If users access a web page on mobile device (including iOS and Android systems), the video will only be played using HTML5. If users access a web page on PC, flash will be used in priority. However, HTML5 is used if the browser does not support Flash. If HTML5 is not supported, the user will be prompted to download a new version of the browser at the player's original location. In both of the above two methods, the video file relevant to the specific player configuration will be displayed.

**What is the difference between "Source file URL" and "Video with Web player code" displayed in "Publish Video" in "Video Management"?**

Source file URL corresponds to the video with specific bit rate, and contains no player information itself. The video can be opened in the browser directly, and played using browser or player built in the operating system.

Web player code corresponds to the codes used to edit web, including Flash address, adaptive HTML code and IFRAME code. Currently, the code can contain player configuration information (e.g. definition, video ads, social-sharing, etc.) and security password (optional). This code can be embedded into a web page edited by user.

**Is web player code supported in mobile devices?**

This code can be used to play videos on various mobile devices. For more information, please see "Adaptive HTML" displayed in "Publish Video" in the "Video Management".

**In "Video Management", if I modify player configuration after the "Web player code" has been published, do I need to republish the published HTML code?**

No, the system will automatically maintain and update the code. The published player code will take effect immediately when the player configuration is modified.

In "Web Player Management", what will happen if I delete a certain custom player?
In this case, since the custom player is deleted, the video files will be automatically associated to the default player configuration, which will be applied to the video files. The code that is already published can still be used. To change the configuration, please redefine and select a player, then re-publish the code.

**What is a playback password?**

Playback password is a security mechanism that ensures that the video content is only viewed by authorized users. When you play a video, you need to enter an 8-digit alphanumeric password. The password is case-sensitive (space and special characters are not supported). The video can be played normally only when you enter a correct password. You can configure playback password individually for each video file when publishing them. This password is suitable for scenarios where the video content require basic protection.

**What are blacklist/whitelist?**

You can use blacklist/whitelist to allow and restrict the request for accessing videos published by a player code from a particular web page. These lists are effective to videos published by the player code. Users can enable this feature globally and specify to use a blacklist or a whitelist. Each list can contain up to 10 URLs and functions by checking the source referer. To protect the video file URL, please see [URL Hotlink Protection](http://cloud.tencent.com/document/product/266/2875).

