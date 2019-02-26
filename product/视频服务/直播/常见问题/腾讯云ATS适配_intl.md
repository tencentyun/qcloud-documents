
Apple Inc. announced in WWDC 2016 that by default all new Apps submitted as of January 1, 2017 will not be allowed to use `NSAllowsArbitraryLoads=YES` to bypass ATS restriction. Tencent Cloud will officially support HTTPS as of December 12th. By then, you just need to use the new SDK version (API remains the same) and change the video URLs' prefix from `http://` to `https://`. The new SDK can be automatically adapted to the change.



Please note that compared with HTTP, HTTPS brings a higher security, which is not absolutely necessary for videos, while leading to a reduced connection speed and a higher CPU utilization. If your App still needs to use HTTP under Apple's new policy, you need to modify Info.plist by adding `myqcloud.com` to `NSExceptionDomains`, as shown below.  

![myqcloud](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/myqcloud.png)

Disabling ATS for specific domain names can be approved by Apple's audit team, but you may need to specify that `myqcloud.com` is a domain name for video playback.

