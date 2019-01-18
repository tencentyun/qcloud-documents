## Feature Overview
* The referer mechanism based on HTTP protocol identifies the request source using the referer field carried in the HTTP header. Developers can identify and authenticate the source of video request by configuring the referer blacklist/whitelist.
* Blacklist and whitelist are supported. After the video playback request reaches the CDN node, the node authenticates the request source according to the Referer blacklist/whitelist configured by the user. For requests meeting the requirements, CDN will return the video data. Otherwise, the response code of 403 will be returned to reject the playback request.

## Configuration Wizard
Tencent Cloud VOD "Console" -> "Global Settings" -> "Domain Name Settings" -> "Hotlink Protection Settings".

![Image](https://mc.qcloudimg.com/static/img/cf5a076e57d3287852bf4ab3fe609bbe/image.png)

"Enable Referer Hotlink Protection" -> Select "Whether to Leave Referer Empty" -> Select blacklist/whitelist and add objects -> OK.

![Image](https://mc.qcloudimg.com/static/img/a8519825840de1bc0cb23cccc40436f6/image.png)

After the configuration is saved, it takes about 5 minutes for this configuration to take effect for all the CDN nodes.

## Notes
* This feature is optional and disabled by default.
* After this feature in enabled, select and enter the blacklist or whitelist. As the blacklist and whitelist are mutually exclusive, only one mode is supported at a time.
* You can choose whether to leave referer empty for the requested video (that is, whether to directly enter the video URL in the browser to play the video).
* The number of domain names in a blacklist/whitelist should be between 1 and 10 (inclusive), with each recorded in a separate row.
* Do not append the protocol names (`http://` and `https://`) in front of domain names. Domain names use prefix match. For example, if `abc.com` is entered, `abc.com/123` and `abc.com.cn` are also matched. In addition, wildcard (such as `*.abc.com`) can be used in prefix.

