## Overview
Tencent Cloud VOD provides hotlink protection to control the video playback permissions. When the hotlink protection is enabled, Tenctent Cloud CDN node checks the key information in the playback requests and returns the video data for the approved requests.

## Type and Capability

![](https://mc.qcloudimg.com/static/img/25a737ebfe83cd06104dfb70aedce42d/image.png)

Tencent Cloud VOD hotlink protection is classified into Referer hotlink protection and Key hotlink protection.

### Referer Hotlink Protection
The referer mechanism based on HTTP protocol identifies the request source using the referer field in the playback request header. Developers can list some domain names into the blacklist/whitelist, based on which the CDN node authenticates and allow or deny the playback requests accordingly.

For more information about Referer hotlink protection, please see [Referer Hotlink Protection](/document/product/266/14046).

### Key Hotlink Protection
It allows developers to combine the playback control parameters of a video to the video URL in the form of QueryString. The CDN node checks the playback control parameters in the URL and controls the playback of video based on the parameters. Key hotlink protection supports "Hotlink Protection Validity Period Control" and ""Video Playback Duration Control" by using the "Expiration Time Parameter" and "Trial Time Parameter".

#### Hotlink Protection Validity Period Control
It specifies the expiration time in the video URL. If the requested video URL has expired, the video cannot be played. In this way, you can set a validity period for the video URL to prevent other people from transferring the video URL to other sites for long-term use.

#### Video Allowable Playback Duration Control
It specifies the trial duration in the video URL. For example, only the first 5 minutes of video is allowed to be played. In this way, the trial mode for unpaid users is implemented.

For more information about Key hotlink protection, please see [Key Hotlink Protection](/document/product/266/14047).

