Apple Inc. announced in WWDC 2016 that by default all new Apps submitted as of January 1, 2017 are not be allowed to use `NSAllowsArbitraryLoads=YES` to bypass ATS restrictions. Tencent Cloud will officially support HTTPS as of December 12. By then, you only need to use the new version of SDK (APIs remain unchanged) and change the video URL prefix from `http://` to `https://`. The new SDK can be automatically adapted to the change.

Please note that compared with HTTP, HTTPS provides a higher security (which is not absolutely necessary for videos), but leads to a lower connection speed and a higher CPU utilization. If HTTP is still required for your App under Apple's new policy, you need to modify Info.plist by adding `myqcloud.com` to `NSExceptionDomains`, as shown below.
![myqcloud](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/myqcloud.png)
Disabling ATS for specific domain names can be approved by Apple's audit team, but you may need to specify that `myqcloud.com` is a domain name for video playback.

