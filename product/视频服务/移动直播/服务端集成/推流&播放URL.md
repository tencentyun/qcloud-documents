## 快速获得URL
如果您是想要生成一组URL用于测试，那您只需要打开[直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage)，点击 **生成推流地址** 按钮，即可生成一个推流URL和三种不同播放协议的播放URL。
![](https://mc.qcloudimg.com/static/img/cc7c9364fab232a94025b4ee1a2ac3d8/image.png)

使用我们的 Demo [视频云工具包](https://cloud.tencent.com/document/product/454/6555#DE) 中的 **RTMP 推流** 和 **直播播放器** 功能，可以快速测试推流 URL 和播放 URL 的有效性。


## 后台派发URL

从设计灵活性的角度来讲，后台直接派发 URL 要比把 URL 写死在 APP 里要好得多。相应的，如果您的直播产品是主播可以自由开播的，那么像上面这样手动生成 URL 地址也无法满足需求。

这时，就需要您的后台自动派发 URL 了，文档 [DOC](https://cloud.tencent.com/document/product/454/9875) 中介绍了腾讯云推流和播放 URL 的组成，以及如何让您的后台业务服务器自己生成 URL。

## 为什么推不上去？

- 过期时间不要太短，超过过期时间的 URL 即视为无效。
![](https://mc.qcloudimg.com/static/img/da82219b2d8068dc1aa1fe1d00abb6a3/image.png)
- 一个推流 URL 不可以有两个人同时推流，否则会相互影响。