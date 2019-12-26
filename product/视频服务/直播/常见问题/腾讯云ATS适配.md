
苹果在 WWDC 2016 中表示，从2017年01月01日起，所有新提交的 App 默认不能使用 `NSAllowsArbitraryLoads=YES` 来绕过 ATS 的限制。腾讯云已正式支持 HTTPS，您只需要使用新版 SDK（接口无变化），并且将原来的视频地址的前缀从 `http://` 换成 `https://` 即可，SDK 内部会自动适配。

但需要提醒的是，HTTPS 相比于 HTTP，在引入更多安全性（视频方面并不是特别需要）的同时也牺牲了连接速度和 CPU 使用率。所以如果您 App 在新的上架政策下，还需要继续使用 HTTP，方法是修改 Info.plist，将`myqcloud.com`加入到`NSExceptionDomains`中。具体的修改如图所示：  

![](https://main.qcloudimg.com/raw/9cd1a8754cb0b2e7d2d407fec1f82db1.png)

针对特定域名禁用 ATS 是可以被苹果审核所接受的，您可能需要在审核时进行说明，`myqcloud.com` 是用于视频播放的域名。
