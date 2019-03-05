
苹果在WWDC 2016中表示，从2017年1月1日起，所有新提交的app默认不能使用`NSAllowsArbitraryLoads=YES`来绕过ATS的限制。腾讯云将于12月12日正式支持HTTPS，届时您只需要使用新版SDK（接口无变化），并且将原来的视频地址的前缀从http://换成https:// 即可，SDK内部会自动适配。



但需要提醒的是，https相比于http，在引入更多安全性（视频方面并不是特别需要）的同时也牺牲了连接速度和CPU使用率。所以如果您APP在新的上架政策下，还要需要继续使用HTTP，方法修改Info.plist，将`myqcloud.com`加入到`NSExceptionDomains`中。具体的修改如图所示:  

![myqcloud](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/myqcloud.png)

针对特定域名禁用ATS是可以被苹果审核所接受的，您可能需要在审核时进行说明，`myqcloud.com`是用于视频播放的域名。
